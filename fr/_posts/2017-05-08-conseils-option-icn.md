---
layout: fr
title: "Nos conseils pour l'option ICN : idées à coder"
author: Clément Beauseigneur, Garance Gourdel, Antoine Pietri et Jill-Jênn Vie
---

Voici des idées d'activités pour [l'option ICN](/programme-ta-culture/) au lycée, ou plus généralement toute activité de programmation pour lycéens.

Cette liste se veut **pluridisciplinaire**, afin de ne pas se limiter aux applications en sciences dures.

Nous avons décidé de les regrouper dans 4 catégories :

- Exploration de grosses données
- Création artistique numérique
- Réseaux et protocoles
- Intelligence artificielle

Pour ajouter des idées à cette liste :

- [Éditer directement sur GitHub](https://github.com/jilljenn/tryalgo.org/edit/master/fr/_posts/2017-05-08-conseils-option-icn.md)
- [Éditer dans Google Docs](https://docs.google.com/document/d/19-4QwakWPoZ5_X11sca8SswEzCFQ5pQllI2unUIeDqE/edit?usp=sharing)

## Exploration de grosses données

OK, on peut écrire des scripts. Mais tant qu'à faire autant les faire tourner sur des vraies données massives !

- Liste des mots du [Scrabble](http://jill-jenn.net/algo/stage-python/dictionnaires.html) (336531 mots)
    - Combien y a-t-il de mots de la langue française finissant par un K ?  
    (simple boucle for puis if)
    - Quels sont les mots qu'on peut former avec un jeu de lettres donné ?  
    (avec `Counter` par exemple)
    - Pendu ?
        - Quelle est la liste des mots possibles à un moment donné de la partie (expression régulière basique, test de conditions) ? (Mettre des jeunes en binôme où l'un des deux essaie de tricher avec la liste du Scrabble.)
        - Calculer le meilleur coup possible ?
- [Top 250 d'IMDb](http://jill-jenn.net/algo/stage-python/dictionnaires.html) au format JSON avec réalisateurs et acteurs
    - Requêtes de base de données SQLite (qui a réalisé tel film, etc.)
- Analyse de fichiers de sous-titres via l'[API](http://trac.opensubtitles.org/projects/opensubtitles) de [opensubtitles.org](https://www.opensubtitles.org/fr) ?
    - Lexique récurrent chez Tarantino vs. Woody Allen
- Plus difficile : Données sous forme de graphe
    - Données de cinéma avec visualisation Neo4j
![Neo4j](https://raw.githubusercontent.com/neo4j-examples/neo4j-movies-template/master/img/verifyCloudAtlasMovie.png)

## Création artistique numérique

Composition assistée par ordinateur, sous différentes formes :

- Générer de la mise en forme
    - Du texte avec des lettres de tailles différentes (HTML ou JavaScript)
    - Calcul du dégradé d'une couleur vers une autre (différentes fonctions d'interpolation, [rouge-vert-bleu](https://fr.wikipedia.org/wiki/Codage_informatique_des_couleurs) ou [teinte-saturation-lumière](https://fr.wikipedia.org/wiki/Teinte_saturation_lumière))
- Du texte, à partir de mots d'un corpus
    - Facile : concaténation de Sujet + Verbe + Complément à partir d'une base de données, cf. [Kamoulbox](http://kamoulbox.free.fr)
    - Si on se sert d'une chaîne de Markov avec un outil tout fait comme [markov.py](https://github.com/jilljenn/markov.py)
        - Que se passe-t-il si on compose des phrases à partir de deux romans différents ? (Ex. [*Alice au pays des merveilles* & *Hamlet*](http://www.eblong.com/zarf/markov/))
        - Génération de dissertation automatique à partir d'articles Wikipédia
        - Plus difficile : comprendre la chaîne de Markov
    - Plus impressionnant : génération de HTML caractère par caractère correctement formaté (!) à partir de réseaux de neurones récurrents (LSTM, cf. [l'article d'Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/))
- Musicale à partir de notes (ou fréquences)
    - [Trinket](https://trinket.io/music) : framework Python pour dessiner ou écrire de la musique dans une syntaxe simple
    - [MML](https://en.wikipedia.org/wiki/Music_Macro_Language) : pour générer du midi en [Ruby](https://gist.github.com/jangler/5892763) ou [Node.js](https://github.com/KatsuomiK/mml2smf)
    - [PMX](http://vie.jill-jenn.net/2017/03/29/transcription-de-partitions-musique-anime/) : pour générer des partitions et du midi
    - On peut donc écrire des boucles qui génèrent du code qu'on peut faire jouer à Trinket, ou mieux : une chaîne de Markov ([markov.py](https://github.com/jilljenn/markov.py)) pour écrire une partition dans l'un des langages ci-dessus.
- Génération d'images
    - [Rosaces de code.org](https://code.org/frozen) à partir de blocs d'instructions ([Blockly](https://blockly-games.appspot.com), loué pour son feedback immédiat)
    - Fractales : [courbe du dragon](http://jill-jenn.net/algo/stage-python/projets.html), etc.
    - Réalisation de mosaïque à partir de photos existantes ?
    - Animées : déplacement d'une particule, ex. [faire rebondir la balle du casse-briques](http://jill-jenn.net/conferences/cassebriques/)
- Génération de blocs dans Minecraft
    - ([Silex Labs](https://www.silexlabs.org) avait fait une API, on peut peut-être leur demander)
    - Apprendre à utiliser des boucles pour automatiser et gagner du temps

## Réseaux et protocoles

- Récupérer via une API
    - [les films](http://www.omdbapi.com) (ex. [Scott Pilgrim](http://www.omdbapi.com/?t=scott+pilgrim))
    - [la position des arbres dans Paris](https://opendata.paris.fr/explore/dataset/les-arbres/)
    - [la météo](http://openweathermap.org/api)
- Création d'un bot qui répond à l'utilisateur, par exemple sur IRC.
- Utiliser une API de reconnaissance des images (couleur, ou tags type [illustration2vec](http://illustration2vec.net))
- Faire des requêtes à une base de données
    - Ex. Jeu RPG type Pokémon ou OGame avec MySQL
- Interagir avec des machines à distance
    - Contrôler un ordi à distance (ex. SSH depuis le smartphone)
    - Créer un chat avec des sockets, cf. TP de Marin à [GCC](http://gcc.prologin.org) 2016, n'hésitez pas à leur écrire à `gcc` à `prologin.org` pour l'obtenir
- Plus difficile : Parcours en largeur/profondeur de Wikipédia : quel est l'itinéraire obtenu si pour chaque article on clique sur le premier lien ? (Avec des bibliothèques comme [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) en Python.)

## Intelligence artificielle (au stade de concept)

- Coder une IA qui joue à un jeu
    - Morpion
    - Jeu de Nim ex. allumettes
    - Petite IA type Zelda : [Vindinium.org](http://vindinium.org) ou les finales de [Prologin](https://prologin.org)
    - Existe-t-il un équivalent de [Core War](https://en.wikipedia.org/wiki/Core_War) pour les enfants ? Si non, il faut le créer !
    - Difficile : Pathfinding dans un labyrinthe (peut être possible si l'on dispose d'un debugger, ex. surbrillance des blocs dans [Blockly Maze](https://blockly-games.appspot.com/maze))
- Recommandation de films
    - Cf. [cette présentation à GCC 2016](https://github.com/mangaki/movielens) sur les plus proches voisins (niveau lycée)
    - « Qu'est-ce qui peut advenir de mes données ? »
    - « Comment sortir les gens de leur zone de confort pour leur faire découvrir des œuvres nouvelles ? »
- Reconnaissance d'images
    - La direction dans laquelle pointe un doigt dans une image ([pointerpointer.com](pointerpointer.com))
    - Difficile : Reconnaissance des chiffres
        - via calcul de score de perceptron, cf. TP d'Étienne à GCC 2016, n'hésitez pas à leur écrire à `gcc` à `prologin.org` pour l'obtenir

<p style="font-style: italic; background: #eee; padding: 1em">
Ce post a été rédigé par des étudiants de l'ENS Paris-Saclay et EPITA.<br />
Clément Beauseigneur est vice-président de <a href="https://prologin.org">Prologin</a> et développeur à Google, Garance Gourdel est en licence d'informatique, Antoine Pietri est ingénieur Inria et Jill-Jênn Vie en postdoc à RIKEN, Tokyo.</p>
