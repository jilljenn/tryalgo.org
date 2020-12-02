---
layout: fr
title: Compte rendu du workshop algo n° 1
excerpt_separator: <!--more-->
---

Présents :

- Guillaume Aubian
- Clément Beauseigneur
- Maxim Berman
- Thomas Espitau
- Thomas Domingues
- Jill-Jênn Vie
- X

<!--more-->

## Pour débuter en algo

- [Un TP sur les labyrinthes](http://tryalgo.org/tp4/)

## Optimisation

- [Sujets Google Hash Code des éditions précédentes](https://hashcode.withgoogle.com/past_editions.html)
- [Primers](http://primers.xyz), une initiative par des fans avec d'autres problèmes

### Le sujet de l'année dernière : Data Center

- [Code](https://bitbucket.org/serialk/hashcode2015/) et [pad](https://bimestriel.framapad.org/p/hashcode2015)

### Multiplicative Weights

- Cf. le cours de Christoph Dürr sur l'agrégation d'experts (heuristiques)
- [The Multiplicative Weights Update Method: a Meta Algorithm and Applications](https://www.cs.princeton.edu/~arora/pubs/MWsurvey.pdf)

### Upper-Confidence Bound Algorithm

- [Optimism in the Face of Uncertainty: the UCB1 Algorithm](http://jeremykun.com/2013/10/28/optimism-in-the-face-of-uncertainty-the-ucb1-algorithm/) par Jeremy Kun.
- [Implémentation en d3.js](http://jiji.cat/bandits/)

### Monte Carlo Tree Search

Un papier de journal super clair, [A Survey of Monte Carlo Tree Search Methods](http://repository.essex.ac.uk/4117/1/MCTS-Survey.pdf), IEEE 2012

- [Implémentation en Python](http://mcts.ai/code/python.html) sur [mcts.ai](http://mcts.ai) (beaucoup de ressources ici !)
- Slides de Michèle Sebag : [Monte-Carlo Tree Search](https://www.lri.fr/~sebag/Slides/InvitedTutorial_CP12.pdf)
- Slides de Rémi Munos : [From Bandits to Monte Carlo Tree Search: The optimistic principle applied to Optimization and Planning](http://chercheurs.lille.inria.fr/~munos/papers/files/AAAI2013_slides.pdf), AAAI 2013

Et si on utilisait MCTS pour résoudre des problèmes d'optimisation combinatoire ? IBM s'est posé la même question :

- [Guiding Combinatorial Optimization with UCT](http://www.cs.toronto.edu/~horst/cogrobo/papers/uctmip.pdf), 2012, Sabharwal & Samulowitz, IBM Watson Research Center, cited by 15
- [Bandit-based search for constraint programming](https://hal-polytechnique.archives-ouvertes.fr/file/index/docid/863451/filename/paper123.pdf), 2013, Sebag et al., cited by 11

C'est amusant, parce que ce papier vient de IBM Watson Research, et que ce jour-là (6/2) il y a justement [Watson for President](http://watson2016.com) qui a fait [la une de Hacker News](https://news.ycombinator.com/item?id=11047268). C'est celui qui avait explosé tout le monde à l'équivalent anglophone de *Questions pour un champion* :

<iframe width="100%" height="315" src="https://www.youtube.com/embed/WFR3lOm_xhE" frameborder="0" allowfullscreen></iframe>

## Ressources liées au code

### Comment faire pour éditer du code collectivement ?

Première réponse : vous n'avez pas envie de faire ça. Un projet git semble suffisant.  
Deuxième réponse : Lorsqu'on tape *collaborative code editor*, il y a plein de résultats. Mais la plupart sont payants.

### Python dans le navigateur

- Ça s'appelle [Runestone](http://interactivepython.org/runestone/default/user/login?_next=/runestone/default/index) et ça repose sur [Skulpt](http://www.skulpt.org).
- [Il y a même Turtle dans le navigateur o_O](http://jill-jenn.net/algo/stage-python/projets.html) (projet de terminale S)

J'aimerais m'en servir pour que des jeunes s'amusent à résoudre le jeu du [quart de singe](https://prologin.org/static/archives/2012/demi-finales/sujet/quart-de-singe-bordeaux.pdf), comme [Randall Munroe l'a fait avec Ghost](http://blog.xkcd.com/2007/12/31/ghost/). Pendant ce temps, d'autres gens résolvent le [MasterMind](http://projects.michael0x2a.com/mastermind_solver/) ou le [Go](https://deepmind.com/alpha-go.html).

### Bonus mars 2016 : Jupyter

Jupyter (ex IPython) permet d'avoir des notebooks. Très pratique pour des démos :

- [Recommending Movies](http://mldb.ai/ipy/notebooks/_demos/Recommending%20Movies.html) par Datacritic

Il y a Jupyter qui travaille sur une [intégration à Google Drive](https://github.com/jupyter/jupyter-drive).

- **Docker + Jupyter** = http://tmpnb.org, notebook jetable, supprimé après 10 minutes d'activité.
- **GitHub + Jupyter** = http://mybinder.org, ajoute un badge pour parcourir les notebooks d'un repo (durée : 2 heures).
- **GDrive + Jupyter** = [JupyterDrive](https://github.com/jupyter/jupyter-drive) (pas encore en temps réel)
- **coup de cœur** : [Livebook](http://livebook.inkandswitch.com), modifier un Notebook comme un post de blog, directement dans le navigateur. À base de React.js.

### Coder de la musique dans le navigateur

- [Trinket](https://trinket.io/music) utilise un langage que je ne connais pas, très pratique, pas open source.
- [VexTab](http://www.vexflow.com/vextab/) est open source et Trinket repose dessus en partie.
- On peut même [jouer en MIDI la musique dans le navigateur](http://my.vexflow.com/articles/40).

### Commentaires autres que Disqus

(Pour une raison random, on s'est posé cette question.)

- [Isso](https://posativ.org/isso/) : chiant à installer mais très pratique.
- [HashOver](http://tildehash.com/?page=hashover), bweeeh PHP.
- [commentserve](https://github.com/drewp/commentserve), wut RDF.
