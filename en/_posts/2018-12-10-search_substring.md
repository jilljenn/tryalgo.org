---
layout: en
title:  "Searching a substring"
author: Christoph Dürr, Vincent Jugé and Samuel Tardieu
---

## Statement 

A basic problem in string algorithms is to locate a given substring `needle` in a given string `haystack`. Formally the goal is to find an index i such that the j-th character in `needle` is equivalent to the (i+j)-th character in `haystack`.

A naïve implementation would have worst case time complexity $\Theta(n m)$ where $n,m$ are the respective sizes of the given strings.  Here is a tight example.

> Given positive integer n, locate the string $a^nb$ in the string $a^{2n}$.

The naïve algorithm would try $\Theta(n)$ locations (candidates for the index $i$), compare the characters one by one and only at the end observe the inequality $a \neq b$ and realize a fail. Hence the naïve algorithm has running time $\Theta(n^2)$ on this example.

However there are algorthms of complexity $O(n + m)$, the most famous being Knuth-Morris-Pratt, see [Rechercher des mots dans un texte par l'algorithme de Knuth-Morris-Pratt](http://tryalgo.org/fr/2016/12/11/kmp/) or [tryalgo.knuth_morris_pratt](http://jilljenn.github.io/tryalgo/_modules/tryalgo/knuth_morris_pratt.html).

## Experiments

We did experiments in Java, Python and C++. The latter languages implement the linear time search algorithm, but Java implements the naïve quadratic time algorithm. This has been confirmed by looking at the [code](http://hg.openjdk.java.net/jdk7u/jdk7u6/jdk/file/8c2c5d63a17e/src/share/classes/java/lang/String.java#l1715) of the `String.indexOf(String)` method. Experiments have been done with various versions of Java, up to version 10.  Here is the code we used.

~~~java
class Test_str_find {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int n2 = 2*n;
        StringBuilder needle = new StringBuilder();
        StringBuilder haystack = new StringBuilder();
        for (int i=0; i<n; i++)
            needle.append('a');
        needle.append('b');
        for (int i=0; i<n2; i++) {
            haystack.append('a');
        }
        String s_needle = needle.toString();
        String s_haystack = haystack.toString();
        s_haystack.indexOf(s_needle);
    }
}
~~~

## Workaround

In Java however there is the possibility to search a regular expression in a given string, and this implementation is efficient. Hence you can use it to search for a substring.  The following code has linear time complexity.

~~~java
public int my_indexOf(String needle, String haystack) {
    Pattern p = Pattern.compile(String.quote(needle));
    Matcher m = p.matcher(haystack);
    if (m.find()) 
        return m.start();
    else
        return -1;
}
~~~