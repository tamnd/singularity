# 10. tamnd/singularity-agent: `sing`

`sing` is one Go binary. It does for this project what `rh` does for riemann: it indexes the Lean code, computes the status of the map, runs the trust checks, builds the site. It also runs the agent roles that write statements, proofs, examples and text, and the computations of the lab. The shape of the code follows riemann-agent (`cmd/`, `index/`, `trust/`, `site/`, `agent/`, `llm/`, `prompts/`), so the two can share packages later.

## 10.1 Commands

```
sing help | version
sing index      -lean ../singularity -out records/index.json      # Lean env → declarations, uses, sorry, axioms
sing status     -content ../singularity                            # map + index → records/status.json
sing trust      [-quick] -lean ../singularity                      # 14: axioms, replay, comparator → records/trust.json
sing fidelity   -node SG... | -all                                 # 06.3: run F1 to F5 for a node → records/fidelity.json
sing paper add  <arXiv id | DOI> | list | show <key>
sing node new | check | graph [-route R1] [-dot]
sing queue      [-role prover] [-n 20]                             # the work queue, with the reason for each rank
sing agent run  <role> [-node SG...] [-budget 5]                   # one run of a role; writes a run record and a branch
sing agent report -week 2026-W48                                   # the weekly report (10.8)
sing lab run    <spec> | list | show <run>                         # 13
sing base fetch | build | boundary | split                         # 05.5: the char 0 base
sing site build -content ../singularity -handbook ../singularity-handbook/build -out public
sing site check -dir public | serve -dir public
```

Exit codes as in riemann-agent: 0 success, 1 a check failed, 2 usage, 3 not written yet (the message names the milestone).

## 10.2 Lean access

`sing` talks to Lean in three ways, from cheap to expensive:

1. **Index.** One Lean program, run with `lake env lean --run`, imports `Singularity` and writes each constant with its type, its module, the constants it uses, and whether it depends on `sorryAx`. This is `rh extract` adapted.
2. **Check a file.** `lake env lean <file>` with a JSON message log, for the edit and check loop of a role. A role always works in a fresh worktree of `tamnd/singularity`, so a run cannot break `main`.
3. **Interactive.** A long-lived Lean REPL (the `repl` of leanprover-community, or Pantograph) for the prover role, so that a proof can be tried tactic by tactic against goal states. The REPL runs in a sandbox with no network and a read-only Mathlib.

## 10.3 The roles

Each role is a prompt in `prompts/<role>.md` (front matter with `role` and `version`, as riemann-agent), a Go driver in `agent/<role>.go`, and a test with a fake model.

| Role | Input | Output | Checked by |
|---|---|---|---|
| `reader` | a paper record and its text | the list of its numbered results with page and number; proposed nodes and `uses` edges | a person accepts each node |
| `stater` | a node | the Lean statement in `Statements/` or in a module, with a docstring | build; F1, F2 of 06.3 |
| `prover` | a `stated` node whose uses are `proved` or `proved-mod` | a proof, or a decomposition into new lemma nodes with statements | build; `sing index` shows no `sorry` |
| `planner` | a route and its nodes | the next nodes to state, and a decomposition of a hard node into steps; a short note on why | a person, for any change of `routes.yaml` |
| `refuter` | a statement or a conjecture | a Lean proof of the negation, a counterexample from the lab, or a trivial proof (F4) | build; lab record |
| `explorer` | a question of a route (for example "does invariant ι drop on all examples of degree ≤ d") | a lab spec and its run; a conjecture node when the data suggests one | lab record; a person for a new conjecture node |
| `porter` | a failing build after a bump, or a file of the base | the fix; the `CharZero` split of 05.5 | build |
| `explainer` | a declaration or a node | a docstring, the L2 text of a node, the round-trip English of F5 | a person |
| `writer` | a handbook chapter brief | a chapter section | a person; the handbook check |
| `linker` | a node | its Math 2.0 node and its references | `sing site check` |

The `planner` role is where the research happens: it reads the route documents (04), the status of the map and the lab results, and proposes the next steps. Its proposals are cheap to make and expensive to follow, so a person approves each change of a route.

## 10.4 The queue

The work queue has every node that a role can act on. The rank of a node is

$$
\text{rank} = \frac{w_{\text{route}} \cdot (1 + \text{unblocks})}{1 + \text{attempts}} \cdot \text{age factor}
$$

where `unblocks` is the number of nodes that wait only on this node, and `attempts` counts the failed runs. `sing queue` prints the rank and the reason, so a person can see why the agent works on something. Route weights are in `blueprint/routes.yaml` and are set by people.

## 10.5 The loop of one run

1. Take the top item of the queue for the role, or the node given with `-node`.
2. Make a worktree and a branch `agent/<role>/<tag>-<run>`.
3. Build the context: the node, its uses (statements and docstrings), the papers and the pages of the source, nearby Lean declarations (search by name and by type), and the earlier failed attempts with their error messages.
4. Call the model. For `prover`, iterate: propose a proof, check it in the REPL, read the errors, repair, up to the step and the budget limits.
5. Check the result with the checks of the role (10.3).
6. Write a run record and, on success, open a pull request with the record in its body.

## 10.6 Models, budgets and the ledger

`agent.yaml` in `tamnd/singularity` sets the models and the budget:

```yaml
models:
  default: claude-sonnet-5-5
  prover: claude-opus-5-5
  planner: claude-opus-5-5
  refuter: claude-opus-5-5
  linker: claude-haiku-5-5
budget:
  day: 200      # dollars
  run: 20
  role:
    prover: 120
    refuter: 30
```

As in riemann-agent: with no `agent.yaml` the budget is zero and no call goes out. Every call goes into `agent/ledger.jsonl` with the run, the role, the model, the prompt version, the tokens and the cost. The model ids are configuration, not code: a new model is a change of `agent.yaml`, tested by the evaluation of 10.9.

## 10.7 Untrusted text

Paper text, web pages and lab output are data, not instructions. A role puts them in the prompt inside a marked block and its prompt says that instructions in the block are ignored. A role never runs a command or fetches a URL that comes from such text. The lab runs in a container with no network (document 13).

## 10.8 The weekly report

`sing agent report` writes `reports/2026-Wnn.md` in `tamnd/singularity`: the nodes that changed status, the pull requests opened and merged, the spend by role, the lab runs, the refuted conjectures, and the five largest open nodes of each route with what blocks them. The site shows the reports as the timeline (document 12).

## 10.9 Evaluation of the agent

A fixed set of 200 tasks, `eval/tasks/`, taken from the project's own history: statements to write, lemmas to prove, failed builds to fix, all with a known answer. Each model or prompt change runs the set and reports the pass rate and the cost. A change that lowers the pass rate by more than 5 points is not merged. The set grows by 10 tasks each month from the merged pull requests.
