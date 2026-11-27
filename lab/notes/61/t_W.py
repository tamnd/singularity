import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# The replacement for W at R3 points (Section 61.5).
# At an R3 point, in a prepared coordinate:
#   e = p-exponent of the initial forms of the rigid coefficients of slope sigma* (largest e with all of them in k[X^(p^e)]),
#   Lambda = span of the linear forms L with in(D^(beta) a_i) = L^(p^e) (Lemma 61.12).
# Along rule walks we test:
#   (a) Lemma 61.12: in(D^(beta) a_i) = L^(p^e) with L != 0, computed by Hasse derivatives;
#   (b) Proposition 61.13: points with the same iota over the centre lie on the strict transform of V(L) for L in Lambda;
#   (c) persistence: if the next point is again R3 with the same iota, the strict transform of Lambda lies in Lambda'.
# usage: python3 t_W.py p nwalks depth family seed
import sys, random
from itertools import product
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '53'))
from lib61 import *
from walk61 import family, choose_centre, iota_of
from math import comb

def hasse(P, beta, p):
    out = {}
    for e, c in P.items():
        if all(ei >= bi for ei, bi in zip(e, beta)):
            cc = c
            for ei, bi in zip(e, beta):
                cc = cc * comb(ei, bi) % p
            if cc:
                g = tuple(ei - bi for ei, bi in zip(e, beta))
                out[g] = (out.get(g, 0) + cc) % p
    return {g: c for g, c in out.items() if c}

def pexp(e, p):
    n = 0
    while all(x % (p ** (n + 1)) == 0 for x in e):
        n += 1
    return n

def eres(a, E, ctx):
    """p-exponent of the E-residual initial forms in(a_i) / (largest E-monomial dividing in(a_i)), rigid i of slope sigma*."""
    p = ctx.p
    D, s, d = slopes(a, ctx)
    out = INF
    for i in ctx.rigid:
        if a[i] and Fr(ordp(a[i]), i) == s:
            H = homog(a[i], ordp(a[i]))
            g = [min(e[k] for e in H) if k in E else 0 for k in range(3)]
            H2 = [tuple(e[k] - g[k] for k in range(3)) for e in H]
            out = min(out, min(pexp(x, p) for x in H2))
    return out

