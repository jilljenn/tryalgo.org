---
layout: fr
title: Nos conseils pour l'option ICN
author: Clément Beauseigneur, Garance Gourdel, Antoine Pietri et Jill-Jênn Vie
---

Voici des idées d'activités pour [l'option ICN](/programme-ta-culture/).

- [Éditer directement sur GitHub]()
- [Éditer dans Google Docs](https://docs.google.com/document/d/19-4QwakWPoZ5_X11sca8SswEzCFQ5pQllI2unUIeDqE/edit?usp=sharing)

## Exploration de grosses données

- Liste des mots du scrabble
    - Combien y a-t-il de mots de la langue française finissant par un K ?
    - Quels sont les mots qu'on peut former avec un jeu de lettres donné ?
- Pendu ?
    - Quelle est la liste des mots possibles à un moment donné de la partie ? (Mettre des jeunes en binôme où l'un des deux essaie de tricher.)
    - Calculer le meilleur coup possible ?
- [Top 250 d'IMDb](http://jill-jenn.net/algo/stage-python/dictionnaires.html)
    - Requêtes de base de données (qui a réalisé tel film, etc.)
- Données sous forme de graphe (visualisation Neo4j)
- Analyse de fichiers de sous-titres ? (lexique récurrent chez Tarantino vs. Woody Allen)


## Création artistique numérique

Composition assistée par ordinateur.

- Générer du texte avec des lettres de tailles différentes (HTML ou JavaScript)
    - Calcul du dégradé d'une couleur vers une autre (différentes fonctions d'interpolation)
- De texte, à partir de mots d'un corpus
    - Facile : concaténation de Sujet + Verbe + Complément à partir d'une base de données, cf. [Kamoulbox](http://kamoulbox.free.fr)
    - Que se passe-t-il si on compose des phrases à partir de deux romans différents ?
    - Génération de dissertation automatique à partir d'articles Wikipédia
    - Génération de HTML caractère par caractère correctement formaté (!) à partir de réseaux de neurones récurrents (LSTM, cf. [l'article d'Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/))
- Musicale à partir de notes (ou fréquences) : markov.py
    - [Trinket](https://trinket.io/music) : framework Python pour dessiner ou écrire de la musique
    - MML pour générer du midi
    - PMX pour générer des partitions et du midi
- Génération d'images
    - [Rosaces de code.org](https://code.org/frozen) à partir de blocs d'instructions (Blockly, loué pour son feedback immédiat)
    - Fractales : [courbe du dragon](http://jill-jenn.net/algo/stage-python/projets.html)
    - Réalisation de mosaïque à partir de photos existantes ?
    - Animées : déplacement d'une particule, voire [casse-briques](http://jill-jenn.net/conferences/cassebriques/)
- Génération de blocs dans Minecraft (API de SilexLabs)
    - Apprendre à utiliser des boucles pour automatiser et gagner du temps


## Réseaux et protocoles

- Parcours en largeur/profondeur de Wikipédia : quel est l'itinéraire si pour chaque article on clique sur le premier lien ? (Avec des bibliothèques comme BeautifulSoup en Python.)
- Récupérer la météo via une API (ou la position des arbres dans Paris)
- Création d'un bot qui répond, par exemple sur IRC.
- Utiliser une API de reconnaissance des images
- Faire des requêtes à une base de données (jeu RPG type Pokémon ou OGame avec MySQL)
- Interagir avec des machines à distance (contrôler un ordi à distance, ou sockets de chat, cf. TP de Marin à GCC 2016)


## Intelligence artificielle (au stade de concept)

- Comment automatiquement recommander des films à un utilisateur en fonction de ses goûts ? Cf. [slides de Girls Can Code! 2016](https://github.com/mangaki/movielens)
    - Comment sortir les gens de leur zone de confort pour leur faire découvrir des œuvres nouvelles ?
    - Qu'est-ce qui peut advenir de mes données ?
- Reconnaître la direction dans laquelle pointe un doigt dans une image ([pointerpointer.com](pointerpointer.com))
- Difficile : Reconnaissance de caractères (calcul de score, cf. TP d'Étienne à GCC 2016)
- Coder une IA qui joue à un jeu type Morpion ou jeu de Nim type allumettes
- Difficile : Pathfinding dans un labyrinthe (peut être possible si l'on dispose d'un debugger, ex. surbrillance des blocs dans [Blockly Maze](https://blockly-games.appspot.com/maze))
- Existe-t-il un équivalent du Core War pour les enfants ?
