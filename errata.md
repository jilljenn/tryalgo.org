---
layout: page
title: Errata
---

Voici une liste de coquilles dans le livre.

- page 14 : la définition d'$\Omega$ est erronée, il faut $f(n) \geq c \cdot g(n)$ (merci garkham).

- page 16 : (première phrase) Il se trouve que $\textsf{P} \subseteq \textsf{NP}$, l'intuition étant que si on peut construire une solution en temps polynomial, alors on peut *vérifier* une solution en temps polynomial.

- page 102 : la complexité de l'algorithme pour le voyageur de commerce est $O(&#124;V&#124;^2 2^{&#124;V&#124;})$

- page 112 : dans le code de dist_grid, le *break* devrait être *continue*.

- page 143 (légende 9.9): ... décomposition en chaînes *minimum* dans G ...

- page 146 (fonction tree_adj_to_prec): la ligne n = len(graph) peut être omise.

- page 153 : Donc on peut choisir un sommet arbitraire r, déterminer un sommet v1 de distance maximale de *r*, puis à nouveau déterminer un sommet v2 de distance maximale de v1.

- page 157 (rendu de monnaie): dans la récurrence pour A[i][m] il faut lire min au lieu de max

- page 191 (Tous les chemins pour un laser): peut en fait être réduit à un problème de couplage parfait.  Par contre le graphe n'est pas biparti, et l'algorithme de Edmond (Blossom algorithm) est long à implémenter.


## Clarifications

- page 35, 36 : la fonction présentée prend une liste de mots (*w*) en argument et retourne une liste de liste de mots (*reponse*).
