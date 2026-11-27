"""Recompute the lab rows of note 55, Section 7, from the recorded forms (data only),
with the independent tools of lib60.py and galois."""
import json, sys, itertools, collections, time
import numpy as np
import galois
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib60 import *

SRC = os.path.join(HERE, '..', '55', '')
files = ['run_p2.jsonl', 'run_p3.jsonl', 'run_p5n2.jsonl', 'run_p5n3_w1.jsonl',
         'run_p5n3_w2.jsonl', 'run_p5n3_w3.jsonl', 'run_p5n3.jsonl']
only = set(sys.argv[1:])  # optional row filter like "2,3,1-1-1,4"

cert = {}
for l in open(SRC + 'cert_out.jsonl'):
    r = json.loads(l)
    cert[(r['p'], r['n'], r['D'], tuple(sorted(map(tuple, map(lambda t: (tuple(t[0]), t[1]), r['h'])))))] = r['verdict']


def key_h(h):
    return tuple(sorted(h.items()))


def crit_count_n2(h, p):
    """Projective critical points of a binary form over the closure: (number, all rational)."""
    GF = galois.GF(p)
    dx, dy = deriv(h, 0, p), deriv(h, 1, p)
    D = sum(next(iter(h)))

    def dehom(f, deg):  # f(1, t) as galois Poly, coefficients by power of t
        co = [0] * (deg + 1)
        for a, c in f.items():
            co[a[1]] = (co[a[1]] + c) % p
        return galois.Poly(co[::-1], field=GF)
    a, b = dehom(dx, D - 1), dehom(dy, D - 1)
    g = galois.gcd(a, b) if (a != 0 and b != 0) else (a if b == 0 else b)
    num = 0
    rational = True
    if g.degree > 0:
        for fac, mult in zip(*g.factors()):
            num += fac.degree
            rational &= fac.degree == 1
    # point at infinity (0:1)
    inf = all(f.get((0, D - 1), 0) == 0 for f in (dx, dy))
    num += inf
    return num, rational


rows = collections.OrderedDict()
issues = []
t0 = time.time()
for fn in files:
    for l in open(SRC + fn):
        r = json.loads(l)
        p, n, wt, D = r['p'], r['n'], tuple(r['wt']), r['D']
        k = (p, n, wt, D)
        tag = '%d,%d,%s,%d' % (p, n, '-'.join(map(str, wt)), D)
        if only and tag not in only:
            continue
        if fn == 'run_p5n3.jsonl' and wt != (1, 1, 1):
            continue
        h = from_json(r['h'])
        s = rows.setdefault(k, collections.Counter())
        s['total'] += 1
        # weighted homogeneity and cleanness
        assert all(sum(w * a for w, a in zip(wt, e)) == D for e in h), (k, h)
        assert clean(h, p) == h
        res = resonant(h, p, n)
        tc = torus_test(h, p, n, 'crit')
        off = torus_test(h, p, n, 'off')
        s['res&crit'] += res and tc
        s['off'] += off
        if off != r['off_zero']:
            issues.append(('off_zero mismatch', k, r['h']))
        prep = r['prepared'] or 'none'
        s[prep] += 1
        if prep != 'none':
            if 'images' in r:
                im = [from_json(x) for x in r['images']]
                g = clean(compose(h, im, p, n), p)
                if g != from_json(r['g']):
                    issues.append(('g mismatch', k, r['h']))
                ok = nondeg_all_faces(g, p, n)
                s['verified prepared'] += ok
                if not ok:
                    issues.append(('recorded preparation not nondegenerate', k, r['h']))
            else:
                g = from_json(r['g'])
                ok = nondeg_all_faces(g, p, n)
                s['verified g only'] += ok
        if wt == (1,) * n and n == 2:
            num, rat = crit_count_n2(h, p)
            pred = 'linear' if (num <= 2 and rat) else 'none'
            s['n2 prediction agrees'] += pred == prep
            if pred != prep:
                issues.append(('n2 prediction', k, r['h'], num, rat, prep))
            if prep == 'none':
                v = cert.get((p, n, D, key_h(h)))
                s['cert >=3 pts'] += (num >= 3) and v == 'certified unpreparable'
        if (p, n, wt, D) == (2, 3, (1, 1, 1), 4):
            # A, B, C of Lemma 6.2: rows indexed by the pair of odd coordinates
            M = np.zeros((3, 3), dtype=int)
            pairs = {(0, 1): 0, (0, 2): 1, (1, 2): 2}
            for e, c in h.items():
                odd = tuple(i for i in range(3) if e[i] % 2)
                sq = [(e[i] - (1 if i in odd else 0)) // 2 for i in range(3)]
                M[pairs[odd], sq.index(1)] = 1
            rk = int(np.linalg.matrix_rank(galois.GF(2)(M)))
            v = cert.get((p, n, D, key_h(h)), prep)
            s['rank3'] += rk == 3
            s['rank3 <-> certified'] += (rk == 3) == (v == 'certified unpreparable')
for k, s in rows.items():
    print(k, dict(s))
print('issues:', len(issues))
for i in issues[:30]:
    print(' ', i)
print('time %.0fs' % (time.time() - t0))
