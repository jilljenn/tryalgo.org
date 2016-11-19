---
layout: en
title:  "Seminar room"
category: 2-sat
problem_url: "http://acm.tju.edu.cn/toj/showp2506.html"
problem_name: "Seminar Room"
---

You are given n pairs of time intervals. From each pair select exactly one such that the selected time intervals do not intersect.

## Reduction to 2-SAT

This can be solved in linear time by a reduction to 2-SAT.

You have n boolean variables. Every variable $$x_i$$ corresponds to two literals $$x_i$$ and $$\bar x_i$$.  To every literal there is a given interval.  There is a clause $$\bar x \vee \bar y$$ if the intervals corresponding to literals $$x$$ and $$y$$ intersect.  The clauses form a so-called 2-SAT formula.  The goal is to find a boolean assignment that can satisfy all clauses.

2-SAT formulas can be solved in linear time by an algorithm by Tarjan. Consider a directed graph, where every literal is a vertex and every clause $$x\vee y$$ --- which can also write as $$\bar x \Rightarrow y$$ or $$\bar y \Rightarrow x$$ --- corresponds to the arcs $$(\bar x, y), (\bar y, x)$$.  Clearly the literals of a strongly connected component must have all the same true value.  If there is a variable which sits in the same component as its negation then the  formula has no solution.


![]({{site.images}}exemple-2sat.svg "The implication graph corresponding to the formula (¬a ∨ ¬b) ∧ (b ∨ c) ∧ (a ∨ ¬c) ∧ (a ∨ c)." ){:width="200"}

Otherwise a solution can be found as follows.  When you contract the components you obtain a directed acyclic graph (DAG). Hence there must be a component with no incoming arcs, and a corresponding component with no outgoing arcs.  Assign False to all literals in the first component, which will assign True to all literals in the second component.  Remove these components and repeat.  Implementing it in linear time is a bit tricky.  The easiest is to implement Kosaraju's algorithm.



### trick for translating day:hour:min into minutes

{% highlight Java %}
static int minutes(String a) {
    int j = "MON TUE WED THU FRI SAT".indexOf(a.substring(0, 3)) / 4;
    int h = Integer.parseInt(a.substring(4,6));
    int m = Integer.parseInt(a.substring(7));
    return m + 60 * (h + 24 * j);
}
{% endhighlight %}


### links

- solution from the tryalgo library [two_sat](http://pythonhosted.org/tryalgo/_modules/tryalgo/two_sat.html#two_sat) and [strongly connected components](http://pythonhosted.org/tryalgo/tryalgo/tryalgo.html?highlight=strongly#module-tryalgo.strongly_connected_components)

