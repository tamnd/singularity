# 01. The state of the field, November 2026

This document records what is known on 2026-11-23, with sources. The tags are:
- **[P]**: the primary source was read (abstract page, paper, journal page, repository);
- **[S]**: secondary, from citations, search results or memory, and partly confirmed;
- **[U]**: unverified.

Every [S] and [U] item becomes a task for the `reader` role (document 10) before a node depends on it. Links to arXiv have the form `https://arxiv.org/abs/<id>`.

## 1.1 The problem is open

Resolution of singularities of varieties of dimension $\ge 4$ over a field of characteristic $p > 0$ has no accepted proof. Embedded resolution of a threefold in a smooth fourfold is also open. Non-embedded resolution of threefolds is known (1.3).

Sources for the status:
- the introduction of Bérczi, arXiv:2602.06553 (February 2026) [P];
- google-deepmind/formal-conjectures issue #5403 (2026-09-09), which adds the Lean statement and calls the problem "open from dimension four on" [P]; issue #5441 states local uniformization, open from transcendence degree 4 on [S];
- the ProofAtlas problem page, checked 2026-08-06 [P];
- Cutkosky, Amer. J. Math. 131 (2009), which calls embedded resolution of threefolds "the fundamental open problem" [P].

No talk on resolution of singularities appears in the programme of ICM 2026 (Philadelphia, 23 to 30 July), from a search of a mirror of the schedule that may be incomplete [P]. Oberwolfach reports with char p resolution content are 57/2016, 6/2019, 6/2023 and 45/2025 [S].

Heisuke Hironaka died in Tokyo on 2026-03-18, aged 94 (Japan Times 2026-03-20; Nature obituary 2026-08-28) [S].

## 1.2 Claimed proofs

None of these is accepted, and the project found no public expert assessment of any of them. The project treats them as sources of ideas and of test cases, never as hypotheses (06.6, 14.3).

| Claim | Source | What it claims | Status |
|---|---|---|---|
| Hironaka 2017 | "Resolution of singularities in positive characteristics", preprint dated 2017-03-23, on his Harvard page [P, excerpts] | embedded resolution in all dimensions over any field of char $p$, with a graded algebra $\wp$ and a "local leverage up" method | not refereed, not published; no published gap analysis found [U] |
| Yi Hu, 2022 to 2026 | arXiv:2203.03842 (v4 2022); arXiv:2507.21400 and 2507.21399 (2025); overview arXiv:2608.10272; "Fundamental Lemmas in Universal Resolution", arXiv:2609.24047 [P, abstracts] | 2022: projective resolution over a perfect field, through Mnëv-Lafforgue universality and universal blowups of Grassmannians. 2025: the weaker "for each $X$ there is a smooth $Y \to X$ with $Y$ resolvable". 2026: corrects Chapters 5, 6 and 8 of the 2025 paper | no referee report or expert comment found; the claim narrowed over time; the step from smooth-local to global resolution is the hard part in char $p$ (3.3.4) |
| Chenxiao Tian, 2026 | arXiv:2608.20066, 798 pages, filed in math.GM [P, abstract and front matter] | canonical strong embedded resolution and principalization over a perfect field, with Hasse-derivative saturation of marked Rees algebras and an "exceptional history" order | no expert reaction found; the abstract does not address the known obstructions of 1.6 |

[U] A Lean formalization is the strongest test that a long claimed proof can get. The project does not plan one, because the cost is high and the chance of success is low. The project does take each claim's main invariant as a candidate for the lab test E2 (document 13): an invariant that the lab shows to go up on a certified example (13.4) refutes the claim's key lemma at low cost. A refutation is published to the author first.

## 1.3 Dimension 3 and below

