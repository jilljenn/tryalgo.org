---
layout: en
title:  "Sprague-Grundy theorem"
category: games
author: Christoph Dürr
problems:
   "uva:Treblecross": https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1502
---

Given a 2 player impartial game, decide for a given configuration if there is a possibility for the first player to win assuming the second player plays perfectly.

## Summary

See the corresponding [wikipedia page](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem) for more details.

The theory says the following.   Suppose you have a directed acyclic graph, with a pebble on a cell. Two players move in turns the pebble along an outgoing arc to a successor vertex. The first player who cannot move the pebble anymore looses.

Which are the winning and which are the loosing configurations? Well this can be determined recursively. Vertices with zero outdegree are loosing vertices.  Vertices that lead to a loosing vertex are winning vertices.  Vertices that lead only to loosing vertices are loosing vertices.

Now we can augment this binary information by replacing it by a non-negative integer, called the *Grundy number* or *nimber*.  Vertices with zero outdegree get the number 0.  In general the number assigned to a vertex is the smallest non-negative integer which does not belong to one of the reachable vertices.  Clearly a vertex is winning iff its nimber is positive.

These number became interesting when combining two games, and this is the purpose of the Sprague-Grundy theorem.  Suppose you combine two DAGs into one game.  Now there is a pebble in each graph, hence a game configuration is a pair of vertices, one from each graph.  A valid move is to move one of the pebbles to a successor, and to leave the other pebble untouched.   This is a game that could  be decribed by a much bigger and single DAG.  The Sprague-Grundy theorem says that the nimber of configuration (u,v) is simply the bitwise exclusive OR of the nimbers of u and of v.

## Example

See [this page](http://lbv-pc.blogspot.fr/2012/07/treblecross.html) for an excellent and more detailed explanation of a solution to the following problem.

You are given a row of cells, some of which are marked. Two players in turn each marks a cell. The first player who reaches a configuration with 3 adjacent marked cells wins.  The goal is to list all cells such that if the first player marks one of those, then he can always win the game.

    intial configuration: .....X.
    player 1:             ..X..X.
    player 2:             ..X.XX.
    player 1 wins:        ..X.XXX


Basically you first need to detect patterns where the first player can immediately win, namely .XX, X.X or XX.  Then by adding X.. to the left and ..X to the right we end up with a string of the form X..?X..?X etc, where every sequence of points has some length at least 2.  These sequences form sub-games, where the 2 first and 2 last points are forbidden cells, since the opponent can then immediately win.  The trick is then to compute the nimber for configurations of the form X.{k}X for every k up to 200.  Then you can combine these numbers with XOR in order to decide whether some configuration is loosing or not.

The following code solves this problem in time $$O(n^2)$$.
{% highlight python %}
from sys import *

def readint():    return int(input())
def readstr():    return input().strip()
def readarray(f): return map(f, input().split())


N = 205  # compute nimber until until 200 + 2 + 2 for the added border

# number[i] is nimber number of game on X.{i}X
nimber = []

for L in range(N):
    reachable = set()                # compute nimber numbers for accessible states
    for i in range(2, L - 2):        # i = allowed position to play (not too close to border)
        reachable.add(nimber[i] ^ nimber[L - i - 1])
    val = 0                          # find smallest value NOT in set reachable
    while val in reachable:
        val += 1
    nimber.append(val)


def solve(config):
    """ This part has complexity O(N)
    """
    # if "XXX" in config:              # should never happen, but who knows
    #     return []
    sol = set()                      # first test if player can win right now
    pattern = [".XX", "X.X", "XX."]
    for i in range(3):
        last = config.find(pattern[i])
        while last != -1:
            sol.add(last + i)        # position of . in pattern in config
            last = config.find(pattern[i], last + 2)  # +2 because X.X?? matches ??X.X
    if sol:
        return sol
    config = "X.." + config + "..X"  # this trick avoids particular processing at border
    sizes = []                       # sizes of subgames
    s = 0
    for z in config[1:]:             # avoid initial X
        if z == 'X':                 # determine sizes of . sequences delimited by X
            sizes.append(s)
            s = 0
        else:
            s += 1                   # count the z='.'
    current = 0                      # compute nimber of given configuration
    for s in sizes:
        current ^= nimber[s]
    start = -2                       # start of current . sequence
    for s in sizes:
        for j in range(2, s - 2):    # compute nimber of playing j in this . sequence
            if current ^ nimber[s] ^ nimber[j] ^ nimber[s - j - 1] == 0:
                sol.add(start + j)   # is loosing configuration for second player
        start += s + 1
    return sol


for testcase in range(readint()):
    sol = solve(readstr())
    if sol:
        print("WINNING")
        format = "%i"
        for i in sorted(sol):
            print(format % (i + 1), end='')
            format = " %i"
    else:
        print("LOSING")
    print()
{% endhighlight %}
