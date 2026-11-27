import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# F4 longer run, plain class, DIV on: detect exact recurrence of (a, E)
import lib51
from lib51 import *
lib51.DIV = True; lib51.CLS = "plain"
for p in (3, 5, 7):
    m = 2 * p
    a = [ONE] + [{} for _ in range(m)]
    a[2] = {(2, 0, 1): 1}; a[m] = {(0, 2 * p + 1, 0): 1}
    f = F(a, set(), p); E = set(); seen = {}; hist = []
    for step in range(4 * p + 6):
        key = (repr([sorted(x.items()) for x in a[1:]]), tuple(sorted(E)))
        if key in seen:
            hist.append("RECUR step %d = step %d" % (step, seen[key])); break
        seen[key] = step
        io, r = iota(f, a, E); S, t = rule_centre(f, a, E)
        pts = points_over(f, a, E, S)
        hist.append("%s%s" % (S, str(io[1])))
        nxt = [(d, E2) for j, l, nu, d, E2 in pts if j == 2 and all(x == 0 for x in l)]
        if not nxt: hist.append("end %d pts" % len(pts)); break
        a, E = nxt[0]
    print(p, " ".join(hist))
