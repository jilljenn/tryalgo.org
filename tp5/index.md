---
layout: page
title: "TP 5 : Couplage et flots"
parent: Problems
---

[Slides](/static/couplages-flots.pdf)

## Exercices

- [Book Club](https://uva.onlinejudge.org/contests/345-11652823/12880.pdf) (SWERC 2014)
- [It Can Be Arranged](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=602&page=show_problem&problem=4417) (SWERC 2013)
- [Sentry Robots](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3994)

## Couplage maximum dans un graphe biparti

{% highlight c++ %}
#include <iostream>
#include <vector>
using namespace std;

int n, m;
bool visit[10000];
int match[10000];
vector<int> graph[10000];

bool augment(int u) {
    int v;
    for(int i = 0; i < graph[u].size(); ++i) {
        v = graph[u][i];
        if(!visit[v]) {
            visit[v] = true;
            if(match[v] == -1 || augment(match[v])) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

for(int i = 0; i < n; ++i)
    match[i] = -1;
for(int i = 0; i < n; ++i) {
    for(int j = 0; j < n; ++j)
        visit[j] = false;
    augment(i);
}
{% endhighlight %}

## Flot maximum

{% highlight c++ %}
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

#define SIZE 2 * 100 + 4
#define INF 1e9

int n, m;
bool visit[SIZE];
vector<int> graph[SIZE];
unordered_map<int, int> capacity, flow;

bool augment(int u, int val) {
    visit[u] = true;
    if(u == 2 * n + 3)
        return val;
    int v, res, delta, cuv;
    for(int i = 0; i < graph[u].size(); ++i) {
        v = graph[u][i];
        cuv = capacity[u * SIZE + v];
        if(!visit[v] && cuv > flow[u * SIZE + v]) {
            res = min(val, cuv - flow[u * SIZE + v]);
            delta = augment(v, res);
            if(delta > 0) {
                flow[u * SIZE + v] += delta;
                flow[v * SIZE + u] -= delta;
                return delta;
            }
        }
    }
    return 0;
}

void add(int u, int v, int c) {
    graph[u].push_back(v);
    flow[u * SIZE + v] = 0;
    flow[v * SIZE + u] = 0;
    capacity[u * SIZE + v] = c;
    graph[v].push_back(u);
    capacity[v * SIZE + u] = 0;
}

do {
    for(int i = 0; i <= t2; ++i)
        visit[i] = false;
} while(augment(s1, 1e9) > 0);
{% endhighlight %}
