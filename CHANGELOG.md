# Changelog

Each release has a section. The newest release is first.

## Unreleased

- The node SG00000016 (a kangaroo point) is proved by Singularity.Examples.kangaroo in tamnd/singularity-lean#45. The nodes SG00000011 and SG00000013 have notes on their Lean definitions, and SG00000015 has the exact statement of the bound of Moh, which Lean states and does not prove.
- The node SG0000000K (the regular locus is open) now states the result over an arbitrary field, which can be imperfect. Its Lean proof is Singularity.regularLocus_isOpen_of_field in tamnd/singularity-lean#47. The new node SG00000038 is the flat descent of regularity, with the proof Singularity.Algebra.isRegularLocalRing_of_flat.
- The node SG0000001J (patching in dimension 4) has the kind conjecture, because it is open.
- The nodes SG0000001B and SG0000001D named Lean proofs that do not exist. They now have only the Lean statement. The status check showed them as stated before, so no status changes.
- The new node SG00000039 is one cycle of the first example of Hauser and Perlega, certified by Singularity.Examples.hauserPerlegaCycle in tamnd/singularity-lean#49. The node SG00000017 now states the full theorem of [HP19a], with the residual order that tends to infinity. Its Lean statement is planned, because the Lean proof covers only one cycle.

## 0.2.13 - 2026-11-24

- The Lean records are at commit 82bb73d of tamnd/singularity-lean, with 368 declarations. The node SG00000037 is proved.
- The release v0.2.13 of tamnd/singularity-lean.
- The node SG00000037 (a regular local ring has multiplicity one), with its Lean proof in tamnd/singularity-lean#42. The note of SG00000034 now refers to it.

## 0.2.12 - 2026-11-24

- The Lean records are at commit 4baa010 of tamnd/singularity-lean, with 349 declarations. The nodes SG00000035 and SG00000036 are proved.
- The release v0.2.12 of tamnd/singularity-lean.
- The nodes SG00000035 (generic regularity over a perfect field) and SG00000036 (the regular locus is open over a perfect field), each with its Lean proof in tamnd/singularity-lean. The node SG0000000K now uses SG00000036. SG0000000K stays planned, because the case of an imperfect field is not proved.

## 0.2.11 - 2026-11-24

- The Lean records are at commit bb9fc55 of tamnd/singularity-lean, with 341 declarations. The nodes SG00000031, SG00000032 and SG00000034 are proved, and SG00000033 is defined.
- The release v0.2.11 of tamnd/singularity-lean.
- The nodes SG00000031 (the theorem of Hilbert and Serre), SG00000032 (the Hilbert-Samuel polynomial), SG00000033 (the Samuel multiplicity) and SG00000034 (the laws of the multiplicity), each with its Lean declaration in tamnd/singularity-lean#38.

