---
layout: page
title: 128 algorithms in Python
lang: en
---

We made a Python package [available on PyPI](https://pypi.python.org/pypi/tryalgo/) :

    pip install tryalgo

Several options:

- [Browse the algorithms on GitHub](https://github.com/jilljenn/tryalgo)
- [Browse the docs](http://pythonhosted.org/tryalgo/)
- [Download all files in a ZIP](https://github.com/jilljenn/tryalgo/archive/master.zip)

<iframe src="https://ghbtns.com/github-btn.html?user=jilljenn&amp;repo=tryalgo&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

## An example: coin change

{% highlight python %}
from tryalgo.subsetsum import coin_change

print(coin_change([3, 5, 11], 29))
# Returns True because 29 = 6*3 + 0*5 + 1*11
{% endhighlight %}

<a href="http://pythonhosted.org/tryalgo/_modules/tryalgo/subsetsum.html#coin_change" target="_blank">See the source code (6 lines)</a>

## Demo: our Dijkstra's algorithm on the graph of Paris

See our [Jupyter notebook](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb) (in French): [**TryAlgo Maps in Paris**](http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank"><img src="/static/paris.png" /></a>
