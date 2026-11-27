"""Note 54: exact search for planar branches of corner runs with deg_{x,w} g = D (D = 2 or 3).
Start: g = y^{p-D} z^{p-D} (F(x, w) + terms divisible by y z, of x,w-degree <= D), F a random binary form of degree D.
A branch is a sequence of steps (chart from the word, all q^2 translations tried at once) keeping rho and ord g >= p.
It is planar-like if its translations after step s0 span F_q^2 (rank 2).  DFS tries first the translations
that raise the rank of the late translations.  Usage: p e D n depth seed budget"""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core54 import *

def start(K, D):
    p = K.p; G = {}
    for i in range(D + 1):
        if random.random() < 0.7: G[(i, D - i, 0, 0)] = random.randrange(1, K.q)
    if not G: G[(D, 0, 0, 0)] = 1
    for _ in range(random.randint(1, 6)):
        i = random.randint(0, D); l = random.randint(0, D - i)
        j = random.randint(1, 3); k = random.randint(1, 3)
        G[(i, l, j, k)] = random.randrange(1, K.q)
    g = {(i, l, j + p - D, k + p - D): c for (i, l, j, k), c in G.items()}
    return {m: c for m, c in g.items() if not all(x % p == 0 for x in m)}

def word(depth):
    w = []; cur = random.choice('yz')
    while len(w) < depth: w += [cur] * random.randint(1, 3); cur = 'z' if cur == 'y' else 'y'
    return w[:depth]

class Out(Exception): pass

def dfs(S, g, rho, w, s0, ts, budget, need):
    budget[0] -= 1
    if budget[0] < 0: raise Out
    K = S.K
    if not w:
        return (ts, g) if (not need or rank(K, ts[s0:]) == 2) else None
    R = S.step_all(g, w[0])
    if R is None: return None
    ok = np.nonzero((R['rho'] == rho) & (R['ordg'] >= K.p))[0]
    late = ts[s0:] if len(ts) >= s0 else []
    cur = rank(K, late)
    def key(c):
        t = S.pairs[c]
        if len(ts) < s0 or cur == 2: return 0
        return 0 if rank(K, late + [t]) > cur else 1
    for c in sorted(ok, key=key):
        r = dfs(S, S.column(R, c), rho, w[1:], s0, ts + [S.pairs[c]], budget, need)
        if r: return r
    return None

def extend(S, g, rho, maxlen=6, bud=4000):
    best = 0
    for L in range(1, maxlen + 1):
        found = False
        for w in itertools.product('yz', repeat=L):
            if L >= 2 and len(set(w)) < 2: continue
            try:
                if dfs(S, g, rho, list(w), 0, [], [bud], False): found = True; break
            except Out: pass
        if not found: return best
        best = L
    return best

if __name__ == '__main__':
    p, e, D, n, depth, seed, budget = map(int, sys.argv[1:8])
    random.seed(seed); K = Fq(p, e); S = Stepper(K, D); t0 = time.time()
    st = dict(starts=0, any_deep=0, planar=0, timeout=0); found = []
    for _ in range(n):
        g = start(K, D); I = invariants(K, g)
        if not I or I['ordg'] < p or I['rho'] < 1 or I['d'] != D: continue
        st['starts'] += 1; w = word(depth)
        try:
            if dfs(S, g, I['rho'], w, depth, [], [budget], False): st['any_deep'] += 1
        except Out: pass
        try:
            r = dfs(S, g, I['rho'], w, depth // 3, [], [budget], True)
        except Out:
            st['timeout'] += 1; continue
        if r:
            st['planar'] += 1; ts, gm = r; J = invariants(K, gm)
            found.append(dict(late=ts[depth // 3:], d=J['d'], rho=J['rho'], lem51=lemma51_condition(K, gm),
                              ext=extend(S, gm, I['rho'])))
            print('  planar branch:', found[-1], flush=True)
        print('progress', st, 'time %.0f' % (time.time() - t0), flush=True)
    print(p, e, 'D', D, 'depth', depth, 'budget', budget, st, 'time %.0f' % (time.time() - t0), flush=True)
