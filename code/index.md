---
layout: page
title: Code
---

## Tous les codes sont open source : le package <a href="https://github.com/jilljenn/tryalgo" target="_blank">tryalgo</a>

<a class="github-button" href="https://github.com/jilljenn/tryalgo/archive/master.zip" data-icon="octicon-cloud-download" data-style="mega" aria-label="Download jilljenn/tryalgo on GitHub">Télécharger tous les codes</a>

<iframe src="https://ghbtns.com/github-btn.html?user=jilljenn&amp;repo=tryalgo&amp;type=fork&amp;count=true&amp;size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

Ou avec pip : <strong>pip3 install tryalgo</strong>.

## Exemple d'algorithme : rendu de monnaie

{% highlight python %}
from tryalgo.subsetsum import coin_change

print(coin_change([3, 5, 11], 29))
# True car 29 = 6*3 + 0*5 + 1*11
{% endhighlight %}

<a href="http://pythonhosted.org/tryalgo/_modules/tryalgo/subsetsum.html#coin_change" target="_blank">Voir le source (6 lignes)</a>

### Démo avec Jupyter notebook : <a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank">TryAlgo Maps in Paris</a>

<a href="http://nbviewer.jupyter.org/github/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb" target="_blank"><img src="/static/paris.png" /></a>
