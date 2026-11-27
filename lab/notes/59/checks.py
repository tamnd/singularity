"""Referee checks for note 57 (independent code, nothing imported from the scripts of note 57)."""
import math
from fractions import Fraction as Fr
R2 = math.sqrt(2)
def val(e): return float(e[0]) + float(e[1]) * R2
class S:
    """truncated series over F_p in x1,x2 (exponents in Q^2), weights (1, sqrt2)"""
    def __init__(s, p, B): s.p, s.B = p, B
    def cl(s, d): return {e: c % s.p for e, c in d.items() if c % s.p and val(e) <= s.B + 1e-9}
    def add(s, a, b, k=1):
        r = dict(a)
        for e, c in b.items(): r[e] = r.get(e, 0) + k * c
        return s.cl(r)
    def mul(s, a, b):
        r = {}
        for e1, c1 in a.items():
            for e2, c2 in b.items():
                e = (e1[0] + e2[0], e1[1] + e2[1])
                if val(e) <= s.B + 1e-9: r[e] = r.get(e, 0) + c1 * c2
        return s.cl(r)
    def pw(s, a, n):
        r = {(Fr(0), Fr(0)): 1}
        for _ in range(n): r = s.mul(r, a)
        return r
    def v(s, a): return min((val(e) for e in a), default=math.inf)
    def lead(s, a): return min(a, key=val)

def ex311(p, B=30):
    A = S(p, B)
    fac = [1, 2, 6, 24]
    x1 = {(Fr(1), Fr(0)): 1}
    x3 = {(Fr(n), Fr(0)): 1 for n in fac}
    a = A.mul(A.pw(x1, 3), x3)
    inv = {(Fr(-2), Fr(0)): 1}
    c = A.add({}, A.mul(x1, x3), -1)          # c = -x1 x3, an element of K
    th = dict(c)
    for _ in range(15): th = A.mul(A.add(A.pw(th, p), a, -1), inv)
    f = lambda y: A.add(A.add(A.pw(y, p), A.mul(A.pw(x1, 2), y), -1), a, -1)
    print(f"Ex 3.11, p={p}: nu(f(theta)) >= {A.v(f(th)):.1f}; nu(theta)={A.v(th):.3f}; "
          f"nu(theta - (-x1 x3)) = {A.v(A.add(th, c, -1)):.3f} (expected 2p-2 = {2*p-2})")
    trunc = {e: cc for e, cc in th.items() if val(e) <= 2.5}
    print(f"   value truncation of theta below 2.5 = {trunc}; nu(theta - trunc) = {A.v(A.add(th, trunc, -1)):.3f}")
    # rationality: x3 = (theta^p - x1^2 theta)/x1^3 recovers x3
    rec = A.mul(A.add(A.pw(th, p), A.mul(A.pw(x1, 2), th), -1), {(Fr(-3), Fr(0)): 1})
    print(f"   x3 - (theta^p - x1^2 theta)/x1^3 has value >= {A.v(A.add(rec, x3, -1)):.1f} (so F = k(x1,x2,theta,x4) is rational)")

def prop41b(p, B=10):
    """root of X^p - z^(p-1) X - s^p, v(t)=1, v(z)=sqrt2, s = t + t^2 + t^6 + ..., iterate X = s + (z^(p-1)X)^(1/p)"""
    A = S(p, B)
    s = {(Fr(n), Fr(0)): 1 for n in (1, 2, 6)}
    X = dict(s)
    for _ in range(10):
        Y = A.mul({(Fr(0), Fr(p - 1)): 1}, X)
        X = A.add(s, A.cl({(e[0] / p, e[1] / p): cc for e, cc in Y.items()}))
    e = A.lead(A.add(X, s, -1))
    print(f"Prop 4.1(b), p={p}: leading exponent of theta0 - s = ({e[0]},{e[1]}), value {val(e):.5f}, "
          f"formula ((p-1)sqrt2+1)/p = {((p-1)*R2+1)/p:.5f}")
    s2 = {(Fr(n), Fr(0)): 1 for n in (2, 3, 6)}   # ord s = 2 > sqrt 2
    print(f"   if ord_t s = 2 the formula assumption v(theta0) = v(s) fails: 2 > sqrt2, Newton polygon of X^p - z^(p-1)X - s^p has slopes "
          f"{R2:.4f} (p-1 roots) and {2*p-(p-1)*R2:.4f} (one root)")

