import os, sys, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
import linwalk; from linwalk import walk, check; linwalk.PNZ=0.1
def survive(K,g,rho,word):
    if not word: return True
    for a in range(K.q):
        for b in range(K.q):
            try: g2=step(K,g,word[0],a,b)
            except AssertionError: continue
            I=invariants(K,g2)
            if I and I['rho']==rho and I['ordg']>=K.p and survive(K,g2,rho,word[1:]): return True
    return False
for p,e in ((3,1),(5,1),(7,1),(3,2)):
    K=F(p,e); random.seed(7*p+e); nf=0; alive=0
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
        gm,trans,rho=r; ch=check(K,gm,c,rho)
        if not(ch['form'] and ch['drho'] and ch['curves'] and ch['surf']):
            nf+=1
            if any(survive(K,gm,rho,w) for w in (('y','z','y'),('z','y','z'),('y','y','z'),('z','z','y'))): alive+=1
    print(p,e,'failing endpoints',nf,'with a 3-step continuation using both letters',alive)
