---
layout: en
title:  "Edges expiring"
category: union-find
---

Given a graph with expiring dates for every edge, when will the graph be disconnected? See [codility:psi2012](https://codility.com/programmers/challenges/psi2012/)

![](/~durrc/tryalgo/images/edges-expiring.png)


### Union-find

The trick is to inverse the time and to add edges to an initial empty graph, in the reverse order they are expiring.  Once the current graph is connected you know that the answer is the time of the last added edge.  Use union-find to maintain connected components.  Hence the problem can be solved in quasi linear time.
