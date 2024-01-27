---
layout: page
title: All posts by category
parent: Blog posts
---

# All posts by category

See also our list [ordered by date](..).

<ul>
{% assign sorted_cats = site.categories | sort %}
{% for category in sorted_cats %}
	{% if category[0] != "en" and category[0] != "fr" %}
		{% assign sorted_posts = category[1] | sort:'title' %}
		<li>{{ category[0] | capitalize }}
		<ul>
		  {% for post in sorted_posts %}
		    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
		  {% endfor %}
		</ul>
		</li>
	{% endif %}
{% endfor %}
</ul>
