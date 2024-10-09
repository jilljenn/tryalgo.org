---
layout: en
title:  "2 player game on a row of coins"
category: games
author: Christoph Dürr
excerpt_separator: <!--more-->
problems:
   "spoj:Problem 4": http://www.spoj.com/problems/CODEM4/
   "cses:Removal game": https://cses.fi/problemset/task/1097
---

Consider a 2 player game that plays on a row of coins.  Players in turn remove either the leftmost or the rightmost coin until the row is empty. What is the maximum amount that the first player can collect if both players play optimally?

![]({{site.images}}row-game.svg "The next player in turn can take either the leftmost or rightmost coin." ){:width="250"}


<!--more-->

Since the sum of the amount drawn by both players is constant in all scenarios (it is the total coin sum), the game is said to be *constant sum*, which in essence is as a *zero sum* game by translation.

## A game on a DAG

Say the coin values of the initial coin row are $$x_0,x_1,\ldots,x_{n-1}$$.  Then every game configuration is an interval of the form [i,j], and the game ends here if i=j. If i<j then the next configuration is either [i+1,j] or [i,j-1].

Hence the game plays on a DAG, where vertex (i,j) with i<j has outgoing arcs to vertices (i+1,j) and (i,j-1).  The value of the game in this situation can therefore be computed by dynamic programming.

## Dynamic Program

Dynamic Programming is the swiss knife that every programmer should have always ready to use.
We call it swiss but in fact these tools are much older.  In the antic roman culture such knifes were [known](http://www.laboiteverte.fr/un-outil-multifonction-de-la-rome-antique/).


![](http://www.laboiteverte.fr/wp-content/uploads/2015/11/rome-antique-outil-multifonction-01.jpg "Credit: la boîte verte" ){:width="400"}


For each of these configurations [i,j] we denote by *smart[i,j]* the optimal gain that the first player can obtain if both players play optimally.  We also consider the scenario where the first player tries to maximize his gain and the second to minimize his gain.  For this scenario we denote by *dumb[i,j]*  the gain achieved by the player starting at configuration [i,j].  In addition we denote *sum[i,j]* to be the sum $$x_i+\ldots+x_j$$.

We have the base case $$dumb[i,i]=smart[i,i]=x_i$$ because there is only one way to play. Then for i<j we have

$$ smart[i,j] = sum[i,j] - \min\{ smart[i+1,j], smart[i,j-1]\}.$$


![]({{site.images}}row-game-dag.svg "The value of the game smart[i,j] depends on smart[i+1,j] and smart[i,j-1]." ){:width="250"}

In case the second player is dumb, we have to distinguish the case when it is the turn for player 1 or for player 2.
Player 1 wants to maximize his gain, while player 2 wants to minimize it.  Player 1 starts to play on the configuration [0,n-1], and hence gets to play all configurations where j-i has the same parity as n-1.

Hence when j-i+n is odd we have

$$ dumb[i,j] = sum[i,j] - \min\{ dumb[i+1,j], dumb[i,j-1]\},$$

otherwise we have

$$ dumb[i,j] = sum[i,j] - \max\{ dumb[i+1,j], dumb[i,j-1]\}.$$


{% highlight c++ %}
#include <iostream>

using namespace std;

int main() {
  int testCases;
  cin >> testCases;
  while (testCases-->0) {
    int n;
    cin >> n;
    int smart[n][n], dumb[n][n], sum[n][n];
    for (int i = 0; i < n; i++) {
        cin >> sum[i][i];
        smart[i][i] = dumb[i][i] = sum[i][i];
    for (int d = 1; d < n; d++)
      for (int i = 0; i + d < n; i++) {
        int j = i + d;
        sum[i][j] = sum[i][j-1] + sum[j][j];
        smart[i][j] = sum[i][j] - min( smart[i+1][j], smart[i][j-1] );
        if ((d + n) % 2)
          dumb[i][j] = sum[i][j] - min( dumb[i+1][j], dumb[i][j-1] );
        else
          dumb[i][j] = sum[i][j] - max( dumb[i+1][j], dumb[i][j-1] );
      }
    }
    cout << dumb[0][n-1] << " " << smart[0][n-1] << endl;
  }
  return 0;
}
{% endhighlight %}

## Update October 2024

Here is a simpler solution. Each interval [i:j] represents a configuration of the game. We only need to compute the maximum score obtained by the player that starts on this configuration, without distinction if its the first or the second player in the initial configuration.

For indices i,j, let $A[i,j]$ be the maximum score the first player can obtain, when playing on a row of coins from index i to index j (excluded). Also let $S[i,j]$ be the total sum of those coins. Then, since it is a zero sum game, the maximum score is $S[i,j]$ minus the maximum score of the second player in the next round. And the later is $A[i+1,j]$ or $A[i,j-1]$ depending on the choice of the first player. Hence we have the recursion

$$
  A[i,j] = S[i,j] - \min\{A[i+1,j], A[i,j-1]\},
$$

leading to the following dynamic program.

{% highlight Python %}
import sys

def readint(): return int(sys.stdin.readline())
def readints(): return list(map(int, sys.stdin.readline().strip().split()))

n = readint()
x = readints()

A = [ [0 for j in range(n+1)] for i in range(n + 1)]
S = [ [0 for j in range(n+1)] for i in range(n + 1)]

for j_i in range(1, n+1):           # difference 1 <= j - i <= n
    for i in range(n - j_i + 1):    # 0 <= i <= n-1
        j = i + j_i                 # j <= n
        S[i][j] = S[i][j-1] + x[j-1]
        A[i][j] = S[i][j] - min(A[i+1][j], A[i][j-1])
print( A[0][n] )
{% endhighlight %}



