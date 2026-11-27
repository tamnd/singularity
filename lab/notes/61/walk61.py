import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Walks under the intrinsic Rule 6.0 (Rule 61.9 of note 61).
# usage: python3 walk61.py p nwalks depth family seed clsmode
#   family: gen | pow | ex52 | ex53 | ex54 | ex536 | ex45 | ex46 | t44a | t44b | t44c | f1 | ex533
#   clsmode: plain | res | om (om: the main step asks only that omega be constant along the centre)
import sys, random, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from t_random import gen as gen53

def family(fam, ctx, rng):
    p, m = ctx.p, ctx.m
    if fam in ('gen', 'pow'):
        a, S = gen53(ctx, rng, fam)
        return a, frozenset()
    ex = {
        'ex52': ([(1, (1, 1, 0), 1), (m, (2 * p - 1, 2 * p, 0), 1)], {0, 1}),
        'ex53': ([(2, (2, 1, 0), 1), (m, (2 * p, 1, 0), 1)], {1}),
        'ex54': ([(2, (2, 0, 1), 1), (m, (0, 2 * p + 1, 0), 1)], set()),
        'ex536': ([(2, (p, 0, 0), 1), (2, (0, p, 0), 1), (2, (0, 0, p + 1), 1), (m, (0, 0, p * p + 1), 1)], set()),
        'ex45': ([(1, (3, 0, 0), 1), (m, (0, 4 * p + 1, 0), 1)], set()),
        'ex46': ([(1, (1, 0, 0), 1), (m, (0, 2 * p + 1, 0), 1)], set()),
        't44a': ([(1, (1, 0, 0), 1), (m, (2 * p + 1, 0, 0), 1)], set()),
        't44b': ([(1, (2, 0, 0), 1), (m, (4 * p + 1, 0, 0), 1)], set()),
        't44c': ([(1, (3, 0, 0), 1), (m, (6 * p + 1, 0, 0), 1)], set()),
        'f1': ([(1, (0, 2, 0), 1), (m, (5 * p, 0, 0), 1)], set()),
        'ex533': ([(m, (2 * p, 2 * p, 0), 1), (m, (2 * p, 0, 2 * p + 1), 1)], {0}),
    }[fam]
    a = mk(ctx, ex[0])
    if rng.random() < 0.5 and fam not in ('ex533',):
        # hide the example by a random translation of order >= 2
        h = {}
        for _ in range(2):
            e = [0, 0, 0]; e[rng.randrange(3)] += 1; e[rng.randrange(3)] += 1
            h = add(h, mono(e, rng.randint(1, p - 1)), p)
        a = translate(a, h, ctx)
    return a, frozenset(ex[1])

def iota_of(inv, E, mode):
    if mode == 'om':
        return (0, inv['omega'])
    c = cls_plain(inv) if mode == 'plain' else cls_res(inv, E)
    return (c, inv['omega'])

def generic_iota(a, E, S, ctx, mode):
    g = generic_inv(a, E, S, ctx)
    if mode == 'om':
        c = 0
    elif mode == 'plain':
        c = 0 if g['regime'] == 'R2' else 1
    else:
        smu = sum((mu_star(a, k, ctx) for k in E if k in S), Fr(0))
        c = 0 if (g['sigma'] - smu <= 1 and g['sigma'] <= g['D']) else 1
    return (c, g['omega']), g

def choose_centre(a, E, inv, ctx, mode):
    """a is fully prepared and adapted, so mu_k(z) = mu_k^* and permissibility is read in z."""
    mu = inv['mu']
    divs = [(k,) for k in range(3) if permissible(a, (k,), ctx)]
    if divs:
        divs.sort(key=lambda S: (-(mu[S[0]] if S[0] in E else -1), S))
        return divs[0], 'div'
    perm = [S for S in subsets() if permissible(a, S, ctx)]
    if inv['omega'] == 0:
        perm.sort(key=lambda S: (len(S), -sum((mu[k] for k in E if k in S), Fr(0)), S))
        return perm[0], 'mono'
    io = iota_of(inv, E, mode)
    cands = []
    for S in perm:
        if len(S) == 3 or generic_iota(a, E, S, ctx, mode)[0] == io:
            cands.append((len(S), -sum((mu[k] for k in E if k in S), Fr(0)), S))
    cands.sort()
    return cands[0][2], 'main'

