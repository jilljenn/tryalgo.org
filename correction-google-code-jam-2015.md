---
layout: page
title: Correction du Code Jam 2015
published: false
---

<p class="message"><strong>Attention !</strong> Je fournis un code de réponse, si vous n'avez pas commencé à chercher, je vous invite à tester le A et le D avant de revenir sur cette page.</p>

## A - Standing Ovation

> Dans un public, certaines personnes ne se lèvent pour applaudir que lorsque un certain nombre de personnes se sont déjà levées.<br />
On vous donne pour chaque <em>k</em> le nombre de personnes qui attendent que <em>k</em> personnes se soient levées pour applaudir, vous devez indiquer le nombre minimum de personnes à ajouter pour créer une <em>standing ovation</em>.

Il suffisait de simuler un ajout de personnes de la salle dès qu'il y a un blocage, c'est-à-dire que des gens attendent pour applaudir. Pour cela, on parcourt la liste des nombres de personnes par nombre requis (de personnes pour applaudir) croissant.

### Une solution en Python 2.7

{% highlight python %}
T = int(raw_input())
for t in range(T):
    nb_stand = 0
    r = 0
    smax, number = raw_input().split()
    smax = int(smax)
    for required in range(smax + 1):
        if number[required] == '0':
            continue
        if nb_stand + r < required:
            r += required - (nb_stand + r)
        nb_stand += int(number[required])
    print 'Case #%d: %s' % (t + 1, r)
{% endhighlight %}

## B - Infinite House of Pancakes

### Un code qui ne marche pas en Python 2.7

{% highlight python %}
from heapq import heapify, heappop, heappush

T = int(raw_input())
for t in range(T):
    D = int(raw_input())
    P = map(lambda x: -int(x), raw_input().split())  # Max-heap
    save = P[:]
    heapify(P)
    nb_steps = -min(P)
    record = nb_steps
    for time in range(nb_steps):
        minus_n = heappop(P)
        n = -minus_n
        if time + n < record:
            record = time + n  # Update record
        if n == 1:
            break
        a = n / 2
        b = n - a
        heappush(P, -a)
        heappush(P, -b)
    print 'Case #%d: %s' % (t + 1, record)
{% endhighlight %}

## C - Dijkstra



## D - Ominous Omino
