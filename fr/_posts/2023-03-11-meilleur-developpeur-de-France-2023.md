---
layout: fr
title: Meilleur developpeur de France 2023
author: Christoph Dürr
---

Le 9 mars 2023 avait lieu la compétition *Meilleur Développeur de France 2023*. Les algorithmes nécessaires sont résoudre les problèmes sont assez simples, mais il faut coder rapidement. Après coup, et à tête reposée, voici comment on aurait pu résoudre certains des problèmes.

Cette page évoluera au fur et à mesure que Isograd publie les problèmes.

- Retrouvez les problèmes [ici](https://www.isograd-testingservices.com//FR/solutions-challenges-de-code).

# MDF round 1 Pizza - Découpage des pizzas

Déterminer le nombre de composantes connexes. Pour chaque cellule $(i,j)$, si elle contient '#', alors augmenter un compteur et composantes et explorer la composante par un parcours BFS ou DFS, comme vous préférez. Utilisez la même matrice, pour marquer les cellules visitées, par exemple par la lettre `M`.

# MDF round 2 Jeux Olympiques - Ascenseurs

On vous donne $m$ intervalles de la forme $[\ell_i, r_i]$ et on veut savoir si leur union inclut un intervalle donnée $[e,n]$.

Fausse piste: Si vous construisez un graphe, où chaque intervalle $[\ell_i, r_i]$, génère une arête $(\ell_i,r_i)$, alors il vous manque des informations dans votre modélisation. L’ascenseur peut servir *toutes* les stations entre $\ell_i$ et $r_i$, pas seulement relier les extrémités.

Difficulté. Les extrémités des intervalles sont entiers. Et on doit distinguer une instance $[1,1],[2,2]$ de l'instance $[1,2]$, qui elle peut relier les étages 1 et 2.

Technique: on va balayer les intervalles de gauche à droite. Soit $T$ l'ensemble de toutes les extrémités d'intervalles plus les valeurs $e,n$. Pour chaque $\textrm{etage}\in T$ en ordre croissant, on maintient une valeur `couvert`, qui dit combien d’ascenseurs peuvent aller de cet étage à l'étage suivant. Un compteur `C[etage]` indique de combien cette valeur change, d'un étage au suivant dans $T$.

{% highlight python %}
import sys
from collections import Counter

def readints(): return list(map(int, readstr().split()))

n, m, e = readints()
A = [readints() for _ in range(m)]


def solve(A, low, high):
    C = Counter({low:0, high:0})
    for left, right in A:
        if left < right:
            C[left] += 1
            C[right] -= 1
    L = [(etage, C[etage]) for etage in C]
    # print(L)
    couvert = 0
    for etage, delta in sorted(L):
        couvert += delta
        if not couvert and low <= etage < high:
            return False
    return True 

if solve(A, e, n):
    print("YES")
else:
    print("NO")
{% endhighlight %}

# MDF round 3 Basket - Égalité au tableau d'affichage

D'abord on détermine *manuellement* les couples de chiffres qui s'obtiennent par exactement un changement sur l'affichage. Puis on essaye les trois possibilités de corriger le premier, deuxième ou troisième chiffre.

{% highlight python %}
import sys

def readints(): return list(map(int, readstr().split()))


couples = [ 
[0, 8],
[5, 6],
[6, 8],
[1, 7],
[3, 9],
[5, 9]]

possible = set()
for a, b in couples:
    possible.add((a, b))
    possible.add((b, a))

def solve(L):
    a, b, c = L 
    if (a, c - b) in possible:
        return (c - b, b, c) 
    if (b, c - a) in possible:
        return (a, c - a, c)
    if (a + b, c) in possible:
        return (a, b, a + b)
    return None 
    

abc = solve(readints())
if abc:
    print(*abc)
else:
    print("Impossible")
{% endhighlight %}

# MDF round 5 Poubelles - Le dédale du local

Étant donnée une fonction $f$ de $\{1,\ldots,n\}$ dans $\{1,\ldots,n\}$, et un entier $k$ calculez $f^k(1)$, où $f^k$ est la fonction $f$ itérée $k$ fois. Le problème est que $k$ est énorme, 10 puissance 12. Plusieurs solutions sont possibles.

## Solution en $O(n \log k)$ par exponentiation rapide

Étant donnée $f$ on peut calculer en temps $O(n)$, la fonction $f^2$. Puis avec la même méthode, étant donnée $f^2$ on peut calculer en temps $O(n)$, la fonction $f^4$, et ainsi de suite, jusqu'à $f^{2^{40}}$. Puis on peut décomposer $k$ en somme de puissances de 2, et appliquer les fonctions correspondantes. Par exemple, pour $k=13=8+4+1$, on aurait $f^k(1) = f^8(f^4(f^1(1)))$.

## Solution en $O(n)$ par détection de cycle

La fonction $f$ itéré sur la valeur initiale $1$, produit une séquence infinie $(a_i)_{i\geq 0}$ avec $a_0=1$, qui se répète au bout d'un moment. Il existe alors deux entiers $p,q$, tel que pour $k \geq p$, on ait $f^k(1) = f^{p + ((k-p) \bmod q)}(1)$. On peut trouver ces deux entiers en construisant la séquence $(a_i)_i$ et en associant dans un dictionnaire pour chaque $v$ de la séquence, le premier indice $i$ avec $a_i=v$. Une technique alternative est celle du lièvre et de la tortue, voir [ici](https://fr.wikipedia.org/wiki/Algorithme_du_li%C3%A8vre_et_de_la_tortue) et [ici](https://github.com/jilljenn/tryalgo/blob/master/tryalgo/tortoise_hare.py).

# MDF round 5 Chocolat - Vox populi

Notre solution a une complexité de $O((n + k )2^k)$, où $k=13$ est le nombre maximum d'ingrédients au total. L'idée est d'abord de remplacer les ingrédients par un numéro unique 0,1,..,12. Puis chaque client $i$ correspond à un ensemble $C_i$ de 3 entiers. Un ensemble $S$ est une solution si et seulement si il intersecte tous les  ensembles $C_i$.

Pour comprendre ce code, il faut connaître la technique de codage des ensembles dans les entiers. Le singleton {i} est représenté par 2 puissance i, qui s'écrit `1 << i`. L'intersection se calcule avec le ET binaire, qui s'écrit `&`. La différence symétrique, s'écrit `^`, l'union `|` et pour un ensemble non-vide $S$ dont le minimum est $i$, l'ensemble singleton {i} s'écrit `S & -S`.

{% highlight python %}
import sys

def readint(): return int(sys.stdin.readline())
def readstr(): return sys.stdin.readline().strip()
def readints(): return list(map(int, readstr().split()))

# lire l'entrée

n = readint()
client_str = [readstr().split() for i in range(n)]

# associer à chaque ingrédient un numéro unique 0, 1, 2, etc
# set permet d'enlever les doublons
# list permet de leur associer des indices

L = list(set(ingr for c in client_str for ingr in c))

# rank[s] est le numéro de l'ingrédient s (de type str) 

rank = {s:i for i, s in enumerate(L)}

# maintenant chaque client correspond à un ensemble de 3 ingrédients
# on code les ensembles dans un bitvector

client = [0] * n 
for i, ci in enumerate(client_str):
    for ingr in ci:
        client[i] |= 1 << rank[ingr]

# comme il n'y a que 2**13 candidats pour les solutions, on les essaye tous

def cardinality(S):
    retval = 0
    while S:
        retval += 1
        S ^= S & -S 
    return retval 

def is_solution(S):
    for required in client:
        if S & required == 0:
            return False 
    return True
    
best = 14 # = infini pour ce problème

m = len(rank)
# essayer toutes les solutions (sauf l'ensemble vide)
for S in range(1, 1 << m):
    if is_solution(S):
        c = cardinality(S)
        if c < best:
            best = c 
print(best) 
{% endhighlight %}
