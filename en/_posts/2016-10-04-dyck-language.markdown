---
layout: en
title:  "Dyck language"
category: strings
author: Christoph Dürr
problems:
   "spoj:Can you make it empty 2": http://www.spoj.com/problems/EMTY2/en/
---

Given a 01-string we have to decide in linear time if it can be obtained by starting with the empty word and repeatedly inserting the word 10 in an arbitrary position.

## The Dyck language

Just consider 1 as an opening parenthesis and 0 and a closing parenthesis. Then the problem consist in recognizing if the word is well parenthesized, in the sense that you can match opening to closing parenthesized and any two matchings are disjoint or nested.

## A variant

To make it more fun, consider the variant where we have to insert not the word 10 but the word 100.  Associate to each letter a score, the score of 1 is +2 and the score of 0 is -1.  Define the score of a word as the sum of the scores of its letters. By adding the scores of the letters along the word we obtain scores for each prefix of the string.

![]({{site.images}}make-it-empty.svg "The highest point corresponds always to a factor 100 in the string. Removing it preserves the condition that the score never becomes negative and ends at zero." ){:width="300"}

Now we claim that the word is in the language if and only if the score of every prefix is non-negative and the score of the whole string is zero.  For  one direction of the proof assume the word satisfies these conditions.  The key idea  is the observation that the prefix with the highest score corresponds to a factor in the word of the form 100.  Removing it preserves the conditions.  Eventually we end up with the empty word.

Clearly this condition can be checked in linear time with a single pass on the string.


