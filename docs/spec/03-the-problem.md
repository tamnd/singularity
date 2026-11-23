# 03. The problem, mathematically

This document states the problem in its usual forms and shows how those forms are related. It then explains why the characteristic 0 proof does not carry over to characteristic p: each place where the proof breaks, with the example that shows it. Documents 04 (routes) and 06 (Lean statements) build on this one. Section 01.2 has the citations. Here a result is named by its authors and year only.

## 3.1 The statements

Throughout, $k$ is a field, $p = \operatorname{char} k$, and a *variety* is a reduced separated scheme of finite type over $k$. For a reduced scheme $X$, $\operatorname{Reg}(X)$ is the set of points $x$ where $\mathcal{O}_{X,x}$ is a regular local ring, and $\operatorname{Sing}(X)$ is its complement. A scheme of finite type over a field is excellent, so $\operatorname{Reg}(X)$ is open, and it is dense when $X$ is reduced.

**Definition 3.1 (Resolution).** A *resolution* of a reduced excellent scheme $X$ is a proper morphism $\pi : Y \to X$ such that

1. $Y$ is regular;
2. $\pi$ is an isomorphism over $\operatorname{Reg}(X)$;
3. $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.

Conditions 2 and 3 together make $\pi$ birational, and they rule out the trivial answers ($Y = \emptyset$, or $Y = \operatorname{Reg}(X) \sqcup Z$ with $Z$ a regular scheme over $\operatorname{Sing}(X)$). A resolution is *projective* if $\pi$ is projective. It is *by blowups* if $\pi$ is a composite of blowups $Y = X_r \to \cdots \to X_0 = X$ with centres $C_i \subset X_i$ that lie over $\operatorname{Sing}(X)$. Over a perfect field, "regular" is the same as "smooth over $k$". Over an imperfect field it is weaker, and regular is the right notion: a regular variety over an imperfect field need not have any smooth model (Section 3.3.6).

**Definition 3.2 (Strong or embedded resolution).** Let $X \subset M$ be a closed subscheme of a regular scheme. An *embedded resolution* is a sequence of blowups $M_r \to \cdots \to M_0 = M$ with regular centres $C_i$ such that each $C_i$ has normal crossings with the exceptional divisor $E_i$ of the earlier blowups, the strict transform $X_r$ of $X$ is regular, and $X_r$ has normal crossings with $E_r$. It is *strong* if each $C_i$ lies over $\operatorname{Sing}(X)$, so that nothing changes over $\operatorname{Reg}(X)$.

**Definition 3.3 (Principalization).** Let $M$ be regular, $E$ a simple normal crossings divisor on $M$, and $I \subset \mathcal{O}_M$ a coherent ideal that is not zero on any component. A *principalization* of $(M, I, E)$ is a sequence of blowups in regular centres that have normal crossings with the boundary, such that the total transform $I \mathcal{O}_{M_r}$ is the ideal of a simple normal crossings divisor that is supported on the new boundary $E_r$.

**Definition 3.4 (Local uniformization).** Let $X$ be an integral variety with function field $K$, and let $\nu$ be a valuation of $K/k$ with centre $x$ on $X$. *Local uniformization* of $\nu$ asks for a projective birational morphism $X' \to X$ such that the centre of $\nu$ on $X'$ is a regular point. *Embedded local uniformization* asks for the same for a given subvariety, in normal crossings form.

**Definition 3.5 (Alteration).** An *alteration* of an integral $X$ is a proper, surjective, generically finite morphism $Y \to X$ with $Y$ integral. De Jong (1996) proved that every variety over any field has an alteration from a regular variety. Gabber made the degree prime to any given $\ell \neq p$. Temkin (2017) made the degree a power of $p$.

### 3.1.1 How the forms are related

| From | To | How, and in which dimensions |
|---|---|---|
| Principalization in dim $n$ | embedded resolution of subvarieties of dim $< n$ | blow up, follow the strict transform; the usual "order reduction" argument, for all $n$, any char |
| Embedded resolution in ambient dim $n+1$ | resolution of hypersurfaces of dim $n$ | trivial |
| Embedded resolution of all $X \subset \mathbb{A}^N$ with compatible gluing | resolution of all varieties | needs the centres to be independent of the embedding (functoriality); in char 0 this is a theorem of the algorithm; in char p it is part of the problem |
| Resolution in dim $n$ | local uniformization in dim $n$ | trivial |
| Local uniformization of all valuations in dim $n$ | resolution in dim $n$ | Zariski's patching: proved for $n \leq 3$ (Zariski in char 0; Abhyankar, Cossart and Piltant in char p). **Open for $n \geq 4$ in char p.** |
| Resolution of all excellent schemes of dim $n$ in char p | resolution of varieties of dim $n$ | trivial; the converse needs Temkin's reduction, which is known in char 0 only |
| Resolution in dim $n$ | resolution in dim $n$ by blowups, strong | not automatic in char p; Cossart-Piltant give it in dim 3 |

