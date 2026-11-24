---
title: The route report
description: The state of the nine routes R1 to R9 at milestone S7, with the Lean status of each node, the negative results and the smallest next step in Lean.
lead: Resolution of singularities in dimension 4 in characteristic p is an open problem. No route is close to a proof. This report says what each route has, what is known to fail, and which small node in Lean comes next.
---
## How to read this report

The routes are in `blueprint/routes.yaml` and in spec 04 of the project. The [routes](/routes/) page lists them. This report is the first route report of spec 04, section 4.11. It is for milestone S7.

The Lean status of each node comes from the record of the map, `records/lean.json`, at commit 80e2938 of singularity-lean, on 2026-11-24. The map then has 109 nodes: 56 proved, 1 proved with a named hypothesis, 13 defined, 7 stated, 5 open and 27 planned. The node pages always show the current status. This page does not change when the record changes.

The words for the status are the words of the map. A node is *planned* when it has no Lean statement in the library. It is *stated* when the library has the statement and no proof. It is *defined* when the library has the definition. It is *proved* when the library has a proof with no axiom other than `propext`, `Classical.choice` and `Quot.sound`. It is *proved-mod* when the proof has a named hypothesis. It is *open* when it is a conjecture of the map.

The citations are keys of the [papers](/paper/) of the map. This report gives a section or a theorem number only when a node note of the map gives it.

## The common core

Every route meets the purely inseparable core $z^q + F(x_1, \dots, x_n)$ with $q = p^e$ and $n = 4$. The problem P1 asks for a resolution of the reduced hypersurface $z^p + g = 0$. It is the conjecture [SG00000009](node:SG00000009), status open. The library proves that P1 in dimension $n$ follows from resolution in dimension $n$ ([SG0000001X](node:SG0000001X), proved, `Singularity.purelyInseparableHypersurfaceResolution_of_resolutionInDim`). So P1 is a special case of the open problem, and not a way around it.

## R1. Characteristic polyhedra

Weight 0.25.

**Idea.** Hironaka's characteristic polyhedron of $f$ is the intersection of the projected Newton polyhedra of $f$ over all choices of $z$ that keep the form of $f$ ([Hir67](paper:Hir67)). It does not depend on the choice of $z$ ([CJSch19](paper:CJSch19)). Cossart-Jannsen-Saito used it to resolve excellent surfaces ([CJS20](paper:CJS20)). Cossart-Piltant used it to resolve threefolds in every characteristic ([CP08](paper:CP08), [CP09](paper:CP09)) and arithmetic threefolds ([CP14](paper:CP14), [CP19](paper:CP19)).

**Key steps and nodes.**

- The Newton polyhedron, [SG00000011](node:SG00000011): defined (`Singularity.newtonPolyhedron`). The library proves that the order is the least total degree on the polyhedron (`Singularity.isLeast_sum_newtonPolyhedron`).
- The characteristic polyhedron, [SG00000014](node:SG00000014): planned. The planned name `Singularity.characteristicPolyhedron` is not in the library.
- Hironaka's polyhedra game, [SG00000012](node:SG00000012): planned ([Spi83](paper:Spi83), [Zei06](paper:Zei06)).
- The Hilbert-Samuel function, [SG0000000Q](node:SG0000000Q): defined. Its laws, the theorem of Hilbert and Serre, the Hilbert-Samuel polynomial and the laws of the multiplicity are proved ([SG0000002D](node:SG0000002D), [SG00000031](node:SG00000031), [SG00000032](node:SG00000032), [SG00000034](node:SG00000034)). A regular local ring has multiplicity one: proved ([SG00000037](node:SG00000037)).
- Bennett's theorem that the Hilbert-Samuel function does not go up under a permissible blowup, [SG0000000R](node:SG0000000R): planned ([Benn70](paper:Benn70)).
- The order does not go up under a point blowup, [SG0000003A](node:SG0000003A): proved (`Singularity.ord_le_of_pointChart`). The points of the same order lie in the directrix, [SG0000003B](node:SG0000003B): proved (`Singularity.mem_directrix_of_ord_pointChart_eq`).

