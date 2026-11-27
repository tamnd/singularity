import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Greedy minimisation of the jump example B of data/jump.txt (Example 61.11).
import sys, ast
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
ctx = Ctx(3); p = 3; m = 6
L = [l for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'jump.txt')) if l.startswith('EX')]
d = ast.literal_eval(L[int(sys.argv[1]) if len(sys.argv) > 1 else 4][3:])
def parse(s):
    P = {}
    if s.strip() == '0': return P
    for t in s.split(' + '):
        c, e = t.split('*x^')
        P[ast.literal_eval(e)] = int(c)
    return P
a = [{(0, 0, 0): 1}] + [parse(s) for s in d['a']]
E = frozenset(d['E']); S = tuple(d['S'])
def jump(a):
    if not is_mult_m(a, ctx): return None
    half = scal(a[p], pow(2, p - 2, p), p)
    if not any(a[i] for i in ctx.rigid) and clean(add(a[m], scal(mul(half, half, p), -1, p), p), p) == {}: return None
    if KEEP_OM and invariants(a, E, ctx)['omega'] == 0: return None
    if not is_fully_prepared(a, ctx): return None
    if not permissible(a, S, ctx): return None
    inv = invariants(a, E, ctx)
    if inv['delta'] >= INF: return None
    if len(S) < 3 and generic_inv(a, E, S, ctx)['omega'] != inv['omega']: return None
    for j, lam, nu, b in points_over(a, S, ctx, allnu=False):
        E2 = new_E(E, S, j, lam)
        i2 = invariants(b, E2, ctx)
        if i2['omega'] > inv['omega']:
            return (inv, j, lam, E2, i2, omega(b, E2, ctx))
    return None
KEEP_OM = len(sys.argv) > 2
assert jump(a)
changed = True
while changed:
    changed = False
    for i in range(1, m + 1):
        for e in list(a[i]):
            b = [dict(x) for x in a]; del b[i][e]
            if jump(b):
                a = b; changed = True
print('S', S, 'E', sorted(E))
for i in range(1, m + 1):
    if a[i]: print(f'a_{i} =', fmt(a[i]))
inv, j, lam, E2, i2, wz = jump(a)
print('xi:', inv['regime'], 'delta', inv['delta'], 'mu', {k: str(v) for k, v in inv['mu'].items()}, 'omega', inv['omega'])
print('generic point of centre omega', generic_inv(a, E, S, ctx)['omega'] if len(S) < 3 else '-')
print("xi': chart", j, 'lam', lam, 'E2', sorted(E2), 'omega in z\'', wz, 'intrinsic', i2['omega'], 'delta', i2['delta'], 'mu', {k: str(v) for k, v in i2['mu'].items()}, i2['regime'])
for jj, lam2, nu, b in points_over(a, S, ctx, allnu=False):
    if jj == j and lam2 == lam:
        print("transform coefficients:")
        for i in range(1, m + 1):
            if b[i]: print(f"  a'_{i} =", fmt(b[i]))
        print("  vertex at xi' solvable by", wsolvable(b, W_XI, ctx))