**Curves and surfaces.**
- Lipman, Ann. of Math. 107 (1978): excellent surfaces, by normalized blowups of the singular locus [S].
- Cossart-Jannsen-Saito, Springer LNM 2270 (2020), arXiv:0905.2191, with an appendix by Schober: canonical embedded resolution of excellent two-dimensional schemes by permissible blowups, with the Hilbert-Samuel function, the directrix and Hironaka's characteristic polyhedron [P]. This is the main char-free toolkit for the invariants.
- Hauser-Perlega, Publ. RIMS 60 (2024) 767-813, from Perlega's thesis arXiv:2011.14443: embedded resolution of surfaces in 3-space with a modified residual order that survives kangaroo points [P].
- Hauser-Wagner, arXiv:1403.6789: $z^p + f(x, y)$ with a correction term to the residual order [P].
- Kawanoue-Matsuki, arXiv:1205.4556 (Adv. Stud. Pure Math. 70, 2016): surfaces in the IFP framework, with an invariant that drops at every blowup; the monomial case in arXiv:1507.05195 [P].
- Benito-Villamayor, Compositio 149 (2013), arXiv:1004.1803: a new invariant from elimination algebras, which gives embedded resolution of surfaces [P].

**Threefolds.**
- Abhyankar (1966) for algebraically closed fields of char $p > 5$; Cutkosky, Amer. J. Math. 131 (2009) 59-127, arXiv:math/0606530, a shorter proof of the same theorem [P].
- Cossart-Piltant, J. Algebra 320 (2008) and 321 (2009): birational resolution of threefolds over every field of char $p > 0$, including small $p$ and imperfect fields, by local uniformization and patching [P/S].
- Cossart-Piltant, J. Algebra 529 (2019) 268-535, arXiv:1412.0868: Grothendieck's resolution conjecture for reduced quasi-excellent schemes of dimension $\le 3$ [P].
- Kollár, arXiv:2012.05327 and 2102.03162, and Bhatt-Ma-Patakfalvi-Schwede-Tucker-Waldron-Witaszek, arXiv:2012.15801: projective log resolutions for quasi-excellent schemes of dimension $\le 3$ [P]. BMP+ say that the dimension 3 theorems do not give a resolution by a sequence of blowups in regular centres. That gap is the embedded problem.

**Special classes in every dimension.**
- Martínez-Núñez, arXiv:2611.18258 (2026-11-13): equivariant resolution of varieties with a torus action of complexity $\le 3$ in char $p$, by proper polyhedral divisors, resolution of the quotient of dimension $\le 3$, and toroidal resolution [P]. One of the few unconditional results in dimension $\ge 4$, for a special class.
- Włodarczyk, Adv. Math. 407 (2022), arXiv:2007.13846: functorial resolution of locally toric (binomial) varieties in every characteristic, by cobordant blowups [P].
- Abramovich-Schober, arXiv:2208.08951: weighted resolution of binomial varieties in every characteristic [P].

## 1.4 Local uniformization and valuations

Zariski's strategy is local uniformization along every valuation, then patching. In char $p$ local uniformization is known in dimension $\le 3$ (Abhyankar; Cossart-Piltant) and open from 4 on. No claim of a general proof was found.

| Result | Source |
|---|---|
| Abhyankar valuations admit local uniformization, if the residue field extension is separable | Knaf-Kuhlmann, Ann. Sci. ENS 38 (2005) [P] |
| the separability hypothesis removed | Cutkosky, arXiv:2003.06374 [P] |
| every valuation admits local uniformization in a finite (Galois) extension of the function field | Knaf-Kuhlmann, Adv. Math. 221 (2009), arXiv:math/0702856 [P] |
| local uniformization after a purely inseparable extension | Temkin, J. Algebra 373 (2013), arXiv:0804.1554 [P] |
| reduction to valuations of height one | Temkin, arXiv:2301.09160, to appear in J. Algebra [P]; Novacoski-Spivakovsky, arXiv:1204.4751 and 1509.03122 [P/S] |
| Knaf's conjecture for pure extensions | Novacoski, arXiv:2401.00182 (v2 2026-10-16) [P] |
| Teissier's 2003 conjecture: valuations have tight extensions to the completion | Herrera Govantes-Olalla Acosta-Spivakovsky-Teissier, arXiv:2607.11223 (July 2026) [P]; the abstract calls this a step in two recent approaches to local uniformization in char $p$, which it does not name [U] |
| key polynomials for simple extensions of valued fields | Herrera-Mahboub-Olalla-Spivakovsky, J. Singularities 25 (2022), arXiv:1406.0657 [S] |

