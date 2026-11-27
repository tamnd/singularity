# Note 52: referee report on note 50

These are the scripts of research note 52, the referee report on note 50. The code was written from the definitions of Volume 7 of the handbook. It does not use the scripts of note 50 in `lab/notes/50`. The translations are in F_q, the words are finite, and the searches have caps. So the tests are not proofs.

## The claims

Section 7 of note 52, "Tests", is marked [C], and so is item 9 of the summary: independent tests over F_3, F_9, F_5, F_25, F_7 and F_49 agree with the report. The scripts are the evidence for these items of Section 7:

1. Item 1 (`sanity.py`): Example 6.1 of note 50 for p = 3, 5, 7 and Example 3.17.22 of the handbook for p = 5, 7. For Example 3.17.22, rho = 3, d = 4 and nu^G = 1 on the surface V(x, y) (the counterexample of Section 3.7).
2. Item 2 (`linwalk.py`), Theorem 4.1 of note 50: no failure of the end checks in G = c' X^d, d = rho + 1 < p, both curves >= d and both surfaces >= rho.
3. Item 3 (`tie.py`, `tie2.py`, `tie3.py`), Step 3, the tie class: the end points that fail the check of item 2 have their last nonzero translation of w at step 14 to 17 of 18, and no failing end point has a continuation of 3 steps with both letters.
4. Item 4 (`t1.py`, `t1diag.py`), Lemma 4.1 and Proposition 5.2 of note 50 in the Hahn field model: with random translations, all 720 cases pass. With adversarial translations, T1 fails in 132 of 600 cases, and these walks are linear.
5. Item 5 (`deg2.py`, `deg2b.py`), Theorem 5.3: no branch has late translations of rank 2 that do not lie on one line, except one dead end of finite length over F_5.
6. Item 6 (`lem21.py`), Lemma 2.1: along the Euclid word, both exponents are nonnegative from level 15 on at the latest, and at least 5 at level 150.

## The files

- `core.py`: the fields F_p and F_{p^2} = F_p[t]/(t^2 - n), the step with division by L^p and cleaning, r, rho, G, d, in G, nu^G of the two corner curves and the two corner surfaces, and the substitution x = X + c W.
- `sanity.py`: item 1. No arguments.
- `linwalk.py`: item 2. Arguments: `p e n depth seed`. Here q = p^e and n is the number of starts.
- `tie.py`, `tie2.py`, `tie3.py`: item 3. No arguments. They use `linwalk.py`.
- `t1.py`, `t1diag.py`: item 4. No arguments. `t1diag.py` uses `t1.py`.
- `deg2.py`, `deg2b.py`: item 5. Arguments: `p e n depth seed`. `deg2b.py` reads the functions of `deg2.py`.
- `lem21.py`: item 6. No arguments.

## Run

From the root of the repository:

```sh
python3 lab/notes/52/sanity.py
python3 lab/notes/52/lem21.py
python3 lab/notes/52/linwalk.py 3 1 400 18 1
python3 lab/notes/52/tie.py
python3 lab/notes/52/tie2.py
python3 lab/notes/52/tie3.py
python3 lab/notes/52/t1.py
python3 lab/notes/52/t1diag.py
python3 lab/notes/52/deg2.py 3 1 40 9 1
python3 lab/notes/52/deg2b.py 3 1 60 9 1
```

For the other fields of items 2 and 5, change `p e` to `3 2`, `5 1`, `5 2`, `7 1` or `7 2`, and the number of starts as in the table of item 5.

## Expected output

`sanity.py` prints for p = 5 and p = 7:

```
5 ex3.17.22 rho 3 d 4 surf_y 1 curve 4 fixed True True
7 ex3.17.22 rho 3 d 4 surf_y 1 curve 4 fixed True True
```

`lem21.py`:

```
cases 1468 min exponent < 5 after 150 steps 0 latest first level with both exponents >= 0 15
```

`linwalk.py 3 1 400 18 1` gives `'fail': 0`. The run here gives 85 deep walks with 627 late nonzero translations. Note 52 reports 88 and 792 for the same arguments, so the copy of `core.py` or of `linwalk.py` may differ from the version of the run in the note. The count of failures is the same.

`tie2.py` gives the steps of the last nonzero translation for the failing and the passing end points:

```
3 1 fail lastnz: [16, 17]  pass lastnz: [-1]
5 2 fail lastnz: [15, 16, 17]  pass lastnz: [-1]
7 1 fail lastnz: [14, 16, 17]  pass lastnz: [-1]
```

`tie3.py` gives the numbers of item 3 exactly:

```
3 1 failing endpoints 10 with a 3-step continuation using both letters 0
5 1 failing endpoints 10 with a 3-step continuation using both letters 0
7 1 failing endpoints 9 with a 3-step continuation using both letters 0
3 2 failing endpoints 5 with a 3-step continuation using both letters 0
```

`t1.py` prints one line for each field, theta and mode. In the 12 lines with `rand` all 60 cases pass the three checks (720 cases). In the 12 lines with `adv` the inequality holds in 468 of 600 cases. `t1diag.py` prints the 132 adversarial failures for each field and theta. In this run 131 of them have a linear tail in the last 6 steps (the window of the script), and 10 of them have f = 0.

`deg2.py 3 1 40 9 1` gives the row of F_3 in the table of item 5 (0 branches of rank 2, 3 starts over the budget):

```
3 1 depth 9 {'starts': 40, 'alive_any': 0, 'planar_alive': 0, 'timeout': 3}
```

`deg2b.py 3 1 60 9 1` gives `'planar': 0`. The budget is a wall time, so the counts of starts over the budget depend on the machine. The run here gives 48 starts with a branch to depth 9 and 7 over the budget, and the note has 50 and 6.

## Run time

On a laptop: `sanity.py` 0.1 s, `lem21.py` 0.5 s, `linwalk.py 3 1 400 18 1` 0.4 s, `tie.py` 5 s, `tie2.py` 1.4 s, `tie3.py` 200 s, `t1.py` 85 s, `t1diag.py` 70 s, `deg2.py 3 1 40 9 1` 80 s, `deg2b.py 3 1 60 9 1` 180 s. The runs over F_25 and F_49 of item 5 took more than 590 s and the note does not report them.

## Dependencies

Python 3 and its standard library.

## Changes from the original

Each script inserts the folder of the script into `sys.path` in place of an absolute path, and `deg2b.py` opens `deg2.py` from the folder of the script. So the scripts run from any directory, also with `python3 -I`. The docstring of `core.py` names note 50 in place of the old path. The helper scripts that the note does not cite (`t1diag2.py`, `t1lib.py`) are not copied. The mathematics is not changed.
