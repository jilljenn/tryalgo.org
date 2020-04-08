---
layout: en
category: graphs
title: "Flooding a landscape"
author: Christoph Dürr
problems:
    "leetcode:407": https://leetcode.com/problems/trapping-rain-water-ii/
---

Given a description of a landscape, describe how the rain water will drain.

# Problem statement

You are given a rectangular grid. Grid cells represent squares of a landscape.  Every grid cell `c` has an integer height, denoted `height[c]`.  It is raining, and water can drain to the border of the grid, following a path of grid cells with non-increasing height.  Compute for each grid cell, how much water is trapped above it.  (The actual problem asks only for the total amount.)

![Photo by Jan Egil Kristiansen]({{site.images}}trapped_rain.jpg){:width="600"}

# Reduction to a shortest path problem

When you see the word "flood", you might think that this is a flow problem. But it can be reduced to a variant of a shortest path problem. 

Consider a path `P` from some cell `c` to a border cell. Water above `c` can drain to the border along `P`.  Formally, if the water height above `c` exceeds stricty the maximum `height[d]` over all grid cells `d` in `P`, then this exceedend can drain along `P`.  This means that for every grid cell we wish to compute a path to the border minimizing the maximum height of the traversed cells. THis call this value the *height* of the path.  If this height is `k`, then the trapped water level above `c` is precisely `k`. 

This can be done by a variant of Dijkstra's algorithm, where instead of the addition of edge costs we use the maximum operator, and instead of having weights on the edges, we have weights on the edges.  The algorithm computes for every grid cell `c`, the trapped water level above it in a variable `water[c]`.  It uses a priority queue called `heap`, storing triplets. Each triplet consists of a cell coordinate and the maximum height of a discovered path from the border to this cell.

~~~python
from heapq import heappop, heappush, heapify


class Solution:    
        
    def sum_matrix(self, M):
        return sum(sum(row) for row in M)


    def trapRainWater(self, heightMap):
        rows = len(heightMap)
        cols = len(heightMap[0])
        R = range(rows)
        C = range(cols)
        water = [[None for j in C] for i in R]
        # initialize with border cells
        heap = [(heightMap[i][j], i, j) for i in R for j in C if 
                i == 0 or i == rows - 1 or j == 0 or j == cols - 1]
        heapify(heap)
        while heap:
            h, i, j = heappop(heap)
            if water[i][j] is None:
                water[i][j] = h
                for i2, j2 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= i2 < rows and 0 <= j2 < cols:
                        priority = max(h, heightMap[i2][j2])
                        heappush(heap, (priority, i2, j2))
        return self.sum_matrix(water) - self.sum_matrix(heightMap)
~~~



# Complexity

The complexity is linear in the grid size.
