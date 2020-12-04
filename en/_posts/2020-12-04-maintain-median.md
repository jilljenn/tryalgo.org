---
layout: en
category: data structures
title: "maintaining the median of a dynamic set"
author: Christoph Dürr
problems:
   "spoj:RMID": https://www.spoj.com/problems/RMID/
---

Propose a data structure which permits to maintain a set of integers S, allowing to add elements and to remove the median. Both operations should work in logarithmic time

# Two priority queues

In case of an even cardinality the median is defined as the smaller median of the two candidates. The idea is to maintain two priority queues. One containing the values below the median and including it. The other one containing all larger elements.

    [___lower___:m]  [____higher____]       m = median

The invariant is that the size of the lower queue is between the size of the higher queue and the size of the higher queue plus one.
So whenever the queue sizes change, after an insertion or retrieval of the median, balancing operations might be necessary. One such operation consists in removing the smallest element from the higher queue and to add it to the lower queue.

# Implementation issue

Since we need a max-priority queue and a min-priority queue, we could either use specialized queues with a customed comparator given at the construction. Or -- and I prefer the simplicity of this solution -- to store in the lower queue all the values multplied by -1. We need to take care of the sign change when inserting or removing though.

This code is not accepted by the judge, the limit is too harsh for Python.

This is how you remove the median.
{% highlight python %}
    median =  -heappop(lower)
{% endhighlight %}

This is how you insert a number. Observe how we compare it with the median to decide which is the receiving queue.
{% highlight python %}
    if not lower or n <= -lower[0]:
        heappush(lower, -n)
    else:
        heappush(higher, n)
{% endhighlight %}

And this is how you balance the queues.
{% highlight python %}
    # re-balance heaps
    if len(lower) == len(higher) + 2:
        heappush(higher, -heappop(lower))
    elif len(lower) == len(higher) - 1:
        heappush(lower, -heappop(higher))
    n = readint()
{% endhighlight %}
