---
layout: page
title: Ecole Centrale Supélec s'entraîne
---

# Lundi 14 oct 2019, 13-15:30

Présents : Christoph, Adnane, Victor, Francisco.

On a parlé des problèmes suivants:

-   [wordladder](https://www.spoj.com/problems/UFPT2015G/) — Calculer par BFS les distances entre les mots du dictionnaire. Variante 1: insérer des sommets correspondant à des remplacements de lettres, par exemple W_RD. Christoph: je n'ai pas encore réussit à faire passer ma solution.
-   [Radar Installation](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3634) — vu en TD. Réduction vers couverture d'intervalles. Soution gloutone.
-   [Frosting on the Cake](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=5215) — sommer les longueurs des colonnes et lignes de même modulo par 3
-   [Taxi Cab Scheme](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3642) — réduction vers le problème de couverture d'un DAG par un nombre minimum de chemins: graphe biparti U = sommets correspants aux destinations des requêtes, V = .. au sources des requêtes, il y a une arête si un taxi a assez de temps de servir les deux requêtes. Couplage dans ce graphe: un arête du couplage indique que c'est le même taxi qui sert les deux requêtes. Le nombre de taxi utilisés est le nombre de requêtes moins la taille du couplage
-   [Mission Improbable](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=5108) — expliqué [ici](https://tryalgo.org/en/matching/2017/05/31/mission-improbable/).
-   [Landscaping](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4908) — se réduit vers un problème de coupe. Un sommet par case, ainsi qu'une source s et un puits t. Les poids sur les arêtes: si la case x est haute c(s,x)=0, c(x,t)=a, si la case est basse c(s,x)=b, c(x,t)=0. Entre deux cases adjacentes x,y il y a une arête de poids c(x,y)=b. Une coupe correspond à un solution, et la valeur de la coupe est la valeur de la solution.
-   [Manhattan](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1260) — se réduit vers 2-SAT. Une variable booléenne par route indicant son orientation. Imaginons que pour une route on demande (x et y) ou (a et b). Ceci est équivalent à (x ou a) et (x ou b) et (y ou a) et (y ou b), qui sont des clauses 2-SAT. — résoudre une formule 2-SAT: chaque clause x ou y, génère deux implications non x => y et non y => x. Alors construire un graphe orienté avec ces arcs. Si pour une variable x il existe un chemin de x à non x et de non x à x, alors la formule n'est pas satisfiable, sinon elle l'est.

# Lundi 21 oct, 12h avec son repas

Café CROUS du bâtiment Eiffel. On parlera des problèmes:

-    [Honest Rectangle](https://www.spoj.com/problems/RECTANGLE/) — en détail, avec code
-    [Dragon Maze](https://code.google.com/codejam/contest/2929486/dashboard#s=p3)
-    [Stock Charts](https://code.google.com/codejam/contest/204113/dashboard#s=p2)
-    [Poker Hands](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1256) — avec code
-    [Anagram checker](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=84)
-    [Weird Advertisement](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=3134)

# Honest Rectangle


## Idea

Conceptually, we fill a matrix M with rows indexed by h and columns indexed by
w. M[x,y] contains x * y.  Avery gets a value from this matrix, while Pat gets
an anti-diagonal. We will erase entries corresponding to (w,h) pairs which are
not compatible with the conversation. The surviving entries are the solution.

|   "Avery: I don't know what w and h are." 
|   means that we erase all entries which are unique, 
|
|   "Pat: I knew that." 
|   means we erase all anti-diagonals where we erased individual entries.
|
|   "Avery: Now I know what they are." 
|   means we erase all entries which are not unique among the remaining entries.
|
|   "Pat: I now know too." 
|   means we erase all anti-diagonals which do not contain exactly one entry.

## Implementation

We don't really store the matrix M, but maintain an bookkeeping array, namely:

count_prod[y] is the number of non-deleted pairs (w,h) 
    such that w * h = y.

The function count_unique uses this table to determine for each anti-diagonal
how many entries it has which are unique in M.

## Complexity

in the order of 5 * U^2, which is ok for U = 1000

## Code

~~~ python
import sys, string

def readint(): return int(sys.stdin.readline())

def readstr(): return sys.stdin.readline().strip()

L = readint()
U = readint()

possibilities = [(w, h) for w in range(L, U + 1) for h in range(w, U + 1)]
count_prod = [0] * (U * U + 1)

"""
returns a table unique, such that unique[y] is the number of pairs (w,h) 
    with w + h == y and count_prod[w * h] == 1.
"""
def count_unique():
    unique = [0] * (U + U + 1)
    for w, h in possibilities:
        if count_prod[w * h] == 1:
            unique[w + h] += 1
    return unique


for w, h in possibilities:   # add all possible pairs
    count_prod[w * h] += 1

unique1 = count_unique()

for w, h in possibilities:   # remove pairs after Pat says: I knew that.
    if unique1[w + h] > 0:
        count_prod[w * h] -= 1

unique2 = count_unique()

for w, h in possibilities:   # filter surviving pairs
    if unique1[w + h] == 0 and unique2[w + h] == 1 and count_prod[w * h] == 1:
        print(w, h)
~~~

# [wordladder](https://www.spoj.com/problems/UFPT2015G/) — Help Needed, not accepted by SPOJ


Compute distances in a Hamming distance defined graph on given words.

## complexity 

    n * k * 27 * 2  +  n * n * k

for n the number of words and k their length.
which is about 8 million. should be ok.

## General approach

Use BFS to compute the distances from the source word. Do the same for the
target word. Then if target is reachable from source, we have already one
candidate solution distance. Next we iterate over all words u reachable from
source and all words v reachable from target with Hamming distance 2 between u
and v.  We compute the lexicographical smallest word in between u and v. This
gives us another candidate solution.
We keep the best candidate solution.

A solution is a pair (distance, added_word), where it comes in handy that "0"
is smaller as all given words.

## (Improvements)[https://runestone.academy/runestone/books/published/pythonds/Graphs/BuildingtheWordLadderGraph.html
]

For the BFS we could iterate over all 27 * 8 possible neighbors of a word and
check if they belong to the dictionary. But we could also precompute a list of
words for every replacement. For example replace["AB.C"] would contain all
words from the dictionary that match the regular expression "AB.C".   Doing
this the complexity will reduce to n * k * 2 * a, where a is the average
number of words which differ at the same position, which likely to be a small
constant, much less than 27.  The second part will have complexity n * k ** 2 *
b, where b is the average number of words which differ in exactly two
positions, also expected to be much smaller than 27 ** 2.

Experiments show that that we gain a factor of 5 at least in the running time.

## Code 

~~~ python
import sys, string
from collections import defaultdict

def readint(): return int(sys.stdin.readline())

def readstr(): return sys.stdin.readline().strip()

n = readint()
tout = [readstr() for _ in range(n)]
dico = set(tout)
Pos = range(len(tout[0]))

def all_remove1(w):
    for p in Pos:
        yield w[:p] + "_" + w[p+1:]

def all_remove2(w):
    for q in Pos:
        for p in range(q):
            yield w[:p] + "_" + w[p + 1: q] + "_" + w[q + 1:]

all_replace1 = defaultdict(lambda: set())
for w in tout:
    for remove1 in all_remove1(w):
        all_replace1[remove1].add(w)

all_replace2 =  defaultdict(lambda: set())
for w in tout:
    for remove2 in all_remove2(w):
        all_replace2[remove2].add(w)

def distances(start):
    Q = [start]
    d = {start : 0}
    while Q:
        w = Q.pop()       # BFS
        for remove in all_remove1(w):
            for replace in all_replace1[remove]:
                if replace in dico and replace not in d:
                    d[replace] = d[w] + 1
                    Q.append(replace)
    return d

def two_steps(u, v):
    """If Hamming distance is 2, returns a string in between at Hamming distance
       1 from u and from v and minimal in lexicographical order. 
       Otherwise returns None.
    """
    # positions where u and v differ
    p = [i for i in Pos if u[i] != v[i]]
    if len(p) != 2:
        return None
    i, j = p
    if u[i] < v[i]:
        return u[:j] + v[j] + u[j + 1:]
    else:
        return v[:j] + u[j] + v[j + 1:]


left = distances(tout[0])
right = distances(tout[1])
# print(left, right)
if tout[1] in left:
    best = (left[tout[1]], "0")
else:
    best = (float('inf'), "0")   # par défault si pas de solution

for u in left:
    for remove in all_remove2(u):
        for v in all_replace2[remove]:
            if v in right:
                w = two_steps(u, v)
                if w is not None and w not in dico:
                    alternative = (left[u] + 2 + right[v], w)
                    if alternative < best:
                        best = alternative

if best[0] != float('inf'):
    print(best[1])
    print(best[0])
else:
    print(0)
    print(-1)

~~~