**Defect**, the core obstruction of route R2:
- Cutkosky-Mourtada, arXiv:1711.02726: the defect of the finite extensions that come from projections is the only obstruction in their setting [P].
- Kuhlmann-Rzepka, arXiv:1811.04396 (Trans. AMS [S]): dependent and independent Artin-Schreier defect, deeply ramified fields [P].
- Cutkosky-Kuhlmann-Rzepka, Math. Nachr. 298 (2025): a degree $p$ extension has independent defect if and only if its module of relative Kähler differentials is zero [S].
- Kuhlmann, J. reine angew. Math. 719 (2016), tame valued fields; Dutta-Kuhlmann, Pacific J. Math. 307 (2020); Kuhlmann, arXiv:2503.13157 [S].

**Teissier's program**: Teissier, arXiv:1401.5204, overweight deformations of toric varieties [S]; Mourtada-Schober, "Teissier singularities", C. R. Math. (2025), arXiv:2502.01239, a class that would play the role of quasi-ordinary singularities in a char $p$ Jung method [P/S].

## 1.5 Invariants and programs in char p

| Program | Main sources | Missing piece |
|---|---|---|
| Hauser and coauthors: residual order, kangaroo points, corrections | Hauser, Bull. AMS 40 (2003) and 47 (2010) [P/S]; arXiv:0811.4151 [S]; Hauser-Schicho, arXiv:1010.0163 [S]; Hauser-Perlega, J. Algebraic Geom. 28 (2019), arXiv:1802.05010 [P], and arXiv:1906.09593 [S]; Hauser-Perlega 2024 (1.3) | a correction term that controls the kangaroo part in every dimension |
| Kawanoue-Matsuki: idealistic filtrations (IFP), leading generator systems, invariant $(\sigma, \tilde\mu, s)$ | Kawanoue, Publ. RIMS 43 (2007), arXiv:math/0607009; Kawanoue-Matsuki, arXiv:math/0612008, 1205.4556, 1507.05195 [P] | termination in the monomial case |
| Villamayor school: Rees algebras with Hasse-Schmidt operators, elimination algebras, Samuel slope | Villamayor, arXiv:math/0606795, math/0606796, 0712.3733 [S]; Bravo-Villamayor, Adv. Math. 224 (2010) [S]; Benito-Villamayor 2013 [P]; Bravo-Encinas-Pascual-Escudero, Nash multiplicity sequences, arXiv:1802.02566, 1811.12203 [S]; Benito-Bravo-Encinas, asymptotic Samuel function, Rev. Mat. Complut. 37 (2024), arXiv:2107.14188 [P], and arXiv:2506.14993 (the Samuel slope characterizes regularity) [P] | a decreasing invariant in the wild case, where elimination loses information |
| Cossart-Jannsen-Schober: characteristic polyhedra | Cossart-Jannsen-Schober, RACSAM 113 (2019), arXiv:1805.10660; Cossart-Schober, Collect. Math. 72 (2021), arXiv:1411.2522; Schober, arXiv:1410.6541, 1410.6543, 1708.04784 [S] | an invariant built from the polyhedron that drops in dimension $\ge 4$ |
| Włodarczyk's char $p$ program | RIMS lecture notes, December 2008, unpublished [S] | |
| Abramovich-Quek-Schober, "Invariants of singularities in arbitrary characteristics" | cited as in preparation [U] | |

