---
layout: page
title: Configuration tips
parent: Competitions
---

1. TOC
{:toc}

## Compilation

Pour un fichier A.cpp

    make A

La commande [officielle](https://swerc.eu/2023/environment/) est :

    g++ -x c++ -Wall -Wextra -O2 -std=gnu++20 -static -pipe A.cpp -o A

### C++ compilation flags

If we take a obviously bad code:

```c++
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main(void) {
    int t[5];
    cout << t[6] << endl;
    return 0;
}
```

If your compiler flags contain (i.e. the "args" of your tasks.json config file in VSCode/Codium):

                "-fsanitize=address",
                "-fsanitize=undefined",
                "-std=c++20",

Then you should have some nice error message:

    bad.cpp:7:16: runtime error: index 6 out of bounds for type 'int [5]'
    bad.cpp:7:16: runtime error: load of address 0x7fffffffd5d8 with insufficient space for an object of type 'int'

## Tests

Pour exécuter un fichier de tests :

    ./A < A.in

Pour exécuter un [tas de fichiers de tests](https://bitbucket.org/jilljenn/acm/src) :

    for x in *in; do ./A < $x; done
    cat *out  # Pour comparer

You may want to check cph [competitive programming helper](https://codeforces.com/blog/entry/116939). There are browser extensions to import the testcases in VSCode or other IDEs.

I am impressed by [the notebook of KTH](https://github.com/kth-competitive-programming/kactl) which is tested, like any notebook should be.

If you want to troll, you should learn about [policy-based data structures](https://codeforces.com/blog/entry/11080).

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

### Version OCaml

Merci à Clémence Réda pour cette version.

{% highlight ocaml %}
(* La fonction prend en argument un graphe non orienté sous forme de liste *)
(* d'adjacence et affiche le graphe correspondant sous forme d'un code DOT *)

type graphe = int*int list array;;

let print = Printf.printf;;

let grapheno g = 
  let n=Array.length g in
  print "graph g { \n";
  for i=0 to (n-1) do
     let rec affiche liste = match liste with
      |[] -> ()
      |(b,c)::q -> print "%d -- %d [label=%d]; \n" i b c;affiche q
     in affiche g.(i);
  done;print " } \n";;

(* version orientée *)

let grapheo g = 
  let n=Array.length g in
  print "digraph g { \n";
  for i=0 to (n-1) do
     let rec affiche liste = match liste with
      |[] -> ()
      |(b,c)::q -> print "%d -> %d [label=%d]; \n" i b c;affiche q
     in affiche g.(i);
  done; print " } \n";;

(* version avec liste d'arêtes, non orienté *)

let graphelno g =
   print "graph g { \n";
   let rec affiche liste = match liste with
     |[] -> print " } \n"
     |(i,j,poids)::q -> print "%d -- %d [label=%d]; \n" i j poids;affiche q
   in affiche g;;

(* version avec liste d'arêtes, orienté *)

let graphelo g =
   print "digraph g { \n";
   let rec affiche liste = match liste with
     |[] -> print " } \n"
     |(i,j,poids)::q -> print "%d -> %d [label=%d]; \n" i j poids;affiche q
   in affiche g;;

let graphe = [(1,2,0);(3,1,0);(4,5,0);(4,8,0);(1,7,0);(1,4,0);(7,1,0);(2,4,0)];;
graphelno graphe;;
{% endhighlight %}
