import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Random tests: nu-lemma (Lemma 3.3), Proposition 4.2, re-adaptation effects, weak transform bound.
import sys, random
from lib53 import *

def rand_poly(ctx, S, i, rng, nterms, extra):
    P = {}
    for _ in range(nterms):
        while True:
            e = [rng.randint(0, i + extra) for _ in range(3)]
            sS = sum(e[k] for k in S)
            if sS >= i and sum(e) <= i + extra:
                break
        P = add(P, mono(e, rng.randint(1, ctx.p - 1)), ctx.p)
    return P

def gen(ctx, rng, fam):
    S = tuple(sorted(rng.sample(range(3), rng.randint(1, 3))))
    m, p = ctx.m, ctx.p
    a = [{(0, 0, 0): 1}] + [{} for _ in range(m)]
    if fam == 'gen':
        for i in range(1, m + 1):
            if rng.random() < 0.35:
                a[i] = rand_poly(ctx, S, i, rng, rng.randint(1, 2), rng.randint(0, 3))
        if not a[m]:
            a[m] = rand_poly(ctx, S, m, rng, 1, rng.randint(0, 4))
    else:  # 'pow': (z^p + g)^2 + rigid perturbation
        g = rand_poly(ctx, S, p, rng, rng.randint(1, 2), rng.randint(0, 3))
        a[p] = scal(g, 2, p)
        a[m] = add(mul(g, g, p), rand_poly(ctx, S, m, rng, 1, rng.randint(1, 4)), p)
        i = rng.choice(ctx.rigid)
        a[i] = rand_poly(ctx, S, i, rng, 1, rng.randint(0, 3))
    # hidden translation in (x_S): linear + quadratic part
    h = {}
    for k in S:
        if rng.random() < 0.6:
            e = [0, 0, 0]; e[k] = 1
            h = add(h, mono(e, rng.randint(1, p - 1)), p)
    if rng.random() < 0.4:
        k = rng.choice(S); e = [0, 0, 0]; e[k] = 1; e[rng.randrange(3)] += 1
        h = add(h, mono(e, rng.randint(1, p - 1)), p)
    a = translate(a, h, ctx)
    return a, S

def omega_const(a, E, S, ctx):
    mu = mus(a, set(E) & set(S), ctx)
    dS = min(Fr(ordS(a[i], S), i) for i in range(1, ctx.m + 1) if a[i])
    return dS - sum(mu.values(), Fr(0)) == omega(a, E, ctx)

def run(p, n, fam, seed):
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(samples=0, raw_nu=0, raw_nu_v0_in_U=0, raw_nonadapted=0, pts=0, nu_bad=0,
              hyp_pts=0, hyp_up=0, nohyp_pts=0, nohyp_up=0, readapt_up=0, readapt_up_R1=0,
              readapt_up_R2=0, readapt_up_R3=0, lin_adapt=0, lin_adapt_mu_change=0, prep_pts=0)
    examples = []
    for _ in range(n):
        a, S = gen(ctx, rng, fam)
        if not any(a[i] for i in range(1, ctx.m + 1)):
            continue
        st['samples'] += 1
        T = tangent_cone(a, ctx)
        if not is_adapted(a, ctx):
            st['raw_nonadapted'] += 1
        for j, lam, nu, b in points_over(a, S, ctx):
            if nu:
                st['raw_nu'] += 1
                v = [0, 0, 0, nu]; v[j] = 1
                for k, l in lam.items():
                    v[k] = l
                if in_U(T, v, p):
                    st['raw_nu_v0_in_U'] += 1
        try:
            a2, nprep, lin = adapt(a, ctx)
        except RuntimeError:
            continue
        assert is_adapted(a2, ctx)
        if not any(a2[i] for i in range(1, ctx.m + 1)):
            continue
        E = frozenset(k for k in range(3) if rng.random() < 0.5)
        w0 = omega(a2, E, ctx)
        for S2 in subsets():
            if not permissible(a2, S2, ctx):
                continue
            hyp = omega_const(a2, E, S2, ctx)
            for j, lam, nu, b in points_over(a2, S2, ctx):
                st['pts'] += 1
                if nu:
                    st['nu_bad'] += 1
                    examples.append(('nu', a2, S2, j, lam, nu))
                    continue
                E2 = new_E(E, S2, j, lam)
                w1 = omega(b, E2, ctx)
                if hyp:
                    st['hyp_pts'] += 1
                    if w1 > w0:
                        st['hyp_up'] += 1
                        examples.append(('hyp_up', a2, E, S2, j, lam, w0, w1))
                else:
                    st['nohyp_pts'] += 1
                    if w1 > w0:
                        st['nohyp_up'] += 1
                        if len([x for x in examples if x[0] == 'nohyp_up']) < 2:
                            examples.append(('nohyp_up', a2, E, S2, j, lam, w0, w1))
                try:
                    b2, np2, lin2 = adapt(b, ctx)
                except RuntimeError:
                    continue
                if np2:
                    st['prep_pts'] += 1
                if lin2:
                    st['lin_adapt'] += 1
                    if mus(b2, E2, ctx) != mus(b, E2, ctx):
                        st['lin_adapt_mu_change'] += 1
                w2 = omega(b2, E2, ctx)
                if hyp and w2 > w0:
                    st['readapt_up'] += 1
                    r = regime(b2, ctx)
                    st['readapt_up_' + r] += 1
                    if len([x for x in examples if x[0] == 'readapt']) < 3:
                        examples.append(('readapt', a2, E, S2, j, lam, w0, w1, w2, r, slopes(b, ctx), slopes(b2, ctx), np2, lin2))
    return st, examples

