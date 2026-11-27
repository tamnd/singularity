"""Deep search from given starts: is there a branch of depth L whose translations in each of the
windows [L/3, 2L/3) and [2L/3, L) have rank 2?  usage: deep63.py p e L budget seed startrepr"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, time, ast
from core63 import Field, step, invariants
from search63 import det, is_rank2, word_blocks

def run(F, g0, word, budget, rng, tlimit=300):
    rho0 = invariants(F, g0)[4]
    L = len(word); w1, w2 = L // 3, (2 * L) // 3
    allT = [(a, b) for a in range(F.q) for b in range(F.q)]
    st = {'nodes': 0, 'best': 0, 't0': time.time(), 'found': None}
    def ok(trans):
        return is_rank2(F, trans[w1:w2]) and is_rank2(F, trans[w2:])
    def dfs(g, m, trans):
        st['best'] = max(st['best'], m)
        if m == L:
            if ok(trans):
                st['found'] = (trans, invariants(F, g)); return True
            return False
        order = allT[:]; rng.shuffle(order)
        win = trans[w2:] if m >= w2 else trans[w1:] if m >= w1 else []
        nz = [v for v in win if v != (0, 0)]
        if m >= w1:
            if nz:
                order.sort(key=lambda t: 0 if det(F, nz[0], t) else (1 if t != (0, 0) else 2))
            else:
                order.sort(key=lambda t: 0 if t != (0, 0) else 1)
        for t in order:
            st['nodes'] += 1
            if st['nodes'] > budget or time.time() - st['t0'] > tlimit:
                raise TimeoutError
            try:
                h = step(F, g, word[m], *t)
            except ValueError:
                continue
            inv = invariants(F, h)
            if inv is None or inv[4] != rho0 or inv[0] < F.p:
                continue
            if dfs(h, m + 1, trans + [t]):
                return True
        return False
    try:
        dfs(g0, 0, []); status = 'done'
    except TimeoutError:
        status = 'budget'
    return status, st

if __name__ == '__main__':
    p, e, L, budget, seed = map(int, sys.argv[1:6])
    g0 = dict(ast.literal_eval(sys.argv[6]))
    word = sys.argv[7] if len(sys.argv) > 7 else None
    F = Field(p, e); rng = random.Random(seed)
    if word is None or word == 'blocks':
        word = word_blocks(rng, L)
    else:
        word = (word * L)[:L]
    status, st = run(F, g0, list(word), budget, rng)
    print('L', L, 'word', ''.join(word), status, 'nodes', st['nodes'], 'max depth', st['best'], 'found', st['found'])
