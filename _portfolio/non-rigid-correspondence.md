---
title: "Non-Rigid Shape Correspondence"
excerpt: "<img width='50%' src='/images/previews/cao23siggraph.png'>"
collection: portfolio
---

## Publications

{% for post in site.publications reversed %}
  {% if post.categories contains 'correspondence' %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}
