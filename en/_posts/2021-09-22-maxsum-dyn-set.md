---
layout: en
category: data structures
title: "Maintaining sum of k largest items in a dynamic set"
author: Christoph Dürr
problems:
   "KICKSTART:Festival": https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
---

Maintain a set, allowing to add or remove elements and to query the sum of the up to k largest items.

# Use two heaps

The idea is to use 2 heaps. We will use a min-heap 'large', where the top
element is its smallest item.  As well as a max-heap 'small', where the top
element is its largest item.

    large:            small:
    [800, 400, 350]   [200, 100]
               ^top    ^top
    <-----k------->

The invariant is that if the set contains less than k items, then it is
entirely stored in 'large', while 'small' is empty. Otherwise 'large' stores
the k largest items of the set, and 'small' all the others.

Maintaining the invariant, simply consists to move items from one heap to
another, if the cardinality of the large set is not k.

# Application

In the above mentioned problem, we are given n weighted intervals, and need to
find a set of up to k intervals, all intersecting, maximizing the total
weight of this set.  This can be solved by a sweep line algorithm.  Just scan
the intervals from left to right, adding or removing weights to a dynamic
set, when the endpoints of the corresponding intervals are processed.  Fairly easy.  Hence overall time complexity is O(n log n).

# Implementation in Python

Here we use our implementation of lazy heaps, explained [here](https://tryalgo.org/en/data%20structures/2021/09/22/lazyheap/).

{% highlight python %}
from sys import stdin
from collections import Counter
from heapq import *

def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().strip().split()))
def readstr(): return stdin.readline().strip()

class dynset:
    """Maintains a multiset and keeps track of the sum of its k largest elements.
    large is the minheap containing the up to k largest elements.
    small is the maxheap containing the smaller elements.
    in fact we use a minheap but invert the values.
    """
    def __init__(self, k):
        self.k = k
        self.large = lazyheap()
        self.small = lazyheap()

    def balance(self):
        """maintains invariant on heap sizes
        """
        if self.large.n > self.k:
            self.small.push(-self.large.pop())
        if self.large.n < self.k and self.small.n > 0:
            self.large.push(-self.small.pop())

    def add(self, value):
        # negate value to make a maxheap
        self.large.push(value)
        self.balance()

    def remove(self, value):
        # from which heap should we remove?
        if value < self.large.top():  
            self.small.remove(-value)
        else:
            self.large.remove(value)
        self.balance()



def solve(k, n, h, s, e):
    D = dynset(k)
    """scan time line by processing an event list.
    +hi means we enter interval i, -hi means we leave it.
    """
    events = [(s[i], +h[i]) for i in range(n)]  
    events += [(e[i] + 1, -h[i]) for i in range(n)]  
    best = 0
    for (time, delta) in sorted(events):
        if delta < 0:
            D.remove(-delta)
        else:
            D.add(delta)
        best = max(best, D.large.sum)
    return best

for test in range(readint()):
    d, n, k = readints()
    h = [0] * n
    s = [0] * n
    e = [0] * n
    for i in range(n):
        h[i], s[i], e[i] = readints()
    print('Case #%d: %s' % (test + 1, solve(k, n, h, s, e)))
{% endhighlight %}

