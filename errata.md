---
layout: page
title: Erratum from the book
parent: Algorithms
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

- page 98 : Meigu Guan était enseignant-chercheur (puis doyen) de la *Shandong Normal University*. Il a travaillé sur le problème de l'inspection des routes pendant le grand bond en avant de 1958-1960 (avant la révolution culturelle chinoise). Jack Edmonds s'est intéressé à son travail et a appelé le problème le "problème du postier chinois" en honneur de Guan. Merci à Wikipedia et à Ning Yan Zhu pour avoir remarqué notre erreur. Voir également [<span class="citation" data-cites="grotschel2012euler">(Grötschel and Yuan, 2012)</span>](#ref-grotschel2012euler)


- page 100 : la formule devrait se lire comme

$$    \frac{d'[n][v] - d'[k][v]}{n-k}  = \frac{d[n][v] - n\Delta - (d[k][v] - k\Delta)}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \frac{n\Delta - k\Delta}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \Delta$$

- page 102 : la complexité de l'algorithme pour le voyageur de commerce est $O(&#124;V&#124;^2 2^{&#124;V&#124;})$

- page 110 : la boucle extérieur doit se faire au plus n fois, pas n+2.

- page 112 : dans le code de dist_grid, le *break* devrait être *continue*.

- page 122 : au lieu de $\sum_{E_\ell}\ell$ il faut lire $\sum \ell$, qui représente $\sum_{u\in U} \ell(u) + \sum_{v\in V} \ell(v)$.

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

- page 154 : dans l'implémentation de Gale-Shapley, la ligne `celib.put(spouse[j])` devrait être `celib.append(spouse[j])`. La file `celib` pourrait être remplacée par une pile, pour simplification. 

- page 155 : dans la récurrence pour Opt il faut lire $c\geq p_i$ au lieu de $c\geq c_i$

- page 157 (rendu de monnaie): dans la récurrence pour A[i][m] il faut lire min au lieu de max

- page 170 (arbres de Huffman): le code était erroné dans le cas d'une liste de fréquences {'a':1, 'b':1, 'c':2}, car en cas d'égalité des fréquences le tas essayé de comparer les arbres, qui peuvent être une chaîne de caractère (pour arbres à un noeud), ou une liste (pour les arbres plus grands) et donc être incomparables. La solution est de travailler avec un tas de couples (fréquence, indice_d_arbre) et stocker les arbres à part. Voir le [code source](https://jilljenn.github.io/tryalgo/_modules/tryalgo/huffman.html#huffman).

- page 181 : dans le commentaire du code il faut comprendre que la décomposition binaire de b contient 2 puissance p et non pas (a puissance (2 puissance p)).

- page 188 : On a alors s(i,i)=0. Il faut lire opt(i,i)=0.

- page 191 (Tous les chemins pour un laser): peut en fait être réduit à un problème de couplage parfait.  Par contre le graphe n'est pas biparti, et l'algorithme de Edmond (Blossom algorithm) est long à implémenter.  Voir ce [billet]({% post_url en/2016-07-16-mirror-maze %}).

- page 204 (Algorithme en \\(O(n^3)\\)): il faut lire \\(S \subseteq\\{0,\ldots,n-1\\}\\) au lieu de \\( S \subseteq\\{1,\ldots,n-1\\} \\).  Aussi l'operation `expr[S][vL - vR] = ...` ne doit se faire que si la différence `vL - vR` est  positive.  Et pour finir la complexité est pire que $O(n^3)$ car il faut tenir compte des deux boucles internes sur les clés dans `expr[L]` et `expr[R]`.  Voir ce [billet]({% post_url en/2017-06-29-le-compte-est-bon %}).

- page 207: La boucle intérieure devrait débuter à i * i au lieu de 2 * i pour atteindre la complexité annoncée.

## Clarifications

- page 35, 36 : la fonction présentée prend une liste de mots (*w*) en argument et renvoie une liste de liste de mots (*réponse*).

## English translation

Some typos we spotted in the book.

- page 40 Figure 1.8: there should be two different gray shades among the rectangles. In the final print they might be too close to be distinguished.

- page 47, head of section 2.5: the second abra should be aligned with the suffix of the string abracadabra above.

- page 55: In the code of *powerstring_by_find*,  the variables *u* and *x* should be the same. Moreover in CPython and in Pypy the complexity of `haystack.find(needle)` with $m=\textrm{len(haystack)},\: n=\textrm{len(needle)}$ is $O((n-m) * n)$ instead of $O(n + m)$. Hence the function *powerstring_by_find* has quadratic time complexity, which makes it not very useful.

- page 115: the formula should be

$$    \frac{d'[n][v] - d'[k][v]}{n-k}  = \frac{d[n][v] - n\Delta - (d[k][v] - k\Delta)}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \frac{n\Delta - k\Delta}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \Delta$$

- page 116: Meigu Guan was a lecturer (then president) of Shandong Normal University. He worked on the route inspection problem during the Great Leap Forward of 1958-1960 (before the Chinese Cultural Revolution). Jack Edmonds got interested in his work and called the problem "Chinese postman problem" in honor of Guan. Thanks Wikipedia and Ning Yan Zhu for noticing our mistake. See also [<span class="citation" data-cites="grotschel2012euler">(Grötschel and Yuan, 2012)</span>](#ref-grotschel2012euler)

- page 143: the expression $\sum_{E_\ell}\ell$ should be instead $\sum \ell$, which stands for $\sum_{u\in U} \ell(u) + \sum_{v\in V} \ell(v)$.

- page 151: in the implementation of Gale-Shapley, the line `singles.put(spouse[j])` should be `singles.append(spouse[j])`. Equivalently the FIFO queue `singles` could be replaced by a stack, simplifying the code.

- page 170 (Huffman trees): the code would generate an error for example on given frequencies {'a':1, 'b':1, 'c':2}, because in case of identical frequencies, the heap would compare trees, which can be either strings (in case of a single node) or lists (in case of larger trees) and hence be incomparable. The solution is to work with a heap over (frequency, tree_index) pairs and store the trees separately. See the [source code](https://jilljenn.github.io/tryalgo/_modules/tryalgo/huffman.html#huffman).

- page 213: Indeed, an integer y can be written -> any composite integer y

- page 213: The inner loop should start at i * i instead of 2 * i for the announced complexity.

- page 240, last line: suffix of t begn inning -> beginning

## References

<div id="refs" class="references csl-bib-body hanging-indent"
role="doc-bibliography">
<div id="ref-grotschel2012euler" class="csl-entry"
role="doc-biblioentry">
Grötschel, Martin, and Ya-xiang Yuan. 2012. <span>“Euler, Mei-Ko Kwan,
K<span>ö</span>nigsberg, and a Chinese Postman.”</span> <em>Optimization
Stories</em> 43. <a
href="https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf">https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf</a>.
</div>
</div>

## References

<div id="refs" class="references csl-bib-body hanging-indent"
role="doc-bibliography">
<div id="ref-grotschel2012euler" class="csl-entry"
role="doc-biblioentry">
Grötschel, Martin, and Ya-xiang Yuan. 2012. <span>“Euler, Mei-Ko Kwan,
K<span>ö</span>nigsberg, and a Chinese Postman.”</span> <em>Optimization
Stories</em> 43. <a
href="https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf">https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf</a>.
</div>
</div>
