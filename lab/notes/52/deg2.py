"""Note 52, Theorem 4.3: no planar corner run with deg_{x,w} g <= 2.
DFS over walks of given depth (alternating-block words), all translations; a walk is planar-like
if its translations after step s0 are not all on one line through 0. Count starts admitting such a walk."""
import os, sys, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
def start(K,p):
    d=2; a=b=p-d
    G={}
    for (i,l) in ((2,0),(1,1),(0,2)):
        if random.random()<0.7: G[(i,l,0,0)]=K.rand(True)
    if not G: G[(2,0,0,0)]=1
    for _ in range(random.randint(1,5)):
        i=random.randint(0,2); l=random.randint(0,2-i); j=random.randint(0,3); k=random.randint(0,3)
        if i+l+j+k<=2: j+=1;k+=1
        G[(i,l,j,k)]=K.rand(True)
    return clean(K,{(i,l,j+a,k+b):c for (i,l,j,k),c in G.items()})
def online(K,ts):
    for l1 in range(K.q):
        for l2 in range(K.q):
            if (l1,l2)!=(0,0) and all(K.add[K.mul[l1][a]][K.mul[l2][b]]==0 for a,b in ts): return True
    return False
def dfs(K,g,rho,word,s0,ts,budget):
    budget[0]-=1
    if budget[0]<0: raise TimeoutError
    if not word: return not online(K,ts[s0:])
    for a in range(K.q):
        for b in range(K.q):
            try: g2=step(K,g,word[0],a,b)
            except AssertionError: continue
            I=invariants(K,g2)
            if I and I['rho']==rho and I['ordg']>=K.p:
                if dfs(K,g2,rho,word[1:],s0,ts+[(a,b)],budget): return True
    return False
p,e,n,depth,seed=map(int,sys.argv[1:6]); random.seed(seed); K=F(p,e)
st=dict(starts=0,alive_any=0,planar_alive=0,timeout=0)
for _ in range(n):
    g=start(K,p); I=invariants(K,g)
    if not I or I['ordg']<p or I['rho']<1: continue
    st['starts']+=1
    w=[];cur=random.choice('yz')
    while len(w)<depth: w+=[cur]*random.randint(1,2); cur='z' if cur=='y' else 'y'
    w=w[:depth]
    try:
        if dfs(K,g,I['rho'],w,depth//3,[],[20000]): st['planar_alive']+=1
    except TimeoutError: st['timeout']+=1
print(p,e,'depth',depth,st,flush=True)
