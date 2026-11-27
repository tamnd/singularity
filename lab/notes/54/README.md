# Note 54: planar corner runs in degree 3, and in every degree below p

These are the scripts of research note 54. The code was written from the definitions of Volume 7 of the handbook. It shares no code with the scripts of notes 50 and 52 in `lab/notes/50` and `lab/notes/52`.

## The claims

Section 8 of note 54, "Tests", is marked [C], and so is the row "Tests of all of the above over F_3, F_5, F_7, F_11, F_25, F_49: no failure, no planar branch" of the table of results. The theorems are proved in the note, so the tests check the proofs and the code. The scripts are the evidence for these items:

1. Item 1 (`core54.py`, `selftest.py`): the vectorized step agrees with a direct substitution, and the formula for rho agrees with the generators of Theta. The result is 0 mismatches in 1500 checks.
2. Item 2 (`search54.py`), for Theorem 5.3 of note 52 and Theorem 5.1 of note 54: no branch of depth 9 or 12 that keeps rho has late translations of rank 2. The table of item 2 gives the runs.
3. Item 3 (`hahn54.py`), for Theorem 3.2: v(f(Phi_infinity)) < lambda_1 + 1 + theta and the leading term of f(Phi_m) becomes stable. The result is 0 failures.
4. Item 4 (`dom54.py`), for Proposition 4.1 and the divisibility step of Theorem 5.1: 0 failures of the dominance in planar mode. In the control with linear translations the dominance fails, so the test can see failures.

## The files

- `core54.py`: the fields F_p and F_{p^2} = F_p[t]/(t^2 - n), one step for all q^2 translations at once as a matrix product, and the invariants r_y, r_z, d, rho and ord g.
- `selftest.py`: the self test of item 1.
- `search54.py`: the search of item 2. Arguments: `p e D n depth seed budget`.
- `hahn54.py`: the Hahn model of item 3. Arguments: `p D trials seed`.
- `dom54.py`: the dominance test of item 4. Arguments: `p D trials seed [planar|linear]`.

## Run

From the root of the repository:

```sh
python3 lab/notes/54/selftest.py
python3 lab/notes/54/hahn54.py 5 3 300 1
python3 lab/notes/54/dom54.py 5 3 80 1
python3 lab/notes/54/dom54.py 5 3 80 1 linear
python3 lab/notes/54/search54.py 5 1 3 300 9 13 200000
```

The rows of the table of item 2 use these arguments (p e D n depth seed budget): `5 2 2 60 9 11 200000`, `5 2 3 60 9 15 200000`, `7 2 2 40 9 12 200000`, `7 2 3 30 9 16 100000`, `5 1 3 300 9 13 200000`, `5 1 3 200 12 17 200000`, `7 1 3 300 9 14 200000`, `7 1 3 200 12 18 200000`, `11 1 3 100 9 19 200000`, `5 2 3 60 9 22 20000` and `7 2 3 40 9 23 20000`. Each run was stopped after at most 5000 s.

## Expected output

`selftest.py`:

```
checks 1500 mismatches 0
```

`dom54.py 5 3 80 1` gives the numbers of item 4 for (p, D) = (5, 3) exactly:

```
mode planar p 5 D 3 trials 80 dominance results {'ok': 159} Theorem 5 step {'divisible': 80}
```

`dom54.py 5 3 80 1 linear` is the control. It gives `'notdominant': 10` in its dominance results.

`hahn54.py 5 3 300 1` gives `failures 0`. Note 54 does not give the seeds of item 3. With seed 1 the count of undecided trials is 137, and the note has 120.

`search54.py` gives a last line with `'planar': 0`. The last line of the run `search54.py 5 1 3 300 9 13 200000` of note 54 (the file `d3_f5.txt`) is:

```
5 1 D 3 depth 9 budget 200000 {'starts': 295, 'any_deep': 195, 'planar': 0, 'timeout': 7} time 892
```

## Run time

On a laptop: `selftest.py` 0.5 s, `hahn54.py 5 3 300 1` 4 s, `dom54.py 5 3 80 1` 12 s. The runs of `search54.py` with the arguments of item 2 take 900 s to 5000 s each. With 20 starts (`search54.py 5 1 3 20 9 13 200000`) the run takes less than 1 s. Its last line is `{'starts': 19, 'any_deep': 11, 'planar': 0, 'timeout': 0}`, the same as the line for start 19 of `d3_f5.txt`.

## Dependencies

Python 3 and NumPy (`core54.py` uses `numpy` for the matrix products). `hahn54.py` and `dom54.py` use only the standard library.

## Changes from the original

`selftest.py` and `search54.py` insert the folder of the script into `sys.path` in place of an absolute path. So the scripts run from any directory, also with `python3 -I`. The docstring of `core54.py` names the notes in place of the old paths. The result files and the shell scripts that started the long runs on the project machine are not copied. The mathematics is not changed.
