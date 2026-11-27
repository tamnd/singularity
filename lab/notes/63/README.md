# Note 63: referee report on note 54 (planar runs of degree below p)

These are the scripts of research note 63. Note 63 checks Part B of note 54 and reruns its tests with new code. The code shares nothing with the scripts of note 54 in `lab/notes/54`.

## The claims

Section 6 of note 63, "Tests", is marked [C]. The scripts are the evidence for these items:

1. Item 1, the self test (`selftest63.py`): the iterated steps agree with the closed form of Lemma 3.17.1 of the handbook, and the generators of Theta give the same rho as the monomial description of note 50, Section 1. The result is 0 mismatches.
2. Item 2, the Hahn field test of Theorem 3.2 and Proposition 4.1 of note 54 (`hahn63.py`, output `results/hahn63.txt`): for deg f < p, no failure of (a), (b), the chain (c) or the dominance in the certified trials. For deg f >= p, only the chain (c) fails.
3. Item 3, the searches for planar corner runs (`search63.py`, `deep63.py`, `runs63.py`): for deg < p, no branch meets criterion 1 or criterion 2.
4. Item 4, the positive control for criterion 2 (`control63.py`, output `results/control63.txt`): without the rho condition, the search finds criterion 2 branches from most `pcls` starts over F_2.

The row "Tests of Section 8" of the table of results of note 63 is also [C]. It uses these runs.

## The files

- `core63.py`: the fields F_p and F_{p^2}, one step by direct expansion of (x + a)^i (w + b)^l, the cleaning, and the invariants. rho comes from the generators g_x, g_w, y g_y, z g_z of Theta.
- `selftest63.py`: the self test of item 1.
- `hahn63.py`: the Hahn field test of item 2. Arguments: `p D trials levels mode seed`, with mode `planar`, `sparse` or `linear`.
- `search63.py`: the depth first search for criterion 1. Arguments: `p e cls D nstarts depth seed budget [tlimit]`.
- `deep63.py`: the search for criterion 2 (rank 2 in both windows). Arguments: `p e L budget seed g0 [word]`.
- `runs63.py`: the driver for criteria 1 and 2 on random starts of a class. Arguments: `p e cls D nstarts L1 L2 seed budget tlimit`.
- `control63.py`: the positive control of item 4. Arguments: `p e cls D nstarts L seed budget`.
- `results/hahn63.txt`, `results/control63.txt`: the outputs that note 63 cites.

## Run

From the root of the repository:

```sh
python3 lab/notes/63/selftest63.py
python3 lab/notes/63/hahn63.py 5 3 200 14 planar 1
python3 lab/notes/63/control63.py 2 1 pcls 2 10 15 2 100000
python3 lab/notes/63/runs63.py 3 1 bin 2 60 9 15 107 100000 60
python3 lab/notes/63/search63.py 3 1 bin 2 3 9 1 20000 30
```

The other rows of `results/hahn63.txt` use the arguments that the row shows, for example `hahn63.py 2 2 300 16 planar <seed>`. The search rows of item 3 use `runs63.py` with the classes `bin`, `pcls` and `gen` and the arguments of the table of item 3.

## Expected output

`selftest63.py`:

```
closed form vs iterated steps: mismatches 0 of 54
rho generators vs monomial description: mismatches 0 of 1200
```

`hahn63.py 5 3 200 14 planar 1` gives the first line of `results/hahn63.txt` exactly:

```
p 5 D 3 levels 14 mode planar {'trials': 200, 'exact': 170, 'failA': 0, 'failB': 0, 'failC': 0, 'dom_checked': 504, 'dom_fail': 0, 'div_checked': 164, 'div_fail': 0, 'zero': 0}
```

`control63.py 2 1 pcls 2 10 15 2 100000` gives `criterion-2 hits without rho condition 8`, as in `results/control63.txt`. Note 63 does not give the seeds of the control runs. Other seeds give 5 to 10 hits.

The search scripts give a line with `'rank2': 0` (`search63.py`) or `'rank2_1': 0` and `'rank2_2': 0` (`runs63.py`) for deg < p.

## Run time

On a laptop: `selftest63.py` 0.1 s, `hahn63.py 5 3 200 14 planar 1` 6 s, `control63.py` with 10 starts 0.1 s, `search63.py 3 1 bin 2 3 9 1 20000 30` 3 s. The search runs of item 3 with 30 to 100 starts and the budgets of the table take up to 5000 s each.

## Dependencies

Python 3 and its standard library.

## Changes from the original

Each script that imports a module of this folder inserts the folder of the script into `sys.path`. So the scripts run from any directory, also with `python3 -I`. The docstring of `core63.py` names the notes in place of the old paths. The mathematics is not changed.
