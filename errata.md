---
layout: page
title: Errata
---

Voici une liste de coquilles dans le livre.

- page 14 : la définition d'$\Omega$ est erronée, il faut $f(n) \geq c \cdot g(n)$ (merci garkham).

- page 15 : La chaîne de formatage doit contenir %.02f%% à la place de %.02f pour qu'un pourcentage s'affiche en sortie.

- page 16 : (première phrase) Il se trouve que $\textsf{P} \subseteq \textsf{NP}$, l'intuition étant que si on peut construire une solution en temps polynomial, alors on peut *vérifier* une solution en temps polynomial.

- page 70: À tout moment donnée on maintient dans *open* le nombre d'intervalles ouverts. - Il fallait lire *nb_open*.

- page 102 : la complexité de l'algorithme pour le voyageur de commerce est $O(&#124;V&#124;^2 2^{&#124;V&#124;})$

- page 112 : dans le code de dist_grid, le *break* devrait être *continue*.

- page 143 (légende 9.9): ... décomposition en chaînes *minimum* dans G ...

- page 146 (fonction tree_adj_to_prec): la ligne n = len(graph) peut être omise.

- page 147 (fonction extract): la concaténation à une chaîne ayant une complexité linéaire, la complexité de la fonction `extract` est en O(n^2). Pour arriver à une complexité linéaire il faudrait coder le préfixe par une liste chaînée. Cette liste est ensuite transformée en temps linéaire en un mot de code lors du traitement d'une feuille. Voir ce [code](http://pythonhosted.org/tryalgo/_modules/tryalgo/huffman.html#extract).

- page 153 : Donc on peut choisir un sommet arbitraire r, déterminer un sommet v1 de distance maximale de *r*, puis à nouveau déterminer un sommet v2 de distance maximale de v1.

- page 155 : dans la récurrence pour Opt il faut lire $c\geq p_i$ au lieu de $c\geq c_i$

- page 157 (rendu de monnaie): dans la récurrence pour A[i][m] il faut lire min au lieu de max

- page 191 (Tous les chemins pour un laser): peut en fait être réduit à un problème de couplage parfait.  Par contre le graphe n'est pas biparti, et l'algorithme de Edmond (Blossom algorithm) est long à implémenter.

- page 204 (Algorithme en \\(O(n^3)\\)): il faut lire \\(S \subseteq\\{0,\ldots,n-1\\}\\) au lieu de \\( S \subseteq\\{1,\ldots,n-1\\} \\)

## Clarifications

- page 35, 36 : la fonction présentée prend une liste de mots (*w*) en argument et renvoie une liste de liste de mots (*reponse*).
