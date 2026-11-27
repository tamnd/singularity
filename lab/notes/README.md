# The scripts of the research notes

Each folder `NN/` has the scripts that research note NN gives as evidence for its claims with the tag [C] (numerical evidence only). The file `NN/README.md` names the claims, gives the commands, the expected output and the run time, and lists the dependencies. Run the commands from the root of the repository. Each script finds its helper modules and its data by paths relative to its own file. The scripts of note 61 use `53/lib53.py`, and the script `62/fam3_rerun.py` uses `56/tower.py`.

| Folder | Note | Dependencies |
|---|---|---|
| `50/` | Conjecture L° and Hypothesis H1 for linear corner runs in four variables | standard library |
| `51/` | a centre rule for the rigid layer | standard library |
| `52/` | referee report on note 50 | standard library |
| `53/` | referee report on note 51 | standard library |
| `54/` | planar corner runs in degree 3, and in every degree below p | NumPy for `core54.py`, `selftest.py` and `search54.py` |
| `55/` | Newton and Frobenius preparation | sympy, except `summ.py` |
| `56/` | the parts of Target T, the low degree experiment | standard library |
| `57/` | zero defect projections and independent defect | standard library |
| `59/` | referee report on note 57 | standard library |
| `60/` | referee report on note 55 | sympy, NumPy and galois |
| `61/` | the residual slope on the characteristic polyhedron | standard library |
| `62/` | referee report on note 56 | standard library |
| `63/` | referee report on note 54 | standard library |

The test `tests/test_smoke.py` runs each script that takes less than 30 seconds and uses only the standard library, and it compares the output with the expected lines of the folder. The workflow `lab` runs it:

```sh
cd lab/notes
python3 -m unittest discover -s tests -t . -v
```

The long searches are not in the test. A search over finite fields, along finite words and with a budget, can find a counterexample, but it cannot prove that there is none. So a [C] claim stays a claim of its note.

The notes 58, 64 and 65 are not here yet, because they are still being written. The large outputs, the logs of the long runs and the downloaded papers are not here.
