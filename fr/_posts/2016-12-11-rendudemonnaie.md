---
layout: fr
title: Rendu de monnaie, bases de programmation dynamique
author: Jill-Jênn Vie & Clémence Réda
---

## Contexte

Le problème du rendu de monnaie s'énonce de façon simple : étant donné un système de pièces à disposition (je ne peux rendre que des pièces de 50 centimes, 1 euro, 2 euros...) et un montant à rendre, rendre ce montant avec un nombre minimal de pièces du système que l'on s'est donné. Les applications d'une solution à ce problème sont faciles à concevoir : nul n'a envie de récupérer 1 euro en pièces de 1 centime s'il s'est aventuré à payer 2 euros pour une malheureuse bouteille de soda à un distributeur. Non, vraiment personne.

## Une première méthode

Imaginons un distributeur de boissons un peu particulier, quelque part dans l'Union européenne, qui rend la monnaie, uniquement en pièces de 2 centimes, 5 centimes, 10 centimes, 50 centimes et 1 euro.

Une première méthode serait de considérer les pièces une par une, en commençant par les pièces de plus grande valeur, et de décroître le montant à rendre (en enlevant la valeur de la pièce que l'on considère à ce moment) jusqu'à ce que le montant soit inférieur à la valeur de la pièce que l'on regarde. On considère alors la plus grande valeur de pièce inférieure au montant, et on itère le raisonnement jusqu'à ce que le montant atteigne zéro.

Petite note : cette méthode correspond à un algorithme *glouton*, c'est-à-dire un algorithme qui prend une décision sans regarder les conséquences sur le problème global. Pour cet algorithme, on choisit de rendre la pièce de plus grande valeur, inférieure au montant, tant que le montant mis à jour reste inférieur à cette pièce, sans vérifier que cette condition assure de rendre la totalité du montant. 

Par exemple : ma machine veut rendre 1 euro 22 centimes. Avec le système que l'on s'est posé ci-dessus :

* On regarde la pièce de 1 euro. Alors on peut enlever une pièce de 1 euro au montant : on obtient 22 centimes à rendre. Or 22 centimes est inférieur à 1 euro et à 50 centimes, donc on passe à la pièce de 10 centimes.

* On regarde la pièce de 10 centimes. Alors on peut enlever deux fois la pièce de 10 centimes pour obtenir 2 centimes à rendre (inférieur à 10 centimes et à 5 centimes).

* On regarde la pièce de 2 centimes. Il suffit d'enlever une pièce de 2 centimes pour rendre le montant total.

Au final, l'algorithme retourne "rendre 1 pièce de 1 euro, 2 pièces de 10 centimes, 1 pièce de 2 centimes". Et bonne nouvelle, les instructions de la méthode peuvent être implémentées. 

On note *amount* le montant, et *coins* qui est un tableau -trié !- qui contient dans chaque case une valeur de pièce différente du système que l'on s'est donné (par exemple, pour notre système, cela donne [2,5,10,50,100]) : dans la case *i*, on a la valeur de la *i*ème plus petite valeur de pièce. 

Le but est d'obtenir un tableau *chosen* (qui a pour taille le nombre de pièces différentes de notre système de pièces) tel que dans la case *i* on a le nombre de pièces de *i*ème plus petite valeur nécessaire pour rendre le montant *amount*. 

On note pour tout tableau T, T[i] la valeur de la *i*ème case de T, et *n* le nombre de pièces du système. Pour les moins informaticiens d'entre vous, il est important de noter que dans un algorithme *amount* est une variable qui contient un entier (en centimes), et non un entier en lui-même. Autrement dit, *amount* peut varier au cours du temps. C'est une case mémoire que l'on peut regarder, augmenter ou diminuer. Et c'est la même chose pour chaque case du tableau *coins*. Le symbole "A <- x" signifie affecter la valeur x à la variable A.

En pseudocode, cela peut donner :

{% highlight python %}
Pour i allant de 1 à n
    Tant que amount >= coins[i] 
        1) amount <- amount - coins[i]
        2) chosen[i] <- chosen[i] + 1
Retourner le tableau chosen
{% endhighlight %}

Pour l'implémentation en Python, voir ci-dessous :

