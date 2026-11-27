"""Positive control for criterion 2: same search as deep63.run, but the rho condition is dropped
(only ord >= p is kept), so rank-2 branches should be found if the machinery works.
usage: control63.py p e cls D nstarts L seed budget"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random
import core63, deep63
from search63 import start
p, e, cls, D, n, L, seed, budget = sys.argv[1:9]
p, e, D, n, L, seed, budget = map(int, (p, e, D, n, L, seed, budget))
F = core63.Field(p, e); rng = random.Random(seed)
real = core63.invariants
def fake(F_, g):
    inv = real(F_, g)
    return None if inv is None else inv[:4] + (0,)
deep63.invariants = fake
found = starts = 0
tries = 0
while starts < n and tries < 100 * n:
    tries += 1
    g = start(F, rng, cls, D)
    inv = real(F, g) if g else None
    if inv is None or inv[0] < p:
        continue
    starts += 1
    from search63 import word_blocks
    st, S = deep63.run(F, g, word_blocks(rng, L), budget, rng, 60)
    found += S['found'] is not None
print('control', p, e, cls, D, 'L', L, 'starts', starts, 'criterion-2 hits without rho condition', found)
