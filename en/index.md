---
layout: page
title: Tryalgo posts ordered by date
---

See also our list [ordered by categories](categories).

{% for post in site.posts %}
  {% if post.layout == 'en' %}
  <div class="post">
            <h2>
          <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
        </h2>
    <p class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%b %-d, %Y" }}</time>
        {% if post.problems %}
            <br>Related problem:
            {% for pb in post.problems %}
               <a href="{{ pb[1] }}">[{{ pb[0] }}]</a>
            {% endfor %}
        {% endif %}
    </p>

        {{ post.excerpt }}

  </div>
  {% endif %}
{% endfor %}

