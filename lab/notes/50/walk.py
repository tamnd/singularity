# Random corner walks keeping rho; records H1 and L-circ data.
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, json
from fq import *

def children(F, g, rho, nz_only=False, charts='yz'):
    out = []
    for ch in charts:
        for a in range(F.q):
            for b in range(F.q):
                if nz_only and a == 0 and b == 0: continue
                g2 = step(F, g, ch, a, b)
                if g2 is None or not g2: continue
                if data(F, g2)[3] == rho:
                    out.append((ch, a, b, g2))
    return out

def rand_g(F, rng, fam):
    p, q = F.p, F.q
    ry, rz = rng.randrange(0, 2*p), rng.randrange(0, 2*p)
    G = {}
    def put(m, c): padd(F, G, m, c)
    d = rng.randrange(2, p)  # degree of the initial part
    if fam == 'bin':      # binary initial form
        for i in range(d+1): put((i, d-i, 0, 0), rng.randrange(q))
    elif fam == 'line':   # power of a line
        put((d, 0, 0, 0), 1 + rng.randrange(q-1))
    elif fam == 'nonbin': # initial form involving y or z
        for _ in range(3):
            i = rng.randrange(d+1); l = rng.randrange(d+1-i); j = rng.randrange(d+1-i-l)
            put((i, l, j, d-i-l-j), 1 + rng.randrange(q-1))
    # tail of higher degree
    for _ in range(rng.randrange(1, 6)):
        i = rng.randrange(p); l = rng.randrange(p-i)
        e = rng.randrange(max(0, d+1-i-l), d+2*p)
        j = rng.randrange(e+1)
        put((i, l, j, e-j), 1 + rng.randrange(q-1))
    g = {(i, l, j+ry, k+rz): c for (i, l, j, k), c in G.items()}
    g = clean(F, g)
    return g

def walk(F, g, depth, rng, pnz=0.8, theta=None):
    ry, rz, d, rho = data(F, g)
    path = []
    # chart word with blocks of length 1..3 alternating: the Euclid word of an irrational theta
    word = []
    let = rng.choice('yz')
    while len(word) < depth:
        word += [let] * rng.randint(1, 3); let = 'y' if let == 'z' else 'z'
    for t in range(depth):
        forced = word[t]
        ch_ = children(F, g, rho, charts=forced)
        if not ch_: break
        nz = [c for c in ch_ if c[1] or c[2]]
        pool = nz if (nz and rng.random() < pnz) else ch_
        # keep both letters: bias to switch letter sometimes
        ch, a, b, g = rng.choice(pool)
        h = initial(F, g)
        ry, rz, d2, rho2 = data(F, g)
        path.append((ch, a, b, d2, rho2, binary(h), nu_curve(g, 'y'), nu_curve(g, 'z'), len(g)))
        if len(g) > 4000: break
    return path, g

def rank_dirs(F, trans):
    """rank over F_q of the set of translation vectors."""
    vs = [(a, b) for a, b in trans if a or b]
    if not vs: return 0
    a0, b0 = vs[0]
    for a, b in vs[1:]:
        if F.add[F.mul[a0][b]][F.neg[F.mul[b0][a]]]: return 2
    return 1

if __name__ == '__main__':
    p, k, fam, N, depth, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    F = GF(p, k); rng = random.Random(seed)
    st = dict(walks=0, deep=0, deep_nz=0, tail_rank2=0, h1fail=0, lfail=0, lfail_bin=0, line_end=0)
    for n in range(N):
        g0 = rand_g(F, rng, fam)
        if not g0 or ordg(g0) < p or degxw(g0) >= p: continue
        r0 = data(F, g0)[3]
        if r0 < 1: continue
        path, g = walk(F, g0, depth, rng)
        st['walks'] += 1
        if len(path) < depth: continue
        st['deep'] += 1
        tail = path[depth//2:]
        nzc = sum(1 for s_ in tail if s_[1] or s_[2])
        if nzc == 0: continue
        st['deep_nz'] += 1
        if rank_dirs(F, [(s_[1], s_[2]) for s_ in tail]) == 2: st['tail_rank2'] += 1
        last = path[-1]
        h = initial(F, g)
        if binary(h) and len(set(m[0] for m in h)) >= 1:
            pass
        bad_h1 = not last[5]
        bad_l = min(last[6], last[7]) < last[4]
        if bad_h1: st['h1fail'] += 1
        if bad_l:
            st['lfail'] += 1
            if last[5]: st['lfail_bin'] += 1
        if bad_h1 or bad_l:
            print(json.dumps(dict(g0=show(F, g0, 30), rho=r0, path=path, inG=show(F, h, 20))), flush=True)
    print('STATS', p, k, fam, depth, st, flush=True)
