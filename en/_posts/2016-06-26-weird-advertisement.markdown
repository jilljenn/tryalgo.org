---
layout: en
title:  "Weird Advertisement"
category: geometry
---

You are given n rectilinear rectangles and a threshold k, and want to find out the total area covered by at least k rectangles.
See [Weird Advertisement](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=3134).


## Sweep line algorithm with a segment tree

This problem can be solved in time \\( O(k n \log n) \\) using the sweep line algorithm.
Sweep a vertical line from top to bottom over the rectangles. The left and right borders of all rectangles partition the x-axis into elementary intervals. We would like to maintain a counter for each of them, indicating how many rectangles currently contain the interval on the sweep-line.

So we need a data-structure that permits to increment and decrement these counters over an interval of indices, whenever the sweep-line touches the top or bottom border of a rectangle.  During these operations we just need to keep track of the total length of all elementary intervals that have their associated counter at least k.

A [segment tree]({% post_url en/2016-06-25-segment-tree %}) is the appropriate data structure for this purpose. Every node corresponds to an interval over the x-axis and contains as an integer *shift*.  The value of the counter associated to an elementary interval I is the sum of the *shift* values over all nodes on the path from the root to the leaf corresponding to I.

![]({{ site.images }}weird-advertisement.svg "The segment tree and the sweep-line."){:width="600"}

In addition to *shift* we associate to every node of the tree a table *covered*.  For a node p corresponding to x-axis interval I the entry *p.covered[i]* contains the total length of the elementary intervals that are covered by at least i rectangles among the intervals that incremented the *shift* value of some node in the interval.  In particular *p.covered[0]* is just the length of I. We describe the data structure as if *covered* were a vector of unbounded dimension, but in the implementation we would just truncate it after the index k, because we only case about the value *root.covered[k]*.  When the sweep-line moves down by distance $$\Delta$$ to the next event, then the total area of rectangles that are covered by at least k rectangles and that have been seen by the sweep-line is simply $$\Delta$$ times *root.covered[k]*

The data-structure maintains the following relation between *covered* and *shift*.  If a node p has two descendants with respective *covered* vectors $$a_0,a_1,\ldots$$ and $$b_0,b_1,\ldots$$, and $$\ell=p.\textrm{shift}$$, then the vector *p.covered* is equal to

$$
		p.\textrm{covered} = \underbrace{(a_0+b_0),\ldots,(a_0+b_0)}_{\ell+1},(a_1+b_1),(a_2+b_2),\ldots
$$