- The nodes SG0000002W (effective Cartier divisors), SG0000002X (Zariski's Main Theorem) and SG0000002Y (the dimension of a variety). With these nodes, each row of tier T1 in the corpus has a node on the map.
- The nodes SG0000002Z (a local ring is regular if and only if its completion is regular) and SG00000030 (excellent rings), for Chapters 4 and 5 of Volume 1 of the handbook. The node SG0000000K now uses SG00000030.

## 0.2.10 - 2026-11-24

- The node SG0000002V (the regular locus of a scheme is open in characteristic zero), with its Lean proof `Singularity.regularLocus_isOpen_of_charZero`. The node SG0000000K now uses SG0000002V. SG0000000K stays planned, because the case of positive characteristic is not proved.
- The Lean records are at commit b939ac7 of tamnd/singularity-lean, with 231 declarations.
- The release v0.2.10 of tamnd/singularity-lean.

## 0.2.9 - 2026-11-24

- The nodes SG0000002R (the Jacobian criterion for a hypersurface over a regular ring), SG0000002S (generic regularity in characteristic zero) and SG0000002T (the regular locus is open in characteristic zero), each with its Lean proof in tamnd/singularity-lean.
- The node SG0000000K (the regular locus is open) now uses SG0000002T, and SG0000000G (the Jacobian criterion) now uses SG0000002R. SG0000000K stays planned, because the scheme statement and the case of positive characteristic are not proved.
- The Lean records are at commit 4213622 of tamnd/singularity-lean, with 229 declarations.
- The release v0.2.9 of tamnd/singularity-lean.

## 0.2.8 - 2026-11-24

- The nodes SG0000002N (the regular locus is stable under generization), SG0000002P (a regular system of parameters spreads to a neighbourhood) and SG0000002Q (the criterion of Nagata), each with its Lean proof in `Singularity/Algebra/RegularLocus.lean`.
- The node SG0000000K (the regular locus is open) now uses SG0000002Q. It stays planned, because it also needs a nonempty open regular locus for each domain of finite type over a field.
- The Lean records are at commit 9cf5ebe of tamnd/singularity-lean, with 215 declarations.
- The release v0.2.8 of tamnd/singularity-lean.

## 0.2.7 - 2026-11-24

- The node SG0000002M (the converse of the theorem of Serre) with its Lean proof `Singularity.Algebra.isRegularLocalRing_of_hasProjectiveDimensionLT`. A Noetherian local ring whose residue field has finite projective dimension is regular.
- The node SG0000000H (localizations of a regular local ring) is now proved, with the Lean proof `Singularity.Algebra.isRegularLocalRing_localization`. It uses SG0000002M. Its Lean name was a placeholder before this change.
- `records/lean.json` and `records/base-charzero.json` from tamnd/singularity-lean at a1e5c55, with the files `Singularity/Algebra/SerreConverse.lean` and `Singularity/Algebra/RegularLocalization.lean`. The record has 200 declarations, and each uses only the three standard axioms.
- The release v0.2.7 of tamnd/singularity-lean.

## 0.2.6 - 2026-11-24

- The nodes SG0000002G (the maximal ideal of a regular local ring is generated by a regular sequence) and SG0000002H (the residue field of a regular local ring has projective dimension equal to the dimension), with their Lean proofs in `Singularity/Algebra/RegularSequence.lean`. SG0000002H is the first half of the theorem of Serre. The node SG0000000H (localizations of a regular local ring) now uses SG0000002H. Its proof needs the converse half, which is not in Lean yet.
- `records/lean.json` and `records/base-charzero.json` from tamnd/singularity-lean at 1bde104, with the files `Singularity/Algebra/HilbertSamuel.lean` and `Singularity/Algebra/RegularSequence.lean`. The record has 175 declarations, and each uses only the three standard axioms.
- The node SG0000000Q (the Hilbert-Samuel function) now has the Lean definition `Singularity.Algebra.hilbertSamuel`, the function $n \mapsto \ell(M/I^n M)$. Before this change its Lean name was a placeholder that did not exist. The statement says that the Samuel multiplicity needs the theorem of Hilbert and Samuel, which is not in Lean yet.
- The nodes SG0000002D (the laws of the Hilbert-Samuel function, with finiteness), SG0000002E (the order of an element) and SG0000002F (the laws of the order, with the intersection theorem of Krull). The node SG00000013 (order and residual order) now uses SG0000002E.
- The release v0.2.6 of tamnd/singularity-lean.

## 0.2.5 - 2026-11-24

- The node SG0000001Y (the reduction to integral varieties) is now a theorem with the Lean proof `Singularity.Reduction.reductionToIntegral`. It was a named hypothesis. The source is the Stacks project.
- The node SG0000000D (characteristic 0) now has the Lean proof `Singularity.resolutionInDim_charZero`, which takes no hypothesis. Its status changes from proved-mod to proved.
- The node SG0000001A (curves) now has the Lean proof `Singularity.Curves.resolutionInDim_one`. Its status changes from stated to proved.
- `records/lean.json` and `records/base-charzero.json` from tamnd/singularity-lean at ad0770f, with the files `Singularity/Scheme/Components.lean` and `Singularity/Scheme/Reduction.lean`. The record has 148 declarations, and each uses only the three standard axioms.
- Trust check Q6 now records that no published theorem is still a hypothesis.
- The release v0.2.5 of tamnd/singularity-lean.

## 0.2.4 - 2026-11-24

- The node SG0000002B (the normal locus of a domain with a finite normalization) with its Lean proof.
- The node SG0000002C (integral curves have a resolution in each characteristic) with its Lean proof `Singularity.Curves.integralResolutionInDim_one`. The resolution is the normalization. The node SG0000001A uses SG0000002C and SG0000001Y. Its status stays stated, because the general case needs the reduction to integral varieties.
- `records/lean.json` from tamnd/singularity-lean at 4ab4320, with the files `Singularity/Algebra/NormalLocus.lean` and `Singularity/Curves/Resolution.lean`. It has 109 declarations, and each uses only the three standard axioms.
- The release v0.2.4 of tamnd/singularity-lean.

## 0.2.3 - 2026-11-24

- The papers Eis95 (Eisenbud, Commutative Algebra with a View Toward Algebraic Geometry) and Lan02 (Lang, Algebra).
- The nodes SG00000028 (the integral closure of a polynomial ring in a purely inseparable extension is finite), SG00000029 (the integral closure of a polynomial ring in each finite extension is finite) and SG0000002A (the normalization of an affine curve over each field is a Dedekind domain), each with its Lean proof.
- The node SG0000000M (finiteness of normalization, the theorem of E. Noether) now has a precise statement and its Lean proof `Singularity.Algebra.finite_integralClosure`. Before this change its Lean name was a placeholder that did not exist.
- `records/lean.json` from tamnd/singularity-lean at 1ef1ad1, with the file `Singularity/Algebra/NormalizationCharP.lean`. It has 92 declarations, and each uses only the three standard axioms.
- The release v0.2.3 of tamnd/singularity-lean.

## 0.2.2 - 2026-11-24

- The nodes SG00000024 (normal schemes of dimension at most 1 are regular), SG00000025 (finiteness of the integral closure in the separable case) and SG00000026 (finiteness of normalization in characteristic 0), each with its Lean proof. The node SG0000000M uses SG00000025, and the node SG0000001A uses SG00000024.
- `records/lean.json` from tamnd/singularity-lean at 756fa03, with the files `Singularity/Algebra/Normalization.lean` and `Singularity/Scheme/NormalDimOne.lean`. It has 74 declarations, and each uses only the three standard axioms.
- The node SG00000027, the normalization of an affine curve in characteristic 0 is a Dedekind domain, with its Lean proof.
- `records/lean.json` from tamnd/singularity-lean at 0cb57d5, with the file `Singularity/Curves/Affine.lean`. It has 76 declarations.
- The release v0.2.2 of tamnd/singularity-lean.

## 0.2.1 - 2026-11-24

- The nodes SG00000021 (the quotient of a regular local ring by a parameter), SG00000022 (regular local rings of dimension 1) and SG00000023 (a regular local ring is a unique factorization domain, planned). The node SG0000000J has its Lean proof, and its statement is now the domain part only. The node SG0000001A uses SG00000022.
- `records/lean.json` from tamnd/singularity-lean at 0df69ef, with the file `Singularity/Algebra/Regular.lean`. It has 69 declarations.
- `records/trust.json`: the replay with leanchecker passes on both packages. Q3 stays open, because the replay uses the same kernel.
- The release v0.2.1 of tamnd/singularity-lean, with `Singularity/Algebra/Regular.lean`.

## 0.2.0 - 2026-11-23

- The nodes SG0000001Y (the reduction to integral varieties, a named hypothesis), SG0000001Z (integral varieties in characteristic 0) and SG00000020 (Hironaka's theorem in the form of formal-conjectures). The nodes SG0000000D and SG0000000E have their Lean proofs.
- `records/lean.json` from tamnd/singularity-lean at 453191c, with the declarations of the base package. `records/base-charzero.json` is the record of the base package alone.
- `records/trust.json`, the first trust report. Q1, Q2 and Q6 are yes. Q3 and Q4 are not run yet.
- The paper records AM69, FC, HirLean and Mathlib, for the citations of the handbook.
- The release v0.2.0 of tamnd/singularity-lean, with the workflow `trust` for the replay of both packages.

## 0.1.0 - 2026-11-23

- The spec, documents 00 to 16.
- The style check `scripts/style.py`.
- The workflows: lint, scorecard and dependency updates.
- The first map: the blueprint nodes, the routes and the paper records for the corpus.
- The site pages `/problem/`, `/map/`, `/trust/` and `/papers/`, and the deploy of https://singularity.tamnd.com to Cloudflare from the main branch.
- The Lean names of the fidelity nodes, the node SG0000001W for dimension 0 and the node SG0000001X for the fidelity of P1.
- `records/lean.json`, the record of the Lean build. The map takes the status of each node from this record.
