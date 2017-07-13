---
layout: en
title: "SymPy vs. SageMath: symbolic computation and automatic differentiation in Python"
category: arithmetics
author: Jill-Jênn Vie
---

[What automatic differentiation looks like](https://en.wikipedia.org/wiki/Automatic_differentiation).

[TensorFlow does it](https://stackoverflow.com/a/36373220/827989) for computing gradients automatically.

![SymPy vs. SageMath](/static/sympy-sagemath.png)

[Differences between SymPy and SageMath on sympy's wiki](https://github.com/sympy/sympy/wiki/SymPy-vs.-Sage)

## SymPy

[Try SymPy in your brother](http://docs.sympy.org/latest/tutorial/intro.html#a-more-interesting-example) (live shell on every page, wow!).

    pip install sympy

- [Someone doing approximate matrix differentiation](https://zulko.wordpress.com/2012/04/15/symbolic-matrix-differentiation-with-sympy/)
- [Tests for differentiation with tensors](https://github.com/sympy/sympy/blob/49649c2bd0488840fe1cb47184e35b0fb42c7098/sympy/tensor/tests/test_indexed.py) (GitHub)
- [Derivatives by array](http://docs.sympy.org/latest/modules/tensor/array.html#derivatives-by-array): it can derivate by vector, do a symbolic differentiation.
- [Output towards TensorFlow](http://docs.sympy.org/latest/modules/utilities/lambdify.html#sympy.utilities.lambdify.lambdify)

See [this interesting Jupyter notebook](https://github.com/jilljenn/tryalgo.org/blob/master/_notebooks/SymPy%20Demo.ipynb)!

## SageMath

[Try it on CoCalc](https://cocalc.com) (formerly SageMathCloud).

You can [download this SageMath worksheet (logreg.sagews)](https://github.com/jilljenn/tryalgo.org/tree/master/_notebooks) to load it there.

- Many tools about block design in combinatorics, Galois fields, etc.
- Really used by cryptographers.
- See the [extensive documentation](http://doc.sagemath.org/html/en/reference/index.html)

Also: [Suffix trees and arrays?!](http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/words/suffix_trees.html)

## But…

But unlike Wolfram Alpha, they cannot output a [Pikachu curve](https://www.wolframalpha.com/input/?i=pikachu+curve) :/

<blockquote class="twitter-tweet" data-lang="fr"><p lang="de" dir="ltr">Type pikachu curve in Wolfram Alpha: <a href="https://t.co/axW9M3b9nv">https://t.co/axW9M3b9nv</a> <a href="https://twitter.com/hashtag/Pok%C3%A9mon?src=hash">#Pokémon</a> <a href="https://t.co/BJrG4U5qx4">pic.twitter.com/BJrG4U5qx4</a></p>&mdash; Jill-Jênn Vie (@jjvie) <a href="https://twitter.com/jjvie/status/885408471998320640">13 juillet 2017</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
