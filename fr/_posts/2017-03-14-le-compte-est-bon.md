---
layout: fr
title: Le Compte est bon ?
author: Jill-Jênn Vie
---

Pourrez-vous résoudre cette énigme du jeu Le Compte est bon ?

 

<center>
<h2>952</h2>
<h3>25  50  75  100  3  6</h3>
</center>

 

(C'est passé à la télé en 1997, et la solution est cocasse.)

<iframe width="560" height="315" src="https://www.youtube.com/embed/pfa3MHLLSWI?ecver=1" frameborder="0" allowfullscreen></iframe>

Parce que nous, si. Faites **pip install tryalgo**, puis en Python :

    >>> from tryalgo.arithm_expr_target import arithm_expr_target
    >>> arithm_expr_target([25, 50, 75, 100, 3, 6], 952)

<a name="cheat" href="#cheat" onclick="document.querySelector('#solution').style.display = 'block';">Show output (spoiler)</a>

<div id="solution" style="display: none">
<div class="highlighter-rouge">
<pre class="highlight">
<code>'((((75*3)*(100+6))-50)/25)=952'</code>
</pre>
</div>
</div>

Ce n'est pas la seule solution, mais toutes les solutions impliquent de diviser par 50 ou 25, et donc de passer par des grands nombres. Merci Pascal Lafourcade pour avoir remarqué cela.

[Voir l'algorithme permettant de résoudre Le Compte est bon](https://jilljenn.github.io/tryalgo/_modules/tryalgo/arithm_expr_target.html#arithm_expr_target)
