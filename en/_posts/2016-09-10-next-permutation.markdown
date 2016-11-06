---
layout: en
title:  "Next permutation"
category: permutations
---

Given a table with n integers, compute the permutation which comes lexicographically next, or answer that the given order is maximal. [spoj:NEXTPERM](http://www.spoj.com/SHORTEN/problems/NEXTPERM/).

The given table does not have to be a permutation on $$\{0,1,\ldots,n-1\}$$, it can contain elements with multiplicity.

## Key observation

Given a table $$t=(t_0,t_1,\ldots,t_{n-1})$$ we want to transform it into the lexicographically next one.  For this purpose we want to preserve a longest prefix of t, and have a lexicographically smallest suffix.

## A linear time algorithm

The algorithm consists in 3 steps.  First we need to find the largest index p --- called *pivot* --- such that t[p] < t[p+1].  The idea is that the suffix of t starting at p+1 is a non-increasing sequence and therefore lexicographically maximal.  It such a pivot does not exist, we know that t is already lexicographically maximal.

Now it is clear that t[p] has to be increased, but in a minimal manner. Hence we search for an index s such that t[s] is minimal and t[s] > t[p].  Since p+1 is a valid candidate, such an index always exist.

Once we swapped t[p] with t[s] we obtain a table that is lexicographically larger than the initial table t.  Finally we can sort the suffix of t starting at p+1, in order to obtain a smallest permutation that is lexicographically larger than t.   Note that in order to sort this suffix it suffices to reverse it.

## Example


        initial table |  0  |  2  |  1  |  6  |  5  |  2  | 1
        choose pivot  |  0  |  2  | [1] |  6  |  5  |  2  | 1
        swap          |  0  |  2  | [2] |  6  |  5  | [1] | 1
        reverse       |  0  |  2  |  2  | [1  |  1  |  5  | 6]
        final table   |  0  |  2  |  2  |  1  |  1  |  5  | 6


## Links

* [code](http://pythonhosted.org/tryalgo/_modules/tryalgo/next_permutation.html#next_permutation)
