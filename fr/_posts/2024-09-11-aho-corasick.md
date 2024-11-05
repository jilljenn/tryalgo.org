---
layout: fr
title: Aho-Corasick
category: strings
author: Christoph Dürr
---

Étant donnée une liste de chaînes de caractères L, construire une structure de données qui permet en temps linéaire d'identifier toutes les occurrences des mots de L à l'intérieur d'un mot S donné. 

## Note

(dernière mise à jour de ce billet: 5 novembre 2024)

Ce billet est inspiré d'une page similaire du site web excellent [CP-Algorithms](https://cp-algorithms.com/string/aho_corasick.html), qui a son tour est une traduction d'un site web russe très complet.

Dans ce billet nous allons utiliser de manière interchangeable les termes *chaîne*, *chaîne de caractères* et *mot*.

## Idée clé

L'algorithme de Knuth-Morris-Pratt construit en quelque sorte un automate à partir d'un mot W donné, et permet en temps linéaire d'identifier toutes les occurrences de W comme sous-chaîne d'une chaîne S donnée. Plutôt que de construire un automate indépendant pour chaque mot dans L, on va construire un seul automate pour tout l'ensemble des mots dans L.

## Arbre préfixe

Le premier ingrédient est de construire un arbre préfixe (aussi appelé une *trie*), pour tous les mots dans L. L'arbre est enraciné avec des arcs qui pointent partant de la racine. Les arcs sortant d'un nœud sont étiquetés par des lettres distinctes. Ainsi on associe à un nœud un mot qui est la concaténation des lettres le long du chemin de la racine vers ce nœud. Si le mot est dans L, alors cette propriété est stockée dans un attribut `pattern` du nœud. Dans notre implémentation, `pattern` sera l'indice du mot dans L, ou la constante -1 le cas échéant.

Dans l'illustration ci-dessous, les nœuds correspondants à des mots dans L={i,in,tin,sting} sont montrés avec un contour double. Les arcs rouges et bleus seront expliqués par la suite.

<img src="/fr/images/aho-corasick1.svg" style="float: center"/> 

## Liens suffixes

Un tel arbre va être utilisé comme un automate. En partant de la racine, on va suivre les liens sortants tel qu'indiqués par les lettres successives dans S. 

Supposons que l'exécution de l'automate a atteint un sommet v, après avoir traité un préfixe T de S, et que la prochaine lettre est c. Malheur: aucun arc sortant n'est étiqueté par c. Que faire ? Il nous faut bien aller vers un sommet de l'arbre, mais lequel ? 

L'idée est que nous cherchons à maintenir l'invariant suivant. À chaque sommet u de l'arbre correspond un mot, tel que défini par le chemin de la racine vers u. Certains de ces mots pourraient être des suffixes de T. Et le mot associé à v est le plus long de ces suffixes.

Alors comme il n'y pas d'arc avec c qui sort de v, on doit se rabattre sur un suffixe plus court. Soit w le mot associé au nœud v. On cherche alors le sommet u qui correspond au plus long suffixe strict de w. *Strict* veut dire qu'il n'est pas w lui-même, mais plus court. 

L'arbre est augmenté avec un *lien suffixe* partant de tout sommet, excepté la racine, qui dans cet exemple va de v à u. Et on va suivre ces liens, jusqu'à ce qu'on tombe sur un sommet qui aurait un arc sortant étiqueté par la lettre c, au pire de cas on remonte vers la racine. Puis on fait la transition habituelle par la lettre c à partir de ce sommet.

On pourrait penser alors que le traitement d'une chaîne $s$ ne se fait pas en temps linéaire en la longueur de $s$, car pour une lettre donnée on doit suivre peut-être plusieurs liens suffixe. Imaginons que nous observons dans $s$ une fenêtre. La sous-chaine de $s$ dans la fenêtre est le mot qui correspond au nœud courant dans la trie. Quand nous traitons la lettre suivante dans $s$, nous agrandissons la fenêtre vers la droite d'une position, et quand nous remontons avec un lien suffix dans la trie, alors nous diminuons la fenêtre de la gauche par au moins une position. Les deux bords de la fenêtre ne vont que vers la droite et leur nombre total de déplacements est majoré par deux fois la longueur de $s$.

