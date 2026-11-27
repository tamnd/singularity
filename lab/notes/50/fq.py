# Exact arithmetic over F_q, q = p^k, and the step map in four variables (x, w, y, z).
# Polynomials: dict {(i, l, j, k): c} meaning c x^i w^l y^j z^k, c an int code of F_q.
import itertools, random
from math import comb

IRR = {(3,2):[1,0,1], (5,2):[2,0,1], (7,2):[3,0,1], (3,3):[1,2,0,1], (2,2):[1,1,1]}  # monic irreducibles, low to high

class GF:
    def __init__(s, p, k=1):
        s.p, s.k, s.q = p, k, p**k
        q = s.q
        def vec(n): return [(n // p**t) % p for t in range(k)]
        def code(v): return sum(c * p**t for t, c in enumerate(v))
        s.add = [[code([(a+b) % p for a, b in zip(vec(x), vec(y))]) for y in range(q)] for x in range(q)]
        s.neg = [code([(-a) % p for a in vec(x)]) for x in range(q)]
        if k == 1:
            s.mul = [[(x*y) % p for y in range(q)] for x in range(q)]
        else:
            f = IRR[(p, k)]
            def mulv(u, v):
                r = [0]*(2*k-1)
                for i, a in enumerate(u):
                    for j, b in enumerate(v):
                        r[i+j] = (r[i+j] + a*b) % p
                for t in range(2*k-2, k-1, -1):
                    c = r[t]
                    if c:
                        for u2 in range(k+1):
                            r[t-k+u2] = (r[t-k+u2] - c*f[u2]) % p
                return r[:k]
            s.mul = [[code(mulv(vec(x), vec(y))) for y in range(q)] for x in range(q)]
        s.inv = [0]*q
        for x in range(1, q):
            for y in range(1, q):
                if s.mul[x][y] == 1: s.inv[x] = y
    def pw(s, a, n):
        r = 1
        for _ in range(n): r = s.mul[r][a]
        return r
    def intc(s, n):  # integer n as an element of the prime field
        return n % s.p

def padd(F, P, mono, c):
    if c == 0: return
    o = P.get(mono, 0)
    n = F.add[o][c]
    if n: P[mono] = n
    else: P.pop(mono, None)

def clean(F, g):
    p = F.p
    return {m: c for m, c in g.items() if any(e % p for e in m)}

def expand_shift(F, i, a):
    """(X + a)^i as list of (t, coeff) for X^t."""
    out = []
    for t in range(i+1):
        b = comb(i, t) % F.p
        if b == 0: continue
        c = F.mul[b][F.pw(a, i-t)] if (i-t) > 0 else b
        if c: out.append((t, c))
    return out

def step(F, g, chart, a, b, check=True):
    """One step: chart 'y' or 'z', translation (a, b). Returns cleaned L^{-p} pi(g), or None if ord g < p."""
    p = F.p
    out = {}
    cache = {}
    for (i, l, j, k), c in g.items():
        e = i + l + j + k - p
        if e < 0:
            return None
        if (i, a) not in cache: cache[(i, a)] = expand_shift(F, i, a)
        if (l, b) not in cache: cache[(l, b)] = expand_shift(F, l, b)
        for t, c1 in cache[(i, a)]:
            cc = F.mul[c][c1]
            for s_, c2 in cache[(l, b)]:
                c3 = F.mul[cc][c2]
                if chart == 'y':
                    padd(F, out, (t, s_, e, k), c3)
                else:
                    padd(F, out, (t, s_, j, e), c3)
    return clean(F, out)

def ordg(g):
    return min(sum(m) for m in g) if g else 10**9

def data(F, g):
    """Return (ry, rz, d, rho)."""
    p = F.p
    ry = min(m[2] for m in g); rz = min(m[3] for m in g)
    d = 10**9; rho = 10**9
    for (i, l, j, k) in g:
        deg = i + l + (j - ry) + (k - rz)
        d = min(d, deg)
        if i % p or l % p: rho = min(rho, deg - 1)
        if j % p or k % p: rho = min(rho, deg)
    return ry, rz, d, rho

def initial(F, g):
    ry, rz, d, rho = data(F, g)
    return {(i, l, j-ry, k-rz): c for (i, l, j, k), c in g.items() if i + l + (j-ry) + (k-rz) == d}

def binary(h):
    return all(m[2] == 0 and m[3] == 0 for m in h)

def nu_curve(g, which):
    """nu^G along V(x, w, y) (which='y') or V(x, w, z) (which='z') at the origin chart."""
    ry = min(m[2] for m in g); rz = min(m[3] for m in g)
    if which == 'y':
        return min(i + l + (j - ry) for (i, l, j, k) in g)
    return min(i + l + (k - rz) for (i, l, j, k) in g)

def nu_surf(g, which):
    ry = min(m[2] for m in g); rz = min(m[3] for m in g)
    if which == 'y':
        return min(i + (j - ry) for (i, l, j, k) in g)
    return min(i + (k - rz) for (i, l, j, k) in g)

def lin_change(F, g, M):
    """Substitute x -> M[0][0] x + M[0][1] w, w -> M[1][0] x + M[1][1] w."""
    out = {}
    for (i, l, j, k), c in g.items():
        # (m00 x + m01 w)^i (m10 x + m11 w)^l
        A = {(0, 0): c}
        for (u, v), n in (((M[0][0], M[0][1]), i), ((M[1][0], M[1][1]), l)):
            for _ in range(n):
                B = {}
                for (s, t), cc in A.items():
                    padd(F, B, (s+1, t), F.mul[cc][u]); padd(F, B, (s, t+1), F.mul[cc][v])
                A = B
        for (s, t), cc in A.items():
            padd(F, out, (s, t, j, k), cc)
    return clean(F, out)

def degxw(g):
    return max(m[0] + m[1] for m in g)

def show(F, g, lim=12):
    items = sorted(g.items(), key=lambda t: (sum(t[0]), t[0]))[:lim]
    return ' + '.join(f"{c}*x^{i}w^{l}y^{j}z^{k}" for (i, l, j, k), c in items) + (' ...' if len(g) > lim else '')
