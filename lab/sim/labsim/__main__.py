"""The command line: python3 -m labsim step|walk|check ..."""

import argparse
import json
import sys

from . import certificate
from .charts import Point
from .invariants import invariants, nu_G
from .poly import Ring
from .walk import survey


def _pairs(text):
    out = {}
    for part in (text or "").split(","):
        if part.strip():
            k, v = part.split("=")
            out[k.strip()] = int(v)
    return out


def _list(text):
    return [v.strip() for v in (text or "").split(",") if v.strip()]


def _show(R, F, E):
    iv = invariants(F, E)
    print(f"F = {F}")
    print(f"divisor = {','.join(R.names[i] for i in sorted(E))}  terms = {iv.terms}  r = {iv.r}  d = {iv.d}  rho = {iv.rho}  tau = {iv.tau}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="labsim")
    sub = ap.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("step", help="apply charts and print the invariants")
    st.add_argument("-p", type=int, required=True)
    st.add_argument("-k", type=int, default=1)
    st.add_argument("-q", type=int)
    st.add_argument("-vars", required=True)
    st.add_argument("-f", required=True)
    st.add_argument("-divisor", default="")
    st.add_argument("-chart", action="append", default=[], help="a chart variable; repeat for a sequence")
    st.add_argument("-t", action="append", default=[], help="translations var=code,... for the chart at the same place")
    st.add_argument("-centre", default="", help="the variables of a coordinate centre, for each chart")
    st.add_argument("-nu", action="append", default=[], help="print nu^G along V(vars) at the end")
    wk = sub.add_parser("walk", help="random walks with q = p and the checks of note 03")
    wk.add_argument("-p", type=int, required=True)
    wk.add_argument("-n", type=int, default=3)
    wk.add_argument("-walks", type=int, default=200)
    wk.add_argument("-depth", type=int, default=8)
    wk.add_argument("-seed", type=int, default=1)
    ck = sub.add_parser("check", help="check a certificate in JSON")
    ck.add_argument("file")
    a = ap.parse_args(argv)

    if a.cmd == "step":
        R = Ring.over(a.p, _list(a.vars), a.k)
        P = Point(R.parse(a.f), a.q or a.p, _list(a.divisor)).cleaned()
        _show(R, P.F, P.E)
        centre = _list(a.centre) or None
        for n, j in enumerate(a.chart):
            t = _pairs(a.t[n]) if n < len(a.t) else {}
            s = P.chart(j, t, centre)
            print(f"-- {j}-chart t = {t}" + (f" centre = {centre}" if centre else "") + f"  h = {s.h}  multiplicity kept = {s.multiplicity_kept}")
            P = Point(s.F, P.q, s.E)
            _show(R, P.F, P.E)
        for S in a.nu:
            print(f"nu^G along V({S}) = {nu_G(P.F, P.E, _list(S))}")
        return 0
    if a.cmd == "walk":
        names = [f"x{i + 1}" for i in range(a.n)]
        print(survey(Ring.over(a.p, names), a.walks, a.depth, a.seed))
        return 0
    with open(a.file, encoding="utf-8") as fh:
        faults = certificate.check(json.load(fh))
    for f in faults:
        print(f)
    print("ok" if not faults else f"{len(faults)} faults")
    return 1 if faults else 0


if __name__ == "__main__":
    sys.exit(main())
