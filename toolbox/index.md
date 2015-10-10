---
layout: page
title: Boîte à outils
front: true
---

## Compilation

Pour un fichier A.cpp

    make A

La commande officielle est :

    g++ -w -O2 -pipe -std=gnu++0x A.cpp -o A

## Tests

Pour exécuter un fichier de tests :

    ./A < A.in

Pour exécuter un [tas de fichiers de tests](https://bitbucket.org/jilljenn/acm/src) :

    for x in *in; do ./A < $x; done
    cat *out # Pour comparer

## Graphviz

Pour visualiser un graphe, la syntaxe est la suivante :

    digraph G {
        rankdir=LR;
        s -> 1 [label=1];
        s -> 2;
        1 -> 3;
        1 -> 4 [label=1];
        2 -> 4;
        3 -> t;
        4 -> t [label=1];
    }

Et la commande :

    dot -Tpng graph.dot > graph.png

Donne le graphe suivant :

<img src="/static/graphviz.png" />

Par exemple, ce code C++ peut faire l'affaire :

{% highlight c++ %}
void graphviz() {
    cout << "digraph G {" << endl;
    int v;
    for(int u = 0; u < 2 * n + 2; ++u) {
        for(int i = 0; i < graph[u].size(); ++i) {
            v = graph[u][i];
            cout << u << " -> " << v << "[label=" << flow[u * SIZE + v] << "];" << endl;
        }
    }
    cout << "}" << endl;
}
{% endhighlight %}

En remplaçant éventuellement `flow` par `capacity`.
