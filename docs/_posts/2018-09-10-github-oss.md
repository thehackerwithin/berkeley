---
layout: post2
title: Mark Mikofski -- Git Version Control with GitHub
time: 4-5:30pm
comments: true
category: upcoming
tags: meeting
---

# Agenda
1. [Requirements](#requirements)
2. [Objectives](#objectives)
3. [What is Git VCS?](#git-vcs)
4. [GitHub Pages](#github-pages)
5. [Git Primer](#git-primer)
6. [Winning Workflow](#winning-workflow)

## Requirements
To prepare for this tutorial make sure you have the following:

1. We're going to use Git, so make sure you have Git installed on a laptop,
and of course, don't forget to bring your laptop to the tutorial.

    - MacOS: you already have git, open a terminal and type git
    - Windows: install [Git-for-Windows](https://gitforwindows.org/), no admin
    - Linux: use your app manager, *eg* Ubuntu: `sudo apt install git`

   For more info, see the [Git SCM Book on installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2. We're going to make a personal webpage on GitHub, so make sure your computer
has working internet access. AFAIK anyone can use
[CalVisitor or AirBears WiFi](https://studenttech.berkeley.edu/get-online)
connection for free.
3. If you are not already registered for GitHub, please create an account. I
strongly recommend that you enable
[two factor authentication](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/)
using an app like Google Authenticator.
4. You'll probably want a basic editor like Notepad on Windows, TextEdit on Mac,
and gedit in Linux, or you can also just edit your files directly on GitHub.
Anything will do, but *not* a word-processor, no, and a fullblown IDE is also
probably overkill. Something like [Sublime Text](https://www.sublimetext.com/)
or [Notepad++](https://notepad-plus-plus.org/) is just right IMHO.
5. A willingness to participate, try new things, make mistakes, learn and have fun!

## Objectives
At the end of this tutorial you will be able to do the following:

1. explain to a colleague what version control is, why it's important, what it's
important for, and when to use it
2. use Git to version control your documents between iterations
3. teach a coworker to use basic git commands, and to create a pull request on GitHub
4. collaborate with others on GitHub using a feature-branch workflow
5. make a personal webpage using GitHub Pages

## In case of fire, git commit, git push and leave the building
![In case of fire, git commit, git push and leave the building](https://github.com/louim/in-case-of-fire/blob/master/in_case_of_fire.png)
*(c) 2015 [Louis-Michel Couture](https://twitter.com/louim)*

## Git VCS
What is Git? And why is it important? 

### XKCD on Git
![xkcd 1597: Git](https://imgs.xkcd.com/comics/git.png)

### Git on Git
>Git is a [free and open source](https://git-scm.com/about/free-and-open-source)
distributed version control system designed to handle everything from small to
very large projects with speed and efficiency. [1]

### Version Control Software (VCS) _aka_ Source Code Management (SCM)
But what is Version Control?

> ... version control, _aka_ source control, is the management of changes to
documents, computer programs, large web sites, and other collections of
information. [2]

Whether you're writing a dissertation, developing an analysis, or writing code,
you will revise, revise, and revise. Each iteration is important. Using Git VCS
gives you the ability:

* to reverse your work
* take a new direction without losing your current position
* recover from a hard drive crash
* continue your work from a different laptop
* collaborate with others, 

#### References
1. [Git SCM](https://git-scm.com/)
2. [Wikipedia: Version Control](https://en.wikipedia.org/wiki/Version_control)

## GitHub Pages
GitHub is an online hosted Git service that more or less acts as a centralized
repository for its users. 


## Git Primer
The most important Git command is `git`. If you type it in a terminal you get a
list of the other most important Git commands such as `init`, `clone`, `status`,
`log`, `diff`, `add`, `commit`, `checkout`, `remote add`, `pull`, and `push`.

The

1. Add your name and email using `git config`

    $ git config --global user.name "Your Name Comes Here"
    $ git config --global user.email you@yourdomain.example.com

### XKCD on Git Commit
![xkcd 1296: Git Commit](https://imgs.xkcd.com/comics/git_commit.png)


## Winning Workflow
The secret power of using Git with GitHub is how easy it makes collaborating
with others. AFAIK the feature-branch workflow is the most frequent method of
collaboration on GitHub. I outlined it's steps in a THW-Berkeley talk last year
on [using GitHub in OSS](https://bids.github.io/dats/posts/2017-10-04-github-oss-f17.html).

## Additional Info