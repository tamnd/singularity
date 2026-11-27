# Check of Prop 2.2 / Remark 2.3 of note 56 over a finite field F_{p^k}.
# X = {sum_{i=0}^5 x_i^{q+1} = 0} in P^5, q = p^m.  For P not on X and x on X with
# sum P_i x_i^q = 0, compute ord_t F(x + tP) (= local degree of the projection from P at x).
# Claim checked: order q+1 everywhere on R_P if P is F_{q^2}-rational, and order q at
# most points of R_P otherwise.
import itertools, random, sys
p, m, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])   # field F_{p^k}, need 2m | k
q = p ** m
assert k % (2 * m) == 0
Q = p ** k
def polymulmod(a, b, mod):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    while len(r) >= len(mod):
        c = r[-1]
        if c:
            for i in range(len(mod)):
                r[len(r) - len(mod) + i] = (r[len(r) - len(mod) + i] - c * mod[i]) % p
        r.pop()
    return r
def toint(a): return sum(c * p ** i for i, c in enumerate(a))
def tolist(n): return [(n // p ** i) % p for i in range(k)]
# find primitive polynomial of degree k (monic, coefficients low to high)
for coeffs in itertools.product(range(p), repeat=k):
    mod = list(coeffs) + [1]
    if coeffs[0] == 0: continue
    x = [0, 1]; e = [1]; seen = set(); ok = True
    for i in range(Q - 1):
        n = toint(e + [0] * (k - len(e)))
        if n in seen: ok = False; break
        seen.add(n); e = polymulmod(e, x, mod)
    if ok and len(seen) == Q - 1: break
EXP = [0] * (2 * Q); LOG = [0] * Q
e = [1]
for i in range(Q - 1):
    n = toint(e + [0] * (k - len(e))); EXP[i] = n; LOG[n] = i; e = polymulmod(e, [0, 1], mod)
for i in range(Q - 1, 2 * Q): EXP[i] = EXP[i - (Q - 1)]
def add(a, b): return toint([(x + y) % p for x, y in zip(tolist(a), tolist(b))])
def neg(a): return toint([(-x) % p for x in tolist(a)])
def mul(a, b): return 0 if a == 0 or b == 0 else EXP[LOG[a] + LOG[b]]
def pw(a, n):
    if n == 0: return 1
    return 0 if a == 0 else EXP[(LOG[a] * n) % (Q - 1)]
def inv(a): return EXP[(Q - 1 - LOG[a]) % (Q - 1)]
def F(x):
    s = 0
    for xi in x: s = add(s, pw(xi, q + 1))
    return s
# polynomial in t: F(x + tP) as list of coefficients, via the identity-free direct expansion
def ordt(x, P):
    # coefficients of F(x+tP) in t, computed by brute force expansion of (x_i + t P_i)^{q+1}
    from math import comb
    co = [0] * (q + 2)
    for xi, Pi in zip(x, P):
        for j in range(q + 2):
            c = comb(q + 1, j) % p
            if c: co[j] = add(co[j], mul(c, mul(pw(xi, q + 1 - j), pw(Pi, j))))
    for j, c in enumerate(co):
        if c: return j
    return 99
def frob_root(a):  # a^(1/q)
    return pw(a, (Q // q))
def points_on_RP(P, N):
    # R_P = X cap {sum P_i^{1/q} x_i = 0} (set-theoretically). Solve x_5 linearly, x_4 by search.
    Pr = [frob_root(Pi) for Pi in P]
    out = []
    j5 = max(i for i in range(6) if Pr[i])
    others = [i for i in range(6) if i != j5]
    tries = 0
    while len(out) < N and tries < 50 * N:
        tries += 1
        x = [0] * 6
        free = others[:-1]; last = others[-1]
        for i in free: x[i] = random.randrange(Q)
        for v in range(Q):
            x[last] = v
            s = 0
            for i in others: s = add(s, mul(Pr[i], x[i]))
            x[j5] = mul(neg(s), inv(Pr[j5]))
            if F(x) == 0 and any(x):
                out.append(list(x)); break
    return out
random.seed(1)
def rational(P):  # projectively F_{q^2}-rational?
    i = next(i for i in range(6) if P[i]); c = inv(P[i]); Pn = [mul(c, a) for a in P]
    return all(pw(a, q * q) == a for a in Pn)
sub = [a for a in range(Q) if pw(a, q * q) == a]   # F_{q^2}
for kind in ['rational', 'general']:
    for trial in range(3):
        while True:
            P = [random.choice(sub) if kind == 'rational' else random.randrange(Q) for _ in range(6)]
            if any(P) and F(P) != 0 and rational(P) == (kind == 'rational'): break
        pts = points_on_RP(P, 12)
        g = [sum(1 for _ in [0]) for _ in pts]
        # sanity: sum P_i x_i^q = 0 on these points
        chk = all(eval_ok for eval_ok in [sum_check for sum_check in [True]])
        orders = []
        for x in pts:
            s = 0
            for xi, Pi in zip(x, P): s = add(s, mul(Pi, pw(xi, q)))
            assert s == 0
            orders.append(ordt(x, P))
        print('q=%d field F_%d^%d' % (q, p, k), kind, 'orders along R_P:', orders)
