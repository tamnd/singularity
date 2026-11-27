"""Theorem 4.1 of note 50: linear runs (late translations in ker l, l = x + c w).
At the end of each deep walk with nonzero translations: check in G = const * l^d in the
original coordinates, d = rho + 1, 2 <= d < p, and in the coordinates (X = l, w):
nu^G of the corner curves >= d and of the corner surfaces >= rho."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *

def start(K, c, p):
    d = random.randint(2, p - 1)
    a = random.randint(0, p); b = random.randint(0, p)
    while a + b + d < p: a += 1
    Gp = {(d, 0, 0, 0): K.rand(True)}
    for _ in range(random.randint(1, 6)):
        i = random.randint(0, p - 1); l = random.randint(0, p - 1 - i)
        j = random.randint(0, 3); k = random.randint(0, 3)
        if i + l + j + k <= d and (i, l, j, k) != (d, 0, 0, 0):
            j += 1; k += 1
        Gp[(i, l, j, k)] = K.rand(True)
    if random.random() < 0.4:
        Gp[(0, 1, d - 1, d - 1)] = K.rand(True)   # tie case of Step 3
    gp = clean(K, {(i, l, j + a, k + b): co for (i, l, j, k), co in Gp.items()})
    # back to (x, w): X = x + c w
    g = subst_x(K, gp, c)
    return g

PNZ = 0.8
def walk(K, g, c, depth):
    p = K.p
    I = invariants(K, g)
    if I is None or I['rho'] < 1 or I['ordg'] < p: return None
    rho = I['rho']
    word = []
    while len(word) < depth:
        word += [random.choice('yz')] * random.randint(1, 3)
        word[-1] = word[-1]
    # force alternation of blocks
    w2 = []; cur = random.choice('yz')
    while len(w2) < depth:
        w2 += [cur] * random.randint(1, 3); cur = 'z' if cur == 'y' else 'y'
    word = w2[:depth]
    trans = []
    for ch in word:
        bs = list(range(1, K.q)); random.shuffle(bs)
        bs = bs + [0] if random.random() < PNZ else [0] + bs
        ok = False
        for bb in bs:
            aa = K.neg[K.mul[c][bb]]
            try:
                g2 = step(K, g, ch, aa, bb)
            except AssertionError:
                continue
            I2 = invariants(K, g2)
            if I2 and I2['rho'] == rho and I2['ordg'] >= p:
                g = g2; trans.append((aa, bb)); ok = True; break
        if not ok: return None
    return g, trans, rho

def check(K, g, c, rho):
    p = K.p
    I = invariants(K, g)
    gp = subst_x(K, g, K.neg[c])      # coordinates X = x + c w, w
    J = invariants(K, gp)
    inG = J['inG']
    okform = J['binary'] and len(inG) == 1 and list(inG)[0][1] == 0 and list(inG)[0][0] == J['d']
    return dict(form=okform, drho=(J['d'] == rho + 1 and 2 <= J['d'] < p),
                curves=min(J['curve_y'], J['curve_z']) >= J['d'],
                surf=min(J['surf_y'], J['surf_z']) >= rho,
                surf_eq_rho=min(J['surf_y'], J['surf_z']) == rho, d=J['d'])

if __name__ == '__main__':
    p, e, n, depth, seed = map(int, sys.argv[1:6])
    random.seed(seed)
    K = F(p, e)
    stats = dict(starts=0, deep=0, deep_nz=0, fail=0, surfeq=0)
    fails = []
    for _ in range(n):
        c = K.rand()
        g = start(K, c, p)
        stats['starts'] += 1
        r = walk(K, g, c, depth)
        if r is None: continue
        gm, trans, rho = r
        stats['deep'] += 1
        ch = check(K, gm, c, rho)
        if ch['surf_eq_rho']: stats['surfeq_all'] = stats.get('surfeq_all', 0) + 1
        if any(t != (0, 0) for t in trans[depth // 2:]):
            stats['deep_nz'] += 1
            stats['nz_late'] = stats.get('nz_late', 0) + sum(t != (0, 0) for t in trans[depth // 2:])
            if not (ch['form'] and ch['drho'] and ch['curves'] and ch['surf']):
                stats['fail'] += 1; fails.append((g, trans, ch))
            if ch['surf_eq_rho']: stats['surfeq'] += 1
    print(p, e, stats)
    for f in fails[:3]: print('FAIL', f)
