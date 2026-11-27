import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
import linwalk; from linwalk import walk, check; linwalk.PNZ=0.1
# Step 3 (tie) class: Y (X^d + u (yz)^(d-1) W + terms of high value)
for p,e in ((3,1),(3,2),(5,1),(5,2),(7,1),(7,2)):
    K=F(p,e); random.seed(7*p+e); st=dict(deep=0,fail=0,surfeq=0,nzlate=0)
    for _ in range(200):
        d=random.randint(2,p-1); a=b=p-d
        while a+b+d<p: a+=1
        Gp={(d,0,0,0):1,(0,1,d-1,d-1):K.rand(True)}
        for _ in range(random.randint(0,4)):
            i=random.randint(0,p-1); l=random.randint(0,p-1-i)
            Gp[(i,l,d+random.randint(0,2),d+random.randint(0,2))]=K.rand(True)
        gp=clean(K,{(i,l,j+a,k+b):co for (i,l,j,k),co in Gp.items()})
        c=K.rand(); g=subst_x(K,gp,c)
        r=walk(K,g,c,18)
        if r is None: continue
        gm,trans,rho=r; st['deep']+=1
        st['nzlate']+=sum(t!=(0,0) for t in trans[9:])
        ch=check(K,gm,c,rho)
        if not(ch['form'] and ch['drho'] and ch['curves'] and ch['surf']): st['fail']+=1
        if ch['surf_eq_rho']: st['surfeq']+=1
    print(p,e,st)
