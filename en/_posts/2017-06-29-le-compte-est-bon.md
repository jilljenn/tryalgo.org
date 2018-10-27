---
layout: en
title:  "Forming arithmetic expression meeting target value"
category: arithmetics
author: Christoph Dürr and Jean-Christophe Filliatre
---

Given n integers and a target value form an arithmetic expression evaluating to the target value.

## Summary

You are given the integers 3, 100, 8, 8, 10, 6 and need to approach the target value 683.  The allowed operations are addition, multiplication, subtraction (only if the result is positive) and division (only if the result is integer).  And every given integer can appear at most once in the solution. A solution in this example would be

    6 * 100 + 8 * 10 + 3 = 683.

## Complexity

One can use dynamic programming to solve the problem, even though the resulting complexity would be huge.

We could upper bound it by the number of arithmetic expressions one can form with the given numbers, regardless of the restrictions on the subtraction and division.  Then even restricting to expressions involving all n given numbers there are quite many expressions.  An expression can be viewed as a binary tree with n leafs, and hence n-1 inner nodes.  The number of those trees is the [Catalan number](https://en.wikipedia.org/wiki/Catalan_number) $C_{n-1}$, which is $(2n-2)!/(n!(n-1)!)$.  This number needs to be multiplied by $4^{n-1}$ corresponding to the number of possibilities to assign one of the four operators to each of the inner nodes.

Due to the constraints on subtractions and divisions, the actual number of valid expressions might be smaller than this rough estimation, but nevertheless it is huge.
Hence the algorithm is practical only for small n, say less than 10.


### Dynamic Program

Let $x_0,x_1,\ldots,x_{n-1}$ be the given integers.
We denote by $S\subseteq\\{0,1,\\ldots,n-1\\}$ a selection of these integers.
In a table `expr` we store for every set S in `expr[S]` a dictionary. It contains (key, value) pairs of the form `(v,f)` where `f` is a valid arithmetic expression formed by the integers $\\{x_i:i\\in S\\}$  and `v` is the value of `f`.

Initially `expr[{i}]` is a dictionary associating to the value $x_i$ the singleton expression $x_i$.  Then for every non-singleton set $S$ we populate the dictionary `expr[S]` as follows.
Any arithmetic expression involving the integers $\\{x_i:i\\in S\\}$ consists of an arithmetic expression tree with some operator `op` in the root and a left subtree over a set $L$ and a right subtree over a set $R$ where $L$ and $R$ are non-empty sets partitioning $S$.  Therefore for fixed set $S$ we loop over all non-empty strict subsets $L\subset S$.  For each $L$ we set $R=S\setminus L$ and loop over all values $v_L$ in `expr[L]` and all values $v_R$ in `expr[R]`.  Now for each operator `op` among +,*,-,/ for which $v:=v_L \textrm{op} v_R$ is a valid expression we can associate in `expr[S]` to the key $v$ the expression `expr[L][`$v_L$`] op expr[R][`$v_R$`]`.

![]({{site.images}}arthm-expr-target.svg "A decomposition of an arithmetic expression." ){:width="600"}

These operations need to be done for all sets $S$ in a lexicographical order that ensures that all subsets  of $S$ have already been processed.

### Implementation details

Since $n$ is a very small number it is most convenient for us to represents sets as integers. For example the set $S={0,3,4}$ is represented as the integer $2^0 + 2^3 + 2^4$.  This has the advantage that bit manipulation operators can be used to encode set operators. For example the bitwise and denoted `&` corresponds to the intersection and the test `L & S == L` tests whether the set encoded by $L$ is a subset of the set encoded by $S$.


{% highlight python %}
def arithm_expr_target(x, target):
    """ Create arithmetic expression approaching target value
    :param x: allowed constants
    :param target: target value
    :returns: string in form 'expression=value'
    :complexity: huge
    """
    n = len(x)
    expr = [{} for _ in range(1 << n)]  # expr[S][val] = string of expr. of value val using only values from set S
    for i in range(n):
        expr[1 << i] = {x[i]: str(x[i])}   # store singletons
    tout = (1 << n) - 1
    for S in range(3, tout + 1): # 3 = first number which is not a power of 2
        if expr[S] != {}:
            continue             # in that case S is a power of 2
        for L in range(1, S):    # decompose set S into non-empty sets L and R
            if L & S == L:
                R = S ^ L
                for vL in expr[L]:         # combine expressions from L
                    for vR in expr[R]:     # with expressions from R
                        eL = expr[L][vL]
                        eR = expr[R][vR]
                        expr[S][vL] = eL
                        if vL > vR:        # difference cannot become negative
                            expr[S][vL - vR] = "(%s-%s)" % (eL, eR)
                        if L < R:   # briser la symétrie
                            expr[S][vL + vR] = "(%s+%s)" % (eL, eR)
                            expr[S][vL * vR] = "(%s*%s)" % (eL, eR)
                        if vR != 0 and vL % vR == 0:  # only integer divisions
                            expr[S][vL // vR] = "(%s/%s)" % (eL, eR)
    # chercher expression la plus proche du but
    for dist in range(target + 1):
        for sign in [-1, +1]:
            val = target + sign * dist
            if val in expr[tout]:
                return "%s=%i" % (expr[tout][val], val)
    # partie jamais atteinte si x contient des nombres entre 0 et but
    pass
{% endhighlight %}