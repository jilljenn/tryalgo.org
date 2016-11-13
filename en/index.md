---
layout: page
title: Tryalgo posts ordered by date
---

See also our list [ordered by categories](categories).

{% for post in site.posts %}
  {% if post.layout == 'en' %}
  <div class="post">
            <h2>
          {{ post.title }}
        </h2>
    <p class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time></p>

        {{ post.excerpt }} ... <a class="post-link" href="{{ post.url }}">more</a>
     
  </div>
  {% endif %}
{% endfor %}

