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
        {% if post.problem_url %}
        <br>Related problem: <a href="{{ post.problem_url }}">[{{ post.problem_name }}]</a>
        {% endif %}
        {% if post.problem_urls %}
            <br>Related problems:
            {% for url in post.problem_urls %}
               <a href="{{ url }}">[{{ url }}]</a>
            {% endfor %}
        {% endif %}
    </p>

        {{ post.excerpt }}

  </div>
  {% endif %}
{% endfor %}

