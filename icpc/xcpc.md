---
layout: page
title: XCPC
parent: ICPC Training
grand_parent: Competitions
---

# XCPC

XCPC is a local selection contest at École Polytechnique.
Top 2 to 3 teams (with probability 1) from the contest will advance to [SWERC](https://swerc.eu/) to represent the school.

XCPC 2026 will happen on November 7 in computer rooms of X, from 1 PM to 6 PM.

## Registration

In order to participate, your team must be registered.
If you have attended PDV/MODAL course this year and you have a team, then you are registered.
If you have filled out the google form for XCPC/XCAIC registration or contacted Jill-Jênn Vie about it, then you are registered.
If you wish to register your team, contact jill-jenn.vie@inria.fr or manoprenko@gmail.com.

# XCPC regulations

We are following the [regulations of SWERC](https://swerc.eu/2026/regulations/). Main points and technical details are outlined below.

- Teams of up to 3 participants with **one** computer per team. All the teams will use computers of Polytechnique. Bringing your own computer or keyboard is forbidden. We can provide AZERTY keyboard on demand.
- Teams will be ranked according to the number of problems solved. We will break ties according to time penalty, that is, the sum of minute timestamps for solved problems, with a penalty of 20 min per failed attempt, only taken into account for solved problems.
- It is forbidden to use any electronic devices except your team's computer, <span style="color: red">including phones</span>, watches, AR glasses, etc.
- It is forbidden to access any online resources except the judging system and authorized offline documentation.
- It is forbidden to use search engines or <span style="color: red">any AI models</span>.
- It is forbidden to bring any written notes. Blank paper and writing tools are authorized.
- Teams are allowed to access and consult an offline version of [cppreference.com](https://cppreference.com/) and the team reference document. They can exceptionally copy paste from a clone of the KACTL repository.

## Programming languages

The following programming languages will be present in the judging system:

| Language | Version | Compilation command | Execution command |
| -------- | ------- | ------------------- | ----------------- |
| C | gcc 14.2.0 | gcc -x c -Wall -O2 -static -pipe "$@" -lm | ./"$@" |
| C++ | g++ 14.2.0 | g++ -x c++ -std=c++23 -Wall -O2 -static -pipe "$@" | ./"$@" |
| Java | OpenJDK 21 | javac -encoding UTF-8 -sourcepath . -d . "$@" | java -Dfile.encoding=UTF-8 -XX:+UseSerialGC -Xss64m -Xms{ML - 16m} -Xmx{ML - 16m}  "$@" |
| Kotlin | Kotlin 2.4.21 | kotlinc -d . "$@" | kotlin -Dfile.encoding=UTF-8 -J-XX:+UseSerialGC -J-Xss64m -J-Xms{ML - 16m} -J-Xmx{ML - 16m} "$@" |
| Python | PyPy3 7.3.19 | - | pypy3 "$@" |

All problems are guaranteed to have solutions in C++. There is no such guarantee for other programming languages.

## Team reference document

This part of regulations significantly differs from SWERC/WF.

Teams are allowed to use the provided [KACTL](https://github.com/kth-competitive-programming/kactl/blob/main/kactl.pdf) reference document.
It will not be printed and will be available in the testing system in pdf format.
Teams are authorized to consult this document and copy its content.

## Printing

We will try to provide a possibility of printing your solutions and other text files during the contest.
However, we cannot guarantee its availability during the contest.

# Advice

- Read the problem statements and check the constraints. Split the work with your team.
- Think on paper. You are encouraged to write on the problem statements (e.g. highlight constraints).
- Manage your time: solve the easy problem(s) as soon as possible.
- Every minute counts, so don't give up. If it's hard, it's hard for everybody.
- Build some testcases yourself.

## Common mistakes

- Do not forget `long long`
- Your code should have upper bounds that are high enough.
- Do not forget to clear your structures between two consecutive testcases.
