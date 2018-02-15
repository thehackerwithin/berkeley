---
layout: layout
title: "About"
---

<!-- You can edit this whole page, remove it, or use it as basis for any non-post pages you have. -->
<section class="content">

# The {{ site.name }}, {{ site.chapter }}

<b>Spring 2018 is here!</b>

<ul class="listing">
<li>
<span>Spring 2018</span><a href="{{ site.url }}/upcoming.html">Upcoming Topics</a>
</li>
  {% assign upcoming = (site.posts | where: "category" , "upcoming") %}
  {% for post in upcoming reversed %}
    {% if forloop.first %}
	<li style="text-indent: 2em;">
		<span>{{ post.date | date: "%B %e, %Y" }}</span> Next topic: <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
	</li>
    {% endif %}
  {% endfor %}
<li>
<span>2014-2017</span><a href="{{ site.url }}/previous.html">Previous Topics</a>
</li>
</ul>

## What:

This is a weekly peer learning group for sharing skills and best practices for
research computing and data science. In these friendly sessions, peers at all levels
of experience share topics useful in our data analysis and software development
workflows.

This meeting would be a great venue for introducing new libraries,
showing off useful features of a data processing/analysis/visualization library or programming
language you're using, or bringing up a computational problem you're
having.

## Who:

Anyone interested how to learn and do things by programming computers is welcome to come to our meetings. You don't need to be affiliated with UC-Berkeley and you don't need to come every week. There is no set of prerequsites, although we frequently use bash and the command line, python, R, GitHub, and Jupyter notebooks.

## Where:

We meet at the [Berkeley Institute for Data Science](https://bids.berkeley.edu). Room 190, Doe Library, The University of California - Berkeley. It is on the ground floor of the main library. If you walk up the big marble steps across Memorial Glade, then turn left right as you walk in, you'll be there!

## When:

Wednesdays at 5pm (Berkeley time -- starting officially at 5:10, but have a friendly chat from 5:00-5:10 if you like). While the main session should occupy less than an hour, the
lightning talks and hacking session usually go on until 6:30pm. See the [upcoming topics list]({{ site.url }}/upcoming.html)
or the [calendar](http://bit.ly/1cqFKuh)
for the topic for this week.

## How:

### Communications
* [Mailing list](https://groups.google.com/a/lists.berkeley.edu/forum/#!forum/ucb-hacker-within)
* [Slack channel](http://thehackerwithin.slack.com) if you've got an account
  * [Go here to get an invite to the slack channel](http://theslackerwithin.herokuapp.com) -- invite token "berkeley"

### Participating:

Participating is really easy.
<ul>
<li>At **5:00pm**, we gather and go through a round of introductions.
New faces are always appearing!</li>
<li>Next, a volunteer will give a **tutorial** or lead a
**discussion** about a
computational topic. This topic can be anything useful, new, or
interesting to scientists who compute. It may be some new skill you have recently picked
up in your research, a productivity tool you have recently learned to love, an overview of a
useful library, or anything you feel we would enjoy learning.</li>
<li>Finally, there will be a time for a couple of **Lightning Talks**, which
are 5-10 minute blasts of information about a particular topic or
question of interest to the group.
**Note** that the lightning talk time is a good way to bring a
question to the group. If you have a bug you need help with, here's the
place to ask many ears about it at once.
</li>
</ul>

## Why:

The tenets of scientiﬁc endeavor (e.g., data control, reproducibility,
comprehensive documentation, and peer review) suffer in projects that fail
to make use of current development tools such as unit testing, version
control, automated documentation, and others.

To avoid these pitfalls, this weekly meeting exists for sharing skills and best practices for
computational scientific applications. This group is modeled after The
Hacker Within, which  began as a student organization at the University of Wisconsin-Madison and
is now reborn as a collection of such chapters around the world. Each of
the chapters convenes a community of scientists, at all levels of their
education and training, to share their knowledge and best practices in
using computing to accomplish their work.

<a href="http://twitter.com/share" class="twitter-share-button" data-count="none" data-via="{{ site.twitter }}">Tweet</a>
<a href="http://twitter.com/{{ site.twitter }}" class="twitter-follow-button" data-show-count="false">Follow @{{ site.twitter }}</a>
<script src="http://platform.twitter.com/widgets.js" type="text/javascript"></script>
</section>
