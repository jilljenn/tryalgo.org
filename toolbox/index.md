---
layout: page
title: Configuring VSCode
parent: Competitions
---

# Configuring VSCode

1. TOC
{:toc}

## Compile with g++

For a file `A.cpp`, the simplest command in a terminal is:

    make A

In VSCode, you can compile using Ctrl+B.

If we take an obviously bad code:

```c++
#include <iostream>
using namespace std;

int main(void) {
    int t[5];
    cout << t[6] << endl;
    return 0;
}
```

If you naively compile it, you may just get a random number displayed in your terminal.

If you click the gear after Ctrl+B, you can customize the compiler flags in `tasks.json`. Add the following `args` from [AddressSanitizer](https://github.com/google/sanitizers/wiki/addresssanitizer):

                "-fsanitize=address",
                "-fsanitize=undefined",
                "-std=c++20",

You can also add other flags from the [official SWERC command](https://swerc.eu/2024/environment/) (notably the extra `-Wall -Wextra`):

    g++ -x c++ -Wall -Wextra -g -O2 -std=gnu++20 -static -pipe A.cpp -o A

Then you should have some nice error message:

    bad.cpp:7:16: runtime error: index 6 out of bounds for type 'int [5]'
    bad.cpp:7:16: runtime error: load of address 0x7fffffffd5d8 with insufficient space for an object of type 'int'

## Compile using clang (notably on Mac)

{: .note }
Unfortunately, AddressSanitizer does not work on Apple Silicon Macs. But clang may give you nice messages anyway.

If we use clangd instead, the code above will raise the following warning:

    /usr/bin/clang -std=gnu++14 -fcolor-diagnostics -fansi-escape-codes -g /Users/jj/code/icpc/test.cpp -o /Users/jj/code/icpc/test
    /Users/jj/code/icpc/test.cpp:6:13: warning: array index 6 is past the end of the array (that has type 'int[5]') [-Warray-bounds]
        6 |     cout << t[6] << endl;
          |             ^ ~
    /Users/jj/code/icpc/test.cpp:5:5: note: array 't' declared here
        5 |     int t[5];
          |     ^
    1 warning generated.

It's also possible to download gcc on Homebrew, like `g++-15`, but you won't have AddressSanitizer anyway.

## Execute tests

To execute one file of testcases:

    ./A < A.in

To execute several files of testcases and redirect output:

    for x in *in; do ./A < $x > $x.out; done
    diff A.out A.in.out  # For example, or diff -y to display side by side

## Competitive Programming Helper

- In VSCode, install the VSCode extension **cph** [competitive programming helper](https://codeforces.com/blog/entry/116939).
- Download the browser extension **Competitive Companion** on [Chrome](https://chromewebstore.google.com/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/competitive-companion/).
- When you are on some problem statement on Kattis, click the **+** of the browser extension.
- Go back to VSCode and choose your language (`cpp`) to create a new file and import the testcases from Kattis to VSCode.

## Notebooks

[The 25-page notebook from KTH](https://github.com/kth-competitive-programming/kactl) is stress-tested, like any notebook should be.

In particular, you can check its entry about [policy-based data structures](https://codeforces.com/blog/entry/11080).

# Visualization with Graphviz

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