{% highlight python %}
def moneyback(amount, coins):
    n = len(coins)
    chosen = [0] * n 
    for i in range(n - 1, -1, -1):
        while amount >= coins[i]: 
            amount -= coins[i] 
            chosen[i] += 1 
    assert amount == 0 
    return chosen
{% endhighlight %}

Petit commentaire du code : à la ligne 4, le -1 permet de parcourir le tableau coins dans l'ordre décroissant du numéro de cases, pour récupérer la plus grande valeur de pièce. A la ligne 5, on recherche la plus grande valeur de pièce inférieur au montant qu'il reste à rendre. A la ligne 6, on utilise la pièce trouvée, et on met à jour le montant qu'il reste à rendre. A la ligne 7, on augmente donc le nombre de pièces de cette valeur utilisées pour rendre la monnaie sur le montant initial. A la ligne 8, on vérifie que l'on a bien rendu toute la monnaie (sinon le client va râler !). A la ligne 9, on retourne le tableau contenant le nombre de pièces rendues de chaque type.

Par exemple, en utilisant l'algorithme ci-dessus pour 1 euro 77 centimes à rendre, et notre système de pièces précédent :

{% highlight python %}
amount = 177
coins = [2, 5, 10, 50, 100]

moneyback(amount, coins)
>> chosen = [1, 1, 2, 1, 1]
{% endhighlight %}

(Pour celles et ceux qui ne sont pas familiers avec Python, on initialise les variables *amount* et *coins* puis on appelle la fonction *moneyback* pour obtenir le résultat).

En effet, pour 177 centimes, sur notre système de pièces de 2 cts, 5 cts, 10 cts, 50 cts et 1 €, on a décomposé nos 177 centimes en 1 pièce de 2 cts, 1 pièce de 5 cts, 2 pièces de 10 cts, 1 pièce de 50 cts et 1 pièce de 1 €. Donc 100 + 50 + 10x2 + 5 + 2 = 177 ! Ouf, ça marche !

Hum, vraiment ?

Supposons à présent que Bob souhaite acheter un jus de tomate à 1,59 €, et qu'il ait entré 2 euros dans la machine. Le montant à rendre est donc 41 centimes. Si vous faites tourner l'algorithme ci-dessus avec cette initialisation, il va crasher. Il VA crasher, croyez-moi.

Que s'est-il donc passé ? Reprenons l'algorithme calmement, nonobstant le fait qu'il vient de nous crasher/cracher à la figure (pas très sympa). L'exception relevée souligne que l'on n'a pas rendu (apparemment) le bon montant, ce qui correspond à la ligne "*assert amount == 0*" dans le code Python. Prenons notre bon (?) vieux système 2-5-10-50-100. On doit rendre 41 centimes. Cela élimine déjà la possibilité de rendre avec une pièce de 1€ ou de 50 cts. On peut prendre des pièces de 10 cts, puisque 10 cts < 41 cts.

On prend alors 4 pièces de 10 centimes et... on reste bloqué. Car il faut rendre encore 1 centime ! Si la machine était douée de parole, elle pourrait éventuellement convaincre le client que la perte d'un ridicule centime est bien futile. Si le client avait tout son temps, la machine pourrait reprendre ses calculs, et s'arrêter à 3 pièces de 10 centimes, puis regarder les autres pièces. On appelle cela faire du *backtracking* : autrement dit, si un calcul plante, on revient sur nos pas, et on reprend nos calculs depuis une position qui nous permet de choisir une autre façon de calculer, par exemple ici, choisir seulement 3 pièces de 10 centimes et chercher à décomposer le montant restant avec des pièces de 5 et 2 centimes. Il est clair que non seulement cette stratégie ne garantit pas la minimalité du nombre de pièces, car la machine va crier victoire dès qu'elle aura trouvé une solution, même non optimale, mais qu'en plus, cela risque de prendre un certain temps, puisqu'on peut faire les calculs, dans le pire cas, pour toute combinaison de pièces. Ouf, c'était la parenthèse *backtracking*.

