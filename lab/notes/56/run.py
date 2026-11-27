import random, sys, time, math
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tower import Ring, tower

def fam(p, n=5):
    """f_p = z^2 + 2 z a + (a^2)_{<p}, a = -x^2/2 + x^{p-2} + y^{(p+1)/2};
    variables (x, y, w, v, z) = indices 0..4."""
    R = Ring(n, p, p + 2)
    inv2 = pow(2, p - 2, p)
    def mono(**k):
        e = [0] * n
        for name, d in k.items(): e['xywvz'.index(name)] = d
        return tuple(e)
    a = {mono(x=2): (-inv2) % p, mono(x=p - 2): 1, mono(y=(p + 1) // 2): 1}
    a2 = R.mul(a, a)
    c = {e: v for e, v in a2.items() if sum(e) < p}
    f = {mono(z=2): 1}
    for e, v in a.items():
        ee = list(e); ee[4] += 1
        f[tuple(ee)] = (f.get(tuple(ee), 0) + 2 * v) % p
    f = R.add(f, c)
    return R, f

def rand_germ(R, b, d, nterms):
    n, p = R.n, R.p
    f = {}
    # initial form: random form of degree b with a few terms
    for _ in range(nterms):
        deg = random.choice([b] * 2 + list(range(b, d + 1)))
        e = [0] * n
        for _ in range(deg): e[random.randrange(n)] += 1
        f[tuple(e)] = random.randrange(1, p)
    if min(sum(e) for e in f) != b:
        e = [0] * n; e[random.randrange(n)] = b; f[tuple(e)] = 1
    return f

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'fam':
        for p in [7, 11, 13, 29, 31, 37, 41, 43]:
            random.seed(p)
            R, f = fam(p)
            deg = max(sum(e) for e in f)
            t = time.time()
            log = tower(R, [f], maxlev=3)
            print(p, 'deg f =', deg, 'ord f =', min(sum(e) for e in f), log, '%.1fs' % (time.time() - t))
    elif mode == 'rand':
        p = int(sys.argv[2]); b = int(sys.argv[3]); N = int(sys.argv[4]); nt = int(sys.argv[5])
        random.seed(1000 * p + b)
        stats = {}
        R = Ring(5, p, p + 1)
        for s in range(N):
            d = random.randrange(b + 1, p)
            f = rand_germ(R, b, d, nt)
            log = tower(R, [f], maxlev=3, ncomb=2)
            key = tuple((l[2], l[3].split(':')[0]) for l in log)
            stats[key] = stats.get(key, 0) + 1
        for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
            print(v, k)

def fam2(p, n=5):
    """low-degree variant: a = x^{(p-1)/2} - x^{(p+1)/2}/2 + y^{(p+3)/2}; deg f = (p+5)/2."""
    R = Ring(n, p, p + 2)
    inv2 = pow(2, p - 2, p)
    def mono(**k):
        e = [0] * n
        for name, d in k.items(): e['xywvz'.index(name)] = d
        return tuple(e)
    a = {mono(x=(p - 1) // 2): 1, mono(x=(p + 1) // 2): (-inv2) % p, mono(y=(p + 3) // 2): 1}
    a2 = R.mul(a, a)
    c = {e: v for e, v in a2.items() if sum(e) < p}
    f = {mono(z=2): 1}
    for e, v in a.items():
        ee = list(e); ee[4] += 1
        f[tuple(ee)] = (f.get(tuple(ee), 0) + 2 * v) % p
    return R, R.add(f, c)

if __name__ == '__main__' and sys.argv[1] == 'fam2':
    for p in [7, 11, 13, 29, 31, 37, 41, 43]:
        random.seed(p)
        R, f = fam2(p)
        print(p, 'deg f =', max(sum(e) for e in f), tower(R, [f], maxlev=3))
