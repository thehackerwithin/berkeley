---
layout: post
title: Git and GitHub -- Ciera and Matthias
comments: true
category: upcoming
tags: meeting git h2g2 backtothefuture github rickandmorty xkcd cthulhu
---


## Introduction to Git and GitHub

Wether you are lost in the woods trying to save a bear cub stuck in a tree, or
defending earth against alien invasion, [git][gitscm] is a tool of
choice to collaborate and save your progress to come [back in time][backtothefuture] and save the
day again if needed. 

Though using git (and GitHub) can be quite intimidating or look like dark magic.
We will gently introduce you to simple git concept, from [Just memorize these shell commands][xkcd],
to some dark voodoo allowing you to do a [66 way Cthulhu merge][octopus].

We will learn wether or not Linus Torvald (Git Creator) actually said the
following statemnts [or not][satirical], and wether the following statement have
a bit of truth in them:

> "all meaningful operations can be expressed in terms of the rebase command"

> [git is] so hard to use, but that turns out to be its big appeal

It is true that [actual manual page][man], can be hard to distinguish from [markov-chain text][fake-man], but you probably don't need to dive into it now.

## What we'll do

### The basics

We'll start pretty soft. Make sure you have git installed, and that it works.

We'll make sure you know the basics to already use git on your own, and to be ready to collaborate.

- Clone a repository
- Fork a GitHub repository
- Create a repository from scratch.
- Make a commit
- Make a branch
... 
- Create a Pull request on GitHub
- Update your local repository.

### DON'T PANIC

Even if it looks insanely complicated to operate and and partly to keep intergalactic travelers from panicking we'll discuss what to do when things go south.

Long story short, keep calm and ``commit -A`` (and `push`) if you are really scared. Nothing is ever lost.

What happen in case of broken whatever ? If you are in "Detached head state", "merge conflict", or anything else ? We got you covered !

### Advanced tactics !

Narrow down a bug ? Let's bisect. Want to hide your mistakes ? rebase/amend.
Have erased a mistake from history that was not a mistake ? reflog to the
rescue.

### Blips and Chitz !

Git is no fun without all the configuration option and tricks that make your life easier.

Checkout a PR by it's number ? oowee! 
Diff words instead of lines ? Can doooo !
Local and global gitignore ? Sure !

## Requirement

### Git

Try to have git installed on your laptop before coming to the hacker within.
If you are on windows we recommend git-bash, which should be bundled with [GitHub for Desktop][githubfordesktop].

Git should be bundled on recent Macs, you can also install it with [GitHub for Desktop][githubfordesktop], or [Homebrew](https://brew.sh).

User of linux probably already have git installed as well , or know how to install it with your favorite package manager.

### GitHub

Create a GitHub account on https://github.com setup credentials not to always have to enter your password.

## Resources

You can [train][trygithub] in your browser !

## Attendees

During the hacker within, let's see if we can add a list of attendees ! Put your
name down here in one of these lines (choose at random to avoid conflicts)























[octopus]: http://marc.info/?l=linux-kernel&m=139033182525831
[git-scm]: https://git-scm.com/
[trygithub]: try.github.com
[fake-man]: https://git-man-page-generator.lokaltog.net/
[satirical]: http://typicalprogrammer.com/linus-torvalds-goes-off-on-linux-and-git/
[xkcd]: https://xkcd.com/1597/
[backtothefuture]: http://www.mattluedke.com/back-git-history/
[man]: https://git-scm.com/docs/git-commit
[githubfordesktop]: https://desktop.github.com/
