---
layout: en
title:  "Shortest cycle"
category: cycles
author: Christoph Dürr, Louis Abraham and Finn Völkel and students present at the Nov 5 meeting
---

Find a shortest cycle in a given undirected graph. See [GIRTH](http://www.spoj.com/problems/GIRTH/) or [FTOUR](http://www.spoj.com/problems/FTOUR/).

## Algorithm in time $$O(|V|\cdot |E|)$$ using BFS

The BFS graph traversal can be used for this purpose. [Here](http://stackoverflow.com/questions/20847463/finding-length-of-shortest-cycle-in-undirected-graph) is a discussion why DFS cannot help for this problem.

The key observation is the following. Suppose you start a BFS exploration at some root vertex $$r$$.  The exploration places the vertices into levels according to the distance from the root, where the root is in level 0. The BFS exploration distinguishes between different kind of edges. First there are the *forward edges* which lead to unmarked vertices.  These edges form the BFS tree.  The remaining edges form cycles with the tree, and are called *traversal edges*.  These edges can only connect vertices from the same level or from adjacent levels.

If from a vertex $$u$$ at level $$i$$ we discover a traversal edge to a neighbor $$v$$ at level $$j$$ then we know that there is a cycle consisting of the path from $$r$$ to $$u$$ in the BFS tree, the edge $$(u,v)$$ and the path from $$v$$ to $$r$$ in the BFS tree.  This cycle has length $$i+1+j$$.  Also the cycle is simple if and only if $$r$$ is the lowest common ancestor of $$u$$ and $$v$$ on the BFS tree.  Otherwise we know that there is a simple cycle of length at most $$i+j$$. 

Hence in order to find a shortest cycle simply loop over all possible root vertices $$r$$. Initiate a BFS search at $$r$$, and for every non-forward edge $$u,v$$ you encounter, keep track of the tree vertices $$r,u,v$$ that minimize the sum of the levels of $$u$$ and of $$v$$.  After that you know that for the minimizers $$r,u,v$$, there is a shortest cycle containing these vertices.  Then you just need a last BFS search initiated at $$r$$, or alternatively you can store with the minimizers $$r,u,v$$ the correspondonding BFS tree.  From that tree you obtain the shortest path from $$r$$ to $$u$$ and to $$v$$.   Together with the edge $$(u,v)$$ they form a shortest cycle.  

![]({{site.images}}shortest-cycle.svg "Forward edges are depicted as solid arrows. Neighbors of vertex u: The edge (u,c) will be part of the BFS tree, while edges (u,a) and (u,b) are part of a simple cycle." ){:height="500"}

### Pruning

Once you have discovered a cycle of length k you can prune the tree at the level k/2, meaning that you don't need to explore below that level because you won't discover shorter cycles then.

{% highlight python %}
def bfs(graph, root, prune_level):
    """make a pruned BFS search of the graph starting at root.
    returns the BFS tree, and possibly a traversal edge (u,v) that with the tree
    forms a cycle of some length.
    Complexity: O(V + E)
    """
    n = len(graph)
    level = [-1] * n                      # -1 == not seen
    tree = [None] * n                     # pointers to predecessors
    toVisit = deque([root])               # queue for BFS
    level[root] = 0                       
    tree[root] = root                     
    best_cycle = float('inf')             # start with infinity
    best_u = None
    best_v = None
    while toVisit:
        u = toVisit.popleft()           
        if level[u] >= prune_level:
            break
        for v in graph[u]:
            if tree[u] == v:              # ignore the tree edge
                continue
            if level[v] == -1:            # new vertex - tree edge
                level[v] = level[u] + 1
                toVisit.append(v)
                tree[v] = u
            else:                         # vertex already seen - traversal edge
                has_cycle = True
                prune_level = level[v] - 1
                cycle_len = level[u] + 1 + level[v]
                if cycle_len < best_cycle:  # footnote (1)
                    best_cycle = cycle_len
                    best_u = u
                    best_v = v
    return tree, best_cycle, best_u, best_v
    
    
def path(tree, v):
    """returns the path in the tree from v to the root
    Complexity: O(V)
    """
    P = []
    while not P or P[-1] != v:
        P.append(v)
        v = tree[v]
    return P
    
    
def shortest_cycle(graph):
    """Returns a shortest cycle if there is any
    Complexity: O(V * (V + E))
    """
    best_cycle = float('inf')
    best_u = None
    best_v = None
    best_tree = None
    V = list(range(len(graph)))
    for root in V:
        tree, cycle_len, u, v = bfs(graph, root, best_cycle // 2)
        if cycle_len < best_cycle:
            best_cycle = cycle_len
            best_u = u
            best_v = v
            best_tree = tree
    if best_cycle == float('inf'):
        return None                   # no cycle found
    Pu = path(best_tree, best_u)
    Pv = path(best_tree, best_v)
    return Pu[::-1] + Pv              # combine path to make a cycle
{% endhighlight %}


### Links

- [excellent lecture note](http://webcourse.cs.technion.ac.il/234247/Winter2003-2004/ho/WCFiles/Girth.pdf)
