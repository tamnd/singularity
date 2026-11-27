# Rerun the family of Prop 7.2 of note 56 with the tower code of note 56 (../56/tower.py),
# for more primes and for all admissible r, plus the plain germ z^2 - x^p.
import random, sys
import os
# The folder of tower.py: the first argument, or ../56 next to this script.
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '56'))
from tower import Ring, tower
def mono(n, **k):
    e = [0] * n
    for a, d in k.items(): e['xywvz'.index(a)] = d
    return tuple(e)
def fam3(p, r, n=5):
    R = Ring(n, p, p + 2)
    f = {mono(n, z=2): 1, mono(n, z=1, x=r): 2 % p, mono(n, z=1, x=p - r): 2 % p, mono(n, x=2 * r): 1}
    return R, f
for p in [5, 7, 11, 13, 19, 23]:
    for r in range(1, (p - 1) // 2 + 1):
        random.seed(p * 100 + r)
        R, f = fam3(p, r)
        print(p, r, 'deg', max(sum(e) for e in f), tower(R, [f], maxlev=3))
    random.seed(p)
    R = Ring(5, p, p + 2)
    g = {mono(5, z=2): 1, mono(5, x=p): p - 1}
    print(p, 'z^2-x^p', tower(R, [g], maxlev=3))
