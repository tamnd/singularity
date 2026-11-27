import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Search for a cycle of Rule 61.9 on Example 5.4 of note 51 (p = 3): states (coefficients, E) that recur.
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from walk61 import choose_centre, iota_of
p = int(sys.argv[1]) if len(sys.argv) > 1 else 3
ctx = Ctx(p); m = ctx.m
MODE = sys.argv[3] if len(sys.argv) > 3 else 'plain'
c = int(sys.argv[2]) if len(sys.argv) > 2 else 0
a = mk(ctx, [(2, (2, 0, 1), 1), (m, (0, 2 * p + 1, c), 1)]); E = frozenset([2]) if c else frozenset()
def key(a, E):
    return (tuple(tuple(sorted(x.items())) for x in a), E)
a, _ = E_adapt(a, ctx)
frontier = [(a, E, [])]
seen = {}
for depth in range(int(sys.argv[4]) if len(sys.argv) > 4 else 10):
    nf = []
    for a, E, hist in frontier:
        inv = invariants(a, E, ctx)
        S, kind = choose_centre(a, E, inv, ctx, MODE)
        io = iota_of(inv, E, MODE)
        k = key(a, E)
        h = hist + [(sorted(E), inv['regime'], str(io[1]), S, kind, fmt(a[2]), fmt(a[m]))]
        if k in seen:
            print('CYCLE of length', len(h) - 1 - seen[k], 'after', seen[k], 'steps')
            for x in h[seen[k]:]: print('  ', x)
            sys.exit()
        seen[k] = len(h) - 1
        for j, lam, nu, b in points_over(a, S, ctx, allnu=False):
            E2 = new_E(E, S, j, lam)
            b, info = E_adapt(b, ctx)
            if iota_of(invariants(b, E2, ctx), E2, MODE) == io and sum(len(x) for x in b) < 60:
                nf.append((b, E2, h))
    frontier = nf
    print('depth', depth, 'frontier', len(frontier))
