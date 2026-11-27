"""Checks of the named examples of note 55."""
import random, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prep import *
from cert import crit_points_n2, crit_points_n3, covers
rng = random.Random(0)
ex = {
 'fano p=2': (2, 3, (1, 1, 1), 4, {(2, 1, 1): 1, (1, 2, 1): 1, (1, 1, 2): 1}),
 'p=3 x^5y+xy^5': (3, 2, (1, 1), 6, {(5, 1): 1, (1, 5): 1}),
 'p=5 x^4y+xy^4': (5, 2, (1, 1), 5, {(4, 1): 1, (1, 4): 1}),
 'p=3 weight (2,3)': (3, 2, (2, 3), 12, {(3, 2): 1, (0, 4): 1}),
}
for name, (p, n, wt, D, h) in ex.items():
    print(name, 'resonant', resonant(h, p, n), 'torus crit', has_torus_crit(h, p, n),
          'off zero', has_torus_crit(h, p, n, True))
    # classical condition: no torus singular point of {h = 0}
    hs = to_sym(h, n)
    gens = [to_sym(deriv(h, i, p), n) for i in range(n)] + [hs]
    mon = 1
    for v in XS[:n]: mon *= v
    G = groebner([g for g in gens if g != 0] + [1 - T * mon], T, *XS[:n], modulus=p, order='grevlex')
    print('   {h=0} smooth in torus:', G.exprs == [1])
    for f in faces(h, wt, n):
        if len(f) < len(h):
            print('   proper face', sorted(f), 'torus crit', has_torus_crit(f, p, n))
    if wt in ((1, 1), (1, 1, 1)):
        if n == 2:
            print('   crit points in P^1:', crit_points_n2(h, p))
        else:
            F, pts = crit_points_n3(h, p)
            print('   crit points in P^2 over F_%d:' % F.q, pts, ' covers:', len(covers(F, pts)))
    k, im, g, tr = prepare(h, wt, D, p, n, rng)
    print('   F_p search:', k, tr)