The pairing of the two Villamayor arXiv numbers math/0606795 and math/0606796 with the titles "Rees algebras on smooth schemes" and "Hypersurface singularities in positive characteristic" is [U].

## 1.6 Obstructions and counterexamples

Each item is a candidate for a Lean counterexample (13.4) and a regression test for every proposed invariant (E2).

1. **Maximal contact fails.** Narasimhan, Proc. AMS 87 (1983): the equimultiple locus need not lie in a smooth hypersurface. The char 2 example $x^2 + yz^3 + zw^3 + y^7 w$ in $\mathbb{A}^4$ has a curve of singular points with 4-dimensional tangent space (Abramovich, arXiv:2503.17321, Remark 5.5.3) [S/P].
2. **Moh's stability theorem is false.** Moh, Publ. RIMS 23 (1987), bounded the increase of the residual order [S]. Hauser-Perlega, arXiv:1802.05010, give a purely inseparable hypersurface and a cycle of point blowups along which the residual order grows, which disproves Moh's stability claim [P]. It is not a counterexample to resolution. The exact one-step bound of Moh that survives is a task for the `reader` role.
3. **Kangaroo points.** Hauser, arXiv:0811.4151: the residual order jumps after a blowup, which is impossible in char 0 [S].
4. **The weighted invariant in char 2.** For Whitney's umbrella in char 2 the natural char $p$ analogue of the ATW invariant is not upper semicontinuous, and it is not invariant under smooth morphisms (Abramovich, arXiv:2503.17321, Remark 5.9.3) [P].
5. **Char 2 pinch points.** Abramovich-Temkin, arXiv:2602.15612 (v3 2026-07-06): weighted blowups cannot give a resolution that preserves normal crossings; every such pinch point is the coarse space of a normal crossings stack [P].
6. **Tangent spaces of stacks grow.** Abramovich-Quek-Schober, arXiv:2412.16426 (Beitr. Algebra Geom. 2026): plane curves in char $p$ by multi-weighted blowups, where the tangent space of the stack can go up [P].
7. **Nash blowups fail in dimension $\ge 4$.** Castillo-Duarte-Leyton-Álvarez-Liendo, arXiv:2409.19767, Ann. of Math. 203 (2026): toric counterexamples in every characteristic [P]. Follow-ups: arXiv:2511.01772 (the non-normalized Nash blowup fails in dimension 3), 2501.09811, 2511.17862, 2604.07519 [S].
8. **Local monomialization fails.** Cutkosky, Math. Ann. 362 (2015), arXiv:1404.7459 [P]; erratic birational behaviour in defect towers, arXiv:2111.12818, whose Theorem 5.6 was withdrawn in v3 [P].
9. **Defect** (1.4).

## 1.7 Characteristic 0 since 2018

The char 0 theorem was made short, memoryless and functorial. The methods are the templates that route R4 tries in char $p$.
- Weighted blowups: Abramovich-Temkin-Włodarczyk, arXiv:1906.07106, Algebra Number Theory 18 (2024) [P]; McQuillan, GAFA 30 (2020) [S]; ATW, arXiv:1709.03185 (JEMS 2020) [P], 1709.03206 [S], 2003.03659 [P].
- Logarithmic and multi-weighted: Quek, arXiv:2005.05939 [S]; Abramovich-Quek, arXiv:2112.06361 [P]; Abramovich-Belotto-Quek-Temkin-Włodarczyk, arXiv:2503.13341, and ATW, arXiv:2503.13345 (2025) [P]; foliated orbifolds, arXiv:2503.00926 [P].
- Cobordant blowups: Włodarczyk, arXiv:2203.03090, 2301.12452 (with results in every characteristic for restricted classes) [P]; Włodarczyk, arXiv:2602.14266 (2026) [P].
- **Temkin, "Dream resolution I: enough derivations"**, arXiv:2503.18205, and **II: excellent schemes**, arXiv:2507.11698 (v3 June 2026) [P]. An axiomatic frame: resolution by weighted blowups needs only enough derivations. It names exactly what char $p$ lacks, and it is the best interface for char $p$ experiments of route R4.
- Surveys: Temkin, arXiv:2303.00407; Abramovich, ICM 2018, arXiv:1711.09976, and CIRM notes arXiv:2503.17321 [P]; Oberwolfach Seminars 50 (2023) [S].
- Weighted methods in char $p$, for special cases: arXiv:2208.08951, 2412.16426, 2507.01232 (torus actions, non-perfect fields allowed, Math. Scand. 132 (2026)) [P].
- Foliations in char $p$: Posva, arXiv:2405.05735, resolution of 1-foliation singularities on surfaces and threefolds [P]. p-closed derivations are a candidate for "enough derivations" in char $p$.

