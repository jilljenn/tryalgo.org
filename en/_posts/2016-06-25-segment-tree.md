---
layout: en
title:  "Segment tree"
category: data structures
---

Maintain a numerical table that implements the following operations in logarithmic time: query the entry at some index, add a value to all entries between two given indices.

## Binary tree

Without loss of generality suppose that the table has a size n in the form of a power of 2.
The idea is to work with a binary tree with n leafs, each corresponding to an entry in the table.  Every node *p* in the tree has a value label *p.val*, including the leafs.  The relation between the tree and the table is as follows. The total value along the path from the root to a leaf equals the corresponding table entry.  In that sense the tree encodes the table. The data structure consists only of the tree, not of the table.

![]({{ site.images }}segment_tree_mapping.svg "A segment tree encoding the table below. Every cell is a node, and the two rectangles below the left and right descendants."){:width="500"}

As we have seen querying the entry at some index can be done in logarithmic time (which is the depth of the tree).  Now we explain how to perform table updates.  To each node *p* we associate the interval formed by all the table indices corresponding to the leafs of the subtree. We call this interval *p.span*.  For a leaf *p*, the interval *p.span* consists only of the corresponding table index. For an inner node *p* with descendants *p.left* and *p.right*, the interval *p.span* is the (disjoint) union of *p.left.span* and *p.right.span*.

Updates are done by descending recursively the tree, as follows.  Note that the span is not stored with the nodes but implicitly given as a parameter with each call.

{% highlight python %}
def update(node p, p_span,  update_span, delta_val):  # pseudo code
    """
    add delta_val to the table at all indices in
    the intersection of p_span and update_span
    """
    if update_span and p_span are disjoint:
        return  # nothing to do
    if p_span is included in update_span:
        p.val += delta_val   # update only this node
        return
    split p_span into p_span_L and p_span_R
    update(p.left,  p_span_L, update_span, delta_val)
    update(p.right, p_span_R, update_span, delta_val)
{% endhighlight %}

To convince yourself that the update procedure, when initiated at the root, terminates in logarithmic time, simply observe that for each level k there will be at most two calls to *update* with p_span of size \\( 2^k \\).

![]({{ site.images }}segment_tree_update.svg "Adding a value Δ to all table entries in an index interval is done by adding it to some nodes of the tree."){:width="500"}

## Extension

A really nice feature of segment trees is that they allow you to maintain additional information about the table, which can be quickly queried.  Suppose you want to query the sum of the table entries between two indices.  To answer these queries quickly we store in each node *p* a score, which is the sum of the table entries over all indices in *p.span*. Hence

    p.score = p.val + p.left.score + p.right.score

The to answer the query we have to make recursive calls as follows.

{% highlight python %}
def sum_query(node p, p_span,  query_span):  # pseudo code
    """
    return the sum of the table over all indices in
    the intersection of p_span and update_span
    """
    if update_span and p_span are disjoint:
        return 0   # neutral element for the sum
    if p_span is included in update_span:
        return p.score
    split p_span into p_span_L and p_span_R
    return (  sum_query(p.left,  p_span_L, query_span)
            + sum_query(p.right, p_span_R, query_span) )
{% endhighlight %}

## More extensions

Similarly it is possible to adapt segment trees to answer min or max queries.  For this purpose one only need to specify

* a neutral value to be returned on queries over empty intervals. This can be 0 for sum-queries, \\( +\infty \\) for min-queries, or \\( -\infty \\) for max-queries.
* a score-update procedure to be applied on leafs, when their value has changed
* a score-udpate procedure to be applied on inner nodes, when their value has changed
* a combine-query function that computes the answer to a query from the answers obtained from each recursive query on the node successors.


#### For more information

* [An animated visualization](http://visualgo.net/segmenttree)
* [A wiki page](http://wcipeg.com/wiki/Segment_tree)
* [Sample code](https://jilljenn.github.io/tryalgo/_modules/tryalgo/range_minimum_query.html#RangeMinQuery)
