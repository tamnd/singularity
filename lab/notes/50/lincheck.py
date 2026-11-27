# Deep linear runs (translations in ker x): check the conclusions of Theorem B at the end of the walk:
# in G = c x^d, d = rho + 1, corner curves nu^G >= d, corner surfaces V(x,y), V(x,z) nu^G >= rho.
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random
from fq import *
from walk import walk, rand_g
p, k, N, depth, seed = map(int, sys.argv[1:6])
F = GF(p, k); rng = random.Random(seed)
st = dict(deep_lin=0, inG_xd=0, d_eq_rho1=0, curves_ge_d=0, curves_ge_rho=0, surf_ge_rho=0)
for n in range(N):
    g0 = rand_g(F, rng, 'line')
    if not g0 or ordg(g0) < p or degxw(g0) >= p or data(F, g0)[3] < 1: continue
    path, g = walk(F, g0, depth, rng, pnz=0.9)
    if len(path) < depth: continue
    tail = path[depth//2:]
    if not any(s[2] for s in tail): continue
    if any(s[1] for s in tail): continue   # only runs with translations in ker x in the tail
    st['deep_lin'] += 1
    ry, rz, d, rho = data(F, g); h = initial(F, g)
    st['inG_xd'] += all(m == (d, 0, 0, 0) for m in h)
    st['d_eq_rho1'] += (d == rho + 1)
    cy, cz = nu_curve(g, 'y'), nu_curve(g, 'z')
    st['curves_ge_d'] += min(cy, cz) >= d
    st['curves_ge_rho'] += min(cy, cz) >= rho
    sy, sz = nu_surf(g, 'y'), nu_surf(g, 'z')
    st['surf_ge_rho'] += min(sy, sz) >= rho
    if min(sy, sz) < rho or min(cy, cz) < d:
        print('CASE', show(F, g0, 20), path[-1], (cy, cz, sy, sz), flush=True)
print('STATS', p, k, depth, st, flush=True)
