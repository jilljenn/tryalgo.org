---
layout: fr
title: Arbre de Fenwick
excerpt_separator: <!--more-->
---

C'est une structure de données dynamique : elle permet de stocker un tableau de $n$ valeurs et de réaliser efficacement les opérations suivantes :

- mettre à jour une valeur du tableau ;
- calculer la somme d'une plage du tableau.

<!--more-->

**Update 28 septembre 2024.** On peut aussi faire des range add et point query avec peu de modifications. Et on peut faire range add et query sum en ayant deux tels tableaux. Voici plusieurs posts sur le sujet :

- [CP Algorithms](https://cp-algorithms.com/data_structures/fenwick.html#3-range-update-and-range-query)
- [CF: Range sum query without segment tree](https://codeforces.com/blog/entry/94227)
- [CF: Historic sums](https://codeforces.com/blog/entry/99895)
- Un [blog post de Petr](https://blog.mitrichev.ch/2013/05/fenwick-tree-range-updates.html) à ce sujet.

Notez qu'on peut l'adapter pour répondre à des requêtes de minimum d'une plage (cf. [range min query](https://en.wikipedia.org/wiki/Range_minimum_query) sur Wikipédia) mais on préférera peut-être utiliser un segment tree.

- Voir l'article Wikipédia sur les [arbres de Fenwick](https://en.wikipedia.org/wiki/Fenwick_tree)  
(on les appelle aussi *binary indexed trees*)
- [Voir le code](https://jilljenn.github.io/tryalgo/_modules/tryalgo/fenwick.html) sur TryAlgo Docs
- [Voir le code](https://github.com/jilljenn/tryalgo/blob/master/tryalgo/fenwick.py) sur GitHub
