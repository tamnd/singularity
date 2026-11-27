import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
import linwalk; from linwalk import walk, check; linwalk.PNZ=0.1
for p,e in ((3,1),(5,2),(7,1)):
    K=F(p,e); random.seed(7*p+e); out=[]
    for _ in range(200):
        d=random.randint(2,p-1); a=b=p-d
        Gp={(d,0,0,0):1,(0,1,d-1,d-1):K.rand(True)}
        for _ in range(random.randint(0,4)):
            i=random.randint(0,p-1); l=random.randint(0,p-1-i)
            Gp[(i,l,d+random.randint(0,2),d+random.randint(0,2))]=K.rand(True)
        gp=clean(K,{(i,l,j+a,k+b):co for (i,l,j,k),co in Gp.items()})
        c=K.rand(); g=subst_x(K,gp,c)
        r=walk(K,g,c,18)
        if r is None: continue
        gm,trans,rho=r
        ch=check(K,gm,c,rho)
        bad=not(ch['form'] and ch['drho'] and ch['curves'] and ch['surf'])
        last=max([i for i,t in enumerate(trans) if t!=(0,0)],default=-1)
        out.append((bad,last,ch))
    print(p,e,'fail lastnz:',sorted(set(o[1] for o in out if o[0])),' pass lastnz:',sorted(set(o[1] for o in out if not o[0])))
    print('  sample fail', [o[2] for o in out if o[0]][:1])
