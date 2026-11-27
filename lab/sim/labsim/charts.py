"""Cleaning, point charts and coordinate charts for f = z^q + F.

The setting is section 2 of Hauser and Perlega, arXiv:1802.05010, and note 03. The field is perfect, so each monomial c x^(q a) is the q-th power (c^(1/q) x^a)^q.
"""

from dataclasses import dataclass, field as dc_field

from .poly import Poly, binomial_terms


def is_power_of(q, p):
    while q > 1 and q % p == 0:
        q //= p
    return q == 1


def clean(F, q):
    """Remove the monomials with all exponents divisible by q.

    The result is (G, h) with F = G - h^q, so the change z -> z + h takes z^q + F to z^q + G. A constant term is a q-th power too, so it goes into h.
    """
    R, K = F.ring, F.ring.F
    if not is_power_of(q, K.p):
        raise ValueError(f"q = {q} is not a power of p = {K.p}")
    kept, h = {}, {}
    for e, c in F.terms.items():
        if all(a % q == 0 for a in e):
            h[tuple(a // q for a in e)] = K.root(K.neg(c), q)
        else:
            kept[e] = c
    return Poly(R, kept), Poly(R, h)


def is_clean(F, q):
    return all(not all(a % q == 0 for a in e) for e in F.terms)


def new_divisor(E, j, t, S):
    """The divisor after the x_j-chart of the blowup with centre V(x_i, i in S): the exceptional divisor V(x_j), and the old components that stay through the point."""
    return frozenset({j} | {i for i in E if i != j and (i not in S or not t.get(i, 0))})


class ChartError(ValueError):
    """The centre is not permissible: the order of F along it is less than q."""


def chart_map(F, q, j, t=None, S=None, strip_units=False):
    """The transform x_j^(-q) F(...) in the x_j-chart of the blowup with centre V(x_i, i in S).

    S is a set of indices with j in S. S = None is the point centre. The chart maps x_i to x_j (x_i + t_i) for i in S other than j and keeps the other variables. t is a dict from indices to field elements, with support in S minus j. The result is not cleaned.

    With strip_units, the map divides by the q-th power unit (x_i + t_i)^s for each translated i, where s is the largest multiple of q with x_i^s dividing F. This keeps the clean part up to a unit and keeps r, d and rho.
    """
    R, K = F.ring, F.ring.F
    n = R.n
    S = frozenset(range(n)) if S is None else frozenset(S)
    t = {i: c for i, c in (t or {}).items() if c}
    if j not in S:
        raise ValueError("the chart variable must be in the centre")
    if any(i not in S or i == j for i in t):
        raise ValueError("a translation must be in the centre and not in the chart variable")
    if not F.terms:
        return Poly(R, {})
    if F.order_along(S) < q:
        raise ChartError(f"the order along the centre is {F.order_along(S)} < q = {q}")
    strip = {}
    if strip_units:
        for i in t:
            m = min(e[i] for e in F.terms)
            strip[i] = q * (m // q)
    out = {}
    for e, c in F.terms.items():
        base = list(e)
        base[j] = sum(e[i] for i in S) - q
        parts = [(base, c)]
        for i, ti in t.items():
            a = e[i] - strip.get(i, 0)
            nxt = []
            for b, cc in parts:
                for s, cs in binomial_terms(K, a, ti):
                    b2 = list(b)
                    b2[i] = s
                    nxt.append((b2, K.mul(cc, cs)))
            parts = nxt
        for b, cc in parts:
            key = tuple(b)
            v = K.add(out.get(key, 0), cc)
            if v:
                out[key] = v
            else:
                out.pop(key, None)
    return Poly(R, out)


@dataclass
class Step:
    """One chart step: the input, the chart, and the cleaned result."""

    j: int
    t: dict
    centre: frozenset
    raw: Poly
    F: Poly
    h: Poly
    E: frozenset
    multiplicity_kept: bool


@dataclass
class Point:
    """A point of a resolution run: f = z^q + F with the divisor E (a set of indices)."""

    F: Poly
    q: int
    E: frozenset = dc_field(default_factory=frozenset)

    def __post_init__(self):
        self.E = self.F.ring.indices(self.E)

    @property
    def ring(self):
        return self.F.ring

    def cleaned(self):
        G, _ = clean(self.F, self.q)
        return Point(G, self.q, self.E)

    def _args(self, j, t):
        R = self.ring
        j = R.index(j)
        t = {R.index(v): c for v, c in (t or {}).items()}
        return j, t

    def chart(self, j, t=None, centre=None, strip_units=False):
        """The x_j-chart with the translations t. centre = None is the point centre. Otherwise centre is the set of variables of C = V(x_i, i in centre)."""
        R = self.ring
        j, t = self._args(j, t)
        S = frozenset(range(R.n)) if centre is None else R.indices(centre)
        raw = chart_map(self.F, self.q, j, t, S, strip_units)
        G, h = clean(raw, self.q)
        E2 = new_divisor(self.E, j, t, S)
        kept = bool(G.terms) and G.order() >= self.q
        return Step(j, {i: c for i, c in t.items() if c}, S, raw, G, h, E2, kept)

    def blowup(self, j, t=None, centre=None, strip_units=False):
        """The next point. Raises ChartError if the centre is not permissible."""
        s = self.chart(j, t, centre, strip_units)
        return Point(s.F, self.q, s.E)
