---
layout: page
title: Blog posts
lang: en
has_children: true
nav_order: 5
---

# Latest posts

See also all posts [ordered by category](/blog/categories) or [date](/blog).

{% for post in site.posts limit:10 %}
<div class="post">
  <h2>
    <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
  </h2>
  <p class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time>
    {% if post.category %}
      • <span itemprop="category">{{ post.category }}</span>
    {% endif %}
    {% if post.author %}
      • <span itemprop="author">{{ post.author }}</span>
    {% endif %}
    {% if post.problems %}
    <br>Related problems:
      {% for pb in post.problems %}
        <a href="{{ pb[1] }}">[{{ pb[0] }}]</a>
      {% endfor %}
    {% endif %}
  </p>
  {{ post.excerpt }}
</div>
{% endfor %}
