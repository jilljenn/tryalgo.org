---
layout: fr
title: Comment décomposer un nombre en facteurs premiers ?
author: Christoph Dürr
---

Étant donné n on veut produire en temps linéaire deux tableaux factor et primes, tel que primes contienne tous les nombres premiers entre 2 et n, et que factor[x] contienne le plus petit facteur de x, avec facteur[x]==x si x est premier.

## Le crible de Misra-Gries

Un défaut du [crible d'Eratosthène](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne) est qu'il barre plusieurs fois un même nombre non premier.  Il existe une amélioration proposée par  David Gries et Jayadev Misra en 1978 qui évite ce défaut et qui a une complexité théorique $O(n)$, voir l'[article original](https://www.cs.utexas.edu/users/misra/scannedPdf.dir/linearSieve.pdf).  On gagne donc un facteur $\log \log n$.  Leur algorithme n'est pas beaucoup plus long mais la constante multiplicative dans la complexité est un peu plus grande. Nos expériences ont observées une amélioration des temps de calcul avec en général un facteur $1/2$ pour l'interpréteur `pypy`, mais une déterioration avec un facteur $3$ pour l'interpréteur `python3`.

Dexter Kozen a montré que l'algorithme peut en même temps produire un tableau *factor* qui associe à tout entier $2\leq x < n$ le plus petit facteur entier de $x$.  Ce tableau est très utile pour produire une décomposition en facteurs premiers d'un entier donné.
L'algorithme se base sur une décomposition unique des nombres non premiers. En effet tout entier $y$ peut s'écrire de la forme
$$
  y = \textrm{factor[y]} \cdot x
$$
avec $\textrm{factor}[y] \leq \textrm{factor}[x]$.

L'algorithme énumère tous les entiers non premiers en bouclant d'abord sur $x=2,\ldots,n-1$, puis sur tous les nombres premiers $p$, avec $p\leq \textrm{factor}[x]$, $p$ jouant le rôle de $\textrm{factor}[y]$ dans l'expression $y=p\cdot x$.  L'algorithme est correct, car au moment de traiter $x$, il a déjà trouvé tous les nombres inférieurs ou égaux à $x$ ainsi que le plus petit facteur de $x$.  Comme tout nombre $y$ entre 2 et $n-1$ est traité exactement une fois, la complexité de l'algorithme est $O(n)$.

{% highlight python %}
def gries_misra(n):
    """Prime numbers by the sieve of Gries-Misra
    Computes both the list of all prime numbers less than n,
    and a table mapping every integer 2 ≤ x < n to its smallest prime factor

    :param n: positive integer
    :returns: list of prime numbers, and list of prime factors
    :complexity: O(n)
    """
    primes = []
    factor = [0] * n
    for x in range(2, n):
        if not factor[x]:      # no factor found
            factor[x] = x      # meaning x is prime
            primes.append(x)
        for p in primes:       # loop over primes found so far
            if p > factor[x] or p * x >= n:
                break
            factor[p * x] = p  # p is the smallest factor of p * x
    return primes, factor
{% endhighlight %}
