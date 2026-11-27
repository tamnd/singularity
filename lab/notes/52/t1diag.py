import os, sys, random, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import F
from t1 import run, randpoly
def linear_tail(K, trans, start):
    # is there lambda=(l1,l2) != 0 with l1*a+l2*b=0 for all tail translations?
    tail = trans[start:]
    for l1 in range(K.q):
        for l2 in range(K.q):
            if (l1,l2)==(0,0): continue
            if all(K.add[K.mul[l1][a]][K.mul[l2][b]]==0 for a,b in tail): return True
    return False
for (p,e) in ((3,1),(3,2),(5,1),(5,2),(7,1),(7,2)):
    K=F(p,e)
    for theta in (math.sqrt(2)-1,(math.sqrt(5)-1)/2):
        random.seed(1000*p+10*e+1)
        bad=0; badlin=0; empty=0
        for _ in range(30 if K.q>9 else 60):
            alpha=randpoly(K,random.randint(1,3)); beta=randpoly(K,random.randint(1,3))
            if random.random()<0.5:
                c=K.rand(True); beta={k:K.mul[c][x] for k,x in alpha.items()}
                beta[(random.randint(1,3),random.randint(0,2))]=K.rand(True)
            gamma=randpoly(K,random.randint(0,3))
            hist,trans=run(K,theta,22,alpha,beta,gamma,'adv')
            vmin=min(a+theta*b for (a,b) in list(alpha)+list(beta))
            if hist[-1][1] is None: empty+=1; badlin+=linear_tail(K,trans,6); bad+=1; continue
            if not hist[-1][1]<vmin+1+theta:
                bad+=1; badlin+=linear_tail(K,trans,6)
        print(p,e,round(theta,3),'T1 fails',bad,'of which tail linear',badlin,'(f=0:',empty,')')
