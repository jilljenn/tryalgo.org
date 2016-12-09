---
layout: en
title:  "Traffic Jam"
category: shortest-paths
author: Christoph Dürr
problem_urls:
    "poj:Traffic Jam": http://poj.org/problem?id=1817
    "tju:Traffic Jam": http://acm.tju.edu.cn/toj/showp2272.html
---

Given a grid containing some segments, find the minimum number of times segments need to be displaced such that a particular segment can escape from the grid.

## A shortest path problem in the configuration graph

We model the problem as follows.  On the given 6 by 6 grid are placed n vehicles.  Vehicles are numbered starting from 0, 0 being the special vehicle which has to escape the grid.  Each vehicle has a width equal to 1 and length 2 or 3 grid cells.  It can be placed horizontally or vertically.  Its location is identified by the coordinate of its left most upper most cell.  Depending on the vehicle orientation one of the coordinates is fixed, while the other one can vary.  We define a *configuration* as the vector consisting of the variable coordinates of the vehicles.


![]({{site.images}}RushHour.svg "Example of a configuration" ){:width="400"}

For example the previous configuration would be encoded as follows.

```python
# vehicle     0     1      2     3      4      5     6     7     8
horizontal = [True, False, True, False, False, True, True, True, False]
length =     [2,    2,     3,    3,     2,     2,    3,    2,    2]
fixcoor =    [2,    0,     0,    4,     2,     3,    3,    4,    5]
config =     (0,    0,     1,    0,     2,     4,    2,    3,    4)
```

Now in one step a single vehicle can be displaced, which consists in changing one coordinate of the configuration vector.
This describes some underlying graph, where configurations are vertices and there is an edge between configurations A and B if B can be obtained from A in one step.  The goal is to find a shortest path from the initial configuration to a target configuration (which is one where vehicle 0 reaches the border of the grid).  This can be done by simple BFS traversal of the graph.  The only new part here is that the graph is only implicitly given.

The BFS search on an implicitly given graph uses a function `graph` which maps a vertex to a list of neighboring vertices in the graph.  It also needs a function `is_target` to check if with a given vertex the traversal is completed.

```python
def bfs_implicit(graph, start, is_target):
    dist = {start: 0}
    to_visit = deque([start])
    while to_visit:
        node = to_visit.pop()
        for neighbor in graph(node):
            if neighbor not in dist:   # new vertex
                dist[neighbor] = dist[node] + 1
                to_visit.appendleft(neighbor)
                if is_target(neighbor):
                    return dist[neighbor]
    return None   # target is not reachable
```

So for this problem we have to start building the data structures from the given intial grid. This is done as follows by inspecting the grid on row wise order. As you can see this is the longest path of the code.

```python
def read(grid):
    """ reads the grid and builds the data structure.
    returns current configuration
    """
    global horizontal, fixcoor, length
    row = [-1] * n                             # first coordinates seen of a vehicle
    col = [-1] * n
    horizontal = [None] * n                    # create data structures
    length = [None] * n
    for i in range(dim):                       # loop over all grid cells (i,j)
        for j in range(dim):
            c = grid[i][j]
            if c != '.':
                if c == 'x':                   # determine vehicle index from character
                    v = 0
                else:
                    v = ord(c) - ord('a') + 1
                if row[v] == -1:               # first time vehicle is seen
                    row[v] = i
                    col[v] = j
                    length[v] = 1
                else:                          # rest of the vehicle
                    horizontal[v] = (row[v] == i)
                    length[v] += 1
    fixcoor = []
    config = []
    for v in range(n):                         # set fixed coordinate
        if horizontal[v]:
            fixcoor.append(row[v])
            config.append(col[v])
        else:
            fixcoor.append(col[v])
            config.append(row[v])
    return tuple(config)                       # current configuration
```

Finally to encode the graph, we just need to implement the neighbor oracle function and the target oracle test.  For those we need a helper function that verifies if in a given configuration a given cell is occupied by some vehicle.

```python
def occupied(config, r, c):
    """returns if cell (r,c) is occupied in the given configuration
    """
    if not( 0 <= r < dim and 0 <= c < dim):    # cells around the grid are occupied
        return True
    for v in range(n):             # is vehicle v covering cell (r,c)?
        if (horizontal[v] and fixcoor[v] == r and config[v] <= c < config[v] + length[v] or
          not horizontal[v] and fixcoor[v] == c and config[v] <= r < config[v] + length[v]):
            return True
    return False


def is_target(config):
    return config[0] == dim - length[0]


def graph(config):
    """iterates over all reachable configurations from the given one
    """
    for v in range(n):           # loop over all vehicles
        if horizontal[v]:
            # right
            d = 1
            while not occupied(config, fixcoor[v], config[v] + d + length[v] - 1):
                yield config[:v] + (config[v] + d, ) + config[v+1:]
                d += 1
            # left
            d = 1
            while not occupied(config, fixcoor[v], config[v] - d):
                yield config[:v] + (config[v] - d, ) + config[v+1:]
                d += 1
        else:
            # down
            d = 1
            while not occupied(config, config[v] + d + length[v] - 1, fixcoor[v]):
                yield config[:v] + (config[v] + d, ) + config[v+1:]
                d += 1
            # up
            d = 1
            while not occupied(config, config[v] - d, fixcoor[v]):
                yield config[:v] + (config[v] - d, ) + config[v+1:]
                d += 1
```

We can verify in a quick and rough estimation that the overal running time is acceptable.  A configuration consists of a vector of dimension at most 10 and there are 5 choices for each vector element.  This gives an upper bound of \\( 5^{10} < 2^{24} \\) vertices.  But the actual number must be much smaller since most of the configuration vectors would not be valid by overlapping vehicles.  The number of neighbors of a configuration can also be bounded by \\(5\cdot 10\\). Hence we can estimate the BFS to terminate within a few million operations.