The table has the most important structural fact for the project: **in dimension 4 and up, char p has two open problems, not one.** Local uniformization is open, and it is also open whether local uniformization implies resolution. A route that only proves local uniformization (document 04, routes R2 and R3) still has to solve the globalization problem.

### 3.1.2 What is known (short form)

| dim | char 0 | char p, over a field | mixed char / excellent |
|---|---|---|---|
| 1 | normalization | normalization | normalization (excellent) |
| 2 | Walker 1935, Zariski 1939 | Abhyankar 1956; Lipman 1978 for all excellent surfaces; embedded: Abhyankar, Cossart-Jannsen-Saito (canonical, 2009/2020) | Lipman 1978 |
| 3 | Zariski 1944 | Abhyankar 1966 ($p > 5$); Cossart-Piltant 2008/2009 (all $p$); Cutkosky 2009 simplified proof for $p > 5$ | Cossart-Piltant 2014/2019 (arithmetic threefolds) |
| $\geq 4$ | Hironaka 1964, then constructive and functorial proofs (Villamayor, Bierstone-Milman, Encinas-Hauser, Włodarczyk, Kollár, Abramovich-Temkin-Włodarczyk, McQuillan) | **open**; weak forms: alterations (de Jong, Gabber, Temkin), inseparable local uniformization (Temkin), Abhyankar valuations (Knaf-Kuhlmann) | quasi-excellent of char 0: Temkin 2008 |

Document 01 has the 2026 status, with sources. As of 2026-11-23 no proof for $\dim \geq 4$ in char p is accepted by the experts. Hironaka's 2017 manuscript is not accepted, and no gap-free version exists (document 01).

## 3.2 The characteristic 0 proof in one page

All modern proofs in char 0 have the same skeleton. It is worth stating it carefully, because each step is a place where char p can break, and because two Lean formalizations of 2026 follow this skeleton (document 05).

