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
4. [GitHub](#github)
5. [GitHub Pages](#github-pages)
6. [SSH or HTTPS](#ssh-or-https)
7. [Git Primer](#git-primer)
8. [Winning Workflow](#winning-workflow)

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

## Git VCS
What is Git? And why is it important? 

### In case of fire, git commit, git push and leave the building
![In case of fire, git commit, git push and leave the building](images/in_case_of_fire.png)
*From [GitHub repo `in-case-of-fire`](https://github.com/louim/in-case-of-fire)
(c) 2015 [Louis-Michel Couture](https://twitter.com/louim)*

### Git on Git
>Git is a [free and open source](https://git-scm.com/about/free-and-open-source)
distributed version control system designed to handle everything from small to
very large projects with speed and efficiency. [1]

### XKCD on Git
![xkcd 1597: Git](https://imgs.xkcd.com/comics/git.png)

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

## GitHub
Repeat the following 3 times out loud:

>Git is *not* GitHub, and GitHub is *not* Git.

GitHub is an online hosted Git service that acts as a centralized repository
for its users. You can create and clone Git repositories on GitHub, and you can
pull from and push to Git repositories on GitHub, just as if they were on your
own laptop, another networked laptop, or another  online Git hosting service
like Bitbucket or GitLab.

If you have not already created a GitHub account, you need to create one now to
participate in this tutorial. Also, I encourage you to enable two-factor
authentication (TFA on your GitHub account, and store your backup codes in a
safe location, that you will remember. TFA makes it more difficult to hack your
account.

## GitHub Pages
GitHub allows users to host static content on [GitHub Pages](https://pages.github.com/).
Content written in markdown is automatically rendered as html using
[Jekyll](https://jekyllrb.com/), a Ruby static content generator. GitHub offers
themes to beautify your site look and layout. It's a great place to host your
personal website.

1. To create your personal GitHub Page, you need to create a new repository called
`<your-github-username>.github.io`, for example `mikofski.github.io`.

2. After the new repository is created, open the repository settings, and select
theme chooser.

3. After Choosing a theme, an online editor opens with `index.md`. You can make
edits to this file like change the title to your name.

4. Scroll to the bottom, find where it says commit directly to master, in the
first field enter, "initial commit", and then press the commit button.

**Congratulations!** You've just made your first Git commit on GitHub, and created
your personal website. But, it's far from done. It could use a little mroe work.
Let's take it offline, and iterate on it, till it's just the way you want.

## SSH or HTTPS
In order to pull the repository to your laptop, you'll have to prove to GitHub,
that you are who you say you are, and that you have permission to edit the site.
There are two ways to authenticate to GitHub:

- **SSH**: you create a pair of keys, keep one private, and upload the public
key to GitHub. (Recommended)

  1. if your laptop has a folder called `.ssh` in your user profile and it
  contains two files called `id_rsa` and `id_rsa.pub` then skip to step 4.
  
  2. if your laptop does *not* have a `.ssh` folder, then open a shell type
  `ssh-keygen`
  3. when prompted to for a passphrase, enter something that is easy to remember
  4. on your laptop in a shell, type

         $ eval `ssh-agent`
         $ ssh-add

  5. if prompted for you passphrase and you know it, enter it, but if you don't
  know it, then kill the shell, delete the `.ssh` folder, and restart from step 2
  6. on you laptop, open the `id_rsa.pub` file in `.ssh/` and copy the contents
  7. online in your personal GitHub profile, in settings under SSH keys, click
  New SSH key, paste the contents of your public key and click Add SSH key to save

- **HTTPS**: You use your GitHub username and password, but if you enabled TFA,
this becomes more complicated. You have two more options:

  * Windows: do nothing, Microsoft has already installed a credential manager
  that works with GitHub to prompt you for your TFA code.
  * Mac/Linux Option A: create a personal access token with repo access

    1. in your personal GitHub profile under developer settings click generate
    new personal access token, and check the repo full access box
    2. on your laptop enable git credential store by typing
    `git config credential.store`
    3. then when prompted by Git, use your GitHub username, and the personal
    access token as your password.
 
  * Mac/Linux Option B: download and
  [install the Microsoft Git Crendential manager](https://github.com/Microsoft/Git-Credential-Manager-for-Mac-and-Linux/blob/master/Install.md) - this does
  everything in option 1 for you (Recommended)

## Git Primer
The most important Git command is `git`. If you type it in a terminal you get a
list of the other most important Git commands such as `init`, `clone`, `status`,
`log`, `diff`, `add`, `commit`, `checkout`, `remote add`, `pull`, and `push`.

The first thing you should do, after setting up your `.ssh` keys is to tell Git
your full name and email address to use. Then we can get your new website and
start hacking on it. The following commands are entered in a shell in a folder
you use for projects for. 

1. Add your name and email using `git config`:

       $ git config --global user.name "Your Name Comes Here"
       $ git config --global user.email you@yourdomain.example.com

2. Clone your GitHub repository to your laptop using `git clone`:

       # if you're using SSH
       $ git clone git@github.com:<github-username>/<github-username>.github.io.git

       # if you're using HTTPS
       $ git clone https://github.com/<github-username>/<github-username>.github.io.git

3. Enter the newly cloned repo, display the remotes and the log

       $ git log
       $ git remote
       $ git remote show origin

4. Now open your editor and make some changes to your `index.md` file.

5. Before you make too many changes, go back to the shell and view the status,
a diff from the previous version, and commit your changes

       $ git status
       $ git diff
       $ git commit -am "put any message here, usually under 50 characters"

### XKCD on Git Commit
![xkcd 1296: Git Commit](https://imgs.xkcd.com/comics/git_commit.png)

## Winning Workflow
The secret power of using Git with GitHub is how easy it makes collaborating
with others. AFAIK the feature-branch workflow is the most frequent method of
collaboration on GitHub. I outlined it's steps in a THW-Berkeley talk last year
on [using GitHub in OSS](https://bids.github.io/dats/posts/2017-10-04-github-oss-f17.html).

## Additional Info
- [GitHub help pages](https://help.github.com/) are a wealth of info.
- [Oh Shit Git!](https://ohshitgit.com/) is a funny.
- [Git SCM Documentation](https://git-scm.com/doc) is the official source.
