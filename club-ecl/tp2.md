---
layout: page
title: Shortest paths in Paris
parent: Problems
---

Today we're visualizing graph algorithms on Paris.  
Then you'll have to validate at least one problem.

## Paris graph [Jupyter notebook](https://github.com/jilljenn/tryalgo/blob/master/examples/TryAlgo%20Maps%20in%20Paris.ipynb)

Question 0
:	
A drunkard is making a random walk in Paris. What does it look like?

You can visualize using matplotlib `plt.scatter` with a different color `c='r'` or Folium.

Question 1
:	
Compare a shortest path between two points by walk and by car. Plot both paths.

When we are walking, we can take both sides of the street; and the cost is the length. When we are traveling by car, we have to respect the sides given in the dataset, and the cost is the duration.

Question 2
:	
RATP is asking you to build metro lines that connect any two points of Paris. Cost of digging a line is proportional to its length. What should you do?

Question 3
:	
We want to visit every station of Paris exactly once while walking as few as possible. Write an algorithm for this.

{% highlight python %}
stations = [
    "Gare d'Austerlitz",
    "Gare de Bercy",
    "Gare de l'Est",
    "Gare de Lyon",
    "Gare Montparnasse",
    "Gare du Nord",
    "Gare Saint-Lazare"
]
{% endhighlight %}

## Problems

- [Is it a tree](https://www.spoj.com/problems/PT07Y/)
- [Flowery Trails](https://www.spoj.com/problems/SWERC14B/)
- [Herding](https://www.spoj.com/problems/HERDING/)
- [Cleaning Robot](https://www.spoj.com/problems/CLEANRBT/)
