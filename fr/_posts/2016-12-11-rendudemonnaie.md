---
layout: fr
title: Rendu de monnaie, bases de programmation dynamique
author: Jill-Jênn Vie & Clémence Réda
---

## Introduction

Le problème du rendu de monnaie s'énonce de façon simple : étant donné un système de pièces à disposition (1 euro, 2 euros...) et un montant à rendre, rendre ce montant avec un nombre minimal de pièces. Les applications d'une solution à ce problème sont faciles à concevoir : nul n'a envie de récupérer 1 euro en pièces de 1 centime s'il s'est aventuré à payer 2 euros pour une bouteille de soda à un distributeur. Non, vraiment personne.

## Une première méthode

Imaginons un distributeur de boissons un peu particulier, quelque part dans l'Union européenne, qui rend la monnaie, en pièces de 2 centimes, 5 centimes, 10 centimes, 50 centimes et 1 euro.

Une première méthode, que l'on appelle un raisonnement glouton, serait de commencer par les pièces de plus grande valeur, et décroître le montant à rendre jusqu'à ce que ce dernier soit inférieur à la valeur de la pièce. On considère alors la plus grande valeur de pièce inférieure au montant, et on itère le raisonnement jusqu'à ce que le montant atteigne zéro.

L'algorithme ci-dessus  prend en argument le montant (amount, histoire de ne pas faire tache avec le reste du code), et coins, qui est notre système de pièces (ici, un tableau comportant dans la case numéro i la valeur de la ième plus petite valeur de pièce). On renvoie un tableau chosen qui comporte dans la case numéro i le nombre de pièces numéro i, dans l'ordre croissant de valeur, utilisées pour rendre la monnaie sur amount.

Le reste de l'algorithme suit la démarche que l'on a décrite ci-dessus. Pour l'implémentation, voir [ici](http://livebook.inkandswitch.com/d/htXLJpCecn1h) (cela aussi vaut pour la suite de l'article).

Par exemple, pour 177 centimes, sur notre système de pièces de 2 cts, 5 cts, 10 cts, 50 cts et 1 €, on a décomposé nos 177 centimes en 1 pièce de 2 cts, 1 pièce de 5 cts, 2 pièces de 10 cts, 1 pièce de 50 cts et 1 pièce de 1 €. Donc 100 + 50 + 10x2 + 5 + 2 = 177 ! Ouf, ça marche !

Hum, vraiment ?

Supposons à présent que Bob souhaite acheter un jus de tomate à 1,59 €, et qu'il ait entré 2 euros dans la machine. Le montant à rendre est donc 41 centimes. Vous voyez que l'algorithme (dans le lien ci-dessus) retourne une erreur.

Que s'est-il donc passé ? Reprenons l'algorithme calmement, nonobstant le fait qu'il vient de nous crasher/cracher à la figure (pas très sympa). L'exception relevée souligne que l'on n'a pas rendu (apparemment) le bon montant. Prenons notre bon (?) vieux système 2-5-10-50-100. On doit rendre 41 centimes. Cela élimine déjà la possibilité de rendre avec une pièce de 1€ ou de 50 cts. On peut prendre des pièces de 10 cts, puisque 10 cts < 41 cts.

On prend alors 4 pièces de 10 centimes et... on reste bloqué. Car il faut rendre encore 1 centime ! Si la machine était douée de parole, elle pourrait éventuellement convaincre le client que la perte d'un ridicule centime est bien futile. Si le client avait tout son temps, la machine pourrait reprendre ses calculs, et s'arrêter à 3 pièces de 10 centimes, puis regarder les autres pièces. On appelle cela faire du backtracking : autrement dit, si un calcul plante, on revient sur nos pas, et on reprend nos calculs depuis une position qui nous permet de choisir une autre façon de calculer, par exemple ici, choisir seulement 3 pièces de 10 centimes et chercher à décomposer le montant restant avec des pièces de 5 et 2 centimes. Il est clair que non seulement cette stratégie ne garantit pas la minimalité du nombre de pièces, car la machine va crier victoire dès qu'elle aura trouvé une solution, même non optimale, mais qu'en plus, cela risque de prendre un certain temps, puisqu'on peut faire les calculs, dans le pire cas, pour toute combinaison de pièces. Ouf, c'était la parenthèse backtracking.

