---
layout: fr
title: Différence entre mémoïsation et programmation dynamique
author: Jill-Jênn Vie
excerpt_separator: <!--more-->
---

**Update :** Merci à Marc de Falco qui a trouvé une erreur dans le code initial. J'élabore là-dessus ci-dessous.

L'autre jour, en jury de l'agrégation d'informatique où j'ai eu la chance de participer de 2022 à 2025 en compagnie de collègues et candidats aussi brillants que passionnés, le candidat choisit la leçon sur la [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique) et fait son développement sur le célèbre algorithme de [sac à dos](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos). Une collègue pose la question : "Qu'est-ce qui se passe si les capacités des poids sont **négatives** ?"

Cette question permet d'illustrer une différence entre mémoïsation et programmation dynamique.

On commence par la façon classique de résoudre le problème dans le cas des capacités positives $c_i \geqslant 0$. La relation de récurrence (équation de Bellman) est la suivante.

Si $maxval[i][c]$ est la capacité maximale que l'on peut atteindre avec les $i \geqslant 0$ premiers objets et une capacité limite de $c$, alors $maxval[0][c] = 0$ pour toute capacité $c$ (pas d'objet) et quand $i \geqslant 1$,

$$maxval[i][c] = \max \begin{cases}maxval[i - 1][c] \textrm{ (si on ne prend pas le $i$-ème objet)}\\maxval[i - 1][c - c_i] + v_i \textrm{ si $c \geqslant c_i$ (si on prend le $i$-ème objet)}\end{cases}$$

On peut faire un balayage avec une double boucle pour aller en nombre d'objets croissant et capacité croissante (bottom-up). Complexité temps et mémoire : $O(nC)$ où $n$ est le nombre d'objets et $C$ est la capacité du sac à dos.

```python
capacities = [2, 3, 5]
values = [6, 4, 2]
cmax = 9

def knapsack():
    n = len(capacities)
    max_value = [[0] * (1 + cmax) for _ in range(n + 1)]
    candidates = []
    for i in range(1, n + 1):
        for c in range(0, cmax + 1):
            candidates = [max_value[i - 1][c]]
            if c >= capacities[i - 1]:
                candidates.append(values[i - 1] + max_value[i - 1][c - capacities[i - 1]])
            max_value[i][c] = max(candidates)
    return max_value[n][cmax]

knapsack()
```

<button class="run" disabled>Run</button>

<pre class="output highlight"></pre>

En effet, on peut obtenir une valeur de 10 avec les 2 premiers objets (capacité totale 2 + 3 = 5 en dessous de la limite 9).

Cette méthode nous permet de répondre à toutes les questions possibles : que vaut $maxval$ pour les $i$ premiers objets et une capacité limite $c$ ? On visite tous les états possibles $(i, c)$.

Regardons à présent à quoi ressemblerait une solution qui mémoïserait (i.e. stockerait les appels récursifs pour ne pas recalculer la même quantité plusieurs fois). On peut s'appuyer sur l'astuce Python du décorateur `@cache`. (On est plusieurs profs à penser que la mémoïsation devrait être enseignée avant la programmation dynamique.) Notez au passage à quel point ce code est similaire au précédent. En particulier, si on faisait du Haskell, on n'aurait pas besoin du décorateur.

```python
from functools import cache

capacities = [2, 3, 5]
values = [6, 4, 2]
cmax = 9

@cache
def max_value(i, c):
    candidates = []
    if i == 0:
        return 0
    candidates.append(max_value(i - 1, c))
    if c >= capacities[i - 1]:
        candidates.append(values[i - 1] + max_value(i - 1, c - capacities[i - 1]))
    return max(candidates)

n = len(capacities)
max_value(n, cmax)
```

<button class="run" disabled>Run</button>

<pre class="output highlight"></pre>

Complexité : autant d'appels que strictement nécessaire, $O(nC)$ au pire. Mais soyons plus précis.

Soit $C_M$ le nombre d'états uniques (cases mémoire) parcourus par l'algorithme. On a d'une part $C_M \leq (n + 1)(C + 1)$ car c'est le nombre total d'états possibles, et d'autre part $C_M \leq 2^n$ car c'est le nombre total de combinaisons possibles (et d'appels récursifs si on ne faisait pas de mémoïsation).

On voit bien que selon le régime, par exemple si $n$ est petit et $C$ grand, il vaut mieux tout tester, même avec l'algorithme naïf, plutôt que de remplir tous les états possibles. Si $C$ est petit on a plutôt envie d'exploiter la redondance. Dans tous les cas, l'algorithme de mémoïsation est optimal en temps (mais pas en mémoire). Le gain par rapport au naïf est $C_M / 2^n$ et par rapport à l'algo de programmation dynamique est $C_M / ((n + 1)(C + 1))$. Faudrait que je fasse un dessin sur une instance avec les cases visitées pour chaque algorithme.

