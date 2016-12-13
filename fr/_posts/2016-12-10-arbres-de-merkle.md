---
layout: fr
title: "Arbres de Merkle : la structure de données à l'origine de git, BitTorrent, Bitcoin, Ethereum, The DAO et autres blockchains"
author: Jill-Jênn Vie
---

# Merkle trees (1979)

![](/fr/images/merkle/merkle.jpg)

Le principe est simple : calculer le hash d'un nœud à partir d'un hash de ses fils. Dans un arbre binaire, pour un nœud ayant pour fils $h_1$ et $h_2$ : $$ h(noeud) = h(h1, h2) $$.

Cette structure de données sera à l'origine de tout ce que je vais présenter.

# git (2005)

Logiciel de gestion de versions centralisé. Mais comment garantir l'intégrité des données ? On calcule une hiérarchie de hashes :

![](/fr/images/merkle/git.jpg)

Slide tirée de la présentation [*Code is not text! How graph technologies can help us to understand our code better*](http://www.slideshare.net/japh44/code-is-not-text-how-graph-technologies-can-help-us-to-understand-our-code-better).

[Quelqu'un sur GitHub qui est parvenu à *reverse-engineer* le hash de git.](https://gist.github.com/masak/2415865) Ce n'est pas secret, mais c'est un peu compliqué.

# BitTorrent (2001)

![](/fr/images/merkle/bitcoin.png)

- [Tribler](https://www.tribler.org/MerkleHashes/) qui explique qu'on a besoin qu'un nombre $\log n$ de hashes de pour certifier un tronçon parmi $n$ d'un fichier torrent (authentifié par le hash de la racine) : pas besoin de calculer tous les hashes de l'arbre.
- Notez qu'on a également besoin du numéro du tronçon : sa décomposition en binaire permet de dire si les tronçons sont gauche ou droite, cf. [cette réponse sur Bitcoin Stack Exchange](http://bitcoin.stackexchange.com/questions/42281/what-is-the-canonical-way-of-creating-merkle-tree-branches#comment48760_42281).
- Fun fact : git + BitTorrent = [IPFS](http://gsoc2016onkar.blogspot.fr/2016/06/ipfs.html) (InterPlanetary File System)

# Bitcoin (2009)

> *Tiens mais c'est pas mal ces arbres de Merkle, et si je fabriquais une monnaie avec ?*

![](/fr/images/merkle/nakamoto.png)

- Papier fondateur : [bitcoin.org/bitcoin.pdf](http://bitcoin.org/bitcoin.pdf)
- Curieusement, ce papier ne fait pas mention de la règle : « Pour construire un bloc, il faut trouver une nonce telle que le hash obtenu $< 2^{187}$. Si vous y parvenez, vous remportez 25 BTC soit à peu près 17500 $. » (La valeur 187 dépend du nombre de mineurs.)
- Ce qui me fascine, c'est que lorsqu'on construit un bloc, on ne sait pas encore si on est dans la bonne ligne de temps. C'est la popularité de notre chaîne de blocs qui nous dit si on a gagné ou pas. La chaîne la plus longue gagne.

# Ethereum (2014)

> *Tiens mais c'est pas mal ces arbres de Merkle, et si je fabriquais un langage Turing-complet avec ?  
What could possibly go wrong?*

![](/fr/images/merkle/ethereum.png)

[Ethereum sur Wikipédia](https://en.wikipedia.org/wiki/Ethereum)

[Leur site avec tellement de CSS qu'on croirait qu'ils peuvent sauver le monde du réchauffement climatique](https://ethereum.org)

- [Un article des auteurs qui explique la différence avec Bitcoin](https://blog.ethereum.org/2015/11/15/merkling-in-ethereum/) : il est à présent possible d'avoir accès à des états, et de pouvoir simuler la transition d'un état à un autre, donc de déclencher l'exécution d'un code et de certifier qu'elle aura lieu.
- [Le Yellow Paper difficile à lire](http://paper.gavwood.com)

# The DAO (2016)

> *Tiens mais c'est pas mal ces arbres de Merkle, et si je fabriquais un fonds d'investissement décentralisé avec ?*

DAO : decentralized autonomous organization. Bah oui tiens, pourquoi centraliser les votes lors d'une élection alors qu'on pourrait utiliser le même principe que pour les Bitcoin ?

[The DAO sur Wikipédia](https://en.wikipedia.org/wiki/The_DAO_(organization))

- [White Paper](https://github.com/ethereum/wiki/wiki/White-Paper) sur GitHub
- [L'attaque du 17 juin 2016](https://blog.slock.it/a-dao-counter-attack-613548408dd7#.846l496no) : « *Timing is everything* » : « Il nous reste 25 jours pour sauver le monde, ça ressemble à un film mais c'est pour de vrai, mais avec de l'argent fictif »
- [Un post sur Quora qui explique les différentes raisons pour lesquelles ça s'est mal passé](https://www.quora.com/What-are-the-details-of-the-DAO-hack-that-happened-in-June-2016)
- [Le post-mortem](http://vessenes.com/deconstructing-thedao-attack-a-brief-code-tour/) où l'on découvre que c'est une faute de frappe qui est à l'origine de la disparition de 3,5 millions d'ether. La Faute à l'algo ?
- Depuis cet incident, deux forks-monnaies d'Ethereum perdurent : Ethereum Classic (ETC) et Ethereum (ETH).

# Certificate Transparency vs. DNSChain

Un autre lieu où on aimerait se passer de tiers de confiance, c'est pour les certificats SSL.

Le but de Google's Certificate Transparency :

> *Make it impossible (or at least very difficult) for a CA to issue a SSL certificate for a domain without the certificate being visible to the owner of that domain.*

- [The Trouble with Certificate Transparency](https://blog.okturtles.com/2014/09/the-trouble-with-certificate-transparency/)
- [Certificate Transparency vs. China](http://thehackernews.com/2016/08/github-ssl-certificate.html), 29 août 2016
- Je n'aime pas Ars Technica mais [Google Chrome will banish Chinese certificate authority for breach of trust](http://arstechnica.com/security/2015/04/google-chrome-will-banish-chinese-certificate-authority-for-breach-of-trust/)

# « *Et alors, il y en a qui font ça dans la recherche académique ?* » demande Tito

Oui ! [Andrew Miller, Michael Hicks, Jonathan Katz, and Elaine Shi. “Authenticated Data Structures, Generically”](https://www.cs.umd.edu/~mwh/papers/gpads.pdf), POPL 2014.

Et la grande classe, c'est qu'ils proposent [une implémentation en Caml sur GitHub](https://github.com/amiller/lambda-auth/blob/master/examples/merkle.ml).

Ledit Andrew Miller expose également [son analyse d'Ethereum](https://github.com/LeastAuthority/ethereum-analyses).

Des conférences [pipeau à l'IHP](http://www.societe-informatique-de-france.fr/les-journees-sif/journees-sif-blockchains/) (16/11/2016) et [moins pipeau à Télécom ParisTech](http://www.societe-informatique-de-france.fr/les-journees-sif/journees-sif-blockchains/) (15/11/2016) (lol ils abusent, ils pourraient communiquer).

# Add-ons

- [Namecoin](https://namecoin.org), un fork de Bitcoin pour les noms de domaine et d'autres types de données
- [Tezos](https://tezos.com), un peu [méta](http://club-meta.fr) : les joueurs peuvent voter pour changer les règles
