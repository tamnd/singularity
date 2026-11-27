import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sys, random
from walk61 import *
def trace(p, fam, depth, mode, seed=0, pick='origin'):
    ctx=Ctx(p); rng=random.Random(seed)
    a,E=family(fam,ctx,random.Random(99))  # 99: no hiding for most
    a,info=E_adapt(a,ctx)
    for t in range(depth):
        inv=invariants(a,E,ctx)
        S,kind=choose_centre(a,E,inv,ctx,mode)
        print(t, sorted(E), inv['regime'], 'om*',inv['omega'],'d',inv['delta'],'mu',{k:str(v) for k,v in inv['mu'].items()}, kind, S, '|', [fmt(x) for x in a[1:] ][:], flush=True)
        pts=[x for x in points_over(a,S,ctx,allnu=False)]
        if not pts: print('drop'); return
        for (j,lam,nu,b) in pts:
            E2=new_E(E,S,j,lam); i2=invariants(b,E2,ctx)
            print('     pt j',j,lam,i2['regime'],'om*',i2['omega'])
        x = pts[0] if pick=='origin' else rng.choice(pts)
        j,lam,nu,b=x; E=new_E(E,S,j,lam); a,info=E_adapt(b,ctx)
trace(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], pick=sys.argv[5] if len(sys.argv)>5 else 'origin')
