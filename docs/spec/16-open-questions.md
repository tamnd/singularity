# 16. Open questions

These are the decisions that the spec does not make. Each one has the options, a recommendation, the milestone by which it must be decided, and who decides. "Owner" means the owner of the repositories. "Experts" means the outside reviewers of 06.3 (F6) and 14.1 (Q7).

| Id | Question | Options | Recommendation | By | Who |
|---|---|---|---|---|---|
| Q-01 | Which char 0 base? | (a) resolutionorg/hironaka; (b) riemann-lean; (c) both | (c): hironaka as the dependency, riemann-lean only in the cross-check package (05.6). Settled in principle by the Apache licence of hironaka | S0 | owner |
| Q-02 | Which toolchain pin at the start? | (a) v4.33.1, the pin of riemann-lean; (b) v4.35.0, the pin of hironaka and AxiomMath/Stacks; (c) v4.36.0, the current stable release | (b), then (c) at the first monthly bump (09.3) | S0 | owner |
| Q-03 | Reduced or integral $X$; regular or smooth $Y$; birational in the statement? | (a) the statement of 06.1 (reduced, regular, isomorphism over the regular locus, dense); (b) the formal-conjectures form (integral, smooth, `BirationalOver`, perfect field) | (a) as the main statement, with a proved bridge to (b) (06.4) | S0, frozen at S2 after F6 | owner, experts |
| Q-04 | A separate repository for the base? | (a) a Lake dependency on hironaka; (b) a fork `tamnd/hironaka` for the `CharZero` split; (c) copy the files into `Singularity/Base` | (a) and (b): depend on upstream, change only in the fork, and offer the changes upstream | S1 | owner |
| Q-05 | How to find expert reviewers? | letters to the groups of 01 (1.3 to 1.5); a paid review; a workshop | letters first, at S0, with the statements and the trust page; a paid review of the statements (F6) if no one answers in two months; a small online workshop at S4 | S0 and S2 | owner |
| Q-06 | The weights of the routes | the first weights of 04.1 | keep them for the first year; change them only at milestone reports, from proved and refuted nodes | S3, then each milestone | owner, with the planner role's report |
| Q-07 | Use the Lipman proof of AxiomMath/Stacks (written by models, not reviewed)? | (a) depend on it after a human review and the fidelity battery; (b) prove Lipman again in the project | (a) if a review of its statement and of the definitions it uses passes, because the trust rows check the proof and the review checks the meaning; (b) if the definitions do not match the project's | S4 | owner, one expert |
| Q-08 | De Jong's theorem needs the moduli of stable curves | (a) state DM69 as a `proved-mod` hypothesis; (b) formalize enough of the moduli; (c) a proof that avoids it | (a) first, so that de Jong's argument is in Lean early, then (b) as library work; check what MingchenXia/Hironaka-lean has | S8 | owner |
| Q-09 | Share code with riemann-agent? | (a) a common Go module for the toolchain (index, trust, site); (b) a copy | (a) for `trust`, `index` and `site`, because the two projects have the same trust needs; (b) for the roles, which differ | S0 | owner |
| Q-10 | Reuse rhb for the handbook? | (a) fork rhb as `shb`; (b) a new builder | (a) | S0 | owner |
| Q-11 | How much to send upstream to Mathlib? | (a) tier T1 only; (b) T1 to T3; (c) nothing until the project is stable | (a) at S2, (b) from S5, with the authors listed; never block on review (09.5) | S2 | owner |
| Q-12 | Publication and the disclosure of AI | papers on the arXiv with the role and model credits; a statement of what people checked | follow 14.4; a research result (G4) is posted only after an outside expert has read it, with a section on how it was found and checked | S7 | owner, experts |
| Q-13 | Register with Palomar and publish `formalization.yaml`? | yes or no | yes, at S0, in the v0.4 schema that hironaka uses (14.5) | S0 | owner |
| Q-14 | What to do with the claimed proofs (01, 1.2)? | (a) ignore; (b) the lab test E9; (c) a formalization | (b) only; write to the author before any public result | S3 | owner |
| Q-15 | Is Target T (04.12) worth a route of its own? | a separate route with its own weight, or a part of R2 and R4 | decide after an expert reads 04.12 and the literature search for a known obstruction is done | S3 | owner, one expert |
| Q-16 | Which blowup API, if the three differ? | hironaka `IsBlowUpAlong`; riemann-lean `IsBlowup`; Mayeux's (arXiv:2609.28489); AxiomMath/Stacks | hironaka's, with a proved equivalence to each of the others where they meet the project (06.5, risk 3) | S1 | owner |
| Q-17 | Budget | 200 dollars a day for the agent at the start (10.6) | raise it only when the cost per proved node is measured (S2) | S2 | owner |

## 16.1 Questions for the experts

These are mathematical questions that the project cannot decide alone. They go in the first letters (Q-05).

1. Is the statement of 06.1 the one you would accept as "resolution of singularities in dimension 4 in char p"? In particular: is "regular" with density and an isomorphism over the regular locus the right weak form over an imperfect field?
2. Which of the routes of 04 do you think has a chance, and is the key obstruction stated correctly?
3. Is the reading of Abhyankar's hypothesis $p > 5$ in 04.12 correct? Is there a known obstruction to a theorem of the form "4-folds for $p > N$"?
4. Which published results in your area have known gaps, or are not accepted? (This sets `expert_status` in the paper records, 07.11.)
5. What is the exact one-step bound of Moh (1987) that survives the cycles of Hauser-Perlega?
6. Is patching (Zariski's step 2) in dimension 4 a separate open problem in your view, or does it follow from a strong enough local uniformization?
