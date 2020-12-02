# Préliminaires, servez-vous !

from collections import deque

def affiche(laby):
    for line in laby:
        print(''.join(line))

def reconstruit(n, m, laby, prec):
    def parcourt(i, j):
        laby[i][j] = 'x'
        p = prec[i][j]
        if p:
            parcourt(*p)
    parcourt(n - 1, m - 2)
    affiche(laby)

# Votre mission commence ici

def sortie_accessible(n, m, laby):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def explore(i, j):
        pass # Remplissez ici



    explore(1, 0)
    return laby[n - 1][m - 2] == 'x'

def chemin(n, m, laby):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    deja_vu = [[False] * m for _ in range(n)]
    prec = [[None] * m for _ in range(n)]
    todo = [(1, 0, None)]
    while todo:
        i, j, p = todo.pop()
        # Remplissez ici






    reconstruit(n, m, laby, prec)

def plus_court_chemin(n, m, laby):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    deja_vu = [[False] * m for _ in range(n)]
    prec = [[None] * m for _ in range(n)]
    todo = deque([(1, 0)])
    deja_vu[1][0] = True
    while todo:
        i, j = todo.pop()
        # Remplissez ici








    reconstruit(n, m, laby, prec)

# Lecture de l'entrée

if __name__ == '__main__':
    n, m = map(int, input().split())
    laby = []
    for _ in range(n):
        laby.append(list(input()))
    print(sortie_accessible(n, m, laby))  # Ne décommentez pas ces 3 lignes en même temps car les fonctions modifient le labyrinthe
    # chemin(n, m, laby)
    # plus_court_chemin(n, m, laby)
