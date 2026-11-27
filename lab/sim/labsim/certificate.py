"""Certificates of chart sequences, in the format of target (e.1) of note 11.

A certificate is a JSON object:

    {"p": 2, "k": 1, "q": 8, "vars": ["x", ...], "F": "...", "divisor": ["x", ...],
     "steps": [{"chart": "point", "j": "x", "t": {"y": 1}, "h": "x*w", "F": "...",
                "divisor": ["x", "w"], "d": 6, "witness": [..]}, ...]}

A coordinate step has "chart": "coordinate" and "centre", the list of the variables of the centre. "t" maps a variable to the code of a field element. "h" is the cleaning: the step takes z to z + h. "witness" is the exponent of a term of the residual factor G of degree d. The checker computes each step again and compares each field.
"""

import json

from .charts import ChartError, Point
from .invariants import residual
from .poly import Ring


def _names(R, idx):
    return [R.names[i] for i in sorted(idx)]


def _witness(G, d):
    return list(min(e for e in G.terms if sum(e) == d))


def make(point, steps):
    """The certificate of the steps from the point. A step is (j, t) or (j, t, centre)."""
    R = point.ring
    cert = {"p": R.F.p, "k": R.F.k, "q": point.q, "vars": list(R.names), "F": str(point.F), "divisor": _names(R, point.E), "steps": []}
    P = point
    for st in steps:
        j, t = st[0], st[1]
        centre = st[2] if len(st) > 2 else None
        s = P.chart(j, t, centre)
        P = Point(s.F, P.q, s.E)
        res = residual(P.F, P.E)
        entry = {"chart": "point" if centre is None else "coordinate"}
        if centre is not None:
            entry["centre"] = _names(R, R.indices(centre))
        entry.update({
            "j": R.names[s.j],
            "t": {R.names[i]: c for i, c in sorted(s.t.items())},
            "h": str(s.h),
            "F": str(P.F),
            "divisor": _names(R, P.E),
            "d": res.d,
            "witness": _witness(res.G, res.d),
        })
        cert["steps"].append(entry)
    return cert


def check(cert):
    """Compute the certificate again. The result is a list of faults, empty when the certificate is correct."""
    faults = []
    R = Ring.over(cert["p"], cert["vars"], cert.get("k", 1))
    q = cert["q"]
    P = Point(R.parse(cert["F"]), q, cert["divisor"])
    for n, st in enumerate(cert["steps"], 1):
        centre = st.get("centre") if st.get("chart") == "coordinate" else None
        try:
            s = P.chart(st["j"], st.get("t", {}), centre)
        except (ChartError, ValueError) as err:
            faults.append(f"step {n}: {err}")
            return faults
        if s.h != R.parse(st.get("h", "0")):
            faults.append(f"step {n}: the cleaning is {s.h}, not {st.get('h')}")
        if s.F != R.parse(st["F"]):
            faults.append(f"step {n}: F' is {s.F}")
        if s.E != R.indices(st["divisor"]):
            faults.append(f"step {n}: the divisor is {_names(R, s.E)}")
        if not s.multiplicity_kept:
            faults.append(f"step {n}: the multiplicity drops")
        res = residual(s.F, s.E)
        if res.d != st["d"]:
            faults.append(f"step {n}: the residual order is {res.d}, not {st['d']}")
        wit = tuple(st["witness"])
        if wit not in res.G.terms or sum(wit) != st["d"]:
            faults.append(f"step {n}: the witness is not a term of G of degree d")
        P = Point(s.F, q, s.E)
    return faults


def dumps(cert):
    return json.dumps(cert, indent=1, sort_keys=False)


def loads(text):
    return json.loads(text)
