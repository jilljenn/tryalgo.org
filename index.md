---
layout: page
title: Algorithic Problem Solving
nav_exclude: true
---

# TryAlgo: Algorithmic Problem Solving

## Latest posts

<figure style="float: right; margin-left: 10px; text-align: center;">
    <a href="{% post_url en/2016-11-19-swerc-2016 %}"><img src="/fr/images/swerc2016/swerc2016-thumb.jpg" style="float: right" /></a>
    <figcaption><a href="{% post_url en/2016-11-19-swerc-2016 %}">SWERC 2016</a></figcaption>
</figure>

<ul>
{% for post in site.posts limit:5 %}
    <li> {{ post.date | date: "%b %-d, %Y" }} <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.author }}
    </li>
{% endfor %}
</ul>

## [Code](/code/): the tryalgo Python library of 128+ algorithms

<figure style="float: right; margin-left: 10px; text-align: center;">
    <a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank"><img src="/static/paris.png" width="200" /></a>
    <figcaption>Demo: <a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb">shortest paths in Paris</a></figcaption>
</figure>

    pip install tryalgo

- [Read the docs](https://jilljenn.github.io/tryalgo/)

<iframe src="https://ghbtns.com/github-btn.html?user=jilljenn&amp;repo=tryalgo&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

## [Book](/book): *Competitive Programming in Python*

<a href="https://amzn.to/45itxtF"><img src="/static/tryalgo-en.jpg" style="float: right" width="180" /></a>

We published a book on competitive programming in Python. It contains typical algorithms like shortest paths, or Knuth-Morris-Pratt algorithm for pattern matching, but also some beautiful things you mainly encounter in programming competitions such as Fenwick trees.

- [Buy in English](https://amzn.to/45itxtF) (latest version)
- [Acheter en français](https://amzn.to/3SAzuPt)
- Other languages: [Chinese](https://book.douban.com/subject/30210075/), [Taiwanese](https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP11906)
- [Check the errata](/errata)

[![](/static/books.jpg)](https://amzn.to/3SAzuPt)

Here is some pseudocode to optimize your learning:

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
