---
layout: en
category: graphs
title: "Quadrangle Inequality trick for dynamic programs"
author: Christoph Dürr
problems:
   "spoj:IITKESO207SPA3C": https://www.spoj.com/problems/IITKESO207SPA3C/
   "aizu:ALDS1_10_D": https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_D
---

Given an ordered list of keys with frequencies, build a binary search tree on those keys which minimizes the sum over all keys of its frequency multiplied by its level in the tree.

## Definition

In the 1970's a technique was discovered by Knuth and generalized in the 1980's by Yao, which permits to speedup a dynamic program of a particular form and particular property.

We illustrate the technique on the following problem. Informally, we want to construct a binary search tree, over given keys, which minimizes the average query cost.

Formally, we are given some keys numbered from $1$ to $n$, together with frequency vectors 

$$
    \begin{array}{cccc}
        &\beta_1&   &\beta_2&   &\ldots&  &\beta_n \\
    \alpha_0&   &\alpha_1&  &\alpha_2 & &\alpha_{n-1}&   &\alpha_{n}
    \end{array}
$$

such that $\beta_i$ is the frequency of queries of the $i$-th key, $\alpha_i$ is the frequency of a query between the $i$-th and the $i+1$-th key, and $\alpha_0, \alpha_n$ have obvious interpretations.
 
A binary search tree is a rooted tree where
- every inner node is associated to a key index $i$ and has weight $\beta_i$,
- inner nodes have a left and a right subtree,
- every leaf has weight $\alpha_i$.
Such a tree has to satisfy the usual left-to-right ordering according to the indices of the keys.

![Optimal search tree]({{site.images}}optimal_search_tree_1n.png){:width="600"}

The cost of a tree is called the *weighted path length* and is defined as the sum over all nodes of the weight of the node multiplied with the level of the node in the tree.

An optimal search tree can be computed using dynamic programming. For every $0\leq i\leq j\leq n$ consider the problem of building the optimal search tree for queries restricted to be strictly between the $i$-th key and the $j+1$-th key. We call it the *problem restricted to* $(i,j)$, or *subproblem*. We consider the following values.
- $C[i,j]$ is the cost of the optimal search tree
- $W[i,j]$ is the total frequency of the restricted problem. It is $\alpha_i + \beta_i + \alpha_{i+1}+\beta_{i+1}+\ldots+\beta_{j}+\alpha_j$.
- $R[i,j]$ is the root of the optimal search tree. It is defined only for $i < j$ and satisfies $i+1 \leq R[i,j] \leq j$.

These values lead to the following dynamic program. For the base case $i=j$ we have

$$
    C[i,i] = W[i,i] = \alpha_i
$$

and for $i < j$ we have

$$
    C[i,j] = W[i,j] + \min_{i+1\leq r\leq j} (C[i,r - 1] + C[r,j]) \\
    R[i][i] = \textrm{argmin of above expression}.
$$

The optimal search tree of the subproblem consists of some root $i+1\leq r\leq j$, which motivates the minimum expression above. The addition of $W[i,j]$ comes from the fact that by attaching the left and right subtrees under the root $r$, the level of all their nodes increases by $1$. Since root $r$ has level one, the weight $\beta_r$ has to enter the cost of the tree as well.

![Optimal search tree decomposition]({{site.images}}optimal_search_tree_ij.png){:width="400"}

This leads to a time complexity of $O(n^3)$, because we have $O(n^2)$ variables, each being the minimum over $O(n)$ alternatives.

## Improvement to $O(n^2)$

Donald Knuth made this clever observation 50 years ago, that the root does not have to be searched within the full range. The following range is enough:

$$
        R[i,j - 1] \leq R[i,j] \leq R[i + 1,j],         \tag{(1)}
$$ 

and therefore

$$
        C[i,j] = W[i,j] + \min_{R[i,j-1]\leq r\leq R[i+1,j]} (C[i,r - 1] + C[r,j]).
$$

