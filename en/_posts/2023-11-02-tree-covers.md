---
layout: en
title: Cover trees
category: trees
author: Ahmed Akram Bouaziz, Christoph Dürr, Martín Gómez Abejón, Max Maiche et Christian Zhuang 
problems:
   "uva:11862": https://onlinejudge.org/external/118/11862.pdf
   "spoj:QTREE": https://www.spoj.com/problems/QTREE/
---

Cover a tree with paths or caterpillars.

## Cover with descending paths

Fix an arbitrary root in the given tree. Now for every vertex $v$ we have the notion of its *subtree* $T_v$ rooted at $v$.

We say that a path is descending, if for one of its extreme points $v$, the path is contained in $T_v$.

If we want to cover a tree with descending paths, then this is quite easy. For example there is the trivial solution consisting for every vertex $v$ of the singleton vertex path $\{v\}$. Alternatively we could choose for every inner vertex $v$, an arbitrary descendent $u$. The set of selected edges $(u,v)$ would form again a solution.

So usually we impose some additional conditions.

## Heavy-light decomposition

> The original definition is slightly different, but this one is easier to implement, and has the same desired property.

Here we want to choose for every inner vertex $v$, a descendent $u$ which maximizes $\|T_u\|$. Ties can be broken arbitrarily. These edges are called *heavy*. All other edges are called *light*. Now we have the property, that for every pair of vertices $u,v$ with lowest common ancestor $a$, both paths $u-a$ and $a-v$ traverse at most $\log n$ heavy paths. This is because every light edge $(u,v)$ --- with $u$ descendant of $v$ --- has the property that $T_u$ is at most half as big as $T_v$. Hence each of the two paths can contain at most a logarithmic number of light edges.

This is interesting when we have to maintain a datastructure on the tree, such vertices are labeled with numbers, and we want to add a value $k$ to every vertex along the path between two given vertices $u,v$, or return the sum of these labels along the path. If the tree were a line graph, we could use a segment tree for this purpose. Here we use a segment tree for each heavy path. In fact we can use one big segment tree, with portions of it corresponding to heavy paths.

