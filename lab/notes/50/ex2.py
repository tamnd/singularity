import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
from fq import *
from walk import children
for p in (3, 5, 7):
    F = GF(p, 1)
    g = {(2, 0, p-2, p-2): 1, (0, 1, p-1, p-1): 1}
    rho = data(F, g)[3]
    g1 = step(F, g, 'y', 0, 1)
    out = []
    for c1, a1, b1, g2 in children(F, g1, rho):
        print(p, 'after y,b=1 then', c1, a1, b1, data(F, g2), show(F, g2, 6))
        for c2, a2, b2, g3 in children(F, g2, rho):
            out.append(c1 + c2)
    print(p, 'two-step continuations', sorted(set(out)))
