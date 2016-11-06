---
layout: post
title:  "Partition refinement"
category: data structures
---

Given a partition of {0,1,...,n-1} into disjoint sets $$C_1,\ldots,C_k$$ and a set $$S$$ modify the partition such that each set splits according to membership in S, i.e. produce the partition $$C_1\cap S, C_1\setminus S, \ldots, C_k\cap S, C_k\setminus S$$.  Find a data-structure representing partitions that allow this operation in time $$O(|S|)$$ while preprocessing and space is $$O(n)$$.
  See [partition refinement](https://en.wikipedia.org/wiki/Partition_refinement).


![]({{ site.images }}partition-refinement-definition.svg "A partition of the integers 0,..,7 with some refinements.  Colors are only for illustration.")

## The general approach

Oh well, this post is about a data structure, which not among the simplest.
What we want is to represent a partition as list of lists, every list representing a class of the partition.

When we refine $$C_1,\ldots,C_k$$ by a set $$S$$ (called *pivot set*), we need be careful to do it in time linear in the size of $$S$$.  We cannot loop over all sets $$C_j$$ of the partition and replace them by $$C_j\cap S$$ and $$C_j\setminus S$$.

Instead we need to loop over elements of S.  For each element $$i\in S$$ we need to find the class C which contains i.  Now we want to remove the item i from C, such that eventually it would become $$C\setminus S$$ and insert it into a class that would eventually become $$C\cap S$$. We call this class the *split class* of C.

So for every class C we need to to know if we created already such a split class, and if not, we need to create one when needed.

Hence we need a data structure that would keep track of

- a storage for all classes.  We need to be able to loop over all classes.
- a structure for a class, that allows to loop over all elements and possibly link to a corresponding split class
- a structure for an element, that basically stores its value, and a link to its class

An implementation of *refine* would have the following structure.

- for every item i in the pivot set S
  - let C be the class of i
  - if there not yet a split class for C, then create one
  - remove i from C and insert it into the split class of C
- for all classes C that have split
  - remove the information that C has a corresponding split class

The last step ensures that during the next call to *refine*, the reminder of the class C, which is now $$C\setminus S$$ can again split into a new class.

![]({{ site.images }}partition-refinement-implementation.svg "An implementation of a data structure representing a partition.  The links of the double linked list are shown simplified as gray lines.")


## Double linked lists

The solution we propose allows to maintain an ordering on elements.  This is called an *ordered* permutation refinement data structure.  Elements of a class are ordered, and classes are ordered as well.  When a class C splits into $$C\cap S$$ and $$C\setminus S$$, then C gets replaced by these two classes in that order.

For this purpose we will store classes and items in circular double linked lists.

{% highlight python %}
class DoubleLinkedListItem:
    """Item of a circular double linked list
    """

    def __init__(self, anchor=None):
        """Create a new item to be inserted before item anchor.
           if anchor is None: create a single item circular double linked list
        """
        if anchor:
            self.insert(anchor)
        else:
            self.prec = self
            self.succ = self

    def remove(self):
        self.prec.succ = self.succ
        self.succ.prec = self.prec

    def insert(self, anchor):
        """insert list item before anchor
        """
        self.prec = anchor.prec        # point to the neighbors
        self.succ = anchor
        self.succ.prec = self          # make neighbors point to item
        self.prec.succ = self

    def __iter__(self):
        """iterate trough circular list.
        warning: might end stuck in an infinite loop if chaining is not valid
        """
        curr = self
        yield self
        while curr.succ != self:
            curr = curr.succ
            yield curr
{% endhighlight %}

With this data structure in mind we can define class and item objects, which are list items augmented with some attributes.
An class has a pointer to the head of its item list, and a possible pointer to the corresponding split class.  An item has a pointer to its class, and stores its value.

{% highlight python %}
class PartitionClass(DoubleLinkedListItem):
    """A partition is a list of classes
    """

    def __init__(self, anchor=None):
        DoubleLinkedListItem.__init__(self, anchor)
        self.items = None         # empty list
        self.split = None         # reference to split class

    def append(self, item):
        """add item to the end of the item list
        """
        if not self.items:        # was list empty ?
            self.items = item     # then this is the new head
        item.insert(self.items)


class PartitionItem(DoubleLinkedListItem):
    """A class is a list of items
    """

    def __init__(self, val, theclass):
        DoubleLinkedListItem.__init__(self)
        self.val = val
        self.theclass = theclass
        theclass.append(self)

    def remove(self):
        """remove item from its class
        """
        DoubleLinkedListItem.remove(self)     # remove from double linked list
        if self.succ is self:                 # list was a singleton
            self.theclass.items = None        # class is empty
        elif self.theclass.items is self:     # oups we removed the head
            self.theclass.items = self.succ   # head is now successor
{% endhighlight %}


## The data structure

{% highlight python %}
class PartitionRefinement:
    """This data structure implements an order preserving partition with refinements.
    """

    def __init__(self, n):
        """Start with the partition consisting of the unique class {0,1,..,n-1}
        complexity: O(n) both in time and space
        """
        c = PartitionClass()                  # initially there is a single class of size n
        self.classes = c                      # reference to first class in class list
        self.items = [PartitionItem(i, c) for i in range(n)]   # value ordered list of items

    def refine(self, pivot):
        """Split every class C in the partition into C intersection pivot and C setminus pivot
        complexity: linear in size of pivot
        """
        has_split = []                        # remember which classes split
        for i in pivot:
            if 0 <= i < len(self.items):      # ignore if outside of domain
                x = self.items[i]
                c = x.theclass                # c = class of x
                if not c.split:               # possibly create new split class
                    c.split = PartitionClass(c)
                    if self.classes is c:
                        self.classes = c.split   # always make self.classes point to the first class
                    has_split.append(c)
                x.remove()                    # remove from its class
                x.theclass = c.split
                c.split.append(x)             # append to the split class
        for c in has_split:                   # clean information about split classes
            c.split = None
            if not c.items:                   # delete class if it became empty
                c.remove()
                del c


    def tolist(self):
        """produce a list representation of the partition
        """
        return [[x.val for x in theclass.items] for theclass in self.classes]

    def order(self):
        """Produce a flatten list of the partition, ordered by classes
        """
        return [x.val for theclass in self.classes for x in theclass.items]
{% endhighlight %}

## Links

- An [implementation](https://www.ics.uci.edu/~eppstein/PADS/PartitionRefinement.py) by David Eppstein. It is much more readable, uses dictionaries and does not preserve an ordering on elements and classes.
