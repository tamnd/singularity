import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Independent library for note 53 (referee of note 51).
# Exact arithmetic over F_p in three base variables x0,x1,x2.
# f = z^m + sum a_i z^(m-i), represented by the list a[0..m] of base polynomials.
# A base polynomial is a dict {(e0,e1,e2): c} with c in 1..p-1.
from fractions import Fraction as Fr
from itertools import product
from math import comb, lcm
import random

class Ctx:
    def __init__(self, p):
        self.p = p
        self.m = 2 * p
        self.rigid = [i for i in range(1, self.m + 1) if i % p != 0]
        self.b = 1
        for i in self.rigid:
            self.b = lcm(self.b, i)
        self.B = 1
        for i in range(1, self.m + 1):
            self.B = lcm(self.B, i)

def clean(P, p):
    return {e: c % p for e, c in P.items() if c % p}

def add(P, Q, p):
    R = dict(P)
    for e, c in Q.items():
        R[e] = (R.get(e, 0) + c) % p
    return {e: c for e, c in R.items() if c}

def scal(P, s, p):
    s %= p
    if s == 0:
        return {}
    return {e: (c * s) % p for e, c in P.items()}

def mul(P, Q, p):
    R = {}
    for e, c in P.items():
        for f, d in Q.items():
            g = (e[0] + f[0], e[1] + f[1], e[2] + f[2])
            R[g] = (R.get(g, 0) + c * d) % p
    return {e: c for e, c in R.items() if c}

def pw(P, n, p):
    R = {(0, 0, 0): 1}
    B = P
    while n:
        if n & 1:
            R = mul(R, B, p)
        n >>= 1
        if n:
            B = mul(B, B, p)
    return R

INF = 10 ** 9

def ordp(P):
    return min((sum(e) for e in P), default=INF)

def ordS(P, S):
    return min((sum(e[k] for k in S) for e in P), default=INF)

def ordv(P, k):
    return min((e[k] for e in P), default=INF)

def homog(P, d):
    return {e: c for e, c in P.items() if sum(e) == d}

def mono(e, c=1):
    return {tuple(e): c}

def translate(a, c, ctx):
    """coefficients of f(z + c)."""
    p, m = ctx.p, ctx.m
    cp = [{(0, 0, 0): 1}]
    for _ in range(m):
        cp.append(mul(cp[-1], c, p))
    out = []
    for i in range(m + 1):
        s = {}
        for j in range(i + 1):
            bc = comb(m - j, i - j) % p
            if bc and a[j]:
                s = add(s, scal(mul(a[j], cp[i - j], p), bc, p), p)
        out.append(s)
    out[0] = {(0, 0, 0): 1}
    return out

def is_mult_m(a, ctx):
    return all(ordp(a[i]) >= i for i in range(1, ctx.m + 1))

def slopes(a, ctx):
    p, m = ctx.p, ctx.m
    D = min((Fr(ordp(a[i]), i) for i in (p, m) if a[i]), default=Fr(INF))
    s = min((Fr(ordp(a[i]), i) for i in ctx.rigid if a[i]), default=Fr(INF))
    return D, s, min(D, s)

def regime(a, ctx):
    D, s, d = slopes(a, ctx)
    if s == 1:
        return 'R2'
    if s > D:
        return 'R1'
    return 'R3'

