---
layout: en
title: Longest increasing subsequence
author: Jill-Jênn Vie
excerpt_separator: <!--more-->
---

If we want to find the longest (strictly) increasing subsequence of an array $a$ of size $n$, of course we can assume that $dp[i]$ is the answer for the first $i$ elements and then, as a LIS of size $n$ contains a LIS of size $n - 1$:

$$dp[i] = \max_{\substack{j < i\\ a_j < a_i}} dp[j] + 1$$

This gives a first algorithm in $O(n^2)$. Can we do better?

- We do not need to remember all LIS of size $\ell$. We just need to remember the smallest end for a LIS of size $\ell$, called $t[\ell]$.
- The list of smallest ends happens to be increasing (but not necessarily a subsequence). Each $t[\ell]$ forces $t[\ell - 1]$ to be lower.

In this case, we can binary search for the opt LIS to which we can add one element. This gives $O(n \log n)$. I think this is an example of [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html).

I was wondering what was the $O(n \log n)$ that relies on a segment tree. A [blog post on Codeforces](https://codeforces.com/blog/entry/101210) had the answer (of course!). We need to define a new dp:  
$dp[i, v]$ is the LIS using first $i$ elements finishing in $v$. Then we just need to do a min query over $dp[i, 1:v - 1]$.

(A notebook is on the way.)
