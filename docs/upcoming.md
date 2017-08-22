---
layout: layout
title: "Upcoming Topics"
---

<section class="content">

Upcoming Topics
===============

**Fall 2017**

The Hacker Within will resume for Fall 2017 on Wednesday, September 6th at 4pm in the Berkeley Institute for Data Science.

In addition to these topics, Lightning Talks are welcome at the end of every session, so please don't hesitate to bring some tidbit to share. Also, if you would like to contribute to a topic, contact the volunteer in charge of that topic to see if they would like to collaborate.

<ul class="listing">
  {% assign upcoming = (site.posts | where: "category" , "upcoming") %}
  {% for post in upcoming reversed %}
  <li>
  <span>{{ post.date | date: "%B %e, %Y" }}</span> <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
</section>
