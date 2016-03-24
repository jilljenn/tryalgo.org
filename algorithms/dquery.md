---
layout: page
title: Algorithms
---

## Query number of distinct elements in a table

- Input: a static table x with n integers
- Sequence of m queries: for (i,j) return number of distinct elements among x[i], x[i+1],..., x[j-1]
- Allowed complexity: O(m log n)

>! Solution based on a segment tree

This solution will process all queries at once, and cannot be implemented in form of a data structure.

- Process from left to right, with j=0,1,...,n-1.
- Maintain in a segment tree a boolean table d such that d[i]=1 if there no occurrence of x[i] among x[i+1],x[i+2],...,x[j].
- For this purpose maintain an inverse dictionary, mapping each value x[i] to i if d[i]=1.
- For every query of the form (i,j) return the sum of d between indices i and j.
