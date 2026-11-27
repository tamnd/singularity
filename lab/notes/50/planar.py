# Search for planar behaviour: DFS over all translations along a corner word; flag paths whose
# translations after the first half span F_q^2 (rank 2), and record H1 / L-circ at the end of such paths.
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, json
from fq import *
from walk import children, rand_g, rank_dirs

def dfs(F, g, rho, word, t, path, res, budget):
    if budget[0] <= 0: return
    budget[0] -= 1
    if t == len(word):
        half = path[len(word)//2:]
        r = rank_dirs(F, [(s[0], s[1]) for s in half])
        res['paths'] += 1
        res['maxrank'] = max(res['maxrank'], r)
        nz = sum(1 for s in half if s[0] or s[1])
        res['maxnz'] = max(res['maxnz'], nz)
        if r == 2: res['rank2'].append(list(path))
        if not path[-1][2]: res['h1fail'] += 1
        if path[-1][3] < rho: res['lfail'] += 1
        return
    for ch, a, b, g2 in children(F, g, rho, charts=word[t]):
        path.append((a, b, binary(initial(F, g2)), min(nu_curve(g2, 'y'), nu_curve(g2, 'z'))))
        dfs(F, g2, rho, word, t+1, path, res, budget)
        path.pop()

def rand_deg2(F, rng):
    p, q = F.p, F.q
    ry, rz = rng.randrange(0, 2*p), rng.randrange(0, 2*p)
    G = {}
    for (i, l) in [(2,0),(1,1),(0,2),(1,0),(0,1),(0,0)]:
        for _ in range(rng.randrange(0, 3)):
            e = rng.randrange(max(0, 2 - i - l), 2*p)
            j = rng.randrange(e+1)
            padd(F, G, (i, l, j + ry, e - j + rz), 1 + rng.randrange(q-1))
    return clean(F, G)

if __name__ == '__main__':
    p, k, fam, N, L, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    F = GF(p, k); rng = random.Random(seed)
    tot = dict(g=0, deep=0, rank1=0, rank2=0, h1fail=0, lfail=0)
    for n in range(N):
        g0 = rand_deg2(F, rng) if fam == 'deg2' else rand_g(F, rng, fam)
        if not g0 or ordg(g0) < p or degxw(g0) >= p: continue
        rho = data(F, g0)[3]
        if rho < 1: continue
        word = []; let = rng.choice('yz')
        while len(word) < L: word += [let] * rng.randint(1, 2); let = 'y' if let == 'z' else 'z'
        res = dict(paths=0, maxrank=0, maxnz=0, rank2=[], h1fail=0, lfail=0)
        dfs(F, g0, rho, word, 0, [], res, [3000])
        tot['g'] += 1
        if res['paths']:
            tot['deep'] += 1
            if res['maxrank'] == 1: tot['rank1'] += 1
            if res['maxrank'] == 2:
                tot['rank2'] += 1
                print(json.dumps(dict(g0=show(F, g0, 30), rho=rho, word=''.join(word), path=res['rank2'][0])), flush=True)
            tot['h1fail'] += res['h1fail'] > 0; tot['lfail'] += res['lfail'] > 0
    print('STATS', p, k, fam, L, tot, flush=True)