Mais comment calculer ces liens suffixes? Considérons un arc $u\rightarrow v$ dans la trie, étiqueté par la lettre $c$. En remontant les liens suffixes de $u$, on trouve le premier sommet $u'$, avec un arc sortant $u'\rightarrow v'$ qui est également étiqueté par la lettre $c$. Confondons pour cette explication les nœuds de la trie avec le mot auxquels ils correspondent. Comme $u'$ est un suffixe strict de $u$, on a également que $u'c$ est un suffixe strict de $uc$. Et comme $u'$ est le premier nœud rencontré avec un arc sortant étiqueté par $c$, la chaîne $u'c$ aussi le plus grand des suffixes de $uc$ qui correspond à un nœud dans la trie.

Dans l'illustration ci-haut, les arcs suffixes sont montrés en rouge.

## liens output

Voici une première procédure de recherche.

    Construire la trie et les liens suffixes
    v = racine
    pour toute lettre c dans la chaîne s:
        # avancer dans la trie
        tant qu'il n'existe pas d'arc sortant v -> v' étiqueté par c:
            v = v.suffix
        v = v'
        si v est marqué comme correspondant à un des motifs à trouver:
            annoncer une occurrence de ce motif dans s

Si on applique cette procédure avec l'exemple donnée sur la chaîne `stingin`, alors on trouve bien les occurrences

~~~
stingtin
sting
     tin
~~~

mais on a raté d'autres occurrences de motifs, comme par exemple `i` et `in`. Raison est que certains motifs apparaissent dans d'autres. Alors il faut que pendant le parcours dans la trie, à chaque fois qu'on est dans un nœud v, qu'on trouve tous les suffixes de v (incluant v lui-même), qui soit un des motifs à détecter. Pour cela il suffit de remonter les liens suffixes à partir de v et annoncer une occurrences pour chacun les nœuds rencontrés marqués comme étant des motifs à détecter. Pour accélérer cette recherche, on crée des raccourcis vers le prochain suffix marqué. Nous illustrons ces raccourcis par des arcs bleus qu'on appelle liens `output`.

Par exemple dans la trie ci-haut, il y a un lien `output` de `sti` directement vers `i`.

## Complexité 

La construction de la trie se fait en temps O(mk) où m est la longueur totale des mots dans L, et k est la taille de l'alphabet. **Attention** il faut vérifier pour ce billet que la construction des liens suffix se fait également en temps linéaire.


La recherche des occurrences des mots de L dans un mot S se fait en temps linéaire en la longueur de S.

## Détails d'implémentation 

Les arcs sortant sont implémentés par un tableau `next`. À la place des lettres on travaille en interne avec leur rang, avec un décalage tel que la plus petite lettre a le rang 0. La constante `LOW` donne le code Ascii de la plus petite lettre et `LEN` donne la taille de l'alphabet. Les codes Ascii des lettres dans l'alphabet doivent se suivre sans interruption.

Pour construire les liens suffixe on fait un parcours en largeur de la trie. Ainsi on aura traité les niveaux précédant un nœud au moment de le traiter. Ceci se fait avec une file `Q`, contenant des sommets à traiter.

Ce code contient également une méthode `dump` qui génère l'illustration de ce billet.

{% highlight python %}
class Vertex:
    """Vertex of the Aho-Corasick trie
    """

    LOW = ord('a')  # Ascii code of smallest letter in the alphabet
    LEN = 26        # Alphabet size

    def index(ch):  # transforms the character into internal index
        i = ord(ch) - Vertex.LOW
        assert 0 <= i < Vertex.LEN
        return i

    def __init__(self):
        self.pattern = -1 # -1 means no pattern, otherwise it is the pattern index
        self.next   = [None] * Vertex.LEN
        self.suffix = None
        self.output = None    

