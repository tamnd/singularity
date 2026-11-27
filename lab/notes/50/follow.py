import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab: local imports
import sys, json, re
from fq import *
from walk import children
F = GF(7, 1)
s = "4*x^0w^2y^12z^7 + 2*x^0w^1y^13z^8 + 2*x^1w^0y^13z^8 + 1*x^1w^0y^14z^9 + 3*x^0w^2y^16z^9 + 5*x^2w^0y^17z^12 + 2*x^2w^0y^14z^16"
g = {}
for t in s.split(' + '):
    c, m = t.split('*'); e = list(map(int, re.findall(r'\^(\d+)', m)))
    g[tuple(e)] = int(c)
rho = data(F, g)[3]; print('rho', rho, data(F, g))
word = "zzyzyzzyzz"; path = [(0,0)]*7 + [(1,0),(0,0),(0,1)]
for ch, (a, b) in zip(word, path):
    g = step(F, g, ch, a, b); print(ch, a, b, data(F, g), show(F, g, 8))
# how far can it continue, any word
best = [0]
def dfs(g, depth, w):
    if depth > best[0]: best[0] = depth; print('reach', depth, w, flush=True)
    if depth >= 14: return
    for ch, a, b, g2 in children(F, g, rho):
        dfs(g2, depth+1, w + ch + str(a) + str(b) + ' ')
dfs(g, 0, '')
print('max further depth', best[0])
