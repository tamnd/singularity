#!/bin/sh
cd "$(dirname "$0")" && mkdir -p out
{
for mode in plain res; do
 for p in 3 5 7; do
  case $p in 3) n=600;; 5) n=300;; 7) n=150;; esac
  for fam in gen pow; do echo "$p $n 30 $fam $((11*p)) $mode"; done
  for fam in ex52 ex53 ex54 ex536 ex45 ex46 t44a t44b t44c f1 ex533; do echo "$p 30 40 $fam $((13*p)) $mode"; done
 done
done
} | xargs -P 8 -L 1 sh -c 'timeout 3000 python3 walk61.py $0 $1 $2 $3 $4 $5 > out/w_$0_$3_$5.txt 2>&1'
echo done > out/DONE