def size(a):
    return sum(len(x) for x in a)

def walk(a, E, ctx, rng, depth, mode, st, exs, checknu=False):
    a, info = E_adapt(a, ctx)
    if info['conflict'] or info['capped']:
        st['conflict'] += 1
        return
    inv = invariants(a, E, ctx)
    run_eq = 0
    for t in range(depth):
        if not any(a[i] for i in range(1, ctx.m + 1)):
            st['ends_smooth_or_z'] += 1
            return
        S, kind = choose_centre(a, E, inv, ctx, mode)
        st['steps_' + kind] += 1
        io = iota_of(inv, E, mode)
        gi = generic_inv(a, E, S, ctx) if len(S) < 3 else None
        const = (gi is None) or gi['omega'] == inv['omega']
        pts = points_over(a, S, ctx, allnu=checknu)
        if checknu:
            st['nu_bad'] += sum(1 for x in pts if x[2])
        pts = [x for x in pts if not x[2]]
        if not pts:
            st['drops'] += 1
            st['len_hist'][t] = st['len_hist'].get(t, 0) + 1
            return
        nxt = None
        for (j, lam, nu, b) in pts:
            E2 = new_E(E, S, j, lam)
            st['pts'] += 1
            wz = omega(b, E2, ctx)          # omega in z' (note 51)
            zprep = wsolvable(b, W_XI, ctx) is None
            inv2 = invariants(b, E2, ctx)   # intrinsic
            io2 = iota_of(inv2, E2, mode)
            if const and wz > inv['omega']:
                st['zprime_up_const'] += 1
            if inv2['omega'] > inv['omega']:
                key = 'om_up_' + kind + ('_const' if const else '_nonconst') + ('_zprep' if zprep else '_znotprep')
                st[key] = st.get(key, 0) + 1
                if len(exs) < 12:
                    exs.append(dict(kind=kind, const=const, zprep=zprep, p=ctx.p, a=[fmt(x) for x in a[1:]], E=sorted(E), S=S, j=j, lam=lam,
                                    om=str(inv['omega']), om_z=str(wz), om2=str(inv2['omega']), reg=inv['regime'], reg2=inv2['regime'],
                                    delta=str(inv['delta']), delta2=str(inv2['delta'])))
            if io2 > io:
                st['iota_up_' + kind] += 1
            if not zprep:
                st['zprime_not_prep'] += 1
                st['notprep_regime_' + inv2['regime']] = st.get('notprep_regime_' + inv2['regime'], 0) + 1
            if inv['regime'] != 'R1' and inv2['regime'] == 'R1':
                st['to_R1'] += 1
        j, lam, nu, b = rng.choice(pts)
        E2 = new_E(E, S, j, lam)
        b, info = E_adapt(b, ctx)
        if info['conflict'] or info['capped']:
            st['conflict'] += 1
            return
        if info['lin']:
            st['lin'] += 1
        inv2 = invariants(b, E2, ctx)
        if iota_of(inv2, E2, mode) == io:
            run_eq += 1
        else:
            run_eq = 0
        st['max_eq_run'] = max(st['max_eq_run'], run_eq)
        a, E, inv = b, E2, inv2
        if size(a) > 500:
            st['size_cap'] += 1
            return
    st['depth_limit'] += 1

def main():
    p, n, depth = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    fam, seed, mode = sys.argv[4], int(sys.argv[5]), sys.argv[6]
    checknu = len(sys.argv) > 7
    ctx = Ctx(p)
    rng = random.Random(seed)
    from collections import defaultdict
    st = defaultdict(int)
    st['len_hist'] = {}
    exs = []
    for _ in range(n):
        a, E = family(fam, ctx, rng)
        if not is_mult_m(a, ctx) or not any(a[i] for i in range(1, ctx.m + 1)):
            continue
        st['walks'] += 1
        try:
            walk(a, E, ctx, rng, depth, mode, st, exs, checknu)
        except RuntimeError as e:
            st['error'] += 1
    st = dict(st)
    print(json.dumps(dict(p=p, fam=fam, mode=mode, n=n, depth=depth, stats=st), default=str))
    for e in exs:
        print('EX', json.dumps(e, default=str))

if __name__ == '__main__':
    main()
