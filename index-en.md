---
layout: page
title: Algorithmic Problem Solving
lang: en
parent: Algorithms
---
# Algorithmic Problem Solving

This page [in French](/)

<a href="{% post_url en/2016-11-19-swerc-2016 %}"><img src="/fr/images/swerc2016/swerc2016-thumb.jpg" style="float: right" /></a>

## Latest posts

<ul>
{% for post in site.posts limit:8 %}
    <li> {{ post.date | date: "%b %-d, %Y" }} <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.author }}
    </li>
{% endfor %}
</ul>

## Code: the tryalgo library of 128+ algorithms

We collected implementations of various algorithms and data structures in a [PyPI Python library](https://pypi.python.org/pypi/tryalgo/).

    pip install tryalgo

- [Check the docs](https://jilljenn.github.io/tryalgo/)
- [See on GitHub](https://github.com/jilljenn/tryalgo)
- [Download all files in a ZIP](https://github.com/jilljenn/tryalgo/archive/master.zip)

<iframe src="https://ghbtns.com/github-btn.html?user=jilljenn&amp;repo=tryalgo&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

## Book: *Competitive Programming in Python*

<a href="http://www.amazon.fr/gp/product/2340010055/ref=as_li_tl?ie=UTF8&amp;camp=1642&amp;creative=19458&amp;creativeASIN=2340010055&amp;linkCode=as2&amp;tag=mangaki-21"><img src="/static/cover.jpg" style="float: right" width="180" /></a>

We published a book on competitive programming in Python, documenting most of the content of the library `tryalgo`. It appeared in several languages.

- [English](http://www.cambridge.org/9781108716826) --- this latest translation contains some improved presentations over the other versions
- Other languages: [French](https://www.editions-ellipses.fr/accueil/3853-programmation-efficace-128-algorithmes-quil-faut-avoir-compris-et-codes-en-python-au-cours-de-sa-vie-9782340010055.html), [Chinese](https://book.douban.com/subject/30210075/), [Taiwanese](http://www.drmaster.com.tw/Bookinfo.asp?BookID=MP11906)
- [Check the errata](/errata)

## Problems

- [List of problems](problems)
- [List of competitions](competitions)

See our [Jupyter notebook](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb) (in French): [**TryAlgo Maps in Paris**](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank"><img src="/static/paris.png" /></a>

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
