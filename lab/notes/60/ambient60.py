"""Changes of all n+1 coordinates (x, z) for z^p + h.

Part 1: random automorphisms Psi with z -> lam Z + (order >= 2), x -> A X + b Z + (order >= 2),
for D > p.  Check that in_W(F o Psi) has a torus singular point for W = (p,..,p,D) or
W = (p,..,p,D+1) (Theorem R1 of note 60).
Part 2: D = p.  The linear change that moves the singular lines of z^5 + 2x^2y^2(x+y) to the
coordinate axes; test every face of the result.
"""
import itertools, random, sys
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib60 import *

rng = random.Random(60)


def var(i, m, c=1):
    e = [0] * m
    e[i] = 1
    return {tuple(e): c}


def rand_poly(m, degs, p, density=0.5):
    r = {}
    for d in degs:
        for a in itertools.product(range(d + 1), repeat=m):
            if sum(a) == d and rng.random() < density:
                r[a] = rng.randrange(1, p)
    return r


def in_W(F, W):
    mw = min(sum(w * a for w, a in zip(W, e)) for e in F)
    return {e: c for e, c in F.items() if sum(w * a for w, a in zip(W, e)) == mw}


def run_part1(p, n, h, trials):
    m = n + 1
    D = sum(next(iter(h)))
    F = {tuple(list(a) + [0]): c for a, c in h.items()}
    F[tuple([0] * n + [p])] = 1
    # higher order terms of g
    F = add(F, {tuple(list(a) + [0]): c for a, c in rand_poly(n, [D + 1], p, 0.3).items()}, p)
    stats = {'W': 0, "W''": 0, 'none': 0}
    for _ in range(trials):
        while True:
            A = [[rng.randrange(p) for _ in range(n)] for _ in range(n)]
            import numpy as np
            if int(round(np.linalg.det(np.array(A, dtype=float)))) % p:
                break
        images = []
        for i in range(n):
            img = {}
            for j in range(n):
                if A[i][j]:
                    img = add(img, var(j, m, A[i][j]), p)
            img = add(img, var(n, m, rng.randrange(p)), p)       # b_i Z
            img = add(img, rand_poly(m, [2], p, 0.4), p)          # quadratic terms in X and Z
            images.append(img)
        lam = rng.randrange(1, p)
        zim = add(var(n, m, lam), rand_poly(m, [2, 3], p, 0.4), p)
        images.append(zim)
        Fp = compose(F, images, p, m)
        Fp = {e: c for e, c in Fp.items() if sum(e) <= D + 1}
        W1 = [p] * n + [D]
        W2 = [p] * n + [D + 1]
        if torus_test(in_W(Fp, W1), p, m, 'sing'):
            stats['W'] += 1
        elif torus_test(in_W(Fp, W2), p, m, 'sing'):
            stats["W''"] += 1
        else:
            stats['none'] += 1
    return stats


print('Part 1, Fano p=2:', run_part1(2, 3, {(2, 1, 1): 1, (1, 2, 1): 1, (1, 1, 2): 1}, 40))
print('Part 1, p=3 x^5y+xy^5:', run_part1(3, 2, {(5, 1): 1, (1, 5): 1}, 40))

# Part 2: p = 5, h = 2x^2y^2(x+y) = 2x^3y^2 + 2x^2y^3, D = p = 5.
p, n = 5, 2
h = {(3, 2): 2, (2, 3): 2}
print('h resonant', resonant(h, p, n), 'torus crit off zero', torus_test(h, p, n, 'off'))
for k in range(n):
    print(' d_%d h =' % k, deriv(h, k, p))
F = {(3, 2, 0): 2, (2, 3, 0): 2, (0, 0, 5): 1}
# x = X + Z, y = Y + Z, z = Z
images = [{(1, 0, 0): 1, (0, 0, 1): 1}, {(0, 1, 0): 1, (0, 0, 1): 1}, {(0, 0, 1): 1}]
Fp = compose(F, images, p, 3)
print('F\' =', sorted(Fp.items()))
print('F\' has no monomial in k[X^5,Y^5,Z^5]:', all(any(a % p for a in e) for e in Fp))
fs = faces(Fp, 3)
bad = []
for f in fs:
    s = torus_test(f, p, 3, 'sing')
    if s:
        bad.append(sorted(f))
print('faces:', len(fs), 'faces with a torus singular point:', bad)
