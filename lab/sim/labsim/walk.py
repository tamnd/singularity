"""Random walks of point blowups, with a fixed seed.

A walk starts at a random clean F with a random divisor. At each step it takes a random chart and a random translation over the field, cleans, and records the invariants before and after. It stops when the multiplicity drops, when d = 0, when F has more than max_terms terms, or at the given depth. The walks divide by the q-th power units of the translated coordinates (strip_units in charts.py), as the walks of the Go engine do. This keeps r, d and rho and keeps the polynomials small.
"""

import random
from dataclasses import dataclass, field

from .charts import ChartError, Point, clean
from .invariants import invariants


def random_polynomial(ring, q, rng, terms=(1, 4), extra=6):
    """A random clean polynomial with order at least q: a few monomials of degree q to q + extra."""
    K = ring.F
    n = ring.n
    out = ring.zero()
    for _ in range(rng.randint(*terms)):
        total = rng.randint(q, q + extra)
        cuts = sorted(rng.randint(0, total) for _ in range(n - 1))
        exps = [b - a for a, b in zip([0] + cuts, cuts + [total])]
        out = out + ring.monomial(exps, rng.choice(list(K.nonzero())))
    return clean(out, q)[0]


@dataclass
class StepRecord:
    j: int
    t: dict
    before: object
    after: object

    @property
    def kangaroo(self):
        """The residual order goes up."""
        return self.after.d > self.before.d


@dataclass
class Walk:
    start: Point
    steps: list = field(default_factory=list)
    stop: str = "depth"


def walk(point, depth, rng, translate=0.5, max_terms=400):
    """A random walk of point blowups from the point. translate is the probability that a coordinate other than x_j is translated."""
    R, K = point.ring, point.ring.F
    w = Walk(point)
    P = point.cleaned()
    for _ in range(depth):
        before = invariants(P.F, P.E)
        if not P.F or P.F.order() < P.q:
            w.stop = "multiplicity"
            return w
        if before.d == 0:
            w.stop = "d = 0"
            return w
        if len(P.F) > max_terms:
            w.stop = "size"
            return w
        j = rng.randrange(R.n)
        t = {i: rng.choice(list(K.nonzero())) for i in range(R.n) if i != j and rng.random() < translate}
        try:
            s = P.chart(j, t, strip_units=True)
        except ChartError:
            w.stop = "multiplicity"
            return w
        if not s.multiplicity_kept:
            w.stop = "multiplicity"
            return w
        P = Point(s.F, P.q, s.E)
        w.steps.append(StepRecord(j, s.t, before, invariants(P.F, P.E)))
    return w


@dataclass
class Summary:
    """Counts over a set of walks with q = p, for the statements of note 03."""

    walks: int = 0
    steps: int = 0
    kangaroo: int = 0
    rho_up: int = 0
    dichotomy_fail: int = 0
    moh_fail: int = 0
    switch_fail: int = 0
    stops: dict = field(default_factory=dict)


def survey(ring, walks, depth, seed, divisor_prob=0.6, translate=0.5):
    """Run random walks with q = p and count the failures of Theorem 3.7 (rho in {d - 1, d}), Theorem 3.12 (rho' <= rho), Corollary 3.13 (d' <= d + 1) and Corollary 3.14 (a kangaroo point has tau = 0 and tau' = 1)."""
    p = ring.F.p
    rng = random.Random(seed)
    out = Summary()
    for _ in range(walks):
        F = random_polynomial(ring, p, rng)
        if not F:
            continue
        E = frozenset(i for i in range(ring.n) if rng.random() < divisor_prob)
        w = walk(Point(F, p, E), depth, rng, translate)
        out.walks += 1
        out.stops[w.stop] = out.stops.get(w.stop, 0) + 1
        for s in w.steps:
            out.steps += 1
            a, b = s.before, s.after
            for iv in (a, b):
                if iv.d and (iv.rho is None or not iv.d - 1 <= iv.rho <= iv.d):
                    out.dichotomy_fail += 1
            if b.rho is not None and a.rho is not None and b.rho > a.rho:
                out.rho_up += 1
            if b.d > a.d + 1:
                out.moh_fail += 1
            if s.kangaroo:
                out.kangaroo += 1
                if not (a.tau == 0 and b.tau == 1 and a.rho == b.rho):
                    out.switch_fail += 1
    return out
