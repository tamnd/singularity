"""Numerical checks for the CA family K = F_p(x1, x2, s(x1), s(x2)),
nu(x1) = 1, nu(x2) = sqrt(2), s(x) = sum_n x^(n!).
Series live in F_p((x1, x2)) with exponents in Z^2, value a + b*sqrt(2)."""
import math, random, sys
from fractions import Fraction as Fr
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hahn import Ring

W = (1.0, math.sqrt(2))
BOUND = 26.0

def setup(p):
    R = Ring(p, W, BOUND)
    fact = [1, 2, 6, 24]
    x1 = R.mono((1, 0)); x2 = R.mono((0, 1))
    x3 = R.clean({(Fr(n), Fr(0)): 1 for n in fact})
    x4 = R.clean({(Fr(0), Fr(n)): 1 for n in fact})
    return R, [x1, x2, x3, x4]

def evalpoly(R, h, X):
    tot = {}
    for e, c in h.items():
        m = R.mono((0, 0), c)
        for xi, k in zip(X, e):
            m = R.mul(m, R.power(xi, k))
        tot = R.add(tot, m)
    return tot

def truncate(R, s, gamma):
    """Laurent truncation P with nu(s - P) > gamma, and the leading monomial of s - P."""
    P = {e: c for e, c in s.items() if R.val_mono(e) <= gamma}
    rest = {e: c for e, c in s.items() if R.val_mono(e) > gamma}
    return P, (R.lead(rest) if rest else None)

def perron_steps(vectors):
    """Euclid/Perron algorithm: enlarge the unimodular cone cone(r1, r2), starting
    from the standard basis, until it contains all given vectors (all of positive
    value).  Each step replaces the generator of larger value by the difference."""
    r1, r2 = (1, 0), (0, 1)
    val = lambda r: r[0] * W[0] + r[1] * W[1]
    def inside(a):
        det = r1[0] * r2[1] - r1[1] * r2[0]
        al = (a[0] * r2[1] - a[1] * r2[0]) / det
        be = (r1[0] * a[1] - r1[1] * a[0]) / det
        return al >= 0 and be >= 0
    steps = 0
    while not all(inside(a) for a in vectors):
        if val(r1) < val(r2):
            r2 = (r2[0] - r1[0], r2[1] - r1[1])
        else:
            r1 = (r1[0] - r2[0], r1[1] - r2[1])
        steps += 1
        assert steps < 200
    return steps, r1, r2, val(r1), val(r2)

def test_monomialization(p, trials=40, seed=1):
    random.seed(seed)
    R, X = setup(p)
    ok = 0
    for _ in range(trials):
        h = {}
        for _ in range(random.randint(2, 5)):
            e = tuple(random.randint(0, 2) for _ in range(4))
            h[e] = random.randint(1, p - 1)
        H = evalpoly(R, h, X)
        if not H:
            continue
        gamma = R.val(H)
        if gamma > BOUND / 2:
            continue
        P3, L3 = truncate(R, X[2], gamma)
        P4, L4 = truncate(R, X[3], gamma)
        H0 = evalpoly(R, h, [X[0], X[1], P3, P4])
        (e0, c0), (e1, c1) = R.lead(H), R.lead(H0)
        assert e0 == e1 and c0 == c1, (h, e0, e1)
        # vectors that must become nonnegative after the Perron transform
        vecs = [tuple(int(a) for a in e) for e in list(P3) + list(P4)]
        vecs += [tuple(int(a - b) for a, b in zip(e, e0)) for e in H0 if e != e0]
        vecs += [tuple(int(a - b) for a, b in zip(L[0], e0)) for L in (L3, L4)]
        vecs += [tuple(int(a) for a in e0)]
        vecs = [v for v in vecs if any(v)]
        steps, r1, r2, v1, v2 = perron_steps(vecs)
        ok += 1
        print(f"p={p} h={h} nu(h)={gamma:.4f} M0=x^{tuple(int(a) for a in e0)} perron_steps={steps} new values=({v1:.4f},{v2:.4f})")
    print(f"p={p}: {ok} polynomials, leading term of h equals that of h0 in all cases")

def test_newton(p):
    """f(X) = X^p - x1^2 X - x1^3 x3; root theta in S near -x1 x3 (p >= 3)."""
    R, X = setup(p)
    x1, x2, x3, x4 = X
    a = R.mul(R.power(x1, 3), x3)
    th = R.scal(-1, R.mul(x1, x3))
    inv_x1sq = R.mono((-2, 0))
    for _ in range(12):
        th = R.mul(R.sub(R.power(th, p), a), inv_x1sq)
    f = lambda y: R.sub(R.sub(R.power(y, p), R.mul(R.power(x1, 2), y)), a)
    print(f"p={p}: nu(f(theta)) >= {R.val(f(th)):.3f} (truncation bound {BOUND})")
    gam1 = 2.0  # nu(f'(theta)) = nu(-x1^2) since p*theta^(p-1) = 0
    c, L = truncate(R, th, 2.5)
    g0 = f(c)
    g1 = R.sub(R.scal(p, R.power(c, p - 1)), R.power(x1, 2))
    print(f"   truncation c has {len(c)} terms, nu(theta-c)={R.val(R.sub(th, c)):.4f}, nu(g0)={R.val(g0):.4f}, nu(g1)={R.val(g1):.4f}, Newton condition nu(g0) > 2 nu(g1): {R.val(g0) > 2 * R.val(g1)}")

if __name__ == '__main__':
    for p in (2, 3):
        test_monomialization(p, trials=12)
    for p in (3, 5):
        test_newton(p)