**Obstructions and negative results.** After the first invariants, Cossart-Piltant reduce to $z^p + g(x, y, w)$ and control the polyhedron with invariants that are special to three variables. In four variables no invariant of the projected polyhedron is known to go down. The preparation that computes the polyhedron can need infinitely many changes of coordinates, and it does not work well with étale localization. So a good local invariant does not yet give a global centre (spec 04, section 4.2).

**Next step.** The smallest new node is the characteristic polyhedron of $z^q + F$ with $F$ clean, that is, with no exponent in $q\mathbb{N}^n$. A change $z \mapsto z + h(x)$ gives $z^q + (F + h^q)$ in characteristic $p$. The support of $h^q$ is in $q\mathbb{N}^n$, so it does not meet the support of $F$, and the Newton polyhedron of $F + h^q$ contains that of $F$. Thus the polyhedron over these changes is $\frac{1}{q} N(F)$, and its least total degree is $\operatorname{ord}(F)/q$. This argument is not yet in Lean. It needs only `Singularity.newtonPolyhedron`, `Singularity.IsClean` and the Frobenius. It gives SG00000014 for this class, and it joins R1 to R5.

## R2. Local uniformization and patching

Weight 0.2.

**Idea.** Zariski's plan has two steps. First, local uniformization: for each valuation, find a model on which the centre of the valuation is regular. Second, patching: the Zariski-Riemann space is quasi-compact, so finitely many local solutions cover it, and they must be glued into one regular model ([Zar40](paper:Zar40), [Zar44](paper:Zar44)). Abhyankar did both for surfaces in every characteristic ([Abh56](paper:Abh56), [Abh66](paper:Abh66)). Cossart-Piltant proved local uniformization in dimension 3 in every characteristic ([CP08](paper:CP08), [CP09](paper:CP09)).

**Key steps and nodes.**

- The Zariski-Riemann space is quasi-compact, [SG0000000X](node:SG0000000X): proved.
- The Abhyankar inequality, [SG0000000Y](node:SG0000000Y): proved (`Singularity.abhyankar_inequality`).
- Key polynomials, [SG0000000Z](node:SG0000000Z): defined ([Mac36](paper:Mac36), [Vaq07](paper:Vaq07), [HMOS22](paper:HMOS22)). The library proves parts 1 and 2 of the theorem of MacLane-Vaquié, the first claim of part 3, and the step of part 4 (`Singularity.exists_keyPolynomial_augmentedValuation`). The claim on the graded algebra, the convergence of the chain and the limit augmentations are not in Lean.
- The defect of an extension, [SG00000010](node:SG00000010): planned ([Kuh-book](paper:Kuh-book)).
- Local uniformization of Abhyankar valuations, [SG0000001E](node:SG0000001E): stated (`Singularity.localUniformization_abhyankar`), no proof ([KK05](paper:KK05), [Cut20](paper:Cut20)).
- Local uniformization in dimension 3, [SG0000001F](node:SG0000001F): stated (`Singularity.localUniformization_three`), no proof ([CP08](paper:CP08)). The library proves the cases of transcendence degree 0 and 1 for each $p$ (`Singularity.localUniformizationInDim_zero`, `Singularity.localUniformizationInDim_one`).
- Inseparable local uniformization, [SG0000001G](node:SG0000001G): stated (`Singularity.localUniformization_inseparable`), no proof ([Tem13](paper:Tem13)).
- Local uniformization in dimension 4, [SG0000001H](node:SG0000001H): open. The Lean statement is `Singularity.LocalUniformizationFour`.
- Patching in dimension 4, [SG0000001J](node:SG0000001J): open. The Lean statement is `Singularity.resolution_of_localUniformization_four` ([Pil](paper:Pil)).

**Literature in every dimension.** Local uniformization reduces to valuations of height one ([Tem23](paper:Tem23), [NS14](paper:NS14)). Each valuation has local uniformization after a finite extension of the function field ([KK09](paper:KK09)), and after a purely inseparable extension ([Tem13](paper:Tem13)). Valuations have tight extensions to the completion ([HOST26](paper:HOST26)).

