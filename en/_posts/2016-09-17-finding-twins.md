---
layout: en
title:  "Finding Twins"
category: data structures
author: Christoph Dürr and Michel Habib
excerpt_separator: <!--more-->
problems:
   "spoj:Finding true twins": http://www.spoj.com/problems/TRUETWIN/
---

Two vertices u,v are *twins* if they have the same neighborhood. They are *false* if uv is not an edge and *true* twins if uv is an edge.
Find a false twin pair in time $$O(|V|+|E|)$$.


![]({{ site.images }}twins-definition.svg "The vertices c,d are the only twins in this graph. They are false twins."){:width="300"}

<!--more-->

This algorithm has been around for a while, and the inventor is not known.  Such a result is said to be *folklore*.

## Key observation

Every vertex has quite a partial view of the graph, and can distinguish among all other vertices only between its neighbors and the vertices which are not its neighbors.

![]({{ site.images }}twins-view-a.svg "Vertex a can distinguish between its neighbors (gray) and non-neighbors (white)."){:width="300"}

![]({{ site.images }}twins-view-b.svg "Vertex b can distinguish between its neighbors (gray) and non-neighbors (white)."){:width="300"}

Let's use partition refinement to solve this problem. We start with the trivial partition where all vertices are in one class, namely \{\{a,b,c,d,e,f\}\}. Then we refine it for each vertex u using as pivot set the neighbors N(u) of u.  After refining with N(a), the partition becomes \{\{a,e,f\},\{b,c,d\}\}. After refining with N(b) it becomes \{\{a,f\},\{e\},\{b,c,d\}\}. Eventually after refining with N(v) of all vertices v, we end up with the partition \{\{a\},\{b\},\{c,d\},\{e\},\{f\}\}. And see there, the false twins c,d stayed in the same class.

In fact every pair of vertices u,v that stayed together in the same class during these refinements correspond to false twins, because no vertex could separate them (meaning they are twins) and also u could not separate v from himself, meaning that v is not in the neighborhood of u (meaning they are false twins).

## Extension

How can we find true twins?

<p style="color:white;">Simply refine for each vertex u with the pivot set $$N(u)\cup\{u\}.$$  It should be clear that now real twins cannot separate each other.<p>



