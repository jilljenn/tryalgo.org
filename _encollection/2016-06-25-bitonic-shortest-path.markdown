---
layout: en
title:  "Bitonic shortest path"
category: shortest-paths
---

Given a graph with edge weights and vertex heights find a shortest path from a given source to a given destination, that traverses vertices of first increasing and then decreasing heights.

![]({{ site.images }}bitonic-shortest-path.svg){: width="300px"}

### Dynamic programming

Solve two separate problems, and then combine. For every vertex v find a shortest path from the source that traverses vertices in increasing height order.  This constraint imposes an orientation on the edges, from the lower to the higher endpoint and the resulting graph is acyclic.  Hence you can compute these shortest path by dynamic programming.  Just process vertices in order of increasing heights and choose the best predecessor among the lower height neighbors.  Do the same for descending path from every vertex v to the destination, and combine the paths.  Total complexity is \\( O(n \log n + m ) \\) , where n is the number of vertices and m the number of edges.