This would mean that the time needed to compute $R[i,j]$ is proportional to $R[i,j-1] - R[i+1,j] + 1$. Summing up over all $i,j$ with fixed difference $j-i$, we obtain a telescopic sum of value $O(n)$. Hence the total time complexity is $O(n^2)$.

## A general framework

Such an improvement applies under some condition to any dynamic program of the form

$$
    C[i,i] = 0 \\
    C[i,j] = W[i,j] + \min_{i<k\leq j} (C[i,k-1]+C[k,j]) \mbox{ for } i < j.
$$

The dynamic program above, in essence depends on the matrix $W$. And it is the structure of $W$, which permits the above mentioned improvement. Two properties of $W$ are essential.
1. $W$ satisfies the quadrangle inequality (denoted QI for short) if for every $a\leq b\leq c\leq d$ we have

$$
    W[a,c] + W[b,d] \leq W[b,c] + W[a,d]  
$$

2. $W$ is monotone on the lattice of intervals if  for every $a\leq b\leq c\leq d$ we have

$$
    W[b,c] \leq W[a,d].
$$

F. Frances Yao shows that whenever $W$ satisfies the two properties, then the inequality (1) holds, which allows to solve the dynamic program in quadratic time.

This holds for a variety problems, such as
- Optimal binary search tree for given query frequencies
- Given sets of strings $S_1,\ldots,S_n$, compute the multi-set of strings obtained by concatenating a string from $S_1$ with a string from $S_2$ and so on and finally concatenating with a string from $S_n$. Every concatenation between two strings generates one unit of cost. The goal is to perform the task at minimum cost.
- Compute the triangulation of a convex polygon, minimizing the total length of the added segments.

## The proof idea

For the formal proof we refer to Yao's paper, referenced at the bottom of this document. In a nutshell it consists of the following steps.

**Lemma 1** If $W$ satisfies QI and is monotone on the lattice of intervals, then $C$ also satisfies QI.

<details>
  <summary>Proof</summary>
The proof of

$$
    C[a,c] + C[b,d] \leq C[b,c] + C[a,d] \mbox{ for all } a\leq b\leq c\leq d  
$$

is by induction on the difference $d-a$. When $a=b$ or $c=d$, both sides of the inequality are identical. This establishes the base case $d-a\leq 1$. The induction step considers two cases.
1. **Case $a<b=c<d$** In this case the inequality to show becomes the inverse triangular inequality

$$
    C[a,b]+C[b,d] \leq C[a,d] \mbox{ for all } a<b<d.
$$

Let $k$ be the minimizer for the expression of $C[a,d]$, i.e. $C[a,d]=C_k[a,d]$, using the notation $C_k[a,d] :=  W[a,b] + C[a,k-1]+C[k,b]$. If $k\leq b$ we have

$$
    C[a,b]+C[b,d] \leq C_z[a,b] + C[b,d] \tag{(by opt. of $C[a,b]$)} \\
    = W[a,d] + C[a,k-1]+C[k,b] + C[b,d] \\
    \leq W[a,d] + C[a,k-1] + C[k,d] \tag{(by ind. hyp., using $a<k$)}\\
    = C[a,d]. \tag{(by choice of $k$)}
$$

The case $k > b$ is similar.
2. **Case $a<b<c<d$** Let $k,\ell$ be such that 

$$
    C[b,c] = C_k[b,c] \mbox{ and } C[a,d] = C_\ell[a,d].
$$

If $\ell\leq k$ we have

$$
    C[a,c] + C[b,d] \leq C_\ell[a,c] + C_k[b,d] \tag{(by opt. of $C[a,c]$ and $C[b,d]$)} \\
    = W[a,c] + W[b,d] +C[a,\ell-1] + C[k,c] + C[b,k-1]+C[k,d] \\
    \leq W[b,c] + W[a,d] +C[a,\ell-1] + C[k,c] + C[b,k-1]+C[k,d] \tag{(by QI of $W$)} \\
    \leq W[b,c] + W[a,d] +C[a,\ell-1] + C[b,k-1]+C[k,c] + C[\ell,d] \tag{(by ind. hyp.)} \\
    = C_k[b,c] + C_\ell[a,d] \\
    = C[b,c] + C[a,d].
