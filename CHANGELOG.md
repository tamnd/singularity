# Changelog

Each release has a section. The newest release is first.

## Unreleased

### Changed

- The records are pinned at tamnd/singularity-lean 2ab04e5, the merge commit of tamnd/singularity-lean#128, with 1917 declarations.
- SG00000051 has the Lean statement and proof `Singularity.tauRhoDropExample_codim`. Its notes give the other Lean names and a second example with four variables.

## 0.4.26 - 2026-11-26

### Added

- SG00000051, an example over $\mathbb{F}_2$ in five variables where the codimension of the directrix of the log-Jacobian order goes down from the first case to the first case, since $|r| + d$ is $0$ in the base field.

### Changed

- The notes of SG00000050 refer to SG00000051 for the case where $|r| + d$ is $0$ in the base field.

## 0.4.25 - 2026-11-26

### Changed

- The records now pin the Lean library at a01c6b0, with the codimension of the directrix of the log-Jacobian order from the first case to the first case.
- SG00000050 has the Lean statement and proof `logJacobianDirectrixCodim_le_cleanPart_of_caseA` of tamnd/singularity-lean#126.

## 0.4.24 - 2026-11-26

### Added

- SG00000050, the codimension of the directrix of the log-Jacobian order does not go down from the first case to the first case if $|r| + \operatorname{ord} G$ is not $0$ in the base field, with the example for $p = 2$ where the plain transport fails, for the milestone S7.10 (#193).

### Changed

- The notes of SG0000004Z refer to SG00000050 for the case from the first case to the first case.

## 0.4.23 - 2026-11-25

### Changed

- The records now pin the Lean library at df659d4, with the unramified part of Step 4 of the reduction of Cossart-Piltant and the codimension of the directrix of the log-Jacobian order.
- SG0000004Z has the Lean statement and proof `logJacobianDirectrixCodim_le_cleanPart` of tamnd/singularity-lean#122.
- Note the unramified part of Step 4 of Cossart-Piltant (tamnd/singularity-lean#124) on SG0000001F.
- The records now pin the Lean library at 1db66bb, with the induction on the degree in the reduction of Cossart-Piltant.
- The notes of SG0000001F give the steps of degree p of tamnd/singularity-lean#105 and the induction on the degree of tamnd/singularity-lean#123, with the step of degree p as a hypothesis.
- The records now pin the Lean library at 569368b, with local uniformization over a monomial subfield in the case of one extension.
- The notes of SG0000001E give the case of the theorem of Knaf-Kuhlmann without ramification, defect and splitting from tamnd/singularity-lean#121.

## 0.4.22 - 2026-11-25

### Added

- SG0000004Z, the codimension of the directrix of the log-Jacobian order does not go down at a point where $\rho$ stays and the new point is in the second case, with the counterexample for $p = 2$ in the first case, for the milestone S7.9 (#173).

### Changed

- The records now pin the Lean library at 3d28b00, with the points where the log-Jacobian order stays.
- SG0000004X, the points where the log-Jacobian order stays lie in a directrix, has the Lean statement and proof Singularity.chartVector_mem_directrix_of_logJacobianOrder_eq of tamnd/singularity-lean#119. The notes give the Lean names of the second case, the corollaries and the example.
- The records now pin the Lean library at b7487dc, with the existence of an étale generator in the case of one extension.
- The notes of SG0000004Y give the case of one extension from tamnd/singularity-lean#118.
- The records now pin the Lean library at 8e6b1dc, with the lifting theorem along an étale generator.
- SG0000004C, the lifting of local uniformization along an étale generator, has the Lean statement and proof Singularity.hasLocalUniformization_of_etaleGenerator of tamnd/singularity-lean#116. The existence of an étale generator is the new node SG0000004Y, with no Lean statement.

## 0.4.21 - 2026-11-25

### Changed

- The records now pin the Lean library at 70659f8, with the finite chain criterion of MacLane-Vaquié.
- The notes of SG0000000Z give the criterion for a finite chain in part 4 of MacLane-Vaquié from tamnd/singularity-lean#115.
- The records now pin the Lean library at 656c128, with 1747 declarations and no nonstandard axioms.

## 0.4.20 - 2026-11-25

### Changed

- The notes of SG0000004D and SG0000004F now give the Lean proofs of tamnd/singularity-lean#113: Lemma 2.1.2, Corollary 2.1.6 in the form over $k$, and each claim of the reduction to a larger ground field but the last one.
- The records now come from tamnd/singularity-lean at 07c64a4, with 1718 declarations and no nonstandard axioms.
- SG0000004D, local uniformization of monomial valuations, now has the Lean proof Singularity.hasLocalUniformization_of_isMonomialValuation of tamnd/singularity-lean#111, for value groups of each rank.
- SG0000001R now has a note that says that the Lean name of the statement is planned, after the referee report on Volume 0 of the handbook.

### Added

- SG0000004X, the points where the log-Jacobian order stays lie in a directrix, the analogue for $\rho$ of SG0000003B, for the milestone S7.8 (#164).

## 0.4.19 - 2026-11-25

### Changed

- The records now come from tamnd/singularity-lean at d17dcd2, with 1688 declarations and no nonstandard axioms.
- The note of SG0000004D now gives the Lean proof of local uniformization for monomial valuations of rank 1 (tamnd/singularity-lean#110).

## 0.4.18 - 2026-11-25

### Changed

- The note of SG0000000Z now says that part 4 of MacLane-Vaquié has a Lean proof for each valuation with nonzero support and any value group, and gives the weak form for each valuation (tamnd/singularity-lean#109).
- SG0000004S now has the Lean field `Singularity.logJacobianOrder_eq_zero_iff`, the end case for polynomials, by tamnd/singularity-lean#100. This entry was in the section of 0.4.16 by mistake.
- SG0000004T now has the Lean field `Singularity.cpOmega_eq_logJacobianOrder`, the equality of omega and the log-Jacobian order for polynomials, by tamnd/singularity-lean#107.

## 0.4.17 - 2026-11-25

### Changed

- Referee notes from Volume 1 of the handbook. The nodes SG0000000P, SG0000000N, SG0000000C, SG0000001V and SG00000010 now have a note that says that the Lean name of the statement is planned. SG00000023 now says the theorem of Auslander-Buchsbaum.

## 0.4.16 - 2026-11-25

### Added

- SG0000004W, the definition of an alteration, with the Lean definition Singularity.IsAlteration of tamnd/singularity-lean#104.
- SG0000004V, the lemma of Tschirnhausen for a unit $m$, with the Lean proof of tamnd/singularity-lean#98 (#146).
- SG0000004T, the log-Jacobian order is the invariant omega of Cossart-Piltant for $Z^p + f$ over a perfect field. So omega does not depend on the coordinates, and it does not go up under a point blowup or under the blowup of a regular center with (H1) and (H2), in each dimension and without condition (E). It connects the routes R1 and R5, in #144.
- SG0000004S, the end case of the log-Jacobian ideal: $\rho = 0$ if and only if the equation is of type 0 or of type 1, and then $z^p + g$ is a binomial equation after a change of the coordinates. It is the next step on route R1 for S7, in #142.

### Changed

- Referee fixes from Volume 9 of the handbook. SG00000019 now has the statement of [BBE25, Corollary 3.7]: for an excellent local ring $R$, the Samuel slope is infinite if and only if $R_{\mathrm{red}}$ is regular. The old statement for each Noetherian local ring was false. The papers Kol20, BMP20 and KR23 now have the right year. Kol20 now names its two papers. The why of Wlo22 now says characteristic 0, and the why of AS22 now says what the paper proves.
- The records now come from tamnd/singularity-lean at 01471ae, with 1580 declarations and no nonstandard axioms.
- Referee fixes from Volume 3 of the handbook. The note of SG0000000Z now gives four Lean names with the namespace ContinuousFamily, it says that the limit augmentations add nothing when the values of ν are discrete of rank 1, and it does not repeat a sentence.
- SG0000001K now has the Lean statement Singularity.deJongAlteration, a Prop with no proof. The note says how it is weaker than [dJ96, 4.1].
- The note of SG0000000Z now says that part 4 of MacLane-Vaquié is complete in Lean for a discrete valuation of rank 1 (tamnd/singularity-lean#101).
- The note of SG0000000Z now says that the limit key polynomial is a key polynomial for the limit augmentation, by tamnd/singularity-lean#99 (#146).

## 0.4.15 - 2026-11-25

### Changed

- SG0000004Q and SG0000004R now have Lean fields. The Lean library proves the non-increase of the residual order under the blowup in a regular center with (H1) and (H2), and the counterexample over the field with two elements (tamnd/singularity-lean#96).
- The Lean records are now at tamnd/singularity-lean@103e07f, with 1459 declarations and no axioms outside the standard three. The last refresh was at 93c16b9, with 1163 declarations.

## 0.4.14 - 2026-11-25

### Added

- Experiment E4 of the lab: the specs `lab/specs/e4-p2.yaml`, `e4-p3.yaml` and `e4-p5.yaml` and their runs in `lab/runs/`. They compute the invariants delta, epsilon, omega and iota of Cossart-Piltant [CP19] on the walks of E1 with q = p, for n = 3 and n = 4, with tamnd/singularity-agent#9. `lab/README.md` and the page `/lab/` describe E4.

### Changed

- The note of SG00000041 no longer calls the theorem the second main theorem of [Hir64]. The note of SG00000049 says that the induction needs the functorial form, which Volume 2 cites from [Kol07].
- SG0000004P now has a Lean field. The Lean library proves the transformation law of the log-Jacobian ideal for the blowup in a regular center, for polynomials, as two inclusions, and the lemma on the equimultiple weak transform (tamnd/singularity-lean#95).

## 0.4.13 - 2026-11-25

### Changed

- SG0000003N now has a Lean field. The Lean library proves that the residual order of the log-Jacobian ideal does not go up under a point blowup, for polynomials, and the corollary $d' \le d + 1$ (tamnd/singularity-lean#93).

## 0.4.12 - 2026-11-25

### Added

- The nodes SG0000004P to SG0000004R are new, for Volume 7, Section 3.4 of the handbook. SG0000004P is the transformation law of the log-Jacobian ideal for the blowup in a regular center of positive dimension, with the lemma on the weak transform of an equimultiple ideal. SG0000004Q is the non-increase of the residual order under the conditions (H1) and (H2). SG0000004R is the counterexample that shows that (H1) alone is not sufficient (#130).

## 0.4.11 - 2026-11-25

### Added

- The nodes SG0000004M and SG0000004N are new. SG0000004M is the order at a point by the Hasse-Schmidt derivatives, Volume 7, Proposition 1.1.4 of the handbook. SG0000004N is the test for q-th powers in characteristic p by the Hasse-Schmidt derivatives. Their Lean fields name the theorems of tamnd/singularity-lean#91.

### Changed

- SG0000000W now names Singularity.Algebra.MvHasse.hasseDeriv. The old name Singularity.HasseDeriv did not exist. The notes give the Leibniz rule, the composition rule and the Taylor formula (tamnd/singularity-lean#91).
- SG0000003M now has a Lean field. The Lean library proves the transformation law of the log-Jacobian ideal for polynomials, as two inclusions (tamnd/singularity-lean#90).
- The paper record Cut20 now gives the title, the journal, the volume, the pages and the DOI. The year was 2003, from the number of the preprint, and is now 2022. SG0000001E now cites [Cut20], which removes the condition of separability on the residue field.

## 0.4.10 - 2026-11-25

### Added

- The nodes SG0000003E to SG0000003N are new, for Volume 7, Chapters 3 and 4 of the handbook. SG0000003E is the log-Jacobian ideal and its invariance under the addition of a p-th power, SG0000003F is the dichotomy d - 1 <= rho <= d for a clean F, SG0000003G is the Newton criterion for z^p + g, SG0000003H is the mod p Euler identity, SG0000003J is the rigid layer of a multiplicity divisible by p, and SG0000003K is the lifting test for z^q + g. Their Lean fields name the theorems of tamnd/singularity-lean#85, tamnd/singularity-lean#86 and tamnd/singularity-lean#87. SG0000003M is the transformation law of the ideal under a point blowup, and SG0000003N says that rho does not go up. These two nodes have no Lean proof yet.
- The nodes SG00000040 to SG0000004K are new, for the main results of Volumes 2, 5 and 8 of the handbook. SG00000040 to SG00000049 are the resolution theorems in characteristic 0 and the steps of their proof after [Kol07], with maximal contact, the restriction theorem, the coefficient ideal and order reduction. SG0000004A to SG0000004F are the results on local uniformization in Volume 5, with the theorem of Abhyankar on quadratic sequences, the lifting along an étale generator and the monomial valuations. SG0000004G to SG0000004K are the results on curves and moduli in Volume 8 that the proof of de Jong uses. No new node has a Lean name.
- SG0000001E now uses SG0000004C and SG0000004D, and SG0000001K now uses SG0000004J.

## 0.4.9 - 2026-11-25

### Changed

- The handbook page of the site points to the edition 0.4.9, which has all ten volumes. The new rows are Volumes 2, 5 and 8.
- The statement of SG0000001G now takes the finite set first, so that the purely inseparable extension depends on it, as in [Tem13] and in the Lean statement.
- The new note of SG0000001N says that the theorem of Temkin holds over any field, and that the alteration is not proved to be Galois.
- The note of SG0000000Z gives the limit augmentation of Vaquié from tamnd/singularity-lean#84.
- The note of SG00000014 gives the case f = z^q + F with F clean, where the polyhedron is (1/q) times the Newton polyhedron of F (tamnd/singularity-lean#83).

### Added

- The paper Knu83 is new, for Volume 8 of the handbook. It is the paper of Knudsen on the stacks of stable pointed curves, which de Jong uses for his alterations [dJ96, 2.24]. The record gives the journal, the volume, the pages and the DOI.

## 0.4.8 - 2026-11-25

### Changed

- The records are now at tamnd/singularity-lean@93c16b9, with 1163 declarations. They now have the Lean names of tamnd/singularity-lean#78, #80 and #81. The trust record has no nonstandard axiom.
- The note of SG0000000Z gives the claim of part 3 in the form of μ-equivalence and the uniqueness of the key polynomial in the step (tamnd/singularity-lean#80).
- The note of SG0000001E tells that the divisorial case and the case trdeg K/k at most trdeg of the residue field plus one are proved (tamnd/singularity-lean#81). The note also tells why this method does not work for rational rank 2 or more.

## 0.4.7 - 2026-11-25

### Added

- The papers CP15, Abh59, Cos92, Hir67b, Moh96 and Moh14 are new, for Volume 6 of the handbook. CP15 is the paper of Cossart-Piltant on characteristic polyhedra without completion. Abh59 is the book of Abhyankar on ramification theory, which [CP19, Section 4.2] uses. Cos92 is the paper of Cossart that gives Step 5 of the proof of Cutkosky for threefolds. Hir67b is the Bowdoin lectures of Hironaka on excellent surfaces. Moh96 and Moh14 are two papers of Moh that [CP19] cites. Each record gives the journal, the volume, the pages and the DOI when there is one. The book of Cutkosky already has the record Cut04.

### Changed

- `site/handbook.md` links to edition 0.4.7 of the handbook, which adds Volume 6 on threefolds.
- `records/lean.json` has the record of tamnd/singularity-lean at commit 16a5c93, with 1079 declarations. The new proofs are the characteristic polyhedron (tamnd/singularity-lean#76) and the chain of MacLane (tamnd/singularity-lean#77).
- SG00000015 now has a Lean proof, `Singularity.moh_bound_holds` (tamnd/singularity-lean#78), for point blowups. The note no longer says that the statement may need a hypothesis on the coordinates. The route report gives the new status of R5 and the next targets.
- The note of SG0000000Z gives the chain of MacLane and part 4 of the theorem of MacLane-Vaquié for a valuation with discrete values (tamnd/singularity-lean#77). It also says that a nonzero support alone does not make the chain finite.
- A review of Volumes 1 and 4 of the handbook found four nodes that did not agree with the library. SG0000002H and SG0000000Q said that a result is not in Lean, but SG0000002M and SG00000032 prove it. SG00000034 did not give the condition $d \ge \max(r, s)$ of the monotony law. The note of SG0000001C did not give the condition on the open $U$ correctly.
- SG00000014 now names the Lean definition that exists, `Singularity.charPolyhedron` (tamnd/singularity-lean#76). The earlier name `Singularity.characteristicPolyhedron` did not exist. A note gives what the library proves about the polyhedron and what it does not prove.
- The new site page `site/route-report.md` is the route report of milestone S7. For each route R1 to R9 it gives the idea, the nodes with their Lean status, the literature, the negative results and the smallest next node in Lean, and it ranks the routes by the next feasible step. The routes page links to it.
- `records/lean.json` has the record of tamnd/singularity-lean at commit 80e2938, with 998 declarations. The new proof is the step of part 4 of the theorem of MacLane-Vaquié (tamnd/singularity-lean#75).
- The note of SG0000000Z gives the Lean proof of the step.
- SG0000001P now names the Lean statement and proof that exist (`Singularity.ResolutionInDim` and `Singularity.resolutionInDim_charZero`). The earlier name `Singularity.Base.hironaka` did not exist. The statement no longer says "a sequence of blowups", because the Lean form gives one proper birational morphism.
- The statement of SG0000001J is now for characteristic p and transcendence degree at most 4, as the Lean statement and Conjecture 2.3.2 of Volume 9 of the handbook.

## 0.4.6 - 2026-11-24

### Changed

- `records/lean.json` has the record of tamnd/singularity-lean at commit e66b7a2, with 987 declarations. The new proofs are the first claim of part 3 of the theorem of MacLane-Vaquié (tamnd/singularity-lean#72) and local uniformization in transcendence degree at most 1 (tamnd/singularity-lean#73).
- The notes of SG0000000Z and SG0000001F give the new Lean proofs.
- `site/handbook.md` links to edition 0.4.6 of the handbook.

## 0.4.5 - 2026-11-24

- The handbook page links to the handbook edition 0.4.5. Volume 3 of this edition proves parts 1 and 2 of the theorem of MacLane-Vaquié and gives the Lean statements of local uniformization.
- The nodes SG0000001E, SG0000001F, SG0000001G, SG0000001H and SG0000001J have notes on the Lean statements of local uniformization of tamnd/singularity-lean#69 and tamnd/singularity-lean#70.
- records/lean.json records the Lean build at commit dbde226, with 974 declarations.
- The node SG0000000Z has notes on the Lean proof of parts 1 and 2 of the theorem of MacLane-Vaquié, from tamnd/singularity-lean#68.
- records/lean.json records the Lean build at commit 06a7ed6, with 972 declarations. The build has the statements of local uniformization of tamnd/singularity-lean#69.
## 0.4.4 - 2026-11-24

- The handbook page links to the handbook edition 0.4.4. Volume 3 of this edition gives the Lean definitions of the key polynomials.
- The node SG0000000Z (key polynomials) has notes on the Lean definitions of tamnd/singularity-lean#66: the key polynomials, the monomial valuation and the augmented valuation as a function.
- records/lean.json records the Lean build at commit 0ce0f4d, with 926 declarations.
- The handbook page links to the handbook edition 0.4.3. Volume 3 of this edition gives the Lean proofs of the Zariski-Riemann theorem and the Abhyankar inequality.

## 0.4.3 - 2026-11-24

- The node SG0000000X (the Zariski-Riemann space is quasi-compact) has the Lean proof Singularity.ZariskiRiemann.compactSpace of tamnd/singularity-lean#64.
- records/lean.json records the Lean build at commit 315082e, with 858 declarations.
- The node SG0000000Y (the Abhyankar inequality) has the Lean proof Singularity.abhyankar_inequality of tamnd/singularity-lean#63. Its notes name the relative form.
- records/lean.json records the Lean build at commit 3826806, with 836 declarations.
- The handbook page links to the handbook edition 0.4.2. Volume 4 of this edition gives the Lean statement of embedded resolution.

## 0.4.2 - 2026-11-24

- The node SG0000001C (embedded resolution of surfaces) has the Lean statement Singularity.EmbeddedResolutionSurface of tamnd/singularity-lean#61. The statement is weaker than the theorem of [CJS20], and it is not proved. The notes of the node give the differences.
- The nodes SG0000000T (permissible center) and SG0000000V (simple normal crossings) have the Lean definitions Singularity.IsPermissible and Singularity.IsSncDivisor of tamnd/singularity-lean#61. Their notes give the Lean results on them.
- records/lean.json records the Lean build at commit 23305f9, with 825 declarations.

## 0.4.1 - 2026-11-24

- The papers Vaq07, Kuh10, Kuh10b and Zar44b are new, for Volume 3 of the handbook. The record Mac36 names only the paper of MacLane, because Vaq07 now has its own record.
- The note of the trust check Q3 gives the result of lean4lean on each module of Singularity at commit ce778c3, run on a project server. It accepted the 43 modules.
- The handbook page lists the six volumes of the handbook edition 0.4.1, with links to the PDF and EPUB files of the release. Volume 3, Valuations, is new in this edition.

## 0.4.0 - 2026-11-24

- The handbook page lists the five volumes of the handbook edition 0.4.0, with links to the PDF and EPUB files of the release. Volume 7 of this edition reports the runs of the lab.
- The lab: `lab/README.md`, the specs of the experiments E1 and E2 in `lab/specs/` and their runs in `lab/runs/`, made with `sing lab` of tamnd/singularity-agent. The runs `e1-p2`, `e1-p3`, `e1-p5`, `e1-p7` and the runs `e2-p2`, `e2-p3`, `e2-p5`, `e2-p7` cover p = 2, 3, 5, 7, n = 2, 3, 4 and q = p, p^2. The runs `e1-hp-section3` and `e1-hp-cycle-p2` compute the examples of Hauser and Perlega (arXiv:1802.05010, sections 3 and 4) again. The page `site/lab.md` is the text of the page /lab/ of the site.
- With this release the milestone S3 is complete.

## 0.3.2 - 2026-11-24

- The node SG0000003D (the blowup of a regular curve on a regular surface is an isomorphism) is new. It is proved by Singularity.Algebra.bijective_algebraMap_idealBlowupChart_of_isRegularLocalRing_quotient of tamnd/singularity-lean#57.
- records/lean.json records the Lean build at commit ad6063d, with 778 declarations.

## 0.3.1 - 2026-11-24

- The node SG0000003B (the points of the same order lie in the directrix) has the Lean statement and proof Singularity.mem_directrix_of_ord_pointChart_eq of tamnd/singularity-lean#55.
- records/lean.json records the Lean build at commit bc7fa0d, with 768 declarations.
- The handbook page lists the five volumes of the handbook edition 0.3.2, with links to the PDF and EPUB files of the release.

## 0.3.0 - 2026-11-24

- The node SG0000003A (the order does not go up under a point blowup) is proved by Singularity.ord_le_of_pointChart in tamnd/singularity-lean#52. The node SG0000003B (the points of the same order lie in the directrix) is new, with no Lean proof.
- The node SG0000003C (a chart of the blowup of a regular local ring is regular) is proved by Singularity.Algebra.isRegularRing_blowupChart in tamnd/singularity-lean#53.
- records/lean.json records the Lean build at commit ce778c3, with 745 declarations.
- The trust checks Q3 and Q4 have the state "yes". The note of Q3 gives the results of leanchecker, nanoda and the bundled checkers, and it says that the job of lean4lean on each module gave no result on the hosted runner. The note of Q4 says that the comparator of the base package runs without the sandbox.
- With this release the milestone S2 is complete.

## 0.2.14 - 2026-11-24

- The node SG00000016 (a kangaroo point) is proved by Singularity.Examples.kangaroo in tamnd/singularity-lean#45. The nodes SG00000011 and SG00000013 have notes on their Lean definitions, and SG00000015 has the exact statement of the bound of Moh, which Lean states and does not prove.
- The node SG0000000K (the regular locus is open) now states the result over an arbitrary field, which can be imperfect. Its Lean proof is Singularity.regularLocus_isOpen_of_field in tamnd/singularity-lean#47. The new node SG00000038 is the flat descent of regularity, with the proof Singularity.Algebra.isRegularLocalRing_of_flat.
- The node SG0000001J (patching in dimension 4) has the kind conjecture, because it is open.
- The nodes SG0000001B and SG0000001D named Lean proofs that do not exist. They now have only the Lean statement. The status check showed them as stated before, so no status changes.
- The new node SG00000039 is one cycle of the first example of Hauser and Perlega, certified by Singularity.Examples.hauserPerlegaCycle in tamnd/singularity-lean#49. The node SG00000017 now states the full theorem of [HP19a], with the residual order that tends to infinity. Its Lean statement is planned, because the Lean proof covers only one cycle.
- The node SG00000018 (the example of Narasimhan) is proved by Singularity.Examples.narasimhan in tamnd/singularity-lean#50. Its statement now gives the equation and the curve.
- The Lean records are at commit c51aa70 of tamnd/singularity-lean, with 688 declarations. The commit has the declarations of the release v0.2.15, which changes only the changelog. The nodes SG0000000K, SG00000038, SG00000039, SG00000018 and SG00000016 are proved.
- The releases v0.2.14 and v0.2.15 of tamnd/singularity-lean.
- The node SG0000000K does not use SG00000030 (excellent rings), because its Lean proof does not use excellent rings. Before this change, its status was proved-mod.

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
