---
layout: en
category: ml
title: "Iterative Machine Teaching"
author: Jill-Jênn Vie
---

This is a random discussion surrounding the ICML 2017 paper [Iterative Machine Teaching](https://arxiv.org/pdf/1705.10470.pdf).

Let us assume we are performing SGD to learn a function $f_w : \mathcal{X} \subset \mathbf{R}^d \to \mathcal{Y}$ by minimizing a convex loss $\ell(f_w(x), y)$ over sample $(x, y)$:

$$ \def\grad{\frac{\partial \ell(f_{w_t}(x), y)}{\partial w}} w_{t + 1} = w_t - \eta_t \grad $$

Now comes the weird part: we actually know where we want the algorithm to converge ($w^*$). And we are feeding examples $(x, y)$ to it. After one example:

$$ ||w_{t + 1} - w^*||_2^2 = \left|\left|w_t - \eta_t \grad - w^*\right|\right|_2^2 \\ = ||w_t - w^*||_2^2 + \eta_t^2 \left|\left|\grad\right|\right|_2^2 - 2\eta_t \left\langle w_t - w^*, \grad \right\rangle $$

- The first term is where we were at the previous step, compared to the optimal.
- The second term is the **difficulty** of example $(x, y)$: how much do we move in space?
- The third term is the **usefulness** of example $(x, y)$: how much do we move in the direction that we're interested in? (= going towards $w^*$)

## Active learning

In active learning, we don't know where we are converging, and we don't know the $y$. So we want to move the most:

Ask sample $x$ for which $Var_y\left(\grad\right)$ will be biggest.

By the way, this is Fisher information, right? Variance of the score!

## MAP inference

$$ p(w|X) = p(X|w) p(w)\\ -\log p(w|X) = -\log p(X|w) - \log p(w) $$

If we assume: $w_{t + 1} \sim \mathcal{N}(w_t, (1/\lambda) I_d)$:

$$ w_{t + 1} \textrm{ minimizes } \ell(f_w(x), y) + \lambda ||w - w_t||_2^2 $$

$$ w_{t + 1} \textrm{ verifies } \grad - 2\lambda(w_{t + 1} - w_t) = 0\\ w_{t + 1} = w_t - \frac1{2\lambda} \grad. $$

A mistake is hidden in the formula above. Can you find it?
