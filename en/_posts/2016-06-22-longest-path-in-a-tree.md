---
layout: en
title:  "Longest path in a tree"
category: trees
problems:
   "spoj:PT07Z": http://www.spoj.com/problems/PT07Z/
---

Find a longest path in a tree.

### Dynamic programming

You can choose some vertex as a root, and then do dynamic programming in each subtree. Let A[v] be the length of the longest path in the subtree rooted at v, and starting at v.  In other words A[v] is the depth of the subtree.  Let B[v] be the longest path in the subtree, without any restriction.  Then A[v]=B[v]=0 when v is a leaf and otherwise

    A[v] = max over descendants u of A[u] + 1
    B[v] = max of A[v]
                  A[u1] + 2 + A[u2] where u1≠u2 are descendants
                  B[u] where u is a descendant


### Depth first search

With DFS given a vertex v you can find a furthest vertex v from u.
Start with an arbitrary vertex r to find a furthest vertex u. Then start from u to find a furthest vertex v. The u-v path is a longest path.  It is a nice exercise to prove this claim.

