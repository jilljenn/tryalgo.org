---
layout: en
title:  "Dynamic binary equation system"
category: union-find
author: Christoph Dürr
problems:
   "spoj:Strange Food Chain": http://www.spoj.com/problems/CHAIN/en/
---

You have to maintain a consistent system of equations of the form $$x_i - x_j = d$$.  Write an operation *add(i,j,d)* that decides if the equation $$x_i - x_j = d$$ is consistent with the system and if yes adds it to the system.  Complexity should be almost constant time per request.

## Augmented union-find

A solution to this general problem consists in maintaining sets of variables that are connected by equations in the system.
This is done with a classical union-find structure, where every component is organized in form of a tree. The root is the leader of the component.  A precedence table *prec* indicates for every variable $$x_i$$ the predecessor variable $$x_j$$ in the tree with *j=prec[i]*.  For the leader  $$x_i$$ of a component we have *prec[i]=i*.

We augment this structure by assigning to every variable $$x_i$$ a potential *pot[i]* with the idea that if $$j=prec[i]$$ then $$x_i-x_j=pot[i]$$.  By definition leaders of a component have zero potential.  The potential between a variable and the leader of its component is by definition the sum of the potentials along the path from the variable to its leader.  We have to update the potential accordingly when flattening the paths during a call to the *find* request.

![]({{ site.images }}chain-find.svg "After a find request, the potential of a variable (vertex) equals the difference with the root."){:width="400"}


Now on the operation *add(i,j,d)* we have to first verify if the variables $$x_i$$ and $$x_j$$ belong to the same component.  In this case we can compare their potential and verify whether it satisfies the equality $$x_i - x_j = d$$, in other words verify whether the request is consistent.  In case the variables belong to different components, these components have to be merged by making the leader of one component, say $$x_k$$, a descent of the leader of the other component.  There is a unique way to assign potential *pot[k]* that would be consistent with the given request.

![]({{ site.images }}chain-union.svg "The union-find structure after serving a request of the form y-x=d."){:width="200"}


The following code implements this data-structure.  To obtain the right complexity, a correct implementation should maintain a rank for each component and merge only the smaller rank component into the large rank component.  However in practice this implementation is good enough, even though in the worst case each request could cost O(log n) time.

{% highlight java %}
class UnionFindPotential {

    static int[] prec, pot;  // prec[u] = father of u, prec[root]=root


    static void UnionFindPotential(int n) {
        prec = new int[n];
        pot = new int[n];
        for (int v=0; v < n; v++)   // every vertex forms a singleton component
            prec[v] = v;
    }


    static int find(int v) {
        if (prec[v] == v)           // v is the root of its component
            return v;
        int rv = find(prec[v]);     // rv is the root
        pot[v] = pot[prec[v]] + pot[v];
        prec[v] = rv;
        return rv;
    }


    static void union(int x, int y, int diff) {  // make y - x =d
        int rx = find(x);
        int ry = find(y);
        pot[ry] = diff + pot[x] - pot[y];
        prec[ry] = rx;
    }
}
{% endhighlight %}


## For the special case of integers modulo 3

Some student had this nice idea. We store in a component all variables for which we know that they have the same value.  In addition we have two pointers for the leader of a component, called *before* and *after*.  If r is the leader of a component C and  r' the leader of a component C' and if we know that the variables in C' have value 1 plus the value of the variables in C, then we set *after[r]=r'* and *before[r']=r*.   Now it is clear how to handle the requests of the form x=y or y-x=1.  This might be easier to implement than the solution above, because it allows to use union-find as a blackbox data structure without modification.
