"""Control and follow-up for deg2.py: (a) count starts with any walk to full depth (any translations);
(b) for each start with a branch whose late translations span the plane, extend it as far as possible
and report the longest extension that keeps rho and uses both letters, and the invariants at its end."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import *
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deg2.py')).read().split('p,e,n,depth,seed')[0])
def dfs2(K,g,rho,word,s0,ts,budget,need_planar):
    budget[0]-=1
    if budget[0]<0: raise TimeoutError
    if not word: return (ts,g) if (not need_planar or not online(K,ts[s0:])) else None
    for a in range(K.q):
        for b in range(K.q):
            try: g2=step(K,g,word[0],a,b)
            except AssertionError: continue
            I=invariants(K,g2)
            if I and I['rho']==rho and I['ordg']>=K.p:
                r=dfs2(K,g2,rho,word[1:],s0,ts+[(a,b)],budget,need_planar)
                if r: return r
    return None
def extend(K,g,rho,maxlen=8):
    best=0
    for L in range(1,maxlen+1):
        found=False
        for w in itertools.product('yz',repeat=L):
            if L>=2 and len(set(w))<2: continue
            try:
                if dfs2(K,g,rho,list(w),0,[],[3000],False): found=True; break
            except TimeoutError: pass
        if not found: return best
        best=L
    return best
p,e,n,depth,seed=map(int,sys.argv[1:6]); random.seed(seed); K=F(p,e)
st=dict(starts=0,any_deep=0,planar=0,to=0); ext=[]
for _ in range(n):
    g=start(K,p); I=invariants(K,g)
    if not I or I['ordg']<p or I['rho']<1: continue
    st['starts']+=1
    w=[];cur=random.choice('yz')
    while len(w)<depth: w+=[cur]*random.randint(1,2); cur='z' if cur=='y' else 'y'
    w=w[:depth]
    try:
        if dfs2(K,g,I['rho'],w,depth,[],[5000],False): st['any_deep']+=1
        r=dfs2(K,g,I['rho'],w,depth//3,[],[20000],True)
    except TimeoutError: st['to']+=1; continue
    if r:
        st['planar']+=1; ts,gm=r; J=invariants(K,gm)
        ext.append((ts[depth//3:], J['d'], J['rho'], extend(K,gm,I['rho'])))
print(p,e,'depth',depth,st,'planar branches (late translations, d, rho, longest 2-letter extension):',ext,flush=True)
