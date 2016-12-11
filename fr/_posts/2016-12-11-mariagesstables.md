---
layout: fr
title: Mariages stables, ou comment marier le Prix Nobel d'économie aux sites de rencontres
author: Jill-Jênn Vie & Clémence Réda
---

Note : Une partie de cet article a été reprise d'[ici](http://binaire.blog.lemonde.fr/2016/10/17/a-p-b-la-vie-apres-le-bac/), mais pas de panique, c'était à moi.

## Contexte

La question du mariage stable en informatique, loin d'être une affaire de moeurs plus ou moins libres, intervient assez régulièrement dans des domaines divers de notre vie quotidienne, d'Admission Post Bac à Meetic. Il est à noter que ce problème peut se poser aussi en économie, et que sa résolution algorithmique a valu à l'un de ses concepteurs un Prix Nobel.

Mais revenons à nos mariages. Le point commun (du moins, celui qui nous intéresse) entre Meetic et Admission Post Bac ? Former de façon optimale des couples d'éléments de deux groupes distincts d'individus ou d'entités: bacheliers/établissements de l'enseignement supérieur, hommes/femmes, ... L'optimalité dans un mariage s'agissant traditionnellement d'éviter que l'un des partenaires ne parte chercher son bonheur ailleurs (autrement dit, que deux personnes qui sont engagées dans deux mariages différents se préfèrent à leurs conjoints respectifs) chaque élément pour les deux groupes exprime une liste de préférences qu'il faut respecter au mieux.

## Un exemple concret

Prenons l'exemple d'une application de rencontres telle que Meetic. Vous êtes chargé(e) de faire enfin rencontrer l'amour à d'irascibles célibataires (hétérosexuels, pour simplifier). Vous faites alors la connnaissance d'Anna, Bérénice et Charlotte, et d'Alain, Bernard et Cédric.

Résumons les objectifs à atteindre : (1) sachant qu'il existe le même nombre d'individus pour chaque groupe, il faut marier tous les individus, (2) la polygamie n'étant donc pas autorisée dans cette version de l'algorithme, il faut qu'à un élément de l'un des groupes ne soit associé qu'un seul et unique élément de l'autre groupe, (3) il faut avoir une méthode qui nous assure qu'il n'existe pas de couples (Ariane, Adrien) et (Solal, Isolde) tels qu'Ariane préfère Solal à Adrien et que Solal préfère Ariane à Isolde, ou que Adrien préfère Isolde à Ariane et qu'Isole préfère Adrien à Solal, ce qui constituent des cas de mariage instables.

Une méthode naïve de faire naître l'alchimie entre ces êtres serait de tirer aléatoirement un membre de chaque sexe et d'organiser une rencontre. Cependant, Anna peut avoir rencontré Bernard, et Charlotte, Alain, puis avoir toutes deux décidé d'entamer une relation sans attendre de voir les autres célibataires. Puis plus tard, lors d'un dîner à quatre en l'honneur de leur célibat perdu, Charlotte peut très bien réaliser qu'elle préfère Bernard à son compagnon actuel, et Bernard se dire qu'après tout, Charlotte lui est plus sympathique qu'Anna : bam, mariage instable.

