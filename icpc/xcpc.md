---
layout: page
title: XCPC
parent: ICPC Training
grand_parent: Competitions
---

# XCPC

XCPC is a local selection contest at École Polytechnique.
Top 3 teams from the contest will advance to [SWERC](https://swerc.eu/) to represent the school.

XCPC 2026 will happen on November 7 in computer rooms of X.

## Registration

In order to participate, your team must be registered.
If you have attended PDV/MODAL course this year and you have a team, then you are registered.
If you have filled out the google form for XCPC/XCAIC registration or contacted Jill-Jênn Vie about it, then you are registered.
If you wish to register your team, contact jill-jenn.vie@inria.fr or manoprenko@gmail.com.

# XCPC regulations

We are following the [regulations of SWERC](https://swerc.eu/2026/regulations/). Main points and technical details are outlined below.

## TBD

## Programming languages

The following programming languages will be present in the judging system:

| Language | Version | Compilation command | Execution command |
| -------- | ------- | ------------------- | ----------------- |
| C | gcc 14.2.0 | gcc -x c -Wall -O2 -static -pipe "$@" -lm | < executable > |
| C++ | g++ 14.2.0 | g++ -x c++ -std=c++23 -Wall -O2 -static -pipe "$@" | < executable > |
| Java | OpenJDK 21 | javac -encoding UTF-8 -sourcepath . -d . "$@" | java -Dfile.encoding=UTF-8 -XX:+UseSerialGC -Xss64m -Xms{ML - 16m} -Xmx{ML - 16m}  "$@" |

=== Everything below is irrelevant ===

# XCPC rules
{: .no_toc }

- 7 problems, 3 hours, teams of 2 or 3 with 3 computers.
- It is mandatory to submit solutions in C++.
- You can use Python for generating testcases, for example.
- Please create an account on [Kattis](https://open.kattis.com).
- You have to use the computers provided in the lab.  
To get your AltGr key back, go to Settings > Keyboard > Alt/Compose > choose "Right Super" for example. To change layout, open a Terminal and do `setxkbmap us` or `setxkbmap fr`.

- You have to use the provided [KACTL](https://github.com/kth-competitive-programming/kactl/) notebook, that won't be printed.

```
git clone https://github.com/kth-competitive-programming/kactl.git
```

It's okay to copy-paste code from this repository only.  
Template is in [`content/contest/template.cpp`](https://github.com/kth-competitive-programming/kactl/blob/main/content/contest/template.cpp).

- It's okay to have a config file or macros but please show them to the coach.
- You cannot use Google, LLMs or anything else besides the notebook. But you can browse [cppreference.com](https://cppreference.com/).

## Advice

- Read the problem statements and check the constraints. Split the work with your team.
- Think on paper. You are encouraged to write on the problem statements (e.g. highlight constraints).
- Manage your time: solve the easy problem(s) as soon as possible.
- Every minute counts, so don't give up. If it's hard, it's hard for everybody.
- Build some testcases yourself.

## Common mistakes

- Do not forget `long long`
- Your code should have upper bounds that are high enough.
- Do not forget to clear your structures between two consecutive testcases.
