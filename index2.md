---
layout: default
title: Accueil
---

# Programmation efficace

128 algorithmes qu'il faut avoir compris et codés dans sa vie

    from algorithms import *       # import all you can eat

    try:
      problem = read(sys.stdin)    # needs organisation
      algo = solve(problem)        # needs skills
      solution = implement(algo)   # needs experience
      answer = submit(solution)
      assert answer == "Accept"
    except Submission_error:
      learn_more()
