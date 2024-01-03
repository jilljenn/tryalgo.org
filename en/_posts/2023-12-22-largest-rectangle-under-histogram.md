---
layout: en
title: Largest rectangle under an histogram
category:
    - data structures
author: Jill-Jênn Vie
---

You are given an histogram and want to identify the area of the largest rectangle that fits under the histogram.

There is a solution in linear time [using a stack](https://cp-algorithms.com/dynamic_programming/zero_matrix.html). There is also a divide-and-conquer solution that we describe here.

On range $[l, r]$:
- Find the minimum $m$
- One rectangle candidate is $m \times (r - l + 1)$ 
- Other rectangle candidates are recursively computed on the left and right of the minimum.

So the complexity overall verifies:
$$T(n) = 2T(\frac{n}2) + f(n)$$
where $f(n)$ is the cost of finding the minimum over an interval of length $n$.

## Finding the minimum efficiently over a range

This task can be done:

- Either in $O(n)$ naively
- In $O(\log n)$ using a [range minimum query structure](https://cp-algorithms.com/data_structures/sparse-table.html)
- Or even in $O(1)$ using a [sparse table](https://cp-algorithms.com/data_structures/sparse-table.html).

## Overall complexity

1. If $f(n) = O(n)$, master theorem says complexity is $T(n) = \Theta(n \log n)$.
2. If $f(n) = O(1)$, master theorem says complexity is $T(n) = \Theta(n)$.
3. If $f(n) = O(\log n)$, well master theorem can't be used; we can use instead a generalization called the [Akra-Bazzi theorem](https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_method) (1998) with $p = 1, g(x) = \log x$:

$$\begin{align}
T(x) & = \Theta\left(x\left(1 + \int_1^x \frac{g(u)}{u^2} du\right)\right)\\
& = \Theta\left(x\left(1 + \left[- \frac{\log x + 1}{x} + 1\right]\right)\right)\\
& = \Theta(2x - \log(x))
& = O(x).
\end{align}$$
