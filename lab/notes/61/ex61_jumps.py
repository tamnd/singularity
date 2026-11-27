import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Examples 61.10 and 61.11 (p = 3): the intrinsic omega increases under a permissible centre along which omega is constant.
# For each: the jump at the named centre, and the behaviour at every point over the centre chosen by Rule 61.9.
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from walk61 import choose_centre
ctx = Ctx(3)
EXS = {
 '61.10 (curve centre)': ([(3, (0, 2, 4), 2), (4, (3, 5, 5), 2), (6, (0, 4, 8), 1)], {1, 2}, (1, 2)),
 '61.11 (point centre)': ([(3, (1, 3, 2), 1), (6, (2, 6, 4), 1), (6, (8, 4, 14), 1)], {0, 1, 2}, (0, 1, 2)),
}
for name, (terms, E, S0) in EXS.items():
    a = mk(ctx, terms); E = frozenset(E)
    inv = invariants(a, E, ctx)
    print(name, 'prepared', is_fully_prepared(a, ctx), 'omega', inv['omega'], 'delta', inv['delta'], 'mu', {k: str(v) for k, v in inv['mu'].items()})
    rule, kind = choose_centre(a, E, inv, ctx, 'plain')
    for S in (S0, rule):
        ups = []
        for j, lam, nu, b in points_over(a, S, ctx, allnu=False):
            E2 = new_E(E, S, j, lam); i2 = invariants(b, E2, ctx)
            ups.append((str(i2['omega']), str(omega(b, E2, ctx)), j, lam))
        tag = 'rule centre (%s)' % kind if S == rule else 'test centre'
        print('  ', tag, S, 'max intrinsic omega over points', max(u[0] for u in ups) if ups else None, 'points', ups)