**Obstructions and negative results.** The first obstruction is defect. Kuhlmann classifies the Artin-Schreier defect extensions ([Kuh10b](paper:Kuh10b), [Kuh16](paper:Kuh16)). In the setting of Cutkosky-Mourtada, defect is the only obstruction ([CM17](paper:CM17)). Cutkosky-Kuhlmann-Rzepka characterize independent defect with the relative Kähler differentials ([CKR25](paper:CKR25)). So the hard case is dependent Artin-Schreier defect in transcendence degree 4. Local monomialization fails in characteristic $p$ ([Cut15](paper:Cut15)), so the method of characteristic 0 does not carry over. The second obstruction is patching. No patching theorem in dimension 4 is known in any characteristic. Thus R2 needs two new theorems, SG0000001H and SG0000001J.

**Next step.** The smallest new node is the definition of the defect of a finite extension of valued fields (SG00000010), with one Artin-Schreier extension of defect $p$ as a certified example. Volume 9 of the handbook has defect examples in its chapter on failures. A Lean proof of SG0000001E in a small case would be the next larger step.

## R3. Rees algebras, elimination and idealistic filtrations

Weight 0.15.

**Idea.** Replace the marked ideal of characteristic 0 by an object that is stable under all differential operators. Villamayor and his school use Rees algebras with the Hasse-Schmidt operators and an elimination algebra in place of a hypersurface of maximal contact ([Vil07](paper:Vil07), [Vil08](paper:Vil08), [BV10](paper:BV10)). Kawanoue-Matsuki use idealistic filtrations ([Kaw07](paper:Kaw07), [KM10](paper:KM10), [KM16](paper:KM16)). Both reduce resolution to an end case.

**Key steps and nodes.**

- Hasse-Schmidt derivations, [SG0000000W](node:SG0000000W): planned ([HSDer](paper:HSDer)). The planned name `Singularity.HasseDeriv` is not in the library.
- Maximal contact fails in characteristic $p$, [SG00000018](node:SG00000018): proved (`Singularity.Examples.narasimhan`, [Nar83](paper:Nar83)).
- The Samuel slope characterizes regularity, [SG00000019](node:SG00000019): planned ([BBE24](paper:BBE24), [BBE25](paper:BBE25)).

**Literature.** Both programs resolve surfaces. Benito-Villamayor give an invariant in characteristic $p$ that does not go up ([BenV13](paper:BenV13)). The Nash multiplicity sequence is an invariant in every characteristic ([BEP](paper:BEP)). Giraud studied what remains of maximal contact in positive characteristic ([Gir75](paper:Gir75)).

**Obstructions and negative results.** Narasimhan's example is the key negative result. In characteristic 2, let $f = x^2 + y z^3 + z w^3 + y^7 w$. The curve $(t^{32}, t^7, t^{19}, t^{15})$ is in the locus of order 2 of $f$, and no power series of order 1 vanishes on it. Thus no smooth hypersurface germ, also no formal one, contains the points of order 2. The Lean proof covers the formal statement (`Singularity.Examples.two_le_order_of_subst_eq_zero`). The step to the étale statement is not in Lean. In characteristic $p$, the end case of these programs is not monomial. An inseparable equation such as $z^p + g$ remains, and the elimination algebra forgets it. This is the core of R5.

**Next step.** The smallest new node is a positive partner of Narasimhan's example. Let $f = z^m + \sum_{k \le m-2} a_k(x) z^k$ have order $m$, with $m$ a unit in $k$. The coefficient of $z^{m-1}$ in $f(X + b)$ is $m b_z$, so each rational point of order at least $m$ has $b_z = 0$. Thus $z = 0$ has maximal contact at these points. This form is the form of Tschirnhausen. In the chart of $x_j$ of a point blowup, $a_k = x_j^{m-k} a_k'$ and the strict transform is $z'^m + \sum_{k \le m-2} a_k' z'^k$, so the form is kept. The lemma is not yet a node and not in Lean. It is the derivative argument of Target T in spec 04, section 4.12, for $p > m$. In Narasimhan's example $m = p = 2$, so the lemma does not apply.

## R4. Weighted and cobordant blowups

Weight 0.1.