[Here](https://wcipeg.com/wiki/Heavy-light_decomposition) is an excellent detailed explanation.

## Maximizing total path length

Here we want to remove a minimum number of edges in the tree, such that the result consists of a collection of paths. In other words, for every vertex $v$ of degree $d$  at least $3$, we have to remove $d-2$ adjacent edges. Call this number the *deletion number* of vertex $v$.

When removing an edge, it could be between to vertex of positive deletion number, or adjacent only to one. Ideally we prefer the first type of edges. But we cannot remove them greedily, see the example below.

          (a) (b) (c)
    *---1---1---1---1---*
        \|   \|   \|   \|
        *   *   *   *

If we remove the middle edge (b), then we need to remove 2 addition edges. However the optimum here is to remove edges (a) and (c).

We can solve the problem greedily using a different approach. For every vertex $v$, let $A_v$ be the maximum number of edges in a covering of $T_v$ with paths. Let $B_v$ be the same number but with the restriction, that $v$ is the extreme point of a path. This includes the case when $v$ is covered by a singleton vertex path.

Now we say that vertex $u$ is *interesting* if $A_u=B_u$. 

For a leaf $v$ we have $A_v=B_v=0$, and $v$ is interesting.

Consider a vertex $v$ and all its descendants $u$. 

- If none of the descendants is interesting, then $A_v=B_v=\sum A_u$, and $v$ is interesting.
- If a single descendant $u_0$ is interesting, then $A_v=B_v=1+\sum A_u$, and again $v$ is interesting.
- If there are at least two interesting descendants, then $A_v=2+\sum A_u$, $B_v=1+\sum B_u$, and $v$ is not interesting.

We observe that $B_v$ is either $A_v$ or $A_v-1$.

## Cover a tree with caterpillars

A caterpillar is a tree, which consists of a single path, with leafs attached to it. In other words, every vertex of degree at least $3$, can have at most 2 non-leaf neighbors. The goal is to cover the tree with caterpillars, maximizing the total number of edges in these caterpillars.

The optimal covering with caterpillars can be computed with dynamic programming. But we could only find a tedious solution. Which we sketch here.

~~~C++
/*
  Airbus vs. Boeing
  http://uva.onlinejudge.org/contests/258-febc44a2/11862.html

  dynamic programming

  We want to remove a minimal number of edges to turn a forest in a
  graph that can be drawn without crossings as a bipartite
  graph. These graphs are called caterpillars. A caterpillar is a tree
  where the longest path has only leafs attached to it.

  our notation for caterpillars:

  a-node : has two neighbors of degree>1
  b-node : has degree>1 and one neighbor of degree>1
  c-node : has degree=1

  c--b--a--a--a--b--c
    / \    \|    /\|\
   c   c   c   c c c

  DFS fixes an orientation of the trees.  
  Tv := subtree with root v
  p[v] = parent node of v in the tree

  in the following asum, bsum, csum refers to the sum over sons of v
  and k to the number of sons
  the type of the father is without taking into accounts Tv

  D[v] = max where v has no father to connect to
  
  C[v] = max where v has a degree 0 father
  
  B[b] = max where v has a type B father

  A[v] = max where v has a type A father, 
         (or a B father, but v can only be a leaf of its father)

  let CD0 be the maximum of c[u]-d[u] among all sons u of v
  let BA0 be the same for b[u]-a[u]
  let BA1 be the second maximum value of this difference

  then

  D[v] = 0 of v has no son, otherwise
       = max{ dsum,     -- do not connect to sons
              dsum+CD0, -- become leaf of a single son
              asum,     -- become a star
              asum+BA0, -- let one son to become B
              asum+BA1} -- let two sons become B

  C[v] = max{ D[v],       -- don't connect to father, otherwise...
              1+asum,     -- become star
              1+asum+BA0, -- become B
              1+asum+BA0+BA1 }  -- become A with two B sons

  B[v] = max{ D[v],       -- don't connect to father, otherwise...
              1+asum,     -- become B (father becomes A)
              1+asum+BA0 } -- become A with one B son

  A[v] = max{ D[v],       -- don't connect to father
              1+dsum }    -- become leaf of its father

  Complexity is O(N log N) but could be made linear.
*/

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int MAX=200;

int    n; // number of vertices

map<string,int> name;

// internally vertices have indices
int name2idx(string s) {
  if (name.find(s) == name.end()) {
    int i = name.size();  // assign new number
    name[s] = i;
  }
  return name[s];
}

int d[MAX];        // degrees
int E[MAX][MAX];   // neighbors : N[u][i] = i-th neighbor of u
int p[MAX];        // parent node in tree, -1 for root, -2 not yet visited
const int ROOT=-1, NOT_YET_VISITED = -2;
int A[MAX], B[MAX], C[MAX], D[MAX];

#define forallNeighbors(v,u) for(int u,i##u=0; (u=E[v][i##u], i##u<d[v]); i##u++)
#define forallSons(v,u)      forallNeighbors(v,u) if (p[u]==v)
#define forallVertices(v)    for(int v=0; v<n; v++)

void DFS(int f, int v) {
  p[v] = f;
  forallNeighbors(v,u) 
    if (p[u] == NOT_YET_VISITED)
      DFS(v,u);
  //                              c
  int asum = 0, dsum = 0;
  int k    = 0;  // number of sons
  vector<int> BA, CD;

  forallSons(v,u) {
    asum += A[u];
    dsum += D[u];
    k++;
    BA.push_back(B[u] - A[u]);
    CD.push_back(C[u] - D[u]);
  }
  sort(   BA.begin(), BA.end());
  reverse(BA.begin(), BA.end());
  sort(   CD.begin(), CD.end());
  reverse(CD.begin(), CD.end());

  int BA0 = k>0 && BA[0]>0 ? BA[0] : 0;
  int BA1 = k>1 && BA[1]>0 ? BA[1] : 0;
  int CD0 = k>0 && CD[0]>0 ? CD[0] : 0;
  
  //                              d
  if (k==0)
    D[v] = 0;
  else 
    D[v] = max( dsum+CD0, asum+BA0+BA1 );
  //                              c
  C[v] = max(D[v], 1+asum+BA0+BA1 );
  //                              b
  B[v] = max(D[v], 1+asum+BA0 );
  //                              a
  A[v] = max(D[v], 1+dsum );
}

int DFS() {
  int total=0;
  forallVertices(v)
    p[v] = NOT_YET_VISITED;   // use parent label to mark non-visited
  forallVertices(v)
    if (p[v]==NOT_YET_VISITED) {
      DFS(ROOT, v);
      total += D[v];
    }
  return total;
}

int main() {
  for (int testCase=1; true; testCase++) {
    cin >> n;
    if (n<=0) break;
    if (n>MAX) for (;;) {}
    name.clear();
    //                            read vertices
    forallVertices(v) {
      string vertex;
      cin >> vertex;
      d[name2idx(vertex)] = 0;
    }
    //                            read edges
    int m;
    cin >> m;
    string nameU, nameV;
    while (m-->0) {
      cin >> nameU >> nameV;
      int u = name2idx(nameU);
      int v = name2idx(nameV);
      E[u][d[u]++] = v;
      E[v][d[v]++] = u;
    }
    cout << "Case " << testCase << ": " << DFS() << endl;
  }
  return 0;
}

~~~

