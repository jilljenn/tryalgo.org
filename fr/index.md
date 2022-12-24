---
layout: page
title: Seulement en français
parent: Latest posts
---

# Billets en français

{% assign posts = site.posts | where:'layout', 'fr' %}

{% for post in posts %}
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
    <br>Problèmes liés :
      {% for pb in post.problems %}
        <a href="{{ pb[1] }}">[{{ pb[0] }}]</a>
      {% endfor %}
    {% endif %}
  </p>
  {{ post.excerpt }}
</div>
{% endfor %}
