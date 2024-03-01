---
layout: page
title: Geometry
parent: Problems
---

## Exercices

(Bientôt.)

## Astuces

### Tour gauche

Est-ce que aller de `a` à `b` à `c` fait un virage à gauche ?

{% highlight python %}
def left_turn(a, b, c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0
{% endhighlight %}

### Aire d'un polygone

$$ A = \frac12 \sum_{i=0}^{n-1} (x_iy_{i+1} - x_{i+1}y_i) $$

{% highlight python %}
def area(p):
    A = 0
    for i in range(len(p)):
        A += p[i - 1][0] * p[i][1] - p[i][0] * p[i - 1][1]
    return A / 2.
{% endhighlight %}
