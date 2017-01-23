---
layout: post
title: Advanced Git and GitHub - Ross Barnowski, Kyle Barbary, Katy Huff
comments: true
category: posts
tags: meeting git reproducibility
---

## Attending

- Anyone is welcome. We hope you'll join us!

## Meeting Info

- When: 4:00pm - 5:30pm
- Where: [BIDS, Room 190 of Doe Library](https://bids.berkeley.edu).
- Who: Anyone interested in software development best practices is welcome to come to our meetings.
- How: A predetermined main topic (45 minutes) will be followed by impromptu lightning talks (5 minutes each)

## Ross Barnowski

Ross is a graduate student in Kai Vetter's group in Nuclear Engineering. He has 
long hair. 

## Kyle Barbary

Kyle is a cosmologist and BIDS data science fellow. Kyle likes bicycles.

## Katy Huff

Katy is a nuclear engineer and BIDS data science fellow.

## Discussion: Advanced Git

We'll be talking about a bunch of cool git stuff. This will range from powerful
hacks everyone can use to awkward workarounds only a couple of people will ever
use. 



### Undoing Stuff

- git reset hard vs soft
- revert, why to revert, how to revert
- git stash and git stash pop
- getting a specific file from checkout 

      git checkout <branch> -- <file>


### Useful Configurations and Stuff

- show your current branch in the terminal prompt
- aliasing (very quick example with git config --global alias.unstage 'reset HEAD --')
- the [hub](https://github.com/github/hub) project to make interacting with github a little nicer (follows aliases nicely)
- Creating a template for git commit messages with 

      git config (git config --global commit.template ~/.gitmessage.txt)

- the mailmap, for normalizing the many possible commit names of your various contributors

### Dealing with Branches, Remotes, and Collaboration

- remotes
- setting up SSH keys 
- the DAG
- [git flow](http://nvie.com/posts/a-successful-git-branching-model/) for collaborating
- git tagging


### Rebasing

- rebasing 

### Specialized Knowledge

- cherry-picking a commit from one branch to another
- detaching a single subdirectory and its history from a big repo to make it its own repo
- the github api: futz with github from the command line

## Lightning Talks

Additionally, there will be a time for a couple of **Lightning Talks**, which are 
5-10 minute blasts of information about a particular topic or question of 
interest to the group.  This topic can be anything useful, new, or interesting 
to scientists who compute. It may be some new skill you have recently picked up 
in your research, a productivity tool you have recently learned to love, a 
quick demo of a useful library, or anything you feel we would enjoy learning.  
**Note** that the lightning talk time is a good way to bring a question to the 
group. If you have a bug you need help with, here's the place to ask many ears 
about it at once.  


### Name : Topic

Notes and links

### Name : Topic

Notes and links

## Hacky Hour  

Inspired by the hackers of
[Australia](http://thehackerwithin.github.io/swinburne/), we're taking this
opportunity to try out a Hacky Hour. After the meeting is over, folks can stick
around to review one another's code. This part of the meeting is meant to be
very casual, so feel free to pop open a beverage if you need to take the edge
off of the code reviews (byo).
