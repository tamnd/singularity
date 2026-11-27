"""Driver: random starts of a class; criterion 1 (note 54 style: rank 2 after L/3, depth L1)
and criterion 2 (rank 2 in both windows [L/3,2L/3) and [2L/3,L), depth L2).
usage: runs63.py p e cls D nstarts L1 L2 seed budget tlimit"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, time
from core63 import Field, invariants, deg_xw
from search63 import start, search, extend, word_blocks
import deep63

p, e, cls, D, nstarts, L1, L2, seed, budget, tlimit = sys.argv[1:11]
p, e, D, nstarts, L1, L2, seed, budget = map(int, (p, e, D, nstarts, L1, L2, seed, budget))
tlimit = float(tlimit)
F = Field(p, e); rng = random.Random(seed)
S = {'starts': 0, 'deep1': 0, 'rank2_1': 0, 'dead1': 0, 'budget1': 0, 'deep2': 0, 'rank2_2': 0, 'budget2': 0}
t0 = time.time(); tried = 0
while S['starts'] < nstarts and tried < 100 * nstarts:
    tried += 1
    g = start(F, rng, cls, D)
    if not g:
        continue
    inv = invariants(F, g)
    if inv is None or inv[4] < 1 or inv[0] < p:
        continue
    if cls != 'pcls' and deg_xw(g) != D:
        continue
    S['starts'] += 1
    w = word_blocks(rng, L1)
    status, st = search(F, g, w, budget, rng, L1 // 3, tlimit)
    S['deep1'] += 1 if (st['deep'] or st['planar']) else 0
    S['budget1'] += status == 'budget'
    if st['planar']:
        S['rank2_1'] += 1
        ext = extend(F, st['planar'][1], inv[4], None)
        if ext['y'] == 0 and ext['z'] == 0:
            S['dead1'] += 1
        print('C1 start', sorted(g.items()), 'word', ''.join(w), 'trans', st['planar'][0], 'ext', ext, flush=True)
    w2 = word_blocks(rng, L2)
    status, st = deep63.run(F, g, w2, budget, rng, tlimit)
    S['deep2'] += st['best'] == L2
    S['budget2'] += status == 'budget'
    if st['found']:
        S['rank2_2'] += 1
        print('C2 start', sorted(g.items()), 'word', ''.join(w2), 'found', st['found'], flush=True)
    if S['starts'] % 10 == 0:
        print('progress', S, 'time %.0f' % (time.time() - t0), flush=True)
print('FINAL', p, e, cls, D, 'L1', L1, 'L2', L2, 'budget', budget, S, 'time %.0f' % (time.time() - t0), flush=True)
