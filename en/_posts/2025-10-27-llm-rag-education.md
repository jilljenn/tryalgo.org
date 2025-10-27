---
layout: en
title: LLMs and RAG in education
author: Jill-Jênn Vie
excerpt_separator: <!--more-->
---

This summer, I was in Palermo where the Educational Data Mining, Learning at Scale & AI in Education conferences were held.

I presented Anav Agrawal's RAG tool, which we use in our course.

> Anav Agrawal, Jill-Jênn Vie. AlgoAce: Retrieval-Augmented Generation for Assistance in Competitive Programming. CSEDM 2025 - 9th Educational Data Mining in Computer Science Education Workshop, Jul 2025, Palermo, Italy. [[paper]](https://hal.science/hal-05089333) [[code]](https://github.com/AnavAgrawal/AlgoAce/)

I'll tell you about what some colleagues from Cornell University and Berkeley University presented because it's truly impressive.

## Cornell

The professor (Rene Kizilcec) has 270 students.  
He uploads his PDFs to some website [hita.ai](https://www.hita.ai) developed by former students.  
Students can ask questions anonymously (it sources the answers to the pages of the course slides or to specific points in a course video) and the professor sees the anonymous conversations (this part is the most valuable).  
He has automatic analytics on the most frequently asked questions.  
The (6k?) students have asked 64k questions on the platform (local LLM) in a few years.  
The professor uses it to verify that students are actually reading the articles he assigns (students have to debate a question with an AI that has read the article).

He told the anecdote that his colleague noticed that 5 students were cheating and told them: "Wow, I'm really impressed by the richness of your reasoning, how about you come and discuss it in my office?" and then the students said "Nooo, sorry, we cheated."

## Berkeley

Narges Norouzi has 900-1700 students per cohort in their first CS1 course, required for all students in the computer science and engineering departments.  
Students are allowed to use an autograder for their homework but not for graded labs or projects <https://sp25.datastructur.es/policies/> see also, from a different u, <https://eecs-autograder.github.io/autograder.io>  
They reuse the (1 million) code submissions from students over the previous (7) years to help students debug, see what types of hints are useful, which directly feeds into their (the professors') research. They have 105,000 queries from 2,000 students from the 2023-2024 academic year to their local LLM.  
They are not allowed to conduct randomized controlled trials; their ethics committee (IRB) prohibits it, due to the impactness of this course and its scale.  
They show that students complete homework faster with AI (unsurprisingly) but not practical assignments faster (they even have some negative results on practical assignments).  
They had two papers nominated for best paper at AIED 2025 (below), one of which uses the curriculum to automatically determine students' progress in the course (knowledge tracing) and make appropriate recommendations.

> Modeling Student Knowledge Progression in Intelligent Tutoring Interactions
Abigail O’Neill, Kanav Mittal, Hanna Schlegel, Gireeja Ranade and Narges Norouzi <https://drive.google.com/file/d/1As0EAEXOeyTnDqaMCOQqYY__BaN_d9gq/view?usp=sharing>

> Askademia: A Real-Time AI System for Automatic Responses to Student Questions
Gaurav Tyagi, Meenakshi Mittal, Azalea Bailey, Gireeja Ranade and Narges Norouzi <https://drive.google.com/file/d/1TOAuYZutWz8IWmWj_NLneL8atbUEcoVK/view?usp=drive_link>
