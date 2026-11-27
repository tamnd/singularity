import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Exact traces of the examples of note 51 under the rule (all points over each centre are listed).
from lib51 import *
from run51 import iota0, start
import random

def show(f, a):
    return " ".join("a%d=%s" % (i, sorted(a[i].items())[:3]) for i in range(1, f.m + 1) if a[i])

def trace(fam, p, args=(), depth=8, follow=None):
    m = 2 * p
    a = start(fam, p, m, random.Random(0), list(args))
    f = F(a, set(), p); E = set()
    a, info = adapt(f, a)
    print("==", fam, "p=%d" % p, args)
    path = []
    for step in range(depth):
        io, r = iota(f, a, E); D, s = slopes(f, a)
        S, ties = rule_centre(f, a, E)
        print(" step %d: regime R%d delta=%s D=%s sigma=%s E=%s iota=(%d,%s) iota0=%s centre V(z,x_S) S=%s ties=%d" % (
            step, r, min(D, s), D, s, sorted(E), io[0], io[1], iota0(f, a), S, ties))
        print("   ", show(f, a))
        pts = points_over(f, a, E, S)
        if not pts:
            print("   multiplicity drops"); break
        rows = []
        for j, lams, nu, d, E2 in pts:
            d2, (k, dch) = adapt(f, d)
            io2, r2 = iota(f, d2, E2); D2, s2 = slopes(f, d2)
            rows.append((j, lams, nu, r2, io2, iota0(f, d2), d2, E2, k, dch, min(D2, s2)))
            print("    chart x%d lams=%s nu=%d -> R%d delta=%s iota=(%d,%s) iota0=%s prep=%d dirch=%s" % (
                j, lams, nu, r2, min(D2, s2), io2[0], io2[1], iota0(f, d2), k, dch))
        # follow: the point with the largest iota (worst case), or a given choice
        if follow == "max":
            row = max(rows, key=lambda t: (t[4], t[5]))
        elif follow == "maxiota0":
            row = max(rows, key=lambda t: (t[5], t[4]))
        else:
            row = rows[0]
        a, E = row[6], row[7]

import sys
DEPTH = int(sys.argv[1]) if len(sys.argv) > 1 else 8
for p in (3, 5, 7):
    trace("ex45", p, follow="max", depth=DEPTH)
    trace("f1", p, follow="maxiota0")
    trace("t44", p, (2, 4 * p + 1), follow="max")
    trace("ex46", p, follow="max")