Donc, nous sommes bien dans la vie, la vraie, et la seule issue, qui semble inéluctable, est la destruction de la machine par un coup de pied bien placé. Cependant, il existe une solution avec un nombre de pièces minimal : 3 pièces de 10 centimes, 1 pièce de 5 centimes et 3 pièces de 2 centimes. Est-ce donc possible de trouver une solution autrement que par intervention divine ? Bien sûr !

## Programmation dynamique

Avant d'aborder l'algorithme, quelques notions théoriques sur la *programmation dynamique*, qui en est le principe clé. Avec l'exemple précédent, nous avons entraperçu un algorithme glouton (qui, dans les grandes lignes, fonce sur la première possibilité, qui paraît optimale, qui se présente) et un algorithme avec du backtracking (qui calcule sans réflexion et qui, en cas d'impasse, revient en arrière pour reprendre ses calculs), ainsi que leurs inconvénients ici. La programmation dynamique, lorsqu'elle est applicable, permet de s'affranchir des deux difficultés présentées.

Qu'est-ce qu'on voudrait ? Un programme qui : rend toujours (dans l'idéal...) la monnaie, quels que soient le système de pièces et le montant, dans un temps raisonnable (donc pas toi, backtracking) et qui garantit rendre la monnaie avec un nombre de pièces minimal.

Une idée serait de pouvoir calculer en "peu de temps" la solution pour notre problème *incrémentalement*, c'est-à-dire en calculant petit à petit la solution, et en particulier, en s'aidant des calculs sur des problèmes plus petits pour résoudre le problème initial plus gros. Un choix astucieux de l'ordre des plus petits problèmes à considérer est donc primordial.

Formalisons cette idée un peu vague.

En effet, soit un problème à plusieurs types de paramètres : dans l'exemple qui nous intéresse, on a deux types de paramètres :
* le système de pièces, avec 5 instances;
* le montant à rendre, que l'on peut découper en 42 instances : 0 euro, 1 centime, 2 centimes, ..., 41 centimes.

(1) On cherche d'abord à décomposer le problème en sous-problèmes en ces différents paramètres, qui seront supposés plus rapides et plus simples à résoudre : ici par exemple, on a 5x42 sous-problèmes, qui sont "chercher à rendre 0/1/ .../ 41 centimes avec des pièces de valeur inférieure au égale à 2 centimes/5 centimes/10 centimes/50 centimes/1 euro".

(2) Pour cela, on cherche d'abord un ou plusieurs *cas de base* : les cas où on peut répondre le plus rapidement sont les cinq sous-problèmes qui consistent à rendre 0 euro avec des pièces (ça devrait aller), et également les cinq sous-problèmes qui consistent à rendre de la monnaie avec des pièces de 2 cts uniquement, dont on ne peut déduire des sous-problèmes (qui porteraient sur des pièces de valeur plus petite strictement que 2 centimes), vu que la pièce de 2 cts est la pièce de plus petite valeur de notre système de monnaie.

(3) Puis, pour récupérer la solution du problème global, on cherche une relation (dite *de récurrence*) impliquant un ou des sous-problèmes bien choisis qui répondra à un problème de taille supérieure. Puis on choisit un ordre de résolution pour cette famille de sous-problèmes qui permettra d'exploiter la relation de récurrence, pour partir des sous-problèmes les plus simples, résolus ci-dessus, pour arriver au problème qui nous intéresse.

Pour éclaircir ce fouillis qui doit paraître nébuleux, par exemple, si on veut rendre 20 centimes avec des pièces de valeur inférieure ou égale à 5 cts, on cherche à retirer une pièce de 5 cts au montant courant, puis à trouver la solution optimale au problème "rendre 20-5=15 cts avec des pièces de valeur inférieure ou égale à 5 cts". On fait alors appel au sous-problème (15 cts, 5 cts) qui est bien strictement plus petit que notre problème (20 cts, 5 cts), avec (a, b) < (c, d) si et seulement si a < c ou a = c et b < d. Or la solution optimale pour rendre 15 cts en pièces de 2 ou 5 cts est en 3 pièces (de 5 centimes). Donc la solution optimale de (20 cts, 5 cts) est donc 1 + 3 = 4 pièces en tout (4 pièces de 5 centimes ici).

Déduisons de cet exemple la démarche générale (pour deviner une relation de récurrence, rien ne vaut un exemple).

Pour rendre un montant *m* avec des pièces de valeur inférieure ou égale à *v* (problème (*m*,*v*)), si *v* est plus grand strictement que *m*, alors on retourne la solution (le nombre de pièces rendues) du problème (*m*,*v'*) où *v'* est la plus grande valeur de pièce strictement inférieure à *v*; sinon, si *n* est la solution optimale (le nombre minimal de pièces rendues) du problème (*m-v*,*v*), alors on retourne *1+n*.

Ecrivons la démarche précédente en pseudocode. On initialise la matrice (un tableau qui contient dans chaque case un tableau) *least_coins* telle que *least_coins*[i][j] donne le nombre minimal de pièces pour un rendu de *j* centimes avec des pièces de valeur inférieure ou égale à celle de la *i*ème plus petite pièce du système de pièces. Les cases de *least_coins* sont initialisées à *+infini* (car tout nombre fini de pièces est inférieur à *+infini*...).

Petit précis mathématique, utile pour la résolution du cas de base avec la pièce de plus petite valeur *coins*[1] (qui est notée *coins*[0] dans l'algorithme en Python, car les tableaux sont indexés à partir de 0 en Python) : le théorème de la division euclidienne (dont on s'épargnera la démonstration) affirme que pour tous entiers positifs *a* et *b*, a >= b, il existe un unique couple d'entiers positifs (*q*, *r*) (où *q* est le quotient et *r* < b est le reste) tel que a = b x q + r.

{% highlight python %}
Initialisation du tableau least_coins
    # Cas de base
    Pour tout montant m, où 0 <= m <= amount
        Si dans la division euclidienne de m par coins[1], r = 0
           alors least_coins[0][m] <- q
    Pour i, 1 <= i <= n
        Pour j, 0 <= j <= amount
             # On donne la valeur du problème (j, coins[i-1])
             # à la solution du problème (j, coins[i])
             1) least_coins[i][j] <- least_coins[i-1][j]
             # Si retirer la pièce de valeur coins[i] au montant courant
             # permet de rendre moins de pièces que la solution du problème
             # (j, coins[i-1])
             2) Si coins[i] <= j et least_coins[i][j - coins[i]]+1 < least_coins[i][j]
                    least_coins[i][j] <- least_coins[i][j - coins[i]] + 1