def weak_transform_test(p, n, seed):
    """[S] fact: ord of x_j^{-c} pi^* I at points over xi is <= c when ord_C I = ord_xi I = c."""
    ctx = Ctx(p)
    rng = random.Random(seed)
    bad = tested = 0
    for _ in range(n):
        S = tuple(sorted(rng.sample(range(3), rng.randint(2, 3))))
        c = rng.randint(1, 5)
        gens = [rand_poly(ctx, S, c, rng, rng.randint(1, 3), rng.randint(0, 3)) for _ in range(rng.randint(1, 2))]
        if min(ordS(g, S) for g in gens) != c or min(ordp(g) for g in gens) != c:
            continue
        for j in S:
            others = [k for k in S if k != j]
            for lv in product(range(p), repeat=len(others)):
                lam = {k: lv[t] for t, k in enumerate(others)}
                o = INF
                for g in gens:
                    # reuse blowup with g placed as a_c and permissibility in degree c only
                    a = [{(0, 0, 0): 1}] + [{} for _ in range(ctx.m)]
                    a[c] = g
                    bb = blowup(a, S, j, lam, 0, ctx)
                    o = min(o, ordp(bb[c]))
                tested += 1
                if o > c:
                    bad += 1
    return tested, bad

if __name__ == '__main__':
    p = int(sys.argv[1]); n = int(sys.argv[2]); fam = sys.argv[3]
    st, ex = run(p, n, fam, 1000 + p)
    print(f"p={p} fam={fam}", st)
    for e in ex[:8]:
        print('  ', e[0], [fmt(x) for x in e[1][1:]] if isinstance(e[1], list) else '', e[2:])
    if fam == 'gen':
        print('weak transform', weak_transform_test(p, 300, 7 + p))

def rule51(a, E, ctx):
    io = iota(a, E, ctx)
    cands = []
    for S in subsets():
        if permissible(a, S, ctx) and (len(S) == 3 or iota_generic(a, E, S, ctx) == io):
            mu = mus(a, set(E) & set(S), ctx)
            cands.append((len(S), -sum(mu.values(), Fr(0)), S))
    cands.sort()
    return cands[0][2]

def walks(p, n, fam, seed, depth=12):
    """Rule 5.1 walks; records omega in z' and after re-adaptation, and linear adaptations."""
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(walks=0, pts=0, nu_bad=0, zprime_up=0, re_up=0, re_up_by_regime={}, lin=0, lin_omega_up=0,
              lin_omega_down=0, class_up=0, drops=0)
    ex = []
    for _ in range(n):
        a, S = gen(ctx, rng, fam)
        try:
            a, _, _ = adapt(a, ctx)
        except RuntimeError:
            continue
        if not any(a[i] for i in range(1, ctx.m + 1)):
            continue
        E = frozenset()
        st['walks'] += 1
        for t in range(depth):
            S = rule51(a, E, ctx)
            io = iota(a, E, ctx)
            pts = points_over(a, S, ctx)
            if not pts:
                st['drops'] += 1
                break
            j, lam, nu, b = rng.choice(pts)
            st['pts'] += 1
            if nu:
                st['nu_bad'] += 1
            E2 = new_E(E, S, j, lam)
            w1 = omega(b, E2, ctx)
            if w1 > io[1]:
                st['zprime_up'] += 1
            try:
                b2, np2, lin2 = adapt(b, ctx)
            except RuntimeError:
                break
            w2 = omega(b2, E2, ctx)
            if lin2:
                st['lin'] += 1
                if w2 > w1: st['lin_omega_up'] += 1
                if w2 < w1: st['lin_omega_down'] += 1
            io2 = iota(b2, E2, ctx)
            if io2[0] > io[0]:
                st['class_up'] += 1
            if io2[0] == io[0] and w2 > io[1]:
                st['re_up'] += 1
                r = regime(b2, ctx)
                st['re_up_by_regime'][r] = st['re_up_by_regime'].get(r, 0) + 1
                if len(ex) < 3:
                    ex.append((regime(a, ctx), slopes(a, ctx), io, slopes(b, ctx), w1, r, slopes(b2, ctx), w2, np2, lin2, [fmt(x) for x in a[1:]], sorted(E), S, j, lam))
            a, E = b2, E2
            if sum(len(x) for x in a) > 400:
                break
    return st, ex

if __name__ == '__main__' and len(sys.argv) > 4:
    st, ex = walks(p, int(sys.argv[4]), fam, 77 + p)
    print('walks', st)
    for e in ex:
        print('   re_up', e)
