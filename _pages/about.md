---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am Dongliang Cao, who is the PhD student at [University of Bonn](http://cs.uni-bonn.de/) under the supervision of [Prof. Florian Bernard](https://scholar.google.com/citations?user=9GrQ2KYAAAAJ) in the [visual computing group](https://lovc.cs.uni-bonn.de/). Before that I received my computer science Master's degree with distinction from the Technical University Munich (in 2022) and Bachelor's degree from  Zittau Görlitz University of Applied Sciences and Tongji University (in 2019).

My research interest is related to shape analysis, including shape matching, controllable shape generation, shape manipulation. If you have interest to collaborate with me, feel free to contact me. 


News
======
  <ul>{% for post in site.news reversed %}
    {% include archive-news.html %}
  {% endfor %}</ul>

Publications
======
{% for post in site.publications reversed %}
  {% assign currentdate = post.date | date: "%Y" %}
  {% if currentdate != date %}
<h3>{{ currentdate }}</h3>
    {% assign date = currentdate %}
  {% endif %}
  {% include archive-single-publication.html %}
{% endfor %}