---
layout: fr
title: Gamme pythagoricienne
category: strings
author: Jill-Jênn Vie
---

En musique, on change d'octave en doublant la fréquence. On passe à la quinte en multipliant par 3/2.

Donc pour passer au demi-ton suivant il suffit de multiplier la fréquence par $2^{1/12}$. En Python :

```python
for i in range(12):
    print(i, 220 * (2 ** (i / 12)))
```

<button id="run" onclick="evaluatePython()" disabled>Run</button>

<pre id="output" class="highlight"></pre>

Ah oui mais c'est embêtant ça car on sait que la quinte parfaite est à 3/2 ce qui donnerait un mi à 330 Hz et non à 329.63 Hz (cf. ligne 7).

Du coup, soit tous les pianos sont faux, soit les demi-tons ne sont pas égaux. La réponse est la première.

To know more check this amazing presentation from Kenya Otsuka (Kyoto University):

<embed src="/static/20221226_Otsuka.pdf" width="100%" height="551" 
 type="application/pdf">

<script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
<script>
const res = document.getElementById("output");
const run = document.getElementById("run");
const code = document.getElementsByClassName("language-python")[0];

async function main() {
    let pyodide = await loadPyodide({
        stdout: (text) => {res.textContent += text + "\n";},
        stderr: (text) => {res.textContent += text;}
    });
    run.disabled = false;
    return pyodide;
}
let pyodideReadyPromise = main();

async function evaluatePython() {
    let pyodide = await pyodideReadyPromise;
    try {
        let output = pyodide.runPython(code.textContent);
    } catch (err) {
        console.log(err);
    }
}
</script>
