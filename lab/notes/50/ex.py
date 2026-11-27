import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
from fq import *
from walk import children
for p in (3, 5):
    F = GF(p, 1)
    g = {(2, 0, p-2, p-2): 1, (0, 1, p-1, p-1): 1}
    print('p', p, data(F, g), show(F, g, 8))
    for ch in 'yz':
        for b in range(p):
            g2 = step(F, g, ch, 0, b)
            if g2 is None: continue
            print(' ', ch, b, data(F, g2), show(F, g2, 8), 'children', [(c, a, bb) for c, a, bb, _ in children(F, g2, data(F, g)[3])])
