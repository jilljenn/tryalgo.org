---
layout: en
title:  "Union of rectangles"
category: geometry
---

You are given n rectilinear rectangles and want to find out the total area covered by their union.
See [Rectangles](http://acm.tju.edu.cn/toj/showp1049.html).

## Sweep line algorithm with a segment tree

This problem can be solved in time \\( O(n \log n) \\) using the sweep line algorithm.
Sweep a vertical line from left to right over the rectangles. Divide the y axis into *elementary y-intervals* by considering all y coordinates from the input.  Maintain a counter for each y-interval, which keeps track of how many rectangles currently cover this interval on the sweep line.
These counters are index from 0 to say n-1, using the ordering along the y-axis.  Whenever the sweep line reaches the left side of a rectangle, the counters need to be incremented at indices corresponding to included intervals.  Whenever the sweep line reaches the right side of a rectangle this operation is inverted by decreasing the counters.

Now to keep track of the area of the union of rectangles over the part seen so far, we need to determine the total length over all intervals who's counter is positive.


![]({{ site.images }}union-of-rectangles.svg "Counters are incremented when the left side of a rectangle is encountered.")

So we need a data structure that maintains an array of counters, each has an associated constant length.
The data structure must implement the following operations.

* increment all entries between given indices i and j
* decrement all entries between given indices i and j
* query the total length of all intervals whose counter is positive.

The segment tree is the right choice for this data structure. It has complexity \\( O(\log n) \\) for the update operations and \\( O(1) \\) for the query.  We need to augment the segment tree with a *score* per node, with the following properties.

* every node corresponds to a y-interval being the union of the elementary y-intervals over all the indices in the span of the node.
* if the node value is zero, the score is the sum of the scores of the descendants (or 0 if the node is a leaf).
* if the node value is positive, the score is the length of the y-interval corresponding to the node.

The sweep line algorithm consists of processing an event list. An event consists of a y-interval, a delta value +1 or -1 (left or right side), and an x-value. Events are ordered according to their x-values.

#### For more information

* [Sample code](http://pythonhosted.org/tryalgo/_modules/tryalgo/union_rectangles.html#union_rectangles)
