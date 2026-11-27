#!/bin/sh
# Walks of Rule 61.9' (mode om) for all families.
cd "$(dirname "$0")" && mkdir -p out
{
for p in 3 5 7; do
  case $p in 3) n=300;; 5) n=150;; 7) n=60;; esac
  for fam in gen pow; do echo "$p $n 30 $fam 11 om"; done
  for fam in ex52 ex53 ex54 ex536 ex45 ex46 t44a t44b t44c f1 ex533; do echo "$p 20 40 $fam 12 om"; done
done
} | xargs -P 6 -L 1 sh -c 'timeout 2400 python3 walk61.py $0 $1 $2 $3 $4 $5 > out/om_$0_$3.txt 2>&1'
touch out/DONE_om
