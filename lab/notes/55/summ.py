import json,sys,collections
rows=collections.OrderedDict()
for f in sys.argv[1:]:
    for l in open(f):
        r=json.loads(l); k=(r['p'],r['n'],tuple(r['wt']),r['D'])
        s=rows.setdefault(k,collections.Counter())
        s['total']+=1; s['off']+=r['off_zero']
        s[r['prepared'] or 'none']+=1
        if r['off_zero']: s['off_'+(r['prepared'] or 'none')]+=1
print('| (p,n,w,D) | degenerate resonant | off zero | linear | Frobenius | none | none, off zero |')
print('|---|---|---|---|---|---|---|')
for k,s in rows.items():
    print('| %s | %d | %d | %d | %d | %d | %d |'%(str(k).replace(' ',''),s['total'],s['off'],s['linear'],s['frobenius'],s['none'],s['off_none']))