## 1.8 Alterations

- de Jong, Publ. Math. IHÉS 83 (1996): regular alterations of every variety [S].
- Gabber, in Illusie-Laszlo-Orgogozo, Astérisque 363-364 (2014), arXiv:1207.3648: alterations of degree prime to any $\ell \neq p$, by local uniformization prime to $\ell$ [P/S].
- Temkin, Ann. of Math. 186 (2017), arXiv:1508.06255: alterations of $p$-power degree (tame distillation) [P/S].
- With Temkin 2013, "resolution up to a purely inseparable alteration of $p$-power degree" is the strongest unconditional statement in all dimensions. It is a natural target for the library (G2).
- Uses of alterations in place of resolution: Kelly, Astérisque 391 (2017) [S]; Huber-Kebekus-Kelly, arXiv:1407.5786 [S]; Huber-Kelly, arXiv:1706.05244 [S].

## 1.9 Artificial intelligence on this problem

- **Bérczi, arXiv:2602.06553** (February 2026) [P]. AlphaEvolve searches for lexicographic ranking functions on a toy blowup simulator in dimension 4, char 3, on the family $z^3 + g + z^2 h$ (benchmarks of 71, then 100 cases). It finds a 5-component ranking with bounded-delay descent and states two conjectures. Not a proof, and the simulator has a restricted class of centres. This is the closest published work to the lab of document 13, and its two conjectures are the first nodes of kind `conjecture` on route R5.
- Bérczi-Fan-Zeng, arXiv:2307.00252 (ICML 2023 workshop): reinforcement learning on Hironaka's polyhedra game [P]. Bérczi-Hashemi-Klüver, arXiv:2411.00566 [U].
- No AI-generated claimed proof of char $p$ resolution was found.

## 1.10 Lean: what exists

| Project | What it has | Licence, date | Tag |
|---|---|---|---|
| resolutionorg/hironaka | char 0 Hironaka, Kollár, Włodarczyk, Bierstone-Milman, algebraic and analytic; comparator CI; written by Claude agents operated by Resolution | Apache-2.0; 2026-09-30 to 2026-10-20; Lean v4.35.0 | [P], read and measured (document 05); the code is not yet audited by the project |
| riemann-lean, `Development/ResolutionOfSingularities` | a second, independent char 0 proof | no licence; 2026-11-20; Lean v4.33.1 | [P] (document 05) |
| AxiomMath/Stacks | `StacksCore` (reviewed by people) and `StacksFrontier` (written by models, not reviewed), about 64,000 modules; blowups, `IsRegular`, `IsExcellent`, `IsNagataRing`, `IsModification`, `IsAlteration`; resolution of excellent surfaces (Stacks tag 0BGK, Lipman) | Apache-2.0; 2026-11-04 | [P] for licence and date, [S] for content |
| AxiomMath/MMP | minimal model program in dimension $\le 4$, char 0 | Apache-2.0; 2026-11-16 | [S] |
| google-deepmind/formal-conjectures | `Scheme.HasResolution` and `resolution_of_singularities` (perfect field, research open), solved variants `_of_charZero`, `_of_topologicalKrullDim_le_three`, `exists_not_hasResolution_of_not_perfectField`; `LocalUniformization.lean` | Apache-2.0 | [P] |
| Mayeux, arXiv:2609.28489 (August 2026, v2 November), code `rndmx/MULTI-PROJ-BLOW` | "Projective blowups: a formal and multicentered proof", which claims the first formalization of blowups in a proof assistant | | [P] abstract; its date is before the hironaka repository and the riemann-lean release, so the claims do not conflict, but the three blowup APIs should be compared (06.5, risk 3) |
| daattavya98/HironakaLean-public, MingchenXia/Hironaka-lean | smaller projects; the second claims de Jong's theorem | Apache-2.0 | [S]; to read before node T7 |

