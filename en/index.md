---
layout: page
title: Most recent 8 posts
---

See also all posts [ordered by categories](categories).

{% for post in site.posts limit:8 %}
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

