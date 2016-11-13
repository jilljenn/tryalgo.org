---
layout: en
title:  "Weird Advertisement"
category: geometry
---

You are given \\( n \\) rectilinear rectangles and a threshold \\( k \\), and want to find out the total area covered by at least \\( k \\) rectangles.
See [Weird Advertisement](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=3134).

## Sweep line algorithm with a segment tree

This problem can be solved in time \\( O(k n \log n) \\) using a sweep line algorithm.
Sweep a **horizontal line** from top to bottom over the rectangles. The left and right borders of all rectangles partition the \\( x \\)-axis into elementary intervals.

The idea is to maintain, at each instant, the total length of intervals covered by at least \\( i \\) rectangles, for each \\( i = 0, \ldots, k \\).

So we need a data structure that allows incrementing and decrementing efficiently counters over a range of elementary intervals, whenever the sweep line crosses the top or bottom border of a rectangle.

A [segment tree]({% post_url en/2016-06-25-segment-tree %}) is the appropriate data structure for this purpose. Every node (resp. leaf) \\( p \\) corresponds to an (resp. elementary) interval over the \\( x \\)-axis and contains:

- an integer `shift`, that represents the number of rectangles related to this node (actually, those that start or end with this interval) ;
- an array `covered`, where `p.covered[i]` contains the total length of intervals covered by at least \\( i \\) rectangles considered within the subtree rooted in \\( p \\). In particular, `p.covered[0]` is just the length of \\( I \\).

The number of rectangles related to an elementary interval \\( I_0 \\) is the sum of the *shift* values over all nodes on the path from the leaf related to \\( I_0 \\) to the root.

![]({{ site.images }}weird-advertisement.svg "The segment tree and the sweep-line."){:width="600"}

We describe the data structure as if `covered` were a vector of unbounded dimension, but in the implementation we would just truncate it after the index \\( k \\), because we only care about the value `root.covered[k]`.

The data structure maintains the following relation between `covered` and `shift`.  If a node \\( p \\) has two descendants with respective `covered` vectors $$a_0,a_1,\ldots$$ and $$b_0,b_1,\ldots$$, and $$\ell=$$ `p.shift`, then the vector `p.covered` is equal to

$$
		\texttt{p.covered} = \underbrace{(a_0+b_0),\ldots,(a_0+b_0)}_{\ell+1},(a_1+b_1),(a_2+b_2),\ldots
$$

## Computing the solution

Events are triplets `(x_1, x_2, y, type, p)` where:

- \\( [x_1, x_2] \\) is an interval at \\( y \\)-coordinate \\( y \\);
- ``type`` denotes whether the rectangles starts or ends;
- ``p`` is a pointer to the corresponding node in the segment tree.

When the sweep line moves down by distance $$\Delta$$ to the next event, then the total area of rectangles covered by at least \\( k \\) rectangles that have been crossed by the sweep line is simply $$\Delta$$ times `root.covered[k]`, which is added up to some total.
