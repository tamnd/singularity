import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Example 5.4 of note 51 under Rule 61.9 (intrinsic omega, plain class), p = 3:
# f = z^6 + x0^2 x2 z^4 + x1^7, E empty. Follows a chosen branch and prints the invariants.
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from walk61 import choose_centre, iota_of
p = int(sys.argv[1]) if len(sys.argv) > 1 else 3
ctx = Ctx(p); m = ctx.m
a = mk(ctx, [(2, (2, 0, 1), 1), (m, (0, 2 * p + 1, 0), 1)]); E = frozenset()
a, _ = E_adapt(a, ctx)
for t in range(12):
    inv = invariants(a, E, ctx)
    S, kind = choose_centre(a, E, inv, ctx, 'plain')
    print(t, 'E', sorted(E), inv['regime'], 'iota', iota_of(inv, E, 'plain'), 'mu', {k: str(v) for k, v in inv['mu'].items() if k in E}, 'centre', S, kind, '|', 'a_2 =', fmt(a[2]), ' a_m =', fmt(a[m]))
    pts = points_over(a, S, ctx, allnu=False)
    same = [(j, lam, b) for j, lam, nu, b in pts if iota_of(invariants(b, new_E(E, S, j, lam), ctx), new_E(E, S, j, lam), 'plain') == iota_of(inv, E, 'plain')]
    print('   points', len(pts), 'with the same iota', [(j, lam) for j, lam, b in same])
    if not same: break
    j, lam, b = same[-1]
    E = new_E(E, S, j, lam); a, _ = E_adapt(b, ctx)