# least_coins[n][amount] contient le nombre minimal de pièces rendues pour le montant amount
# avec des pièces de valeur inférieure ou égal à coins[n]
# On cherche maintenant à récupérer la valeur de chaque pièce rendue
# On initialise une variable j avec pour valeur la valeur de la variable amount
j <- amount
i <- n
Tant que j est différent de 0
   # On considère les pièces dans l ordre décroissant de valeur
    Si j >= coins[i] 
        # Si la solution minimale pour le problème (j, coins[i]) est
        # celle obtenue en enlevant une pièce de valeur coins[i] au montant j
        Si least_coins[i][j - coins[i]] + 1 = least_coins[i][j]
            # Alors on ajoute dans la case i du tableau chosen 1 (i.e. on rend une autre
            # pièce de valeur coins[i])
            1) chosen[i] <- chosen[i] + 1
            2) j <- j - coins[i]
        Sinon
            # Sinon, on ne peut pas utiliser de nouvelle pièce de valeur coins[i]
            1) i <- i - 1
Retourner le tableau chosen
{% endhighlight %}

Implémentons alors l'algorithme en Python.

{% highlight python %}
def moneyback_dyn(amount, coins):
    n = len(coins)
    least_coins = [[float('inf')] * (amount + 1) for _ in range(n)]
    for sub_amount in range(amount + 1): 
        if sub_amount % coins[0] == 0: 
            least_coins[0][sub_amount] = sub_amount #  coins[0]
    for i in range(1, n): 
        for j in range(amount + 1):
            least_coins[i][j] = least_coins[i - 1][j] 
            if coins[i] <= j: 
                if least_coins[i][j - coins[i]] + 1 < least_coins[i][j]:
                    least_coins[i][j] = least_coins[i][j - coins[i]] + 1
    chosen = [0] * n
    j = amount
    i = n - 1
    while j: 
        if j >= coins[i]:
            if least_coins[i][j - coins[i]] + 1 == least_coins[i][j]: 
                chosen[i] += 1 
                j -= coins[i] 
                continue 
        i -= 1
    return chosen
{% endhighlight %}

