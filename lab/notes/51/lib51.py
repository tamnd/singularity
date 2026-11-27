import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Library for note 51 (track M2): exact polynomial arithmetic over F_p in the base variables
# (x, y, w) = indices (0, 1, 2); f = sum_i a_i z^{m-i}, a_0 = 1.
from math import comb, gcd
from fractions import Fraction as Fr
from itertools import product
import random

N3 = 3
ONE = {(0, 0, 0): 1}
INF = float('inf')

def add(A, B, p, s=1):
    R = dict(A)
    for e, c in B.items():
        R[e] = (R.get(e, 0) + s * c) % p
    return {e: c for e, c in R.items() if c}

def mul(A, B, p):
    R = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items():
            e = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2])
            R[e] = (R.get(e, 0) + c1 * c2) % p
    return {e: c for e, c in R.items() if c}

def scal(A, s, p):
    return {e: c * s % p for e, c in A.items() if c * s % p}

def order(A):
    return min((sum(e) for e in A), default=INF)

def form(A, d):
    return {e: c for e, c in A.items() if sum(e) == d}

def ord_S(A, S):
    return min((sum(e[s] for s in S) for e in A), default=INF)

def translate(a, c, p):
    """coefficients of f(z + c)"""
    m = len(a) - 1
    cp = [ONE]
    for k in range(1, m + 1):
        cp.append(mul(cp[-1], c, p) if c else {})
    out = []
    for i in range(m + 1):
        s = {}
        for j in range(i + 1):
            b = comb(m - j, i - j) % p
            if b and a[j] and cp[i - j]:
                s = add(s, scal(mul(a[j], cp[i - j], p), b, p), p)
        out.append(s)
    out[0] = ONE
    return out

def shift(A, var, lam, p):
    """x_var -> x_var + lam"""
    if lam % p == 0:
        return dict(A)
    R = {}
    for e, c in A.items():
        k = e[var]
        for t in range(k + 1):
            b = comb(k, t) * pow(lam, k - t, p) * c % p
            if b:
                ee = list(e); ee[var] = t; ee = tuple(ee)
                R[ee] = (R.get(ee, 0) + b) % p
    return {e: c for e, c in R.items() if c}

def blowup_chart(A, i, S, j):
    """centre V(z, x_s : s in S), chart of x_j (j in S): x_s = x_j x_s', z = x_j z'; divide by x_j^i"""
    R = {}
    for e, c in A.items():
        ee = list(e)
        ee[j] = sum(e[s] for s in S) - i
        if ee[j] < 0:
            raise ValueError("not permissible")
        R[tuple(ee)] = c
    return R

class F:
    """f with boundary: a = coefficient list, E = set of indices k with {x_k = 0} exceptional through 0"""
    def __init__(self, a, E, p):
        self.a = a; self.E = set(E); self.p = p; self.m = len(a) - 1
        m = self.m; e = 0
        while m % p ** (e + 1) == 0:
            e += 1
        self.e = e; self.q = p ** e; self.m0 = m // self.q
        self.rigid = [i for i in range(1, m + 1) if i % self.q]
        self.qidx = [i for i in range(1, m + 1) if i % self.q == 0]

def is_mult_m(a):
    return all(order(a[i]) >= i for i in range(1, len(a)))

def slopes(f, a=None):
    a = f.a if a is None else a
    D = min(Fr(order(a[i]), i) if a[i] else INF for i in f.qidx)
    s = min(Fr(order(a[i]), i) if a[i] else INF for i in f.rigid)
    return D, s

