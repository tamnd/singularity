"""Referee 63: independent core for corner runs in four variables.

Written from the definitions of handbook Section 3.17 (Lemma 3.17.1 setting).
A point is a dict {(i, l, j, k): c} for c x^i w^l y^j z^k, c in F_q (coded 0..q-1).
No code is shared with the scripts of notes 54, 50 or 52.
"""
import random
from math import comb


class Field:
    def __init__(self, p, e):
        self.p, self.e = p, e
        self.q = p ** e
        q = self.q
        if e == 1:
            self.add = [[(a + b) % p for b in range(q)] for a in range(q)]
            self.mul = [[(a * b) % p for b in range(q)] for a in range(q)]
        else:
            # F_p[t]/(t^2 - n), n a non-residue (p odd), or t^2 + t + 1 for p = 2
            if p == 2:
                def mulp(a0, a1, b0, b1):
                    # t^2 = t + 1
                    c0 = a0 * b0 + a1 * b1
                    c1 = a0 * b1 + a1 * b0 + a1 * b1
                    return c0 % 2, c1 % 2
            else:
                squares = {(x * x) % p for x in range(1, p)}
                n = next(x for x in range(2, p) if x not in squares)
                def mulp(a0, a1, b0, b1):
                    return (a0 * b0 + n * a1 * b1) % p, (a0 * b1 + a1 * b0) % p
            enc = lambda c0, c1: c0 + p * c1
            self.add = [[enc((a % p + b % p) % p, (a // p + b // p) % p) for b in range(q)] for a in range(q)]
            self.mul = [[enc(*mulp(a % p, a // p, b % p, b // p)) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(q) if self.mul[a][b] == 1) for a in range(1, q)]
        # powers table
        self.pw = [[1] * 64 for _ in range(q)]
        for a in range(q):
            for k in range(1, 64):
                self.pw[a][k] = self.mul[self.pw[a][k - 1]][a]

    def intc(self, n):
        """image of the integer n in F_q"""
        return n % self.p  # the prime field elements are coded 0..p-1


def addto(F, d, key, c):
    if c == 0:
        return
    o = d.get(key, 0)
    s = F.add[o][c]
    if s:
        d[key] = s
    elif o:
        del d[key]


def clean(F, g):
    p = F.p
    return {m: c for m, c in g.items() if not (m[0] % p == 0 and m[1] % p == 0 and m[2] % p == 0 and m[3] % p == 0)}


def step(F, g, chart, a, b):
    """blow up the origin, take the chart, translate by (a, b), divide by L^p, clean"""
    p = F.p
    out = {}
    cache = {}
    for (i, l, j, k), c in g.items():
        tot = i + l + j + k - p
        if tot < 0:
            raise ValueError("ord < p")
        key = (i, l)
        if key not in cache:
            ex = []
            for s in range(i + 1):
                cs = F.mul[F.intc(comb(i, s))][F.pw[a][i - s]]
                if cs == 0:
                    continue
                for t in range(l + 1):
                    ct = F.mul[F.intc(comb(l, t))][F.pw[b][l - t]]
                    if ct == 0:
                        continue
                    ex.append((s, t, F.mul[cs][ct]))
            cache[key] = ex
        if chart == 'y':
            jj, kk = tot, k
        else:
            jj, kk = j, tot
        for s, t, cst in cache[key]:
            addto(F, out, (s, t, jj, kk), F.mul[c][cst])
    return clean(F, out)


def invariants(F, g):
    """(ord g, r_y, r_z, d, rho) from the generators g_x, g_w, y g_y, z g_z of Theta"""
    if not g:
        return None
    p = F.p
    ordg = min(sum(m) for m in g)
    gens = [[], [], [], []]
    for (i, l, j, k), c in g.items():
        if i % p:
            gens[0].append((i - 1, l, j, k))
        if l % p:
            gens[1].append((i, l - 1, j, k))
        if j % p:
            gens[2].append((i, l, j, k))
        if k % p:
            gens[3].append((i, l, j, k))
    allm = [m for G in gens for m in G]
    if not allm:
        return None
    ry = min(m[2] for m in allm)
    rz = min(m[3] for m in allm)
    rho = min(m[0] + m[1] + m[2] - ry + m[3] - rz for m in allm)
    # G = g / y^ry z^rz ; check divisibility
    for m in g:
        if m[2] < ry or m[3] < rz:
            raise ValueError("g not divisible by the monomial of Theta")
    d = min(m[0] + m[1] + m[2] - ry + m[3] - rz for m in g)
    return ordg, ry, rz, d, rho


def deg_xw(g):
    return max(m[0] + m[1] for m in g)


def initial_form(g, inv):
    ordg, ry, rz, d, rho = inv
    return {m: c for m, c in g.items() if m[0] + m[1] + m[2] - ry + m[3] - rz == d}
