---
layout: en
title:  "Representing graphs in Python"
category: graphs
author: Christoph Dürr
---

How to represent a graph in Python ?

## Dedicated class

Some libraries use a class to represent graphs. For example the very complete Python library [NetworkX](https://networkx.github.io/documentation/networkx-1.10/overview.html) provides a class for direction graphs (*DiGraph*) and for undirected graphs (*Graph*). Each class has methods to add nodes (*add_node*), and edges (respectively arcs) (*add_edge*), as well as a method to iterate over all neighbors of a vertex (*neighbor*), for a directed graph to iterate over the endpoints of incoming or outgoing arcs (*predecessors* and *successors*).

The [iGraph](http://igraph.org/python/) library also provides a class to represent graphs and is particular useful to visualize them and to read and write graphs to files in various formats.

## Dictionary

The [Python Algorithms and Datastructures](https://www.ics.uci.edu/~eppstein/PADS/) library by David Epstein made the choice of using simply a dictionary to represent graphs.  The keys are nodes, and could be for example strings, and the values are adjacency lists.
Consider the following example graph.

![]({{site.images}}graph__model_names.svg "Example graph" ){:width="300"}

A dictionary adjacency list representation of this graph would like follows.

```python
G = { "Alice":  ["Bob", "Claire", "Frank"],
      "Bob":    ["Alice"],
      "Claire": ["Alice", "Dennis", "Esther", "Frank"],
      "Dennis": ["Claire", "Esther", "George"],
      "Esther": ["Claire", "Dennis"],
      "Frank":  ["Alice", "Claire", "George"],
      "George": ["Dennis", "Frank"]
    }
```

This graph representation leads to quite elegant code. Looping over all nodes in the graph is done by `for v in G`  and looping over all neighbors simply by `for u in G[v]`.  Edge weights need to be stored in a separate structure such that `weight[v][u]` is the weight of the edge (v,u). Such a structure would simply be a dictionary of dictionaries.

## Lists

However in the *tryalgo* library we choose to work with vertex integer identifiers. On of the reason is efficiency and the other one is that the resulting code could be easier translated into C++.
 So the vertices of a graph of `n` nodes will be numbered from 0 to `n-1`.  With such a numbering the graph above could have the following identifiers.

![]({{site.images}}graph__model_id.svg "Example graph with integer identifiers" ){:width="200"}

The advantage of this representation is that we can use a list instead of a dictionary and gain some access time. Even if accesses to a dictionary are in linear time in the worst case (which almost never happens), the practical access time is constant. But this constant is bigger than the access to an element of a Python list. Vertex labels have to be stored in a separate table, associating the vertex identifier to its label.

The above graph would be represented in Python as follows.

```python
G = [[1, 2, 5],     # neighbors of 0
     [0],           # neighbors of 1
     [0, 3, 4, 5],  # neighbors of 2
     [2, 4, 6],     # neighbors of 3
     [2, 3],        # neighbors of 4
     [0, 2, 6],     # neighbors of 5
     [3, 5]]        # neighbors of 6
```

Again, edge weights are stored in a separate data structure, with the same syntax as for the dictionary, such that `weight[u][v]` is the weight of the edge (u,v).  This time the edge weights can be represented as lists of lists, as you reprensent a 2-dimensional array in Python. If the graph is sparse one could as well use a lists of dictionary to store edge weights.

## Mapping vertex names to identifiers

However in many applications we would like to name vertices by strings or tuples, rather than identifiers. An example is given in the next section.  For this purpose we propose to use a class `Graph` that permits to maintaining the mapping between vertex names and vertex identifiers.

The method `add_node(name)` adds a new vertex to the graph with a given name, and returns the corresponding identifier.  It is assumed that the graph does not have another vertex with the same name.

The method `add_edge(name_u, name_v, weight_uv=None)` adds a new edge to the graph, where endpoints are identified by names. For convenience if
The optimal edge weight is then attached to the edge.  Internally an undirected graph is represented as a directed graph, where every edge (u,v) generates the two arcs (u,v) and (v,u).  A similar method `add_arc` permits to add only a single arc.

The graph class has also a method `__len__` which returns the number of vertices and an element operator, which returns the adjacency list for a given vertex identifier. These two methods/operators permit to use the graph class in exactly the same manner as a list-list representation of graphs, as described in the previous section. As a result one can pass an object of the class `Graph` as parameter to all graph algorithms implementations of the *tryalgo* library.

Here is the implementation of the class.

```python
class Graph:
    def __init__(self):
        self.neighbors = []
        self.name2node = {}
        self.node2name = []
        self.weights = []

    def __len__(self):
        return len(self.node2name)

    def __getitem__(self, v):
        return self.neighbors[v]

    def add_node(self, name):
        assert name not in self.name2node
        id = self.name2node[name] = len(self.name2node)
        self.node2name.append(name)
        self.neighbors.append([])
        self.weights.append({})
        return id

    def add_edge(self, name_u, name_v, weight_uv=None):
        self.add_arc(name_u, name_v, weight_uv)
        self.add_arc(name_v, name_u, weight_uv)

    def add_arc(self, name_u, name_v, weight_uv=None):
        if name_u not in self.name2node:
            self.add_vertex(name_u)
        if name_v not in self.name2node:
            self.add_vertex(name_v)
        u = self.name2node[name_u]
        v = self.name2node[name_v]
        self.neighbors[u].append(v)
        self.weights[u][v] = weigh_uv
```

## Example

To illustrated the above graph class, we refer to a problem posted in the [BattleDev March'2018](https://battledev.blogdumoderateur.com/) competition.  You are given a n by n grid representing a maze. A cell can either be empty, contain a door, a wall or a person or a duck. Ducks and persons can walk in this maze, by small steps. A step leads to to a vertically or horizontally neighboring cell, provided it does not contain a wall or a locked door.  The goal is to find out if it possible to lock some doors so that no person can get in touch with a duck.  And if it is possible we want to know the minimal number of doors we need to lock.

Clearly this is a min s-t-cut problem, it is a just a matter of finding the right graph. For this purpose we have 2 vertices for every grid cell (i,j), namely a vertex (IN,i,j) and a vertex (OUT,i,j). If (i',j') is adjacent to (i,j), then there is an arc from (OUT,i,j) to (IN,i',j') of infinite capacity.  In addition there is an arc from (IN,i,j) to (OUT,i,j) with capacity 0 if the cell is a wall, capacity 1 if the cell is a door and capacity infinite otherwise.

In this graph there are two more vertices, a source s that is connected to every vertex (IN,i,j) for cells containing a person, and a target vertex t that is connected from every vertex (OUT,i,j) for cells containing a duck. If the maximum s-t-flow in this graph has infinite value then the persons cannot be separated from the ducks.  Otherwise the value of the flow is the answer.  The infinite capacity can be represented by  the number of cells in the grid.


![]({{site.images}}battledev2018_flow.svg "reduction to a maximum s-t-flow problem" ){:width="600"}

In the graph on the right, the arcs of capacity 0 are not depicted, the black arcs have infinite capacity, and the red arc has unit capacity.

