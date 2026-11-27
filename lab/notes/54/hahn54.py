"""Note 54: Hahn-model test of Statement D (Theorem 3) and of the dominance in Proposition 4.
Run: Euclid word of theta (y-chart if v(y_m) < v(z_m)), M_{j+1} = y_0 z_0 / (y_{j+1} z_{j+1}) as a Laurent
monomial in (y_0, z_0), value v(y_0) = 1, v(z_0) = theta.  phi_m = sum_{j<m} a_j M_{j+1}, psi_m likewise,
Phi_inf truncated at J terms (exact below v(M_{J+1})).  f in H[X, W] of degree D < p with coefficients
random polynomials in y_0, z_0; adversarial choices: f built from a line X - cW, translations sparse off a line.
Checks: (a) f(Phi_inf) != 0 below the truncation and v f(Phi_inf) < lambda_1 + 1 + theta;
(b) v f(Phi_m) constant (= v f(Phi_inf)) for m >= m0, with the leading term stable.
Usage: p D trials seed"""
import sys, random, math
from math import comb
p, D, trials, seed = map(int, sys.argv[1:5]); random.seed(seed)
TH = math.sqrt(2) - 1
def val(m): return m[0] + TH * m[1]
def mul(A, B, bound):
    C = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            m = (ma[0] + mb[0], ma[1] + mb[1])
            if val(m) < bound: C[m] = (C.get(m, 0) + ca * cb) % p
    return {m: c for m, c in C.items() if c}
def add(A, B):
    C = dict(A)
    for m, c in B.items(): C[m] = (C.get(m, 0) + c) % p
    return {m: c for m, c in C.items() if c}
def scal(A, s): return {m: (c * s) % p for m, c in A.items() if (c * s) % p}
def v(A): return min(val(m) for m in A) if A else float('inf')
def lead(A): m = min(A, key=val); return m, A[m]
J = 40
y, z = (1, 0), (0, 1); M = []
for j in range(J):
    if val(y) < val(z): z = (z[0] - y[0], z[1] - y[1])
    else: y = (y[0] - z[0], y[1] - z[1])
    M.append((1 - y[0] - z[0], 1 - y[1] - z[1]))   # M_{j+1} = y_0 z_0 / (y_{j+1} z_{j+1})
VMAX = val(M[-1])          # all sums below VMAX are exact
def series(coef, upto): return {M[j]: c for j, c in enumerate(coef[:upto]) if c}
def evalf(f, P, Q, bound):
    out = {}; Pp = [{(0, 0): 1}]; Qp = [{(0, 0): 1}]
    for k in range(D): Pp.append(mul(Pp[-1], P, bound)); Qp.append(mul(Qp[-1], Q, bound))
    for (i, l), c in f.items(): out = add(out, mul(c, mul(Pp[i], Qp[l], bound), bound))
    return out
def deriv(f, var):
    g = {}
    for (i, l), c in f.items():
        e = i if var == 0 else l
        if e % p: g[(i - 1, l) if var == 0 else (i, l - 1)] = scal(c, e)
    return g
def randcoef(lowdeg=2):
    return {(a, b): random.randrange(1, p) for a in range(lowdeg + 1) for b in range(lowdeg + 1 - a) if random.random() < 0.4} or {(0, 0): 1}
def make_f(kind, c):
    f = {}
    if kind == 'random':
        for i in range(D + 1):
            for l in range(D + 1 - i):
                if random.random() < 0.6: f[(i, l)] = randcoef()
        f[(D, 0)] = randcoef()
    else:  # built from the line X - cW, to force cancellation: f = (X - cW)^D + y_0 z_0 * (lower random)
        lin = {(1, 0): {(0, 0): 1}, (0, 1): {(0, 0): (-c) % p}}
        f = {(0, 0): {(0, 0): 1}}
        for _ in range(D):
            g = {}
            for (i, l), a in f.items():
                for (i2, l2), b in lin.items():
                    k = (i + i2, l + l2); g[k] = add(g.get(k, {}), mul(a, b, 99))
            f = g
        for i in range(D):
            for l in range(D - i):
                if random.random() < 0.5: f[(i, l)] = add(f.get((i, l), {}), mul(randcoef(), {(1, 1): 1}, 99))
    return {k: a for k, a in f.items() if a}
bad = 0; stats = []; und = 0
for t in range(trials):
    kind = random.choice(['random', 'line']); c = random.randrange(p)
    # translations: planar but sparse off the line a = c b
    a = []; b = []
    for j in range(J):
        bj = random.randrange(p)
        if random.random() < 0.25: a.append(random.randrange(p))
        else: a.append((c * bj) % p)
        b.append(bj)
    a[J - 1] = (c * b[J - 1] + 1) % p
    P, Q = series(a, J), series(b, J)
    f = make_f(kind, c)
    cmin = min(v(cf) for (i, l), cf in f.items() if i + l > 0)
    bound = VMAX + cmin - 1e-9      # f(Phi_inf) - f(Phi_trunc) has value >= v(M_{J+1}) + cmin
    F = evalf(f, P, Q, bound)
    lam1 = min(v(evalf(deriv(f, 0), P, Q, bound)), v(evalf(deriv(f, 1), P, Q, bound)))
    okA = bool(F) and v(F) < lam1 + 1 + TH
    # (b): stabilization
    traj = []
    for m in range(0, J, 2):
        Fm = evalf(f, series(a, m), series(b, m), bound)
        traj.append((m, round(v(Fm), 4), lead(Fm) if Fm else None))
    m0 = next(i for i in range(len(traj)) if all(tr[1:] == traj[-1][1:] for tr in traj[i:]))
    okB = traj[-1][1] == round(v(F), 4) and traj[m0][0] < J - 6
    if not F or lam1 + 1 + TH >= bound and v(F) >= bound: und += 1; continue
    if not (okA and okB): bad += 1; print('FAIL', kind, okA, okB, v(F), lam1, traj[-4:])
    stats.append((kind, round(v(F), 3), round(lam1, 3), traj[m0][0]))
print('p', p, 'D', D, 'trials', trials, 'failures', bad, 'undecided (truncation)', und, 'VMAX %.4f' % VMAX)
print('sample (kind, v f(Phi), lambda1, stabilization level):', stats[:12])