def leading_data(a, ctx):
    """For a prepared coordinate at an R3 point: (e, list of (i, beta, L)) ."""
    p = ctx.p
    D, s, d = slopes(a, ctx)
    ins = []
    for i in ctx.rigid:
        if a[i] and Fr(ordp(a[i]), i) == s:
            ins.append((i, homog(a[i], ordp(a[i]))))
    e = min(min(pexp(g, p) for g in H) for i, H in ins)
    q = p ** e
    Ls = []
    for i, H in ins:
        for g in H:
            gam = tuple(x // q for x in g)
            for t in range(3):
                if gam[t] % p:
                    beta = tuple(q * (gam[u] - (1 if u == t else 0)) for u in range(3))
                    h = hasse(a[i], beta, p)
                    o = ordp(h)
                    ih = homog(h, o)
                    # check in(h) = L^q
                    L = {}
                    ok = (o == q)
                    if ok:
                        for g2, c2 in ih.items():
                            if sum(g2) != q or max(g2) != q:
                                ok = False
                                break
                        if ok:
                            lin = tuple(next((c2 for g2, c2 in ih.items() if g2[u] == q), 0) for u in range(3))
                            # c^q = c for c in F_p, so the linear form has the same coefficients
                            Lpoly = {ek(u): lin[u] for u in range(3) if lin[u]}
                            ok = clean(pw(Lpoly, q, p), p) == ih
                            L = lin
                    Ls.append((i, beta, L if ok else None))
    return e, Ls

def span_rank(vecs, p):
    rows = [list(v) for v in vecs if any(v)]
    r = 0
    cols = 3
    for c in range(cols):
        piv = next((k for k in range(r, len(rows)) if rows[k][c] % p), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [x * inv % p for x in rows[r]]
        for k in range(len(rows)):
            if k != r and rows[k][c] % p:
                f = rows[k][c]
                rows[k] = [(x - f * y) % p for x, y in zip(rows[k], rows[r])]
        r += 1
    return r

def direction(S, j, lam):
    v = [0, 0, 0]
    v[j] = 1
    for k, l in lam.items():
        v[k] = l
    return v

def strict_L(L, S, j, lam):
    """strict transform of the linear form L (with L(v) = 0) in the chart of x_j at lam, as a linear form in the new variables."""
    out = [0, 0, 0]
    for t in range(3):
        if t in S and t != j:
            out[t] = L[t]
        elif t not in S:
            out[t] = L[t]
    # coefficient of x_j: sum over t in S of L[t] * (lam_t or 1) = L(v) = 0 for t in S; terms outside S give x_t, unchanged
    return tuple(out)

def main(p, n, depth, fam, seed):
    ctx = Ctx(p)
    rng = random.Random(seed)
    st = dict(walks=0, R3=0, R3_bad=0, e_hist={}, lemma_fail=0, tau_hist={}, same_pts=0, same_pts_bad=0, off_W=0, persist=0, persist_fail=0, e_up=0, tau_up=0)
    exs = []
    for _ in range(n):
        a, E = family(fam, ctx, rng) if fam != 'r3bad' else r3bad(ctx, rng)
        if not is_mult_m(a, ctx):
            continue
        st['walks'] += 1
        a, info = E_adapt(a, ctx)
        prevL = None
        for t in range(depth):
            if info['conflict'] or info['capped']:
                break
            inv = invariants(a, E, ctx)
            io = iota_of(inv, E, 'plain')
            S, kind = choose_centre(a, E, inv, ctx, 'plain')
            data = None
            if inv['regime'] == 'R3':
                st['R3'] += 1
                e, Ls = leading_data(a, ctx)
                st['e_hist'][e] = st['e_hist'].get(e, 0) + 1
                er = eres(a, E, ctx)
                if prevL is not None:
                    key = 'eres_trans_%d_%d' % (prevL[2], er)
                    st[key] = st.get(key, 0) + 1
                if e >= 1:
                    st['R3_bad'] += 1
                if any(L is None for _, _, L in Ls):
                    st['lemma_fail'] += 1
                Lam = [L for _, _, L in Ls if L]
                tau = span_rank(Lam, p)
                st['tau_hist'][tau] = st['tau_hist'].get(tau, 0) + 1
                data = (e, Lam, tau)
                if prevL is not None:
                    key = 'e_trans_%d_%d' % (prevL[0], e)
                    st[key] = st.get(key, 0) + 1
                if prevL is not None and e == prevL[0]:
                    st['persist'] += 1
                    if span_rank(Lam + [prevL[1]], p) > tau:
                        st['persist_fail'] += 1
                        if len(exs) < 6:
                            exs.append(('persist_fail', [fmt(x) for x in a[1:]], sorted(E), prevL, Lam))
                    if e > prevL[0]:
                        st['e_up'] += 1
            pts = [x for x in points_over(a, S, ctx, allnu=False)]
            if not pts:
                break
            same = []
            for (j, lam, nu, b) in pts:
                E2 = new_E(E, S, j, lam)
                inv2 = invariants(b, E2, ctx)
                if iota_of(inv2, E2, 'plain') == io and inv['regime'] == 'R3':
                    st['same_pts'] += 1
                    same.append((j, lam, b, E2))
                    v = direction(S, j, lam)
                    wz_same = omega(b, E2, ctx) == inv['omega'] and all(inv['mu'][k] == 0 for k in E)
                    if wz_same:
                        st['off_W_tested'] = st.get('off_W_tested', 0) + 1
                    if wz_same and data and any(sum(L[u] * v[u] for u in range(3)) % p for L in data[1]) and len(S) == 3:
                        st['same_pts_bad'] += 1
                        if len(exs) < 6:
                            exs.append(('off_W', [fmt(x) for x in a[1:]], sorted(E), S, j, lam, data))
            if same and data:
                j, lam, b, E2 = rng.choice(same)
                # persistence is tested for the strict transform of one leading form
                L = data[1][0]
                prevL = (data[0], strict_L(L, S, j, lam), eres(a, E, ctx)) if len(S) == 3 else None
            else:
                j, lam, nu, b = rng.choice(pts)
                E2 = new_E(E, S, j, lam)
                prevL = None
            a, info = E_adapt(b, ctx)
            E = E2
            if prevL is not None:
                inv3 = invariants(a, E, ctx)
                if inv3['regime'] != 'R3':
                    prevL = None
    print(f"p={p} fam={fam}", st)
    for x in exs:
        print('EX', x)

def r3bad(ctx, rng):
    p, m = ctx.p, ctx.m
    a = [{(0, 0, 0): 1}] + [{} for _ in range(m)]
    L = {}
    while not L:
        L = {ek(u): rng.randint(0, p - 1) for u in range(3)}
        L = {g: c for g, c in L.items() if c}
    a[2] = pw(L, p, p)
    for _ in range(rng.randint(1, 3)):
        d = rng.randint(p + 1, p + 3)
        g = [0, 0, 0]
        for _ in range(d):
            g[rng.randrange(3)] += 1
        a[2] = add(a[2], mono(g, rng.randint(1, p - 1)), p)
    g = [0, 0, 0]
    for _ in range(p * p + rng.randint(1, 3)):
        g[rng.randrange(3)] += 1
    a[m] = mono(g, 1)
    E = frozenset(k for k in range(3) if rng.random() < 0.3)
    return a, E

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))
