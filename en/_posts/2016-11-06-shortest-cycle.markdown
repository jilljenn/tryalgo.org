---
layout: en
title:  "Shortest cycle"
category: cycles
---

Find a shortest cycle in a given undirected graph.

## Algorithm in time $$O(|V|\cdot |E|)$$ using BFS

The BFS graph traversal can be used for this purpose. [Here](http://stackoverflow.com/questions/20847463/finding-length-of-shortest-cycle-in-undirected-graph) is a discussion why DFS cannot help for this problem.

The key observation is the following. Suppose you start a BFS exploration at some root vertex $$r$$.  The exploration places the vertices into levels according to the distance from the root, where the root is in level 0. The BFS exploration distinguishes between different kind of edges. First there are the *forward edges* which lead to unmarked vertices.  These edges form the BFS tree.  The remaining edges form cycles with the tree.  These edges can only connect vertices from the same level or from adjacent levels.

If from a vertex $$u$$ at level $$i$$ we discover an edge to a neighbor $$v$$ at level $$j$$ then we know that there is a cycle consisting of the path from $$r$$ to $$u$$ in the BFS tree, the edge $$(u,v)$$ and the path from $$v$$ to $$r$$ in the BFS tree.  This cycle has length $$i+1+j$$.  Also the cycle is simple if and only if $$r$$ is the lowest common ancestor of $$u$$ and $$v$$ on the tree.  Otherwise we know that there is a simple cycle of length at most $$i+j$$. 

Hence in order to find a shortest cycle simply loop over all possible root vertices $$r$$. Initiate a BFS search at $$r$$, and for every non-forward edge $$u,v$$ you encounter, keep track of the tree vertices $$r,u,v$$ that minimize the sum of the levels of $$u$$ and of $$v$$.  After that you know that for the minimizers $$r,u,v$$, there is a shortest cycle containing these vertices.  Then you just need a last BFS search initiated at $$r$$, so that you obtain the shortest path from $$r$$ to $$u$$ and to $$v$$.  Together with the edge $$(u,v)$$ they form a shortest cycle.  

![]({{site.images}}shortest-cycle.svg "Neighbors of vertex u.  The edge (u,c) will be part of the BFS tree, while edges (u,a) and (u,b) are part of a simple cycle." ){:width="200"}

### Links

- [lecture notes](http://theory.stanford.edu/~virgi/cs267/lecture2.pdf).

