---
layout: fr
title: Aho-Corasick
category: strings
author: Christoph Dürr
---

Étant donnée une liste de chaînes de caractères L, construire une structure de données qui permet en temps linéaire d'identifier toutes les occurrences des mots de L à l'intérieur d'un mot S donné. 

## Note

Ce billet est inspiré d'une page similaire du site web excellent [CP-Algorithms](https://cp-algorithms.com/string/aho_corasick.html), qui a son tour est une traduction d'un site web russe très complet.

Dans ce billet nous allons utiliser de manière interchangeable les termes *chaîne*, *chaîne de caractères* et *mot*.

## Idée clé

L'algorithme de Knuth-Morris-Pratt construit en quelque sorte un automate à partir d'un mot W donné, et permet en temps linéaire d'identifier toutes les occurrences de W comme sous-chaîne d'une chaîne S donnée. Plutôt que de construire un automate indépendant pour chaque mot dans L, on va construire un seul automate pour tout l'ensemble des mots dans L.

## Arbre préfixe

Le premier ingrédient est de construire un arbre préfixe (aussi appelé une *trie*), pour tous les mots dans L. L'arbre est enraciné avec des arcs qui pointent partant de la racine. Les arcs sortant d'un nœud sont étiquetés par des lettres distinctes. Ainsi on associe à un nœud un mot qui est la concaténation des lettres le long du chemin de la racine vers ce nœud. Si le mot est dans L, alors cette propriété est stockée dans un attribut `output` du nœud. Dans notre implémentation, `output` sera l'indice du mot dans L.

Dans l'illustration ci-dessous, les nœuds correspondants à des mots dans L sont montrés avec un contour double.

<img src="/fr/images/aho-corasick1.svg" style="float: center"/> 

Les nœuds v de l'arbre auront également un pointeur sur l'ancêtre u dans l'arbre, et la lettre qui a mené de u à v. Ces variables sont appelées `ancestor` et `anc_i` dans notre implémentation.

## Liens suffixes

Un tel arbre va être utilisé comme un automate. En partant de la racine, on va suivre les liens sortants tel qu'indiqués par les lettres successives dans S. 

Supposons que l'exécution de l'automate a atteint un sommet v, après avoir traité un préfixe T de S, et que la prochaine lettre est c. Malheur: aucun arc sortant n'est étiqueté par c. Que faire ? Il nous faut bien aller vers un sommet de l'arbre, mais lequel ? 

L'idée est que nous cherchons à maintenir l'invariant suivant. À chaque sommet u de l'arbre correspond un mot, tel que défini par le chemin de la racine vers u. Certains de ces mots pourraient être des suffixes de T. Et le mot associé à v est le plus long de ces suffixes.

Alors comme il n'y pas d'arc avec c qui sort de v, on doit se rabattre sur un suffixe plus court. Soit w le mot associé au nœud v. On cherche alors le sommet u qui correspond au plus long suffixe strict de w. *Strict* veut dire qu'il n'est pas w lui-même, mais plus court. 

L'arbre est augmenté avec un *lien suffixe* partant de tout sommet, qui dans cet exemple va de v à u. Et on va suivre ces liens, jusqu'à ce qu'on tombe sur un sommet qui aurait un arc sortant étiqueté par la lettre c, au pire de cas on remonte vers la racine. Puis on fait la transition habituelle par la lettre c à partir de ce sommet.

Pour ne pas à avoir retrouver à chaque fois cette recherche, on stocke dans chaque nœud v dans une table `tr` (pour *transition*), la destination de cette dernière transition. Concrètement `v.tr[c]` serait ce nœud atteint par la transition.

Mais comment calculer ces liens suffixes? Il nous suffit de remonter de v, vers son ancêtre v', de suivre son lien suffix à lui, puis faire une transition par la lettre qui a mené de v à v'.

Ainsi deux fonctions sont intimement liées. `get_link` qui calcule le lien suffix d'un nœud et `go(c)` qui effectue une transition à partir d'un nœud donné. 

Notez que les liens suffixes sont calculés au fur et à mesure des besoins, et pas d'un coup initialement.

Dans l'illustration ci-dessous, les sommets correspondant à des mots de L ont un double bord. Les arcs sortant du trie sont en noir. Les liens suffixes sont en blue, et les arcs de transition en vert. L'arbre a été calculé pour les mots "A", "AB", "BC", "BCA", "C" et "CAA". Les liens de suffixe et de transition sont apparus après avoir fait dérouler l'automate sur le mot "ABCACAABBA".

<img src="/fr/images/aho-corasick3.svg" style="float: center"/> 

## Complexité 

La construction de l'arbre se fait en temps O(mk) où m est la longueur totale des mots dans L, et k est la taille de l'alphabet.

La recherche des occurrences des mots de L dans un mot S se fait en temps linéaire en la longueur de S.

## Détails d'implémentation 

Les arcs sortant sont implémentés par un tableau `next`. À la place des lettres on travaille en interne avec leur rang, avec un décalage tel que la plus petite lettre a le rang 0. La constante `LOW` donne le code Ascii de la plus petite lettre et `LEN` donne la taille de l'alphabet. Les codes Ascii des lettres dans l'alphabet doivent se suivrent sans interruption.

L'ancêtre de la racine est la racine elle même. C'est par ce test qu'on identifie la racine.

{% highlight python %}
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Aho-Corasick

christoph dürr - 2024
"""

__all__ = ["Aho_Corasick"]

class Vertex:
    """Vertex of the Aho-Corasick trie
    """

    LOW = ord('@')  # Ascii code of smallest letter in the alphabet
    LEN = 27        # Alphabet size

    def __init__(self, ancestor, anc_i):
        self.next = [None] * Vertex.LEN
        self.output = -1
        self.tr = [None] * Vertex.LEN
        self.anc_i = anc_i          # char rank leading to vertex from ancestor
        if ancestor is None:        # vertex is the root
            self.ancestor = self    
            self.link = self
        else:
            self.ancestor = ancestor
            if ancestor.ancestor is ancestor:
                self.link = ancestor 
            else:
                self.link = None

    def go(self, i):
        """ follow a go link for given character with rank i"""
        if self.tr[i] is None:
            if self.next[i] is not None:
                self.tr[i] = self.next[i]
            elif self.ancestor is self:
                self.tr[i] = self 
            else:
                self.tr[i] = self.get_link().go(i) 
        return self.tr[i] 
    
    def get_link(self):
        if self.link is None:
            self.link = self.ancestor.get_link().go(self.anc_i)
        return self.link 
    

class Aho_Corasick:

    def __init__(self, words):
        self.root = Vertex(None, -1)
        for k, s in enumerate(words):        
            """ ajoute la chaîne s"""
            v = self.root   # descendre dans l'arbre
            for ch in s:    # créer des sommets manquants
                i = ord(ch) - Vertex.LOW
                if v.next[i] is None:
                    v.next[i] = Vertex(v, i)
                v = v.next[i]
            v.output = k 

    def match(self, s):
        """ find all substrings of s which are among the stored strings.
            Iterates over positions in s and the matched string ending at this position.
        """
        v = self.root 
        for i, ch in enumerate(s):
            v = v.go(ord(ch) - Vertex.LOW)
            if v.output != -1:
                yield (i, v.output)
{% endhighlight %}

## Problèmes

Attention, le code Python est trop lent pour ces problèmes.

- [Word Puzzles](https://www.spoj.com/problems/WPUZZLES/)
- [Ada and Jobs](https://www.spoj.com/problems/ADAJOBS/)