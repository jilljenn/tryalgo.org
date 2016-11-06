---
layout: en
title:  "2 player game on a row of coins"
category: games
author: Christoph Dürr
excerpt_separator: <!--more-->
---

Consider a 2 player game that plays on a row of coins.  Players in turn remove either the leftmost or the rightmost coin until the row is empty. What is the maximum amount that the first player can collect if both players play optimally? See [Problem 4](http://www.spoj.com/problems/CODEM4/).

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



