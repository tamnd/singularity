# Note 60: Referee report on note 55

These are the scripts of research note 60, the referee report on note 55, "Newton and Frobenius preparation" (track NW). The scripts were written independently of the scripts of note 55. They use only the recorded forms of note 55, the files `run_*.jsonl` and `cert_out.jsonl` in `../55`, as input data.

## The claims

- Section 5, the lab rows [C]. `lab60.py` recomputes all 37 rows of the lab table of note 55, 418 forms in all, from the recorded forms: weighted homogeneity, cleanness, resonance, the torus critical points, each of the 178 recorded preparations, the number of critical points for n = 2 in the standard weight, and the rank of (A, B, C) of Lemma 6.2 of note 55 in the row (2, 3, (1,1,1), 4). `brute60.py rows` searches all of GL_n(F_p) for the rows (2, 3, (1,1,1), 4), (3, 2, (1,1), 6) and (5, 2, (1,1), 5). The recorded outputs are `lab60.out` and `brute_rows.out`.
- Section 6, the C4 test cases [C]. `c4.py` recomputes the three test cases of Section 12 of note 55: the Fano form xyw(x+y+w) for p = 2, x^5y + xy^5 for p = 3 and x^4y + xy^4 for p = 5.
- Section 1.2, the machine check of Theorem 1.2 [C]. `ambient60.py`, Part 1, draws 40 random automorphisms of all coordinates (x, z) for the Fano form (p = 2) and for x^5y + xy^5 (p = 3), and finds a degenerate face for the weight W or W'' in each case.
- Section 1.3, Example 1.5 and Remark 11.3 of note 55. `ambient60.py`, Part 2, computes the change x = X + Z, y = Y + Z for z^5 + 2x^2y^2(x + y) over F_5 and the three faces of its Newton polytope with a torus singular point. Example 1.5 is exact. It reproduces the phenomenon of Remark 11.3 of note 55, which is [C] there.
- `brute60.py prop54`, `prop111` and `thm112` check Counterexample 3.1, Counterexample 4.1 and Theorem 11.2 of the note. These statements are [P]. The scripts are only checks.

## The files

- `lib60.py`: polynomials over F_p, faces, cleaning, composition, and the torus tests by Gröbner bases with the Rabinowitsch variable.
- `lab60.py`: the lab rows (Section 5). An optional argument filters the rows, for example `2,3,1-1-1,4`.
- `brute60.py`: the brute force over GL_n(F_p) and the counterexamples. The first argument is the mode: `rows`, `prop54`, `prop111` or `thm112`.
- `c4.py`: the C4 test cases (Section 6).
- `ambient60.py`: changes of all coordinates (Sections 1.2 and 1.3).
- `lab60.out`, `brute_rows.out`: the recorded outputs of `lab60.py` and `brute60.py rows`.

## Run

From the root of the repository:

```sh
python3 lab/notes/60/c4.py
python3 lab/notes/60/ambient60.py
python3 lab/notes/60/brute60.py prop54
python3 lab/notes/60/brute60.py prop111
python3 lab/notes/60/brute60.py thm112
python3 lab/notes/60/brute60.py rows
python3 lab/notes/60/lab60.py
```

## Expected output

`lab60.py` prints one line for each row of note 55 and ends with:

```text
issues: 0
```

`brute60.py rows` prints one line for each form and ends with:

```text
(2, 3, (1, 1, 1), 4) agree 12 of 12 ; preparable 3
(3, 2, (1, 1), 6) agree 12 of 12 ; preparable 3
(5, 2, (1, 1), 5) agree 12 of 12 ; preparable 4
```

`c4.py` ends with:

```text
p=2 Fano xyw(x+y+w): 168 linear changes over F_2, top face degenerate in 168
p=3 x^5y+xy^5: 48 linear changes over F_3, top face degenerate in 48
p=5 x^4y+xy^4: 480 linear changes over F_5, top face degenerate in 480
```

`ambient60.py` prints `Part 1, Fano p=2: {'W': 21, "W''": 19, 'none': 0}`, `Part 1, p=3 x^5y+xy^5: {'W': 38, "W''": 2, 'none': 0}` and, for Part 2, `F' has no monomial in k[X^5,Y^5,Z^5]: True` and three faces with a torus singular point.

`brute60.py prop54` prints `weight preserving changes over F_3: 12  top face degenerate: 12`. `brute60.py prop111` prints the strict transform `t**4*x + t**2 + t + z**3` and the gradient `[1, 0, 0]` at P. `brute60.py thm112` prints three points t0 with phi'(t0) = 0 and phi''(t0)/2 different from 0.

## Run time

Measured on one core of a laptop:

- `c4.py`: 20 s.
- `ambient60.py`: 3 s.
- `brute60.py prop54`, `prop111`, `thm112`: 2 s to 7 s each.
- `brute60.py rows`: 46 s.
- `lab60.py`: 110 s. The recorded output says 152 s.

## Dependencies

All scripts need sympy (the note used sympy 1.14.0). `lab60.py`, `c4.py` and `brute60.py` also need numpy (2.5.5 here). `lab60.py`, `c4.py` and `brute60.py thm112` also need galois (the note used galois 0.4, the run here used galois 0.4.11). `lab60.py` and `brute60.py rows` read the recorded files in `../55`.

```sh
python3 -m pip install sympy==1.14.0 galois==0.4.11 numpy
```

## Changes from the original

The original scripts added their own absolute directory to `sys.path` and read the files of note 55 from an absolute path. The copies add the directory of the script to `sys.path` and read the files of note 55 from `../55`, relative to the script. There is no other change.
