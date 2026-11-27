# Changelog

Each release has a section. The newest release is first.

## Unreleased

### Added

- SG00000090 to SG00000096 for the corner runs in four variables with $\deg_{x, w} g \ge p$, in Volume 7, Section 3.18 of the handbook. The nodes are the results of research note 64 that the referee report in note 67 marks safe, in the form that note 67 corrected. SG00000090 and SG00000091 are Theorem 3.1 and Corollary 3.2 of note 64: on a planar run each nonzero $f \in \hat H[X, W]$ of any degree has $f(\Phi_\infty) \ne 0$, so Conjecture T holds for the planar runs, and the dominant part of $f$ is additive. SG00000092 is Theorem 5.3 of note 64: there is no planar corner run under the condition (C), which contains each $g$ with $\deg_{x, w} g \le p$. SG00000093 is Corollary 5.5 of note 64: each corner run with $\deg_{x, w} g \le p$, under (C), or in $K[[y, z]][x^p, w^p]$ is linear and satisfies Conjecture L. SG00000094 and SG00000095 are Theorem 6.1 and Corollary 6.2 of note 64: for $g \in K[[y, z]][x^p, w^p]$ the run is linear, the initial form is a power of a line, and L° holds, and for $g = B_1 x^p + B_2 w^p + B_0$ this is true for each rank. SG00000096 is Conjecture P of note 64, that there is no planar corner run. It is open. None of the new nodes has a Lean proof.

### Changed