1. **Reduce to principalization.** Embed $X$ locally in a smooth $M$. Resolve $X$ by principalizing its ideal, and then take the strict transform. Show that the result does not depend on the embedding, and glue.
2. **The order.** For an ideal $I$ on smooth $M$, let $\operatorname{ord}_x I$ be the largest $a$ with $I_x \subset \mathfrak{m}_x^a$. Let $a = \max_x \operatorname{ord}_x I$, and let $\operatorname{Sing}(I, a)$ be the closed set where the order is $a$.
3. **Derivatives lower the order.** If $\operatorname{ord}_x I = a$, then the ideal $D^{a-1} I$, generated by all derivatives of order $\leq a - 1$ of elements of $I$, has order 1 at $x$. A local generator $h$ of order 1 defines a smooth hypersurface $H = V(h)$. This uses $\partial^{a-1}(x^a)/\partial x^{a-1} = a!\,x$, and $a!$ is a unit. **This step needs $a! \neq 0$ in $k$.**
4. **Maximal contact.** $H$ contains $\operatorname{Sing}(I, a)$, and after any blowup with a centre inside $\operatorname{Sing}(I, a)$, the strict transform of $H$ contains the new locus of order $a$. So the problem moves into $H$, a smooth scheme of dimension one less. $H$ is a *hypersurface of maximal contact*.
5. **The coefficient ideal.** On $H$, take $C(I) = \sum_{j < a} (D^j I)^{a!/(a-j)}|_H$. This is the ideal that "remembers" $I$ in dimension $\dim M - 1$. Resolving $C(I)$ on $H$ lowers the maximal order of $I$.
6. **Independence of choices.** Different hypersurfaces of maximal contact give the same result. This holds up to an étale or formal coordinate change (Włodarczyk's lemma, or the homogenization of Kollár), so the algorithm is well defined and functorial for smooth morphisms.
7. **The monomial case and the boundary.** Separate the exceptional divisors (the boundary) from the rest. When all that is left is a monomial in the boundary, resolve it by a combinatorial rule.
8. **The invariant.** The invariant is a sequence (order, number of old exceptional components, then the same for the coefficient ideal on $H$, and so on). It lives in a well ordered set, it is upper semicontinuous, its maximum locus is smooth, and it drops strictly after the blowup of that locus. Induction ends the algorithm.

In the weighted version (Abramovich-Temkin-Włodarczyk 2019, McQuillan 2019), the invariant is the sequence $(a_1, \dots, a_k)$ of orders of the successive coefficient ideals. The centre is the weighted blowup of $J = (x_1^{1/a_1}, \dots, x_k^{1/a_k})$, and the invariant drops after a single weighted blowup. The proof is shorter, but it uses the same steps 3 to 6 and the same $a! \neq 0$.

## 3.3 Where characteristic p breaks

Each item has: what fails, the example that shows it, and what is known about a way around it.

### 3.3.1 Derivatives do not lower the order

$\partial(x^p) = 0$. For $f = x^p + y^q$ with $q > p$ and $p \mid q$, every derivation kills $f$ to an element of order $\geq q - 1$, or kills it fully. Step 3 has no analogue. The usual fix replaces derivations by Hasse-Schmidt derivations, or by the full ring of differential operators $\mathcal{D}_M$ (Giraud, Villamayor, Kawanoue-Matsuki). $\mathcal{D}^{\leq a-1} I$ then does have order 1 when $a < p$, and more generally when $a$ is not divisible by $p$, but for $a = p^e$ the order-one elements that it gives are of the form $x^{p^e}$ "plus terms", and their zero set is not a hypersurface of maximal contact.

### 3.3.2 Hypersurfaces of maximal contact do not exist

Narasimhan (1983) gave a hypersurface in $\mathbb{A}^4$ over a field of char 2 whose locus of maximal order is a curve that, near the origin, is not contained in any smooth hypersurface. So no smooth hypersurface can contain $\operatorname{Sing}(I, a)$, and step 4 fails at the first blowup, not just after some blowups. The weaker notion of *weak maximal contact* or the *hypersurface of maximal contact along the maximal order locus up to finitely many blowups* (Hauser, Encinas-Villamayor) still exists, but the order of the coefficient ideal on it can go up under blowup (3.3.3).

### 3.3.3 The residual order can increase

Take a hypersurface of order $p^e$ in coordinates where it has the form $f = z^{p^e} + g(x_1, \dots, x_n)$, plus terms that do not matter after a coordinate change. The *residual order* is the order of $g$ after the best choice of $z$ (the order of the coefficient ideal). In char 0 it does not go up under a permissible blowup. In char p it can go up. Moh (1987) bounded the increase under one blowup and claimed a stability theorem. Hauser and Perlega (2019, arXiv:1802.05010) found a cycle of point blowups along which the residual order keeps growing, which disproves the stability claim (01, 1.6). Hauser called the points where the invariant goes up *kangaroo points*, and Hauser and Perlega characterized them (arXiv:1906.09593). The upshot is that the natural lexicographic invariant is not monotone, and any proof needs a secondary invariant that pays for the increases.

### 3.3.4 No smooth-functorial invariant is known

In char 0 the invariant is computed from derivatives, so it commutes with smooth morphisms and the algorithm is functorial. In char p every proposed invariant (Hironaka's characteristic polyhedron, Moh's invariant, the IFP invariants of Kawanoue-Matsuki, the elimination algebra invariants of Villamayor and Benito) depends on choices that are not canonical, or has only been shown to be canonical in low dimension. The dimension 3 proofs of Cossart and Piltant are not functorial. Whether a functorial resolution exists at all in char p is open. Without functoriality the gluing step 1 of Section 3.2 is a real problem, not bookkeeping.

### 3.3.5 Wild ramification and defect

Local uniformization reduces to questions about extensions of valued fields. In char 0 every such extension of a henselian field is *defectless*: the fundamental equality $[L:K] = e f$ holds. In char p there are *defect extensions*, where $[L:K] = p^d e f$ with $d > 0$, and they come from Artin-Schreier extensions $y^p - y = a$ and purely inseparable extensions $y^p = a$. Kuhlmann's program shows that defect is the main obstacle to local uniformization, and it resolves the case of Abhyankar valuations, where the defect cannot occur (Knaf-Kuhlmann 2005). Cutkosky (2015) gave counterexamples to *local monomialization* of morphisms in char p, a statement that is true in char 0. So some char 0 strengthenings are false in char p, and a proof must avoid them.

### 3.3.6 Imperfect fields and inseparability

Over an imperfect field: regular is not smooth; generic smoothness fails; a variety can be regular and geometrically non-reduced. A resolution cannot commute with inseparable base change: if $X$ is regular over $k$ and $X_{k^{1/p}}$ is singular, there is nothing to resolve over $k$ but there is over $k^{1/p}$. So the right statement over imperfect $k$ is the one with "regular" (Definition 3.1), and functoriality can only be asked for separable base change. Temkin's inseparable local uniformization (2013) is the strongest positive result: every valuation can be uniformized after a finite purely inseparable extension of the function field.

### 3.3.7 Zariski patching stops at dimension 3

Zariski's proof that local uniformization for all valuations implies resolution uses the compactness of the Zariski-Riemann space and a combinatorial argument about how to merge two local resolutions. That argument works up to dimension 3, because the "bad locus" of a merge is of dimension at most 1 there and can be handled by surface resolution. Above dimension 3 no one has made it work, in any characteristic. In char 0 this is not needed, because Hironaka gives the global result directly.

## 3.4 What is known about the core cases

The difficulties all appear already for hypersurfaces of order $p$ in the form
$$
f = z^p + g(x_1, \dots, x_n), \qquad (\ast)
$$
or more generally $z^p + a_1 z^{p-1} + \cdots + a_p$ with $\operatorname{ord} a_i \geq i$. The purely inseparable case $(\ast)$ is the core, as Hauser and Schicho, Hauser and Wagner, and Hauser and Perlega argue, and as Cossart and Piltant's threefold proof confirms: their main technical work is on Artin-Schreier and purely inseparable equations of degree $p$ over a regular base of dimension 2.

So a natural sub-problem, and the first research target of document 04, is:

> **Problem P1.** Resolve hypersurfaces of the form $(\ast)$ with $n = 4$ (so the hypersurface is a 4-fold in a 5-dimensional ambient space) over an algebraically closed field of char $p$, by blowups in regular centres.

and the related

> **Problem P2.** Find an invariant $\iota$ of $(\ast)$, defined from the Newton polyhedron, the characteristic polyhedron of Hironaka, or the differential operators, with values in a well ordered set, such that a canonical choice of centre makes $\iota$ drop. Moh's one-step bound, the cycles and the kangaroo characterization of Hauser-Perlega, the corrected residual orders of Hauser-Wagner and Hauser-Perlega (2024), Bérczi's ranking functions (2026), and the dimension 3 invariants of Cossart-Piltant are the inputs.

## 3.5 Two simplifications that are not available

It is easy to think that two classical reductions make the problem smaller. They do not.

1. **"It is enough to resolve hypersurfaces."** Every variety is birational to a hypersurface, but a resolution of a birational model is not a resolution of $X$ (condition 2 of Definition 3.1 fails). With strong embedded resolution for hypersurfaces one can do more, but the reduction from all varieties to hypersurfaces needs the functoriality of 3.3.4.
2. **"It is enough to resolve over $\overline{\mathbb{F}}_p$."** A variety over $k$ spreads out over a finitely generated $\mathbb{F}_p$-algebra, but the resolution of the special fibre does not lift. Even the reduction to fields finitely generated over $\mathbb{F}_p$ needs care: $X$ is defined over such a subfield $k_0$, but a resolution $Y_0$ of $X_0$ gives a resolution of $X$ only if $Y_0 \otimes_{k_0} k$ is still regular, and regularity is preserved by separable extensions and not by inseparable ones. (It descends along every field extension, by faithful flatness, which is the wrong direction here.) The project treats this reduction as a theorem to prove, with the hypothesis on $k/k_0$ that it needs, and not as a free step. One cannot reduce to finite fields, and one cannot reduce to perfect fields: a resolution of $X_{k^{\text{perf}}}$ need not descend to $k$, because $X$ can be regular at a point where $X_{k^{\text{perf}}}$ is singular (3.3.6). The perfect case is a weaker theorem, and it is the one that formal-conjectures states (06.4).

## 3.6 Lessons for the project

1. **State the right thing.** The main theorem must use "regular", not "smooth", and must have the density condition 3 of Definition 3.1. Document 06 has the Lean form and the checks.
2. **There are two problems in dimension $\geq 4$.** Local uniformization, and patching. A route must say which it solves.
3. **The core is degree $p$.** Formal work on $(\ast)$ (polyhedra, residual orders, Moh's bound, kangaroo points, cycles) is directly useful to every route, so it comes early (document 07, tier T4).
4. **Char 0 is a library, not a template.** The char 0 Lean proof (document 05) gives the blowup machinery, the normal crossings theory, the combinatorics of the monomial case and the descent and gluing arguments. Its use of derivatives must be replaced, not generalized.
5. **A counterexample is a result.** Several char 0 statements are false in char p (Narasimhan, Cutkosky, Moh's examples). A computer search that finds a new one is progress, and the agent has a role for it (document 10, role `refuter`; document 13).
