---
layout: en
title:  "Edges expiring"
category: union-find
problems:
   "codility:psi2012": https://codility.com/programmers/challenges/psi2012/
excerpt_separator: <!--more-->
---

Given a graph with expiring dates for every edge, when will the graph be disconnected?

![]({{ site.images }}edges-expiring.svg){:width="400"}

**Update Sep 28, 2024.** This can also be solved as a binary search for the answer.

<!--more-->

### Key observation

The trick is to inverse the time and to add edges to an initial empty graph, in the reverse order they are expiring.  Once the current graph is connected you know that the answer is the time of the last added edge.  Use union-find to maintain connected components.  Hence the problem can be solved in quasi linear time.

### union-find

Union-Find is a data structure which maintains a partition.  Every set in the partition corresponds to a connected component.  Initially every vertex is a component by itself.  *Find(v)* returns a representative of the component containing v.  The components are organized as a tree, with the representative as root.  The table f contains for every vertex v the father f[v] in that tree. We have f[v]=v iff v is the root of a tree.
Union merges two components by attaching one tree below another.  The function *Find(v)* walks all the way from vertex v to the root, and attaches the vertices along the path directly below the root. This flattens the tree.

![]({{site.images}}union-find1.svg "Union-find structure representing the partition {7,8,12}, {2,3,4,5,6}, {1,9,10,10}.
After merging the component containing 3 with the one containing 10, the arc 1->5 is added." ){:width="300"}

![]({{site.images}}union-find2.svg "After the query Find(11) the vertices along the path from 11 to the root 5 are directly attached to the root." ){:width="400"}

The following code is simple and could be good enough in practice if you are lucky.

{% highlight c++ %}
// from Hao Fu
void MakeSet(int f[],int a) {
    f[a]=a;
}
int Find(int f[],int a) {
    if(f[a]==a) return a;
    return f[a]=Find(f,f[a]);
}
bool Same(int f[],int a,int b) {
    return Find(f,a)==Find(f,b);
}
void Union(int f[],int a,int b) {
    f[Find(f,a)]=Find(f,b);
}
{% endhighlight %}

But in order to ensure worst case complexity almost constant for the *Find* and *Union* operation, you need to maintain a rank for each component and attach always the tree with smaller rank below the one with largest.

{% highlight python %}
# from tryalgo.kruskal

class UnionFind:
    """Maintains a partition of {1,..,n}
    """
    def __init__(self, n):
        self.up = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """:returns: identifier of part containing x
        :complexity: O(inverse_ackerman(n))
        """
        if self.up[x] == x:
            return x
        else:
            self.up[x] = self.find(self.up[x])
            return self.up[x]

    def union(self, x, y):
        """ merges part that contain x and part containing y
            :returns: false if x,y are already in same part
            :complexity: O(inverse_ackerman(n))
        """
        repr_x = self.find(x)
        repr_y = self.find(y)
        if repr_x == repr_y:       # déjà dans la même composante
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up[repr_y] = repr_x
        else:
            self.up[repr_x] = repr_y
        return True
{% endhighlight %}
