# Test of Theorem T_{<p} (Conjecture T in degree < p) on planar sequences.
# Laurent polynomials in (y_N, z_N): dict {(a, b): c} over F_q. Value v(y^a z^b) = a + b*theta.
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, random, math
from fq import GF, padd

def lmul(F, A, B):
    out = {}
    for (a, b), c in A.items():
        for (a2, b2), c2 in B.items():
            padd(F, out, (a+a2, b+b2), F.mul[c][c2])
    return out

def ladd(F, A, B):
    out = dict(A)
    for m, c in B.items(): padd(F, out, m, c)
    return out

def lead(A, th):
    if not A: return None
    m = min(A, key=lambda e: e[0] + e[1]*th)
    return m, m[0] + m[1]*th

p, k, trials, steps, seed = map(int, sys.argv[1:6])
F = GF(p, k); rng = random.Random(seed)
th = math.sqrt(2) - 1 if seed % 2 else (math.sqrt(5) - 1) / 2
# word from Euclid on (1, th): y-chart when v(y) < v(z)
vy, vz = 1.0, th; word = []
for _ in range(steps):
    if vy < vz: word.append('y'); vz -= vy
    else: word.append('z'); vy -= vz
# level-m coordinates as Laurent monomials in y_N, z_N
Y, Z = (1, 0), (0, 1); Ms = [(0, 0)]
for ch in word:
    if ch == 'y': Z = (Z[0]-Y[0], Z[1]-Y[1]); L = Y
    else: Y = (Y[0]-Z[0], Y[1]-Z[1]); L = Z
    Ms.append((Ms[-1][0]+L[0], Ms[-1][1]+L[1]))
bad = 0; ok = 0
for t in range(trials):
    # planar translations: random nonzero vectors, many directions
    trans = [(rng.randrange(F.q), rng.randrange(F.q)) for _ in range(steps)]
    deg = rng.randrange(1, p)
    # random f in F_q[y,z][X,W] of degree deg
    f = {}
    for _ in range(rng.randrange(2, 7)):
        i = rng.randrange(deg+1); l = rng.randrange(deg+1-i)
        f[(i, l, rng.randrange(3), rng.randrange(3))] = 1 + rng.randrange(F.q-1)
    def evalf(fd, phi, psi):
        out = {}
        pw = {}
        def power(P, n):
            if (id(P), n) not in pw:
                R = {(0, 0): 1}
                for _ in range(n): R = lmul(F, R, P)
                pw[(id(P), n)] = R
            return pw[(id(P), n)]
        for (i, l, a, b), c in fd.items():
            T = lmul(F, lmul(F, power(phi, i), power(psi, l)), {(a, b): c})
            out = ladd(F, out, T)
        return out
    def deriv(fd, var):
        out = {}
        for (i, l, a, b), c in fd.items():
            e = i if var == 0 else l
            if e % p == 0: continue
            m = (i-1, l, a, b) if var == 0 else (i, l-1, a, b)
            padd(F, out, m, F.mul[e % p][c])
        return out
    fx, fw = deriv(f, 0), deriv(f, 1)
    phi, psi = {}, {}; hist = []
    for j in range(steps):
        a, b = trans[j]
        if a: padd(F, phi, Ms[j+1], a)
        if b: padd(F, psi, Ms[j+1], b)
        if j >= steps - 6:
            hist.append(tuple(lead(evalf(h, phi, psi), th) for h in (f, fx, fw)))
    # stability of the leading term of f over the last 6 points, and the inequality
    lf = [h[0] for h in hist]
    if None in lf: bad += 1; continue
    stable = all(x[0] == lf[0][0] for x in lf)
    B = min(x[1] for x in hist[-1][1:] if x is not None)
    ineq = lf[-1][1] < B + 1 + th - 1e-9
    if stable and ineq: ok += 1
    else: bad += 1; print('BAD', f, lf, hist[-1], flush=True)
print('STATS T', p, k, 'theta', round(th, 6), 'steps', steps, 'ok', ok, 'bad', bad)