- The notes of SG0000006Z, SG00000075 and SG00000071, Conjectures L, L° and L+, name the new cases with $\deg_{x, w} g \ge p$ in which they hold. The three nodes stay conjectures. The notes of SG0000007D say that H1 holds in the form $\operatorname{in} G_m \in K[x'_m]$ for $g \in K[[y, z]][x^p, w^p]$.
- The notes of SG0000008E and SG0000008K name SG00000090 and SG00000092 for $\deg f \ge p$ and $\deg_{x, w} g \ge p$. The notes of SG0000006Y name SG00000095 for each rank.

## 0.4.66 - 2026-11-27

### Added

- SG0000008P to SG0000008Z for track NW, the Newton and Frobenius preparation of research note 55, in the form that the referee report in note 60 corrected. SG0000008P is Theorem 5.3 of note 05 in the weight form, with the Lean proof Singularity.newtonNondegenerate_purelyInseparable_iff for a perfect reduced ring. SG0000008Q is the counterexample $z^p + t x^p$ over $\mathbb{F}_p(t)$, which shows that the perfect field is necessary, with the Lean proof Singularity.newtonNondegenerate_ratFunc_example. SG0000008R is Theorem 4.1 of note 55 for the changes of $x$ and the cleanings. SG0000008S is Theorem 4.3 of note 55 for all changes of coordinates when $D > p$. SG0000008T is the corrected Proposition 5.4(b). SG0000008V is the corrected Proposition 11.1, with "singular or not transverse". SG0000008W and SG0000008X are Theorems 10.1 and 11.2. SG0000008Y is the Fano obstruction in characteristic 2. SG0000008Z is a conjecture for the open case $D = p$. Only SG0000008P and SG0000008Q have a Lean proof.
- SG00000089 to SG0000008N for the corner runs in four variables of Volume 7, Section 3.18 of the handbook, "Planar runs and the hypothesis H1". The nodes are the results of research notes 50, 52 and 54 that the referee reports in notes 52, 54 and 63 mark safe, in the corrected form of these reports. SG00000089 and SG0000008A are Theorem 4.1 and Corollary 5.1 of note 50: a corner run with $\deg_{x, w} g < p$ that is not planar satisfies Hypothesis H1 and Conjectures L and L°. SG0000008C, SG0000008F, SG0000008H and SG0000008J are Lemma 4.1, Proposition 5.2, Lemma 5.1 and Theorem 5.3 of note 52. SG0000008B, SG0000008D, SG0000008E, SG0000008G, SG0000008K, SG0000008M and SG0000008N are Lemma 1.1, Lemma 3.1, Theorem 3.2, Proposition 4.1, Theorem 5.1, Corollary 5.2 and Theorem 7.1 of note 54. SG0000008E is Statement D, that is, Conjecture T for the planar runs and the polynomials of degree less than $p$. SG0000008K says that there is no planar corner run with $1 \le \deg_{x, w} g < p$. SG0000008M says that each corner run with $\deg_{x, w} g < p$ is linear and satisfies H1, L and L°. SG0000008N says that a run is linear in all free coordinates or in none. None of the new nodes has a Lean proof.
- The lab simulator `lab/sim` (track LB, issue 289). It is a Python package with no dependencies. It computes over F_p and F_{p^k}, cleans z^q + F, makes point charts and coordinate charts with translations and the divisor update, and gives r, d, rho, tau, the hypotheses (H1) and (H2) and nu^G along coordinate strata. It also makes random walks and checks the certificates of note 11. The test bank has the kangaroo point of Hauser and Example 3.17 of note 03, the cycle of Hauser and Perlega, Examples 3.13.21, 3.14.9 and 3.15.18 of Volume 7 of the handbook, and the counterexamples of notes 38, 40 and 42. The new workflow `lab` runs the tests.

### Changed

- The Lean record is the record of singularity-lean 0.4.51, with 3512 declarations.
- The notes of SG0000003G name the Lean proof of the weight form SG0000008P. The notes of SG0000003M name the Lean proof of Theorem 3.11 of research note 03 at a point of the chart that is not its origin (Singularity.map_logJacobian_eq_map_pointChart_zero). The notes of SG0000003E and SG0000003F name the Lean proofs of Lemma 3.6(3) and Corollary 3.8 of note 03 for the adapted changes of coordinates of $k[x]$. The Lean fields of these nodes do not change.
- SG0000007D, Hypothesis H1 for $\deg_{x, w} g < p$, has the kind theorem. SG0000008M proves it.
- SG0000007E, Theorem 3.17.33, has no hypothesis. Its title does not name H1.
- The notes of SG0000006Z and SG00000075, Conjectures L and L°, say that they hold for $\deg_{x, w} g < p$ and are open for $\deg_{x, w} g \ge p$. The two nodes stay conjectures. The notes of SG00000071 name the runs with $\deg_{x, w} g < p$ for which it holds.

## 0.4.65 - 2026-11-27

### Added

- SG0000007W to SG00000088 for Target T of the research notes: Jung's method for 4-folds in characteristic $p > 24$, Volume 9, Section 3.21 of the handbook. The nodes are the results of research note 56 that note 62 marks safe, in the corrected form of note 62. SG00000082 is Theorem 14.4 of Cutkosky in dimension 4, with the embedded resolution of divisors in $\mathbb{P}^4$ (SG0000007W) as a hypothesis. SG00000083 gives resolution of 4-folds for $p > 24$ from SG00000082 and the patching statement SG0000007X, which has no finite set in its premise and so is a priori stronger than SG0000001J. SG00000084 is the Hermitian 4-fold, where each linear projection has local degree at least $q$ and the tame projections are exactly those from $\mathbb{F}_{q^2}$-rational points. SG00000085 is Jung's method under a bound on the completed local degrees. SG00000086 is the folklore theorem on hypersurfaces of bounded degree in large characteristic. SG00000087 and SG00000088 are the Hasse derivative test and the corrected example of a disguised $z^2 - x^p$. SG0000007Y, SG0000007Z and SG00000080 are the cited theorems of Albanese, Abhyankar and Kato as hypotheses. None of the new nodes has a Lean proof.
- Paper records Kat94 and Niz06 for the resolution of log regular schemes.

## 0.4.64 - 2026-11-27

### Changed

- SG00000068, Example 3.15.18 of Volume 7 of the handbook, has the Lean proof Singularity.Translations.exRun_of_charts over `ZMod p`. Lean has no definition of a corner run with free translations, so the Lean statement is a sequence of chart steps with $\rho = 1$.
- SG0000003M, the transformation law of the log-Jacobian ideal under a point blowup, has the Lean proof Singularity.map_logJacobian_eq_map_pointChart. This is Theorem 3.11 of research note 03 as an equality in the local ring of the origin of the chart, in place of the two inclusions.
- The notes of SG0000003E, SG0000003F and SG0000003N name the Lean proofs of part 2 of Lemma 3.6 for polynomial units, of Corollary 3.8 and Definition 3.9 in fixed coordinates, and of Corollary 3.14 of research note 03. The notes of SG0000006B and SG0000006E name the Lean proofs of the facts on Lucas's theorem and on the primitive vectors of Section 3.16 of Volume 7, and the notes of SG0000004F name the Lean proof of the formula for the transcendence degree. These nodes keep their Lean fields, or have none, because the Lean proofs are partial.
- records/lean.json pins singularity-lean 0.4.48 at commit 0cff052, with the base package at commit 6ba20cb. The record has 3340 declarations and none with sorry. records/base-charzero.json and records/trust.json name the new commits and the new count.

## 0.4.63 - 2026-11-27

### Added

- SG0000007F to SG0000007V for the base blowups of the algorithm of Cossart for $z^p + g$ of Volume 7, Section 4.3 of the handbook, and for the Lucas form of Volume 7, Section 4.1. SG0000007F and SG0000007G are Lemmas 10.3 and 10.4 of the research notes, with Lean proofs by the theorem of Lucas. SG0000007H and SG0000007J give the order of $z^q + g$ along the lifted center and the chart, with Lean proofs. SG0000007K and SG0000007M compute the generic multiplicity. SG0000007N says that the lifting test holds for a regular center if and only if the hypersurface has multiplicity $p$ at the generic point of the center, and then the blowup is permissible. SG0000007P says that no regular center in the multiplicity $p$ locus fails. SG0000007Q reads the test from the clean part. SG0000007R and SG0000007S bound the invariant $\nu$ of Cossart along a failing center. SG0000007T and SG0000007V are failing centers of the algorithm, and SG0000007V passes through a point of multiplicity $p$. The proofs are in notes 10, 43 and 47 of the research notes. SG0000007K to SG0000007V have no Lean proof.

### Changed

- records/lean.json pins singularity-lean 0.4.46 at commit 4e04231, with the base package at commit d84acc8. The record has 3198 declarations and none with sorry. records/base-charzero.json and records/trust.json name the new commits and the new count.

## 0.4.62 - 2026-11-27

### Added

- SG0000006J to SG0000007E for the corner runs with translations in four variables of Volume 7, Section 3.17 of the handbook. The nodes give the closed form of the transform and the criterion for the drop in four variables, the counterexample $x^2 y^{p-2} z^{p-2} + F$ to the finiteness of the translations, the reduction of a cylindrical point to three variables, the corner surfaces and corner curves with the order of $G$ at least $\rho$, the counterexample $x w (x + w) y^{p-3} z^{p-3}$ to Conjecture L+, and the case of degree less than $p$ under the hypothesis H1. The proofs are in notes 38 to 42 of the research notes. None of the nodes has a Lean proof.

## 0.4.61 - 2026-11-27

### Added

- SG00000069, SG0000006A, SG0000006B, SG0000006C, SG0000006D, SG0000006E, SG0000006F, SG0000006G and SG0000006H for the finiteness of the translations of Volume 7, Section 3.16 of the handbook. SG00000069 says that the closed form of the transform and the criterion for the drop hold when $g$ is a power series in $x$. SG0000006A is the Kaplansky inequality for power series along the translations. SG0000006B says that the tie set of the limit values has only $1$ and powers of $p$. SG0000006C, SG0000006D and SG0000006E treat the three cases of the tie set for $\mu x + F(x^p)$. SG0000006F says that a change of the free coordinate keeps an infinite number of nonzero translations. SG0000006G gives only a finite number of nonzero translations for $\mu x + F(x^p, y, z)$. SG0000006H gives only a finite number of nonzero translations for each clean $g \in K[[y, z]][x]$, so Question 3.13.18 has a positive answer for each corner run with free translations. The proofs are in notes 34 to 37 of the research notes. None of the nodes has a Lean proof.

### Changed

- records/lean.json pins singularity-lean 0.4.44 at commit 1fe514d, with the base package at commit 1017a8e. The notes of SG0000005Z name the Lean proof of Lemma 3.14.6 and of parts 1 to 3 of Theorem 3.14.7 with no hypothesis.

## 0.4.60 - 2026-11-27

### Changed

- The records pin tamnd/singularity-lean 0.4.43 at commit 8c9ec55, with 3138 declarations. The base record is from commit 6c993dc.
- The notes of SG0000005Z (Theorem 3.14.7) and SG00000061 (Example 3.14.9) name the Lean proofs of their parts in Singularity/Invariant/OriginRunsCorner.lean, and the parts that are not in Lean.

## 0.4.59 - 2026-11-27

### Added

- SG00000062, SG00000063, SG00000064, SG00000065, SG00000066, SG00000067 and SG00000068 for the runs with free translations of Volume 7, Section 3.15 of the handbook. SG00000062 says that the sequence of the translations of a corner run is a pseudo Cauchy sequence of transcendental type over the completion. SG00000063 says that $\rho$ does not depend on the cleaning, on the free coordinate or on a factor $\varepsilon^p$, and that a change of the free coordinate gives again a corner run with free translations. SG00000064 makes $\partial_x g_m$ a monomial times a unit for $m$ large when the run has an infinite number of nonzero translations. SG00000065 is the tame case, where the dominant index of Kaplansky is $1$. SG00000066 says that no corner run with free translations of $\mu x + B_0$ keeps $\rho \ge 1$. SG00000067 gives only a finite number of nonzero translations when $\deg_x g < p$. SG00000068 is the run of $x^2 y^{p-2} z^{p-2}$, with $\rho = 1$ at each point. The proofs are in notes 30 and 33 of the research notes. Note 33 corrects Theorem 6 of note 30, which said that no such run keeps $\rho \ge 1$. None of the nodes has a Lean proof.

## 0.4.58 - 2026-11-27

### Changed

- The records pin tamnd/singularity-lean 0.4.41 at commit 8cd9a21, with 2994 declarations. The base record is from commit 4d150bd.
- SG0000005X (Lemma Y) has a Lean proof: Singularity.OriginRuns.length_add_one_le_phi.
- SG0000005Y (Theorem A) has a Lean proof for polynomials: Singularity.OriginRuns.originRun_not_forall_one_le. The notes give the hypotheses of the Lean form.

### Added

- SG0000005X, SG0000005Y, SG0000005Z, SG00000060 and SG00000061 for the origin runs of Volume 7, Section 3.14 of the handbook. SG0000005X is the potential for the difference of two exponent vectors. SG0000005Y says that an origin run that uses all the charts an infinite number of times reaches $\rho = 0$. SG0000005Z gives the corner curves with the order of $G$ at least $\rho$ for an origin run that uses $k$ charts, with $2 \le k \le n - 1$. SG00000060 answers Question 3.13.18 for each origin run in each dimension $n \ge 3$. SG00000061 is an origin run in four variables that uses three charts for ever and has no surface with the order of $G$ at least $\rho$. The proofs are in notes 31 and 32 of the research notes. None of the nodes has a Lean proof.

## 0.4.57 - 2026-11-27

### Changed

- The records pin tamnd/singularity-lean 0.4.40 at commit c1f9cda, with 2876 declarations. The base record is from commit 42abe98.
- SG0000005S has a Lean proof: Singularity.CornerCurves.curveRun_end. It no longer lists SG0000005R in uses, because its proof is a direct computation. The notes name the Lean proofs of the conditions (H1) and (H2) and of the two cases $a > p$ and $a < p$.

## 0.4.56 - 2026-11-27

### Changed

- The records pin tamnd/singularity-lean 0.4.39 at commit 5f87c06, with 2857 declarations. The base record is from commit 17e98b6.

### Fixed

- SG0000005S: the statement now separates the cases $a > p$ and $a < p$. If $a < p$, the run of corner curves stops after a finite number of steps with $\rho = a - 1$. The notes name the Lean coverage in Singularity/Invariant/LogJacobianCornerCurves.lean.

## 0.4.55 - 2026-11-27

### Added

- The node SG0000005W is Theorem 3.13.27 and Corollary 3.13.28 of Volume 7 of the handbook: for $g = B_1 x^p + B_0$, a corner run with free translations has only a finite number of nonzero translations, and its corner curves have $\nu^G \ge \rho$ for $m$ large. It has a proof in the text and no Lean proof.

## 0.4.54 - 2026-11-27

### Added

- The node SG0000005V is Corollary 3.13.23 of Volume 7 of the handbook: at the end of a long enough stretch of corner charts with no translation, both corner curves have $\nu^G \ge \rho$. It has a proof in the text and no Lean proof.

## 0.4.53 - 2026-11-27

### Added

- The node SG0000005T is Lemma 3.13.14 of Volume 7 of the handbook for a coordinate subvariety and polynomial $h$: the order of $G$ along $Z$ is at most the order of the log-Jacobian ideal along $Z$ plus 1. It is proved in Lean by `Singularity.orderGAlong_le_idealOrdAlong_add_one` (tamnd/singularity-lean#173). The node SG0000005M uses it. The records pin the Lean release 0.4.38.

### Changed

- The notes of SG0000005M say that the claim on coordinate subvarieties is in Lean.

## 0.4.52 - 2026-11-27

### Added

- The node SG0000005R is Theorem 3.13.20 of Volume 7 of the handbook: for $n = 3$ and an infinite run of the two corner charts at the origin, both corner curves have $\nu^G \ge \rho$ for $m$ large. The node SG0000005S is Example 3.13.21: the blowups of the corner curves alone can keep $\rho$ for ever. Both nodes have proofs in the text and no Lean proof.

## 0.4.51 - 2026-11-27

### Added

- The node SG0000005Q is the run of Example 3.13.15 of Volume 7 of the handbook: along each sequence of the two corner charts, the point is clean, the log-Jacobian ideal is $(x^p, y^m z^l)$ and $\rho = p$. It is proved in Lean by `Singularity.CornerRuns.cornerRun_of_charts` (tamnd/singularity-lean#171). The node SG0000005M uses it. The records pin the Lean release 0.4.37.

### Changed

- The notes of SG0000005M say which parts are in Lean. The claim on subvarieties is not in Lean.

## 0.4.50 - 2026-11-27

### Added

- The nodes SG0000005N and SG0000005P are Examples 3.13.10 and 3.13.11 of Volume 7 of the handbook: the run that takes the corners on the surface $x = 0$, and the run of Cossart and Piltant that follows a curve in a plane. Both are proved in Lean by `Singularity.SurfaceRuns.surfaceRun_of_charts` and `Singularity.SurfaceRuns.cpRun` (tamnd/singularity-lean#169). The records pin the Lean release 0.4.36.

## 0.4.49 - 2026-11-27

### Added

- The node SG0000005M is Example 3.13.15 of Volume 7 of the handbook: a run of $g = x^p y z + y^{p+2} z^{p+1}$ with $\Delta = \{y, z\}$ that takes the corners for ever and lies on no subvariety of positive dimension along which the order of $G$ is at least $\rho$. It shows that the conjecture SG0000005K is false. It has no Lean proof yet.

### Changed

- The notes of SG0000005K say that the conjecture is false by SG0000005M, and give the corrected form.

## 0.4.48 - 2026-11-26

### Added

- The nodes SG0000005H and SG0000005J are the two infinite runs of Volume 7, Section 3.12 of the handbook: the run along the $y$-axis and the run at an isolated point of the locus of $\rho$. Both are proved in Lean by `Singularity.CurveRuns.curveRun` and `Singularity.CurveRuns.isolatedRun` (tamnd/singularity-lean#162). The Lean proof does not give the claim that the origin is isolated in the locus.
- The node SG0000005K is the hypothesis H4' of Volume 7, Section 3.13: each infinite run where $\rho \ge 1$ stays lies on a subvariety of positive dimension along which the order of $G$ is at least $\rho$. It is open.
- The paper Chr79 is new. It is the theorem of Christol on automatic series, which Volume 7, Section 3.13 uses for the transcendental curve of the example of Cossart and Piltant.

### Changed

- The records are pinned at singularity-lean fb37ddb (release v0.4.35), with 2607 declarations.

## 0.4.47 - 2026-11-26

### Added

- The papers Hir77, Hir03, Hir05, Hir17, Kuh00, Cut99, CP04, Cut24 and San17 are new, for Volume 5, Chapter 5 of the handbook. Hir77, Hir03 and Hir05 are the papers of Hironaka on idealistic exponents and infinitely near singular points. Hir17 is the manuscript of Hironaka of 2017 on his web page, which announces resolution in characteristic $p$. It is not refereed. Kuh00 is the paper of Kuhlmann on the valuation theoretic and model theoretic aspects of local uniformization. Cut99 is the memoir of Cutkosky on local monomialization. CP04 is the paper of Cutkosky-Piltant on the ramification of valuations. Cut24 is the counterexample of Cutkosky to strong local monomialization for independent defect, arXiv:2302.07710, now in Ann. Fac. Sci. Toulouse Math. San17 is the paper of San Saturnino on the defect and key polynomials, arXiv:1412.7697, now in J. Algebra 481 (2017). Each record gives the journal, the volume, the pages and the DOI when there is one.

## 0.4.46 - 2026-11-26

### Changed

- SG0000000Y: the notes tell that tamnd/singularity-lean#156 proves that a divisorial valuation is discrete of rank 1 (Volume 3, Corollary 2.2.4 of the handbook).

## 0.4.45 - 2026-11-26

### Changed

- SG0000005C: the Lean statement and proof are `Singularity.KangarooExample.kangarooExample`, over $\mathbb{F}_2$ in three variables (tamnd/singularity-lean#158). The proof checks the two steps, the cases of the three points and the values 1, 2 and 1 of $\tau_\rho$. The status is now proved.
- The records are pinned at tamnd/singularity-lean cadf65e, the merge commit of the release 0.4.33, with 2337 declarations. The base record is at cbfeb79.

## 0.4.44 - 2026-11-26

### Changed

- SG0000000Y: the notes say that tamnd/singularity-lean#153 proves that the residue field of an Abhyankar valuation is finitely generated (Volume 3, Corollary 2.2.4 of the handbook). The Lean name is `Singularity.IsAbhyankarValuation.fg_residueField`.

## 0.4.43 - 2026-11-26

### Changed

- SG0000005D: the field `negation` is `Singularity.KangarooCounterexample.not_kangarooPathConjecture`. The status is now refuted. The entry of release 0.4.41 said that the map has no status for a false conjecture. That was not correct.
- SG0000005G: the Lean proof is `Singularity.KangarooCounterexample.not_kangarooPathConjecture`, over $\mathbb{F}_2$ in three variables (tamnd/singularity-lean#150). The node no longer uses SG0000005D, since the proof does not use the conjecture. The status is now proved.
- The records are pinned at tamnd/singularity-lean c42c2c0, the merge commit of the release 0.4.31, with 2143 declarations.

### Fixed

- CP14 and CP15: the arXiv identifier 1203.2484 belongs to CP15, "Characteristic polyhedra of singularities without completion". It was on CP14 by mistake. CP14 now has the full title of the RACSAM paper and no arXiv identifier.

## 0.4.42 - 2026-11-26

### Changed

- SG0000005F: the node no longer uses SG0000005D. The theorem proves a case of the conjecture, and its proof does not use the conjecture. The status is now proved.

## 0.4.41 - 2026-11-26

### Added

- SG0000005E: in the first case the directrix of the log-Jacobian order is the intersection of the directrices of the forms $E_i F = r_i F + x_i \partial_i F$ for $i \in \Delta$ (Volume 7, Lemma 3.11.4 of the handbook). The Lean statement and proof are `Singularity.logJacobianDirectrix_eq_iInf_caseAForm`.
- SG0000005F: the kangaroo path conjecture holds if the codimension of the directrix at the start is at most 1 (Volume 7, Proposition 3.11.5 of the handbook). The Lean statement and proof are `Singularity.kangarooPath_of_codim_le_one`.
- SG0000005G: a kangaroo path over $\mathbb{F}_2$ in three variables where the codimension of the directrix goes down from 2 to 1 (Volume 7, Example 3.11.6 of the handbook). This is a counterexample to SG0000005D. There is no Lean computation yet.

### Changed

- SG0000005D: the statement and the notes now say that the conjecture is false, with SG0000005G as the counterexample. The map has no status for a false conjecture, thus the status stays open.
- The records are pinned at tamnd/singularity-lean d081656, the merge commit of tamnd/singularity-lean#149, with 2018 declarations.

## 0.4.40 - 2026-11-26

### Changed

- SG0000000Y: the note says that the value group of an Abhyankar valuation is free of finite rank in Lean (tamnd/singularity-lean#146). The residue field part is not in Lean.

## 0.4.39 - 2026-11-26

### Added

- SG0000005B: the codimension of the directrix does not go down along a run of points of the second case, and at the last step it is at most the full codimension (Volume 7, Proposition 3.11.1 of the handbook). The Lean statement and proof are `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen`.
- SG0000005C: an example over $\mathbb{F}_2$ where the codimension of the directrix goes down at the last step of a kangaroo path, back to its value at the start (Volume 7, Example 3.11.2 of the handbook). There is no Lean computation yet.
- SG0000005D: the conjecture that the codimension of the directrix does not go down along a kangaroo path (Volume 7, Conjecture 3.11.3 of the handbook). The Lean statement is `Singularity.KangarooPathConjecture`. It is open.

### Changed

- The records are pinned at tamnd/singularity-lean 979cb14, the merge commit of tamnd/singularity-lean#143, with 2013 declarations.

## 0.4.38 - 2026-11-26

### Changed

- Note the passage from the base field to the decomposition field (tamnd/singularity-lean#141) on SG0000001F.

## 0.4.37 - 2026-11-26

### Changed

- The records are pinned at tamnd/singularity-lean 1d8b1df, the merge commit of tamnd/singularity-lean#139, with 1989 declarations.
- SG00000059 has the Lean statement and proof `Singularity.idealOrd_logJacobianTangent_eq_ord`, and SG0000005A has `Singularity.residualOrderAlong_cleanPart_le_of_forall_eq_zero`. Their notes give the other Lean names.
- Note the choice of the monomial subfield of an Abhyankar valuation (tamnd/singularity-lean#138) on SG0000001E.

## 0.4.36 - 2026-11-26

### Added

- SG00000059 and SG0000005A for the milestone S7.16. For a clean $F$, the order of $\widetilde\Theta_0(G)$ is the residual order $d$, so the case of the log-Jacobian order is the type $d - \rho$. At a step where $\rho$ stays and no component of the divisor leaves, $d$ does not go up, and $\tau_\rho$ does not go down if $d$ stays.

### Changed

- The record Liu places Lipman's theorem in Chapter 8 (Theorem 8.3.44), not Chapter 9.
- SG0000003D cites Stacks tag 00NR (a regular quotient of a regular local ring) in place of 00NQ.

## 0.4.35 - 2026-11-26

### Changed

- The records are pinned at tamnd/singularity-lean 084346f, the merge commit of tamnd/singularity-lean#136, with 1952 declarations.
- SG00000057 has the Lean statement and proof `Singularity.logJacobianFullDirectrixCodim_le_cleanPart`, and SG00000058 has `Singularity.fullDirectrixExample_codim`. Their notes give the other Lean names.

## 0.4.34 - 2026-11-26

### Added

- SG00000057 and SG00000058 for the milestone S7.15. The full codimension $\widetilde\tau$ of the directrix, which uses all of $\widetilde\Theta(G)$ in both cases, does not go down at a step from the second case where $\rho$ stays. An example over $\mathbb{F}_2$ shows that it can go down at a step from the first case.

## 0.4.33 - 2026-11-26

### Changed

- The records are pinned at tamnd/singularity-lean 3b63a7b, the merge commit of tamnd/singularity-lean#134, with 1937 declarations.
- SG00000055 has the Lean statement and proof `Singularity.idealOrd_logJacobianTangent_cleanPart_of_forall_eq_zero`, and SG00000056 has `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_forall_eq_zero`. Their notes give the other Lean names.

## 0.4.32 - 2026-11-26

### Added

- SG00000055 and SG00000056 for the milestone S7.14. If $\rho$ stays, the old point is in the first case and no component of the divisor leaves, then the new point is in the first case, and $\tau_\rho$ does not go down. The two nodes have no hypothesis on $p$.

## 0.4.31 - 2026-11-26

### Changed

- The records are pinned at tamnd/singularity-lean b1c2ad8, the merge commit of tamnd/singularity-lean#132, with 1927 declarations.
- SG00000054 has the Lean statement and proof `Singularity.caseAToCaseBExample_cases`. Its notes give the other Lean names.

## 0.4.30 - 2026-11-26

### Added

- SG00000054, an example over $\mathbb{F}_3$ in three variables for the milestone S7.13. The old point is in the first case with $p \mid |r| + d$, $\rho$ stays, and the new point is in the second case. So the hypothesis of SG00000052 on $|r| + d$ is necessary.

## 0.4.29 - 2026-11-26

### Changed

- The records are pinned at tamnd/singularity-lean acb8b07, the merge commit of tamnd/singularity-lean#130, with 1921 declarations.
- SG00000052 has the Lean statement and proof `Singularity.idealOrd_logJacobianTangent_cleanPart_of_caseA`, and SG00000053 has `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_ne_zero`. Their notes give the other Lean names.

## 0.4.28 - 2026-11-26

### Added

- SG00000052, a proposition for the milestone S7.12. If $\rho$ stays, the old point is in the first case and $p$ does not divide $|r| + d$, then the new point is in the first case.
- SG00000053, a corollary for the milestone S7.12. In the same situation $\tau_\rho$ does not go down, so SG00000050 holds with no hypothesis on the new point.

## 0.4.27 - 2026-11-26

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
