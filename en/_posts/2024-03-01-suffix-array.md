---
layout: en
title: Suffix Array
category: strings
author: Christoph Dürr
---

Given a string s, sort all cyclic shifts of s. Formally produce a table p such that p[j]=i if s[i:]+s[:i] has rank j among all cyclic shifts.

## Example

On input "bobocel", here are all cyclic shifts, together with by how much they are shifted.

    bobocel 0
    obocelb 1
    bocelbo 2
    ocelbob 3
    celbobo 4
    elboboc 5
    lboboce 6

And the same list, but lexicographically sorted. Together with the rank in the new order.

    0 bobocel 0
    1 bocelbo 2
    2 celbobo 4
    3 elboboc 5
    4 lboboce 6
    5 obocelb 1
    6 ocelbob 3

Hence on this example we should output `p=[0, 2, 4, 5, 6, 1, 3]`.

## Complexity

The naïve algorithm for this problem stores all cyclic shifts in a list and sorts it. This takes time $O(n^2 \log n)$, because the list has size $n$, and comparing two strings of length $n$ takes time $O(n)$.

The problem can be solved in time $O(n)$, under some conditions on the alphabet. But we present an $O(n \log^2 n)$ implementation, which is good enough for most programming contests.

## The key operation

The algorithm relies on a simple sorting function `sort_class`, which not only sorts a given string or list `s`, but also returns additional informations. It returns two tables `p` and `c` such that

- p[j]=i if s[i] has rank j in `sorted(s)`.
- c[i]=j if s[i] has rank j in `sorted(set(s))`.

Note that the second table groups identical elements in s, and gives a rank only to the equivalence classes. For example

    index   =  0123456
    input s = "bobocel"

after sorting s we have for example (because identical letters can be ordered arbitrarily within each other)

    original index =  0245613
    sorted s       = "bbceloo"

If we rank all distinct letters of the input string we have

    rank           = 0 1 2 3 4
    sorted(set(s)) = b c e l o

Hence our function returns

    p = [0, 2, 4, 5, 6, 1, 3]
    c = [0, 4, 0, 4, 1, 2, 3]
    s =  b  o  b  o  c  e  l  # for comparison

## The cyclic version

We present here the cyclic version of the problem. If we want to sort the suffixes of a given string s, then we can just sort the cyclic shifts of s + special, where special is a dummy character, smaller than all characters in s.

## Iteration

The idea is that for K being every integer power of 2, we want to sort the K-lengths prefixes of all cyclic shifts. For example for K=2 and s="bobocel" we want to sort the following strings.

    bo
     ob
      bo
       oc
        ce
         el
          lb

But we already have the order and equivalence classes of all (K/2)-length prefixes of all cyclic shifts. Now every K-lengths prefix is the concatenation of two (K/2)-length prefixes, say `xy`. Let i be the equivalence class of `x` and j be the equivalence class of `y`. Then the pair (i,j) represents the equivalence class of `xy`. We can use `sort_class` to translate the pairs into rank integers. 

The strings of the example above correspond to the following pairs, where the table `c` from the previous iteration makes the correspondance.

    (0, 4)
     (4, 0)
      (0, 4)
       (4, 1)
        (1, 2)
         (2, 3)
          (3, 0)


In total we have a logarithmic number of outer iterations, each costs `O(n log n)`, leading to the claimed complexity.

## Implementation

{% highlight python %}
def sort_class(s):
    """ sorts s and returns additional information

    :param s: string or list
    :returns p, c: p[j]=i if s[i] has rank j in sorted(s) and c[i] is rank of s[i] in sorted(set(s))
    :complexity: O(n log n) or better if sort makes use of specific values in s
    """
    S_index = [(x, i) for i, x in enumerate(s)]
    p = [i for x, i in sorted(S_index)]
    x2c = {x : i for i, x in enumerate(sorted(set(s)))}
    c = [x2c[x] for x in s]
    return p, c


def sort_cyclic_shifts(s):
    """ given a string s, sort lexicographically all cyclic shifts of s.

    The i-th cyclic shift of s is s[i:] + s[i:]
    :param s: string or list
    :returns L: such that L[j]=i if the i-th cyclic shift of s has rank j
    :complexity: O(n * log(n)^2)
    """
    p, c = sort_class(s)
    n = len(s)
    K = 1
    while K <= n:
        L = [(c[i], c[(i + K) % n]) for i in range(n)]
        p, c = sort_class(L)
        K <<= 1 
    return p

def suffix_array(s):
    """ given a string s, sort lexicographically suffixes of s
    :param s: string
    :returns: R with R[i] is j such that s[j:] has rank i
    :complexity: O(n log^2 n)
    """
    special = chr(0)
    assert special < min(s) 
    L = sort_cyclic_shifts(s + special)
    return L[1:]
{% endhighlight %}

## Update September 2024

Programming is often a question of compromise. The implementation of `sort_class` is quite short. But its usage of a dictionary makes it a bit slow. The construction of array `c` can be improved by processing all items in order, as given by p, and keeping track of the distinct values seen so far. This gives an improvement of about 30% in a test we made. In many implementations the sorting of `S_index` is done by two stages of bucket sort. Since the keys are couples of ranks, we can sort first by the second rank, and then do a stable sort on the first rank. This will generate quite some lines of code in Python, and we don't feel ready yet for so much compromise.

{% highlight python %}
def sort_class(s):
    """ sorts s and returns additional information

    :param s: string or list
    :returns p, c: p[j]=i if s[i] has rank j in sorted(s) and c[i] is rank of s[i] in sorted(set(s))
    :complexity: O(n log n) or better if sort makes use of specific values in s
    """
    S_index = [(x, i) for i, x in enumerate(s)]
    p = [i for x, i in sorted(S_index)]
    c = [0] * len(s)
    curr_class = 0
    c[p[0]] = curr_class
    for i in range(1, len(s)):
        if s[p[i]] != s[p[i-1]]:
            curr_class += 1
        c[p[i]] = curr_class
    return p, c
{% endhighlight %}

## References

- [an O(nlogn) implementation in CP-algorithms](https://cp-algorithms.com/string/suffix-array.html) -- describes applications
- [Visualization in action](https://visualgo.net/en/suffixarray?slide=1)
- [Quest for the quickest implementation in Python](https://louisabraham.github.io/articles/suffix-arrays)