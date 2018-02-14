feuille = [
	["rouge", [1, 3]],
	["blanc", [0, 2, 4]],
	["rouge", [1, 5]],
	["rouge", [0, 4, 6]],
	["rouge", [1, 3, 5, 7]],
	["rouge", [2, 4, 8]],
	["blanc", [3, 7]],
	["rouge", [6, 4, 8]],
	["blanc", [5, 7]]
]

def remplissage(feuille, i, courante):
	[remplacer, voisins] = feuille[i]
	feuille[i] = [courante, voisins]
	pixels_accessibles = voisins
	pixels_deja_vus = [False]*len(feuille)
	while (len(pixels_accessibles) != 0):
		p = pixels_accessibles[0]
		pixels_deja_vus[p] = True
		pixels_accessibles = pixels_accessibles[1:]
		[c, v] = feuille[p]
		if (c == remplacer):
			feuille[p] = [courante, v]
			voisins_a_ajouter = []
			for voisin in v:
				if (not pixels_deja_vus[voisin]):
					pixels_accessibles = [voisin] + pixels_accessibles
	return(feuille)

print(remplissage(feuille, 7, "bleu"))
