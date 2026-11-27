"""C4 test cases of note 55, Section 12, recomputed independently."""
import itertools, sys, time
import numpy as np
import galois
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib60 import *

cases = {
    'p=2 Fano xyw(x+y+w)': (2, 3, {(2, 1, 1): 1, (1, 2, 1): 1, (1, 1, 2): 1}),
    'p=3 x^5y+xy^5': (3, 2, {(5, 1): 1, (1, 5): 1}),
    'p=5 x^4y+xy^4': (5, 2, {(4, 1): 1, (1, 4): 1}),
}


def proj_points(F, n):
    q = F.order
    for v in itertools.product(range(q), repeat=n):
        v = list(v)
        nz = [i for i in range(n) if v[i]]
        if not nz or v[nz[0]] != 1:
            continue
        yield F(v)


def eval_poly(h, F, v):
    s = F(0)
    for a, c in h.items():
        t = F(c)
        for i, ai in enumerate(a):
            t = t * v[i] ** ai
        s = s + t
    return s


def crit_set(h, p, n, k):
    F = galois.GF(p ** k)
    ders = [deriv(h, i, p) for i in range(n)]
    pts = []
    for v in proj_points(F, n):
        if all(eval_poly(d, F, v) == 0 for d in ders):
            pts.append(v)
    return F, pts


for name, (p, n, h) in cases.items():
    print('==', name)
    print(' resonant:', resonant(h, p, n))
    print(' torus crit:', torus_test(h, p, n, 'crit'), ' off zero:', torus_test(h, p, n, 'off'),
          ' torus sing of {h=0}:', torus_test(h, p, n, 'sing'))
    for f in faces(h, n)[1:]:
        print('  proper face', sorted(f), 'torus crit:', torus_test(f, p, n, 'crit'))
    for k in ([1, 2, 3, 4] if p == 2 else [1, 2, 4] if p == 3 else [1, 2]):
        F, pts = crit_set(h, p, n, k)
        tor = [v for v in pts if all(x != 0 for x in v)]
        vals = [eval_poly(h, F, v) for v in tor]
        print('  over F_%d: %d projective critical points, %d in torus, h values there %s'
              % (F.order, len(pts), len(tor), [int(x) for x in vals]))

# Fano covering check over F_4 and F_16: no three independent lines cover P^2(F_2)
p, n, h = cases['p=2 Fano xyw(x+y+w)']
for k in (2, 4):
    F = galois.GF(2 ** k)
    fano = [F(list(v)) for v in itertools.product(range(2), repeat=3) if any(v)]
    lines = list(proj_points(F, 3))
    # incidence: which Fano points lie on each line
    inc = []
    for L in lines:
        inc.append(frozenset(i for i, v in enumerate(fano) if L[0] * v[0] + L[1] * v[1] + L[2] * v[2] == 0))
    best = 0
    found = False
    t0 = time.time()
    # only lines through at least one Fano point matter for the maximum
    useful = [(L, s) for L, s in zip(lines, inc) if s]
    for (L1, s1), (L2, s2), (L3, s3) in itertools.combinations(useful, 3):
        cov = len(s1 | s2 | s3)
        if cov > best or cov == 7:
            M = galois.GF(2 ** k)(np.array([L1, L2, L3]))
            if np.linalg.matrix_rank(M) == 3:
                best = max(best, cov)
                if cov == 7:
                    found = True
    print('Fano cover over F_%d: lines %d, max covered by 3 independent lines = %d, cover of all 7: %s (%.1fs)'
          % (2 ** k, len(lines), best, found, time.time() - t0))

# all linear changes over the prime field: top face after cleaning always has a torus critical point
for name, (p, n, h) in cases.items():
    cnt = bad = 0
    for M in itertools.product(range(p), repeat=n * n):
        A = [M[i * n:(i + 1) * n] for i in range(n)]
        det = int(round(np.linalg.det(np.array(A, dtype=float))))
        if det % p == 0:
            continue
        images = []
        for i in range(n):
            img = {}
            for j in range(n):
                if A[i][j]:
                    e = [0] * n
                    e[j] = 1
                    img[tuple(e)] = A[i][j]
            images.append(img)
        g = clean(compose(h, images, p, n), p)
        cnt += 1
        if not g or torus_test(g, p, n, 'crit'):
            bad += 1
    print('%s: %d linear changes over F_%d, top face degenerate in %d' % (name, cnt, p, bad))
