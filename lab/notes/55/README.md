# Note 55: Newton and Frobenius preparation

These are the scripts of research note 55, "Newton and Frobenius preparation" (track NW). The scripts are the lab of Part C of the note. They search changes of coordinates that prepare a resonant weighted homogeneous face z^p + h, and they make certificates for the failures in the standard weight. Note 60 is the referee report on note 55. Its scripts are in `../60` and use the recorded files of this folder as input data.

## The claims

- Section 7, the lab table [C]. The columns from "resonant, degenerate" to "not prepared over F_p" come from `prep.py` (the rows with p = 2 and p = 3, and the rows with p = 5 and n = 2), `prep_p5n3.py` and `prep_p5n3w.py` (rows with p = 5, n = 3). `summ.py` makes the table from the recorded files `run_*.jsonl`. The last column, "certified unpreparable", comes from `cert.py`. The certificates themselves use Theorems 4.1 and 4.3 of the note and are [P] for the rows marked so.
- Section 6, Proposition 6.5, "full preparation" [C]: the lab prepared all 12 random resonant cubics with p = 3, n = 3, 10 over F_3 and 2 over F_27. This is the row (3,3,(1,1,1),3) of `run_p3.jsonl` (10 forms prepared by a linear change over F_3) and the two lines "prepared over F_27" of `cert_out.jsonl`.
- Section 11, Remark 11.3 [C]: for z^5 + x^4y + xy^4 over F_25 the linear change that moves the three singular lines to the coordinate axes gives a form with no p-th power monomial and with three degenerate edges. The script is `ambient.py`.
- `examples.py` checks Examples 5.3, 5.5 and 6.4 (the Fano form). These examples are [P]. The script is only a check.

## The files

- `prep.py`: the search of Section 7. It also has the polynomials over F_p, the resonance test, the Gröbner test for torus critical points and the faces.
- `gfq.py`: the finite fields F_{p^k}.
- `cert.py`: the certificates for the failures in the standard weight.
- `summ.py`: the table of Section 7 from the recorded files. It uses only the standard library.
- `examples.py`: Examples 5.3, 5.5 and 6.4.
- `ambient.py`: Remark 11.3.
- `prep_p5n3.py`, `prep_p5n3w.py`: the rows with p = 5, n = 3 and D = 5. `prep_p5n3w.py` takes the index of one weight, so that the weights can run in parallel.
- `run_p2.jsonl`, `run_p3.jsonl`, `run_p5n2.jsonl`: the recorded output of `prep.py` for p = 2, 3 and 5 (n = 2).
- `run_p5n3_old.jsonl`, `run_p5n3.jsonl`: the recorded output of `prep_p5n3.py` for the weight (1,1,1). The row (5,3,(1,1,1),5) of the table has the 7 forms of the two files.
- `run_p5n3_w1.jsonl`, `run_p5n3_w2.jsonl`, `run_p5n3_w3.jsonl`: the recorded output of `prep_p5n3w.py` for the weights (1,1,2), (1,2,2) and (1,2,3).
- `cert_out.jsonl`: the output of `cert.py` on `run_p5n2.jsonl`, `run_p3.jsonl` and `run_p2.jsonl`, in this order.
- `cert_p5n3.jsonl`: the output of `cert.py` on the forms of the row (5,3,(1,1,1),5).

## Run

From the root of the repository:

```sh
python3 lab/notes/55/summ.py lab/notes/55/run_p2.jsonl lab/notes/55/run_p3.jsonl lab/notes/55/run_p5n2.jsonl lab/notes/55/run_p5n3_w1.jsonl lab/notes/55/run_p5n3_w2.jsonl lab/notes/55/run_p5n3_w3.jsonl lab/notes/55/run_p5n3_old.jsonl lab/notes/55/run_p5n3.jsonl
python3 lab/notes/55/examples.py
python3 lab/notes/55/ambient.py
python3 lab/notes/55/cert.py lab/notes/55/run_p5n2.jsonl lab/notes/55/run_p3.jsonl lab/notes/55/run_p2.jsonl > cert_out.jsonl
python3 lab/notes/55/cert.py lab/notes/55/run_p5n3_old.jsonl lab/notes/55/run_p5n3.jsonl > cert_p5n3.jsonl
python3 lab/notes/55/prep.py SEED COUNT [PRIMES [NS]] > run.jsonl
python3 lab/notes/55/prep_p5n3w.py SEED COUNT WEIGHT_INDEX > run_p5n3_w.jsonl
```

For `prep.py`, PRIMES is a comma separated list (the default is 2,3,5) and NS is a comma separated list of the numbers of variables (the default is 2,3). The note used COUNT = 12. The note does not record the seeds, so a new search gives other random forms. The recorded files are the data of the table.

## Expected output

`summ.py` prints the table of Section 7 in Markdown, with one row for each (p, n, w, D). The first and the last rows are:

```text
| (2,3,(1,1,1),2) | 12 | 12 | 12 | 0 | 0 | 0 |
| (5,3,(1,1,1),5) | 7 | 7 | 0 | 0 | 7 | 7 |
```

The columns are: the number of forms, the forms with a torus critical point off the zero set, the forms prepared by a linear change, the forms prepared by a Frobenius type change, the forms not prepared, and the forms not prepared with a critical point off the zero set.

`examples.py` prints for the Fano form `crit points in P^2 over F_2: [...]  covers: 0` (seven points and no cover by three independent lines) and `F_p search: None` for each example.

`ambient.py` prints `number of terms of F o B: 12  p-th power monomials: []` and the three degenerate edges.

`cert.py` prints one JSON line for each form that is not prepared in the standard weight, with a `verdict`. On the three recorded runs the output has the same lines as `cert_out.jsonl`: 66 lines "certified unpreparable", 2 lines "prepared over F_27", 2 lines "cover exists, no preparation found" and 17 lines "undecided".

## Run time

Measured on one core of a laptop:

- `summ.py`: less than 0.1 s.
- `examples.py`: 0.4 s.
- `ambient.py`: 0.3 s.
- `cert.py` on the three recorded runs: 160 s of CPU time (9 min of wall time on a loaded machine). Most of the time goes to the forms with p = 2, n = 3 and D = 6.
- `prep.py`: the full search of the note took minutes for each prime. The rows with p = 5, n = 3 are slow, and the note made them with `prep_p5n3w.py`, one weight in each process.

## Dependencies

`summ.py` uses only the standard library. The other scripts need sympy (the note used sympy 1.14.0) for the Gröbner bases over F_p:

```sh
python3 -m pip install sympy==1.14.0
```

## Changes from the original

The original scripts added the current directory to `sys.path` and were run from their own directory. The copies add the directory of the script to `sys.path`, so they run from any directory. There is no other change.
