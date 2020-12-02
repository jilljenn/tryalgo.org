---
layout: en
title:  "Alternating direction method of multipliers"
author: Jill-Jênn Vie
---

Introducing [ADMM](https://web.stanford.edu/~boyd/papers/pdf/admm_slides.pdf)!

Let's say we want to solve:

minimize $f(x) + g(z)$  
subject to $Ax + Bz = c$

Objective:

$$ L(x, z, u) = f(x) + g(z) + u^T(Ax + Bz - c) + \rho/2 ||Ax + Bz - c||^2_2 $$

ADMM does:

$$ x^{k + 1} = argmin_x L(x, z^k, y^k)\\
z^{k + 1} = argmin_z L(x^{k + 1}, z, y^k)\\
y^{k + 1} = y^k + \rho(Ax^{k + 1} + Bz^{k + 1} - c) $$

This is a quite general problem. Actually this is a special case:

minimize $F(x, z)$  
subject to $G(x, z) = 0$

where $F : (x, z)$ is biconvex, which means convex in $x$ (for each $z$) and in $z$ (for each $x$).

ADMM would become:

$$x^{k + 1} = argmin_x (F(x, z^k) + \rho/2 || G(x, z^k) + u^k ||^2_2)\\
z^{k + 1} = argmin_z (F(x^{k + 1}, z) + \rho/2 ||G(x^{k + 1}, k) + u^k||^2_2)\\
u^{k + 1} = u^k + G(x^{k + 1}, z^{k + 1})$$

Please note that when $G = 0$, ADMM becomes alternate minimization.

It can also be applied to nonnegative matrix factorization. In this case with $G = 0$ one can recover ALS.

- Vincent Cotter, Pierre Alquier. [1-bit Matrix Completion: PAC-Bayesian Analysis of a Variational Approximation](https://arxiv.org/abs/1604.04191)
- [Matrix Factorization in PyTorch](http://blog.ethanrosenthal.com/2017/06/20/matrix-factorization-in-pytorch/) (I guess ADMM > ALS > SGD, but it should be tried)

Some GitHub repos:

- [Mangaki](https://github.com/mangaki/mangaki)
- [Implicit](https://github.com/benfred/implicit) by Ben Frederickson (nice blog posts out there)
- [Spotlight](https://github.com/maciejkula/spotlight) by Maciej Kula
