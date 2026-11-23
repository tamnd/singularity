# 02. The goal

## 2.1 In one sentence

Prove in Lean that every variety of dimension 4 over a field of positive characteristic has a resolution of singularities, and on the way formalize the whole theory that the problem rests on, each result with its paper, its proof in words and its Lean proof, in public, at singularity.tamnd.com.

## 2.2 Why now

Three facts of 2026 make this a project and not a wish. Document 01 has the sources.

1. **The char 0 theorem is already in Lean, twice.** `resolutionorg/hironaka` (Apache-2.0, October 2026, about 420,000 lines) proves Hironaka's Main Theorems I and II and Kollár's and Włodarczyk's functorial forms; the riemann-lean release of 2026-11-20 has a second, independent proof of about 140,000 lines (document 05). AxiomMath/Stacks (November 2026) has blowups, excellence and a model-written resolution of excellent surfaces, and google-deepmind/formal-conjectures states the open problem. The machinery that every route needs (blowups, normal crossings, blowup sequences, the monomial case) exists under a licence the project can use. The project starts at the point where the characteristic p difficulty starts.
2. **Large formalizations are fast now.** In 2026 Fermat's Last Theorem was formalized with AI systems (`anthropics/fermats-last-theorem`, September), the hironaka formalization of char 0 resolution was written by Claude agents and published in October 2026, and AxiomMath/Stacks has about 16 million lines, most of them written by models. The cost of formalizing a known proof, even a long one like Cossart-Piltant, has fallen by orders of magnitude. What is still slow is checking statements and reading proofs (document 01).
3. **AI systems produce research results that experts accept,** in combinatorics, number theory and analysis, monthly through 2026. None is yet in this area. The problem is a fair test: it is old (Zariski, Abhyankar, Hironaka), central, well posed, and has a clean formal statement.

This does not make the open problem easy. Many strong mathematicians have worked on it for 60 years. The plan treats the open case as a research bet and makes every other part of the project worth doing if the bet fails.

## 2.3 The levels of success

| Level | Name | What it means | Measured by |
|---|---|---|---|
| G1 | The library | every theorem of tiers T1 to T7 of document 07 is `proved` in Lean: the known theory, from regular rings to Cossart-Piltant, alterations and local uniformization of Abhyankar valuations | the node count by tier, `records/status.json` |
| G2 | The first formal proofs | first machine-checked proofs of resolution in dimensions 2 and 3 in every characteristic, and of de Jong's theorem | the trust rows Q0 to Q5 of those top theorems |
| G3 | The handbook | Volumes 0 to 8 released, every chapter `reviewed` | releases of the handbook |
| G4 | New partial results | a new theorem on the problem, accepted by experts: for example P1 of 3.4 for $n = 4$ in some range of $p$, local uniformization of a new class of valuations in dimension 4, a new monotone invariant for degree $p$ hypersurfaces, a patching theorem in dimension 4, or a new counterexample to a conjectured invariant | a proved node of kind `theorem` or `counterexample` on a route, with a preprint read by an outside expert |
| G5 | The open case | `ResolutionDimFourCharP` proved, with all nine trust rows **yes** | 06.6 and 14 |
| G6 | Beyond | all dimensions (`ResolutionOfSingularities` for every $p$), or the strong, embedded and principalization forms | the same |

G1 to G3 are engineering with known difficulty. G4 is research with a reasonable chance in two years. G5 and G6 are the open problem. The milestones (document 15) are set so that each one finishes some of G1 to G4, and the project reports its progress on each level separately.

## 2.4 What "all related theories and papers" means

It means the corpus of document 07: every paper and book whose results are on a path from the axioms of commutative algebra to one of the theorems of 14.2 or to a step of a route of document 04. For each such paper the project keeps a record, a node for each result it uses, and a status. It does not mean all of algebraic geometry. A paper enters the corpus when a node needs it, and the corpus list says why each paper is there. Document 07 sets the first list, 142 rows of papers and books in nine tiers.

## 2.5 Non-goals

- **Not a new resolution algorithm in char 0.** The base has one. The project may formalize the weighted and logarithmic methods (tier T8 of document 07) because the char p routes need them, not for their own sake.
- **Not Mathlib.** The project sends general parts upstream (09.5) but does not wait for review and does not shape its code to the Mathlib review queue.
- **Not mixed characteristic first.** Arithmetic threefolds and excellent schemes are in the corpus, but the target is varieties over a field.
- **Not a claim engine.** The project does not announce a solution of the open problem on the strength of a Lean build. 06.6 has the rule.

## 2.6 What would show the plan is wrong

- If the base does not build on the project's machines, or its char 0 boundary (05.5, step 5) runs through the blowup and normal crossings files, the char-free foundations must be rewritten, at a cost of several months. Measured in milestone S1.
- If the fidelity battery finds that the char 0 statements of the base are not faithful, or the two bases disagree (05.6), every use of the base must be re-checked. Measured in S1.
- If, after the formalization of Cossart-Piltant (S6), no route has a node of the size of a paper lemma that is new and true, the G4 plan is wrong and the project re-plans its research with the experts it has met by then.
