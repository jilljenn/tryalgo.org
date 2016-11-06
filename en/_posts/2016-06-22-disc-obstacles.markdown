---
layout: post
title:  "Disc obstacles"
category: geometry
---

Find a shortest path in the plane between two points avoiding given obstacles with disc shapes.  See [Save the Princess](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3072).

### Build a weighted graph

First compute for every pair of discs all 4 tangent segments.  The corresponding 8 endpoints are added to the edge set of the graph, together with the source and the target point.  Add edges between points if the corresponding segments do not intersect obstacles (other than on the border).  Then the shortest path can be computed with Dijkstra's algorithm.  The complexity to build the graph is \\( O(n^3) \\) with a naive approach, and dominates the complexity of computing the shortest paths.  As the instances have n bounded by 50, the running time is small enough.

![](/~durrc/tryalgo/images/disc-obstacles.png)

Not all segments are shown