**Mathlib** on 2026-11-23 has `Scheme.IdealSheafData`, `Hom.smoothLocus`, `IsRegularLocalRing`, `topologicalKrullDim`, `IsProper`, `Smooth`, `Scheme.BirationalOver`, normalization and `Ideal.reesAlgebra`. It does not have blowups, regular schemes, excellence, Cartier divisors, Cohen-Macaulay rings (open PRs only, for example #26218), Hilbert-Samuel functions, Hasse-Schmidt derivations on schemes, or the Zariski-Riemann space (PR #31938 was closed). Open PRs on regular local rings include #28683, #35561, #29802, #46021 and #39510; on Cartier divisors and Pic, #44200; on the Cohen structure theorem, #44551 and #44577 [S]. Document 07 turns this into tier T1.

**Lean tooling.** Lean v4.36.0 is the current stable release, and v4.37.0-rc1 is on master. Since v4.35 there are `lake check`, `lake comparator` and the `--paranoid` mode, which replays in the independent checkers (lean4lean, nanoda and others) [S]. The Mathlib Initiative's `formalization.yaml` schema (v0.4, used by hironaka) and the Palomar registry record formal statements and their sources [P/S]. verso-blueprint is the blueprint tool of the newer projects [S]. A run of kernel soundness bug reports in July and August 2026 (the "Summer of Soundness Bugs") is the reason for the second kernel check of 14.1 [S].

## 1.11 Large formalizations and AI provers in 2026

[S] for all items of this section, from searches made on 2026-11-23.
- Fermat's Last Theorem: `anthropics/fermats-last-theorem`, September 2026.
- The Riemann Hypothesis: the riemann-lean release of 2026-11-20 (Levent Alpöge), a Lean FRO statement of 2026-11-21, and the Xena checklist post of 2026-11-12 on how to check such a claim.
- `openai/math`: 722 manuscripts, among them the termination of lc flips for fourfolds.
- Provers: AlphaProof (Nature 2025), Aristotle, Seed-Prover 1.5, Goedel-Prover-V2, Gauss (sphere packing).
- Mathlib had about 2,700 open pull requests in October 2026.

The lesson for this project: the formalization of a known proof is no longer the bottleneck. The bottlenecks are three. The statement must be faithful (06.3). The proof must be read by a person (14.1, Q7). And new mathematics is still needed for the open case (04).

## 1.12 What the project takes from this

1. The library has a licensed char 0 base and many formal statements to bridge to (05, 06.4). Tier T1 still has large gaps in Mathlib.
2. The obstruction list of 1.6 is the first test suite of the lab (E2): every candidate invariant must survive it.
3. The active research lines of 2024 to 2026 are four: Samuel slope invariants (Benito-Bravo-Encinas), corrected residual orders (Hauser-Perlega), the Dream framework and weighted methods in char $p$ (Temkin; Abramovich-Quek-Schober), and defect theory (Kuhlmann; Cutkosky). They set the first weights of the routes (04).
4. Bérczi's AlphaEvolve work shows that a search for ranking functions in dimension 4 is feasible at a small scale. The project's lab does the same at a larger scale, with certificates and Lean proofs.
5. The claimed proofs (1.2) are checked only by the cheap method of 1.2: refute a key lemma on a certified example, or leave it alone.
