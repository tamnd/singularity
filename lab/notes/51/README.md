# Note 51: a centre rule for the rigid layer

These are the scripts of research note 51, "A centre rule for the rigid layer: the form (b'') of note 49" (track M2, issue 287).

## The claims

- Lemma 3.3 (the nu-lemma) [C]: 0 exceptions in 17 658 points. In each run of Section 7 the count `nu_nonzero` is 0.
- Proposition 4.2 [C]: omega in the coordinate z' does not increase under the rules (the count `omega_fixed_up` is 0 in mode `rule`), and it increases 9 times for random centres that violate the hypothesis (mode `rand`).
- Remark 4.4 [C]: after re-preparation omega can increase, at R1 points, 4 of 2606 points (mode `rule`, family `pow`, p = 3).
- Examples 5.2 to 5.4: one step of the rule, the drop with the monomial step and the divisorial step, and the loop of Example 5.4. The scripts are `loop51.py` and `loop51b.py`.
- Section 7, "Lab" [C]: the table of the walks. The script is `run51.py`. The campaign scripts `campaign.sh`, `expl.sh` and `variants.sh` run all rows. `ex51.py` gives the full traces of the explicit examples.

## The files

- `lib51.py`: exact polynomial arithmetic over F_p in three base variables, translation by Hasse binomials, preparation as in Lemma 2.1 of note 44, the tangent cone, the vertex space and the linear adaptation of Lemma 3.2, mu_k, omega, the class, the rules, and all points of multiplicity m over a coordinate centre in all charts.
- `run51.py`: walks. Usage: `run51.py MODE FAMILY p walks depth seed [N M]`, with MODE `rule` or `rand` and FAMILY `gen`, `pow`, `t44 N M`, `ex45`, `ex46` or `f1`. The environment variables `DIV=1` (the divisorial step) and `CLS=res` (the residual class) select the variants "div" and "div+res" of the table.
- `ex51.py`: the full traces of Examples 4.5 and 4.6 of note 44, of Theorem 4.4 of note 44 with (N, M) = (2, 4p + 1) and of the family `f1`, for p = 3, 5, 7. The argument is the depth (default 8). The output of the note is for depth 40.
- `loop51.py`, `loop51b.py`: Examples 5.2 to 5.4.
- `summ.py`: a summary of the lines of `run51.py` in output files.
- `campaign.sh`, `expl.sh`, `variants.sh`: the campaigns of Section 7. They change to their own folder and write to standard output.

## Run

```sh
python3 lab/notes/51/loop51.py
python3 lab/notes/51/loop51b.py
python3 lab/notes/51/ex51.py 40
python3 lab/notes/51/run51.py rule pow 3 200 30 3
DIV=1 python3 lab/notes/51/run51.py rule pow 3 200 30 3
python3 lab/notes/51/run51.py rand pow 3 20 30 3
sh lab/notes/51/campaign.sh > campaign.txt
python3 lab/notes/51/summ.py campaign.txt
```

## Expected output

- `loop51.py`: for p = 3, 5, 7 the line with MONO=True ends with "drop", and the line with DIV=True ends with "drop". The last lines (Example 5.4) give, for the class "plain", a sequence of R3 points with iota (1, '1'), and for the class "res" a drop.
- `loop51b.py`: "RECUR step 10 = step 3" for p = 3, "RECUR step 16 = step 5" for p = 5 and "RECUR step 22 = step 7" for p = 7. The period is 2p + 1.
- `ex51.py 40`: the same output as `ex51.txt` of the note, 570 lines. The first line is "== ex45 p=3 ()".
- `run51.py rule ...`: one line that starts with "rule pow 3 [] {", with 'nu_nonzero': 0 and 'omega_fixed_up': 0. The run `run51.py rule pow 3 200 30 3` gives the row "rule, base, pow, 3" of the table of Section 7 exactly: 'walks': 200, 'points': 2606, 'prep': 551, 'iota_up': 4, 'omega_up': 4, 'drops': 188, 'unterminated': 7. The 4 lines that start with "BAD ('iota_up'" are the 4 points of Remark 4.4, each from (1, Fraction(2, 15)) to (1, Fraction(1, 6)).

## Run time

Measured on one core of a laptop: `loop51.py` 1.5 s, `loop51b.py` 1.7 s, `ex51.py 40` 0.5 s, `run51.py rule pow 3 20 30 3` 4 s, `run51.py rand pow 3 20 30 3` 3 s. `run51.py rule pow 3 200 30 3` takes about 5 minutes. The campaigns take some hours: each run has a limit of 600 s to 1500 s.

## Dependencies

Python 3.9 or later, standard library only.

## Changes from the original

Each script has two lines at the top that put the folder of the script on `sys.path`, so that the scripts run from any directory and with `python3 -I`. The campaign scripts change to their own folder. The mathematics is not changed. These files of the folder of the note are not copied: `edit44.py` and `44-backup.md` (an edit of note 44, not evidence), the outputs `ex51.txt`, `campaign.txt`, `res_*.txt`, `variants.txt`, and the folders `par/` and `var/` (outputs of earlier runs).
