---
layout: post
title:  "Translate between Java and C++  style identifiers"
category: strings
author: Christoph Dürr
---

Java style  identifiers consist of lower and upper case letters, starting with lower cases. C++ style identifiers consist of lower case letters and the underscore sign.  Given a word you should detect its style and translate it into the other style, or produce the string "Error!" if it not in one of the styles. See [Java vs C ++](http://www.spoj.com/problems/JAVAC/en/).

## A linear time algorithm

It is based on a finite state automaton, that we depict here. The algorithm processes the letters of the string in order, and according to the current state possibly produces some string and moves to another state.

![]({{site.images}}java-vs-c++.svg "The finite state automaton solving the problem. Transitions which are not depicted all lead to a trash state that corresponds to producing the string ERROR." ){:width="700"}


{% highlight java %}
import static java.lang.Character.*;


class Main {

    static final int JAVA=0, CPP=1, UNDER=2, NONE=3, FIRST=4;

    static String translate(String s) {
    StringBuffer r = new StringBuffer();
    int state=FIRST;
    for (char c: s.toCharArray()) {
        if (c=='_')
        switch (state) {
        case JAVA:
        case FIRST:
            return "Error!";
        case NONE:
        case CPP:
            state = UNDER;
            break;
        case UNDER:
            return "Error!";
            // nothing to do
        }
        else if (isUpperCase(c))
        switch (state) {
        case FIRST:
            return "Error!";
        case NONE:
            state = JAVA;
            // pas de break expres
        case JAVA:
            r.append("_"+toLowerCase(c));
            break;
        case CPP:
        case UNDER:
            return "Error!";
        }
        else // c is a lower case letter
        switch (state) {
        case FIRST:
            state = NONE;
            // pas de break expres
        case UNDER:
            r.append(toUpperCase(c));
            state = CPP;
            break;
        default:
            r.append(c);
        }
    }
    if (state==UNDER)
        return "Error!";
    else
        return ""+r;
    }

    public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    System.out.println(translate(in.next()));
    }
}
{% endhighlight %}



