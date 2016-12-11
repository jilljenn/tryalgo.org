---
layout: en
title:  "Traveling salesman"
category: graphs
problems:
   "tju:Collecting beepers": http://acm.tju.edu.cn/toj/showp2696.html
---

Given a complete oriented arc-weighted graph find a cycle that visits every vertex exactly once (a *Hamiltonian* cycle) and that has minimal length.

## A dynamic programming algorithm in time \\( O(n^2 2^n ) \\)

Let w be the arc lengths.
Let the vertices be numbered from 0 to n-1.  Let vertex n-1 be a source.  For every \\( S \\subseteq \\{0,\\ldots,n-2\\} \\) and every \\( v\\not\\in S \\) we want to find the shortest path from the source to v that traverses all vertices from S exactly once and only those.
Let O[S][v] be this value.

![]({{site.images}}traveling-salesman.svg){:width="400"}

For the base case we have
\\[
        O[\\emptyset][v] = w[n-1][v]
\\]

which is the length of the arc from the source to v.
and for non empty set S
\\[
        O[S][v] = \\min_{u\\in S} O[S \\setminus\\{v\\}][u] + w[u][v].
\\]

The goal is to compute \\( O[\\{0,\\ldots,n-2\\}][n-1] \\).

The claimed complexity follows from the fact that there are \\(O(n 2^n )\\) variables and each needs time \\(O(n)\\) to be computed.

Note: in this algorithm we choose n-1 as the source and not say 0, which makes the set definitions easier.

## The implementation

For these problems the instances are small, say about n=15.  Then we can encode the sets into integers, using the binary decomposition of an integer as the characteristic vector of a set.
For example to loop over all non empty sets \\( S \\subseteq \\{0,\\ldots,n-2\\} \\) we write

{% highlight python %}
for S in range(1, (1<<n-1)):
{% endhighlight %}

and to test if a vertex u belongs to the set S we write

{% highlight python %}
if (1<<u) & S:
{% endhighlight %}

