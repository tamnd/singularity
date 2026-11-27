#!/bin/sh
cd "$(dirname "$0")"
for v in "DIV=1 CLS=plain" "DIV=1 CLS=res"; do
 for p in 3 5 7; do
  W=200; [ $p = 5 ] && W=80; [ $p = 7 ] && W=30
  for fam in gen pow; do echo "VARIANT $v"; env $v timeout 1500 python3 run51.py rule $fam $p $W 30 $p; done
 done
done