## Analyse de l'algorithme de programmation dynamique

Avant toute chose : cet algorithme termine-t-il ? Nous pouvons répondre immédiatement : oui, car pour la construction du tableau *least_coins*, on n'a que des boucles *for*, qui donnent explicitement le nombre (fini) de boucles de l'algorithme. On a justifié aussi dans l'algorithme que la boucle *while* pour la construction de *chosen* terminait.

Cela vérifié, faisons tourner cet algorithme à la main sur notre exemple (il sera facile de vérifier le résultat en faisant tourner l'implémentation ci-dessus). Il est bon aussi de le tester sur des exemples plus simples pour être au moins relativement convaincu qu'il donne le bon résultat.

Donc, pour les 41 cts que Bob attend désespérément, à rendre avec des pièces de valeur 2, 5 et 10 cts :

*least_coins*[10][41] = 1 + *least_coins*[10][31] = 1 + 1 + *least_coins*[10][21] = 1 + 1 + 1 + *least_coins*[10][11]

Or *least_coins*[5][11] + 1 = 1 + *least_coins*[5][6] = 1 + *least_coins*[2][6] = 1 + 1 + 1 + 1 + *least_coins*[2][0] = 4 est inférieur à *least_coins*[10][11] (car le tableau least_coins est initialisé à infini. C'est bizarre dit comme cela, mais en pratique, c'est juste un très grand entier)

Et de même, *least_coins*[5][6] est supérieur à *least_coins*[2][6] = 3 pour la même raison.

Il en résulte que *least_coins*[10][41] = 3 + 4 = 7 pièces (3 de 10 cts, 1 de 5 cts, 3 de 2 cts).

## Pour aller plus loin

L'exemple ci-dessus vous a peut-être convaincu, mais ce n'est pas assez rigoureux pour montrer que l'algorithme donne le bon résultat pour tout problème de rendu de monnaie, c'est-à-dire qu'il est correct. Toutefois, l'un des avantages les plus importants de la programmation dynamique est que la correction de l'algorithme tombe pratiquement tout crue. C'est une (sorte de) démonstration par récurrence. On montre que la solution trouvée pour le cas de base est optimale, puis que la relation de récurrence donne une solution optimale à partir des solutions optimales des sous-problèmes.

La programmation dynamique permet de réaliser les calculs avec un temps optimal, mais pas forcément en espace. La plupart du temps, on stocke les calculs intermédiaires pour les sous-problèmes dans un tableau ou une matrice, par exemple *least_coins* ici. Une façon d'encore limiter le temps de calcul est d'appeler récursivement sur la relation de récurrence, au lieu de calculer itérativement : autrement dit, créer un tableau, faire une fonction rendu(valeur maximale des pièces, montant) qui récupère la valeur associée dans le tableau si elle est déjà calculée, et qui sinon le complète. On l'appelle alors avec les paramètres de notre problème global.

Cela permet de ne calculer que les sous-problèmes dont nous avons besoin, et pas tous. La terminaison est peut-être moins évidente à déceler dans cette version récursive, mais la valeur des arguments de la fonction appelée décroît strictement (au sens que l'on a donné dans l'article) jusqu'à arriver aux paramètres pour le cas de base, donc l'algorithme termine.

Enfin, revenons sur l'algorithme glouton précédent. En réalité, il n'est pas totalement mauvais : il est même optimal en temps et en espace, sous certaines conditions portant sur le système de monnaie, qui est alors dit canonique : ce serait le cas de notre système si nous lui avions ajouté la pièce de 1 ct. La raison étant que l'on peut rendre n'importe quelle somme en pièces de 1 ct, même si ce n'est pas très pratique. Il est intéressant d'ailleurs de noter qu'aujourd'hui la plupart des distributeurs utilisent cet algorithme glouton, essentiellement car il est très rapide par rapport à la programmation dynamique. Et sans doute parce que les distributeurs sont plus résistants aux coups de pied qu'il n'y paraît.
