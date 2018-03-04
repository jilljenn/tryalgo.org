---
layout: en
category: geometry
title: "Sieve of Eratosthenes"
author: Christoph Dürr
problems:
    "hackercup:DownToZeroII": https://www.hackerrank.com/challenges/down-to-zero-ii
---

Compute for every integer n between 0 and N (excluded), the minimum number of operations to reduce it to zero. Allowed operations: decrease by 1 or divide by a factor, not larger than its square root.

## Key ingredient

The key ingredient is the [ieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). This is simple procedure to find all prime numbers below some given integer N. Simply fill a boolean table T, which initially is all True, except for indexes 0 and 1.  Process from index 2 to N (excluded).  When processing p, if T[p] is True, then we know that p is a prime. Now set T[ap] to False for all integers a at least 2, (not exceeding the table size).

This procedure takes time $O(N \log N)$.

## Model as a shortest path problem

We can model the problem as a shortest path problem in an acyclic directed graph, which therefore naturally leads to a dynamic program.
For every vertex we wish to find the distance to the vertex 0.

![shortest path model]({{site.images}}DownToZeroII.svg){:width="600"}

## Dynamic program using decomposition into prime factors

The idea is to compute for every n --- in the range 0 to N --- the distance d[n]  between the vertices n and 0.  Clearly we have d[0]=0 and d[n]= 1 + min(d[n-1], min(d[n/a])), where the second minimum is taken over all factors a of n with a*a <= n.  The dynamic program simply fills the table in order of increasing indexes.

The key difficulty is to find the non-trivial factors for a given integer n.  By *non-trival* we mean factors that are *strictly* between 1 and $n$.  One possibility is to use the sieve of Eratosthenes. Let *F[n]* be the list of all primes dividing $n$. If $p^2$ divides n then p is present twice in the list.
The table F is filled up in order of increasing indexes.

Initially all entries of F are empty.  Then for every $p$ from 2 to $N$, we check if *F[p]* is empty. If it is the case, then $p$ is a prime number and we proceed as follows. For every integer multiple of $p$ not exceeding $N$, namely $p, 2p, 3p$ etc we add $p$ to its list stored in *F*.  Then for every integer multiple of $p^2$ we add again $p$ to its list stored in *F*. And we repeat so for all integer powers of *p*, not exceeding $N$.

Just to create confusion we renamed *F* as *decomp* in the following implementation.

{% highlight python %}
# decomp[n] contains the list of prime factors of n
# if p squared divides n then p is twice in this list
# time complexity could be improved with a dictionary instead of a list
decomp = [[] for _ in range(N)]

for p in range(2, N):  # Eratosthenes
    if not decomp[p]:  # p is a prime number
        k = 1          # power of p
        pk = p         # pk is p to the power k
        apk = pk       # apk will range over all multiples of p ** k
        while apk < N:
            while apk < N:             # stop when table end is reached
                # mark that api has p ** k as factor
                decomp[apk].append(p)  # p will be added k times in total
                apk += pk              # loop over all multiples of p ** k
            k += 1     # now consider the next exponent
            pk *= p    # maintain pk is p to the power k
            apk = pk   # start again at 1 * p ** k
{% endhighlight %}

Now given $n$ we know the list *F[n]* of its prime numbers. Every strict and non-empty sublist *L* of *F[n]* corresponds to a factor of $n$, simply by multiplying all the primes in *L*.

In the implementation below we use a useful function from the module *itertools*, which iterates over all sublists of a given size.

{% highlight python %}
from itertools import combinations
from operator import mul
from functools import reduce

# iterates over all non-trival factors of n
def factors(n):
    for i in range(1, len(decomp[n])):
        for L in combinations(decomp[n], i):
            yield reduce(mul, L)
{% endhighlight %}

Now we can implement the dynamic program.

{% highlight python %}
# d[n]  is the minimal number of steps to reduce n to zero
d = [0] * N

for n in range(1, N):
    d[n] = 1 + d[n - 1]
    for f in factors(n):
        if f > 1 and f * f <= n and d[n] > 1 + d[n // f]:
            d[n] = 1 + d[n // f]
{% endhighlight %}


## Dynamic program using multiplicities

A much easier solution is to implement the dynamic program not by processing all arcs grouped by the source vertex, but grouped by the target vertex.  Suppose that initially $d[n]=n$, which corresponds to repeated applications of the decrement operation, reducing $n$ to zero. We process $n$ from 2 to $N$, with the property that at the moment $n$ is processed, $d[n]$ contains the correct answer. At that moment, we consider all integer multiples of $n$, of the form $an$ with $a<=n$, and $an<=N$, and update $d[an]$ by $min(d[an], 1 + d[n])$, corresponding to a division of $an$ by its factor $a$.

Note that in the implementation below, we make sure that $a$ does not exceed $n$ and that $an$ is strictly smaller than $N$.
{% highlight python %}
d = [n for n in range(N)]

for n in range(2, N):
    for a in range(2, min((N - 1) // n, n) + 1):
        if d[a * n] > 1 + d[n]:
            d[a * n] = 1 + d[n]
{% endhighlight %}

## Complexity

The procedure above makes at most $N/n$ comparisons for every $n$, which sum up to $O(N \log N)$,  using the harmonic number equality $H_N=1+1/2+...+1/N=O(\log N)$.

The Python implementation of the first versions takes 13 seconds, using the pypy interpreter, while the second one takes only 0.4 seconds.

This measures have to be considered with care as they are sensible to the machine environment.