Pour éviter ce cas gênant, avant la période des rencontres, vous demandez à ces six personnes de vous remettre solennellement après réflexion une liste des célibataires qu'elles désirent voir, dans l'ordre croissant de préférence. On suppose que les participants ne mentent pas sur leur liste de préférences, ni qu'ils ne changent d'avis entretemps... (la différence entre l'algorithmique et la vraie vie).

Une autre méthode serait de ne considérer que les voeux d'un seul groupe, par exemple, de ne considérer que les voeux des femmes, et de choisir pour chacune d'entre elles l'homme qu'elles préfèrent. Mais si Anna et Charlotte sont toutes deux follement éprises de Bernard, comment les départager ? Et la personne qui parle de choisir au hasard dans ces situations est priée de sortir. Il est facile d'imaginer que si le sort attribue Charlotte à Bernard, et que Bernard s'avère un fervent admirateur d'Anna au détriment de sa chère et tendre, nous retombons sur un cas de mariage instable.

Il va donc falloir prendre en compte les voeux des individus des deux groupes.

## Algorithme de Gale-Shapley (1962)

La lourde tâche vous revient donc de marier de façon optimale les six personnes précédemment citées entre elles. Pour mener à bien votre projet, notons que l'on peut associer deux personnes A et B (c'est-à-dire qu'à part si on trouve un meilleur arrangement, on mariera dans le futur A avec B).

Prenons l'un des hommes arbitrairement -nous verrons plus tard que l'ordre n'influe pas sur le résultat final- Alain : sa liste indique qu'il voudrait voir Anna, Charlotte et sinon Bérénice. Associons-le pour l'instant avec Anna. Passons à Bernard, qui lui aimerait voir Charlotte, Bérénice, puis Anna. Puisque Charlotte n'est encore associée à personne, vous pouvez mettre Bernard avec Charlotte. Enfin, Cédric indique sur sa liste qu'il souhaiterait voir Charlotte, puis Anna, puis Bérénice. Vous pouvez mettre Cédric avec Bérénice, dernière femme disponible. Mais, si Charlotte avait placé Cédric avant Bernard dans sa liste ? (Il fallait bien que les ordres de préférence des femmes interviennent à un moment. Heureusement...) Vous retomberiez sur la situation décrite dans le paragraphe précédent.

Dans le cas où Charlotte préfère Cédric à Bernard, le mieux est alors de rompre le couple Charlotte/Bernard, et d'associer finalement Cédric à Charlotte, et Bernard à Bérénice. Le couple Anna/Alain est conservé. Vous obtenez un mariage stable -victoire !

Formalisons l'intuition décrite ci-dessus. Soient M et F les deux groupes disjoints d'entités à associer. Chaque élément de M et de F n'appartient au début à aucun couple, et soit L[i] la liste de préférence d'éléments de F de l'élément i de M, triée dans l'ordre croissant de préférence, telle que tout élément de cette liste n'a pas encore été envisagé pour former un couple avec l'élément i. Soit également Lf[i] la liste triée par ordre de préférence d'éléments de M de l'élément i de F. Il est important de constater que les listes Lf ne seront pas modifiées durant l'algorithme, contrairement aux listes L.

Tant qu'il existe un élément i de M qui n'est dans aucun couple, tel que L[i] soit non vide

1) prendre un tel élément m
2) retirer le premier élément f de la liste L[m]. Si f n'appartient à aucun couple :
3) a) alors créer le couple (m,f)
3) b) sinon considérer le couple actuel (m',f). Si m' est placé avant m dans Lf[f] :
3) a) i) alors ne rien modifier
3) a) ii) sinon rompre le couple (m',f) et créer le nouveau couple (m,f)

Fin du tant que
Retourner la liste des couples créés

L'instruction "ne rien modifier" peut paraître surprenante et faire douter de la terminaison de l'algorithme. Mais on peut constater que le nombre d'éléments dans l'ensemble des listes L décroît strictement à chaque boucle tant que et finira par atteindre zéro, car on envisage une association à chaque fois. Ouf, vous n'y passerez pas la nuit.

Faisons tourner cet algorithme à la main. On associe à Alain le nombre 1, à Bernard 2 et à Cédric 3. De même, on associe à Anna le nombre 1, à Bérénice 2 et à Charlotte 3. On peut donc avoir en entrée de l'exemple précédent :

L[1] = {1,3,2}, L[2] = {3,2,1}, L[3] = {3,1,2}

Lf[1] = {1,2,3}, Lf[2] = {3,1,2}, Lf[3] = {1,2,3}

Soit couples la liste (initialisée à vide) qui contient les couples de personnes associées.

Prenons m = 1 (Alain). Le premier élément de L[1] est 1 (Anna). On ajoute donc à couples la paire (1,1).

A la deuxième itération, on considère m = 2 (Bernard). Le premier élément de L[2] est 3 (Charlotte). On ajoute donc à couples la paire (2,3).

A la troisième itération, on considère m = 3 (Cédric). Le premier élément de L[3] est 3 (Charlotte). Comme Charlotte est déjà associée à Bernard, on considère Lf[3] la liste de préférences de Charlotte. Comme 2 (Bernard) est placé avant 3 (Cédric) dans LF[3], Charlotte reste avec Bernard, et on associe à Cédric Bérénice. On ajoute alors à couples la paire (3,2).

Tous les éléments de M étant associés, on stoppe l'algorithme. couples contient alors (1,1),(2,3),(3,2). Et on vérifie que cela forme un mariage stable -qui ne présente pas de cas d'instabilité. 

## Pour aller plus loin

La preuve de correction de cet algorithme consiste à montrer que ce dernier fait bien ce qu'on lui demande : après les trivialités (chaque instance de M et de F apparaît une et une seule fois dans la liste des couples créés, les couples sont des paires constituées d'un élément de M et d'un élément de F...), vérifier que pour tous couples (m,f) et (m',f') retournés, il est impossible que m préfère f' à f, et f' préfère m à m' (ou que f préfère m' à m, et m', f à f'), autrement dit, que le mariage soit instable. Un raisonnement par l'absurde permet de confirmer que l'algorithme est correct.

Par exemple, considérons le cas où il y a deux couples (m,f) et (m',f') tels que m préfère f' à f, et f' préfère m à m'. Mais si le couple (m,f) a été retourné par l'algorithme, et que m préfère f' à f, alors nécessairement, d'après l'algorithme, ou (1) m a déjà envisagé de s'associer à f' alors que celle-ci était associée à un m'' (non nécessairement m') placé avant m, et, dans ce cas, si (m',f') a été retourné par l'algorithme, alors soit m'' = m', soit m' est placé avant m'' dans la liste des préférences de f', donc finalement, f' préfère m' à m'', lui-même préféré à m, ce qui contredit l'hypothèse. Ou (2) m et f' ont été associés (car f' n'était associée à personne, ou à quelqu'un de moins bien placé que m dans sa liste de préférences, quand m a envisagé de s'associer avec elle), mais un jour, un m'' placé devant m dans la liste de préférences de f a envisagé de s'associer à f', et le couple (m,f') a été rompu pour former (m'',f'), puis ou m'' = m', ou à son tour m' placé devant m'' dans la liste de préférences de f' a fait rompre le couple (m'',f') pour former (m',f'). Donc f' préfère m' à m'', et m'' à m, ce qui contredit de nouveau l'hypothèse. L'autre cas cité se traite de la même façon.

Une première chose est de se demander comment faire dans le cas où les deux groupes ne sont pas de la même taille. Il faut avoir redéfinir l'idée de mariage instable, en ajoutant le cas où B engagé dans une relation avec A préfère C qui est célibataire.

Une autre chose importante est de remarquer que, si l'ordre pour considérer les hommes ne compte pas (un raisonnement par l'absurde fonctionne bien pour le démontrer), dans cette version de l'algorithme, les préférences des éléments de M sont privilégiées par rapport à celles des éléments de F. En effet, reprenons l'exemple du dessus. Nous avons les couples Anna/Alain, Charlotte/Bernard et Bérénice/Cédric. Nous n'avons eu besoin de prendre en compte à aucun moment les préférences de Bérénice par exemple, alors que nous avons dû au moins une fois évaluer les préférences de chaque homme. Que ses préférences soient Cédric, Alain, Bernard ou Bernard, Alain et Cédric, la liste de couples suivant l'algorithme précédent n'aurait pas changé. Il est alors facile de constater que la situation s'inverse si le "tant que" de l'algorithme précédent concerne les éléments de F plutôt que ceux de M.