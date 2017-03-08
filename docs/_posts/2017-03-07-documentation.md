---
layout: post
title: Documentation and Continuous Integration in Python with Sphinx and Travis CI -- Nelle Varoquaux, Chris Holdgraf, Matthias Bussonnier
comments: true
category: posts
tags: meeting
---

# Documentation and Travis

Welcome to this special session the The Hacker Within Berkeley which will take
place at the usual BIDS location but during the
[Docathon](https://bids.github.io/docathon) event that span the week of March 6
to 10.

During the Talks on Monday 6th, you had a quick overview of Sphinx, RMarkdown,
and how [Travis-Ci](https://travis-ci.org) can be used to deploy documentation.

Today we'll get our hands dirty and try to deploy this ourself using GitHub,
Travis, and GhPages on our own, as well as describe what to do (and not to do)
when doing so. 


## Requirements

The requirements are minimal and the time of the Hacker Within session should be
enough to get them, though, getting these in advance will help to follow along.

- get a GitHub account
- Login on Travis-CI with your GitHub

If possible:

  - install the `travis` ruby gem on your machine (`$ gem install travis` should
    be enough)
  - have [doctr](https://github.com/drdoctr/doctr) installed on your local
    machine.


## High level overview

Understanding how to deploy documentation from Travis requires a minimal
understanding on how Travis works.

In particular we will discuss the safe ways to store credentials in the
`.travis.yml` file, what do to, not to do, when these credential get decrypted
and when they are not. 

We'll setup a repository that deploy itself on GitHub pages when pushed on
master.




