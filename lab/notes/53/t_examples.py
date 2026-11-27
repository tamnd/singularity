import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Prop 2.1, Examples 5.2-5.4 (Rule 5.1, own implementation), omega dependence, R3 maximal contact.
import sys
from lib53 import *

def mk(ctx, terms):
    a = [{(0, 0, 0): 1}] + [{} for _ in range(ctx.m)]
    for i, e, c in terms:
        a[i] = add(a[i], mono(e, c), ctx.p)
    return a

def rule51(a, E, ctx):
    """Rule 5.1: largest-dimensional permissible coordinate centre through the origin with iota constant."""
    io = iota(a, E, ctx)
    cands = []
    for S in subsets():
        if permissible(a, S, ctx) and (len(S) == 3 or iota_generic(a, E, S, ctx) == io):
            mu = mus(a, set(E) & set(S), ctx)
            cands.append((len(S), -sum(mu.values(), Fr(0)), S))
    cands.sort()
    return cands[0][2]

def prop21(p):
    ctx = Ctx(p)
    a = mk(ctx, [(1, (3, 0, 0), 1), (ctx.m, (0, 4 * p + 1, 0), 1)])
    out = [f"p={p}: origin regime {regime(a, ctx)} iota0={iota0(a, ctx)}"]
    for S in [(0, 1), (0, 1, 2)]:
        assert permissible(a, S, ctx)
        best = None
        for j, lam, nu, b in points_over(a, S, ctx):
            b2, n, lin = adapt(b, ctx)
            v = iota0(b2, ctx)
            if best is None or v > best[0]:
                best = (v, j, lam, nu, regime(b2, ctx))
            assert nu == 0
        out.append(f"   centre S={S}: max iota0 over points = {best}")
    return out

def walk(a, E, ctx, branch, steps):
    """follow Rule 5.1 along a branch; branch(S) -> (j, lam). Returns list of states."""
    hist = []
    for t in range(steps):
        S = rule51(a, E, ctx)
        hist.append((t, tuple(sorted(E)), regime(a, ctx), iota(a, E, ctx), S, fmt(a[2]) if ctx.p > 2 else '', fmt(a[ctx.m])))
        j, lam = branch(S, a, E)
        b = blowup(a, S, j, lam, 0, ctx)
        if not is_mult_m(b, ctx):
            hist.append((t + 1, 'drop'))
            return hist
        E = new_E(E, S, j, lam)
        b2, n, lin = adapt(b, ctx)
        assert n == 0 and lin == 0
        a = b2
    return hist

def ex52(p):
    ctx = Ctx(p)
    a = mk(ctx, [(1, (1, 1, 0), 1), (ctx.m, (2 * p - 1, 2 * p, 0), 1)])
    E = frozenset({0, 1})
    st0 = (a, E)
    S = rule51(a, E, ctx)
    b = blowup(a, S, 0, {1: 0}, 0, ctx)
    E2 = new_E(E, S, 0, {1: 0})
    return f"p={p}: iota={iota(a, E, ctx)} regime={regime(a, ctx)} centre={S}; after chart x0 origin same data: {b == a and E2 == E}; adapted {is_adapted(a, ctx)}"

def ex53(p):
    ctx = Ctx(p)
    a = mk(ctx, [(2, (2, 1, 0), 1), (ctx.m, (2 * p, 1, 0), 1)])
    E = frozenset({1})
    S = rule51(a, E, ctx)
    b = blowup(a, S, 1, {0: 0}, 0, ctx)
    E2 = new_E(E, S, 1, {0: 0})
    others = [(j, lam, nu) for j, lam, nu, bb in points_over(a, S, ctx)]
    return f"p={p}: iota={iota(a, E, ctx)} regime={regime(a, ctx)} centre={S}; chart x1 origin same data: {b == a and E2 == E}; points of mult m over xi: {others}"

def ex54(p, steps):
    ctx = Ctx(p)
    a = mk(ctx, [(2, (2, 0, 1), 1), (ctx.m, (0, 2 * p + 1, 0), 1)])
    E = frozenset()
    def branch(S, a, E):
        j = 2 if 2 in S else S[0]
        return j, {k: 0 for k in S if k != j}
    return walk(a, E, ctx, branch, steps)

def omega_dep(p):
    ctx = Ctx(p)
    m = ctx.m
    a = mk(ctx, [(m, (2 * p, 2 * p, 0), 1), (m, (2 * p, 0, 2 * p + 1), 1)])
    E = {0}
    b = translate(a, mono((0, 3, 0)), ctx)
    return (f"p={p}: z: adapted={is_adapted(a, ctx)} slopes={slopes(a, ctx)} omega={omega(a, E, ctx)} | "
            f"z+x1^3: adapted={is_adapted(b, ctx)} slopes={slopes(b, ctx)} omega={omega(b, E, ctx)}")

def r3_contact(p):
    ctx = Ctx(p)
    m = ctx.m
    a = mk(ctx, [(2, (p, 0, 0), 1), (2, (0, p, 0), 1), (2, (0, 0, p + 1), 1), (m, (0, 0, p * p + 1), 1)])
    D, s, d = slopes(a, ctx)
    ordJ = ctx.b * s
    # in(J_r) at order ordJ is c * in(a_2)^(b/2); the linear part of D^(beta) in(g), |beta| = ordJ - 1,
    # has X_i-coefficient c_alpha * alpha_i, alpha = beta + e_i. So an order-1 element exists iff
    # some monomial of in(a_2)^(b/2) has an exponent prime to p.
    ina2 = homog(a[2], ordp(a[2]))
    # exponents of in(a2)^(b/2): all are sums of exponents of in(a2); check those of in(a2) itself
    # and, for p = 3, expand fully.
    allp = all(x % p == 0 for e in ina2 for x in e)
    full = None
    if p == 3:
        G = pw(ina2, ctx.b // 2, p)
        full = all(x % p == 0 for e in G for x in e), len(G)
    return f"p={p}: regime={regime(a, ctx)} sigma*={s} D={D} b={ctx.b} ord J_r={ordJ} (p | ord: {ordJ % p == 0}); in(a2) in k[X^p]: {allp}; full expansion check {full}"

if __name__ == '__main__':
    for p in (3, 5, 7):
        print('\n'.join(prop21(p)))
    for p in (3, 5, 7):
        print('5.2', ex52(p))
    for p in (3, 5, 7):
        print('5.3', ex53(p))
    for p in (3, 5, 7):
        h = ex54(p, 3 * p + 2 * (2 * p + 1) + 2)
        print(f'5.4 p={p}')
        for row in h:
            print('   ', row)
        # recurrence check
        states = {}
        for row in h:
            if len(row) > 2:
                key = (row[1], row[5], row[6])
                if key in states:
                    print(f'    state at step {states[key]} recurs at step {row[0]}')
                    break
                states[key] = row[0]
    for p in (3, 5, 7):
        print('omega', omega_dep(p))
    for p in (3, 5, 7):
        print('R3', r3_contact(p))
