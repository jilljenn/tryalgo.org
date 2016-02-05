#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google hashcode - c.durr - 2016

# Pizza Google
# http://primers.xyz/7
# weighted set packing

# from string import upper
"""
Résultats:

glouton avec priorité nombre de blancs par rectangle: 8994

glouton et recherche locale: 9526
opération: ajouter un rectangle à sol, enlever de sol tous
ceux qui intersectent R et compléter de manière gloutonne.
ou alors enlever rectangle R de sol, et compléter de manière
gloutonne (en excluant temporairement R).

diviser pizza en k régions, et pour chacune résoudre le
sous-problème par un programme linéaire à variables entière
utilisant CPLEX en limitant le temps à une heure.
Puis amélioration par recherche locale.

k score before/after local search
--------------------------
1  8888  9826
2 10141 10149
3 10162 10167
4 10170 10176
5 10190 10194
6 10190 10198
"""

from sys import *
import random
from functools import reduce

def readints():   return list(map(int, stdin.readline().split(',')))
def readstr():    return stdin.readline().strip()

def rect(i,j,w,h):
    for a in range(i, i+h):
        for b in range(j, j+w):
            yield (a,b)

# read input
print("read input")
width, height, minsum, maxsize = readints()
P = []  # pizza
for _ in range(height):
    line = readstr()
    row = list(map(lambda c: int(c=='H'), line))
    P.append(row)

print("create shapes")
# create shapes
S = [] # shapes as width, height pairs
for w in range(1, maxsize+1):
    for h in range(1, maxsize+1):
        if w * h > maxsize:
            break
        S.append((w, h))

print("create slices")
# create valid positions, there are 105 536
Q = [] # slices as row, col, width, height, sum tuples
for i in range(height):
    for j in range(width):
        for w, h in S:
            if i + h > height or j + w > width:
                continue
            rectsum = sum(P[a][b] for a,b in rect(i, j, w, h))
            if rectsum < minsum:
                continue
            Q.append((i, j, w, h, rectsum))

print("create grid")
# G[i][j] = list of slices covering cell (i,j)
G = [[[] for j in range(width)] for i in range(height)]
for k in range(len(Q)):
    i, j, w, h = Q[k][:4]
    for a, b in rect(i,j,w,h):
        G[a][b].append(k)

print("create conflict graph")
# create conflict graph, there are 51 417 010 constraints
C = [reduce(set.union, [set(G[a][b]) for a,b in rect(*Q[k][:4])] ) for k in range(len(Q))]
for k in range(len(Q)):
    C[k].remove(k)


def inbounds(k, bounds):
    return bounds[0] <= Q[k][0] and Q[k][0] + Q[k][3] <= bounds[1]


def write_lp(filename, bounds):
    with open(filename, 'w') as f:
        # generate LP
        f.write("Maximize\n")
        f.write("  obj: ")
        for k in range(len(Q)):
            if inbounds(k, bounds):
                f.write(" +%i x%i" % (Q[k][2]*Q[k][3], k))
        f.write("\n")
        f.write("Subject To\n")
        for i in range(height):
            for j in range(width):
                if G[i][j]:
                    f.write("  c%i_%i: " % (i, j))
                    for k in G[i][j]:
                        f.write(" +x%i" % k)
                    f.write(" <= 1\n")
        for k in range(len(Q)):
            if sol[k]:
                f.write("x%i = 1\n" % k)
        f.write("Binary\n")
        for k in range(len(Q)):
            if inbounds(k, bounds):
                f.write(" x%i\n" % k)
        f.write("End\n")


print("create shape order")
# greedy solution
order = []
for k in range(len(Q)):
    i, j, w, h, rectsum = Q[k]
    # priority "number white" -(w*h - rectsum)        gives score 8994
    # priority "density" (-(w*h - rectsum)/float(w*h) gives score 8972
    # priority "black, white" rectsum, -w*h           gives score 8953
    order.append((-(w*h - rectsum), k))
order.sort()

#  combined with 1-add-rem-local search 9526
#  combined with 1-add-local search 9511
#  combined with 1-rem-local search 9199

print("select greedily")
# boolean solution vector
sol = [False] * len(Q)
conflicts = [0] * len(Q)
# conflict[k] = number of k1 from the solution k conflicts with
score = 0


def save():
    global hist_add, hist_rem, score
    hist_add = []
    hist_rem = []


def add(k):
    global hist_add, hist_rem, score
    hist_add.append(k)
    assert not conflicts[k]
    sol[k] = True
    score += Q[k][2] * Q[k][3]
    for k2 in C[k]:
        conflicts[k2] += 1


def rem(k):
    global hist_add, hist_rem, score
    hist_rem.append(k)
    assert sol[k]
    sol[k] = False
    score -= Q[k][2] * Q[k][3]
    for k2 in C[k]:
        conflicts[k2] -= 1


def read(filename):
    print("read solution")
    for line in open(filename, 'r'):
        if line[0]=='x':
            p = line.find(' ')
            k = int(line[1:p])
            add(k)


def restore():
    global hist_add, hist_rem, score
    list_add = hist_rem[:]
    list_rem = hist_add[:]
    for k in list_rem:
        rem(k)
    for k in list_add:
        add(k)


def greedy():
    for item in order:
        k = item[-1]
        if not conflicts[k] and not sol[k]:
            add(k)

def local_change(k1):
    before = score
    save()
    if sol[k1]:
        rem(k1)
        conflicts[k1] += 1  # force greedy *not* to select k1
        greedy()
        conflicts[k1] -= 1
    else:
        for k2 in C[k1]:
            if sol[k2]:
                rem(k2)
        add(k1)
        greedy()
    if before > score:
        restore()

# -lp <nb_parts>
# -read <solutionfile>
# nothing

save()

if len(argv)==3 and argv[1]=="-lp":
    nb_parts = int(argv[2])
    last = 0
    for p in range(1, nb_parts+1):
        b = min(height * p // nb_parts, height)
        print("gen lp from %i to %i" % (last, b))
        write_lp("tmp%i.lp" % p, (last, b))
        last = b
    exit(0)

if len(argv)==3 and argv[1]=="-read":
    read(argv[2])
else:
    greedy()


print("score before local search = %i" % score)

# local search
before = 0
while before < score:
    before = score
    # local = list(range(len(Q)))
    # random.shuffle(local)
    for item in order:
        k = item[-1]
        local_change(k)

# print solution
alphabet = "abcdefghijklmnopqrstuvwxyz"
M = [['_*'[P[i][j]] for j in range(width)] for i in range(height)]
for k in range(len(Q)):
    if sol[k]:
        c = alphabet[ k % len(alphabet)]
        C = c.upper()
        i, j, w, h = Q[k][:4]
        for a in range(i, i+h):
            for b in range(j, j+w):
                if P[a][b]:
                    M[a][b] = C
                else:
                    M[a][b] = c
for line in M:
    print(''.join(line))

# extract score
score = 0
for k in range(len(Q)):
    if sol[k]:
        score += Q[k][2] * Q[k][3]

print("score after local search = %i" % score)
