---
layout: en
title: Approximations of the Euclidean metric traveling salesman problem
category:
    - approximation
author: Jill-Jênn Vie
---

Back in the good ol' *agrégation* days, I remember I used as *développement*[^1] a nice 2-approx algorithm for the traveling salesman problem where the weights on the edges are given by the Euclidean distance between nodes.

 [^1]: This must mean nothing to non-French people but anyway.

I was told it was [Christofides algorithm](https://en.wikipedia.org/wiki/Christofides_algorithm) but actually it was not. It is the "double-tree algorithm".

1. Find a minimum spanning tree $T$ using e.g. [Kruskal's algorithm](https://jilljenn.github.io/tryalgo/_modules/tryalgo/kruskal.html).
2. Duplicate the edges of $T$. Find an Eulerian tour (that exists) using e.g. [Hierholzer's algorithm](https://jilljenn.github.io/tryalgo/_modules/tryalgo/eulerian_tour.html).
3. Shortcut the Eulerian tour. This is a 2-approx of the (Euclidean) metric TSP.

It was hard to find who discovered it but Rozenkrantz et al. say that it is a "widely known but unpublished method" (1977). Christofides and Serdyukov found in 1976 (published in 1978) that by solving a matching problem between nodes of odd order (at the cost of $O(n^3)$), they could improve the approximation ratio to 3/2. This reminds me of the [trick used by ENS Ulm team in Google Hash Code 2014](https://a3nm.net/blog/google_hashcode_2014.html).

To know more, you can check this [other post](https://bochang.me/blog/posts/tsp/).

**Update.** Karlin, Klein and Gharan [found a new algorithm](https://www.quantamagazine.org/computer-scientists-break-traveling-salesperson-record-20201008/) with approximation ratio $3/2 - 10^{-36}$, and got the best paper at STOC 2021.

## References

Rosenkrantz, Daniel J., Richard E. Stearns, and Philip M. Lewis, II. "An analysis of several heuristics for the traveling salesman problem." SIAM journal on computing 6.3 (1977): 563-581.

Christofides, N. "Worst-case analysis of a new heuristic for the traveling salesman problem."
Symp. on New Directions and Recent Results in Algorithms and Complexity (April 1976),
Carnegie-Mellon University, Pittsburgh

Serdyukov, Anatoliy (1978), "О некоторых экстремальных обходах в графах" [On some extremal walks in graphs], Upravlyaemye Sistemy (Управляемые системы) (in Russian), 17: 76–79

Karlin, Anna R., Nathan Klein, and Shayan Oveis Gharan. "A (slightly) improved approximation algorithm for metric TSP." Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing. 2021. <https://arxiv.org/abs/2007.01409>