Donc, nous sommes bien dans la vie, la vraie, et la seule issue, qui semble inéluctable, est la destruction de la machine par un coup de pied bien placé. Cependant, il existe une solution avec un nombre de pièces minimal : 3 pièces de 10 centimes, 1 pièce de 5 centimes et 3 pièces de 2 centimes. Est-ce donc possible de trouver une solution autrement que par intervention divine ? Bien sûr !

## Programmation dynamique

Avant d'aborder l'algorithme, quelques notions théoriques sur la programmation dynamique, qui en est le principe clé. Avec l'exemple précédent, nous avons entraperçu un algorithme glouton (qui, dans les grandes lignes, fonce sur la première possibilité optimale qui se présente) et un algorithme avec du backtracking (qui calcule sans réflexion et qui, en cas d'impasse, revient en arrière pour reprendre ses calculs), ainsi que leurs inconvénients ici. La programmation dynamique, lorsqu'elle est applicable, permet de s'affranchir des deux difficultés présentées.

Qu'est-ce qu'on voudrait ? Un programme qui  : rend toujours (dans l'idéal...) la monnaie, quels que soient le système de pièces et le montant, dans un temps raisonnable (donc pas toi, backtracking) et qui garantit rendre la monnaie avec un nombre de pièces minimal.

Une idée serait de pouvoir calculer en "peu de temps" la solution pour notre problème incrémentalement, c'est-à-dire en calculant petit à petit la solution, et en particulier, en s'aidant des calculs sur des problèmes plus petits pour résoudre le problème initial plus gros. Un choix astucieux des plus petits problèmes à considérer est donc primordial.

Formalisons cette idée un peu vague.

En effet, soit un problème à plusieurs types de paramètres : dans l'exemple qui nous intéresse, on a deux types de paramètres, le système de pièces, avec 5 instances, et le montant à rendre, que l'on peut découper en 42 instances : 0 euro, 1 centime, 2 centimes, ..., 41 centimes. On cherche d'abord à décomposer le problème en sous-problèmes en ses paramètres, qui seront supposés plus rapides et plus simples à résoudre : ici par exemple, on a 5x42 sous-problèmes, qui sont de chercher à rendre 0, 1, ..., 41 centimes avec des pièces de valeur inférieure au égale à 2 centimes, 5 centimes, 10 centimes, 50 centimes et 1 euro.

Pour cela, on cherche d'abord un ou plusieurs cas de base : les cas où on peut répondre le plus rapidement sont les 5 sous-problèmes qui consistent à rendre 0 euro avec des pièces (ça devrait aller), et également les problèmes qui consistent à rendre de la monnaie avec des pièces de 2 cts uniquement, dont on ne peut déduire des sous-problèmes, vu que la pièce de 2 cts est la pièce de plus petite valeur de notre système de monnaie.

Puis, pour récupérer la solution du problème global, on cherche une relation (dite de récurrence) impliquant un ou des sous-problèmes bien choisis qui répondra à un problème de taille supérieure. Puis on choisit un ordre de résolution pour cette famille de sous-problèmes qui permettra d'exploiter la relation de récurrence.

Dans notre exemple, si on veut rendre 20 centimes avec des pièces de valeur inférieure ou égale à 5 cts, on cherche à ajouter une pièce de 5 cts, puis à retrouver la solution minimale pour rendre 15 cts avec des pièces de valeur inférieure ou égale à 5 cts. On fait alors appel au sous-problème (15 cts, 5 cts) qui est bien strictement plus petit que notre problème (20 cts, 5 cts). Or la solution optimale pour rendre 15 cts en pièces de 2 ou 5 cts est en 3 pièces (de 5 centimes). Donc la solution optimale de (20 cts, 5 cts) est donc 1 + 3 = 4 pièces.

Déduisons de cet exemple la démarche générale (pour deviner une relation de récurrence, rien ne vaut un exemple).

Pour rendre un montant m avec des pièces de valeur inférieure ou égale à v (problème (m,v)), si v est plus grand strictement que m, alors on retourne la solution du problème (m,v') où v' est la plus grande valeur de pièce strictement inférieure à v; sinon, si n est la solution optimale du problème (m-v,v), alors on retourne 1+n.

Vous pouvez voir l'algorithme implémenté sur la page précédente.

## Analyse de l'algorithme de programmation dynamique

Avant toute chose : cet algorithme termine-t-il ? Nous pouvons répondre immédiatement : oui, car pour la construction du tableau least_coins, on n'a que des boucles for, qui donnent explicitement le nombre (fini) de boucles de l'algorithme. On a justifié aussi dans l'algorithme que la boucle while pour la construction de chosen terminait.

Cela vérifié, faisons tourner cet algorithme à la main sur notre exemple. Il est bon aussi de le tester sur des exemples plus simples pour être au moins relativement convaincu qu'il donne le bon résultat.

Donc, pour les 41 cts que Bob attend désespérément, à rendre avec des pièces de valeur 2, 5 et 10 cts, si T[i][j] = least_coins[i][j] :

T[10][41] = 1 + T[10][31] = 1 + 1 + T[10][21] = 1 + 1 + 1 + T[10][11]

Or T[5][11] + 1 = 1 + T[5][6] = 1 + T[2][6] = 1 + 1 + 1 + 1 + T[2][0] = 4 est inférieur à T[10][11] (car le tableau least_coins est initialisé à infini. C'est bizarre dit comme cela, mais en pratique, c'est juste un très grand entier)

Et de même, T[5][6] est supérieur à T[2][6] = 3 pour la même raison.

Il en résulte que T[10][41] = 3 + 4 = 7 pièces (3 de 10 cts, 1 de 5 cts, 3 de 2 cts).

## Pour aller plus loin

L'exemple ci-dessus vous a peut-être convaincu, mais ce n'est pas assez rigoureux pour montrer que l'algorithme donne le bon résultat pour tout problème de rendu de monnaie, c'est-à-dire qu'il est correct. Toutefois, l'un des avantages les plus importants de la programmation dynamique est que la correction de l'algorithme tombe pratiquement tout crue. C'est une (sorte de) démonstration par récurrence. On montre que la solution trouvée pour le cas de base est optimale, puis que la relation de récurrence donne une solution optimale à partir des solutions optimales des sous-problèmes.

La programmation dynamique permet de réaliser les calculs avec un temps optimal, mais pas forcément en espace. La plupart du temps, on stocke les calculs intermédiaires pour les sous-problèmes dans un tableau/une matrice, par exemple least_coins ici. Une façon d'encore limiter le temps de calcul est d'appeler récursivement sur la relation de récurrence, au lieu de calculer itérativement : autrement dit, créer un tableau, faire une fonction rendu(valeur maximale des pièces, montant) qui récupère la valeur associée dans le tableau si elle est déjà calculée, et qui sinon le complète. On l'appelle alors avec les paramètres de notre problème global.

Cela permet de ne calculer que les sous-problèmes dont nous avons besoin, et pas tous. La terminaison est peut-être moins évidente à déceler dans cette version récursive, mais la valeur des arguments de la fonction appelée décroît strictement jusqu'à arriver aux paramètres pour le cas de base, donc l'algorithme termine.

Enfin, revenons sur l'algorithme glouton précédent. En réalité, il n'est pas totalement mauvais : il est même optimal en temps et en espace, sous certaines conditions portant sur le système de monnaie, qui est alors dit canonique : ce serait le cas de notre système si nous lui avions ajouté la pièce de 1 ct. La raison étant que l'on peut rendre n'importe quelle somme en pièces de 1 ct, même si ce n'est pas très pratique. Il est intéressant d'ailleurs de noter qu'aujourd'hui la plupart des distributeurs utilisent cet algorithme glouton, essentiellement car il est très rapide par rapport à la programmation dynamique. Et sans doute parce que les distributeurs sont plus résistants aux coups de pied qu'il n'y paraît.
