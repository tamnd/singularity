import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Check (not a jump): f = (z^p + F)^2 + x0^N with F = x1 x2^(p-1) (x0^p + x1^p + x2^p), E = {1, 2}.
# The only permissible centre is the point; Rule 61.9 takes it and the intrinsic omega drops (2 to 2 - 1/p).
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from walk61 import choose_centre, iota_of
for p in (3, 5, 7):
    ctx = Ctx(p); m = ctx.m
    F = mul(mono((0, 1, p - 1)), add(add(mono((p, 0, 0)), mono((0, p, 0)), p), mono((0, 0, p)), p), p)
    N = 10 * p
    a = [{(0, 0, 0): 1}] + [{} for _ in range(m)]
    a[p] = scal(F, 2, p); a[m] = add(mul(F, F, p), mono((N, 0, 0)), p)
    E = frozenset({1, 2})
    b0, info = E_adapt(a, ctx)
    print(f"p={p}: coordinate unchanged by E-adaptation: {b0 == a}, fully prepared: {is_fully_prepared(a, ctx)}, adapted: {is_adapted(a, ctx)}")
    inv = invariants(a, E, ctx)
    S, kind = choose_centre(a, E, inv, ctx, 'plain')
    perm = [T for T in subsets() if permissible(a, T, ctx)]
    gens = {T: str(generic_inv(a, E, T, ctx)['omega']) for T in perm if len(T) < 3}
    print(f"   at xi: regime {inv['regime']} delta {inv['delta']} mu {dict((k, str(v)) for k, v in inv['mu'].items())} omega {inv['omega']}; permissible {perm}, omega at generic points {gens}; rule centre {S} ({kind})")
    worst = None
    for j, lam, nu, b in points_over(a, S, ctx, allnu=True):
        E2 = new_E(E, S, j, lam)
        i2 = invariants(b, E2, ctx)
        wz = omega(b, E2, ctx)
        if worst is None or i2['omega'] > worst[0]:
            worst = (i2['omega'], j, lam, nu, sorted(E2), wz, i2['delta'], dict((k, str(v)) for k, v in i2['mu'].items()), i2['regime'])
    print(f"   max over points of multiplicity {m}: omega* = {worst[0]} at chart x{worst[1]}, lam {worst[2]}, nu {worst[3]}, E' {worst[4]}; omega in z' = {worst[5]}; delta* = {worst[6]}, mu* = {worst[7]}, {worst[8]}")
