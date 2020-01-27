---
layout: en
title:  "Constraint Programming"
author: Christoph Dürr and students from the Ecole Centrale-Supélec, France
---

## The framework

[Constraint programming](https://en.wikipedia.org/wiki/Constraint_programming) is a programming paradigm, which consists of variables and constraints. The goal is to assign values to variables, which satisfy all constraints.  Such an assignment is found via the exploration of a search tree, using variuous prunning rules and search heuristics.

## Our solver

We propose a very basic solver in Python, for the purpose of illustrating the basic concepts.  Do not expect good performances.
It consists of a class called `CSP_Problem`, providing roughly 3 methods: the constructor, a method to add constraints, and a method to find a solution.

Variable names can be any hashable object, integers, strings, or tuples for example.  The domain of each variable is a set of values, which the variable can take.  The constructor takes as argument a dictionnary, where keys are the variable names and the values their domains.

Our class accepts only *binary* constraints, which means that you can force constraints on pair of variables.  This should be enough for most simple projects and keeps the code very simple. The class method `add_constraint(x, y, rel)` takes as argument two variable names `x`  and `y`, as well as a relation `rel`. The relation is simply a set of value pairs of the form `(u,v)` such that assigning `x:=u, y:=v` is valid for this constraint.

Once all constraints are added to the problem, the user can call the method `solve`, which tries to find an assignement of values to variables, satisfying all constraints. If it succeeds it returns a dictionnary, associating to each variable name a value.  In case of failure the return value is `None`.

In addition, the class provides an [iterator](https://pymbook.readthedocs.io/en/latest/igd.html) called `solve_all`, which iterates over all solutions to the problem.

## Disclaimer

The purpose of our solver is to illustrate the principles of constraint programming, and is designed to keep the code simple and short. It is therefore not as efficient as other available constraint programming libraries.


## Examples

A technical detail: During the solving process, our solver modifies the domains of the variables. Therefore it is important that each variable has its own domain object.  This is why the examples below use the function `set` to ensure that every variable has its own copy of the domain.  This restriction applies only to variables, it is perfectly ok for constraints to share the same relation object.

### The n-Queens Problem

You are given an n by n checker board and required to place n queens, such that they cannot attack each other.  The [wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle) page gives more information about this problem.  A simple model for this problem consists of n variables, numbered from 0 to n-1, each having the domain {0,...,n-1}. The i-th variable having value j would mean that there is a queen in row i and column j.
Now for every pair of rows i and k, there is a constraint, which forbids attacking positions of the queens.

~~~Python
# this example fixed n to 8
N = range(8)
P = CSP_Problem({x: set(N) for x in N})
for y in N:
    for x in range(y):  # don't add same constraint twice
        P.add_constraint(x, y, {(u, v) for u in N for v in N if u - v not in [x - y, 0, y - x]})
sol = P.solve()
# pretty print the solution
for i in N:
    for j in N:
        if sol[i] == j:
            print("# ", end='')
        else:
            print(". ", end='')
    print()
~~~

### Sudoku

You are given a 8 by 8 integer matrix, where zeros represent empty cells. The goal is to fill all empty cells with integers 1 to 8, such that two cells in a same row, same column or same block have different values.

~~~Python
grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0],
]
N = range(8)            # row and column indices
domain = range(1, 9)    # 1..8 = domain of variables
var = {(i, j): set(domain) for i in N for j in N}
# set variables for prefilled cells to singleton sets
for i in N:       
    for j in N:
        if grid[i][j]:                    # prefilled ?
            var[i, j] = {grid[i][j]}      # singelton set
P = CSP_Problem(var)
# relation 
different = {(u, v) for u in domain for v in domain if u != v}
# add constraints for pair of cells in same row, column or block
for (i1, j1) in var:
    for (i2, j2) in var:
        if i1 == i2 or j1 == j2 or (i1 // 3 == i2 // 3 and j1 // 3 == j2 // 3):
            P.add_constraint((i1, j1), (i2, j2), different) 
sol = P.solve()
# print solution
for i in N:
    for j in N:
        print(sol[i, j], end=' ')
    print()
~~~

## Technical explanation

### Depth first exploration of a search tree

The solver consists of a depth first exploration of a search tree. Every node corresponds to a partial solution, i.e. a subset of variables are assigned to a value. The remaining variables are said to be still *free*.  Of course the assigned variables must satisfy that any pair of them linked by a constraint are assigned to values satisfying this constraint.

The root of the search tree consists of the *empty assignement*, where all variables are free.  There are two kind of leafs in the tree:  *Solution nodes*, in which all variables are assigned, and *non-solution nodes*, in which there is a free variable, which has an empty domain.

The tree is build and explored in the following recursive manner. When the solver processes a node it starts by selecting a free variable x. Several heuristics are possible here, we choose to select a free variable with the smallest domain (explanation below). Now for every value u in the domain of x, we build a new node of the tree, extending the current assignement by setting x:=u.  Again several heuristics are possible here on the order in which the values of the domain are processed, we choose to loop in an arbitrary order for simplicity.  Before exploring recursively the new node, some constraint propagation is done, which is explained below.


### Selection heuristics of a free variable


The idea is that if this current partial assignment cannot be extended to a complete solution, then we would like to find this out quickly, for example by reducing the domain of a free variable


The exploration of the tree works as follows. The solver starts with the root node

in the sense that some variables are assigned to values, with the property that any two assigned variables satisfy a possibly constraint

For a given constraint on variables x and y, we define the support of a value u in the domain of x as the set of all values v in the domain of y, such that assigning x:=u, y:=v satisfies the constraint.