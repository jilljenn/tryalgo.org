---
layout: en
title:  "The bridge and torch puzzle"
category: graphs
language: en
---

There are n persons that all have to cross a bridge, using a single torch.  Person i takes \\( t_i \\) minutes to cross the bridge.  At most 2 persons can walk on the bridge at the same time and need to carry the torch with them.  If persons i and j cross together their crossing time is \\( \\max\{ t_i, t_j \} \\).  Minimize the total crossing time. See [Bridge](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=978).


<iframe width="560" height="315" src="https://www.youtube.com/embed/7yDmGnA8Hw0" frameborder="0" allowfullscreen></iframe>


## Solution in time O(n log n)

The solution has been discovered by Günter Rote and described in this [paper](http://page.mi.fu-berlin.de/rote/Papers/pdf/Crossing+the+bridge+at+night.pdf).  The description below is very high level, we recommend that you read Günter's paper first.

The solution starts by showing that any optimal solution consists of alternating forward crossings with 2 persons and backward crossings with a single person.  There are \\( n-1 \\) forward crossings and \\( n-2 \\) backward crossings.

Then there is a is a graph representation of the solutions.  Given a solution consider the graph where each vertex corresponds to a person, and there is an edge (i,j) with cost \\( \\max\\{ t_i, t_j \\} \\) if persons i and j cross together the bridge.  The total edge cost represents the total forward crossing cost.  If a vertex i has degree \\( d_i \\) then there are \\(d_i - 1 \\) backward crossings in the solution.  To simplifiy the reduction we conceptually add the constant cost \\( \\sum_i t_i \\) to the objective value, which preserves optimal solutions.  This allows us to incorporate the backward crossing costs into the edge costs.

The new objective is now simply the total edge weight, where the weight of edge (i,j) is \\( t_i + \\max\\{ t_i, t_j\\} + t_j \\).  Finally there is a cost-preserving bijection between solutions and multi-graphs with \\( n-1  \\) edges covering all vertices (every person needs to cross).

The particular structure of the edge weigths give structure to the optimal solution. Namely all optimal solutions have the following shape.  Assume the ordering \\( t_0 \leq  t_1 \leq \ldots \leq t_{n-1} \\).  The last vertices are matched in sequence starting from some vertex index x, which is the unique parameter of choice of the optimal solution.  The vertices before x are all matched with vertex 0.  And there are enough edges (0, 1) to make the required total edge number of \\( n-1 \\).

![]({{site.images}}bridge-and-torch.svg "Optimal solutions are fully described by graphs of this form.")

Hence the algorithm only needs to determine the parameter x.  This is done by analyzing for every possible value of x, the difference in cost of the edge sets {(0, 1), (x, x+1)} and {(0, x), (0, x+1)}.

The final solution crossing sequence is produced from the graph, (from the parameter x), simply by processing edges (i,j) in decreasing j order.  Every edge generates a sequence of crossings that ends with the invariant that person 0 is again on the left side.  Here the cases i bigger or smaller than x are distinguished.  The last forward crossing consists of persons 0 and 1.


{% highlight python %}
def solve(t):
    n = len(t)
    t.sort()                       # increasing order
    if n == 0:                     # special cases
        return 0, []
    elif n == 1:
        return t[0], [t[0]]
    elif n == 2:
        return t[1], [(t[0], t[1])]
    total = (n - 2) * t[0] + sum(t[1:])
    x = n
    threshold = 2 * t[1] - t[0]    # consider edge exchanges
    while t[x - 2] > threshold:
        total -= t[x - 2] - threshold
        x -= 2
    seq = []                       # will be actual crossing sequence
    i = n - 1                      # start from end
    while i > 1:
        if i >= x:
            seq += [(t[0], t[1]), t[1], (t[i - 1], t[i]), t[0]]
            i -= 2
        else:
            seq += [(t[0], t[i]), t[0]]
            i -= 1
    seq.append((t[0], t[1]))       # final crossing
    return total, seq
{% endhighlight %}
