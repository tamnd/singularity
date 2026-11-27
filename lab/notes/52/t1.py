"""Statement T1 of note 50 (proved in note 52, Lemma 3.1) and the dominance for g_x when deg_{x,w} g = 2.
Laurent monomials are exponent vectors (a, b) of y_N^a z_N^b, value a + theta b.
The word is the Euclid word of theta. Translations random (planar) or adversarial (greedy cancellation)."""
import os, sys, random, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import F

def run(K, theta, depth, alpha, beta, gamma, mode):
    v = lambda e: e[0] + theta * e[1]
    y, z, M = (1, 0), (0, 1), (0, 0)
    f = dict(gamma)                       # f_m = alpha phi_m + beta psi_m + gamma
    def addmul(f, poly, s, mono):
        for e, c in poly.items():
            ee = (e[0] + mono[0], e[1] + mono[1]); cc = K.mul[c][s]
            nv = K.add[f.get(ee, 0)][cc]
            if nv: f[ee] = nv
            else: f.pop(ee, None)
    hist = []; trans = []
    for m in range(depth):
        # chart
        if v(z) > v(y): L = 'y'; z = (z[0] - y[0], z[1] - y[1]); Lm = y
        else: L = 'z'; y = (y[0] - z[0], y[1] - z[1]); Lm = z
        M = (M[0] + Lm[0], M[1] + Lm[1])          # M_{m+1}
        # choose translation
        cands = [(a, b) for a in range(K.q) for b in range(K.q) if (a, b) != (0, 0)]
        if mode == 'rand':
            a, b = random.choice(cands)
        else:
            best = None
            for (a, b) in cands:
                if m % 2 == 0 and a == 0: continue      # keep the late translations of rank 2
                if m % 2 == 1 and b == 0: continue
                g2 = dict(f); addmul(g2, alpha, a, M); addmul(g2, beta, b, M)
                val = min((v(e) for e in g2), default=1e9)
                if best is None or val > best[0] + 1e-12: best = (val, a, b)
            _, a, b = best
        addmul(f, alpha, a, M); addmul(f, beta, b, M)
        trans.append((a, b))
        lead = min(f, key=v) if f else None
        hist.append((lead, v(lead) if lead else None, v(M), y, z, M))
    return hist, trans

def to_level(e, y, z):
    # solve e = s*y + t*z
    det = y[0] * z[1] - y[1] * z[0]
    s = (e[0] * z[1] - e[1] * z[0]) // det; t = (y[0] * e[1] - y[1] * e[0]) // det
    assert s * y[0] + t * z[0] == e[0] and s * y[1] + t * z[1] == e[1]
    return (s, t)

def randpoly(K, n, lo=0):
    return {(random.randint(lo, 3), random.randint(0, 3)): K.rand(True) for _ in range(n)}

if __name__ == '__main__':
    out = []
    for (p, e) in ((3, 1), (3, 2), (5, 1), (5, 2), (7, 1), (7, 2)):
        K = F(p, e)
        for theta, name in ((math.sqrt(2) - 1, 'sqrt2-1'), ((math.sqrt(5) - 1) / 2, 'golden')):
            for mode in ('rand', 'adv'):
                random.seed(1000 * p + 10 * e + (mode == 'adv'))
                stab = 0; below = 0; dom = 0; tot = 0
                for _ in range(30 if mode == 'adv' and K.q > 9 else 60):
                    alpha = randpoly(K, random.randint(1, 3)); beta = randpoly(K, random.randint(1, 3))
                    if random.random() < 0.5:      # beta = u alpha + small, to try to cancel
                        c = K.rand(True); beta = {k: K.mul[c][x] for k, x in alpha.items()}
                        beta[(random.randint(1, 3), random.randint(0, 2))] = K.rand(True)
                    gamma = randpoly(K, random.randint(0, 3))
                    depth = 22
                    hist, trans = run(K, theta, depth, alpha, beta, gamma, mode)
                    tot += 1
                    leads = [h[0] for h in hist[-8:]]
                    if len(set(leads)) == 1: stab += 1
                    vmin = min(a + theta * b for (a, b) in list(alpha) + list(beta))
                    if hist[-1][1] is not None and hist[-1][1] < vmin + 1 + theta: below += 1
                    # dominance at the last level: constant coefficient f_m, others M alpha, M beta
                    lead, vl, vM, y, z, M = hist[-1]
                    if lead is None: continue
                    lv = to_level(lead, y, z)
                    ok = True
                    # all other terms of f_m and of M*alpha, M*beta must have both exponents >= lead's and != lead
                    # recompute f_m
                    allterms = []
                    f = dict(gamma)
                    # rebuild f from trans
                    yy, zz, MM = (1, 0), (0, 1), (0, 0)
                    v = lambda e_: e_[0] + theta * e_[1]
                    for (a, b) in trans:
                        if v(zz) > v(yy): zz = (zz[0] - yy[0], zz[1] - yy[1]); Lm = yy
                        else: yy = (yy[0] - zz[0], yy[1] - zz[1]); Lm = zz
                        MM = (MM[0] + Lm[0], MM[1] + Lm[1])
                        for poly, s in ((alpha, a), (beta, b)):
                            for e_, c_ in poly.items():
                                ee = (e_[0] + MM[0], e_[1] + MM[1]); nv = K.add[f.get(ee, 0)][K.mul[c_][s]]
                                if nv: f[ee] = nv
                                else: f.pop(ee, None)
                    for e_ in f:
                        if e_ != lead: allterms.append(e_)
                    for poly in (alpha, beta):
                        for e_ in poly: allterms.append((e_[0] + M[0], e_[1] + M[1]))
                    for e_ in allterms:
                        q = to_level(e_, y, z)
                        if not (q[0] >= lv[0] and q[1] >= lv[1]): ok = False
                    if ok: dom += 1
                out.append((p, e, name, mode, tot, stab, below, dom))
                print(p, e, name, mode, 'cases', tot, 'lead stable last 8', stab, 'v < min+1+theta', below, 'monomial*unit at last level', dom, flush=True)
