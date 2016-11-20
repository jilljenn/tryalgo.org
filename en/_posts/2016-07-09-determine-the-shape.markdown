---
layout: en
title:  "Determine the shape"
category: geometry
problems:
   "uva:Determine the shape": https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2900
---

Given 4 points, place them in clockwise order and determine the shape formed by these points: square, rectangle, rhombus, parallelogram, trapezium or ordinary quadrilateral.


## Elementary tests

A point is represented as a tuple.  Given 3 points a, b, c we can ask if the walk a to b to c is a left turn.

![]({{ site.images }}left-turn.svg "Is the walk from a to b to c a left turn?"){:width="200"}

This is done by computing this simple expression.  Similarly we can test whether the segments a-b and b-c are perpendicular, or if two segments are parallel.  All these tests reduce to computing the determinant of some 2 by 2 matrix.

{% highlight python %}
def left_turn(a, b, c):
    """ is the path a->b->c oriented to the left ?
    """
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0]) > 0


def perpendicular(a, b, c):
    """is the segment a-b perpendicular to the segment b-c?
    """
    return (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1]) == 0


def parallel(a, b, c, d):
    """is the segment a-b parallel to the segment c-d?
    """
    return (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0]) == 0
{% endhighlight %}


## Sorting the points

We know that no 3 points of the given 4 points are co-linear. This means that the points are on their convex hull.
So we would like to place the points in such an order such that any 3 consecutive points form a left turn.  Let the points be p0, p1, p2 and p3.  We can do bubble sort to find the right order. First we test the orientation of p0, p1, p2 and swap p1, p2 if necessary.  Then we know that these 3 points are in order. We just need to find the correct position of p3, by comparing it with p2 and then p1.

{% highlight python %}
    for a, b in [(1, 2), (2, 3), (1, 2)]:
        if left_turn(p[0], p[a], p[b]):
            p[a], p[b] = p[b], p[a]
{% endhighlight %}

## Testing the shapes

To test the actual shapes, we first determine the lengths of the sides, tests if opposite sides are parallel and test if some angle is of 90 degrees.  Then we can test the conditions of the different shapes in reverse order of priority.  Note that for rectangles, once opposite sides have the same lengths it is not necessary to test all angles, one is enough.  Also note that we compare the squares of the lengths rather than the actual lengths, this avoids loss of precision due to the square root.

{% highlight python %}
    length = [ (p[i][0] - p[i-1][0])**2 + (p[i][1] - p[i-1][1])**2 for i in range(4)]
    parallel0 = parallel(p[0], p[1], p[2], p[3])
    parallel1 = parallel(p[1], p[2], p[3], p[0])
    angle90 = perpendicular(p[0], p[1], p[2])
    opp_sides_equal = length[0] == length[2] and length[1] == length[3]
    all_sides_equal = length[0] == length[2] == length[1] == length[3]
    #  -- determine shape in reverse priority order
    shape = "Ordinary Quadrilateral"
    if parallel0 or parallel1:
        shape = "Trapezium"
    if opp_sides_equal:
        shape = "Parallelogram"
    if all_sides_equal:
        shape = "Rhombus"
    if opp_sides_equal and angle90:
        shape = "Rectangle"
    if all_sides_equal and angle90:
        shape = "Square"
{% endhighlight %}

## Note

Our Python solution is too slow for the UVA judge.  The main problem could be the slow I/O of Python.

## References

- [C++ codes](http://geomalgorithms.com/code.html#Core-Classes)
- [basic cheat sheet](http://www.dummies.com/how-to/content/geometry-for-dummies-cheat-sheet.html)

