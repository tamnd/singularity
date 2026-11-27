# Note 61: the residual slope on the characteristic polyhedron

These are the scripts of research note 61, "The residual slope on the characteristic polyhedron, and the centre rule for m = 2p" (track M2, issue 287). They use the exact arithmetic of note 53: `lib61.py` imports `lib53.py` and `walk61.py` imports `t_random.py` from the folder `../53`.

## The claims

- Section 61.1 to 61.3, the lab tests T1 to T4 [C], with `t_single.py`. T1: 0 failures in 5400 random substitutions z -> u z + c with base changes, for p = 3, 5, 7. T2 (Lemma 61.8): 811 cases with E_+ nonempty, 0 failures. T3 (Lemma 61.7): 1800 samples, 0 failures. T4 (Proposition 61.10): 3716 cases, 0 failures, except 6 samples with f = (z + c)^(2p).
- Examples 61.13 and 61.14 (omega increases under omega-constant centres). The examples are [P]. `t_jump.py` finds the jumps (p = 3, depth 4: 37912 points, 64 jumps, none over the centre of Rule 61.9), `min_jump.py` reduces them, and `ex61_jumps.py` recomputes the two examples. `ex_jump.py` is a control where the rule centre is the point and omega drops.
- Example 61.17 (the cycle of Rule 61.9 of period 2p + 1). The example is [P]. `loop54b.py` finds the cycle by exact search for p = 3 (start c = 3 and c = 9) and p = 5 (start c = 5). In mode `om` (Rule 61.9') omega drops at once at each point over the centre. `loop54.py` follows one branch.
- Section 61.8, "Lab" [C], the evidence for Conjecture 61.18 (a) and (b): the walks of Rule 61.9 (`walk61.py ... plain`, `campaign.sh`) and of Rule 61.9' (`walk61.py ... om`, `campaign_om.sh`). Under the rule centres the intrinsic omega never increased. Under Rule 61.9' each walk ended with a drop of the multiplicity. `agg.py` makes the tables from the outputs.
- Section 61.8, "Section 61.6" [C]: the tests of Lemma 61.15, Proposition 61.16 and the persistence of Lambda, with `t_W.py`.

## The files

- `lib61.py`: monomial valuations, the vertex test, preparation, the intrinsic invariants and the values at generic points.
- `walk61.py`: walks. Usage: `walk61.py p walks depth family seed mode`, with mode `plain`, `res` or `om`.
- `campaign.sh`, `campaign_om.sh`: all walk campaigns of Section 61.8. They write to `out/` in this folder.
- `agg.py`: the tables of Section 61.8 from `out/`. Usage, in this folder: `python3 agg.py w_ plain` or `python3 agg.py om_`.
- `t_single.py`: tests T1 to T4. Usage: `t_single.py p samples family seed`.
- `t_jump.py`: the jump search. Usage: `t_jump.py p samples seed depth`.
- `min_jump.py`: the reduction of a jump. It reads `data/jump.txt`, the output of the jump search of the note. Usage: `min_jump.py [index] [keep]`.
- `ex61_jumps.py`, `ex_jump.py`: Examples 61.13 and 61.14, and the control.
- `loop54.py`, `loop54b.py`: Example 61.17. Usage: `loop54b.py p c [plain|om] [depth]`.
- `t_W.py`: Section 61.6. Usage: `t_W.py p walks depth family seed`.
- `trace61.py`: the trace of one walk. Usage: `trace61.py p family depth mode [pick]`.
- `data/jump.txt`: the output of `t_jump.py` of the note, for p = 3 and p = 5 at depth 4.

## Run

```sh
python3 lab/notes/61/ex61_jumps.py
python3 lab/notes/61/ex_jump.py
python3 lab/notes/61/min_jump.py
python3 lab/notes/61/loop54b.py 3 3
python3 lab/notes/61/loop54b.py 3 9
python3 lab/notes/61/loop54b.py 5 5 plain 12
python3 lab/notes/61/loop54b.py 3 3 om
python3 lab/notes/61/walk61.py 3 300 30 gen 11 om
python3 lab/notes/61/walk61.py 3 600 30 gen 33 plain
python3 lab/notes/61/t_single.py 3 300 gen 1
python3 lab/notes/61/t_jump.py 3 50 1 4
python3 lab/notes/61/t_W.py 3 30 10 ex54 5
python3 lab/notes/61/t_W.py 3 25 8 r3bad 1
sh lab/notes/61/campaign.sh
sh lab/notes/61/campaign_om.sh
```

The campaign scripts run 8 and 6 processes at the same time.

## Expected output

- `ex61_jumps.py`: Example 61.13 (printed as 61.10, the old number) gives "prepared True omega 1/12" and the rule centre (2,) with max intrinsic omega 1/12, and the test centre (1, 2) with max intrinsic omega 1/3. Example 61.14 (printed as 61.11) gives "prepared True omega 1/3" and the test centre (0, 1, 2) with max intrinsic omega 2/3.
- `ex_jump.py`: for p = 3 the maximum over the points is "omega* = 5/3", below omega 2 at the point.
- `min_jump.py`: "xi: R1 delta 2 mu {0: '0', 1: '2/3', 2: '4/3'} omega 0" and "intrinsic 1/3" at xi', and "vertex at xi' solvable".
- `loop54b.py 3 3` and `loop54b.py 3 9`: "CYCLE of length 7 after 0 steps". `loop54b.py 5 5 plain 12`: "CYCLE of length 11 after 0 steps". In mode `om` the frontier is 0 at each depth, so no point keeps iota.
- `walk61.py 3 300 30 gen 11 om`: the stats have "walks": 300, "steps_main": 274, "steps_div": 113, "drops": 299, "ends_smooth_or_z": 1 and no "om_up" key. This is the row p = 3, gen of the table of Rule 61.9' (387 steps).
- `walk61.py 3 600 30 gen 33 plain`: the same output as the run of the note for p = 3, gen, plain (1385 steps, 19 walks at the depth limit).
- `t_single.py 3 300 gen 1`: 'T1_bad': 0, 'T2_bad': 0, 'T3_bad': 0, 'T4_delta_bad': 0. The note does not record the seeds of T1 to T4, so the counts differ from the counts of the note.
- `t_jump.py 3 50 1 4`: 'up_rule': 0 and 'zprime_up': 0.
- `t_W.py 3 30 10 ex54 5`: the same output as the run of the note: 'walks': 30, 'R3': 46, 'e_hist': {0: 46}, 'lemma_fail': 0, 'tau_hist': {2: 45, 3: 1}, 'persist': 30, 'persist_fail': 0. This is Example 5.4 in Section 61.8.

## Run time

Measured on one core of a laptop: `ex61_jumps.py` 0.1 s, `ex_jump.py` 1.4 s, `min_jump.py` 0.1 s, `loop54b.py 3 3` 0.3 s, `loop54b.py 5 5 plain 12` 7 s, `loop54b.py 3 3 om` 0.1 s, `walk61.py 3 300 30 gen 11 om` 4 s, `walk61.py 3 600 30 gen 33 plain` 22 s, `t_single.py 3 300 gen 1` 6 s, `t_jump.py 3 50 1 4` 9 s. `t_W.py 3 30 10 ex54 5` takes 2 s. The family `r3bad` is slow: `t_W.py 3 25 8 r3bad 1` did not finish in 15 minutes, and `t_W.py 3 2 3 r3bad 1` takes about 1 minute of CPU time. `t_jump.py 3 1500 1 4` takes about 7 minutes and gives about 4000 samples, as in the note (3982 samples, 37912 points). The seed of the run of the note is not recorded: with seed 1 the run gives 37338 points and 8 jumps, in place of 37912 points and 64 jumps, and again 'up_rule': 0 and 'zprime_up': 0. The file `data/jump.txt` keeps the jumps of the note. The campaigns take more than one hour: each process has a limit of 3000 s (`campaign.sh`) or 2400 s (`campaign_om.sh`).

## Dependencies

Python 3.9 or later, standard library only. The folder `../53` must be present.

## Changes from the original

Each script has two lines at the top that put the folder of the script on `sys.path`. The path of `lib53.py` is `../53` relative to the script, and the campaign scripts change to their own folder. `min_jump.py` reads `data/jump.txt` relative to the script. The mathematics is not changed. The outputs in `out/` of the note and the downloaded paper in `src/` are not copied. `t_basic.py` is not copied, because the note does not cite it.
