# Note 50: Conjecture L° and Hypothesis H1 for linear corner runs in four variables

These are the scripts of research note 50. They compute with exact arithmetic over F_q. The translations are in F_q and not in K, the words are finite, and the searches have caps. So the tests are not proofs.

## The claims

Section 8 of note 50, "Numerical tests", is marked [C]. Example 6.1 is [P] for the first two steps and [C] for the rest. The scripts are the evidence for these items:

1. Item 1, random walks (`walk.py`): no deep walk has late translations of rank 2, and there is no failure of H1 or of L°.
2. Item 2, Theorem 4.1 (`lincheck.py`): at the end of each deep linear run, in G = c x^d, d = rho + 1, nu^G >= d on both corner curves and nu^G >= rho on both corner surfaces. All runs pass (159 of 159 over F_3, 180 of 180 over F_9, 179 of 179 over F_5, 151 of 151 over F_7).
3. Item 3, the search for planar runs (`planar.py`, `planar3.py`, `follow.py`): no branch is a planar run. `planar3.py` checks that no continuation of up to 4 steps from a flagged end point keeps rho and uses both letters. `follow.py` follows the one branch over F_7 with late translations of rank 2 to a dead end.
4. Item 4, Statement T1 in degree less than p (`tcheck.py`): 40 of 40 cases over F_5 and over F_9 pass.
5. Item 5 and Example 6.1 (`ex.py`, `ex2.py`): over F_3, F_5 and F_7, after a y-step with a nonzero translation of w, each step that keeps rho = 1 goes to a point with d = rho = 1, and the only two-step continuations that keep rho use the same letter twice.

## The files

- `fq.py`: the fields F_p, F_9, F_25, F_49 and F_27, the chart with the translation and the cleaning, r, d, rho, and the orders along the corner curves and surfaces.
- `walk.py`: the random walks of item 1. Arguments: `p k class N depth seed`, with class `line`, `nonbin` or `bin`. Here q = p^k.
- `lincheck.py`: the check of item 2. Arguments: `p k N depth seed`.
- `planar.py`: the search of item 3. Arguments: `p k class N L seed`, with class `deg2`, `nonbin` or `bin`.
- `planar3.py`: the search of item 3 with the continuation test of the flagged end points. Same arguments.
- `follow.py`: follows the branch over F_7 of item 3. No arguments.
- `tcheck.py`: the test of item 4. Arguments: `p k trials steps seed`.
- `ex.py`, `ex2.py`: Example 6.1. No arguments.

## Run

From the root of the repository:

```sh
python3 lab/notes/50/ex.py
python3 lab/notes/50/ex2.py
python3 lab/notes/50/follow.py
python3 lab/notes/50/walk.py 3 1 line 300 16 7
python3 lab/notes/50/lincheck.py 3 1 300 18 5
python3 lab/notes/50/planar.py 3 1 deg2 400 10 11
python3 lab/notes/50/planar3.py 3 1 deg2 400 10 11
python3 lab/notes/50/tcheck.py 5 1 40 24 1
python3 lab/notes/50/tcheck.py 3 2 40 24 1
```

The other rows of the tables use the same seeds: `walk.py p k class 300 16 7` for the rows of item 1, `lincheck.py p k 300 18 5` with (p, k) = (3, 1), (3, 2), (5, 1), (7, 1), and `planar.py p k class 400 10 11` for the rows of item 3.

## Expected output

`ex2.py` ends each block with:

```
3 two-step continuations ['yy', 'zz']
5 two-step continuations ['yy', 'zz']
7 two-step continuations ['yy', 'zz']
```

`follow.py` ends with `max further depth 0`.

`walk.py 3 1 line 300 16 7` gives the row "3, F_3, line" of item 1:

```
STATS 3 1 line 16 {'walks': 291, 'deep': 185, 'deep_nz': 185, 'tail_rank2': 0, 'h1fail': 0, 'lfail': 0, 'lfail_bin': 0, 'line_end': 0}
```

`lincheck.py 3 1 300 18 5` gives 159 in each count, and `lincheck.py 7 1 300 18 5` gives 151:

```
STATS 3 1 18 {'deep_lin': 159, 'inG_xd': 159, 'd_eq_rho1': 159, 'curves_ge_d': 159, 'curves_ge_rho': 159, 'surf_ge_rho': 159}
```

`planar.py 3 1 deg2 400 10 11` and `planar3.py 3 1 deg2 400 10 11` give the row "3, F_3, deg2" of item 3. `planar3.py` also prints the flagged end points with `FAIL dead` and their invariants.

```
STATS 3 1 deg2 10 {'g': 368, 'deep': 74, 'rank1': 32, 'rank2': 0, 'h1fail': 1, 'lfail': 1}
```

`tcheck.py 5 1 40 24 1` gives `ok 40 bad 0`, and so does `tcheck.py 3 2 40 24 1`.

## Run time

On a laptop: `ex.py`, `ex2.py` and `follow.py` less than 0.1 s each, `walk.py 3 1 line 300 16 7` 2 s, `lincheck.py 3 1 300 18 5` 2 s, `lincheck.py 7 1 300 18 5` 520 s, `planar.py 3 1 deg2 400 10 11` 55 s, `planar3.py 3 1 deg2 400 10 11` 60 s, `tcheck.py 5 1 40 24 1` 8 s, `tcheck.py 3 2 40 24 1` 0.2 s. The runs over F_7 and the larger fields of items 1 and 3 took up to 2400 s each.

## Dependencies

Python 3 and its standard library.

## Changes from the original

Each script that imports `fq` or `walk` inserts the folder of the script into `sys.path`. So the scripts run from any directory, also with `python3 -I`. The log files, the shell scripts that started the long runs, the copies of the handbook and the scripts that the note does not cite (`planar2.py`, `dfs.py`, `t0.py`, `t1.py`, `t2.py`) are not copied. The mathematics is not changed.