$$

The case $\ell > k$ is similar. And this concludes the proof.
</details>

**Lemma 2** If $C$ satifies QI, then

$$
    K[i,j] \leq K[i,j+1] \leq K[i+1,j+1] \mbox{ for } i\leq j,
$$

where $K[i,j]$ is the minimizer of the minimum expression in the definition of $C[i,j]$, and for convenience we denote $K[i,i]=i$.

<details>
  <summary>Proof</summary>
It holds by definition of $C$ when $i=j$. To show the first inequality in case $i<j$, we will show for $a < b\leq c < d$

$$
    \left[ C_c[a,d] \leq C_b[a,d] \right] \Rightarrow 
    \left[ C_c[a,d+1] \leq C_b[a,d+1] \right].      \tag{(2)}
$$

By the quadrangle inequality we have 

$$
    C[b,d]+C[c,d+1] \leq C[c,d] + C[b,d+1].
$$

And if we add $W[a,d]+W[a,d]+C[a,b-1]+C[a,d-1]$ to both sides we obtain

$$
    C_b[a,d]+C_c[a,d+1] \leq C_c[a,d]+C_b[a,d+1]
$$

which show the implication (2). The proof for the second inequality is similar.
<details>


## Implementation in Python

~~~Python
def optimal_search_tree(alpha, beta):
    """ Compute an optimal search tree

    :param alpha, beta: lists of probability weights index from 0 to n (included)
    :assumes: beta[0] = 0
    :returns: weighted path length of optimal tree and the actual tree. 
              A tree is either an empty list or a list of the form [left, root, right].
    :complexity: O(n^2)
    """
    n = len(alpha) - 1
    P = [[0 for j in range(n+1)] for i in range(n+1)] # cost of subproblem (i,j)
    W = [[0 for j in range(n+1)] for i in range(n+1)] # total weight of subproblem (i,j)
    R = [[0 for j in range(n+1)] for i in range(n+1)] # root of optimal tree for subproblem (i,j)

    for i in range(n + 1):
        # empty trees
        C[i][i] = W[i][i] = alpha[i]
        # weight of index range
        for j in range(i + 1, n + 1):
            W[i][j] = W[i][j - 1] + beta[j] + alpha[j]

    # single node trees
    for i in range(n):
        j = i + 1
        R[i][j] = j
        C[i][j] = C[i][i] + C[j][j] + W[i][j]  
    
    # recursion
    for j_i in range(2, n + 1): # difference between j and i
        for i in range(n - j_i + 1):
            j = i + j_i
            argmin = None
            valmin = float('+inf')
            for r in range(R[i][j - 1], R[i + 1][j] + 1):
                alt = C[i][r - 1] + C[r][j]
                if alt < valmin:
                    valmin = alt
                    argmin = r 
            C[i][j] = W[i][j] + valmin
            R[i][j] = argmin 
     
    # extract solution
    tree = extract_tree(R, 0, n)
    return C[0][n], tree 


def extract_tree(R, i, j):
    """ returns the tree for the subproblem (i,j)
    """
    if i >= j:
        return []
    else:
        root = R[i][j]
        left = extract_tree(R, i, root - 1)
        right = extract_tree(R, root, j)
        return [left, root, right]
~~~




## References

The first reference is the original paper introducing the quadratic time algorithm. There were many followup researchs, which are summarized in the second reference.

- Knuth, D. E., [Optimum binary search trees](https://doi.org/10.1007/BF00264289), Acta Informatica, 1(1), pages 14–25, 1971.
- Yao, F. Frances. [Efficient dynamic programming using quadrangle inequalities.](https://dl.acm.org/doi/pdf/10.1145/800141.804691) Proceedings of the twelfth annual ACM symposium on Theory of computing. 1980.
- Nagaraj, S. V.  [Optimal binary search trees](https://doi.org/10.1016/S0304-3975(96)00320-9), Theoretical Computer Science, 188(1–2), pages 1-44, 1997.

