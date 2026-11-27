"""Lemma 2.1 of note 50: a Laurent monomial Q of positive value has both exponents -> infinity along the run.
The word is the Euclid word of a random theta (y-chart iff v(z) > v(y)), so v(y_m), v(z_m) > 0 throughout."""
import random
from decimal import Decimal, getcontext; getcontext().prec = 200
random.seed(21); bad=0; tot=0; worst=0
for trial in range(3000):
    n_=random.randint(2,400)
    while int(n_**0.5)**2==n_: n_+=1
    theta=(Decimal(n_).sqrt()/random.randint(1,9))%3+Decimal("0.001")
    a=random.randint(-40,40); b=random.randint(-40,40)
    if a+theta*b<=0: continue
    tot+=1
    vy,vz=Decimal(1),theta; e=(a,b); first=None
    for m in range(150):
        if vz>vy: e=(e[0]+e[1],e[1]); vz-=vy      # y-chart: z_m = y_{m+1} z_{m+1}
        else: e=(e[0],e[0]+e[1]); vy-=vz          # z-chart
        if first is None and e[0]>=0 and e[1]>=0: first=m
        if first is not None: assert e[0]>=0 and e[1]>=0
    if min(e)<5: bad+=1
    worst=max(worst, first if first is not None else 999)
print('cases',tot,'min exponent < 5 after 150 steps',bad,'latest first level with both exponents >= 0',worst)
