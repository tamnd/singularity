# Note 53: referee report on note 51

These are the scripts of research note 53, the referee report on note 51 (track M2, issue 287). The code is independent of the code of note 51. The scripts of note 61 import `lib53.py` and `t_random.py` from this folder.

## The claims

- Section 53.8, "Lab" [C]: the table of the random tests. For each sample the coordinate is made adapted, and each point of multiplicity 2p over each permissible coordinate centre is examined (all charts, all lambda in F_p, all nu in F_p). The counts "nu != 0" (Lemma 3.3 of note 51), "hyp up" (Proposition 4.2 of note 51) and "re up" (Remark 4.4 of note 51) are 0 in all rows. The script is `t_random.py`.
- Section 53.8, the weak transform test of Lemma 53.1: no exception in 3105 tests for p = 3, 7520 for p = 5 and 15820 for p = 7. The script is `t_random.py` with the family `gen`.
- Summary table, Examples 5.2, 5.3 and 5.4 of note 51 and Proposition 2.1 of note 51, recomputed for p = 3, 5, 7, and Example 53.3 (omega depends on the adapted coordinate) and Example 53.6 (R3 point). The script is `t_examples.py`. Example 5.2 prints "same data: True".
- Section 53.7: the first step of Example 4.5 of note 44 goes from an R1 point with iota = (1, 2 + 1/2p) to points with iota = (1, 1 - 1/2p) (R3) or (1, 0) (R1), for p = 3, 5, 7. The script is `t_ex45.py`.

## The files

- `lib53.py`: exact arithmetic over F_p in three base variables, translations by binomial coefficients, q-preparation, the tangent cone, the vertex space by the Taylor criterion, the linear adaptation, and the blowups in all charts at all rational points and all nu in F_p.
- `t_examples.py`: the explicit examples.
- `t_random.py`: the random tests and the walks. Usage: `t_random.py p samples family walks`, with family `gen` or `pow`.
- `t_ex45.py`: the first step of Example 4.5 of note 44.

## Run

```sh
python3 lab/notes/53/t_examples.py
python3 lab/notes/53/t_ex45.py
python3 lab/notes/53/t_random.py 3 200 pow 120
python3 lab/notes/53/t_random.py 3 200 gen 120
python3 lab/notes/53/t_random.py 5 200 pow 120
```

The rows of the table of Section 53.8 are `t_random.py p 200 family 120` for p = 3, 5 and `t_random.py 7 60 pow 30` for p = 7.

## Expected output

The outputs of `t_examples.py`, `t_ex45.py` and `t_random.py 3 200 pow 120` and `t_random.py 3 200 gen 120` are the same as the outputs of the runs of the note, byte for byte. Key lines:

- `t_examples.py`: Example 5.2 gives "same data: True", Example 5.4 gives "state at step 7 recurs at step 22" for p = 7, and the last three lines start with "R3 p=3: regime=R3", "R3 p=5: regime=R3" and "R3 p=7: regime=R3".
- `t_ex45.py`: the line "p=7 origin R1 iota=(1, Fraction(29, 14))" and the line "chart x0 lam={1: 0} nu=0: R3 iota=(1, Fraction(13, 14))".
- `t_random.py 3 200 pow 120`: the first line has 'samples': 200, 'pts': 870, 'nu_bad': 0, 'hyp_up': 0, 'nohyp_up': 16 and 'readapt_up': 0. The last line has 'walks': 120, 'pts': 237 and 'class_up': 0.
- `t_random.py 3 200 gen 120`: the first line has 'pts': 754, 'nu_bad': 0 and 'hyp_up': 0, and one line has "weak transform (3105, 0)".

## Run time

Measured on one core of a laptop: `t_examples.py` 0.5 s, `t_ex45.py` 0.1 s, `t_random.py 3 200 pow 120` 21 s, `t_random.py 3 200 gen 120` 39 s. The runs for p = 5 and p = 7 take longer. The run for p = 7 with the family `gen` did not finish in the time of the note.

## Dependencies

Python 3.9 or later, standard library only.

## Changes from the original

Each script has two lines at the top that put the folder of the script on `sys.path`, so that the scripts run from any directory and with `python3 -I`. The mathematics is not changed. The outputs `out_*.txt`, `t_examples.txt`, `t_ex45.txt` and `weak7.txt` of the note are not copied, because the scripts make them again.
