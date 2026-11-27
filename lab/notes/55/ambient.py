"""Remark 55.12: for F = z^5 + x^4 y + x y^4 over F_25, move the three
singular lines of {F=0} to the coordinate axes by a linear change of all
three coordinates (x, y, z), and test Newton nondegeneracy of the result."""
import itertools, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gfq import *
from prep import faces
F = GF(5, 2)
# cube roots of unity
roots = [a for a in F.elements() if a and F.pw(a, 3) == 1]
print('cube roots of 1:', roots)
three = F.frompf(3)
cols = [(1, z, F.mul(three, F.mul(z, z))) for z in roots]
Fpoly = {(0, 0, 5): 1, (4, 1, 0): 1, (1, 4, 0): 1}   # variables (x, y, z)
# check the lines lie in Sing
d = [mderiv(F, Fpoly, i) for i in range(3)]
for c in cols:
    print('F, dF on line:', meval(F, Fpoly, c), [meval(F, di, c) for di in d])
images = []
for i in range(3):
    im = {}
    for j in range(3):
        if cols[j][i]:
            e = [0, 0, 0]; e[j] = 1
            im[tuple(e)] = cols[j][i]
    images.append(im)
G = mcompose(F, Fpoly, images, 3)
print('number of terms of F o B:', len(G), ' p-th power monomials:', [e for e in G if all(i % 5 == 0 for i in e)])
def seg_sing(f):
    E = sorted(f); a0 = E[0]
    d = [E[-1][i] - a0[i] for i in range(3)]
    from math import gcd
    g = 0
    for x in d: g = gcd(g, abs(x))
    u = [x // g for x in d]
    k = next(i for i in range(3) if u[i])
    polys = []
    P0 = [0] * (g + 1)
    for e, c in f.items():
        P0[(e[k] - a0[k]) // u[k]] = c
    polys.append(P0)
    for i in range(3):
        P = [0] * (g + 1)
        for e, c in f.items():
            j = (e[k] - a0[k]) // u[k]
            P[j] = F.mul(c, (a0[i] + j * u[i]) % 5)
        polys.append(P)
    Gc = []
    for P in polys:
        Gc = ugcd(F, Gc, P) if Gc else utrim(P)
    Gc = utrim(Gc)
    while Gc and Gc[0] == 0: Gc = Gc[1:]
    return len(Gc) > 1
bad = []
for f in faces(G, (1, 1, 1), 3):
    E = sorted(f); a0 = E[0]
    dd = [[e[i] - a0[i] for i in range(3)] for e in E[1:]]
    rank2 = any(any(x[i]*y[j]-x[j]*y[i] for i in range(3) for j in range(3)) for x, y in itertools.combinations(dd, 2))
    if not rank2 and seg_sing(f):
        bad.append(sorted(f))
print('degenerate edges:', bad)
print('vertices that are p-th powers or monomials vanishing... vertices are monomials: no torus zeros')