**Idea.** In characteristic 0, one weighted blowup with a canonical centre lowers a simple invariant ([ATW24](paper:ATW24), [ATW20](paper:ATW20), [McQ20](paper:McQ20)). Cobordant blowups do the same with torus actions ([Wlo-cob](paper:Wlo-cob)). The centre comes from derivatives and maximal contact.

**Key steps and nodes.**

- Resolution by weighted blowups, [SG0000001Q](node:SG0000001Q): planned.
- A weighted invariant in characteristic $p$, [SG0000001R](node:SG0000001R): planned. It is a research target.
- Hironaka's theorem in characteristic 0, [SG0000001P](node:SG0000001P): proved-mod (`Singularity.resolutionInDim_charZero`).

**Literature in characteristic $p$.** Weighted methods work for plane curves ([AQS24](paper:AQS24)), binomial varieties ([AS22](paper:AS22)), toroidal varieties ([Wlo22](paper:Wlo22)) and torus actions over non-perfect fields ([AQS25](paper:AQS25)). Temkin's dream resolution needs only enough derivations ([TemD1](paper:TemD1), [TemD2](paper:TemD2)). Posva gives a candidate source of derivations ([Pos24](paper:Pos24)). Abramovich gives remarks on characteristic $p$ ([Abr25](paper:Abr25)).

**Obstructions and negative results.** The centre uses a hypersurface of maximal contact, and Narasimhan's example (R3) shows that none exists in general. Pinch points in characteristic 2 have no weighted resolution that keeps normal crossings ([AT26](paper:AT26)). The tangent space of the stack can grow ([AQS24](paper:AQS24)). Spec 01 lists a third failure, for Whitney's umbrella in characteristic 2.

**Next step.** The combinatorics of weighted blowups does not depend on the characteristic. The smallest new node is the weighted blowup of affine space in its charts, as explicit maps of polynomial rings, with the transform of a monomial. A weighted invariant for $p$ larger than the multiplicity would use the lemma of R3. Stacks are not in Mathlib, so the full statement of SG0000001Q is far.

## R5. The purely inseparable core

Weight 0.15.

**Idea.** The core is $z^q + F$ with $F$ clean. The residual order is the order of $G$ in $F = \prod x_i^{r_i} G$ along the divisor. It can go up under a permissible blowup. Moh bounded the increase ([Moh87](paper:Moh87)). Hauser called the points where it goes up kangaroo points ([Hau08](paper:Hau08)), and Hauser-Perlega characterized them ([HP19b](paper:HP19b)). Hauser-Wagner found a correction term for two variables ([HW14](paper:HW14)), and Hauser-Perlega resolved surfaces in 3-space with a modified residual order ([HP24](paper:HP24)). Hauser-Schicho made the problem a game ([HSch12](paper:HSch12)). Bérczi gives two conjectures ([Ber26](paper:Ber26)).

**Key steps and nodes.**

- Purely inseparable hypersurfaces (P1), [SG00000009](node:SG00000009): open. The Lean statement is `Singularity.PurelyInseparableHypersurfaceResolution`.
- The residual order, [SG00000013](node:SG00000013): defined (`Singularity.residualOrder`, `Singularity.residualOrderAlong`).
- Moh's one-step bound, [SG00000015](node:SG00000015): proved for point blowups in the given coordinates (`Singularity.moh_bound_holds`, tamnd/singularity-lean#78). The proof needs no hypothesis on the coordinates. The bound for larger permissible centers is not proved.
- A kangaroo point, [SG00000016](node:SG00000016): proved (`Singularity.Examples.kangaroo`, `Singularity.Examples.kangaroo_increase`).
- One cycle of Hauser-Perlega, [SG00000039](node:SG00000039): proved (`Singularity.Examples.hauserPerlegaCycle`).
- The Hauser-Perlega cycle, [SG00000017](node:SG00000017): planned. The Lean statement is not in the library.

**Obstructions and negative results.**

