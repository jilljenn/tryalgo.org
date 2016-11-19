---
layout: en
title:  "The rank of a permutation"
category: permutations
problem_urls: ["http://www.spoj.com/problems/PERMRANK/", "http://www.spoj.com/problems/TPERML/"]
problem_names: ["spoj:PERMRANK", "spoj:TPERML"]
---

Given a permutation on {0,1,...,n-1} find its rank for the lexicographical order. Given a rank find the corresponding permutation.

## Example

Say n=4, then the 4!=24 permutations are lexicographically ordered as follows.

|  rank | permutation |
| -----:| -----------:|
|     0 | 0,1,2,3     |
|     1 | 0,1,3,2     |
|     2 | 0,2,1,3     |
|     3 | 0,2,3,1     |
|     4 | 0,3,1,2     |
|     5 | 0,3,2,1     |
|   ... | ....        |
|    23 | 3,2,1,0     |
| ------| ----------- |

## An observation

Suppose we are given a permutation $$(p_{n-1},\ldots,p_1,p_0)$$ and which to compute its rank.

How many permutations start with a 0? Well the remainder is a permutation over {1,..,n-1}, and all these permutations are valid completions of the initial 0. Hence there are $$(n-1)!$$ permutations that start with a 0.  Similarly there are $$(n-1)!$$ permutations that start with a 1, and in the lexicographical order they come after those that start with a 0.  This means that a first contribution to the rank is $$p_{n-1} \cdot (n-1)!$$.

The situation for the next value $$p_{n-2}$$ is slightly different. Again there are $$(n-2)!$$ permutation that start with fixed values $$p_{n-1},p_{n-2}$$.  However there are only $$n-1$$ possibilities for $$p_{n-2}$$, namely all n values excluding $$p_{n-1}$$.  This means that the second contribution to the rank is $$r_{n-2} \cdot (n-2)!$$, where $$r_{n-1}$$ is the rank of $$p_{n-2}$$ among the set $$\{0,1,\ldots,n-1\} \setminus \{p_{n-1}\}$$.  The key is then to translate a vector $$p$$ defining a permutation into a vector of ranks $$r$$ such that $$r_i$$ is the rank of $$p_i$$ among the values $$\{p_{i},\ldots,p_1,p_0\}$$.  For example if p=(2,0,3,1), then r=(2,0,1,0).  The rank of p is then

$$r_{n-1} \cdot (n-1)! + \cdots + r_2 \cdot 2! +  r_1 \cdot 1! \cdot + r_0.$$

Note that $$r_0$$ can safely be omitted in the expression since it is always zero.

The trick is then to compute the ranks $$r_i$$ from the values $$p_i$$.

## An $$O(n^2)$$ algorithm

For this purpose we parse the permutation p, keeping track of the values which have not yet be seen so far and search among them to determine the rank.  We maintain a list *digits* contains all values which have not yet seen in the given permutation.  Note that the last element of the permutation can be ignored, it does not provide any information for the rank.


{% highlight python %}
def permutation_rank(p):
    """Given a permutation of {0,..,n-1} find its rank according to lexicographical order

       :param p: list of length n containing all integers from 0 to n-1
       :returns: rank between 0 and n! -1
       :beware: computation with big numbers
       :complexity: `O(n^2)`
    """
    n = len(p)
    fact = 1                                 # compute (n-1) factorial
    for i in range(2, n):
        fact *= i
    r = 0                                    # compute rank of p
    digits = list(range(n))                  # all yet unused digits
    for i in range(n-1):                     # for all digits except last one
        q = digits.index(p[i])
        r += fact * q
        del digits[q]                        # remove this digit p[i]
        fact //= (n - 1 - i)                 # weight of next digit
    return r
{% endhighlight %}

For the inverse, decompose r into

$$ r_{n-1} (n-1)! + \cdots +  r_2 \cdot 2! + r_1 \cdot 1! + r_0$$

with $$0\leq r_i \leq i$$
and map each $$r_i$$ to the value of rank i among the values {0,...n-1} which have not seen so far.

{% highlight python %}
def rank_permutation(r, n):
    """Given r and n find the permutation of {0,..,n-1} with rank according to lexicographical order equal to r

       :param r n: integers with 0 ≤ r < n!
       :returns: permutation p as a list of n integers
       :beware: computation with big numbers
       :complexity: `O(n^2)`
    """
    fact = 1                                # compute (n-1) factorial
    for i in range(2, n):
        fact *= i
    digits = list(range(n))                 # all yet unused digits
    p = []                                  # build permutation
    for i in range(n):
        q = r // fact                       # by decomposing r = q * fact + rest
        r %= fact
        p.append( digits[q] )
        del digits[q]                       # remove digit at position q
        if i != n - 1:
            fact //= (n - 1 - i)            # weight of next digit
    return p
{% endhighlight %}


## An $$O(n \log n)$$ algorithm

In order to compute the rank of a permutation we use a table called *rank* which maps a value $$p_i$$ to a rank $$r_i$$ as explained above. Initially the table has the identity ranks, i.e. rank[x]=x.  Then after each processed value $$p_i$$ we need to decrement all ranks in *rank* between the indices $$p_i$$ and $$n-1$$.  We can use a [segment tree]({% post_url en/2016-06-25-segment-tree %}) for this purpose.  Then the decrement and access operations to the rank table can be done in logarithmic time.

## Variant

Let s be some string of length n. We can ask the same question about permutations of s.  The difficulty is that there can be repetitions of a same letter in s.  Do you know how compute the rank-permutation bijection for this variant?