def solvable_C(a, ctx):
    """If z is solvable, return the form C with H = (Y + C^p)^2; else None."""
    p, m = ctx.p, ctx.m
    D, s, d = slopes(a, ctx)
    if not (s > D) or D.denominator != 1:
        return None
    Dn = int(D)
    h1 = homog(a[p], p * Dn)
    h2 = homog(a[m], m * Dn)
    if not h1:
        return None
    if any(x % p for e in h1 for x in e):
        return None
    inv2 = pow(2, p - 2, p)
    C = {tuple(x // p for x in e): (c * inv2) % p for e, c in h1.items()}  # c^(1/p) = c on F_p
    if clean(pw(C, m, p), p) != h2:
        return None
    return C

def prepare(a, ctx, cap=40):
    n = 0
    while True:
        C = solvable_C(a, ctx)
        if C is None:
            return a, n
        a = translate(a, scal(C, -1, ctx.p), ctx)
        n += 1
        if n > cap:
            raise RuntimeError('preparation cap')

def tangent_cone(a, ctx):
    """dict over (e0,e1,e2,ez)."""
    m = ctx.m
    T = {(0, 0, 0, m): 1}
    for i in range(1, m + 1):
        if a[i] and ordp(a[i]) == i:
            for e, c in homog(a[i], i).items():
                T[e + (m - i,)] = c
    return T

def in_U(T, v, p):
    """T(Y + t v) == T(Y) in F_p[Y, t] (Taylor coefficients)."""
    acc = {}
    for g, c in T.items():
        ranges = [range(gi + 1) for gi in g]
        for be in product(*ranges):
            if not any(be):
                continue
            bc = 1
            for gi, bi in zip(g, be):
                bc = bc * comb(gi, bi) % p
                if not bc:
                    break
            if not bc:
                continue
            vb = 1
            for vi, bi in zip(v, be):
                if bi:
                    vb = vb * pow(vi, bi, p) % p
                    if not vb:
                        break
            if not vb:
                continue
            key = (tuple(gi - bi for gi, bi in zip(g, be)), sum(be))
            acc[key] = (acc.get(key, 0) + c * bc * vb) % p
    return all(x == 0 for x in acc.values())

def U_space(T, p):
    """All F_p-points of U(T) (a subspace)."""
    present = [any(g[i] for g in T) for i in range(4)]
    idx = [i for i in range(4) if present[i]]
    pts = []
    for w in product(range(p), repeat=len(idx)):
        v = [0, 0, 0, 0]
        for i, wi in zip(idx, w):
            v[i] = wi
        if in_U(T, v, p):
            pts.append(v)
    absent = [i for i in range(4) if not present[i]]
    full = []
    for v in pts:
        for w in product(range(p), repeat=len(absent)):
            u = list(v)
            for i, wi in zip(absent, w):
                u[i] = wi
            full.append(tuple(u))
    return full

def is_adapted(a, ctx):
    if solvable_C(a, ctx) is not None:
        return False
    U = U_space(tangent_cone(a, ctx), ctx.p)
    return all(v[3] == 0 for v in U)

def solve_l(U, p):
    """linear form l (3 coefficients) with l(v_X) = v_Z for all v in U."""
    for l in product(range(p), repeat=3):
        if all((l[0] * v[0] + l[1] * v[1] + l[2] * v[2] - v[3]) % p == 0 for v in U):
            return l
    raise RuntimeError('no l: projection not injective?')

def adapt(a, ctx):
    a, n = prepare(a, ctx)
    D, s, d = slopes(a, ctx)
    lin = 0
    if d == 1:
        U = U_space(tangent_cone(a, ctx), ctx.p)
        if any(v[3] for v in U):
            l = solve_l(U, ctx.p)
            L = {}
            for k in range(3):
                if l[k]:
                    e = [0, 0, 0]; e[k] = 1
                    L[tuple(e)] = l[k]
            a = translate(a, L, ctx)
            lin = 1
            a, n2 = prepare(a, ctx)
            n += n2
    return a, n, lin

def blowup(a, S, j, lam, nu, ctx):
    """chart x_j of the blowup of V(z, x_S); point x_k' = lam[k] (k in S, k != j), z' = nu.
    Returns coefficients centred at the point (u_k = x_k' - lam_k)."""
    p, m = ctx.p, ctx.m
    out = [{(0, 0, 0): 1}]
    # substitution x_k -> x_j (x_k + lam_k)
    cache = {}
    def sub_var(k, e):
        key = (k, e)
        if key not in cache:
            base = {(0, 0, 0): 1}
            if e:
                lin = mono([1 if t == j else 0 for t in range(3)])
                q = {}
                ek = [0, 0, 0]; ek[k] = 1; ek[j] += 1
                q[tuple(ek)] = 1
                if lam[k] % p:
                    ej = [0, 0, 0]; ej[j] = 1
                    q[tuple(ej)] = (q.get(tuple(ej), 0) + lam[k]) % p
                base = pw(q, e, p)
            cache[key] = base
        return cache[key]
    for i in range(1, m + 1):
        s = {}
        for e, c in a[i].items():
            term = mono([e[t] if (t not in S or t == j) else 0 for t in range(3)], c)
            for k in S:
                if k != j and e[k]:
                    term = mul(term, sub_var(k, e[k]), p)
            s = add(s, term, p)
        # divide by x_j^i
        d = {}
        for e, c in s.items():
            assert e[j] >= i, 'not permissible'
            ee = list(e); ee[j] -= i
            d[tuple(ee)] = c
        out.append(d)
    if nu % p:
        out = translate(out, {(0, 0, 0): nu % p}, ctx)
    return out

def permissible(a, S, ctx):
    return all(ordS(a[i], S) >= i for i in range(1, ctx.m + 1))

def new_E(E, S, j, lam):
    return frozenset({j} | (set(E) - set(S)) | {k for k in set(E) & set(S) if k != j and lam[k] == 0})

def points_over(a, S, ctx, allnu=True):
    """All F_p-rational points of multiplicity m over the origin, all charts."""
    p = ctx.p
    res = []
    for j in S:
        others = [k for k in S if k != j]
        for lv in product(range(p), repeat=len(others)):
            lam = {k: lv[t] for t, k in enumerate(others)}
            for nu in (range(p) if allnu else [0]):
                b = blowup(a, S, j, lam, nu, ctx)
                if is_mult_m(b, ctx):
                    res.append((j, lam, nu, b))
    return res

def mus(a, E, ctx):
    return {k: min((Fr(ordv(a[i], k), i) for i in range(1, ctx.m + 1) if a[i]), default=Fr(INF)) for k in E}

def omega(a, E, ctx):
    D, s, d = slopes(a, ctx)
    mu = mus(a, E, ctx)
    return d - sum(mu.values(), Fr(0))

def iota(a, E, ctx):
    r = regime(a, ctx)
    return (0 if r == 'R2' else 1, omega(a, E, ctx))

def iota_generic(a, E, S, ctx):
    """iota at the generic point of C_S, read in the coordinate z."""
    p, m = ctx.p, ctx.m
    D = min((Fr(ordS(a[i], S), i) for i in (p, m) if a[i]), default=Fr(INF))
    s = min((Fr(ordS(a[i], S), i) for i in ctx.rigid if a[i]), default=Fr(INF))
    d = min(D, s)
    mu = mus(a, set(E) & set(S), ctx)
    return (0 if s == 1 else 1, d - sum(mu.values(), Fr(0)))

def subsets(n=3):
    out = []
    for r in range(1, n + 1):
        from itertools import combinations
        out += [tuple(c) for c in combinations(range(n), r)]
    return out

def iota0(a, ctx):
    r = regime(a, ctx)
    if r == 'R1':
        return min(Fr(ordp(a[i]), i) for i in range(1, ctx.p + 1) if a[i])
    return slopes(a, ctx)[1]

def fmt(P):
    return ' + '.join(f"{c}*x^{e}" for e, c in sorted(P.items())) or '0'
