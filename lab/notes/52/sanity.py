import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
# Example 3.17.22 and Example 6.1, Prop 3.17.8 sanity
for p in (3,5,7):
    K=F(p)
    Y=(p-2,p-2)
    g={(2,0,p-2,p-2):1,(0,1,p-1,p-1):1}   # Example 6.1
    I=invariants(K,g); print(p,'ex6.1',I['rho'],I['d'],I['curve_y'],I['surf_y'])
    for ch in 'yz':
        print(' origin',ch, step(K,g,ch,0,0)==g)
    g1=step(K,g,'y',0,1); I=invariants(K,g1); print(' after (0,1):',sorted(g1.items()),I['rho'],I['d'])
    if p>=5:
        g={(4,0,p-4,p-4):1,(0,3,p-3,p-3):1}
        I=invariants(K,g); print(p,'ex3.17.22 rho',I['rho'],'d',I['d'],'surf_y',I['surf_y'],'curve',I['curve_y'], 'fixed', step(K,g,'y',0,0)==g, step(K,g,'z',0,0)==g)
