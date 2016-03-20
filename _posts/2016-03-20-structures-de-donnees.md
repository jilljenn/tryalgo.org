---
layout: post
title: Structures de données
---

Voici une structure de données des structures de données.

Une relation A -> B signifie « *B est un cas particulier de A* ».  
Une relation en pointillés A -> B signifie « *A peut être implémenté par B* ».  
Les nœuds à double bordure sont les types abstraits.

<p><a href="/static/metadatastructure.png"><img src="/static/metadatastructure.png" alt="Une structure de données des structures de données."></a></p>

## Structures moins connues

- [Corde](https://en.wikipedia.org/wiki/Rope_(data_structure)), pour stocker de longues chaînes de caractères
- [Arbre cartésien](https://en.wikipedia.org/wiki/Cartesian_tree), un arbre tournoi qui maintient une séquence donnée par son ordre infixe, efficace pour des problèmes de [minimum d'une plage](https://en.wikipedia.org/wiki/Range_minimum_query).
- [Tableau de suffixes](https://en.wikipedia.org/wiki/Suffix_array), une manière efficace de stocker un [arbre de suffixes](https://en.wikipedia.org/wiki/Suffix_tree).

## Structures de données dynamiques

Une structure de données dynamique doit répondre efficacement à des *requêtes*, qui sont des opérations sur l'ensemble qu'elle contient.

- [Union-find](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) permet de maintenir une partition d'éléments avec des requêtes de recherche et d'union
- [Range minimum query](https://en.wikipedia.org/wiki/Range_minimum_query), permet de maintenir un tableau d'entiers avec des requêtes de minimum d'une plage
- [Arbre de Fenwick](/2016/03/09/arbre-de-fenwick/), permet de maintenir un tableau d'entiers avec des requêtes de somme d'une plage et de mise à jour d'un élément
- [Arbre d'intervalles](https://en.wikipedia.org/wiki/Interval_tree), permet de maintenir un ensemble d'intervalles avec des requêtes : « *Quels intervalles contiennent un certain entier ?* »
