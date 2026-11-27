"""Referee 63: depth first search for corner runs with late translations of rank 2.

usage: search63.py p e cls D starts depth seed budget [timeper]
cls = bin   : y^(p-D) z^(p-D) (h(x, w) + y z R), h a binary form of degree D (D <= p)
cls = pcls  : B1 x^p + B2 w^p + B0 (+ low terms), the class of Corollary 3.17.17, rank 2
cls = gen   : random clean polynomial of (x, w)-degree D with ord >= p
"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, time
from core63 import Field, step, invariants, clean, addto, deg_xw


def binary_form(F, rng, D):
    mode = rng.random()
    h = {}
    if mode < 0.3:  # power of a line
        a, b = rng.randrange(F.q), rng.randrange(F.q)
        if a == 0 and b == 0:
            a = 1
        # (a x + b w)^D
        from math import comb
        for s in range(D + 1):
            c = F.mul[F.intc(comb(D, s))][F.mul[F.pw[a][s]][F.pw[b][D - s]]]
            addto(F, h, (s, D - s), c)
    else:
        for s in range(D + 1):
            if rng.random() < 0.6:
                addto(F, h, (s, D - s), rng.randrange(1, F.q))
        if not h:
            h[(D, 0)] = 1
    return h


def start(F, rng, cls, D):
    p = F.p
    g = {}
    if cls == 'bin':
        e = p - D
        for (s, t), c in binary_form(F, rng, D).items():
            addto(F, g, (s, t, e, e), c)
        for _ in range(rng.randint(1, 4)):
            i = rng.randint(0, D)
            l = rng.randint(0, D - i)
            j = e + rng.randint(1, p + 1)
            k = e + rng.randint(1, p + 1)
            addto(F, g, (i, l, j, k), rng.randrange(1, F.q))
    elif cls == 'pcls':
        a1, b1 = rng.choice([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (0, 0)]), None
        g[(p, 0, a1[0], a1[1])] = 1
        a2 = rng.choice([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (0, 0)])
        addto(F, g, (0, p, a2[0], a2[1]), rng.randrange(1, F.q))
        for _ in range(rng.randint(1, 3)):
            j = rng.randint(0, 2 * p + 2)
            k = rng.randint(max(0, p + 1 - j), 2 * p + 2)
            addto(F, g, (0, 0, j, k), rng.randrange(1, F.q))
        for _ in range(rng.randint(0, 2)):
            i = rng.randint(0, p - 1)
            l = rng.randint(0, p - 1 - i)
            if i + l == 0:
                continue
            j = rng.randint(p - 1, 2 * p)
            k = rng.randint(p - 1, 2 * p)
            addto(F, g, (i, l, j, k), rng.randrange(1, F.q))
    else:
        for _ in range(rng.randint(3, 7)):
            i = rng.randint(0, D)
            l = rng.randint(0, D - i)
            j = rng.randint(0, p + 2)
            k = rng.randint(max(0, p - i - l - j), p + 3)
            addto(F, g, (i, l, j, k), rng.randrange(1, F.q))
    return clean(F, g)


def rank2(vs):
    vs = [v for v in vs if v != (0, 0)]
    if len(vs) < 2:
        return False
    return None  # decided with the field below


def det(F, u, v):
    return F.add[F.mul[u[0]][v[1]]][F.neg[F.mul[u[1]][v[0]]]]


def is_rank2(F, vs):
    vs = [v for v in vs if v != (0, 0)]
    for v in vs[1:]:
        if det(F, vs[0], v):
            return True
    return False


class Budget(Exception):
    pass


def search(F, g0, word, budget, rng, late_from, tlimit):
    inv0 = invariants(F, g0)
    rho0 = inv0[4]
    p = F.p
    allT = [(a, b) for a in range(F.q) for b in range(F.q)]
    state = {'nodes': 0, 'deep': 0, 'planar': None, 't0': time.time()}

    def dfs(g, m, trans):
        if m == len(word):
            state['deep'] += 1
            late = trans[late_from:]
            if is_rank2(F, late):
                state['planar'] = (list(trans), g)
                return True
            return False
        late = [v for v in trans[late_from:] if v != (0, 0)]
        order = allT[:]
        rng.shuffle(order)
        if m >= late_from and late:
            v0 = late[0]
            order.sort(key=lambda t: 0 if det(F, v0, t) else 1)
        elif m >= late_from:
            order.sort(key=lambda t: 0 if t != (0, 0) else 1)
        for t in order:
            state['nodes'] += 1
            if state['nodes'] > budget or time.time() - state['t0'] > tlimit:
                raise Budget()
            try:
                h = step(F, g, word[m], t[0], t[1])
            except ValueError:
                continue
            inv = invariants(F, h)
            if inv is None or inv[4] != rho0 or inv[0] < p:
                continue
            if dfs(h, m + 1, trans + [t]):
                return True
        return False

    try:
        dfs(g0, 0, [])
        status = 'done'
    except Budget:
        status = 'budget'
    return status, state


def extend(F, g, rho0, word2):
    """can the end point g take one more step of each letter with rho kept?"""
    res = {}
    for ch in 'yz':
        cnt = 0
        for a in range(F.q):
            for b in range(F.q):
                try:
                    h = step(F, g, ch, a, b)
                except ValueError:
                    continue
                inv = invariants(F, h)
                if inv and inv[4] == rho0 and inv[0] >= F.p:
                    cnt += 1
        res[ch] = cnt
    return res


def word_blocks(rng, depth):
    w = []
    ch = rng.choice('yz')
    while len(w) < depth:
        w += [ch] * rng.randint(1, 3)
        ch = 'z' if ch == 'y' else 'y'
    return w[:depth]


if __name__ == '__main__':
    p, e, cls, D, nstarts, depth, seed, budget = sys.argv[1:9]
    p, e, D, nstarts, depth, seed, budget = int(p), int(e), int(D), int(nstarts), int(depth), int(seed), int(budget)
    tlimit = float(sys.argv[9]) if len(sys.argv) > 9 else 120.0
    F = Field(p, e)
    rng = random.Random(seed)
    stats = {'starts': 0, 'deep': 0, 'rank2': 0, 'budget': 0, 'dead_end_rank2': 0}
    t0 = time.time()
    tried = 0
    while stats['starts'] < nstarts and tried < 50 * nstarts:
        tried += 1
        g = start(F, rng, cls, D)
        if not g:
            continue
        inv = invariants(F, g)
        if inv is None or inv[4] < 1 or inv[0] < p:
            continue
        if cls != 'pcls' and deg_xw(g) != D:
            continue
        word = word_blocks(rng, depth)
        status, st = search(F, g, word, budget, rng, depth // 3, tlimit)
        stats['starts'] += 1
        if st['deep'] > 0 or st['planar']:
            stats['deep'] += 1
        if status == 'budget':
            stats['budget'] += 1
        if st['planar']:
            stats['rank2'] += 1
            trans, gend = st['planar']
            ext = extend(F, gend, inv[4], None)
            if ext['y'] == 0 and ext['z'] == 0:
                stats['dead_end_rank2'] += 1
            print('RANK2 start', sorted(g.items()), 'rho', inv[4], 'word', ''.join(word), 'trans', trans,
                  'end', invariants(F, gend), 'extensions', ext, flush=True)
    print(p, e, cls, D, 'depth', depth, 'budget', budget, stats, 'time %.0f' % (time.time() - t0), flush=True)