def proot(A, p):
    """p-th root of a polynomial over F_p, or None"""
    R = {}
    for e, c in A.items():
        if any(x % p for x in e):
            return None
        R[tuple(x // p for x in e)] = c
    return R

def solvable_C(f, a):
    """Lemma 2.1: if z is solvable return the form C with H_z = (Y + C^q)^{m0}, else None"""
    D, s = slopes(f, a)
    if not (s > D) or D == INF or D.denominator != 1:
        return None
    D = int(D); q = f.q; m0 = f.m0; p = f.p
    H = {k: form(a[q * k], q * k * D) for k in range(1, m0 + 1)}
    # coefficient of Y^{m0-1} is m0 C^q
    Cq = scal(H[1], pow(m0, -1, p), p)
    C = proot(Cq, p) if q == p else None
    if q != p:
        C = Cq
        for _ in range(f.e):
            C = proot(C, p) if C is not None else None
    if not C:
        return None
    # check H = (Y + C^q)^{m0}
    Cqk = ONE
    for k in range(1, m0 + 1):
        Cqk = mul(Cqk, Cq, p)
        want = scal(Cqk, comb(m0, k) % p, p)
        if want != H[k]:
            return None
    return C

def prepare(f, a, maxit=12):
    """iterate Lemma 2.1; returns (a, number of preparation steps)"""
    k = 0
    while k < maxit:
        C = solvable_C(f, a)
        if C is None:
            return a, k
        a = translate(a, scal(C, -1, f.p), f.p)
        k += 1
    return a, k

def tangent_cone(f, a):
    """T as dict over (X0, X1, X2, Z)"""
    T = {}
    for i in range(f.m + 1):
        A = ONE if i == 0 else form(a[i], i)
        for e, c in A.items():
            T[e + (f.m - i,)] = c
    return T

def invariant_under(T, v, p):
    """is T(X + t v) == T(X) for an indeterminate t? v in F_p^4"""
    R = {}
    for e, c in T.items():
        # expand prod (X_j + t v_j)^{e_j}; track exponent of t as 5th coord
        terms = {(0, 0, 0, 0, 0): c}
        for j in range(4):
            if e[j] == 0:
                continue
            new = {}
            for ex, cc in terms.items():
                for s in range(e[j] + 1):
                    b = comb(e[j], s) * pow(v[j], e[j] - s, p) % p if v[j] or s == e[j] else 0
                    if v[j] == 0 and s != e[j]:
                        continue
                    if b:
                        ee = list(ex); ee[j] += s; ee[4] += e[j] - s; ee = tuple(ee)
                        new[ee] = (new.get(ee, 0) + cc * b) % p
            terms = new
        for ex, cc in terms.items():
            if ex[4] > 0:
                R[ex] = (R.get(ex, 0) + cc) % p
    return all(c == 0 for c in R.values())

def directrix_Z(f, a):
    """vectors v_X with (v_X, 1) in Dir(T), and vectors u with (u, 0) in Dir(T)"""
    T = tangent_cone(f, a)
    p = f.p
    A = [v for v in product(range(p), repeat=3) if invariant_under(T, v + (1,), p)]
    return A, T

def adapt_directrix(f, a):
    """at delta = 1: translate z by a linear form so that Dir(T) is in V(Z). returns (a, changed)"""
    p = f.p
    A, T = directrix_Z(f, a)
    if not A:
        return a, False
    U = [u for u in product(range(p), repeat=3) if any(u) and invariant_under(T, u + (0,), p)]
    v0 = A[0]
    for l in product(range(p), repeat=3):
        if sum(x * y for x, y in zip(l, v0)) % p == 1 and all(sum(x * y for x, y in zip(l, u)) % p == 0 for u in U):
            c = {}
            for j in range(3):
                if l[j]:
                    ee = [0, 0, 0]; ee[j] = 1; c[tuple(ee)] = l[j]
            return translate(a, c, p), True
    raise RuntimeError("no adapting form")

def regime(f, a):
    D, s = slopes(f, a)
    if s > D:
        return 1, D, s
    return (2 if s == 1 else 3), D, s

def adapt(f, a):
    """adapted coordinate: q-prepared, and Dir(T) in V(Z) when delta = 1.
    returns (a, info) with info = (prep steps, directrix change)"""
    a, k = prepare(f, a)
    D, s = slopes(f, a)
    dch = False
    if min(D, s) == 1:
        a, dch = adapt_directrix(f, a)
    return a, (k, dch)

def mu(f, a, k):
    return min((Fr(ord_S(a[i], (k,)), i) for i in range(1, f.m + 1) if a[i]), default=INF)

def omega(f, a, E):
    d = min(Fr(order(a[i]), i) for i in range(1, f.m + 1) if a[i])
    return d - sum(mu(f, a, k) for k in E)

def iota(f, a, E):
    """iota = (class, omega): class 0 for R2, 1 for R1 and R3"""
    r, D, s = regime(f, a)
    if CLS == "res":
        M = sum(mu(f, a, k) for k in E)
        cls = 0 if (s - M <= 1 and s <= D) else 1
        return (cls, omega(f, a, E)), r
    return (0 if r == 2 else 1, omega(f, a, E)), r

def iota_S(f, a, E, S):
    """iota at the generic point of V(z, x_S) in the same coordinate"""
    dS = min(Fr(ord_S(a[i], S), i) for i in range(1, f.m + 1) if a[i])
    sS = min((Fr(ord_S(a[i], S), i) for i in f.rigid if a[i]), default=INF)
    DS = min((Fr(ord_S(a[i], S), i) for i in f.qidx if a[i]), default=INF)
    cls = 0 if (sS == 1 and sS <= DS) else 1
    if CLS == "res":
        M = sum(mu(f, a, k) for k in E if k in S)
        cls = 0 if (sS - M <= 1 and sS <= DS) else 1
    return (cls, dS - sum(mu(f, a, k) for k in E if k in S))

import os
DIV = os.environ.get('DIV', '0') == '1'
CLS = os.environ.get('CLS', 'plain')
MONO = os.environ.get('MONO', '1') == '1'
TIE = os.environ.get('TIE', 'pick')
SUBSETS = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]

def permissible(f, a, S):
    return all(ord_S(a[i], S) >= i for i in range(1, f.m + 1))

def rule_centre(f, a, E):
    """largest coordinate subspace V(z, x_S) in Max with iota constant = iota(0); returns (S, ties)"""
    io, r = iota(f, a, E)
    if DIV:
        # step 0: a component of Max of codimension one in the base (a_i in (x_k)^i for all i) is blown up first
        divs = [S for S in SUBSETS if len(S) == 1 and permissible(f, a, S)]
        if divs:
            S = max(divs, key=lambda S: (sum(mu(f, a, k) for k in S if k in E), [-k for k in S]))
            return S, (len(divs) if len(divs) > 1 else 0)
    if io[1] == 0 and MONO:
        # monomial case (omega = 0): Encinas-Villamayor combinatorial rule, the class is ignored
        cands = [S for S in SUBSETS if permissible(f, a, S)]
    else:
        cands = [S for S in SUBSETS if permissible(f, a, S) and iota_S(f, a, E, S) == io]
    k = min(len(S) for S in cands)
    mins = [S for S in cands if len(S) == k]
    if len(mins) == 1:
        return mins[0], 0
    if TIE == "union":
        U = tuple(sorted(set().union(*mins)))
        return U, len(mins)
    # monomial-case tie-break (Encinas-Villamayor, Bierstone-Milman): keep the minimal number of
    # components; among those prefer the largest sum of mu over S cap E, then the first in index order
    S = max(mins, key=lambda S: (sum(mu(f, a, k) for k in S if k in E), [-k for k in S]))
    return S, len(mins)

def points_over(f, a, E, S):
    """all F_p-rational points of multiplicity m over the origin after blowing up V(z, x_S).
    returns list of (chart, lams, nu, new a, new E)"""
    p, m = f.p, f.m
    out = []
    for j in S:
        b = [ONE] + [blowup_chart(a[i], i, S, j) if a[i] else {} for i in range(1, m + 1)]
        others = [s for s in S if s != j]
        for lams in product(range(p), repeat=len(others)):
            c = b
            for s, lam in zip(others, lams):
                c = [shift(x, s, lam, p) for x in c]
            if not all(order(c[i]) >= 1 for i in f.rigid):
                continue
            for nu in range(p):
                d = translate(c, {(0, 0, 0): nu}, p) if nu else c
                if is_mult_m(d):
                    lamd = dict(zip(others, lams))
                    E2 = {j} | {k for k in E if (k in S and k != j and lamd.get(k, 0) == 0)} | {k for k in E if k not in S}
                    out.append((j, lams, nu, d, E2))
    return out

def size(a):
    return sum(len(x) for x in a)

def rand_supp(S0, i, extra, dens, p, rng, maxdeg=None):
    P = {}
    for ex in product(range(i + extra + 2), repeat=3):
        ds = sum(ex[s] for s in S0)
        if i <= ds <= i + extra and sum(ex) <= i + extra + 1 and rng.random() < dens:
            P[ex] = rng.randrange(1, p)
    return P
