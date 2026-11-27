#!/bin/sh
cd "$(dirname "$0")"
for mode in rule rand; do
for p in 3 5 7; do
  W=200; [ $p = 5 ] && W=80; [ $p = 7 ] && W=30
  for fam in gen pow; do timeout 1500 python3 run51.py $mode $fam $p $W 30 $p; done
  for NM in "1 $((2*p+1))" "2 $((4*p+1))" "3 $((6*p+1))"; do timeout 600 python3 run51.py $mode t44 $p 5 40 1 $NM; done
  for fam in ex45 ex46 f1; do timeout 900 python3 run51.py $mode $fam $p 10 60 1; done
done; done
