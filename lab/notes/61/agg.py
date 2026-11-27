import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Aggregate walk outputs into the tables of Section 61.8.
import json, glob, sys
pref = sys.argv[1]  # 'w_' or 'om_'
mode = sys.argv[2] if len(sys.argv) > 2 else None
expl = {}
for f in sorted(glob.glob('out/' + pref + '*.txt')):
    L = open(f).read().splitlines()
    if not L: print(f, 'pending'); continue
    d = json.loads(L[0]); s = d['stats']
    if mode and d['mode'] != mode: continue
    row = dict(walks=s.get('walks', 0), steps=sum(v for k, v in s.items() if k.startswith('steps_')),
               omup=sum(v for k, v in s.items() if k.startswith('om_up')), iotaup=sum(v for k, v in s.items() if k.startswith('iota_up')),
               zup=s.get('zprime_up_const', 0), unprep=s.get('zprime_not_prep', 0), depth=s.get('depth_limit', 0), toR1=s.get('to_R1', 0),
               maxrun=s.get('max_eq_run', 0), err=s.get('error', 0) + s.get('conflict', 0))
    if d['fam'] in ('gen', 'pow'):
        print(d['p'], d['fam'], d['mode'], row)
    else:
        for k, v in row.items():
            if k == 'maxrun': expl[k] = max(expl.get(k, 0), v)
            else: expl[k] = expl.get(k, 0) + v
print('explicit total', expl)
