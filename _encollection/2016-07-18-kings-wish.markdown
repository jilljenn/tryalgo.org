---
layout: en
title:  "King's Wish"
author: Christoph Dürr,  Henrique Gasparini Fiuza Do Nascimento, Vo Van Huy
category: arithmetics
---

A K by K grid has to be tiled with L by W tiles which can be taken vertically or horizontally.  Given K find L, W such that this tiling is possible and (max(L,W)-min(L,W), L+W) is lexicographically maximal subject to W ≤ L < K.  All numbers are positive integers.
See [King's Wish](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2873).


## A Lemma

We claim that for every valid L, W pair we must have that L and W divide K.

As far as we remember the proof is not trivial, and might along the lines of the proofs of another related theorem (see reference below)

## The algorithm

Decompose K into prime factors of the form

    \\( K = p_1 ^a_1 \\ldots p_r ^a_r \\)

for distinct primes \\(p_1,\\ldots,p_r\\) and positive integers \\(a_1,\\ldots,a_r\\).  First if r=1 then there is no solution.
Else every solution has the following shape

    \\( L = K / p_i ,   W = K / p_i ^a_i. \\)

One you have the decomposition of K into factors, it is easy to try all r candidate solutions and pick the best one.

The Sieve of Eratosthenes will take time roughly \\( O(\\sqrt K ) \\) which is of the order of a million with the given bounds.  Since \\( r \\in O(\\log K) \\) the algorithm has acceptable complexity.


## References

Most available implementations of Edmond's blossom algorithm are a bit long (who can blame?), but the following by David Eppstein is quite elegant:

- [A related theorem with 14 proofs](https://www.maa.org/sites/default/files/pdf/upload_library/22/Ford/Wagon601-617.pdf)

