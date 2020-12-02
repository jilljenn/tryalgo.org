---
layout: fr
title: Compte rendu de l'atelier n° 1
excerpt_separator: <!--more-->
---

## Table des matières

**Généralités**

- [Prise en main](#welcome)
- [Lecture d'un fichier](#read)
- [Écriture dans un fichier](#write)
- [Format des chaînes de caractères](#format)
- [Sous-listes](#sublists)
- [Parcourir une liste](#iterators)

**Activités**

- [Calcul d'intérêts](#banque)
- [Liste des mots de la langue française](#dico)
- [Statistiques sur le Top 250 IMDb (au format JSON)](#imdb)
- [Utilisation d'une API de météo](#meteo)
- [Jeu des boîtes](#boites)
- [Parcours du graphe de Paris](#paris)

<!--more-->

**Ressources**

- [France-ioi](http://www.france-ioi.org/algo/index.php) regorge d'exercices pour progresser !
- Visiblement, [apprendre-python.com](http://apprendre-python.com) est bien fait
- Si vous obtenez une erreur incompréhensible, tapez-la dans Google, vous atterrirez très probablement sur le site de questions-réponses [Stack Overflow](http://stackoverflow.com).

## Généralités

<h3 id="welcome">Prise en main</h3>

[Suivre les instructions ici](http://jill-jenn.net/algo/stage-python/welcome.html)

Concernant les itérateurs qu'on retrouve dans les boucles :

{% highlight python %}
range(3)  # [0, 1, 2]
range(2, 6)  # [2, 3, 4, 5]
{% endhighlight %}

<h3 id="read">Lecture d'un fichier</h3>

{% highlight python %}
with open('fichier.txt') as f:
    for line in f:
        # Pour retirer le retour de ligne final
        line = line.strip()
{% endhighlight %}

Ou bien, pour directement obtenir la liste des lignes :

{% highlight python %}
dico = open('fichier.txt', encoding='utf-8').read().splitlines()
{% endhighlight %}

<h3 id="write">Écriture dans un fichier</h3>

Par exemple, pour dessiner un rectangle 5 × 3 d'étoiles :

{% highlight python %}
# 'w' pour 'write'
with open('fichier.txt', 'w') as f:
    for i in range(5):
        f.write('*' * 3 + '\n')
        # '\n' : caractère de fin de ligne
{% endhighlight %}

<h3 id="format">Format des chaînes de caractères</h3>

{% highlight python %}
print("Je m'appelle", prenom, "et j'ai", age, "ans")
# est équivalent à
print("Je m'appelle %s et j'ai %d ans" % (prenom, age))
# 's' pour 'string' et 'd' pour 'digits', un entier
{% endhighlight %}

<h3 id="sublists">Sous-listes</h3>

Testez les lignes suivantes :

{% highlight python %}
l = liste(1, 101)  # Nombres de 1 à 100
print(l[5])
print(l[2:7])
print(l[:4])
print(l[-3:])
print(l[::3])
print(l[5:45:4])
{% endhighlight %}

Lorsqu'on écrit ``l[n1:n2:n3]`` :

- le premier nombre désigne l'indice de début ;
- le deuxième l'indice de fin ;
- le troisième le pas.

<h3 id="iterators">Parcourir une liste</h3>

Ces deux codes affichent ligne après ligne les caractères d'une chaîne.

{% highlight python %}
# i parcourt [0, 1, …, len(chaine) - 1]
for i in range(len(chaine)):
    print(chaine[i])
# est équivalent à
for lettre in chaine:
    print(lettre)
{% endhighlight %}

Le deuxième a l'avantage d'être plus lisible mais on perd l'information de position du caractère courant dans la chaîne.

## Activités

<h3 id="banque">Calcul d'intérêts</h3>

À partir de :

{% highlight python %}
taux = 5
somme = 27
nb_mois = 10
{% endhighlight %}

Écrire une fonction qui affiche à chaque mois la somme majorée par le taux d'intérêts.

{% highlight python %}
for i in range(1, nb_mois + 1):
    somme = somme * (1 + taux / 100)
    print("Au mois", i, "j'ai", somme)
{% endhighlight %}

Si on crée la fonction suivante, qui prend en argument les paramètres ``somme`` et ``taux`` :

{% highlight python %}
def augmentation(somme, taux):
    return somme * (1 + taux / 100)
{% endhighlight %}

{% highlight python %}
# on peut remplacer la ligne du code précédent
somme = somme * (1 + taux / 100)
# par
somme = augmentation(somme, taux)
{% endhighlight %}

Plus lisible, et notamment pratique lorsque la fonction est sur plusieurs lignes et est réutilisée à plusieurs endroits dans le code. *Don't repeat yourself.*

<h3 id="dico">Liste des mots de la langue française</h3>

[Suivre les instructions ici](http://jill-jenn.net/algo/stage-python/dictionnaires.html)

Sur [cette liste de 336 531 mots](http://jill-jenn.net/algo/stage-python/_static/dico.txt) on pouvait par exemple écrire une fonction qui renvoie le nombre de mots commençant par une certaine lettre donnée en argument :

{% highlight python %}
def commence_par(lettre):
    nb_mots = 0
    for mot in dico:
        if mot[0] == lettre:
            nb_mots += 1
    return nb_mots
{% endhighlight %}

On peut ensuite appeler ``commence_par('c')``, par exemple.

<h3 id="imdb">Statistiques sur le Top 250 IMDb (au format JSON)</h3>

[Suivre les instructions ici](http://jill-jenn.net/algo/stage-python/dictionnaires.html)

Pour déterminer par exemple les dix années où sont sortis le plus de films dans le Top 250, la structure ``Counter`` est très utile, grâce à sa méthode ``most_common`` déjà programmée.

{% highlight python %}
from collections import Counter

nb_occ = Counter()
for film in top:
    nb_occ[film["year"]] += 1
for annee, valeur in nb_occ.most_common(10):
    print('En', annee, 'il y a eu', valeur, 'films dans le top 250')
{% endhighlight %}

<h3 id="meteo">Utilisation d'une API de météo</h3>

Certains sites Web proposent un service appelé API (*application programming interface*) permettant d'obtenir des réponses à des requêtes de type :

- « Quel temps fait-il dans la ville de Cachan ? »  
[http://api.openweathermap.org/data/2.5/weather?q=Cachan](http://api.openweathermap.org/data/2.5/weather?q=Cachan)
- ou « Quel est la durée du film *Inception* ? »  
[http://www.omdbapi.com/?t=Inception](http://www.omdbapi.com/?t=Inception)

(pour afficher plus joliment les données obtenues, essayez [jsonprettyprint.com](http://jsonprettyprint.com))

Seulement, le service nous fournit trop d'informations pour notre utilisation. Pour obtenir la température d'une ville, il faut donc :

- récupérer toutes les données d'une ville en se connectant à ladite adresse ;
- filtrer les données pour ne conserver que la température (en degrés Kelvin) ;
- convertir cette donnée en degrés Celsius et afficher le résultat.

{% highlight python %}
from urllib.request import urlopen
from urllib.parse import urlencode
import json

def get_data(ville):
    return json.loads(urlopen('http://api.openweathermap.org/data/2.5/weather?%s' % urlencode({'q': ville})).read().decode('utf-8'))

def k2c(t):  # Conversion °K -> °C
    return t - 273.15

def afficher_meteo(ville):
    data = get_data(ville)
    celsius = k2c(data['main']['temp'])
    print('À', ville, 'il fait', round(celsius, 2), '°C')

afficher_meteo('La Roque d\'Anthéron')
{% endhighlight %}

<h3 id="boites">Jeu des boîtes</h3>

[Règles du jeu](http://jill-jenn.net/algo/stage-python/_static/jeu.pdf)

<h3 id="paris">Parcours du graphe de Paris</h3>

(Bientôt.)
