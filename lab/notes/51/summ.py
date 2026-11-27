import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sys, ast, glob
keys = ['walks','steps','points','nu_nonzero','omega_fixed_up','prep','iota_up','class_up','iota_eq','eq_pos','iota0_up','drops','cut','unterminated','mono_steps','reg']
for fn in sys.argv[1:]:
    for l in open(fn):
        if l.startswith(('rule', 'rand')) and '{' in l:
            d = ast.literal_eval(l[l.index('{'):].strip())
            print(fn.split('/')[-1], l[:l.index('{')].strip(), {k: d[k] for k in keys})
