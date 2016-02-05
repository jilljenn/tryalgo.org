---
layout: page
title: Conseils Google Hash Code
---

Cette page donne des conseils pour le Google Hash Code et le site d’entraînement [primers.xyz](http://primers.xyz).

Vous avez une seule instance à résoudre. Alors je vous conseille de la lire et peut-être découvrir des propriétés qui pourraient aider. Si c'est un graphe, est-ce que le degré maximal est petit par exemple ?

Il me semble que parfois des approches génériques pourraient donner de bons résultats, à savoir
- une recherche de *branch and bound*
- la recherche locale
- un algorithme glouton.

La dernière méthode pourrait être la plus rapide à mettre en oeuvre mais probablement sera aussi la moins efficace.  Peut-être qu'une première solution gloutonne pourrait être le point de départ pour une recherche locale.

## Set cover et set packing

Soit un univers composé des entiers de 0 à n-1, ainsi qu'une liste d'ensembles sur cet univers.  Dans le problème *set cover* il faut trouver une collection minimal d'ensembles qui couvrent tout l'univers. C'est-à-dire chaque entier de l'univers doit être contenu dans un ensemble de la solution.  Dans la variante pondérée chaque ensemble vient avec un prix, et il faut minimiser le prix total de la solution.

Dans le problème *set packing* il faut trouver une collection d'ensembles disjoints, qui maximisent la taille de leur union.  De manière équivalent on peut aussi chercher à minimiser le nombre d'éléments de l'univers pas couverts par la solution.

Une solution consiste en des décisions binaires sur les ensembles, les éléments de l'univers formant des contraintes.  Par exemple la contrainte *x1+x5 <= 1* demande qu'au plus un des ensembles numéro 1 et 5 soit dans la solution.  Avec des contraintes linéaires de cette forme on peut exprimer les contraintes du problème *set cover* ou *set packing*.

Ces problèmes sont NP-difficiles, mais si les contraintes sont assez indépendantes (ensembles de petite cardinalité, donc grande probabilité que deux ensembles soient disjoints), alors les instances pourraient être résolu en temps raisonnable.

Typiquement on résout une instance par *branch and bound*. C'est à dire pour *set cover* par exemple, on sélectionne un élément pas encore couvert et on essaye tous les ensembles le contenant. Chaque ensemble crée un nouvelle branche dans l'arbre de recherche. Les nœuds de l'arbre sont des sous-instances. Les feuilles sont soit des solutions soit des échecs.  L'arbre peut-être exploré en mode DFS, en maintenant le coût de la solution partielle obtenue et en coupant une branche de l'arbre (interrompre la recherche en un nœud) si le coût dépasse la meilleur solution découverte jusqu'alors.

Avec cette méthode on peut se fixer une limite en temps et juste retourner la meilleure solution trouvée, sans nécessairement prouver son optimalité, ce qui nécessite l'exploration complète de l'arbre.

Je conseille l'utilisation de solveur de programmes linéaires à variable entière (MIP - mixed integer linear program) car ils implémentent le *branch and bound* de manière efficace.  Les solveurs courants sont glpk (projet GNU, mais peu efficace), CPLEX, Gurobi par exemple.  Les licences académiques sont gratuits et il existe des API pour Python, C++, Java, etc.



## Exposition au musée

C'est un problème de *set cover*.  Les ensembles sont définis par des disques et les points qu'ils contiennent.  Pour limiter le nombre de disques potentiels, je propose :

* L = liste vide
* Poser sur le plan une grille avec des cases de dimension 8 fois 8.  Construire un tableau qui associe aux coordonnées d'une case la liste des points inclus.
* Boucler sur tous les points A
* Boucler sur tous les points B,C dans les 9 cases autour de A. La grille permet de ne pas faire trop de tests inutiles de points trop éloignés.
  * Calculer le disque D défini par A, B, C.
  * Si A,B,C sont co-linéaires ou si le rayon de D dépasse 8, ignorer ce triplet et continuer l'itération.
  * Si le rayon dépasse 4, l'agrandir à 8, sinon l'agrandir à 4.
  * Chercher dans les 9 cases l'ensemble S des points inclus dans le disque (avec le nouveau rayon)
  * Ajouter S dans L

Puis dans un post traitement trier L, et par un simple parcours enlever les ensembles identiques de L.

Dans l'instance il y a 5000 points, mais uniformément réparti, le nombre d'ensemble devrait être assez petit et les ensembles aussi.

## Art optimal

Deux idées.

1. **Quadtree** Augmenter artificiellement l'image de 800x600 à 1024x1024 pixels.  Poser sur l'image un quad-tree. Résoudre chaque carré de manière optimale par programmation dynamique.  Si tout blanc, ne rien faire. Sinon soit générer carré noir aux dimensions donnée par l'espace maximale des pixels noirs et ajouter le nombre de pixels blancs dans le carré.  Soit résoudre de manière récursive chaque sous-arbre.  Faire *branch and bound* sur cet arbre.

2. **Glouton.**  Une solution partielle consiste en l'image noir et blanc et des zones grises qui seront de toute façon peinte plus tard.  Le score d'un carré  C dans une telle image est calculé comme suit.  N est le nombre de pixels noirs dans C, B le nombre de pixels blancs.  Le score est N/(1+B). C'est le nombre de pixels noirs peints, divisé par le prix que ça a coûté.  L'idée est de sélectionner le carré au plus grand score.  De le mettre dans la liste SOL, et puis de colorier en gris le carré dans l'image et itérer. On termine quand il n'y a plus de pixel noir.  Alors on parcours la liste SOl et on produit les commandes FILL et ERASE correspondantes.

## Agar.IA

Ce type de problème pourrait être résolu par un algorithme génétique ou par recherche locale.

## Glaces à Gogo

C'est un peu cher à implémenter. Mais on pourrait maintenir un diagramme de Voronoi.  Faire de la recherche locale. Il y a 30.000 pixels et 30 vendeurs de glace.  Si vous trouvez le diagramme de Voronoi trop coûteux, vous pourriez réduire la résolution de la grille, et puis calculer le coût de chaque vendeur de manière naïve.  Plus tard vous pourriez retourner à la véritable résolution.

## Illumination

C'est un problème de maximisation de clauses XOR-SAT.  Je pense que le recuit simulé pourrait fonctionner ici.

## Pizza Google

C'est un problème de *set packing*.  Faire appel à un solveur MIP.
L'instance est grande, alors il peut être intéressant de découper la pizza en k rectangles et résoudre chacun de manière indépendant avec un solveur MIP.  Puis après avoir assemblé les solutions respectives, on peut refaire un tour de recherche locale.

C'est ce qui a été fait [ici](PizzaGoogle.py).


## Et c'est parti

Dans ce problème on vous donne deux graphes G et H au même nombre de sommets. Il faut trouver une bijection entre les sommets qui préserve le plus d'arêtes.  Donc si (u,v) est une arête dans G et (pi(u),pi(v)) une arête dans H, on a gagné un point sur cette arête.   Je ne crois pas que ça aide que H soit bi-parti (la grille amputée de certaines cases), mais peut-être que le degré maximal dans H est 4.

Je chercherait à déterminer dans H une solution partielle connexe.  Si S est l'ensemble des cellules qui ont déjà un sommet de G, alors pour toute case voisine de S je calculerait une liste de priorités en fonction des voisins dans H.  En j'augmenterais S en fonction de ces priorités.  Si le bord de S est vide (S = composante connexe dans H), recommencer avec une autre case arbitraire.

Puis pour terminer je ferais de la recherche locale.  Choisir 2,3 cases et voir si une permutation améliore le score.

