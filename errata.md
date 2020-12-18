---
layout: page
title: Errata
---

Voici une liste de coquilles dans le livre.

- page 15 : Dans la definition de $f\in\Omega(g)$, il faut $f(n) \geq c \cdot g(n)$ au lieu de $f(n)\leq c \cdot g(n)$ (merci [@_garkham](https://twitter.com/_garkham)).

- page 15 : La chaîne de formatage doit contenir %.02f%% à la place de %.02f pour qu'un pourcentage s'affiche en sortie.

- page 16 : (première phrase) Il se trouve que $\textsf{P} \subseteq \textsf{NP}$, l'intuition étant que si on peut construire une solution en temps polynomial, alors on peut *vérifier* une solution en temps polynomial.

- page 21: la ligne self.n=0 est inutile. Tout le code utilise len.

- page 37: The string "None" should be the keyword None.

- page 44: dans la définition de chaîne en puissance, $y^k$ est bien sûr $y$ concaténé $k$ fois, pas $n$.

- page 49 : dans cette implémentation *mirror* vaut -1 lors de la première itération. Ceci n'est pas un problème dans Python, car le dernier élément de *p* vaut 0.  Mais une meilleure implémentation qui fonctionnerait également pour d'autres langages de programmation, initialiserait *c* et *d* à 1 et on débuterait la boucle avec *i=2*.

- page 54 : Observation clé ... alors forcément une des lettres $x_i,x_j$ n'est pas couplée. Il faudrait lire $x_i, y_j$.  Aussi ici A[i,j] est une plus longue sous-séquence maximale, alors que dans l'implémentation A[i][j] en est la longueur.

- page 58 : Dans la récursion pour $G[i]$ il faut lire la condition $P[i] \leq i$.

- page 70: À tout moment donnée on maintient dans *open* le nombre d'intervalles ouverts. - Il fallait lire *nb_open*.  La phrase suivante doit être : .. un nouvel intervalle $[last,x)$ ... et *last* la dernière position à laquelle *nb_open* est devenue positif.

- page 83 Figure 6.7 : L'exemple n'est pas correct. Considérez plutôt le graphe suivant :

![]({{site.images}}bi-connexes-relation.png "Les sommets et les arêtes de déconnexion sont montrés en gras." ){:width="250"}

- page 100 : la formule devrait se lire comme

$$    \frac{d'[n][v] - d'[k][v]}{n-k}  = \frac{d[n][v] - n\Delta - (d[k][v] - k\Delta)}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \frac{n\Delta - k\Delta}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \Delta$$

- page 102 : la complexité de l'algorithme pour le voyageur de commerce est $O(&#124;V&#124;^2 2^{&#124;V&#124;})$

- page 110 : la boucle extérieur doit se faire au plus n fois, pas n+2.

- page 112 : dans le code de dist_grid, le *break* devrait être *continue*.

- page 126 : la ligne 9 *n=len(G)* du code est inutile par la présence de la même instruction en ligne 3.

- page 129 : Il faut lire: Donc pour une preuve par contradiction de la validité de l'algorithme, supposons qu'à la fin, il existe un homme i marié à une femme j' et une femme **j** mariée à un homme i'...

- page 138 point 3. La preuve n'est pas correcte telle quelle. Il faudrait plutôt lire :  Maintenant si pour un flot $f$ donné, on a $f (S) < c (S)$ pour
    toute coupe $S$, alors il existe un chemin augmentant. Pour cela tout
    simplement posons $S =\{s\}$ et $A = \emptyset$. Puisque $f (S) < c (S)$
    il existe une arête $(u, v)$ avec $u \in S, v \not\in S, f (u, v) < c (u,
    v)$. Ajoutons $(u, v)$ à $A$ et $v$ à $S$, et recommençons tant que $t\not\in S$. L'invariant est que $A$ est un arbre couvrant $S$ composé seulement d'arcs non saturés, et donc si $t\in S$ alors $A$ contient chemin
    augmentant.

- page 143 (légende 9.9): ... décomposition en chaînes *minimum* dans G ...

- page 146 (fonction tree_adj_to_prec): la ligne n = len(graph) peut être omise.

- page 147 (fonction extract): la concaténation à une chaîne ayant une complexité linéaire, la complexité de la fonction `extract` est en O(n^2). Pour arriver à une complexité linéaire il faudrait coder le préfixe par une liste chaînée. Cette liste est ensuite transformée en temps linéaire en un mot de code lors du traitement d'une feuille. Voir ce [code](https://jilljenn.github.io/tryalgo/tryalgo/tryalgo.html?highlight=huffman#tryalgo.huffman.extract).

- page 153 : Donc on peut choisir un sommet arbitraire r, déterminer un sommet v1 de distance maximale de *r*, puis à nouveau déterminer un sommet v2 de distance maximale de v1.

- page 155 : dans la récurrence pour Opt il faut lire $c\geq p_i$ au lieu de $c\geq c_i$

- page 157 (rendu de monnaie): dans la récurrence pour A[i][m] il faut lire min au lieu de max

- page 181 : dans le commentaire du code il faut comprendre que la décomposition binaire de b contient 2 puissance p et non pas (a puissance (2 puissance p)).

- page 188 : On a alors s(i,i)=0. Il faut lire opt(i,i)=0.

- page 191 (Tous les chemins pour un laser): peut en fait être réduit à un problème de couplage parfait.  Par contre le graphe n'est pas biparti, et l'algorithme de Edmond (Blossom algorithm) est long à implémenter.  Voir ce [billet]({% post_url en/2016-07-16-mirror-maze %}).

- page 204 (Algorithme en \\(O(n^3)\\)): il faut lire \\(S \subseteq\\{0,\ldots,n-1\\}\\) au lieu de \\( S \subseteq\\{1,\ldots,n-1\\} \\).  Aussi l'operation `expr[S][vL - vR] = ...` ne doit se faire que si la différence `vL - vR` est  positive.  Et pour finir la complexité est pire que $O(n^3)$ car il faut tenir compte des deux boucles internes sur les clés dans `expr[L]` et `expr[R]`.  Voir ce [billet]({% post_url en/2017-06-29-le-compte-est-bon %}).

## Clarifications

- page 35, 36 : la fonction présentée prend une liste de mots (*w*) en argument et renvoie une liste de liste de mots (*réponse*).
