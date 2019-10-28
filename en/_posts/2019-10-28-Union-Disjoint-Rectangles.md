---
layout: en
category: geometry
title: "Union of disjoint rectangles"
author: Christoph Dürr
problems:
    "icpcarchive:City Park": https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=657&page=show_problem&problem=4901
---

Given $n$ rectilinear non overlapping rectangles, discovered the all connected components in their union.

In the illustration below, each connected component is depicted with a different color.

![Union of non overlapping rectangles]({{site.images}}union-disjoint-rectangles.svg){:width="600"}

This is a particular case of the problem of computing the union of given [rectilinear rectangles]({% post_url 2016-06-25-union-of-rectangles %}) . But using a segment tree for this problem is an overkill, as the non-overlapping property of the input allows a much simpler approach.

## Key ingredient

The key ingredient is a very simple algorithm to solve the following problem.
Suppose you are given a set of green and red intervals on the line, with the promise that two intervals of the same color intersect in at most one point.  The goal is to produce the list of green-red interval pairs which intersect.


![Finding intersections of red and green intervals]({{site.images}}union-disjoint-rectangles-intervals.svg){:width="600"}

One can solve this problem in time $O(n \log n)$ by sorting the intervals by their left endpoints and processing them from left to right using the sweep-line technique.  It will be convenient to consider two lists, one for each color. The algorithm is similar to merging two ordered lists. It has a variable x, which takes increasing values, and maintains a reference to a red interval containing  x if any, and a similar reference to a possible green interval.  Intersections between green a red intervals are discovered naturally.

## Reduce to the red-green interval intersection problem

The main difficulty of the problem, is to discover the edges of a graph, where rectangles are vertices, and there is an edge when the sides of two rectangles intersect, even in a single point.  Then we can use a simple graph exploration algorithm, such as DFS, to discover all connected components of the graph.

These edges can be discovered as follows. Consider a height y, and produce a list of all rectangles who's top border is at height y and a list of all rectangles who's bottom border is at height y.  These lists translate naturally into a list of green and red intervals and form an instance to the above mentioned problem. This permits to discover all rectangle adjacencies around a horizontal line at height y, and need to be done for all heights y appearing in the input data. The same procedure must be done for all x coordinates of the input data, discovering horizontal adjacencies between rectangles.

One can use four dictionaries  *top, left, bottom* and *right*, such that *top[y]* contains the list of all rectangles who's top border is at height y. The other dictionaries are defined similarly.


## Complexity

The overall algorithm has complexity $O(n \log n)$, provided that accesses to the dictionaries can be done in 
constant time.