class Aho_Corasick:

    def __init__(self, patterns):
        """patterns is a list of strings. 
        Later when we search for them, we return only their index in that list 
        and the matching position.
        
        :complexity: O(sum(map(len, patterns)))
        """
        # 1. build the trie
        self.root = Vertex()
        for pattern_index, p in enumerate(patterns):        
            # add pattern p to the trie
            v = self.root   # current vertex in the tree ...
            for ch in p:    # ... corresponding to a prefix of p
                i = Vertex.index(ch)
                if v.next[i] is None:   # create vertices on the fly
                    v.next[i] = Vertex()
                v = v.next[i]           # descend in the trie
            v.pattern = pattern_index   # mark that this is a pattern
        # 2. augment with suffix and output links
        Q = []                          # queue of vertices to be processed
        for v in self.root.next:        # special case for direct root descendants
            if v is not None:
                v.suffix = self.root 
                Q.append(v)             # initially Q contains the first level vertices
        while Q:
            u = Q.pop()                     # process u
            for i, v in enumerate(u.next):  # all arcs u -> v labeled i
                if v is not None:
                    a = u.suffix            # go up using suffix links
                    while a is not None and a.next[i] is None:
                        a = a.suffix 
                    if a is not None and a.next[i] is not None:
                        v.suffix = a.next[i]
                        if v.suffix.pattern != -1:
                            v.output = v.suffix
                        else:
                            v.output = v.suffix.output 
                    else:
                        v.suffix = self.root
                    Q.append(v)
        
    def match(self, s):
        """ find all substrings of s which are among the stored strings.
            Iterates over positions in s and the matched string ending at this position.
        """
        v = self.root               # current vertex
        for j, ch in enumerate(s):
            i = Vertex.index(ch)    # descend one step
            while v is not self.root and v.next[i] is None:
                v = v.suffix        # return until transition is possible
            if v.next[i] is not None:
                v = v.next[i] 
            a = v               # now output all found patterns
            while a is not None:
                if a.pattern != -1:
                    yield(j, a.pattern)
                a = a.output
        
    def dump(self):
        """ Produces a dot format representation of the trie
        """ 
        print("digraph G {")
        seen = set()
        Q = [(self.root, 0, "")]
        level = [[self.root]]
        while Q:
            v, r, s = Q.pop()       # vertex, rank, string
            if id(v) not in seen:
                seen.add(id(v))
                if r == len(level):
                    level.append([v])
                else:
                    level[r].append(v)
                if v.pattern != -1:
                    double = "double"
                else:
                    double = ""
                print(f'{id(v)} [shape="{double}circle", label="{s}"]')
                for i in range(Vertex.LEN):
                    ch = chr(i + Vertex.LOW)
                    if v.next[i] is not None:
                        print(f'{id(v)} -> {id(v.next[i])} [label="{ch}"]')
                        Q.append((v.next[i], r+1, s + ch))
                if v.suffix is not None:
                    print(f'{id(v)} -> {id(v.suffix)} [color="red"]')
                if v.output is not None:
                    print(f'{id(v)} -> {id(v.output)} [color="blue"]')
        for same in level:
            print("{rank=same;", end="")
            print(*map(id,same), sep=";", end="}\n")
        print("}")        


if __name__ == "__main__":
    patterns = ["i", "in", "tin", "sting"]
    AC = Aho_Corasick(patterns)
    AC.dump()
    s = "istingin"
    print(s)
    for e, p in AC.match("istingin"):
        k = len(patterns[p])
        print(" "*(e-k+1) + patterns[p])
{% endhighlight %}

## Problèmes

Attention, le code Python est trop lent pour ces problèmes.

- [Word Puzzles](https://www.spoj.com/problems/WPUZZLES/)
- [Ada and Jobs](https://www.spoj.com/problems/ADAJOBS/)