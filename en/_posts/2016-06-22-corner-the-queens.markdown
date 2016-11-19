---
layout: en
title:  "Corner the queens"
category: sequences
problem_url: "https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2835"
problem_name: "Corner the Queen"
---

Two players move in turns a queen on a chessboard, either left, down or diagonally left-down. The first player to reach the lower left corner wins.  For what initial positions is the starting player sure to win?

To make the problem more interesting, you are given a grid dimension rows*cols and have to find out the proportion of initial winning positions.

### Simulation

Let's mark on the grid the loosing positions, by inspecting the possibilities of the players. Then the cells (2,3) and (3,2) are the first loosing positions. All cells in the same column, row or diagonal are winning positions, because the player can place his opponent in a loosing position. Loosing positions are symmetric, as the game is symmetric.  Hence we can focus only on the upper diagonal loosing positions.  Let Y be the set of all y coordinates of the loosing positions discovered so far and (x,y) be the last one.  We can start with Y={3} and (x,y)=(2,3).  Then the next possible position is (x', y') = (x+1, y+2), and while x' is in Y, the next possible position (x', y') = (x'+1. y'+1).

The problem can be solved in linear time in the grid coordinates, which is ok, since the given grid coordinates are bounded by 10e6.

![]({{site.images}}corner-the-queens.svg){:width="400"}

For curiosity:
Successive points happen to be distant in x-coordinate either by 1 or by 2.  The resulting pattern does not seem to have a simple structure, it seems fractal.  Understanding it could lead possibly to a constant time algorithmic solution.  The following string shows this pattern for the first 100 points. A dash means distance 2 and a point distance 1.

    #.##.#.##.##.#.##.#.##.##.#.##.##.#.##.#.##.##.#.##.#.##.##.#.##.##.#.##.#.##.##.#.##.##.#.##.#.##.#
