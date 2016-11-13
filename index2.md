---
layout: default
title: Accueil
---

# Programmation efficace

128 algorithmes qu'il faut avoir compris et codés dans sa vie

{% highlight Python %}
import sys
from algorithms import *  # learn as much as as possible

try:
  problem = read(sys.stdin)
  solution = solve(problem)
  answer = submit(solution)
  assert answer == "Accept"
except Submission_error:
  learn_more()
{% endhighlight %}

