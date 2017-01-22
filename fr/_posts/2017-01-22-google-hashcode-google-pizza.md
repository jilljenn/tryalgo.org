---
layout: fr
title: Google Hashcode - Pizza Régina
author: Christoph Dürr
---

Le concours annuel [Google Hashcode](https://hashcode.withgoogle.com/) consiste à résoudre en équipe une instance d'un problème NP-complet. *Résoudre* veut dire ici produire une solution faisable.  La valeur objectif atteinte est le score de la solution.  Les problèmes présentés sont assez purs, comparés à ceux du concours annuel [Roadef challenge](http://challenge.roadef.org), qui contiennent beaucoup plus de contraintes et sont plus proches d'un problème réel.

Dans ce billet nous décrivons nos expériences avec le problème *Pizza Régina*. La description officielle est [ici](https://sites.google.com/site/hashcode2015/tasks) et l'instance à résoudre se trouve [ici](http://primers.xyz/7).

# Le problème Pizza Régina

On vous donne une grille booléenne et il faut découper dans cette grille des rectangles en maximisant le nombre total de cellules découpés. Les contraintes sont que les rectangles sélectionnés doivent être disjoints, chaque rectangle doit contenir au moins *minsum* cellules à 1 de la grille et avoir une taille au plus *maxsize*.  Pour simplifier les notations nous appellerons tout simplement *rectangles* les rectangles satisfaisant ces contraintes.

Pour l'instance donnée, la grille contient 60*180 cellules, de l'ordre de \\(10^4\\), 10800 pour être précis.
Le nombre de rectangles qui valident les contraintes est de l'ordre de \\(10^5\\).  D'après nos observations les solutions intéressantes sont composées de l'ordre de \\(10^3\\) rectangles.

# Recherche locale

Nous avons expérimenté avec une solution par recherche locale.  Étant donnée une solution, cette recherche cherche à l'améliorer itérativement avec des opérations de la forme suivante, tant qu'une de ces opérations améliore la solution:

- ajouter un rectangle R à la solution (rouge dans la figure schématique)
- enlever les rectangles R' de la solution qui intersectent R (jaune)
- ajouter de manière gloutonne des rectangles R'' si R'' n'intersecte aucun autre rectangle de la solution courante. (bleu)

![](/fr/images/pizza-rech-locale.svg){:width="300"}

Le résultat de cette solution est sensible à l'ordre dans lequel les rectangles sont considérés à la fois pour l'opération d'amélioration locale et pour l'ajout glouton dans cette opération.  Nous avons tiré un ordre uniformément au hasard sur les rectangles pour notre amélioration.

Avec la recherche locale toute seule nous avons seulement obtenu un score de 9629, qui pourrait varier d'une exécution à l'autre en fonction du tirage aléatoire.  En vue de ces résultats, nous avons cherché d'autres approches et utilisé la recherche locale comme post traitement.

# Glouton

Une solution simple est de considérer tous les rectangles dans un certain ordre et de les ajouter dans la solution courante si possible, donc s'il n'y a pas d'intersection avec les rectangles déjà dans la solution.  Oui d'accord, mais quel ordre produira de bonnes solutions ?

Voici les résultats que nous avons obtenus avec différentes alternatives.  Ils sont très similaires.

- choisir un rectangle valide qui maximise le nombre de cellules dans le rectangle qui sont à 0 dans la grille. Ceci donne un score de 8994.
- choisir un rectangle valide qui maximise la proportion de cellules dans le rectangle qui sont à 0 dans la grille. Ceci donne un score de 8972.
- choisir un rectangle qui minimise le nombre de cellules dans le rectangle qui sont à 1 dans la grille. Ceci donne un score de 8953.

# Solution uniforme par bande

Considérons des solutions qui ont la forme suivante.  Les lignes sont partitionnées en bandes de différentes hauteurs.  Un groupe de k lignes consécutives dans cette partition contient seulement des rectangles de hauteur exactement k.

![](/fr/images/pizza-bandes.svg "Une solution construite par bandes de lignes."){:width="800"}

On peut calculer par programmation dynamique une solution optimale qui a cette forme. Il suffit de résoudre les sous problèmes suivants.

- B[i, h, j] = solution optimale pour l'intersection des lignes de i (inclus) à i+h (exclu) et des j premières colonnes.
- A[i] = solution optimale pour les i premières lignes (et toutes les colonnes).

Nous avons de l'ordre \\(\textrm{rows}\cdot\textrm{cols}\cdot\textrm{maxsize}\\) variables B et chacune est la maximisation sur au plus (maxsize+1) choix pour couvrir les cellules de la dernière colonne de la région considérée. Ceci donne de l'ordre de \\(10^6\\) évaluations, ce qui est faisable en moins de quelques secondes.  Le calcul de A est dominé par le calcul de B.

Avec cette approche nous obtenons un score de 8802.

# Solution par coupe de guillotine

Considérons les solution qui ont la forme récursive suivante.  La grille donnée est divisée en deux régions par une séparation verticale ou une séparation horizontale.  Puis chacune des régions est sous divisée de la même manière, jusqu'à obtenir

- soit une région qui contient moins de *minsum* 1's dans la grille.
- soit une région qui est un rectangle valide.

Des découpes de cette forme sont [considérées](https://en.wikipedia.org/wiki/Guillotine_problem) dans l'industrie du verre où d'une grande plaque de verre des rectangles plus petits doivent être découpés, les caractéristiques du verre forçant des solutions de cette forme.

![](/fr/images/pizza-guillotine.svg "En rouge la première découpe, en vert les découpes suivantes et en bleu les suivantes encore."){:width="800"}

Il est possible de calculer la découpe optimale d'une région en calculant les solutions optimales pour toutes les régions dans l'ordre de taille croissant.  Il y a de l'ordre de \\((\textrm{rows}\cdot\textrm{cols})^2\\) régions, donc autant de sous problèmes. La solution optimale de chaque sous problème est la maximisation sur au plus rows+cols différentes options. Ceci donne lieu à de l'ordre de \\(10^{10}\\) itérations, ce qui représente un temps de calcul de l'ordre de l'heure, ce qui est acceptable.

Avec cette approche (suivi de la recherche locale) nous obtenons un score de 10 129. Elle est très facile à implémenter par rapport aux autres approches présentées ici.

{% highlight python %}
Cval = {}
Carg = {}

order = [(w*h, i,j,w,h)  for i in range(rows)
                    for j in range(cols)
                    for h in range(1, rows -i + 1)
                    for w in range(1, cols - j +1)]
order.sort()
for _,i,j,w,h in order:      # traiter les rectangles en ordre croissante de taille
    Cval[i,j,w,h] = 0
    Carg[i,j,w,h] = 0             # zéro = pas de coupe
    tot = ham(i,j,w,h)       # compter les 1's dans le rectangle
    if tot < minsum:         # basis case: rectangle cannot be covered
        continue
    if w * h <= maxsize:     # basis case: rectangle can be fully covered with a single shape
        Cval[i,j,w,h] = w * h
        continue
    for cut in range(1, w):  # coupe verticale
        alt = Cval[i,j,cut,h] + Cval[i,j+cut,w-cut,h]
        if alt > Cval[i,j,w,h]:
            Cval[i,j,w,h] = alt
            Carg[i,j,w,h] = cut   # positif = coupe horizontale
    for cut in range(1, h):  # coupe horizontale
        alt = Cval[i,j,w,cut] + Cval[i+cut,j,w,h-cut]
        if alt > Cval[i,j,w,h]:
            Cval[i,j,w,h] = alt
            Carg[i,j,w,h] = -cut  # négatif = coupe horizontale

sol = []                     # extraire la solution

stack = [(0,0,cols,rows)]    # pile des rectangles à traiter
while stack:
    i,j,w,h = stack.pop()
    cut = Carg[i,j,w,h]
    if cut == 0:
        if Cval[i,j,w,h]:
            sol.append((j,i,w,h))
    elif cut > 0:
        stack.append((i,j,cut,h))
        stack.append((i,j+cut,w-cut,h))
    else:
        stack.append((i,j,w,-cut))
        stack.append((i-cut,j,w,h+cut))
{% endhighlight %}

# Solution par un solveur de programme linéaire à variables entières

Il existe un modèle naturel par programmation linéaire à variables entières (MIP) pour ce problème. Les variables de décision sont associées aux rectangles, et pour chaque cellule de la grille il a une contrainte qui assure qu'au plus un rectangle de la solution couvre la cellule.  Les solveurs de MIP n'arrivent pas à traiter convenablement l'instance qui décrit le problème pour la grille entière.

Alors nous avons entrepris de couvrir la grille par des régions de dimension carré et de résoudre le MIP restreint à chacune des régions.  Concrètement nous avons choisit des régions qui se chevauchement légèrement, pour ne pas interdire de notre solution des rectangles qui seraient à cheval entre les région.

Concrètement pour une région R, nous enlevons d'abord les rectangles de la solution courante qui sont inclus dans R.  Puis nous construisons le modèle MIP restreint au sous problème induit par la région R, en évitant des cellules de R déjà couverts par des rectangles de la solution courante intersectant R sans être inclus.

Voici les résultats obtenus avec cette approche. Si vous voulez vraiment savoir, l'implémentation a utilisée le solveur SCIP 3.2 sur un processeur 1,6 GHz Intel Core i5.

| taille région | taille chevauchement |    score |     temps |
| ------------: | -------------------: | -------: | --------: |
|            30 |                    2 | 10 154   | qq heures |
|            20 |                    6 | 10 045   |    10 min |
|            20 |                    8 | 10 082   |    10 min |
|            20 |                   10 | 10 036   |    10 min |
{:.mbtablestyle}

# Conclusion

Il manque encore plusieurs expériences, pour pouvoir faire une conclusion définitive. Par exemple une recherche par branchement et élagage ou alors une combinaison de la méthode de coupe par guillotine et d'un solveur MIP pour tous les régions suffisamment petites.  Mais au vu des résultats il semble que la méthode de coupe par guillotine donne de très bons résultats pour un code assez facile à mettre en œuvre.

Je remercie Pascale Bendotti et Pierre Fouilhoux pour des discussions qui ont aidé à l'élaboration de ces expériences.

