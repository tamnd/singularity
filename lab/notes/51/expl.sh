#!/bin/sh
cd "$(dirname "$0")"
for p in 5 7; do
  for NM in "1 $((2*p+1))" "2 $((4*p+1))" "3 $((6*p+1))"; do timeout 900 python3 run51.py rule t44 $p 5 40 1 $NM; timeout 900 python3 run51.py rand t44 $p 5 15 1 $NM; done
  for fam in ex45 ex46 f1; do timeout 900 python3 run51.py rule $fam $p 10 60 1; timeout 900 python3 run51.py rand $fam $p 5 15 1; done
done
for NM in "1 7" "2 13" "3 19"; do timeout 900 python3 run51.py rand t44 3 10 20 1 $NM; done
for fam in ex45 ex46 f1; do timeout 900 python3 run51.py rand $fam 3 10 20 1; done
