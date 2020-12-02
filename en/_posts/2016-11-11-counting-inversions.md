---
layout: en
title:  "Counting inversions"
category: permutations
problems:
   "uva:Ping pong": https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4174
---

Given a table, find for every entry how many elements there are to left that are larger and how many elements there are to right that are smaller.  In other words find out how many swaps bubble sort will do on the table.

## A $$O(n\log n)$$ algorithm based on merge sort

Consider one step of the recursive merge sort applied on the table.
In the merge step we are given two consecutive portions of the table which each are already sorted.  A temporary table recieves the result of the merging of the two lists.  We have two pointers i and j that progress in each of the tables and a pointer k in the temporary table.

At any moment we compare the elements pointed by i and j and move the smaller of them to the temporary table. In each of the cases we can identify some inversion pairs as depicted below.

![]({{ site.images }}left-right-inversions.svg "Counting the number of inversions at every merging step."){:width="500"}


In the implementation below, we do not sort the intial given table, but rather a vector *rank* containing indices to the table.
This is necessary since otherwise the items would at some stage of the algorithm not be at their initial position anymore, making it impossible to increase the correct entries in the tables  *left* and *right*

{% highlight python %}
def _merge_sort(tab, tmp, rank, left, right, lo, hi):
    if hi <= lo + 1:             # interval is empty or singleton
        return                   # nothing to do
    mid = lo + (hi - lo) // 2    # divide interval into [lo:mid] and [mid:hi]
    _merge_sort(tab, tmp, rank, left, right, lo, mid)
    _merge_sort(tab, tmp, rank, left, right, mid, hi)
    i = lo                       # merge the two lists
    j = mid
    k = lo
    while k < hi:
        if i < mid and (j == hi or tab[rank[i]] <= tab[rank[j]]):
            tmp[k] = rank[i]
            right[rank[i]] += j - mid
            i += 1
        else:
            tmp[k] = rank[j]
            left[rank[j]] += mid - i
            j += 1
        k += 1
    for k in range(lo, hi):      # copy sorted segment into original table
        rank[k] = tmp[k]


def left_right_inversions(tab):
    """ Compute left and right inversions of each element of a table.

    :param tab: list with comparable elements
    :returns: lists left and right. left[j] = the number of i<j such that tab[i] > tab[j].
    right[i] = the number of i<j such that tab[i] > tab[j].
    :complexity: `O(n \log n)`
    """
    n = len(tab)
    left = [0] * n
    right = [0] * n
    tmp = [None] * n      # temporary table
    rank = list(range(n))
    _merge_sort(tab, tmp, rank, left, right, 0, n)
    return left, right
{% endhighlight %}

