---
layout: page
title: Algorithms
has_children: true
nav_order: 1
---

# Résolution de problèmes algorithmiques

This page [in English](/index-en)

## Code : la bibliothèque tryalgo de 128+ algorithmes

Nous avons implémenté plusieurs algorithmes et structures de données en une [bibliothèque Python](https://pypi.python.org/pypi/tryalgo/).

    pip install tryalgo

- [Voir les codes sur GitHub](https://github.com/jilljenn/tryalgo)
- [Lire la documentation](https://jilljenn.github.io/tryalgo/)
- [Télécharger tous les fichiers en un seul ZIP](https://github.com/jilljenn/tryalgo/archive/master.zip)

<iframe src="https://ghbtns.com/github-btn.html?user=jilljenn&amp;repo=tryalgo&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

## Notre livre : *Programmation efficace*

<a href="http://www.amazon.fr/gp/product/2340010055/ref=as_li_tl?ie=UTF8&amp;camp=1642&amp;creative=19458&amp;creativeASIN=2340010055&amp;linkCode=as2&amp;tag=mangaki-21"><img src="/static/cover.jpg" style="float: right" width="180" /></a>

Nous avons écrit un livre sur la programmation compétitive en Python, qui documente la majore partie de notre bibliothèque `tryalgo`. Il a été publié en plusieurs langues.

Les [**nombreux problèmes algorithmiques**]({% post_url fr/2016-03-15-problemes-algorithmiques %}) de ce livre constituent une préparation efficace aux [**concours de programmation**](/contests/) et entretiens d'embauche d'entreprises spécialisées en informatique.

On y trouve les algorithmes classiques de géométrie ou de recherche de plus court chemin mais également des sujets plus atypiques tels que les [arbres de Fenwick]({% post_url fr/2016-03-09-arbre-de-fenwick %}) ou les liens dansants de Knuth.

**Niveau :** à partir de la L3, ou dès le lycée pour les participants à [Prologin](http://prologin.org) :)

- [acheter en français](http://www.amazon.fr/gp/product/2340010055/ref=as_li_tl?ie=UTF8&camp=1642&creative=19458&creativeASIN=2340010055&linkCode=as2&tag=mangaki-21)
- autres langues : [anglais](http://www.cambridge.org/9781108716826), [chinois](https://book.douban.com/subject/30210075/), [taiwanais](http://www.drmaster.com.tw/Bookinfo.asp?BookID=MP11906)
- [Erratum des versions française et anglaise](/errata)

## Problèmes

- [Liste de problèmes](problems)
- [Liste de compétitions](competitions)

Cf. notre [notebook Jupyter](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb) : [**TryAlgo Maps in Paris**](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank"><img src="/static/paris.png" /></a>

## Blog : Solutions

<a href="{% post_url fr/2016-11-19-swerc-2016 %}"><img src="/fr/images/swerc2016/swerc2016-thumb.jpg" style="float: right" /></a>

### Derniers posts

<ul>
{% for post in site.posts limit:10 %}
    <li> {{ post.date | date: "%b %-d, %Y" }} <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.author }}
    </li>
{% endfor %}
</ul>

### À propos des auteurs

[**Christoph Dürr**](http://www-desir.lip6.fr/~durrc/) est directeur de recherche CNRS en informatique à Sorbonne Université. Spécialisé en algorithmique, il a enseigné à l'École polytechnique de 2007 à 2014 et entraîne régulièrement des équipes pour le concours de programmation [ICPC](/acm/).  
À part ça, il aime beaucoup les carrot-cakes.

[**Jill-Jênn Vie**](http://jill-jenn.net) est chargé de recherches à Inria. Ancien élève de l’École normale supérieure de Paris-Saclay, il a participé à l’organisation du concours d’informatique Prologin de 2010 à 2014.  
À part ça, il est féru de [métafiction](https://club-meta.fr).


Voici un pseudo-code à appliquer pour apprendre un max d'algorithmes :

```python
import tryalgo                 # import all you can eat

try:
    problem = read(statement)    # needs organisation
    algo = solve(problem)        # needs skills
    solution = implement(algo)   # needs experience
    answer = submit(solution)
    assert answer == "Accept"
except SubmissionError:
    learn_more()
```
