# The lab

This directory has the specs and the runs of the computation lab (spec 13, `docs/spec/13-computation-lab.md`). The tool is `sing lab` of [tamnd/singularity-agent](https://github.com/tamnd/singularity-agent). The engine is in Go, in the package `lab` of that repository. Spec 13 planned it in Rust. The specs still name the tool `sing-lab`.

A run is data from examples. It does not prove a statement. A result enters the map only as a node of kind `example`, `counterexample` or `conjecture`, as spec 13 says.

## The simulator

`sim/` has `labsim`, a small Python simulator for single examples, certificates and the test bank of the notes and the handbook. It has real charts with translations and cleaning, and the invariants rho, d and nu^G. See `sim/README.md`.

## The layout

- `specs/<name>.yaml`: a spec. It has the question, the node of the map, the inputs and the outputs. The name starts with the experiment: `e1-`, `e2-` or `e4-`.
- `runs/<id>/`: a run. The id is the date of the run, the name of the spec and the first 8 characters of the sha256 of the spec.
  - `record.json`: the sha256 of the spec, the version and the commit of sing, the seed, the host, the start and the wall time, the counts and the sha256 of each output.
  - `histogram.json`: for each case (p, n, q), the change d' - d of the residual order at each step, the residual order at the start, the reasons why the walks stop, the kangaroo points and the steps over the bound of Moh.
  - `examples.json` (E1): the first 100 examples of each increase of the residual order in each case, and the first walks over the stability bound. An example has F, the divisor, the chart and the translations.
  - `candidates.json` (E2 and E4): for each candidate and each case, the number of steps where the candidate goes up, stays or goes down, and the first failure. A candidate with a scope also has `out_of_scope`, the number of steps outside its scope, which it does not count.
  - `steps.json` (a fixed sequence): the polynomial and the invariants after each given blowup.
  - `summary.md`: a short summary in plain English.

## Run a spec

```sh
sing lab run lab/specs/e1-p2.yaml           # writes lab/runs/<id>/
sing lab run -walks 1000 lab/specs/e1-p2.yaml   # a short test run
sing lab list                                # lists the runs
```

A run is reproducible from the seed in the spec. Each walk has its own random source, which depends only on the seed, the number of the case and the number of the walk. The walks are added up in order, so the outputs do not depend on the number of threads. Two runs of the same spec differ only in the host and the times in `record.json`. An E2 spec names the E1 spec in `walks_from` and makes the same walks again. An E4 spec also has `select`, a list of pairs n and q. It makes again only the walks of those cases of the E1 spec, with the same random sources.

To check an example by hand, give its F, its divisor, its chart and its translations to `sing lab step`:

```sh
sing lab step -p 2 -q 4 -vars x,y,w -f "x^2*y^2*w^3*(w*(x+y)^4+x^13)" -divisor x,y,w -chart x -t y=1
```

## The mathematics

The engine follows section 2 of Hauser and Perlega, arXiv:1802.05010, over K = F_p.

- The equation is f = z^q + F with q = p^e and ord F >= q.
- Cleaning removes from F the monomials with exponents in qN^n. Over F_p this is a change z -> z + h of the variable z.
- The divisor E is a set of the variables x_i. Write F = prod_{i in E} x_i^(r_i) G with each r_i as large as possible. The residual order is d = ord G.
- The x_j-chart with the translations t_i in F_p maps z to x_j z and x_i to x_j (x_i + t_i) for i != j. The transform is F' = x_j^(-q) F(...). The order of f stays q if and only if ord F' >= q after the cleaning. A constant term c of F' is a q-th power. The cleaning removes it with z -> z + c^(1/q), which moves the point to the point of the strict transform over the point of the divisor. `histogram.json` counts these steps as `z_shift_steps`.
- The new divisor is {j} together with the i in E with t_i = 0. The engine cleans F' again.

In random walks the engine also removes q-th power units: when each term of F' has x_i + t_i to a power at least s, with s a multiple of q, it divides by (x_i + t_i)^s. This is a unit and a q-th power at the point. It does not change the cleanness, the order, the r_i, the residual order or the number of terms of the initial form of G. It keeps the polynomials small. The fixed sequences do not use it, so their polynomials are the literal transforms.

## Experiment E4

E4 computes the invariants of Cossart and Piltant, arXiv:1412.0868 (the key CP19 of the map), on the walks of E1 with q = p. The specs are `e4-p2.yaml`, `e4-p3.yaml` and `e4-p5.yaml`. Each one selects the cases n = 3 (a threefold z^p + g(x1, x2, x3)) and n = 4 of its E1 spec. At each point the engine computes these numbers for f = z^p + F with F clean. A clean F gives well adapted coordinates (CP19, Definition 2.24).

- m = p, since a walk keeps the order p.
- ord F = p delta (CP19, Definition 2.11).
- epsilon = ord F - sum r_i, the residual order d (CP19, Definition 2.25).
- omega = epsilon - 1 if a term of the initial form of F has an exponent prime to p in a variable outside E, and omega = epsilon otherwise (CP19, (1.11), (2.44) and Definition 2.68).
- kappa = 1 if omega = 0, and kappa >= 2 otherwise (CP19, Definition 2.68). The engine does not split the values >= 2.

The candidates are `cp-omega` (omega goes up), `cp-iota` (iota = (m, omega, kappa) goes up in the lexicographic order) and `cp-eps-jump` (epsilon goes up, and epsilon(x) = omega(x) with delta(x) an integer does not hold). Theorem 3.13 of CP19 says that `cp-iota` and `cp-eps-jump` never fail at a point with omega(x) > 0, under its hypotheses. So these two candidates count only the steps from a point with omega(x) > 0. The spec also has `d-over-q` of E2, for comparison. These candidates need q = p, and `sing lab run` refuses a spec that uses them on a case with q != p. The summary of an E4 run compares n = 3 and n = 4.

## What a run does not show

- The engine computes in the given coordinates x1, ..., xn after the cleaning. The theorem of Moh (SG00000015) is about well chosen coordinates. So a step over the bound p^(e-1) in a run is not a counterexample to the theorem. It is an example to check in other coordinates.
- The walks use only the points over F_p of the exceptional divisor and only point centres.
- A walk stops at a cap of its spec (the depth, the number of terms, the size of an expansion, the degree). So the data has fewer large polynomials than the family.
- For E2, a candidate with no failure on the walks is not proved to go down.
- For E4, the engine does not check condition (E) of CP19 (Definition 2.32), which Theorem 3.13 of CP19 assumes. It does not compute kappa in {2, 3, 4} (CP19, Definition 5.1) or the invariants of the projection, since these need a choice of coordinate that the engine cannot make. So E4 does not test the Projection Theorem (CP19, Theorem 5.5). The values of omega and epsilon do not depend on the well adapted coordinates (CP19, Remark 2.69), so a failure in E4 is not only a matter of coordinates. It must be checked by hand, with condition (E).

## Raw data

A spec with `raw: true` also writes `runs/<id>/raw/`, with each kangaroo point of each case in JSON lines, compressed with gzip. Git ignores these files, because they are large. The raw files of the runs here are on the project machine that ran them, in `~/sing/lab/runs/<id>/raw/`. `record.json` names the host.

## No containers

The lab runs the engine as a process on the host. Spec 13 runs the external tools (Singular, Macaulay2, SageMath) in containers with pinned images and no network. The lab does not use those tools yet. The container isolation is planned for the milestone that adds them.