À présent, regardons ce qui se passe dans le cas de capacités négatives. (Veillez à bien exécuter les cellules précédentes avant celle-ci.)

~~La mémoïsation fonctionne et reste optimale.~~
**Update :** en fait non, le code ci-dessus est faux. Cherchez un contre-exemple, en voici un.

```python
capacities = [2, -1]
values = [1, 1]
cmax = 1

n = len(capacities)
max_value.cache_clear()  # Sinon les appels sont encore dans la mémoire
max_value(n, cmax)
```

<button class="run" disabled>Run</button>

<pre class="output highlight"></pre>

Ici, la réponse est bonne : 2, on prend tous les objets. Mais si on met les objets dans l'autre ordre :

```python
capacities = [-1, 2]
values = [1, 1]
cmax = 1

n = len(capacities)
max_value.cache_clear()
max_value(n, cmax)
```

<button class="run" disabled>Run</button>

<pre class="output highlight"></pre>

On rate l'objet de poids 2 car on ne s'autorise pas à passer par des états de capacités négatives qu'on pourrait rattraper plus tard. Autorisons donc les capacités négatives tant que l'état final convient. La relation de récurrence est donc :

$$
maxval[0][c] = \begin{cases}0 \textrm{ si $c \geqslant 0$ (il reste de la capacité)}\\
-\infty \textrm{ sinon}\end{cases}\\
maxval[i][c] = \max \begin{cases}maxval[i - 1][c] \textrm{ si on ne prend pas le $i$-ème objet}\\maxval[i - 1][c - c_i] + v_i \textrm{ si on prend le $i$-ème objet}\end{cases}$$

Code modifié :

```python
from functools import cache

capacities = [-1, 2]
values = [1, 1]
cmax = 1

@cache
def max_value_neg(i, c):
    candidates = []
    if i == 0:
        return 0 if c >= 0 else float('-inf')  # Valeur admissible s'il reste de la capacité
    return max(
        max_value_neg(i - 1, c),
        values[i - 1] + max_value_neg(i - 1, c - capacities[i - 1])
    )

n = len(capacities)
max_value_neg(n, cmax)
```

<button class="run" disabled>Run</button>

<pre class="output highlight"></pre>

Quelle est sa complexité ? On pourrait l'améliorer en éliminant les branches non prometteuses (s'il ne reste plus d'objets pour aboutir à un état positif). Qu'en est-il de l'algorithme itératif de programmation dynamique au début de ce billet ?

```python
capacities = [-1, 2]
values = [1, 1]
cmax = 1

knapsack()
```

<button class="run" disabled>Run</button>

<pre class="output highlight language-python highlighter-rouge"></pre>

Exercice au lecteur : comment modifier le code précédent de `knapsack` pour qu'il fonctionne dans le cas de capacités négatives ? Quel est le nombre d'états maximaux à considérer ? Quelle est la structure de données adaptée ? Faites un dessin sur papier pour voir ce qui se passe.

Une autre solution d'un étudiant est de partir d'un état où on a pris toutes les capacités négatives et considérer des actions "enlever l'objet" afin de se ramener au sac à dos à capacités positives. C'est également une solution correcte.

Méta : si ça vous intéresse de voir comment j'ai chargé [pyodide](https://pyodide.org/en/stable/usage/quickstart.html) sur ce blog post Jekyll, vous pouvez regarder [en bas du source de cette page](https://raw.githubusercontent.com/jilljenn/tryalgo.org/refs/heads/master/fr/_posts/2025-09-03-difference-memoisation-programmation-dynamique.md). Vous pouvez [faire une PR](https://github.com/jilljenn/tryalgo.org) pour remplacer le premier bloc par un textarea (avec coloration syntaxique svp) pour modifier le code.

<script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
<script>
const runners = document.querySelectorAll(".run");
const codes = document.getElementsByClassName("language-python");
const results = document.getElementsByClassName("output");

async function main() {
    let pyodide = await loadPyodide();
    runners.forEach((button, index) => {
    	button.disabled = false;
    	button.addEventListener("click", () => evaluatePython(index));
    });
    return pyodide;
}
let pyodideReadyPromise = main();

async function evaluatePython(cellId) {
    let pyodide = await pyodideReadyPromise;
    try {
        let output = pyodide.runPython(codes[cellId].textContent);
        results[cellId].textContent = output;
    } catch (err) {
        console.log(err);
        results[cellId].textContent = err;
    }
}
</script>
