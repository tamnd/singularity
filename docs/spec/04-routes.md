# 04. The routes to dimension 4

A route is a strategy for the open case. Each one has a published history, a key obstruction, and a first set of nodes that the project can state and work on now. The project runs several routes in parallel, because nobody knows which one works, and because the parts they share (tier T4 of document 07) are useful to all of them. This document fixes the routes, says what each one needs, and sets their first weights. The sources are in documents 01 and 07. Claims marked [U] are the project's own guesses and are not in the literature.

The routes are written for an expert reader. Section 3.3 has the failures of char 0 methods that they refer to (3.3.1 derivatives, 3.3.2 maximal contact, 3.3.3 residual order, 3.3.4 no functorial invariant, 3.3.5 defect, 3.3.6 imperfect fields).

## 4.1 Summary

| Route | Idea | Known up to | Key obstruction in dim 4 | First weight |
|---|---|---|---|---|
| R1 | Hironaka's characteristic polyhedra, after Cossart-Jannsen-Saito and Cossart-Piltant | dim 2 (all excellent), dim 3 (Cossart-Piltant) | the dim 3 proof uses projections to dimension 2 and case analysis that does not scale; no invariant known that drops for $z^p + g(x_1, \dots, x_4)$ | 0.25 |
| R2 | Valuations: local uniformization, then patching | dim 3 (Abhyankar for $p > 5$, Cossart-Piltant for all $p$); Abhyankar valuations in all dims (Knaf-Kuhlmann) | valuations with defect in dim 4; patching (Zariski's method) is known only up to dim 3 | 0.20 |
| R3 | Rees algebras, elimination, idealistic filtrations (Villamayor, Benito, Bravo, Encinas, Kawanoue, Matsuki) | dim 2 in all char; programs for all dims, with invariants defined but not shown to drop | the elimination algebra loses information in char p; the "monomial" end case is not monomial | 0.15 |
| R4 | Weighted and cobordant blowups (Abramovich-Temkin-Włodarczyk, McQuillan, Włodarczyk) | char 0, all dims | the weighted centre is defined from derivatives; in char p its invariant does not drop | 0.10 |
| R5 | The core case $z^p + g$: residual order, kangaroo points, secondary invariants (Moh, Hauser and coauthors) | surfaces (Hauser-Wagner, Hauser-Perlega) | find P2 of 3.4: an invariant that pays for the increases of the residual order | 0.15 |
| R6 | Alterations and descent | alterations exist in all dims (de Jong, Gabber, Temkin's $p$-alterations) | the quotient by a wild group (a $p$-group) is not known to have a resolution | 0.05 |
| R7 | Toric and arc methods: Teissier's overweight deformations, jet schemes, Berkovich spaces | some cases of local uniformization | a general reduction to the toric case in char p | 0.05 |
| R8 | Mixed characteristic and the generic fibre | dim 2 (Cossart-Jannsen-Saito), arithmetic threefolds (Cossart-Piltant) | a family over $\mathbb{Z}_p$ whose fibres are the variety; the special fibre does not follow | 0.00 (corpus only) |
| R9 | Special classes in every dimension: torus actions of small complexity, binomial and toroidal varieties | T-varieties of complexity $\le 3$ (Martínez-Núñez 2026), binomial (Włodarczyk 2022, Abramovich-Schober) | no general way to produce the torus action | 0.05 |

The weights set the share of the research budget of the agent (document 10.6) for the first year. They change at each milestone report, from the results (4.11).

## 4.2 R1: characteristic polyhedra

**Idea.** For $f \in R = k[[x_1, \dots, x_n, z]]$ of order $m$ with $\operatorname{in}(f) = z^m$ (or more generally a "directrix" in $z$), Hironaka's characteristic polyhedron $\Delta(f; x; z)$ is the intersection of the Newton polyhedra of $f$ over all choices of $z$ that keep the form. He proved that it exists and is computed by a "vertex preparation" in finitely many steps over a complete ring (1967). It is independent of the choice of $z$, and so is a good invariant. Cossart, Jannsen and Saito used it to give a canonical resolution of all excellent two-dimensional schemes. Cossart and Piltant used it, with a long analysis of projections, to resolve threefolds in every characteristic, and later arithmetic threefolds. Cossart, Jannsen and Schober proved that the polyhedron is intrinsic (arXiv:1805.10660), and Cossart and Schober gave a strictly decreasing invariant in dimension 2 and removed the need for completion. Abramovich's 2025 notes name the hypersurface that realizes the characteristic polyhedron as the char $p$ replacement for maximal contact.

**What works in dim 4.** The polyhedron exists in every dimension. The first invariants (the Hilbert-Samuel function, the directrix, the dimension of the ridge) are defined in every dimension and do not go up under permissible blowups, by Hironaka and by Cossart-Jannsen-Saito.

**Key obstruction.** In dimension 3, after the first invariants, Cossart-Piltant reduce to $z^p + g(x, y, w)$ and control the polyhedron with explicit invariants (the slopes of the polyhedron and projections to two variables). Their argument checks cases that are special to three variables. In four variables the polyhedron projects to a three-dimensional polyhedron and there is no known invariant of it that drops. The well-preparation that computes the polyhedron can need infinitely many coordinate changes, and it is not compatible with étale or smooth localization in high dimension, so even a good local invariant does not give a global centre.

**First nodes.**
1. The characteristic polyhedron: definition, existence by vertex preparation, independence of $z$ (Hironaka 1967; Cossart-Schober for the non-complete case). Tier T4.
2. The non-increase of the Hilbert-Samuel function under permissible blowups (Hironaka, Bennett, Singh). Tier T4.
3. The Cossart-Piltant invariants for $n = 3$, stated in Lean, and their dimension 4 analogues stated as conjectures, each with a lab experiment (E4 of 13.3).

**What success looks like (G4).** A new invariant for $z^p + g(x_1, \dots, x_4)$, defined from the polyhedron, that drops under a canonical choice of centre in a class of cases bigger than the known ones (for example $g$ with a Newton polyhedron with one compact face).

## 4.3 R2: local uniformization and patching

**Idea.** Zariski's two-step plan. Step 1, local uniformization: for each valuation $v$ of $K = k(X)$ centred on $X$, find a modification $X' \to X$ whose centre of $v$ is a regular point. Step 2, patching: the Zariski-Riemann space is quasi-compact, so finitely many local solutions cover it, and they must be glued into one global regular model. Zariski did both in char 0 for dimension at most 3. Abhyankar did both for surfaces in all characteristics and for threefolds with $p > 5$. Cutkosky gave a shorter proof of Abhyankar's threefold theorem. Cossart and Piltant proved local uniformization in dimension 3 in all characteristics and patched the local solutions with the combinatorics of dimension 3 (J. Algebra 2008, 2009).

**What is known in every dimension.**
- Abhyankar valuations (those with equality in the Abhyankar inequality) admit local uniformization (Knaf-Kuhlmann 2005, with a separable residue field extension; Cutkosky, arXiv:2003.06374, without it).
- Local uniformization reduces to valuations of height one (Temkin, arXiv:2301.09160; Novacoski-Spivakovsky).
- Valuations have tight extensions to the completion (Herrera Govantes-Olalla Acosta-Spivakovsky-Teissier, arXiv:2607.11223, July 2026), a step that Teissier's program (R7) needed.
- Every valuation admits local uniformization after a finite extension of the function field (Knaf-Kuhlmann 2009), and after a purely inseparable extension (Temkin 2013, "inseparable local uniformization").
- De Jong's theorem gives local uniformization after a generically finite extension.

**Key obstructions.**
1. *Defect.* For a valuation with defect in an extension of degree $p$ (an Artin-Schreier or purely inseparable extension where $e f < [L : K]$), the char 0 arguments fail. Kuhlmann's classification of defects (dependent and independent) and his theory of tame and deeply ramified fields tell which defects are the hard ones. Cutkosky-Mourtada (arXiv:1711.02726) show that, in their setting, defect is the only obstruction, and Cutkosky-Kuhlmann-Rzepka (2025) characterize independent defect by the vanishing of the relative Kähler differentials. So the hard case is dependent Artin-Schreier defect in towers of transcendence degree 4. Cutkosky's 2015 examples show that local monomialization fails in char p, so the char 0 strategy of Cutkosky for local uniformization does not carry over.
2. *Patching in dimension 4.* Zariski's patching uses the fact that, in dimension at most 3, the local solutions can be made compatible by further blowups whose centres are controlled. In dimension 4 no patching theorem is known, in any characteristic, without a global algorithm. In char 0 the global algorithm (Hironaka) made patching unnecessary. So route R2 needs two new theorems, not one.

**First nodes.**
1. Tier T2: valuations, the Zariski-Riemann space and its quasi-compactness, the Abhyankar inequality, key polynomials (MacLane, Vaquié, Herrera-Olalla-Mahboub-Spivakovsky, Novacoski), defect. Mathlib has valuations and Krull valuations, and no Zariski-Riemann space (PR #31938 was closed).
2. `localUniformization_abhyankar` (Knaf-Kuhlmann): a full formal proof is a milestone (S5).
3. Temkin's inseparable local uniformization, stated with its nodes.
4. Zariski's patching theorem in dimension $\le 3$, stated and then proved, so that the exact place where dimension 3 is used is in Lean. [U] A precise Lean statement of "patching in dimension $n$" as a separate open problem is itself useful: it splits `ResolutionDimFourCharP` into two named open nodes.

**What success looks like (G4).** Local uniformization in dimension 4 for a new class of valuations with defect (for example rank 1 valuations whose defect comes from one Artin-Schreier extension), or a patching theorem in dimension 4 under an extra hypothesis.

## 4.4 R3: Rees algebras, elimination and idealistic filtrations

**Idea.** Replace the marked ideal of char 0 by an object that is stable under all differential operators. Villamayor and his school use Rees algebras with the action of the Hasse-Schmidt differential operators, and an *elimination algebra* in place of the restriction to a hypersurface of maximal contact. Kawanoue and Matsuki use *idealistic filtrations* closed under differential operators and radical saturation (the IFP program), with the "leading generator system" in place of maximal contact. Both define invariants in every dimension and prove that resolution follows if a certain end case (the "monomial" case in char 0) can be solved.

**What works.** Both programs resolve surfaces. Benito and Villamayor gave a new invariant in char p and proved that it does not go up. Kawanoue and Matsuki have an invariant for 3-dimensional ambient spaces. The Nash multiplicity sequence (Lejeune-Jalabert, Hickel, and Bravo-Encinas-Pascual-Escudero) is a char-free invariant that refines the multiplicity. Benito, Bravo and Encinas defined the asymptotic Samuel function (2024) and showed that the Samuel slope characterizes regularity (arXiv:2506.14993, 2025). These char-free invariants are the most promising replacement for the order of the coefficient ideal.

**Key obstruction.** In char p, the end case of these algorithms, where the invariants of char 0 are zero, is not monomial. It is a "small" or "bad" case where an inseparable equation like $z^p + g$ remains and the elimination algebra has forgotten it. Solving the end case in dimension 4 is the open problem for this route. It is close to R5.

**First nodes.**
1. Hasse-Schmidt derivations and differential operators on smooth $k$-algebras in char p (tier T1, a gap in Mathlib).
2. Rees algebras with a differential structure, their integral closure, and the closure under differential operators (Villamayor; Kawanoue).
3. The Nash multiplicity sequence, its upper semi-continuity, and its behaviour under blowups.
4. Benito-Villamayor's invariant and its non-increase.
5. The asymptotic Samuel function and the Samuel slope, with the theorem that the slope characterizes regularity.

**What success looks like (G4).** The end case of the Villamayor or Kawanoue-Matsuki program solved in dimension 4 for $p$ in a range, or a counterexample that shows a published conjecture of this route is false.

## 4.5 R4: weighted and cobordant blowups

**Idea.** In char 0, Abramovich, Temkin and Włodarczyk, and McQuillan, found that one weighted blowup with a canonical centre $J = (x_1^{a_1}, \dots, x_k^{a_k})$ lowers a simple invariant $(a_1, \dots, a_k)$, which gives a very short algorithm with no history. Włodarczyk's cobordant blowups do the same with smooth torus actions. The centre is still found with derivatives and maximal contact.

**What is known in char p.** Weighted methods work in char $p$ for plane curves (Abramovich-Quek-Schober, arXiv:2412.16426), binomial varieties (Abramovich-Schober, arXiv:2208.08951), toroidal varieties (Włodarczyk, arXiv:2007.13846) and torus actions over non-perfect fields (arXiv:2507.01232). Temkin's "Dream resolution" (arXiv:2503.18205, 2507.11698) shows that weighted resolution needs only "enough derivations", which names the one axiom that char $p$ lacks. Candidates to supply it are Hasse-Schmidt derivations and $p$-closed foliations (Posva, arXiv:2405.05735).

**What might survive.** The *combinatorics* of weighted blowups (stacky Proj, toric charts, the invariant as a sequence of rational numbers) is characteristic free. The question is how often the char 0 centre still makes the invariant drop in char p, and what goes wrong when it does not. This is experiment E7 of 13.3. [U] A weighted centre adapted to the characteristic polyhedron of R1 is a hybrid of R1 and R4 that nobody has published, as far as the project knows.

**Key obstruction.** The admissibility of the weighted centre uses that the derivatives of order $a_i - 1$ of $f$ give a hypersurface of maximal contact. That fails in char p (3.3.2), and Narasimhan's example shows that no smooth hypersurface of maximal contact exists in general. Three char $p$ failures of the weighted method are now known (01, 1.6): the invariant is not semicontinuous for Whitney's umbrella in char 2; char 2 pinch points have no weighted resolution that keeps normal crossings (Abramovich-Temkin, 2026); and the tangent space of the stack can grow (Abramovich-Quek-Schober). Non-reduced stabilizers ($\mu_p$, $\alpha_p$) also appear.

**First nodes.** Temkin's Dream axioms, stated in Lean for a ring with a module of derivations, and the theorem that they imply resolution, in the form that does not need char 0. Weighted blowups and stack-theoretic Proj (the base and Mathlib do not have stacks; the project uses the coarse space and the toric charts, which suffices for statements). The ATW invariant, stated over any field.

**What success looks like (G4).** A theorem that the weighted method resolves a stated class of singularities in char p (for example hypersurfaces with $p$ larger than the multiplicity, which is char 0-like), or a characterization of the class where it fails.

## 4.6 R5: the purely inseparable core

**Idea.** By the reductions of 3.4, the core is a hypersurface
$$f = z^p + g(x_1, \dots, x_n)$$
(more generally $z^{p^e} + g$, or $z^p + a_1 z^{p-1} + \dots + a_p$) at a point of an $(n+1)$-dimensional regular ambient space, with $n = 4$ for the open case. Its *residual order* $\operatorname{ord}(g)$ after the best choice of $z$ (modulo $p$-th powers) is the natural second invariant. In char p it can go up under a permissible blowup. Moh bounded the increase. Hauser called the points where it goes up *kangaroo points*, and Hauser and Perlega characterized them. Hauser and Perlega found a cycle of point blowups along which the residual order keeps growing, which disproves Moh's stability theorem (arXiv:1802.05010). Hauser and Wagner found a correction term for $z^p + f(x, y)$, and Hauser and Perlega resolved surfaces in 3-space with a modified residual order (Publ. RIMS 2024). Hauser and Schicho made the problem a combinatorial game, which shows which parts are combinatorial. Bérczi (arXiv:2602.06553, 2026) used AlphaEvolve to find a 5-component lexicographic ranking function with bounded-delay descent on a simulator for $z^3 + g + z^2 h$ in dimension 4, and stated two conjectures. The exact form of Moh's one-step bound is a task for the `reader` role (01, 1.6).

**Why it is the center of the project.** Every other route meets this case. R1 meets it after the Hilbert-Samuel function and the directrix. R3 meets it as the end case. R4 fails on it. A good invariant for it in dimension 4 is the result that would most likely move the field. It is also the most computable case: $g$ is one polynomial, the blowups are explicit, and the lab can test millions of examples (E1, E2).

**Key obstruction.** P2 of 3.4: no invariant is known that, after the residual order, pays for the increases at kangaroo points in dimension $n \ge 3$ (three variables in $g$, the threefold case, is handled by Cossart-Piltant with other methods).

**First nodes.** Tier T4.
1. The order, the residual order and the coefficient ideal of $z^p + g$, as Lean definitions with computable versions over $\mathbb{F}_p$.
2. The transformation of $f$ under a point or a regular curve blowup in each chart, as explicit formulas (13.4).
3. Moh's one-step bound, stated and proved; the Hauser-Perlega cycle as a certified example (13.4).
4. Hauser-Perlega's characterization of kangaroo points.
5. Hauser-Wagner's correction and Hauser-Perlega's modified residual order for surfaces, and their monotonicity.
6. Bérczi's two conjectures, as nodes of kind `conjecture`, with lab experiment E8.
7. [U] A list of candidate secondary invariants for $n = 4$, each a node of kind `conjecture` with its lab test.

**What success looks like (G4).** P1 of 3.4 for $n = 4$ and $p$ in a range (for example $p > \deg g$, or $g$ with a non-degenerate Newton polyhedron), proved in Lean.

## 4.7 R6: alterations and descent

**Idea.** De Jong's theorem gives a regular $Y$ and a proper, surjective, generically finite $Y \to X$. Gabber made the degree prime to any $\ell \neq p$. Temkin made it a power of $p$ (a $p$-alteration). If the alteration is generically Galois with group $G$, then $X$ is birational to $Y/G$, and a resolution of $Y/G$ would follow from a resolution of quotient singularities.

**Key obstruction.** For a tame group (order prime to $p$), quotient singularities can be handled by toroidal methods. For a $p$-group the quotient singularities are wild, and their resolution is as hard as the general case. Temkin's $p$-alteration theorem shows that only $p$-groups are left, which puts the difficulty in one place, but it does not remove it.

**Role in the project.** De Jong's theorem is a theorem the project formalizes for the library (G1 and G2), and the formal statement of "resolution of wild quotient singularities in dimension 4" is a named open node. The route gets a small weight because no one has proposed a way to resolve wild quotients in dimension 4. [U] Wild quotients $Y/(\mathbb{Z}/p)$ of a regular 4-fold are a class where R5 and R6 meet, because the quotient is locally an Artin-Schreier or purely inseparable cover.

## 4.8 R7: toric, arc and non-archimedean methods

**Idea.** Teissier's program: embed a singularity in a toric variety via a valuation and its generators (possibly infinitely many), and show that an "overweight deformation" of a toric variety can be resolved by the toric resolution. Tevelev proved a case of Teissier's conjecture, and the tight extension theorem of 2026 (R2) removes one of its hypotheses. Mourtada and Schober proposed "Teissier singularities" (arXiv:2502.01239) as the char $p$ analogue of quasi-ordinary singularities in Jung's method. Jet and arc schemes (Mourtada and others) read the resolution from the geometry of the space of arcs. Berkovich and adic spaces, used by Temkin, give a topological model of the Zariski-Riemann space.

**Role.** These give local uniformization in special cases and new invariants. The project states the key conjecture of Teissier (local uniformization of every valuation via overweight deformation) as a node and leaves the route at a low weight until a step can be stated in Lean at a reasonable cost.

## 4.9 R8: mixed characteristic

**Idea.** Spread $X$ out over a $p$-adic ring (it is not always possible, because $X$ need not lift) and use the generic fibre, where char 0 resolution exists. Cossart-Jannsen-Saito and Cossart-Piltant proved resolution for excellent surfaces and arithmetic threefolds, which include mixed characteristic.

**Key obstruction.** A resolution of the generic fibre says nothing about the special fibre. The route matters for the corpus (G1) and for the statements, and it is a source of methods (Cossart-Piltant's arithmetic threefolds), not a direct route to varieties over a field.

## 4.10 R9: special classes in every dimension

**Idea.** Find classes of varieties of dimension $\ge 4$ in char $p$ that have a structure that reduces resolution to a known case. Martínez-Núñez (arXiv:2611.18258, November 2026) resolves varieties with a torus action of complexity $\le 3$ equivariantly: the quotient has dimension $\le 3$, which Cossart-Piltant resolve, and the rest is toroidal. Włodarczyk and Abramovich-Schober resolve binomial and toroidal varieties in every characteristic.

**Role.** These are the only unconditional resolution theorems in dimension $\ge 4$ in char $p$. They are cheap targets for G4-sized formal results (they use the library of tiers T1 to T6 and the toric machinery), and they test the infrastructure on dimension 4 objects early. The route does not reach the general case, because no method produces the torus action.

**First nodes.** Toric resolution in every characteristic (KKMS) as a theorem of the library; the theorem of Martínez-Núñez, stated, with its dependence on `resolutionInDim_three` as a hypothesis.

## 4.11 The AI-assisted lab as a method, not a route

Every route uses the lab of document 13, and the agent of document 10. The method is the same on each route:

1. State the next step of the route as a Lean node of kind `conjecture`.
2. Test it in the lab on the families where it should hold (E1 to E7). A failure becomes a certified counterexample (13.4) and the node is `refuted`.
3. If it survives, give it to the `prover` role with a budget, and to the `planner` role to break it into lemmas.
4. Each month, the route report lists the nodes that were stated, refuted and proved, and the weight of the route moves toward the routes with proved new nodes.

A route is paused (weight 0) when it has had a year of budget with no new node proved or refuted, and an outside expert agrees that the obstruction is the one of 4.1. A paused route keeps its nodes on the map.

## 4.12 A candidate first target [U]

The analogy with Abhyankar's threefold theorem suggests a first research target. Abhyankar resolved threefolds for $p > 5$, which for a prime is the same as $p > 3! = 6$. [U] The reason, as the project reads it, is that in that range the ramification of the relevant valuations is tame and the multiplicities that occur are smaller than $p$. The dimension 4 analogue is:

> **Target T.** Resolution of singularities of 4-folds over an algebraically closed field of characteristic $p > N$, for an explicit $N$ (the analogy suggests $N = 4! = 24$).

This is not a known conjecture in this form, and the project does not claim that the analogy is right. It is a useful target for three reasons. If the extensions that the proof meets have degree at most $N$, then for $p > N$ they are tame and have no defect, so the hardest cases of R2 would not occur. Points of multiplicity $m < p$ behave as in char 0 (the derivative argument of 3.2 needs only that $m!$ is a unit), so the char 0 methods (R4) and the `IsUnit` form of the base (05.3) are close to working. Whether the bad points of a 4-fold can be pushed to multiplicity below $N$ is exactly what the target asks. And a proof of T with any $N$ would be the first resolution theorem in dimension 4 in positive characteristic. The first task on T is a check by an expert of whether Abhyankar's reason for $p > 5$ is the one stated here, and a search of the literature for a known obstruction to T. Both are tasks for milestone S3.