- The kangaroo point of [HP19a](paper:HP19a), Section 3. In characteristic 2, $F = x^2 y^2 w^3 (w (x+y)^4 + x^{13})$ with $q = 4$. In the $x$-chart with $y \mapsto y + 1$ the residual order goes from 5 to 7. The increase is $p^{e-1} = 2$, so Moh's bound holds. The bound 6 that the proof of Moh uses fails. Lean proves both facts.
- The false stability theorem. Moh's stability theorem is false for $e \ge 3$ ([HP19a](paper:HP19a), Section 4). The library certifies one cycle for $z^8 + x^4 y^4 w^6 (w^2 + x^3 u^{10})$: 20 point blowups with one cleaning keep the order 8, and the final equation has the starting shape with $d = 4$ in place of $d = 2$. The library does not prove that the residual order goes to infinity when the cycle is repeated. That is SG00000017.
- The lab. The runs E1 and E2 make about 26 million point blowups for $p = 2, 3, 5, 7$ and $n = 2, 3, 4$. No step goes over $p^{e-1}$, and in most cases of the runs the largest increase is equal to $p^{e-1}$ ([e1-p2](/lab/2026-11-24-e1-p2-90966cbf/), [e1-p3](/lab/2026-11-24-e1-p3-08768f1a/), [e1-p5](/lab/2026-11-24-e1-p5-54c44a97/), [e1-p7](/lab/2026-11-24-e1-p7-b358a69f/)). All five candidate secondary invariants of E2 go up at some step ([e2-p2](/lab/2026-11-24-e2-p2-9d8af676/), [e2-p3](/lab/2026-11-24-e2-p3-e8d7d250/), [e2-p5](/lab/2026-11-24-e2-p5-4b5722b1/), [e2-p7](/lab/2026-11-24-e2-p7-9cf24d69/)). The rounded bound of the proof of Moh fails at 111 steps for $p = 2$ and at 30 steps for $p = 3$, all with $q > p$, and at no step for $p = 5$ and $p = 7$. This agrees with [HP19a](paper:HP19a). The random walks do not find the cycle of Hauser-Perlega. The lab computes in the given coordinates at points over $\mathbb{F}_p$ only, and its data proves nothing.
- The open part. No invariant is known that, after the residual order, pays for the increases at kangaroo points when $g$ has 3 or more variables.

**Next step.** Moh's bound for point blowups is now proved for each $e$, so the case $e = 1$ needs no separate work. The next node is SG00000017 for one family of parameters, by induction on the cycle. A second candidate is Moh's bound for a permissible center of dimension 1.

## R6. Alterations and descent

Weight 0.05.

**Idea.** De Jong's theorem gives a regular $Y$ and a proper, surjective and generically finite map $Y \to X$ ([dJ96](paper:dJ96)). Gabber made the degree prime to a given $\ell \neq p$ ([ILO14](paper:ILO14)). Temkin made the degree a power of $p$ ([Tem17](paper:Tem17)). If the alteration is Galois with group $G$, then $X$ is birational to $Y/G$, so a resolution of $Y/G$ is enough.

**Key steps and nodes.** De Jong's alterations, [SG0000001K](node:SG0000001K): planned. Gabber's alterations, [SG0000001M](node:SG0000001M): planned. Temkin's $p$-alterations, [SG0000001N](node:SG0000001N): planned.

**Obstructions and negative results.** Quotients by groups of order prime to $p$ are tame and toroidal methods handle them. Quotients by $p$-groups are wild, and their resolution is as hard as the general case. Temkin's theorem puts all of the difficulty into $p$-groups, but it does not remove it. Nobody has proposed a way to resolve wild quotients in dimension 4.

**Next step.** The smallest new node is the Lean statement of SG0000001K, with a definition of an alteration. A proof is far. Quotients of a regular 4-fold by $\mathbb{Z}/p$ are a class where R5 and R6 meet (spec 04, section 4.7).

## R7. Toric, arc and non-archimedean methods

Weight 0.05.

**Idea.** Teissier's program embeds a singularity in a toric variety through a valuation and its generators, and asks that an overweight deformation of a toric variety be resolved by a toric resolution ([Tei03](paper:Tei03), [Tei14](paper:Tei14)). Tevelev proved a case ([Tev14](paper:Tev14)), and the tight extensions of [HOST26](paper:HOST26) remove one hypothesis. Mourtada-Schober propose Teissier singularities as a characteristic $p$ analogue of quasi-ordinary singularities ([MS25](paper:MS25)).

