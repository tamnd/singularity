---
title: The problem
description: The statement of resolution of singularities, the known cases and the open case in dimension 4 and characteristic p.
lead: Does each variety of dimension 4 over a field of characteristic $p > 0$ have a resolution of singularities?
---
## The statement

Let $X$ be a reduced scheme that is separated and of finite type over a field $k$. A resolution of $X$ is a proper morphism $\pi : Y \to X$ with these properties.

1. $Y$ is regular.
2. $\pi$ is an isomorphism over an open set $U$ of $X$ that contains the regular locus of $X$.
3. The inverse image $\pi^{-1}(U)$ is dense in $Y$.

The Lean form is [IsResolution](node:SG00000004). The statement in dimension $n$ and characteristic $p$ is [ResolutionInDim](node:SG00000006), and the open case is [ResolutionDimFourCharP](node:SG00000007).

The project uses "regular" and not "smooth over $k$". Over an imperfect field, such as $\mathbb{F}_p(t)$, a regular variety need not be smooth, so the statement with "smooth" is false there. The node [Smooth is too strong over an imperfect field](node:SG0000000C) records this. Condition 2 stops a map such as $X \sqcup X \to X$ from counting as a resolution. Condition 3 stops a trivial $Y$. The fidelity checks on the [trust page](/trust/) test these choices in Lean.

## The known cases

| Case | Result | Node |
|---|---|---|
| Characteristic 0, every dimension | Hironaka (1964) | [Characteristic 0](node:SG0000000D) |
| Dimension 1, every characteristic | normalization | [Curves](node:SG0000001A) |
| Dimension 2, every characteristic | Abhyankar (1956), Lipman (1978) | [Surfaces](node:SG0000001B) |
| Dimension 3, $p > 5$ | Abhyankar (1966) | [Threefolds](node:SG0000001D) |
| Dimension 3, every $p$ | Cossart and Piltant (2008, 2009, 2019) | [Threefolds](node:SG0000001D) |
| Every dimension, up to a finite cover | de Jong (1996), alterations | [De Jong's alterations](node:SG0000001K) |

## The open case

In dimension 4 and characteristic $p$, no proof is known. The methods of characteristic 0 use a hypersurface of maximal contact, and in characteristic $p$ such a hypersurface need not exist ([Narasimhan's example](node:SG00000018)). The natural invariants can go up under a blowup ([a kangaroo point](node:SG00000016)), and a claimed stable invariant fails ([the Hauser-Perlega cycle](node:SG00000017)).

The first test case is the purely inseparable hypersurface $z^p + g(x_1, \dots, x_4) = 0$. The node [Purely inseparable hypersurfaces](node:SG00000009) states it.

The project follows nine routes to the open case. Each route has a page under [the routes](/routes/), with the idea, the known results and the key obstruction.
