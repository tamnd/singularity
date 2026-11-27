"""Note 54 core (written from the definitions of handbook Vol 7, Sections 3.15 and 3.17; no code shared
with the scripts of notes 50 or 52).
Field F_q, q = p or p^2 (F_{p^2} = F_p[t]/(t^2 - n), n a non-residue), element u + v t encoded as u + p v.
A point is a dict {(i, l, j, k): c} for the monomial x^i w^l y^j z^k.
step_all(g, chart) returns, for ALL translations (a, b) in F_q^2 at once, the transformed point
(strict transform divided by L^p, then cleaned) in vectorized form, and the invariants r, d, rho, ord."""
import numpy as np, itertools, random
from math import comb

class Fq:
    def __init__(self, p, e=1):
        self.p, self.e, self.q = p, e, p ** e
        if e == 2:
            self.n = next(c for c in range(2, p) if pow(c, (p - 1) // 2, p) == p - 1)
        q = self.q
        self.mul = [[self._mul(a, b) for b in range(q)] for a in range(q)]
        self.add = [[self._add(a, b) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(q) if self.mul[a][b] == 1) for a in range(1, q)]
        # all elements as (u, v) arrays
        el = np.arange(q)
        self.U, self.V = el % p, el // p
    def _add(self, a, b):
        p = self.p
        return ((a % p + b % p) % p) + p * ((a // p + b // p) % p)
    def _mul(self, a, b):
        p = self.p
        if self.e == 1: return (a * b) % p
        u, v, s, t = a % p, a // p, b % p, b // p
        return ((u * s + self.n * v * t) % p) + p * ((u * t + v * s) % p)
    def i2f(self, k): return k % self.p
    def pw(self, a, k):
        r = 1
        for _ in range(k): r = self.mul[r][a]
        return r

def det_nonzero(K, u1, u2):
    return K.add[K.mul[u1[0]][u2[1]]][K.neg[K.mul[u1[1]][u2[0]]]] != 0

def rank(K, vecs):
    vs = [v for v in vecs if v != (0, 0)]
    if not vs: return 0
    for v in vs[1:]:
        if det_nonzero(K, vs[0], v): return 2
    return 1

class Stepper:
    """precomputes the evaluation matrix of the basis a^alpha b^beta on all (a, b) in F_q^2"""
    def __init__(self, K, D=3):
        self.K, self.D = K, D
        q = K.q
        self.pairs = [(a, b) for a in range(q) for b in range(q)]
        B = (D + 1) ** 2
        E = np.zeros((B, q * q), dtype=np.int64)
        for c, (a, b) in enumerate(self.pairs):
            for al in range(D + 1):
                for be in range(D + 1):
                    E[al * (D + 1) + be, c] = K.mul[K.pw(a, al)][K.pw(b, be)]
        self.Eu, self.Ev = E % K.p, E // K.p
    def param(self, g, chart):
        K, D, p = self.K, self.D, self.K.p
        B = (D + 1) ** 2
        rows = {}
        for (i, l, j, k), c in g.items():
            e = i + l + j + k - p
            assert e >= 0
            new = (e, k) if chart == 'y' else (j, e)
            for s in range(i + 1):
                cs = K.mul[c][K.i2f(comb(i, s))]
                if cs == 0: continue
                for t in range(l + 1):
                    ct = K.mul[cs][K.i2f(comb(l, t))]
                    if ct == 0: continue
                    mo = (s, t) + new
                    if all(x % p == 0 for x in mo): continue   # cleaning (independent of a, b)
                    r = rows.get(mo)
                    if r is None: r = rows[mo] = [0] * B
                    idx = (i - s) * (D + 1) + (l - t)
                    r[idx] = K.add[r[idx]][ct]
        return rows
    def step_all(self, g, chart):
        K, p = self.K, self.K.p
        rows = self.param(g, chart)
        monos = list(rows)
        if not monos: return None
        C = np.array([rows[m] for m in monos], dtype=np.int64)
        Cu, Cv = C % p, C // p
        if K.e == 1:
            Vu = (Cu @ self.Eu) % p; Vv = np.zeros_like(Vu)
        else:
            Vu = (Cu @ self.Eu + K.n * (Cv @ self.Ev)) % p
            Vv = (Cu @ self.Ev + Cv @ self.Eu) % p
        mask = (Vu != 0) | (Vv != 0)
        M = np.array(monos, dtype=np.int64)
        big = 10 ** 6
        ry = np.where(mask, M[:, 2:3], big).min(0)
        rz = np.where(mask, M[:, 3:4], big).min(0)
        xw = M[:, 0] + M[:, 1]
        tot = xw + M[:, 2] + M[:, 3]
        ordg = np.where(mask, tot[:, None], big).min(0)
        degG = tot[:, None] - ry[None, :] - rz[None, :]
        wt = degG - (xw[:, None] > 0)
        rho = np.where(mask, wt, big).min(0)
        d = np.where(mask, degG, big).min(0)
        return dict(monos=monos, Vu=Vu, Vv=Vv, mask=mask, ry=ry, rz=rz, ordg=ordg, rho=rho, d=d)
    def column(self, S, c):
        p = self.K.p
        return {m: int(S['Vu'][r, c] + p * S['Vv'][r, c]) for r, m in enumerate(S['monos']) if S['mask'][r, c]}

def invariants(K, g):
    p = K.p
    if not g: return None
    ry = min(m[2] for m in g); rz = min(m[3] for m in g)
    G = {(i, l, j - ry, k - rz): c for (i, l, j, k), c in g.items()}
    d = min(sum(m) for m in G)
    rho = min(sum(m) - (1 if m[0] + m[1] > 0 else 0) for m in G)
    inG = {m: c for m, c in G.items() if sum(m) == d}
    return dict(ry=ry, rz=rz, d=d, rho=rho, ordg=ry + rz + d, G=G, inG=inG,
                binary=all(m[2] == 0 and m[3] == 0 for m in inG),
                curve_y=min(i + l + j for (i, l, j, k) in G), curve_z=min(i + l + k for (i, l, j, k) in G),
                surf_y=min(i + j for (i, l, j, k) in G), surf_z=min(i + k for (i, l, j, k) in G))

def lemma51_condition(K, g):
    """Condition of Lemma 5.1, invariant under linear changes of (x, w): with mu the largest monomial dividing
    all A_kl, (k, l) != (0, 0), the monomial mu itself occurs in A_10 or A_01."""
    nc = [m for m in g if m[0] + m[1] > 0]
    if not nc: return False
    my = min(m[2] for m in nc); mz = min(m[3] for m in nc)
    return (1, 0, my, mz) in g or (0, 1, my, mz) in g

def check_rho_formula(K, g):
    """direct computation of rho from the generators of Theta (for testing the shortcut formula)"""
    p = K.p
    gens = []
    for idx in range(4):
        h = {}
        for m, c in g.items():
            e = m[idx]
            if e % p == 0: continue
            nm = list(m)
            if idx < 2: nm[idx] -= 1
            h[tuple(nm)] = K.mul[c][K.i2f(e)]
        gens.append(h)
    allm = [m for h in gens for m in h]
    ry = min(m[2] for m in allm); rz = min(m[3] for m in allm)
    return ry, rz, min(sum(m) - ry - rz for m in allm)
