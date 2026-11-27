# Note 56: the parts of Target T, the low degree experiment

## The claims

These scripts are the evidence for the claims [C] of Section 7 of research note 56 (Problem 9.9: the maximal contact tower with Hasse derivatives).

- Section 7.4, item 1: for the family of Proposition 7.2, f = z^2 + 2z(x^r + x^(p-r)) + x^(2r), with p = 7, 11, 13, 17, 29, 31, 41 and the degrees 6, 8, 10, 12, 20, 22, 28, the log of the tower is always `[(1,5,2,'pass'), (2,4,p,'FAIL')]` [C]. Script: `fam3.py`.
- Section 7.4, item 2: the families `fam` and `fam2` of the earlier draft give the same log for p = 7, 11, 13, 29, 31, 37, 41, 43 [C]. Script: `run.py fam` and `run.py fam2`.
- Section 7.4, item 3: random germs of low degree essentially never reach an order divisible by p in the first levels, so they never fail [C]. Script: `run.py rand p b N nterms`.

Note 62 (Section 4.4 and item 10 of Section 56.0 of note 56) says that this evidence is weak. With the truncation T = p + 1 and the exponents e!/(e - j) of Kollár, the random runs can only see the order p itself at levels 2 and 3. Also, the function `delta_j` of `tower.py` uses only the multi-indices with |alpha| = j, not |alpha| <= j, so the random runs compute an ideal that can be smaller than Delta^j. The scripts here are the original scripts. This limitation is not fixed.

## The files

- `tower.py`: truncated power series over F_p in n variables, Hasse derivatives with the theorem of Lucas, the test of Lemma 7.1, the restriction to a hypersurface H, and the coefficient ideal of Kollár. `tower(R, gens, maxlev)` gives a list of (level, dimension, order, status).
- `fam3.py`: the family of Proposition 7.2.
- `run.py`: the families `fam` and `fam2`, and the random germs.

The folder `../62` uses `tower.py` without a change.

## Run

From the root of the repository:

```sh
python3 lab/notes/56/fam3.py
python3 lab/notes/56/run.py fam
python3 lab/notes/56/run.py fam2
python3 lab/notes/56/run.py rand 13 2 30 4
```

The arguments of `run.py rand` are the prime p, the order b, the number N of germs and the number of terms of each germ. The seed is 1000 p + b, so a run gives the same output each time.

## Expected output

`fam3.py` prints one line for each p. Each line ends with the same log:

```text
7 r = 2 deg f = 6 [(1, 5, 2, 'pass'), (2, 4, 7, 'FAIL: degree-e part in k[x^p]')]
...
41 r = 14 deg f = 28 [(1, 5, 2, 'pass'), (2, 4, 41, 'FAIL: degree-e part in k[x^p]')]
```

`run.py fam` and `run.py fam2` print the same log for p = 7, 11, 13, 29, 31, 37, 41, 43, with deg f = p - 1.

`run.py rand` prints a count for each log. The status `FAIL` does not occur. For `rand 13 2 30 4` the most frequent logs are `((2, 'pass'), (2, 'pass'), ('>T', 'stop'))` (9 germs) and `((2, 'pass'), (2, 'pass'), (2, 'pass'))` (8 germs).

## Run time

`fam3.py`, `run.py fam` and `run.py fam2` take less than 1 second each. `run.py rand 13 2 30 4` takes about 1 second. Note 56 does not record the number of terms of its random runs. The runs of note 56 with p = 13, b = 3 and with p = 29 had a time limit of 20000 seconds and did not finish when note 62 was written.

## Dependencies

Python 3 and its standard library only.

## Changes from the original

The scripts find `tower.py` in their own folder. The original scripts used an absolute path. The mathematics is not changed.
