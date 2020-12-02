---
layout: fr
title: Google Codejam 2017 - 1B
author: Christoph Dürr et Lê Thanh Hương
---

Nous décrivons ici des solutions pour la ronde 1B du concours [Google Codejam 2017](https://code.google.com/codejam/contest/8294486/dashboard).

# Steed 2: Cruise Control

Une ligne de longueur D kilomètres. Il y a n chevaux. Le cheval i se trouve au temps 0 à la position Ki et il marche avec une vitesse Si vers la destination au kilomètre D. Il lui faut (D-Ki)/Si heures pour arriver à la destination s'il était tout seul.  Le temps d'arrivée le plus tard sur tous les chevaux est le maximum sur cette fraction, disons T, et comme les chevaux ne se dépassent pas, Annie peut arriver au plus tôt au temps T. Donc le cheval d'Annie doit se déplacer avec la vitesse D/T.
La complexité de l'algorithme est linéaire.

![](/fr/images/Steed-2-Cruise-Control.svg){:width="600"}


# Stable Neigh-bors

Considérons les instances courtes d'abord, qui ne contiennent que des couleurs élémentaires. Il faut placer r licornes rouges, b bleues et y jaunes dans une liste circulaire tel que deux licornes adjacentes soient de couleurs différentes. Supposons pour simplifier que les nombres soient ordonnés y ≤ b ≤ r.  Alors les positions des licornes rouges décomposent la liste en r intervalles qui doivent être remplis par les autres couleurs. Ceci n'est possible seulement si y + b ≥ r.
Une telle solution peut être construite comme suit. D'abord on place une licorne bleue dans chacune des b premiers intervalles.  Il n'y a pas de risque à avoir deux licornes bleues dans le même intervalle car b ≤ r. Puis on place les y licornes jaunes dans les intervalles suivants, en débordant de nouveau sur les premiers intervalles si nécessaire.  Il n'y a pas de risque à avoir deux licornes jaunes dans un même intervalle car y ≤ r.

![](/fr/images/Stable-Neigh-bors.svg){:width="600"}

Maintenant considérons les instances longues, qui comportent également o licornes oranges, g vertes et v violettes.  Chacune de ces licornes doit être entourée d'une licorne de la couleur complémentaire, par exemple vert doit être entre deux rouges.

L'idée est alors de construire d'abord une solution avec les couleurs élémentaires, comportant r-g licornes rouges, b-o bleues et y-v jaunes.  Puis pour chacune des couleurs mixtes, par exemple vert, on cherche une licorne rouge et on insère devant elle une séquence de licornes alternants rouge et vert et de longueur 2g.
Dans le cas limite où g est égal à r, il faut que ceux-ci soient les seules couleurs de l'instance pour qu'une solution soit possible.
Ainsi on respecte le nombre de couleurs imposés et la contrainte des couleurs adjacentes distinctes. La complexité de l'algorithme est linéaire en la taille de la sortie.

{% highlight python %}
def solve(n, R, O, Y, G, B, V):
    L = [(R - G, 'R'), (B - O, 'B'), (Y - V, 'Y')]
    # sort pure colors
    L.sort()
    (n0, c0), (n1, c1), (n2, c2) = L
    if n0 < 0 or n0 + n1 < n2:
        return "IMPOSSIBLE"
    s = (c0 + c1 + c2) * (n0 + n1 - n2)
    s += (c1 + c2) * (n2 - n0)
    s += (c0 + c2) * (n2 - n1)
    # add mixed colors
    if G > 0:
        i = s.find("R")
        if i == -1 and s != "":
            return "IMPOSSIBLE"
        else:
            s = s[:i] + ("RG" * G) + s[i:]
    if O > 0:
        i = s.find("B")
        if i == -1 and s != "":
            return "IMPOSSIBLE"
        else:
            s = s[:i] + ("BO" * O) + s[i:]
    if V > 0:
        i = s.find("Y")
        if i == -1 and s != "":
            return "IMPOSSIBLE"
        else:
            s = s[:i] + ("YV" * V) + s[i:]
    return s
{% endhighlight %}

# Pony Express

Ce problème peut être résolu par deux applications à [Floyd-Warshal](https://jilljenn.github.io/tryalgo/tryalgo/tryalgo.html?highlight=warshal#tryalgo.floyd_warshall.floyd_warshall).
D'abord on calcule avec cet algorithme les distances d entre toutes les villes. Dij est la longueur du plus court chemin de la ville i à la ville j.

Puis on peut calculer une matrice de temps de déplacement A, tel que Aij est le temps qu'il faut pour aller de la ville i à la ville j, en utilisant le cheval stationné en i et sans changer de cheval en cours de route.
On appliquant Floyd-Warshal à cette matrice, on trouve la matrice des temps de déplacement, autorisant les changements de cheval.

{% highlight python %}
from sys import stdin
from tryalgo.floyd_warshall import floyd_warshall


def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))


def solve(n, e, s, d):
    # first compute distances in graph
    for row in d:
        for i in range(n):
            if row[i] == -1:
                row[i] = float('inf')
    floyd_warshall(d)
    N = range(n)
    a = [[0 for j in N] for i in N]
    for i in range(n):
        for j in range(n):
            if d[i][j] <= e[i]:
                a[i][j] = d[i][j] / s[i]
            else:
                a[i][j] = float('inf')
    floyd_warshall(a)
    return a

for test in range(readint()):
    n, q = readints()
    e = [0] * n
    s = [0] * n
    for i in range(n):
        e[i], s[i] = readints()
    d = [readints() for _ in range(n)]
    a = solve(n, e, s, d)
    print("Case #%i:" % (test+1), end='')
    for _ in range(q):
        u, v = readints()
        time =  a[u-1][v-1]
        if time == float('inf'):  # peut-être pas nécessaire, s'il y a toujours un chemin possible
            time = -1
        print(" %f" % time, end='')
    print()
{% endhighlight %}
