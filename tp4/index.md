---
layout: page
title: Pathfinding
parent: Problems
---

[Slides](https://jjv.ie/slides/parcours.pdf) en français (Sorbonne Université Camp 2021)

## Débutants

Aujourd'hui, vous allez devoir apprendre à sortir de ce labyrinthe.

    9 17
    #################
    ..........#.....#
    #########.#.###.#
    #...........#...#
    ######.########.#
    #......#.....#..#
    #.######.#..#####
    #........#......#
    ###############.#

### Entrées-sorties

#### Jeux de tests

- [laby1.txt](laby1.txt) : accessible
- [laby2.txt](laby2.txt) : inaccessible
- [laby3.txt](laby3.txt) : plus court chemin non trivial

#### Sources à compléter

- [laby.ml](laby.ml)
- [laby.py](laby.py)

Vous pouvez les appeler comme suit :

    ocaml laby.ml < laby1.txt
    python3 laby.py < laby1.txt

### Exercices

Toutes les fonctions demandées prennent en argument les dimensions `m` × `n` du labyrinthe ainsi que le labyrinthe `laby`. On vous garantit que l'entrée est toujours en `(1, 0)` et la sortie en `(n - 1, m - 2)`.

#### Exercice 1

Écrire une fonction `sortie_accessible` qui renvoie `Vrai` s'il est possible d'accéder à la sortie, `Faux` sinon.

#### Exercice 2

Écrire une fonction `chemin` qui trace un chemin composé de `x` pour accéder à la sortie.

Par exemple, sur le fichier [laby1.txt](laby1.txt), votre code pourra renvoyer :

    #################
    xxxxxxxxxx#.....#
    #########x#.###.#
    #.....xxxx..#...#
    ######x########.#
    #xxxxxx#xxxx.#..#
    #x######x#xx#####
    #xxxxxxxx#xxxxxx#
    ###############x#

#### Exercice 3

Écrire une fonction `plus_court_chemin` qui trace un plus court chemin composé de `x` pour accéder à la sortie.

Par exemple, sur le fichier [laby3.txt](laby3.txt), votre code pourra renvoyer :

    #################
    xxxxxxxxxx......#
    #########x#####.#
    #.......xx......#
    #.######x########
    #.......xxxxxxxx#
    #.########.##.#x#
    #.............#x#
    ###############x#

#### Exercice bonus 4

Vous êtes maintenant muni d'un marteau qui démolit n'importe quel mur avec un coût de 5 (on suppose que se déplacer d'une case a un coût de 1). Écrire une fonction `plus_court_chemin_avec_marteau` qui trace un plus court chemin composé de `x` pour accéder à la sortie.
