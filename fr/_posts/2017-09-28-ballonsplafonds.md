---
layout: fr
title: Des ballons et des plafonds
author: Guillaume Aubian
---

<style TYPE="text/css">
code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
    }
});
MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

Nous allons résoudre le problème **B** du subregional brésilien **ACM-ICPC 2013**, disponible [ici](http://codeforces.com/gym/101473/attachments/download/5792/20132014-acmicpc-brazil-subregional-programming-contest-en.pdf). Il s'agit du plus dur des dix problèmes, puisque c'est le seul que personne n'a résolu sur place.

## Le problème

On vous donne l'emplacement de plusieurs plafonds éventuellement en biais. Au sol sont attachés des ballons remplis d'hélium. Une fois libérés, les ballons s'envolent. Dès qu'ils rentrent en contact avec un des plafonds, deux choses sont possibles :

* soit le plafond est horizontal, et le ballon reste bloqué.
* soit le plafond est en biais, et le ballon glisse le long du plafond jusqu'à l'extrémité la plus haute, avant de quitter ledit plafond.

À la fin, chaque ballon soit s'est envolé dans le ciel, soit est bloqué contre un plafond horizontal.

<img src="/fr/images/ballonsplafonds/grid_balloons.svg" style="float: center"/>

Si le problème se résout facilement, la grosse difficulté est la complexité temporelle : vu le nombre de plafonds et de ballons, une complexité linéarithmique est attendue !

## La solution

### L'idée générale

Dans un premier temps, on rajoute un plafond horizontal au dessus de tous les autres plafonds. Ce faisant, aucun ballon ne va s'envoler dans le ciel : si ça avait du être le cas, le ballon se serait retrouvé bloqué dans le plafond qu'on vient de rajouter. Quand on renvoie la solution, il faut faire attention au fait que les ballons coincés dans ledit plafond se sont en fait envolés.

Pour résoudre notre problème, on va considérer l'ensemble des points du plan correspondant :
* à la position initiale d'un ballon.
* à la position finale d'un ballon.
* à la plus haute des extrémités d'un plafond non-horizontal.

On appelle $E$ l'ensemble des tels points du plan.

L'interêt d'un tel ensemble réside dans le fait que :
* il est facile d'associer à chaque point $x \in E$ le point suivant de $E$ par lequel passe un ballon à la position $x$.
* ayant construit ceci, c'est facile de retrouver la position finale d'un ballon passant par une position de $E$ donnée.

### La relation d'équivalence $\sim$

Soit $\sim$ la relation sur $E$ définie telle que $x \sim y$ si et seulement si un ballon à la position $x$ finit au même endroit qu'un ballon à la position $y$. On vérifie que $\sim$ est réflexive, symétrique et transitive : c'est une *relation d'équivalence*.

Pour savoir où finit un ballon dans une position initiale $x \in E$, on va juste considérer la classe $E_{x} \in E / \sim$ telle que $x \in E_{x}$, et renvoyer le point le plus haut de cette classe d'équivalence.

Une structure de donnée — particulièrement facile à coder — est toute désignée pour faire ça : [union-find](https://fr.wikipedia.org/wiki/Union-find).

Initialement, les classes de $E / \sim$ sont les singletons d'éléments de $E$. Pour chaque $x \in E$, on trouve $y$ la position suivante de $E$ par laquelle passe un ballon à la position $x$, et on unit les classes d'équivalences de $x$ et de $y$.

{% highlight c++ %}
#include <bits/stdc++.h>

using namespace std;
using pos = pair<int,int>;

pos find(map<pos,pos> &uf, pos x) {
    uf[x] = (uf.find(x) == uf.end() || uf[x] == x) ? x : find(uf,uf[x]);
    return uf[x];
}

void unite(map<pos,pos> &uf, pos x, pos y) {
    pos ufx = find(uf,x), ufy = find(uf,y);
    uf[ufx] = uf[ufy] = ufx.second > ufy.second ? ufx : ufy;
}
{% endhighlight %}

On remarque qu'on s'est débrouillé pour que les représentants des classes d'équivalence de $E / \sim$ soient toujours les plus hauts possibles. Ainsi, pour trouver où finit un ballon passant par une position $x \in E$, il n'y a qu'à renvoyer le représentant de la classe d'équivalence de $x$ dans $E / \sim$.

### Une solution naïve

On peut déjà coder une solution naïve : on itère sur tous les $x \in E$, puis pour chaque plafond, on calcule l'intersection entre ledit plafond et la verticale partant de $x$ vers le haut, l'intersection la plus basse correspond au plafond contre lequel va coller un ballon situé en $x$ en premier : appellons ce plafond $e$.

On définit alors y ainsi :
* si $e$ est horizontal, $y$ est l'intersection entre $e$ et la verticale partant de $x$ vers le haut.
* sinon $y$ est l'extrémité la plus haute de $e$.

Dans tous les cas, $y$ est l'élément suivant de $E$ par lequel passe un ballon partant de $x$.

On a besoin de deux fonctions :
* la première prend le plafond juste au dessus d'un point $p$, l'abscisse $x$ de $p \in E$ , et renvoie le prochain point de $E$ par lequel passe un ballon situé en $p$.
* Le deuxième — notée *cmp_range* — permet de comparer deux plafonds situés à la verticale d'un même point, pour trouver le plus bas.

{% highlight c++ %}
using edge = pair<pos,pos>;

pos which_side(edge e, int x) {
    int yl = e.first.second, yr = e.second.second;
    if(yl < yr) return e.second;
    else if(yl > yr) return e.first;
    else return {x,yl};
}

double corr_y(edge e, int x) {
    pair<double,double> l = e.first, r = e.second;
    if(r.first == l.first) return l.second;
    double p = ((double) x - l.first) / ((double) (r.first - l.first)); 
    return ((double) l.second) + p * ((double) (r.second - l.second));
}

bool cmp_range(edge a, edge b) {
    int alx = a.first.first, blx = b.first.first;
    int l = max(alx,blx);
    return corr_y(a,l) < corr_y(b,l);
}
{% endhighlight %}

Comme on itère sur chaque point de $E$, puis sur chaque arête, notre algorithme a une complexité quadratique, ce qui n'est pas assez efficace pour résoudre le problème.

### La solution efficace

Quand on s'intéresse à un $x \in E$ et qu'on itère sur tous les plafonds, on se rend compte qu'on perd *beaucoup* de temps, sur des plafonds qui ne sont même pas à la verticale de $x$. Ce serait bien que quand on traite un $x \in E$, on ait stocké quelque part tous les plafonds à la verticale de $x$.

**Eh bien c'est faisable !**

Pour cela, on utilise une méthode classique : **la sliding window**.

On va s'intéresser à nos plafonds/ballons de la gauche vers la droite (i.e. par abscisse croissante), en s'arrêtant sur des évènements bien particuliers : les extrémités de plafonds et les ballons.

On conserve en parallèle une liste de plafonds en cours : quand on croise l'extrémité gauche d'un plafond, on rajoute celui-ci à cette liste, et quand on croise l'extrémité droite correspondante, on l'y enlève.

Disons que l'on stocke les plafonds en cours dans un *set\<edge\>* que l'on nomme *current_edges*.

C'est là qu'apparaît l'idée qui permet d'avoir du $O(nlog(n))$ : les plafonds de l'ensemble *current_edges* sont tous à la verticale d'un même point. On vérifie donc facilement que la relation *cmp_range* est réflexive, antisymétrique et transitive sur l'ensemble *current_edges* : c'est une *relation d'ordre*. Étant donné un plafond $e$, on peut donc trouver le plus bas plafond plus haut que $e$ en temps logarithmique grace à une dichotomie. Quitte à ce que $e$ soit un segment dégénéré réduit à un point, on peut facilement trouver le plus bas plafond plus haut qu'un point donné. 

À vrai dire, pas besoin de coder de dichotomie, le module *set* de C++ possède déjà ce qu'il nous faut avec la fonction *upper_bound*.

{% highlight c++ %}
bool cmp_ord(pair<pos,pair<int,int>> a, pair<pos,pair<int,int>> b) {
    if(a.first.first < b.first.first) return true;
    if(a.first.first > b.first.first) return false;
    return a.second < b.second;
}

const int maxcoord = 1000001;

int main() {
    int N, C;
    cin >> N >> C;
    N++;
    vector<edge> edges(N);
    vector<pos> balloons(C);
    vector<pair<pos,pair<int,int>>> ord((2 * N)+C);
    map<pos,pos> uf;
    for(int i = 0; i < N - 1; ++i) {
	int w, x, y, z;
	cin >> w >> x >> y >> z;
	vector<pos> two_pow ={% raw %} {{w,x},{y,z}}; {% endraw %}
	sort(two_pow.begin(),two_pow.end());
	edges[i] = {two_pow[0],two_pow[1]};
	ord[2*i] = {edges[i].first,{-1,i}};
	ord[(2*i) + 1] = {edges[i].second,{1,i}};
    }
    edges[N-1] = {% raw %} {{-1,maxcoord},{maxcoord,maxcoord}}; {% endraw %}
    ord[2*(N-1)] = {edges[N-1].first,{-1,N-1}};
    ord[2*(N-1) + 1] = {edges[N-1].second,{1,N-1}};
    for(int i = 0; i < C; ++i) {
	int x;
	cin >> x;
	balloons[i] = {x,0};
	ord[2*N + i] = {balloons[i],{0,i}};
    }
    sort(ord.begin(),ord.end(),cmp_ord);
    bool(*cmp_pt)(edge,edge) = cmp_range;
    set<edge,bool(*)(edge,edge)> current_edges(cmp_pt);
    for(pair<pos,pos> x : ord) {
	pos y = x.first;
	edge eabove = *current_edges.upper_bound({y,y});
	pos z = which_side(eabove,y.first);
	if(x.second.first == 0) unite(uf,y,z);
	else {
	    pair<pos,pos> e = edges[x.second.second];
	    if(y == e.first) {
	        current_edges.insert(e);
		if(y.second > e.second.second) unite(uf,y,z);
	    }
	    else {
		current_edges.erase(e);
		if(y.second > e.first.second) unite(uf,y,z);
	    }
	}
    }
    for(pos p : balloons) {
	pos q = find(uf,p);
	if(q.second == maxcoord) cout << q.first << endl;
	else cout << q.first << " " << q.second << endl;
    }
}
{% endhighlight %}

Un évènement est représenté par une paire (position,(genre de l'évènement, indice du plafond/ballon correspond)) : le genre de l'évènement est $0$ pour un ballon, $-1$ pour l'extrémité gauche d'un plafond et $1$ pour l'extrémité droite.

On trie d'abord les évènements selon l'abscisse de la première coordonnée, puis selon le genre de l'évènement : ceci permet d'éviter les problèmes de ballons à la verticale d'une extrémité de plafond.

