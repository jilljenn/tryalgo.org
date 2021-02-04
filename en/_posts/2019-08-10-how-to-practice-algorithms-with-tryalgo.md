---
layout: en
title:  "How to practice algorithms with tryalgo"
category: miscellaneous
author: Jill-Jênn Vie
---

Hey, if you want to improve your skills in algorithmic problem solving, you don't even need an online judge!

In the [tryalgo repository](https://github.com/jilljenn/tryalgo), we have provided [tests for 128 classic algorithms](https://github.com/jilljenn/tryalgo/blob/master/tests/test_tryalgo.py).

## Howto

First, clone the [tryalgo](https://github.com/jilljenn/tryalgo) repo.

    $ git clone https://github.com/jilljenn/tryalgo
    $ cd tryalgo

Then check that the tests pass:

    $ python3 -m unittest
    ...........................................................................................
    ----------------------------------------------------------------------
    Ran 91 tests in 2.570s

    OK

If you want to practice [union of rectangles](https://jilljenn.github.io/tryalgo/content.html#geometry) for example, open [`tryalgo/union_rectangles.py`](https://github.com/jilljenn/tryalgo/blob/master/tryalgo/union_rectangles.py) and DELETE[^1] the content of the algorithm.

```python
def union_rectangles(R):
    """Area of union of rectangles

    :param R: list of rectangles defined by (x1, y1, x2, y2)
       where (x1, y1) is top left corner and (x2, y2) bottom right corner
    :returns: area
    :complexity: :math:`O(n^2)`
    """
    # OMG I am so deleted, doushiyou
```

The tests should fail now.

    $ python3 -m unittest
    .........................................................................................F.
    ======================================================================
    FAIL: test_union_rectangles (tests.test_tryalgo.TestTryalgo)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/jilljenn/code/tryalgo/tests/test_tryalgo.py", line 1582, in test_union_rectangles
        self.assertEqual(union_rectangles([]), 0)
    AssertionError: None != 0

    ----------------------------------------------------------------------
    Ran 91 tests in 2.939s

    FAILED (failures=1)

Rewrite that algorithm the best you can, until the tests pass.

Enjoy!

You can also write your own tests in [tests/test_tryalgo.py](https://github.com/jilljenn/tryalgo/blob/master/tests/test_tryalgo.py), and potentially [create a PR](https://github.com/jilljenn/tryalgo/pulls) if you find a corner case that we did not think about!

 [^1]: Don't be afraid to break everything, this is a git repository so everything is versioned; if you want to recover the initial file (and know the solution), you can do:

        $ git checkout tryalgo/union_rectangles.py
