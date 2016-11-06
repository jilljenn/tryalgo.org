---
layout: post
title:  "Rank in suffix"
category: segment tree
excerpt_separator: <!--more-->
---

Given an integer table t1,...,tn compute for every position 1≤i≤n the rank of t[i] among the suffix t[i,...,n] that is the number of j≥i such that t[j]≤t[i].  See [puchi and luggage](https://www.hackerearth.com/code-monk-sorting/algorithm/puchi-and-luggage/).


![]({{ site.images }}rank-in-suffix.svg "The rank of element 7 is 4, since 4 elements after 7 are smaller than 7.")

<!--more-->


## A solution in time $$O(n \log n)$$

First suppose that all values in t are between 0 and n-1.  This can be done by creating a sorted copy of t, say s, and compute a reverse lookup table $$s^{-1}$$, that maps every value from $$t$$ to the index of the first occurrence in $$s$$.

Then the trick is to process the table from the end to the beginning. Maintain a segment tree, which is a data structure encoding a table A of size n (initially all zero), allowing the following operations to run in time $$O(\log n)$$:

- query A[0] + A[1] + ... A[r]
- increment A[r].

## The algorithm

- Make a copy s of t.
- sort s
- remove duplicate elements from s
- build a dictionary $$s^{-1}$$ such that $$s^{-1}[s[i]] = i$$
- For each i from n-1 down to 0:
  - compute $$r = s^{-1}[t[i]]$$
  - increment A[r] by 1
  - the answer associated to i is A[0] + ... + A[r]
- output the answers in increasing order of i

## Notes

In the above mentioned problem *puchi and luggage* the specification excluded t[i] from the suffix in which the rank is to be found. Hence all answers have be produced decremented by 1.  This can be obtained by swapping the two segment tree instructions *increment* and *prefix sum* in the above algorithm.