**Key steps and nodes.** Toric resolution, [SG0000001T](node:SG0000001T): planned ([KKMS](paper:KKMS), [Ful93](paper:Ful93)). The conjecture of Teissier is not yet a node.

**Obstructions and negative results.** The embedding can need infinitely many generators. These methods give local uniformization only in special cases. No step of the program in dimension 4 has a statement at a reasonable cost in Lean.

**Next step.** The smallest new node is shared with R9: a regular subdivision of a rational cone of dimension 2. After that, the conjecture of Teissier can be stated as a node of kind `conjecture`.

## R8. Mixed characteristic

Weight 0.0. The plan gives the route no research time.

**Idea.** Spread $X$ out over a $p$-adic ring and use the generic fibre, where resolution in characteristic 0 exists. Cossart-Jannsen-Saito and Cossart-Piltant resolved excellent surfaces and arithmetic threefolds ([CJS20](paper:CJS20), [CP14](paper:CP14), [CP19](paper:CP19)).

**Key steps and nodes.** Quasi-excellent schemes of dimension at most 3, [SG0000001V](node:SG0000001V): planned ([CP19](paper:CP19)).

**Obstructions and negative results.** A variety need not lift to a $p$-adic ring. A resolution of the generic fibre says nothing about the special fibre. The route is a source of methods and statements, not a direct route to varieties over a field.

**Next step.** The smallest new node is the Lean statement of SG0000001V. The project does not plan research time for it.

## R9. Special classes in every dimension

Weight 0.05.

**Idea.** Find classes of varieties of dimension 4 or more in characteristic $p$ with a structure that reduces resolution to a known case. Martínez-Núñez resolves varieties with a torus action of complexity at most 3: the quotient has dimension at most 3 ([MN26](paper:MN26)). Binomial and toroidal varieties have a resolution in every characteristic ([AS22](paper:AS22), [Wlo22](paper:Wlo22)).

**Key steps and nodes.** Binomial varieties, [SG0000001S](node:SG0000001S): planned. Toric resolution, [SG0000001T](node:SG0000001T): planned. The theorem of Martínez-Núñez is not yet a node.

**Obstructions and negative results.** These are the only unconditional resolution theorems in dimension 4 or more in characteristic $p$. They do not reach the general case, because no method produces the torus action or the binomial structure.

**Next step.** The smallest new node is the combinatorial core of SG0000001T in dimension 2: each rational cone of dimension 2 has a regular subdivision. It needs no algebraic geometry. The statement of the theorem of Martínez-Núñez, with resolution in dimension 3 as a hypothesis, would follow.

## The ranking by the next feasible step

The ranking is by the size and the value of the next node in Lean. It is not a ranking by the distance to a proof. Each route is far from a proof.

1. R5. The definitions, the point blowup charts, two certified examples and Moh's bound for point blowups are in Lean. The next targets are the unbounded cycle SG00000017 for one family and Moh's bound for a center of dimension 1.
2. R1. The Newton polyhedron is in Lean. The characteristic polyhedron of $z^q + F$ with $F$ clean is a short argument. It gives the first piece of SG00000014 and joins R1 to R5.
3. R3, with R4. The lemma of Tschirnhausen for a unit order is short, and it is the positive side of Narasimhan's example. It is the first step toward Target T. Hasse-Schmidt derivations come next.
4. R2. Many nodes are proved, and local uniformization is proved in transcendence degree at most 1. The next node, the defect, is a definition and an example. The hard theorems SG0000001H and SG0000001J are far.
5. R9. The regular subdivision of a cone of dimension 2 is small, and it is the start of toric resolution. The route does not reach the general case.
6. R7. It shares the next node with R9. The program of Teissier has no Lean statement yet.
7. R4. The charts of a weighted blowup are small. The method needs stacks and maximal contact, and both are missing.
8. R6. The next node is a statement only. The wild quotients have no plan.
9. R8. The route has weight 0.

## What this report does not claim

The problem is open. No route is close to a proof. The project has proved no new theorem about resolution in dimension 4. The proved nodes are known results, certified examples and reductions. The three next nodes of the ranking are not proved. The lab data are examples, not proofs. The weights of the routes stay as in `blueprint/routes.yaml` until the lead changes them at a milestone report.
