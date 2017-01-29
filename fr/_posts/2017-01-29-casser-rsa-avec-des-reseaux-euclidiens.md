---
layout: fr
title: Casser RSA avec des réseaux euclidiens
author: Jill-Jênn Vie
---

Bonjour.

## Rappels sur RSA

On considère deux nombres premiers $p$ et $q$ gardés secrets. Leur produit $n = pq$ sera public mais sa factorisation doit être difficile, donc il ne faut pas que $p$ et $q$ soient trop petits, ni trop proches l'un de l'autre[^1]

 [^1]: Sinon, en faisant une recherche exhaustive autour de $\sqrt{n}$, il est possible de retrouver $p$ ou $q$.

On choisit un entier $d$ premier avec $\varphi(n) = (p - 1)(q - 1)$, puis $e$ son inverse modulo $\varphi(n)$, c'est-à-dire l'entier de $[1, \varphi(n) - 1]$ vérifiant $ed \equiv 1 \bmod \varphi(n)$.

La paire $(n, d)$ sera la clé privée tandis que $(n, e)$ sera la clé publique. Le chiffrement RSA repose sur deux méthodes principales. Il est très important que $d$ soit gardé secret, puisqu'il permet de déchiffrer les messages.

Algorithme de chiffrement :

:   à partir d'un message clair $m$ et de la clé publique $(n, e)$, on calcule le message chiffré $c = m^e$ mod $n$.

Algorithme de déchiffrement :

:   à partir d'un message chiffré $c$ et de la clé privée $(n, d)$, on recouvre le message clair : $m = c^d$ mod $n$.

## Une première attaque

Supposons que l'on trouve (par magie) un nombre qui est multiple de $p$ mais pas de $q$. Alors en calculant le PGCD de ce nombre avec $n$ on trouvera… $p$. C'est embêtant.

## Une deuxième attaque

![RSA avec LLL](/fr/images/rsa-lll.png)

## Le cas général

En fait la bad news c'est que Coppersmith a prouvé le théorème suivant : Soit $P$ un polynôme unitaire de degré $\delta$ à coefficients entiers et $n$ un entier de factorisation inconnue. Alors on peut trouver en temps polynomial en $(\log n, \delta)$ toutes les racines modulo $n$ de ce polynôme, inférieures ou égales à $n^{1/\delta}$.

### Exemple

Du coup, pour revenir au RSA, si on suppose que :

- $p \geq q$
- la moitié des bits de poids fort de $p$ soit connue : $p = p_0 + \epsilon$ où $\epsilon \leq n^{1/4}$ est inconnu

Alors si on considère le polynôme $P = p_0 + X$, alors $pgcd(P(\epsilon), n) = p \geq n^{1/2}$ tandis que la racine $\epsilon$ est petite donc trouvable en temps polynomial en $\log n$.
