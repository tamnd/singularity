import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Targeted search for increases of the intrinsic omega under permissible centres along which omega is constant
# (the analogue of the jumping phenomenon of Cossart-Piltant, Theorem 3.13).
# f = (z^p + F)^2 + G, F a sum of terms x^(p alpha + beta), G a small rigid or q-part perturbation.
# usage: python3 t_jump.py p n seed
import sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *

def rand_F(ctx, rng):
    p = ctx.p
    F = {}
    for _ in range(rng.randint(1, 4)):
        while True:
            al = [rng.randint(0, 2) for _ in range(3)]
            be = [rng.choice([0, 0, 0, 1, 2]) for _ in range(3)]
            e = [p * x + y for x, y in zip(al, be)]
            if p <= sum(e) <= 3 * p + 2:
                break
        F = add(F, mono(e, rng.randint(1, p - 1)), p)
    return F

def rand_G(ctx, rng):
    p, m = ctx.p, ctx.m
    i = rng.choice(ctx.rigid + [m, m])
    d = rng.randint(i + 1, i + 2 * p)
    e = [0, 0, 0]
    for _ in range(d):
        e[rng.randrange(3)] += 1
    return i, mono(e, rng.randint(1, p - 1))

def make(ctx, rng):
    p, m = ctx.p, ctx.m
    F = rand_F(ctx, rng)
    a = [{(0, 0, 0): 1}] + [{} for _ in range(m)]
    a[p] = scal(F, 2, p)
    a[m] = mul(F, F, p)
    for _ in range(rng.randint(1, 2)):
        i, g = rand_G(ctx, rng)
        a[i] = add(a[i], g, p)
    return a

def step_all(a, E, ctx, st, ex, rng, depth):
    from walk61 import choose_centre
    a, info = E_adapt(a, ctx)
    if info['conflict'] or info['capped'] or not is_fully_prepared(a, ctx):
        return
    inv = invariants(a, E, ctx)
    if inv['delta'] >= INF or inv['omega'] == 0:
        return
    st['samples'] += 1
    rule_S, kind = choose_centre(a, E, inv, ctx, 'plain')
    nxt = []
    for S in subsets():
        if not permissible(a, S, ctx):
            continue
        st['centres'] += 1
        if len(S) < 3 and generic_inv(a, E, S, ctx)['omega'] != inv['omega']:
            continue
        st['const_centres'] += 1
        for j, lam, nu, b in points_over(a, S, ctx, allnu=False):
            E2 = new_E(E, S, j, lam)
            st['pts'] += 1
            inv2 = invariants(b, E2, ctx)
            nxt.append((b, E2))
            if wsolvable(b, W_XI, ctx) is not None:
                st['notprep'] += 1
            if omega(b, E2, ctx) > inv['omega']:
                st['zprime_up'] += 1
            if inv2['omega'] > inv['omega']:
                st['up'] += 1
                isrule = (S == rule_S)
                st['up_rule'] += isrule
                if len(ex) < 10:
                    ex.append(dict(rule=isrule, kind=kind, a=[fmt(x) for x in a[1:]], E=sorted(E), S=S, j=j, lam=lam,
                                   om=str(inv['omega']), d=str(inv['delta']), mu={k: str(v) for k, v in inv['mu'].items()}, reg=inv['regime'],
                                   om_z=str(omega(b, E2, ctx)), om2=str(inv2['omega']), d2=str(inv2['delta']),
                                   mu2={k: str(v) for k, v in inv2['mu'].items()}, E2=sorted(E2), reg2=inv2['regime']))
    if depth > 1 and nxt:
        b, E2 = rng.choice(nxt)
        if sum(len(x) for x in b) < 300:
            step_all(b, E2, ctx, st, ex, rng, depth - 1)

def main(p, n, seed, depth=1):
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(samples=0, centres=0, const_centres=0, pts=0, up=0, up_rule=0, zprime_up=0, notprep=0)
    ex = []
    for _ in range(n):
        a = make(ctx, rng)
        if not is_mult_m(a, ctx):
            continue
        E = frozenset(k for k in range(3) if rng.random() < 0.5)
        step_all(a, E, ctx, st, ex, rng, depth)
    print(f"p={p} depth={depth}", st)
    for e in ex:
        print('EX', e)

def main_old(p, n, seed):
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(samples=0, centres=0, const_centres=0, pts=0, up=0, up_rule=0, zprime_up=0, notprep=0)
    ex = []
    for _ in range(n):
        a = make(ctx, rng)
        if not is_mult_m(a, ctx):
            continue
        E = frozenset(k for k in range(3) if rng.random() < 0.5)
        a, info = E_adapt(a, ctx)
        if info['conflict'] or info['capped'] or not is_fully_prepared(a, ctx):
            continue
        inv = invariants(a, E, ctx)
        if inv['delta'] >= INF or inv['omega'] == 0:
            continue
        st['samples'] += 1
        from walk61 import choose_centre
        rule_S, kind = choose_centre(a, E, inv, ctx, 'plain')
        for S in subsets():
            if not permissible(a, S, ctx):
                continue
            st['centres'] += 1
            if len(S) < 3 and generic_inv(a, E, S, ctx)['omega'] != inv['omega']:
                continue
            st['const_centres'] += 1
            for j, lam, nu, b in points_over(a, S, ctx, allnu=False):
                E2 = new_E(E, S, j, lam)
                st['pts'] += 1
                inv2 = invariants(b, E2, ctx)
                if wsolvable(b, W_XI, ctx) is not None:
                    st['notprep'] += 1
                if omega(b, E2, ctx) > inv['omega']:
                    st['zprime_up'] += 1
                if inv2['omega'] > inv['omega']:
                    st['up'] += 1
                    isrule = (S == rule_S)
                    st['up_rule'] += isrule
                    if len(ex) < 10:
                        ex.append(dict(rule=isrule, kind=kind, a=[fmt(x) for x in a[1:]], E=sorted(E), S=S, j=j, lam=lam,
                                       om=str(inv['omega']), d=str(inv['delta']), mu={k: str(v) for k, v in inv['mu'].items()}, reg=inv['regime'],
                                       om_z=str(omega(b, E2, ctx)), om2=str(inv2['omega']), d2=str(inv2['delta']),
                                       mu2={k: str(v) for k, v in inv2['mu'].items()}, E2=sorted(E2), reg2=inv2['regime']))
    print(f"p={p}", st)
    for e in ex:
        print('EX', e)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 1)
