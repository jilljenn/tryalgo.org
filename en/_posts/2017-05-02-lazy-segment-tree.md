---
layout: en
title:  "Lazy segment tree"
category: data structures
author: Christoph Dürr
---

Maintain a numerical table `tab` that implements the following operations in logarithmic time: for a range of table indices, query the maximum value, query the minimum value, query the sum, set all entries of that range to some value, add some value to all entries of that range.

## Segment tree

The data structure is an enhanced version of the segment tree, which is explained [here]({% post_url en/2016-06-25-segment-tree %}).

Suppose that we have a segment tree for a table `tab` of size 8 containing initially only zeros.  Notice the usage of the half open interval, which might make some notations easier.
Suppose that we want to set `tab[i]` to the value 7 for all i in the range [2,8). In a classical segment tree we would update all the leafs correspond to the entries `tab[2]` to `tab[7]`, here depicted in yellow.

![]({{ site.images }}LazySegmentTree0.svg "A segment tree encoding the table [0,0,7,7,7,7,7,7]."){:width="800"}


The idea is to make lazy updates of the table `tab` by storing in some nodes the instruction that the table value over the corresponding index range is to be set to 7.  This will permit to reduce the time complexity of an update from linear to logarithmic time.  To this purpose we attach with each node of the segment tree a value called `lazyset` which, if not `None`, represents this update instruction.
The following picture illustrates this example, depicting in yellow the  nodes concerned by the update.
The values `maxval,minval,sumval` of a node k represent the result of querying the maximum, the minimum or the sum over the entries in the table corresponding to the index range of k.

![]({{ site.images }}LazySegmentTree1.svg "A lazy segment tree encoding the table [0,0,7,7,7,7,7,7]. A dash (-) represents the None value for lazyset."){:width="800"}

Now we have to implement a clearing procedure `clear` which propagates this instruction to the immediate descendants.  The query methods `max,min` and `sum` called on some node have to clear that node first.
For example when querying the minimum over the range [4,6), we have to clear all the nodes from the root of the tree up the node corresponding to the range [4,6), which is depicted in blue.

![]({{ site.images }}LazySegmentTree2.svg "The effect of clearing the nodes during a request on the range [4,6)."){:width="800"}

Similarly we can augment nodes with the instruction of *adding* a given value to the table over the corresponding index range.  We call this value `lazyadd`.

The update methods `set` and `add` as well as the query methods `max,min` or `sum` have logarithmic time complexity in the table size. The proof is similar as for the standard segment tree.

## Links

* [Sample code](http://pythonhosted.org/tryalgo/_modules/tryalgo/range_minimum_query.html#LazySegmentTree)
