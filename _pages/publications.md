---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <a href="https://scholar.google.com/citations?user=HR0bpvsAAAAJ">my Google Scholar profile</a>.

{% for post in site.publications reversed %}
  {% assign currentdate = post.date | date: "%Y" %}
  {% if currentdate != date %}
<h3>{{ currentdate }}</h3>
    {% assign date = currentdate %}
  {% endif %}
  {% include archive-single-publication.html %}
{% endfor %}