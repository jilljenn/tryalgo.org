data = open('paris.txt').read().splitlines()
N, M, T, C, S = map(int, data[0].split())
graphe = [[] for _ in range(N)]
for i in range(N + 1, N + M + 1):
    a, b, d, c, l = map(int, data[i].split())
    graphe[a].append((b, c, l))
    if d == 2:
        graphe[b].append((a, c, l)) # Build graph

print(graphe[0])
print(graphe[4942])
print(graphe[6755])

noeud = 2780
for i in range(10):
    voisins = graphe[noeud]
    noeud, cout, score = voisins[0]
    print(noeud)
