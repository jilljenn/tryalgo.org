---
layout: en
title:  "Mission improbable"
category: matching
author: Christoph Dürr
---

Explanation for the problem [mission improbable](https://online.acmicpc.org/problems/improbable) from the ACM final in 2017. Read the problem statement first.

## Summary

We are given a matrix with non-negative integers.  The goal is to decrement a maximal total amount the entries of the matrix such to preserve

- the maximum of every row
- the maximum of every column
- positive entries have to stay positive

## Explanation

A positive entry that is neither the maximum in its row nor in its column can be safely decreased to 1.

Now consider a value v appearing as the maximum of some rows and some columns.  In the intersection of those rows and columns are some entries of value v.  We want to decrease as many values to 1 as possible, keeping a minimum number of values at v such to preserve the maximum of each these rows and columns.  Consider the bipartite graph with a vertex for each row of maximum v and a vertex for each column of maximum v. There is an edge for each entry of value v.  In this graph you want to select a minimum edge set that covers each vertex. This reduces in finding a maximum bipartite matching in that graph, and to complete it with arbitrary edges for each unmatched vertex.


![]({{site.images}}mission-improbable.svg "The graph corresponding to the instance depicted in the problem description.  Here we took the union over all values v." ){:width="600"}

### Special case

Suppose that some value v is only the maximum in some rows but not in a column. Then you can just select an arbitrary entry v in each of these row, and decrease to 1 all other entries v from these rows.

### Complexity

The simplest bipartite matching algorithm has complexity $O(n m)$ where n is the number of vertices and m the number of edges. In your case nm is upper bounded by 2 000 000.  The matching algorithm has to be executed several times but on graphs that correspond to disjoint entries of the matrix, hence the overall time complexity is within a few million operations.
