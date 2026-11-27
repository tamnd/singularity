"""Brute force over all linear changes over F_p for some lab rows (forms taken from the
recorded data of note 55), and the counterexamples of note 60."""
import json, sys, itertools, time
import numpy as np
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib60 import *


def lin_images(A, n):
    ims = []
    for i in range(n):
        img = {}
        for j in range(n):
            if A[i][j]:
                e = [0] * n
                e[j] = 1
                img[tuple(e)] = A[i][j]
        ims.append(img)
    return ims


def gl(p, n):
    for M in itertools.product(range(p), repeat=n * n):
        A = [M[i * n:(i + 1) * n] for i in range(n)]
        if int(round(np.linalg.det(np.array(A, dtype=float)))) % p:
            yield A


def linear_preparable(h, p, n):
    for A in gl(p, n):
        g = clean(compose(h, lin_images(A, n), p, n), p)
        if nondeg_all_faces(g, p, n):
            return True
    return False


mode = sys.argv[1]
if mode == 'rows':
    want = {(2, 3, (1, 1, 1), 4), (5, 2, (1, 1), 5), (3, 2, (1, 1), 6)}
    seen = {}
    for fn in ['run_p2.jsonl', 'run_p3.jsonl', 'run_p5n2.jsonl']:
        for l in open(os.path.join(HERE, '..', '55', fn)):
            r = json.loads(l)
            k = (r['p'], r['n'], tuple(r['wt']), r['D'])
            if k in want:
                h = from_json(r['h'])
                t0 = time.time()
                ok = linear_preparable(h, r['p'], r['n'])
                rec = r['prepared'] == 'linear'
                seen.setdefault(k, []).append((ok, rec))
                print(k, 'brute force linear over F_p:', ok, ' recorded:', rec, ' %.1fs' % (time.time() - t0), flush=True)
    for k, v in seen.items():
        print(k, 'agree', sum(a == b for a, b in v), 'of', len(v), '; preparable', sum(a for a, b in v))

if mode == 'prop54':
    # Proposition 5.4(b) counterexample: p = 3, w = (1,2), h = x^4y^4 + x^2y^5, D = 12.
    p, n = 3, 2
    h = {(4, 4): 1, (2, 5): 1}
    print('resonant', resonant(h, p, n), 'torus crit', torus_test(h, p, n, 'crit'),
          'off zero', torus_test(h, p, n, 'off'), '{h=0} sing in torus', torus_test(h, p, n, 'sing'))
    print('d_x h', deriv(h, 0, p), ' d_y h', deriv(h, 1, p))
    cnt = bad = 0
    for al in range(1, p):
        for be in range(1, p):
            for ga in range(p):
                im = [{(1, 0): al}, add({(0, 1): be}, {(2, 0): ga}, p)]
                g = clean(compose(h, im, p, n), p)
                cnt += 1
                bad += torus_test(g, p, n, 'crit')
    print('weight preserving changes over F_3:', cnt, ' top face degenerate:', bad)

if mode == 'prop111':
    # Proposition 11.1: f = z^3 + x^2y + xy^2 + y^4, p = 3, chart x, y = x t, z = x z'.
    import sympy as sp
    x, t, z = sp.symbols('x t z')
    f = z**3 + x**2 * (x * t) + x * (x * t)**2 + (x * t)**4
    Ft = sp.expand(f.subs(z, x * z) / x**3)
    print('strict transform:', Ft)
    P = {x: 0, t: 1, z: 1}
    val = Ft.subs(P) % 3
    grad = [sp.diff(Ft, v).subs(P) % 3 for v in (x, t, z)]
    print('value at P mod 3:', val, ' gradient (d_x, d_t, d_z) mod 3:', grad)
    R = Ft.subs(x, 0)
    print('restriction to E: ', R, ' gradient at P:', [sp.diff(R, v).subs(P) % 3 for v in (t, z)])

if mode == 'thm112':
    # Theorem 11.2 for h = x^4y + xy^4, p = 5: phi(t) = t + t^4 at the critical points.
    import galois
    F = galois.GF(25)
    for t0 in F.elements:
        if t0 != 0 and t0 ** 3 == 1:
            print('t0', int(t0), "phi'(t0) =", int(F(1) + F(4) * t0 ** 3), " phi''(t0)/2 =", int(F(6) * t0 ** 2))
