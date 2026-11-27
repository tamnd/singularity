"""p = 5, n = 3, degree D = 5 only (the run with D = 10 is too slow)."""
import json, random, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prep import *
rng = random.Random(int(sys.argv[1])); count = int(sys.argv[2]); p, n = 5, 3
for wt in [WEIGHTS[3][int(sys.argv[3])]]:
    D = 5
    mons = [a for a in monomials(wt, D, n) if any(i % p for i in a)]
    found = attempts = 0
    while found < count and attempts < 40 * count:
        attempts += 1
        if rng.random() < 0.5:
            sup = rng.sample(mons, rng.randint(2, min(5, len(mons))))
            h = {a: rng.randrange(1, p) for a in sup}
        else:
            h = {a: c for a in mons for c in [rng.randrange(p)] if c}
        if len(h) < 2 or not resonant(h, p, n) or not has_torus_crit(h, p, n):
            continue
        found += 1
        off = has_torus_crit(h, p, n, off_zero=True)
        kind, images, g, tried = prepare(h, wt, D, p, n, rng)
        rec = dict(p=p, n=n, wt=wt, D=D, h=sorted([list(e), c] for e, c in h.items()),
                   off_zero=off, prepared=kind, tried=tried)
        if kind:
            rec['g'] = sorted([list(e), c] for e, c in g.items())
        print(json.dumps(rec), flush=True)
