---
layout: en
title:  "Shortest path in a grid"
category: shortest-paths
author: Christoph Dürr and Jin Shendan
problems:
  "spoj:Laser Phones": http://www.spoj.com/problems/MLASERP/en/
  "spoj:Wandering Queen": http://www.spoj.com/problems/QUEEN/
---

Given a grid with a source cell, a destination cell and obstacle cells, find the shortest path from the source to destination, where every direction change along the path costs 1.

Say the grid has dimensions n times n.

## A simple BFS traversal in time $$O(n^3)$$

Consider a graph, where every vertex is a cell of the grid, and there is an edge between two cells of the same column or the same row if they are not separated by an obstacle.  Now the problem consists in finding a shortest path in this unweighted graph, and this can be done using a BFS traversal of the graph.  There are $$O(n^2)$$ vertices and $$O(n)$$ edges, which leads to the claimed complexity.


## A better analysis shows time is $$O(n^2)$$ in fact

When you visit a cell u at distance dist[u] from the source, then you will explore all neighbors: For each of the 8 directions you will explore the cells in that direction at increasing distance from u, and stop once you reached a cell v that is either on the boundary of the grid, or has already been visited.  But you can also stop if dist[v] equals dist[u].  Because this means that when later you visit vertex v, anyway you will explore the vertices which are beyond v in the u-v direction.

As a result you will look at a cell v at most 8 times, once for each direction. Hence the algorithm runs in linear time.

{% highlight C++ %}
#include <cstdio>
#include <utility>
#include <deque>
#include <cstring>

/* Wandering Queen
http://www.spoj.com/problems/QUEEN/

BFS
but be careful in implementation

tricks (don't know if all are necessary)
- store only cells in queue not (cell,direction)
- flatten the grid in a 1 dimensional matrix, so queue can store single integers not pairs
- add border around grid so we can avoid checking boundaries
*/

using namespace std;

#define MAXN 1002

char grid[MAXN * MAXN];                      // too big to be placed on heap
int dist[MAXN * MAXN];


int main() {
  int testcases;
  scanf("%d", &testcases);
  while (testcases-->0) {
    int nr, nc;
    scanf("%d%d", &nr, &nc);                 // read input
    char *p = grid;
    for (int c=0; c < nc + 2; c++)           // add top border
      *p++ = 'X';
    for (int r = 0; r < nr; r++) {
      *p++ = 'X';                            // add left border
      scanf("%s", p);
      p += strlen(p);
      *p++ = 'X';                            // add right border
    }
    for (int c=0; c < nc + 2; c++)           // add bottom border
      *p++ = 'X';
    *p = '\0';                               // mark end of string
    nc += 2;                                 // count for the additional border
    nr += 2;

    int source = strstr(grid, "S") - grid;   // find source

    const int infinity = MAXN * MAXN;        // big enough number
    fill(dist, dist + MAXN * MAXN, infinity);

    //                                       -- direction offsets
    //             E      NE     N      NW    W   SW     S     SE
    int diff[8] = {-1, -1 - nc, -nc, -nc + 1, 1, 1 + nc, nc, nc - 1};

    deque<int> gray;                         // FIFO queue

    dist[source] = 0;                        // start with single source in queue
    gray.push_front(source);

    int answer = -1;                         // default answer if F unreachable from S

    while ( ! gray.empty()) {                // BFS
      int u = gray.front();
      gray.pop_front();

      if (grid[u] == 'F') {                  // target found
        answer = dist[u];
        break;
      }

      for (int a=0; a < 8; a++) {            // look all 8 neighbors
        int v = u;
        while (true) {                       // walk in one direction
          v += diff[a];
          if (grid[v] == 'X' || dist[v] <= dist[u])   // until obstacle reached or already visited
            break;
          if (dist[v] == infinity) {         // new vertex ?
            dist[v] = dist[u] + 1;
            gray.push_back(v);
          }
        }
      }
    }
    printf("%d\n", answer);
  }
  return 0;
}
{% endhighlight %}


## Improvement through Algorithm A* ?

The algorithm A* is an improvement of the standard Dijkstra shortest path algorithm. All we need is a lower bound on the shortest path to the destination.  We model the problem as follows.  The queen always stands in some grid cell facing  some direction.  She can either walk for free one step in her direction or at the cost of 1 unit walk one step in another direction.
Suppose that the queen stands in position (0,0) and the destination cell is (x,y).  For the lower bound assume that the grid has infinite dimensions and is free of obstacles.  Then the queen could reach the destination in 0, 1, or 2 steps, depending on the directions she is currently facing.  The cost can be determined through a careful case analysis.

{% highlight C++ %}
/* Compares (x,y) to the 8 halflines starting at the origin.
   Returns the minimum number of moves the queen must do in order to reach (x,y)
   if she starts at the origin and walks in direction dir.
*/
int heuristic(int x, int y, int dir) {
  // order : NW, N, NE, E, SE, S, SW, W
  bool is_on[8] = { x== -y && x < 0,   y > 0 && x==0,  x == y && x > 0,
                    x == 0 && x > 0, x == -y && x > 0, x == 0 && y < 0,
              x == y && x < 0, y == 0 && x < 0};
  bool is_left[8] = {x > -y, x > 0, x > y, y < 0, x < -y, x < 0, x < y, y > 0};
  // test if (x,y) lies on a halfline
  for(size_t i = 0; i < 8; ++i)
  {
    if (is_on[i]) {
      if (dir == i)
        return 0;
      else if (dir == i + 3 || dir == i + 5)
        return 2;
      else
        return 1;
    }
  }
  // test if (x,y) lies between two halflines
  for(size_t i = 0; i < 8; ++i)
  {
    if (is_left[i] && ! is_left[ (i + 1) % 8]) {
      if (dir == i + 4 || dir == i + 5)
        return 2;
      else
        return 1;
    }
  }
  // this part should never be reached
  return 0;
}
{% endhighlight %}

Experiments show that this solution is slower than the BFS described above.


## Links

- See [here](http://zobayer.blogspot.fr/2013/12/spoj-queen.html) for another explanation by Hasan Zobayer.

