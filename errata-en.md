---
lang: en
layout: page
title: Errata of the english translation
---

Some typos we spotted in the book.

- page 40 Figure 1.8: there should be two different gray shades among the rectangles. In the final print they might be too close to be distinguished.

- page 47, head of section 2.5: the second abra should be aligned with the suffix of the string abracadabra above.

- page 55: In the code of *powerstring_by_find*,  the variables *u* and *x* should be the same. Moreover in CPython and in Pypy the complexity of `haystack.find(needle)` with $m=\textrm{len(haystack)},\: n=\textrm{len(needle)}$ is $O((n-m) * n)$ instead of $O(n + m)$. Hence the function *powerstring_by_find* has quadratic time complexity, which makes it not very useful.

- page 115: the formula should be

$$    \frac{d'[n][v] - d'[k][v]}{n-k}  = \frac{d[n][v] - n\Delta - (d[k][v] - k\Delta)}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \frac{n\Delta - k\Delta}{n-k}\\
     = \frac{d[n][v] - d[k][v] }{n-k} - \Delta$$

- page 116: Meigu Guan was a lecturer (then president) of Shandong Normal University. He worked on the route inspection problem during the Great Leap Forward of 1958-1960 (before the Chinese Cultural Revolution). Jack Edmonds got interested in his work and called the problem "Chinese postman problem" in honor of Guan. Thanks Wikipedia and Ning Yan Zhu for noticing our mistake. See also [<span class="citation" data-cites="grotschel2012euler">(Grötschel and Yuan, 2012)</span>](#ref-grotschel2012euler)

- page 143: the expression $\sum_{E_\ell}\ell$ should be instead $\sum \ell$, which stands for $\sum_{u\in U} \ell(u) + \sum_{v\in V} \ell(v)$.

- page 170 (Huffman trees): the code would generate an error for example on given frequencies {'a':1, 'b':1, 'c':2}, because in case of identical frequencies, the heap would compare trees, which can be either strings (in case of a single node) or lists (in case of larger trees) and hence be incomparable. The solution is to work with a heap over (frequency, tree_index) pairs and store the trees separately. See the [source code](https://jilljenn.github.io/tryalgo/_modules/tryalgo/huffman.html#huffman).

- page 213: Indeed, an integer y can be written -> any composite integer y

- page 213: The inner loop should start at i * i instead of 2 * i for the announced complexity.

- page 240, last line: suffix of t begn inning -> beginning

## References

<div id="refs" class="references csl-bib-body hanging-indent"
role="doc-bibliography">
<div id="ref-grotschel2012euler" class="csl-entry"
role="doc-biblioentry">
Grötschel, Martin, and Ya-xiang Yuan. 2012. <span>“Euler, Mei-Ko Kwan,
k<span>ö</span>nigsberg, and a Chinese Postman.”</span> <em>Optimization
Stories</em> 43. <a
href="https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf">https://www.math.uni-bielefeld.de/documenta/vol-ismp/16_groetschel-martin-yuan-ya-xiang.pdf</a>.
</div>
</div>
