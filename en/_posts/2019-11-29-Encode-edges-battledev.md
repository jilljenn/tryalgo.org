---
layout: en
category: geometry
title: "Encoding edges by weights"
author: Christoph Dürr
problems:
    "battledev:nov2019,DevOps":  https://r.email1.hellowork.com/tr/cl/ltXrRbtTi9k-rr4pmNMgd-gwMfqWwikSutVdUS3j0H75avh-cv38HxRPVPsz2GNmmDF3m8J2A7oGQXx-GO5VapKBz66KeJXCJenx8ByhAYbMgHzufaipyjTDHit-p8Y1VPDgFAUBfQC1VGDLCrXBNnWCRBdWtgC_q4im7XXFNzsJfi24CN9e11cNs2_IfaTua5ItxhkYATp-EhLXeX6Rmw
---

# Warning

This post describes a solution to the problem stated in the above link. However it will not be accepted by the judge, because the intended problem was a different one.  In the stated problem the condition is that `x[u]+x[v]>y` if and only if (u,v) is an edge. In the intended problem, the condition should be that `sum x[u] over all u in S > y` if and only if `S` is a clique in the graph. The solution to the intended problem is described [here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.228.76&rep=rep1&type=pdf).

# Problem statememt

Given an undirected graph G(V,E), we ask whether it is possible to encode the edges using non-negative integers y and x[v] for every vertex v such that

- y ≥ x[v] for every vertex v
- x[u] + x[v] > y if and only if (u,v) is an edge.

In addition y should be minimized.

# Properties

The key observation is that the inequality x[u] + x[v] > y is monotone in x[v]. Hence the neighborhoods N of two vertices v and v', must be included in each other. This statement is a bit subtle as v or v' could be missing from one of the neighborhoods, because the graph has no self-loops. So the precise statement is, using N[v]:={u:(u,v) ∈ E} and d(v)=|N[v]|,

- for any two vertices v, v' with d(v)≤d(v') we have $N[v]\setminus\{v'\} \subseteq N[v']$.

So we have a necessary condition which we can check in time $O(|V|^2)$, by ordering first the vertices in increasing degree, and checking inclusion of every two successive vertices in this order. The complexity is ok, given the bound $|V|\leq 1000$ from the problem statement.

I claim that the condition is also sufficient. Consider the adjacency matrix of the given graph, using the degree ordering of the vertices. 

Consider the example 5 of the input samples: 

![Example graph]({{site.images}}battledev2019_devops.svg){:width="400"}

We obtain the following adjacency matrix M, where we showed in gray the edges and in white the non-edges. 

![Adjacency matrix]({{site.images}}battledev2019_devops_matrix.svg){:width="400"}

We can observe that the grid partitions into k by k blocks, the row or column of a block corresponds to vertices which have the same degree. k is defined as the number of distinct degrees. In our example k=6. There are only two kind of blocks, those that do not contain any edge, and those that are completely filled with edges, except for the diagonal.  Moreover these gray blocks are in the lower right triangle of the matrix, and contain or do not contain the anti-diagonal cells, depending whether there is a vertex of degree 0. Hence this condition will be important for the solution.

Clearly vertices of different degree need different x-values. Hence max x[v] ≥ k-1, and y ≥ k-1. Since we want to minimize y, it seems good to have the smallest increase in x between adjacent blocks. Hence we suggest the following solution:

- Ff there is a vertex of degree 0, as in our example, we number the blocks from 0 to k-1, and the x-value of a vertex is the number of its block. In addition we choose y=k-1. We cannot do better, with the above observation.
- If there is no vertex of degree 0, then we number the blocks from 1 to k, and choose y = k. We cannot choose y=k-1, otherwise some vertex v has x[v] = 0, and will have zero degree.

