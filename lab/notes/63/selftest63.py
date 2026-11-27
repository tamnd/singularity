"""Self test: iterated steps against the closed form of Lemma 3.17.1."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import random, sys
from math import comb
from core63 import Field, step, clean, invariants, addto


def closed_form(F, g, word, trans):
    """M^{-p} cl g(phi_m + M x, psi_m + M w), all in the exponents at level m."""
    p = F.p
    # exponent vectors of y_N, z_N in y_m, z_m: track matrix
    # y_m^a z_m^b ; y-chart: y_m = y', z_m = y' z' ; z-chart: z_m = z', y_m = z' y'
    Y = (1, 0)
    Z = (0, 1)
    M = (0, 0)
    phi = {}
    psi = {}
    def mapmono(e, chart):
        a, b = e
        return (a + b, b) if chart == 'y' else (a, a + b)
    for ch, (a, b) in zip(word, trans):
        Y, Z, M = mapmono(Y, ch), mapmono(Z, ch), mapmono(M, ch)
        phi = {mapmono(e, ch): c for e, c in phi.items()}
        psi = {mapmono(e, ch): c for e, c in psi.items()}
        L = (1, 0) if ch == 'y' else (0, 1)
        M = (M[0] + L[0], M[1] + L[1])
        if a:
            addto(F, phi, M, a)
        if b:
            addto(F, psi, M, b)
    # X = phi + M x as dict {(s, ya, za): c} with s the power of x
    def lin(ph):
        d = {(0, e[0], e[1]): c for e, c in ph.items()}
        d[(1, M[0], M[1])] = 1
        return d
    def mul(A, B):
        out = {}
        for (s, a1, b1), c in A.items():
            for (t, a2, b2), e in B.items():
                addto(F, out, (s + t, a1 + a2, b1 + b2), F.mul[c][e])
        return out
    X, W = lin(phi), lin(psi)
    Xp = [{(0, 0, 0): 1}]
    Wp = [{(0, 0, 0): 1}]
    D = max(m[0] for m in g) + 1
    E = max(m[1] for m in g) + 1
    for _ in range(D):
        Xp.append(mul(Xp[-1], X))
    for _ in range(E):
        Wp.append(mul(Wp[-1], W))
    out = {}
    for (i, l, j, k), c in g.items():
        mono = (j * Y[0] + k * Z[0], j * Y[1] + k * Z[1])
        for (s, a1, b1), c1 in Xp[i].items():
            for (t, a2, b2), c2 in Wp[l].items():
                addto(F, out, (s, t, mono[0] + a1 + a2, mono[1] + b1 + b2), F.mul[c][F.mul[c1][c2]])
    out = clean(F, out)
    res = {}
    for (s, t, a1, b1), c in out.items():
        res[(s, t, a1 - p * M[0], b1 - p * M[1])] = c
    return res


def rand_g(F, rng, D):
    p = F.p
    g = {}
    for _ in range(6):
        i = rng.randint(0, D)
        l = rng.randint(0, D - i)
        j = rng.randint(0, p + 2)
        k = rng.randint(0, p + 2)
        if i + l + j + k < p:
            j += p
        addto(F, g, (i, l, j, k), rng.randrange(1, F.q))
    return clean(F, g)


if __name__ == '__main__':
    rng = random.Random(63)
    bad = tot = 0
    for (p, e) in [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (5, 2), (7, 1)]:
        F = Field(p, e)
        for trial in range(60):
            D = rng.randint(1, p + 1)
            g = rand_g(F, rng, D)
            word = [rng.choice('yz') for _ in range(5)]
            trans = [(rng.randrange(F.q), rng.randrange(F.q)) for _ in range(5)]
            h = g
            ok = True
            try:
                for ch, (a, b) in zip(word, trans):
                    h = step(F, h, ch, a, b)
            except ValueError:
                continue
            cf = closed_form(F, g, word, trans)
            tot += 1
            if cf != h:
                bad += 1
    print('closed form vs iterated steps: mismatches', bad, 'of', tot)
    # rho from generators versus the monomial description of note 50, Section 1
    bad = tot = 0
    for (p, e) in [(2, 1), (3, 1), (5, 1), (7, 1)]:
        F = Field(p, e)
        for trial in range(300):
            g = rand_g(F, rng, rng.randint(1, p + 1))
            if not g:
                continue
            inv = invariants(F, g)
            if inv is None:
                continue
            ordg, ry, rz, d, rho = inv
            best = None
            for (i, l, j, k) in g:
                ee = i + l + j - ry + k - rz
                if i % p or l % p:
                    v = ee - 1
                elif (ry + j - ry) % p or (k) % p:
                    v = ee
                else:
                    v = None
                if v is not None and (best is None or v < best):
                    best = v
            tot += 1
            if best != rho:
                bad += 1
    print('rho generators vs monomial description: mismatches', bad, 'of', tot)
