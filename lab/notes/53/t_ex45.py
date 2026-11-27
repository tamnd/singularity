import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Omega along the first step of the example of Proposition 2.1 (Example 4.5 of note 44), own code.
from lib53 import *
for p in (3,5,7):
    ctx=Ctx(p); m=ctx.m
    a=[{(0,0,0):1}]+[{} for _ in range(m)]
    a[1]={(3,0,0):1}; a[m]={(0,4*p+1,0):1}
    E=frozenset()
    out=[f"p={p} origin {regime(a,ctx)} iota={iota(a,E,ctx)}"]
    for j,lam,nu,b in points_over(a,(0,1),ctx):
        b2,n,l=adapt(b,ctx); E2=new_E(E,(0,1),j,lam)
        out.append(f"  chart x{j} lam={lam} nu={nu}: {regime(b2,ctx)} iota={iota(b2,E2,ctx)}")
    print("\n".join(out))
