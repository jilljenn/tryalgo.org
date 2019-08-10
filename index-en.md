---
layout: page
title: Algorithmic Problem Solving
lang: en
---

## Latest posts

<ul>
{% for post in site.posts limit:5 %}
    <li> {{ post.date | date: "%d/%m" }} <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.author }}
    </li>
{% endfor %}
</ul>

## [pip install tryalgo](/code/)

<a href="{% post_url en/2016-11-19-swerc-2016 %}"><img src="/fr/images/swerc2016/swerc2016-thumb.jpg" style="float: right" /></a>

This website gathers the following resources:

- [128 classic algorithms](/code/) in Python on [GitHub](https://github.com/jilljenn/tryalgo/tree/master/tryalgo) ;
- various [problems](/problems/) and their [solutions](/en/) ;
- [a handbook](/book/), in French, but that will be soon released in English by Cambridge University Press (2020).

Here is a pseudocode in order to optimize your learning:

```python
import tryalgo                 # import all you can eat

try:
    problem = read(statement)    # needs organisation
    algo = solve(problem)        # needs skills
    solution = implement(algo)   # needs experience
    answer = submit(solution)
    assert answer == "Accept"
except SubmissionError:
    learn_more()
```