def eg(p):
    Om = Fr(p**4, p**4 - 1)
    vals = [Fr(1)] + [sum(Fr(p)**(4*j - 2*i) for j in range(i)) for i in range(1, 6)]
    # check recursion consistency: nu(P_{i+1}) > p^2 nu(P_i) = nu(u^{p^{2i-2}}) + nu(P_{i-1}) for i>=2, and nu(v^{p^2}) = nu(u)
    ok = vals[1] * p**2 == vals[0] and all(p**2 * vals[i] == p**(2*i - 2) * vals[0] + vals[i - 1] and vals[i + 1] > p**2 * vals[i] for i in range(2, 5))
    print(f"EG p={p}: nu(P_0..P_5) = {[str(x) for x in vals]}; binomial balance of recursion holds: {ok}; "
          f"bound (Omega-2)/p = {Om/p - Fr(2,p)} < -1/p^2: {Om/p - Fr(2,p) < Fr(-1,p*p)}")
    print(f"   formula sum_(j<i) p^(4j-2i) at i=0 gives 0, so nu(P_0)=1 must be stated separately")

def perron(w=(1.0, R2), steps=12):
    r1, r2 = (1, 0), (0, 1)
    v = lambda r: r[0]*w[0] + r[1]*w[1]
    out = []
    for _ in range(steps):
        if v(r1) > v(r2): r1 = (r1[0]-r2[0], r1[1]-r2[1])
        else: r2 = (r2[0]-r1[0], r2[1]-r1[1])
        assert abs(r1[0]*r2[1]-r1[1]*r2[0]) == 1 and v(r1) > 0 and v(r2) > 0
        out.append((r1, r2, round(v(r1), 5), round(v(r2), 5)))
    print("Perron on (1,sqrt2):", out[:6], "...", out[-1])

def transc(p, d=4, m=6, N=200):
    """s = sum X^{n!} over F_p: check that 1, s, ..., s^d with polynomial coefficients of degree <= m are
    F_p-linearly independent modulo X^N (rank of the coefficient matrix)."""
    fac, n, f = [], 1, 1
    while f < N: fac.append(f); n += 1; f *= n
    s = [0]*N
    for e in fac: s[e] = (s[e] + 1) % p
    def mul(a, b):
        r = [0]*N
        for i, x in enumerate(a):
            if x:
                for j in range(N - i):
                    if b[j]: r[i+j] = (r[i+j] + x*b[j]) % p
        return r
    pows = [[1] + [0]*(N-1)]
    for _ in range(d): pows.append(mul(pows[-1], s))
    rows = []
    for k in range(d+1):
        for j in range(m+1):
            rows.append([0]*j + pows[k][:N-j])
    # rank over F_p
    M = [r[:] for r in rows]; rank = 0; col = 0
    while rank < len(M) and col < N:
        piv = next((i for i in range(rank, len(M)) if M[i][col]), None)
        if piv is None: col += 1; continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], p-2, p)
        M[rank] = [x*inv % p for x in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][col]:
                c = M[i][col]; M[i] = [(x - c*y) % p for x, y in zip(M[i], M[rank])]
        rank += 1; col += 1
    print(f"transcendence test p={p}: {len(rows)} products X^j s^k (j<={m}, k<={d}) have rank {rank} mod X^{N}")

if __name__ == '__main__':
    for p in (3, 5): ex311(p)
    for p in (2, 3): prop41b(p)
    for p in (2, 3, 5): eg(p)
    perron()
    for p in (2, 3): transc(p)
