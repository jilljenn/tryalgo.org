---
layout: en
title:  "Weird Advertisement"
category: geometry
---

You are given \\( n \\) rectilinear rectangles and a threshold \\( k \\), and want to find out the total area covered by at least \\( k \\) rectangles.
See [Weird Advertisement](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=3134).

## Sweep line algorithm

This problem can be solved in time \\( O(k n \log n) \\) using a sweep line algorithm.
Sweep a **horizontal line** from bottom to top over the rectangles. The left and right borders of all rectangles partition the \\( x \\)-axis into elementary intervals, which we call *segments* from now on.  For example in the figure below we have 8 segments that we will number from 0 to 7 from left to right.

![]({{ site.images }}weird-advertisement.svg "The segment tree and the sweep-line."){:width="600"}
 
Each segment has a fixed `length` and a variable `count`, that keeps track of the number of rectangles containing the segment on the sweep line.  As the line moves down we have to update the counters whenever the top or the bottom of a rectangle is reached.  The solution to the problem is then computed by cumulating in a variable `total_area` the product \\( \Delta \cdot c\\), where \\( \Delta \\) is the distance in \\( y \\) traveled by the sweep line between two updates and \\( c \\) is the total length over all segments where `count` is at least \\( k \\).

The algorithm consists of the sequential processing of a list of events.  An event corresponds either to the top or the bottom of a rectangle.  It is represented by  a tuple \\( (y, d, s_1, s_2 ) \\) where:

-  \\( y \\) is the \\( y \\)-coordinate or the rectangle border;
- \\(d \\) is +1 for the a top border and -1 for a bottom border;
- \\( [s_1, s_2) \\) is a half-open interval over the segments, representing the projection of the rectangle on the \\(x \\)-axis.

The event list is processed in order of increasing \\(y\\) coordinates.  It is not important for the same \\(y\\)-coordinate in which order bottom and top borders are processed.

So on event \\( (y, d, s_1, s_2) \\) first `total_area` is updated as described above, where \\(\Delta\\) is the difference in \\(y\\) between the current and the last event.  Then the value \\(d\\) is added to the variable `count` over all segments in \\( [s_1, s_2) \\). 

On every event there might be as many as \\(\Omega(n)\\) counters to be incremented/decremented.  Hence we need to be a bit clever.

## Segment tree

A [segment tree]({% post_url en/2016-06-25-segment-tree %}) is the appropriate data structure for this purpose. It is a binary tree build on the top of the segments.  Every node corresponds to a interval of segments, and contains an integer variable `val`. This variable represents a lazy update of the counters at the segments.  For example if `val` is 2 then this means an increment of 2 the counters among the corresponding segments. Hence when we want to add \\(d\\) to all segment counters in the interval \\( [s_1, s_2) \\), then we just have to add \\(d\\) to the variable `val` of a logarithmic number of nodes in the segment tree.

Now we need to augment this data structure with additional information that permits is to determine the total length of the segments which have their counter at \\(k\\) at least.  To this purpopse we associate to every node `p` a vector `p.covered` indexed from 0 to \\(k\\).  The idea is that `p.covered[i]` contains the total length over segments with a counter being least \\( i \\).  Now if `root` is the root of this tree, then `root.covered[k]` is exactly the total length \\(c\\) that we need for the update of `total_area`.

The vector `covered` of a node can be computed recursively as follows.  For a leaf node `p` `p.covered[0]` is just the length of the corresponding segment. In addition `p.covered[i] == p.covered[0]` for all \\(i\\) smaller equal `p.val` and `p.covered[i] == 0` for all larger indices.

Now for a node `p` with two descendant nodes `left` and `right` if `p.val=0` then `p.covered` is clearly just the memberwise sum of `left.covered` and `right.covered`.  But in general if `c == left.covered[i] + right.covered[i]` represents the total length of segments with their counter being at least \\(i\\), then with respect to the node `p` we can say that \\(c\\) is the total length of segments with their counter being at least `i + p.val`.  
Hence formally if $$\ell=$$ `p.val`, \\(a =\\)`left.covered` and \\(b =\\)`right.covered`, then the vector `p.covered` is equal to

$$
		\texttt{p.covered} = \underbrace{(a_0+b_0),\ldots,(a_0+b_0)}_{\ell+1},(a_1+b_1),(a_2+b_2),\ldots
$$

The former equation is an invariant that the segment tree needs to maintain on the nodes all the way from `p` to the `root` whenever the value `p.val` is modified. Each of these updates cost only time \\(O(k)\\), which proves the claimed time complexity.


