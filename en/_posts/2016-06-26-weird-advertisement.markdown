---
layout: post
title:  "Weird Advertisement"
category: geometry
---

You are given n rectilinear rectangles and a threshold k, and want to find out the total area covered by at least k rectangles.
See [Wierd Advertisement](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=3134).


## Sweep line algorithm with a segment tree

This problem can be solved in time \\( O(k n \log n) \\) using the sweep line algorithm.
Sweep a vertical line from left to right over the rectangles. The intersections between the line and the rectangles can be partitioned into intervals, each associated with the number of intersections.  So you just need to keep track of the total interval lengths that have at least k intersections.  Whenever the sweep line touches the left side of a rectangle, the corresponding number have to be incremented, and when it touches the right side of a rectangle they have to be decremented.

![]({{ site.images }}weird.svg "In red: the areas covered by at least k=3 rectangles.")

We proceed as for the problem "Union of rectangles", but this time the score of a node is a vector of size k+1.  For a node p corresponding to a y-interval I the value p.score[i] is the portion of I that is covered by at least i rectangles.  If the node value p.val is zero, then p.score is just the member wise sum of p.left.score and p.right.score.  Otherwise it corresponds to the vector starting with p.val times the value \|I\| followed by the vector p.left.score + p.right.score.  The resulting vector has to be truncated after k+1 entries.
