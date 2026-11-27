import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Library for note 61: intrinsic omega on the characteristic polyhedron.
# Builds on ../53/lib53.py (exact arithmetic over F_p, three base variables).
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib53 import *
from lib53 import INF

W_XI = (1, 1, 1)

def ordw(P, w):
    return min((sum(wi * ei for wi, ei in zip(w, e)) for e in P), default=INF)

def inw(P, w, d):
    return {e: c for e, c in P.items() if sum(wi * ei for wi, ei in zip(w, e)) == d}

def wslopes(a, w, ctx):
    p, m = ctx.p, ctx.m
    D = min((Fr(ordw(a[i], w), i) for i in (p, m) if a[i]), default=Fr(INF))
    s = min((Fr(ordw(a[i], w), i) for i in ctx.rigid if a[i]), default=Fr(INF))
    return D, s, min(D, s)

def wsolvable(a, w, ctx):
    """Vertex test for the monomial valuation of weight w (w = (1,1,1): the closed point;
    w = e_k: the generic point of V(x_k); w = 1 on S, 0 elsewhere: the generic point of V(x_S)).
    Returns lambda with in_w f = (Z^p + lambda^p)^2, or None."""
    p, m = ctx.p, ctx.m
    D, s, d = wslopes(a, w, ctx)
    if D >= INF or not (s > D) or D.denominator != 1:
        return None
    Dn = int(D)
    h1 = inw(a[p], w, p * Dn)
    h2 = inw(a[m], w, m * Dn)
    if not h1:
        return None
    if any(x % p for e in h1 for x in e):
        return None
    inv2 = pow(2, p - 2, p)
    lam = {tuple(x // p for x in e): (c * inv2) % p for e, c in h1.items()}
    if clean(pw(lam, m, p), p) != h2:
        return None
    return lam

def wprepare(a, w, ctx, cap=30):
    n = 0
    while True:
        lam = wsolvable(a, w, ctx)
        if lam is None:
            return a, n, False
        a = translate(a, scal(lam, -1, ctx.p), ctx)
        n += 1
        if n >= cap:
            return a, n, True

def wdelta(a, w, ctx, cap=30):
    b, n, capped = wprepare(a, w, ctx, cap)
    return wslopes(b, w, ctx)[2], capped

def ek(k):
    e = [0, 0, 0]; e[k] = 1
    return tuple(e)

def wS(S):
    return tuple(1 if t in S else 0 for t in range(3))

def delta_star(a, ctx):
    return wdelta(a, W_XI, ctx)[0]

def mu_star(a, k, ctx):
    return wdelta(a, ek(k), ctx)[0]

def omega_star(a, E, ctx):
    d = delta_star(a, ctx)
    return d - sum((mu_star(a, k, ctx) for k in E), Fr(0))

ALLW = [W_XI] + [ek(k) for k in range(3)] + [wS(S) for S in ((0, 1), (0, 2), (1, 2))]

def full_prepare(a, ctx, weights=ALLW, cap=60):
    """Simultaneous preparation at the closed point and at the generic points of all
    coordinate primes (Lemma 61.4). Returns (a, steps, capped)."""
    n = 0
    while True:
        moved = False
        for w in weights:
            lam = wsolvable(a, w, ctx)
            if lam is not None:
                a = translate(a, scal(lam, -1, ctx.p), ctx)
                n += 1; moved = True
                break
        if not moved:
            return a, n, False
        if n >= cap:
            return a, n, True

def is_fully_prepared(a, ctx, weights=ALLW):
    return all(wsolvable(a, w, ctx) is None for w in weights)

def linear_adapt(a, ctx):
    """Linear step of Lemma 3.2 of note 51 when delta = 1 and U(T) is not in {v_Z = 0}."""
    D, s, d = slopes(a, ctx)
    if d != 1:
        return a, False
    U = U_space(tangent_cone(a, ctx), ctx.p)
    if not any(v[3] for v in U):
        return a, False
    l = solve_l(U, ctx.p)
    L = {}
    for k in range(3):
        if l[k]:
            L[ek(k)] = l[k]
    return translate(a, L, ctx), True

def E_adapt(a, ctx, cap=6):
    """Fully prepared and adapted coordinate. Returns (a, info) where info records
    whether the linear step was needed and whether a conflict remained."""
    info = dict(lin=0, conflict=False, capped=False)
    for _ in range(cap):
        a, n, c = full_prepare(a, ctx)
        info['capped'] |= c
        a2, lin = linear_adapt(a, ctx)
        if not lin:
            return a, info
        info['lin'] += 1
        a = a2
    info['conflict'] = True
    return a, info

def invariants(a, E, ctx):
    """All intrinsic data at the point, computed by preparation from the given coordinate."""
    d = delta_star(a, ctx)
    mu = {k: mu_star(a, k, ctx) for k in range(3)}
    om = d - sum((mu[k] for k in E), Fr(0))
    b, _, _ = wprepare(a, W_XI, ctx)
    D, s, _ = slopes(b, ctx)
    reg = 'R2' if s == 1 else ('R1' if s > D else 'R3')
    return dict(delta=d, mu=mu, omega=om, regime=reg, sigma=s, D=D)

def cls_plain(inv):
    return 0 if inv['regime'] == 'R2' else 1

def cls_res(inv, E):
    s = inv['sigma']
    smu = sum((inv['mu'][k] for k in E), Fr(0))
    return 0 if (s - smu <= 1 and s <= inv['D']) else 1

def generic_inv(a, E, S, ctx):
    """delta, omega and regime at the generic point of V(x_S) (|S| = 1, 2) or the point (|S| = 3)."""
    w = wS(S)
    b, _, _ = wprepare(a, w, ctx)
    D, s, d = wslopes(b, w, ctx)
    mu = sum((mu_star(a, k, ctx) for k in E if k in S), Fr(0))
    reg = 'R2' if s == 1 else ('R1' if s > D else 'R3')
    return dict(delta=d, omega=d - mu, regime=reg, sigma=s, D=D)

def mk(ctx, terms):
    a = [{(0, 0, 0): 1}] + [{} for _ in range(ctx.m)]
    for i, e, c in terms:
        a[i] = add(a[i], mono(e, c), ctx.p)
    return a
