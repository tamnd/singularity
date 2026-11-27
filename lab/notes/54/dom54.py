"""Note 54: exact test of Proposition 4 (dominance) and Theorem 5 in the Hahn model.
f in K[y_0, z_0][X, W] (polynomial coefficients), so F_m = f(phi_m + M_m X, psi_m + M_m W) is computed exactly.
Along the Euclid word of theta, at levels m in a late window, write each monomial of each coefficient of F_m in
the level-m variables (y_m, z_m) and check: (1) all exponents are >= 0; (2) the leading monomial nu of f(phi_m, psi_m)
(the same for all m in the window) divides every other monomial of F_m with both exponents strictly larger,
so F_m = c nu (1 + h), h in the maximal ideal.  Also the Theorem 5 step: for g of degree D, nu_X | nu_W or
nu_W | nu_X at level m.  Usage: p D trials seed"""
import sys, random, math
from math import comb
p, D, trials, seed = map(int, sys.argv[1:5]); MODE = sys.argv[5] if len(sys.argv) > 5 else 'planar'; random.seed(seed)
TH = math.sqrt(2) - 1
def val(m): return m[0] + TH * m[1]
def pmul(A, B):
    C = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            m = (ma[0] + mb[0], ma[1] + mb[1]); C[m] = (C.get(m, 0) + ca * cb) % p
    return {m: c for m, c in C.items() if c}
def padd(A, B):
    C = dict(A)
    for m, c in B.items(): C[m] = (C.get(m, 0) + c) % p
    return {m: c for m, c in C.items() if c}
LEV = 26
y, z = (1, 0), (0, 1); Ys = [y]; Zs = [z]; M = []
for j in range(LEV):
    if val(y) < val(z): z = (z[0] - y[0], z[1] - y[1])
    else: y = (y[0] - z[0], y[1] - z[1])
    Ys.append(y); Zs.append(z); M.append((1 - y[0] - z[0], 1 - y[1] - z[1]))   # M[j] = M_{j+1}
def tolevel(mono, m):
    (a1, b1), (a2, b2) = Ys[m], Zs[m]; det = a1 * b2 - a2 * b1
    s = (mono[0] * b2 - mono[1] * a2) // det; t = (a1 * mono[1] - b1 * mono[0]) // det
    assert s * a1 + t * a2 == mono[0] and s * b1 + t * b2 == mono[1]
    return (s, t)
# bivariate polynomials in (X, W) with Laurent coefficients: dict (i, l) -> coefficient dict
def bmul(P, Q):
    R = {}
    for k1, c1 in P.items():
        for k2, c2 in Q.items():
            k = (k1[0] + k2[0], k1[1] + k2[1]); R[k] = padd(R.get(k, {}), pmul(c1, c2))
    return {k: c for k, c in R.items() if c}
def badd(P, Q):
    R = dict(P)
    for k, c in Q.items(): R[k] = padd(R.get(k, {}), c)
    return {k: c for k, c in R.items() if c}
def compose(f, m, a, b):
    """f(phi_m + M_m X, psi_m + M_m W); M_m = M[m-1] (M_0 = 1)"""
    Mm = M[m - 1] if m > 0 else (0, 0)
    phi = {M[j]: a[j] for j in range(m) if a[j]}; psi = {M[j]: b[j] for j in range(m) if b[j]}
    PX = badd({(0, 0): phi} if phi else {}, {(1, 0): {Mm: 1}}); PW = badd({(0, 0): psi} if psi else {}, {(0, 1): {Mm: 1}})
    powX = [{(0, 0): {(0, 0): 1}}]; powW = [{(0, 0): {(0, 0): 1}}]
    for _ in range(D): powX.append(bmul(powX[-1], PX)); powW.append(bmul(powW[-1], PW))
    R = {}
    for (i, l), c in f.items(): R = badd(R, bmul({(0, 0): c}, bmul(powX[i], powW[l])))
    return R
def deriv(f, var):
    g = {}
    for (i, l), c in f.items():
        e = i if var == 0 else l
        if e % p:
            g[(i - 1, l) if var == 0 else (i, l - 1)] = {m: (x * e) % p for m, x in c.items()}
    return g
def randcoef():
    return {(u, w): random.randrange(1, p) for u in range(3) for w in range(3 - u) if random.random() < 0.4} or {(0, 0): 1}
def randf(deg):
    f = {(i, l): randcoef() for i in range(deg + 1) for l in range(deg + 1 - i) if random.random() < 0.6}
    f[(deg, 0)] = randcoef(); return f
def check_dom(f, a, b, window):
    leads = []
    for m in window:
        F = compose(f, m, a, b)
        if not F: return 'zero'
        allm = [(k, mo) for k, c in F.items() for mo in c]
        nu = min((mo for k, mo in allm if k == (0, 0)), key=val, default=None)
        if nu is None or min(val(mo) for k, mo in allm) < val(nu): return 'notdominant'
        leads.append(nu)
        qn = tolevel(nu, m)
        for k, mo in allm:
            q = tolevel(mo, m)
            if min(q) < 0: return 'negexp'
            if (k, mo) != ((0, 0), nu) and not (q[0] > qn[0] and q[1] > qn[1]):
                return ('weak', m)
    return 'ok' if len(set(leads)) == 1 else 'leadchanges'
from collections import Counter
res = Counter(); res5 = Counter()
for t in range(trials):
    c = random.randrange(p); a = []; b = []
    for j in range(LEV):
        bj = random.randrange(p); b.append(bj)
        a.append(random.randrange(p) if random.random() < 0.3 else (c * bj) % p)
    if MODE == 'linear': a = [(c * bj) % p for bj in b]      # control: a linear run, where Prop 4 need not hold
    else: a[LEV - 1] = (c * b[LEV - 1] + 1) % p
    if random.random() < 0.5: g = randf(D)
    else:   # adversarial: g = (X - cW)^D + y_0 z_0 (random of degree < D)
        g = {(i, D - i): {(0, 0): (comb(D, i) * pow(-c, D - i, p)) % p} for i in range(D + 1)}
        g = {k: v for k, v in g.items() if v[(0, 0)]}
        for k, cf in randf(D - 1).items(): g[k] = padd(g.get(k, {}), pmul(cf, {(1, 1): 1}))
        g = {k: v for k, v in g.items() if v}
    window = range(LEV - 4, LEV + 1)
    out = {}
    for name, h in (('gX', deriv(g, 0)), ('gW', deriv(g, 1))):
        if h: out[name] = check_dom(h, a, b, window); res[out[name] if isinstance(out[name], str) else out[name][0]] += 1
    # Theorem 5 divisibility at the last level
    if all(out.get(n) == 'ok' for n in ('gX', 'gW') if deriv(g, 0 if n == 'gX' else 1)):
        nus = []
        for h in (deriv(g, 0), deriv(g, 1)):
            if h:
                F = compose(h, LEV, a, b); nus.append(tolevel(min(F[(0, 0)], key=val), LEV))
        ok = len(nus) < 2 or (nus[0][0] <= nus[1][0] and nus[0][1] <= nus[1][1]) or (nus[1][0] <= nus[0][0] and nus[1][1] <= nus[0][1])
        res5['divisible' if ok else 'not divisible'] += 1
print('mode', MODE, 'p', p, 'D', D, 'trials', trials, 'dominance results', dict(res), 'Theorem 5 step', dict(res5))
