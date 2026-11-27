import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Single-point tests for note 61:
#  T1 invariance of omega* under z -> u z + c and under base changes x_t -> x_t + g (t not in E), x_k -> x_k (1 + h) (k in E)
#  T2 Lemma 61.6: delta-prepared and E_+ nonempty implies adapted
#  T3 Lemma 61.4: the simultaneous preparation realises delta*, all mu_k^* and delta*(eta_C)
#  T4 Proposition 61.7: delta and omega at generic points of regular curves and surfaces through xi
#     (coordinate ones and images of coordinate ones under random base changes)
import sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from t_random import gen as gen53

def compose(P, t, g, ctx, mult=False):
    """substitute x_t -> x_t + g (mult False) or x_t -> x_t * (1 + g) (mult True)."""
    p = ctx.p
    base = add(mono(ek(t)), g, p) if not mult else mul(mono(ek(t)), add({(0, 0, 0): 1}, g, p), p)
    out = {}
    cache = {0: {(0, 0, 0): 1}}
    for e, c in P.items():
        n = e[t]
        if n not in cache:
            cache[n] = pw(base, n, p)
        rest = list(e); rest[t] = 0
        out = add(out, mul(mono(rest, c), cache[n], p), p)
    return out

def base_change(a, t, g, ctx, mult=False):
    return [a[0]] + [compose(x, t, g, ctx, mult) for x in a[1:]]

def unit_z(a, u, ctx):
    """coefficients of u^{-m} f(u z) for a constant unit u: a_i -> u^{-i} a_i."""
    p = ctx.p
    return [a[0]] + [scal(a[i], pow(u, -i, p), p) for i in range(1, ctx.m + 1)]

def rand_g(ctx, rng, avoid, deg=(1, 3)):
    p = ctx.p
    g = {}
    for _ in range(rng.randint(1, 2)):
        while True:
            e = [rng.randint(0, 2) for _ in range(3)]
            if e[avoid] == 0 and deg[0] <= sum(e) <= deg[1]:
                break
        g = add(g, mono(e, rng.randint(1, p - 1)), p)
    return g

def main(p, n, fam, seed):
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(samples=0, T1=0, T1_bad=0, T2=0, T2_bad=0, T3=0, T3_bad=0, T4=0, T4_delta_bad=0, T4_omega_bad=0,
              T4_curves=0, T4_moved=0, capped=0)
    bad = []
    for _ in range(n):
        a, S = gen53(ctx, rng, fam)
        if not any(a[i] for i in range(1, ctx.m + 1)):
            continue
        E = frozenset(k for k in range(3) if rng.random() < 0.5)
        st['samples'] += 1
        if wdelta(a, W_XI, ctx)[1]:
            st['capped'] += 1
            continue
        om = omega_star(a, E, ctx)
        # T1
        for _ in range(3):
            c = rand_g(ctx, rng, avoid=rng.randrange(3), deg=(1, 4))
            b = translate(unit_z(a, rng.randint(1, p - 1), ctx), c, ctx)
            kind = rng.randrange(3)
            if kind == 1:
                t = rng.choice([k for k in range(3) if k not in E] or [None])
                if t is not None:
                    b = base_change(b, t, rand_g(ctx, rng, avoid=t, deg=(1, 3)), ctx)
            elif kind == 2 and E:
                k = rng.choice(sorted(E))
                b = base_change(b, k, rand_g(ctx, rng, avoid=-1, deg=(1, 2)), ctx, mult=True)
            st['T1'] += 1
            if omega_star(b, E, ctx) != om:
                st['T1_bad'] += 1
                bad.append(('T1', [fmt(x) for x in a[1:]], sorted(E), str(om), str(omega_star(b, E, ctx))))
        # T3
        b, nst, capped = full_prepare(a, ctx)
        if capped:
            st['capped'] += 1
            continue
        st['T3'] += 1
        ok = slopes(b, ctx)[2] == delta_star(a, ctx)
        for k in range(3):
            ok &= min((Fr(ordv(b[i], k), i) for i in range(1, ctx.m + 1) if b[i]), default=Fr(INF)) == mu_star(a, k, ctx)
        for SS in ((0, 1), (0, 2), (1, 2)):
            ok &= wslopes(b, wS(SS), ctx)[2] == wdelta(a, wS(SS), ctx)[0]
        if not ok:
            st['T3_bad'] += 1
            bad.append(('T3', [fmt(x) for x in a[1:]]))
        # T2
        Eplus = [k for k in E if min((Fr(ordv(b[i], k), i) for i in range(1, ctx.m + 1) if b[i]), default=Fr(INF)) > 0]
        if Eplus:
            st['T2'] += 1
            if not is_adapted(b, ctx):
                st['T2_bad'] += 1
                bad.append(('T2', [fmt(x) for x in b[1:]], sorted(E)))
        # T4: generic points of V(x_S) in Max, after an optional base change that fixes V(x_k), k in E
        d0 = delta_star(a, ctx)
        for SS in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
            for moved in (False, True):
                bb = a
                if moved:
                    free = [t for t in SS if t not in E]
                    if not free:
                        continue
                    t = free[0]
                    bb = base_change(a, t, rand_g(ctx, rng, avoid=t, deg=(1, 3)), ctx)
                g = generic_inv(bb, E, SS, ctx)
                if g['delta'] < 1:
                    continue
                st['T4'] += 1
                st['T4_curves'] += len(SS) == 2
                st['T4_moved'] += moved
                if g['delta'] > delta_star(bb, ctx):
                    st['T4_delta_bad'] += 1
                if g['omega'] > omega_star(bb, E, ctx):
                    st['T4_omega_bad'] += 1
                    bad.append(('T4', [fmt(x) for x in bb[1:]], sorted(E), SS, moved, str(g['omega']), str(omega_star(bb, E, ctx))))
    print(f"p={p} fam={fam}", st)
    for x in bad[:6]:
        print('  BAD', x)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
