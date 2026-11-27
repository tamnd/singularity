import random, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tower import Ring, tower
# f = z^2 + 2 z (x^r + x^(p-r)) + x^(2r), deg f = max(2r, p-r+1)
def fam3(p, r, n=5):
    R = Ring(n, p, p + 2)
    def m(**k):
        e = [0] * n
        for a, d in k.items(): e['xywvz'.index(a)] = d
        return tuple(e)
    f = {m(z=2): 1, m(z=1, x=r): 2 % p, m(z=1, x=p - r): 2 % p, m(x=2 * r): 1}
    return R, f
for p in [7, 11, 13, 17, 29, 31, 41]:
    best = min(range(1, (p - 1) // 2 + 1), key=lambda r: max(2 * r, p - r + 1))
    random.seed(p)
    R, f = fam3(p, best)
    print(p, 'r =', best, 'deg f =', max(sum(e) for e in f), tower(R, [f], maxlev=3))
