# Note 62: referee report on note 56

## The claims

These scripts are the evidence for the numerical checks [C] of research note 62, the referee report on note 56.

- Section 1.1 (Proposition 2.2 of note 56, the Hermitian 4-fold X = {sum x_i^(q+1) = 0} in P^5): the script computes ord_t F(x + tP) at random points x of R_P [C]. For q = 3 over F_(3^6) and q = 5 over F_(5^4), and three centres P that are F_(q^2)-rational, each point gives q + 1. For three centres that are not rational, almost each point gives q, and one point (q = 3) gives q + 1. For q = 9 over F_(3^8), the rational centres give 10 and the other centres give 9 at all 36 points. Script: `hermitian.py`. This is also the check of Proposition 1.2 of note 62.
- Section 4.2, reruns [C]: for p = 5, 7, 11, 13, 19, 23 and each r with 1 <= r <= (p - 1)/2, the family of Proposition 7.2 of note 56 gives the log `[(1,5,2,'pass'), (2,4,p,'FAIL')]`, and the plain germ z^2 - x^p gives the same log. Script: `fam3_rerun.py`.

Section 4.4 of note 62 says that the random runs of note 56 are weak evidence, and that `delta_j` in `../56/tower.py` uses only |alpha| = j, not |alpha| <= j. `fam3_rerun.py` uses `tower.py` without a change, so this limitation stays. It does not change the family of Proposition 7.2, which note 56 proves by hand.

## The files

- `hermitian.py`: finite fields F_(p^k) built from a search for an irreducible polynomial, the Hermitian form, and the orders along R_P.
- `fam3_rerun.py`: the reruns. It imports `tower.py` from `../56`.

## Run

From the root of the repository:

```sh
python3 lab/notes/62/hermitian.py 3 1 6
python3 lab/notes/62/hermitian.py 5 1 4
python3 lab/notes/62/hermitian.py 3 2 8
python3 lab/notes/62/fam3_rerun.py
```

The arguments of `hermitian.py` are p, m and k, with q = p^m and the field F_(p^k). The script needs 2m | k. The seed is fixed, so a run gives the same output each time. `fam3_rerun.py` takes an optional argument: the folder of `tower.py`. The default is `../56` next to the script.

## Expected output

`hermitian.py 3 1 6` prints six lines. The three lines for the rational centres have only the order 4. The three lines for the general centres have the order 3, and one point has the order 4:

```text
q=3 field F_3^6 rational orders along R_P: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
q=3 field F_3^6 general orders along R_P: [3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3]
```

`hermitian.py 5 1 4` gives only the order 6 for the rational centres and only the order 5 for the general centres. Note 62 records that `hermitian.py 3 2 8` gives only 10 and only 9. This run was not repeated to the end for this folder (see the run time).

`fam3_rerun.py` prints one line for each p and r and one line for z^2 - x^p. Each line ends with the log `[(1, 5, 2, 'pass'), (2, 4, p, 'FAIL: degree-e part in k[x^p]')]`, for example:

```text
5 2 deg 4 [(1, 5, 2, 'pass'), (2, 4, 5, 'FAIL: degree-e part in k[x^p]')]
5 z^2-x^p [(1, 5, 2, 'pass'), (2, 4, 5, 'FAIL: degree-e part in k[x^p]')]
```

## Run time

`fam3_rerun.py` takes less than 1 second. `hermitian.py 3 1 6` and `hermitian.py 5 1 4` take about 5 seconds each. `hermitian.py 3 2 8` takes more than 5 minutes. A test run stopped after 300 seconds with no output.

## Dependencies

Python 3 and its standard library only.

## Changes from the original

`fam3_rerun.py` finds `tower.py` in `../56` when it has no argument. The original script needed the absolute path of the folder as its first argument. The mathematics is not changed. `hermitian.py` is not changed.
