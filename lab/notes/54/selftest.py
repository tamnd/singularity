import os, sys, random; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core54 import *
# 1. vectorized step agrees with a direct substitution; 2. shortcut rho agrees with the generators of Theta
def direct_step(K, g, chart, a, b):
    p = K.p; h = {}
    for (i, l, j, k), c in g.items():
        e = i + l + j + k - p
        new = (e, k) if chart == 'y' else (j, e)
        for s in range(i + 1):
            for t in range(l + 1):
                co = K.mul[K.mul[c][K.i2f(comb(i, s) * comb(l, t))]][K.mul[K.pw(a, i - s)][K.pw(b, l - t)]]
                mo = (s, t) + new
                h[mo] = K.add[h.get(mo, 0)][co]
    return {m: c for m, c in h.items() if c and not all(x % p == 0 for x in m)}
random.seed(1); bad = 0; n = 0
for (p, e) in [(3, 1), (5, 1), (5, 2), (7, 1), (3, 2)]:
    K = Fq(p, e); S = Stepper(K)
    for _ in range(30):
        g = {}
        for _ in range(8):
            i = random.randint(0, min(3, p - 1)); l = random.randint(0, min(3, p - 1) - i)
            g[(i, l, random.randint(p - 3, p), random.randint(p - 3, p))] = random.randrange(1, K.q)
        g = {m: c for m, c in g.items() if not all(x % p == 0 for x in m) and sum(m) >= p}
        if not g: continue
        for ch in 'yz':
            R = S.step_all(g, ch)
            for c in random.sample(range(K.q ** 2), 5):
                a, b = S.pairs[c]
                g2 = direct_step(K, g, ch, a, b); n += 1
                if g2 != S.column(R, c): bad += 1
                if g2:
                    I = invariants(K, g2)
                    if (R['ry'][c], R['rz'][c], R['rho'][c]) != check_rho_formula(K, g2) or I['rho'] != R['rho'][c]: bad += 1
print('checks', n, 'mismatches', bad)
