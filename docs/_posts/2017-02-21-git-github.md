---
layout: post
title: Git and GitHub -- Ciera Martinez and Matthias Bussonnier
comments: true
category: posts
tags: meeting git h2g2 backtothefuture github rickandmorty xkcd cthulhu
---

# Git and Github

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
- Create a repository from scratch
- Make a commit
- Make a branch
- Create a Pull request on GitHub
- Update your local repository


## What is the difference between github and git?

### Git 

A lightweight version control system to track changes made to a project through time. There are many ways to use Git on your computer. 

The main ways are:

- [Command Line](https://git-scm.com/book/id/v2/Getting-Started-The-Command-Line) - typing command into terminal (mac)
- [GitHub desktop](https://desktop.github.com/) - GUI
- [In RStudio](https://jennybc.github.io/2014-05-12-ubc/ubc-r/session03_git.html) - GUI 
- [SourceTree](https://www.sourcetreeapp.com/) - GUI

**Suggestion**: Command Line

Command line is the most popular way to use git, therefore you can get help easily. If you know how to run the command line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true. Dont let your inexperience with command line stop you, you only need to learn the very basics of unix to use git.


### Github <i class="fa fa-github" aria-hidden="true"></i> - Remote Hosting

While Git stands alone as a system, Github is a website that hosts your project and Git history. You can use for collaboration, back-up, sharing, and learning. [Github](https://github.com/) is just one of many places to host repositories.  

The main ways are:

- [Bitbucket](https://bitbucket.org/)
- [GitLab](https://gitlab.com/users/sign_in)
- [sourceForce](https://sourceforge.net/)


**Suggestion**: Github

The benefit of Github is that it is the most popular and has many tools to make it easy and fun to use. The main downside is that it does not allow free private repositories.

## Why use Git?

<center><img src="http://www.phdcomics.com/comics/archive/phd101212s.gif" width="50%" height="50%" /></center>

- Allows you to store versions (properly)
- Makes you fearless  
- Restoring Previous Versions
- Collaboration <i class="fa fa-github" aria-hidden="true"></i> - Git allows groups of people to work on the same documents (often code) at the same time, and without stepping on each other's toes (from [tryGit](https://try.github.io/levels/1/challenges/1)).
- Backup <i class="fa fa-github" aria-hidden="true"></i>
- Build easy to maintain websites <i class="fa fa-github" aria-hidden="true"></i>

## Learning Git

Learning git *well* is hard, but I would say only 5% of people who use git know *exactly* what they are doing. 

<center><img src="https://imgs.xkcd.com/comics/git_2x.png" width="50%" height="50%" /></center>

### Why is learning git hard? 

-  Vocabulary is not intuitive and is different depending on the system to use it. Here is a [cheatsheet for common vocabulary](https://help.github.com/articles/github-glossary/)
-  Git is a complex with many ways to approach using it. 
-  Git becomes more complex when working on a team, because there must be rules for how to collaborate and these rules differ depending on the team.  You can learn how a team collaborates usually from a file in the project directory called `CONTRIBUTING.md`.  Example contributing file: [`CONTRIBUTING.md` file for ggplot2](https://github.com/tidyverse/ggplot2/blob/master/CONTRIBUTING.md)

## Demo (Beginner)

###  Requirements

### Git

Try to have git installed on your laptop before coming to the hacker within.
If you are on windows we recommend git-bash, which should be bundled with [GitHub for Desktop][githubfordesktop].

Git should be bundled on recent Macs, you can also install it with [GitHub for Desktop][githubfordesktop], or [Homebrew](https://brew.sh).

User of linux probably already have git installed as well , or know how to install it with your favorite package manager.

### Activity

Basically we are all going to make a small edit to a file in a repository using basic git commands. Here is an overview with many of the command we will use:

<center><img src="http://cierareports.org/downloads/gitCheatSheetGitHub_ForkEasy.png" width="75%" height="75%" /></center>


1. Go here: 
[https://github.com/iamciera/THW_attendence](https://github.com/iamciera/THW_attendence)
2. Press the Fork button ([you'll need a Github account](https://github.com/signup))
3. In your terminal, execute `git clone https://github.com/YOURUSERNAME/THW_attendence`.  Make sure you replace "YOURUSERNAME" with your Github name.  For example mine is iamciera.
4. Enter the new directory with `cd THW_attendence`
5. Add the original remote repo with `git remote add upstream https://github.com/iamciera/THW_attendence`
6. Fetch information about the  remote with `git fetch upstream`
7. Now, you need to check what branch you're in `git branch`.  Make sure you are on the master branch.
8. Now we are ready to edit the file. Open the `README.md` file and add your name to the list. Add under the header of the letter your first name starts with. This is so we avoid merge conflicts. 
9. Commit them. `git commit -am "I added files for the tutorial on my 
    topic.."`  NOTE: *`-am` means you are telling git to "stage all changes in the directory" and that you want to include a commit message*
10. Git push to your origin (your repo on Github) with `git push origin master`
11. Navigate in your browser to: https://github.com/YOURUSERNAME/THW_attendence and press the pull request button.


## Demo (Advanced)

### Advanced tactics !

Narrow down a bug ? Let's bisect. Want to hide your mistakes ? rebase/amend.
Have erased a mistake from history that was not a mistake ? reflog to the
rescue.

### Blips and Chitz !

Git is no fun without all the configuration option and tricks that make your life easier.

Checkout a PR by it's number ? oowee! 
Diff words instead of lines ? Can doooo !
Local and global gitignore ? Sure !

### DON'T PANIC

Even if it looks insanely complicated to operate and and partly to keep intergalactic travelers from panicking we'll discuss what to do when things go south.

Long story short, keep calm and ``commit -A`` (and `push`) if you are really scared. Nothing is ever lost.

What happen in case of broken whatever ? If you are in "Detached head state", "merge conflict", or anything else ? We got you covered !



## Resources
### Examples of how I use Github

-  [SOM Tutorial](https://iamciera.github.io/SOMexample/): To host tutorials
-  [My Website](https://github.com/iamciera/creports): To host website
-  [Example Manuscript Repo](https://github.com/iamciera/sister-of-pin1-material): Host code for my papers
-  [http://ropensci.github.io/reproducibility-guide/](http://ropensci.github.io/reproducibility-guide/): Build things with strangers
-  [Eisen Lab Github](https://github.com/meisenlab): Collaborate with lab members.

### Learning Git

- [Software Carpentry Version Control lesson](https://swcarpentry.github.io/git-novice/)
- You can [train][trygithub] in your browser !
- Spoon-Knife : https://github.com/octocat/Spoon-Knife



### Adventure time prompt

Inspired from [stackoverflow](http://stackoverflow.com/questions/4133904/ps1-line-with-git-current-branch-and-colors)

```bash

function we_are_in_git_work_tree {
    git rev-parse --is-inside-work-tree &> /dev/null
}

function parse_git_branch {
    if we_are_in_git_work_tree
    then
    local BR=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD 2> /dev/null)
    if [ "$BR" == HEAD ]
    then
        local NM=$(git name-rev --name-only HEAD 2> /dev/null)
        if [ "$NM" != undefined ]
        then echo -n "@$NM"
        else git rev-parse --short HEAD 2> /dev/null
        fi
    else
        echo -n $BR
    fi
    fi
}

function parse_git_status {
    if we_are_in_git_work_tree
    then 
    local ST=$(git status --short 2> /dev/null)
    if [ -n "$ST" ]
    then echo -n "| (• ︵•)| (❍ᴥ❍ʋ) "
    else echo -n "| (• ‿ •)| (❍ᴥ❍ʋ)"
    fi
    fi
}

function pwd_depth_limit_2 {
    if [ "$PWD" = "$HOME" ]
    then echo -n "~"
    else pwd | sed -e "s|.*/\(.*/.*\)|\1|"
    fi
}

export PS1="\[\033[32m\]\w\[\033[33m\]\$(parse_git_status)\[\033[00m\] $ "
```






[octopus]: http://marc.info/?l=linux-kernel&m=139033182525831
[gitscm]: https://git-scm.com/
[trygithub]: try.github.com
[fake-man]: https://git-man-page-generator.lokaltog.net/
[satirical]: http://typicalprogrammer.com/linus-torvalds-goes-off-on-linux-and-git/
[xkcd]: https://xkcd.com/1597/
[backtothefuture]: http://www.mattluedke.com/back-git-history/
[man]: https://git-scm.com/docs/git-commit
[githubfordesktop]: https://desktop.github.com/
