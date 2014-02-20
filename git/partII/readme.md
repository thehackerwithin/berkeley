Version Control Part II
=======================

Bienvenido and Howdy!

This material was adapted from work by The Hacker Within as well as Software 
Carpentry.


Collaborating
=======================

Version control really comes into its own when we begin to collaborate with
other people.  We already have most of the machinery we need to do this; the
only thing missing is to copy changes from one repository to another.

Systems like Git and Mercurial allow us to move work between any two
repositories.  In practice, though, it's easiest to use one copy as a central
hub, and to keep it on the web rather than on someone's laptop.  Most
programmers use hosting services like [GitHub](http://github.com) or
[BitBucket](http://bitbucket.org) to hold those master copies; we'll explore
the pros and cons of this in the final section of this lesson.

github?
----------

GitHub is a site where many people store their open (and closed) source
code repositories. It provides tools for browsing, collaborating on and
documenting code. Your home institution may have a repository hosting
system of it's own. To find out, ask your system administrator.  GitHub,
much like other forge hosting services (
[launchpad](https://launchpad.net), [bitbucket](https://bitbucket.org),
[googlecode](http://code.google.com), [sourceforge](http://sourceforge.net)
etc.) provides :

-   landing page support 
-   wiki support
-   network graphs and time histories of commits
-   code browser with syntax highlighting
-   issue (ticket) tracking
-   user downloads
-   varying permissions for various groups of users
-   commit triggered mailing lists
-   other service hooks (twitter, etc.)

**NOTE** Public repos have public licences **by default**. If you don't
want to share (in the most liberal sense) your stuff with the world, pay
github money for private repos, or host your own.


github pasword 
-----------------

Setting up github at first requires a github user name and password.
Please take a moment to [create a free one](https://github.com/signup/free)
(if you want to start paying, you can add that to your account some other
day). 

Create a repository
-----------------------

Let's start by sharing the changes we've made to our current project with the
world.  Log in to GitHub, then create a new repository called `planets` using
their GUI:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/github-create-repo-01.png" alt="Creating a Repository on GitHub (Step 1)" />

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/github-create-repo-02.png" alt="Creating a Repository on GitHub (Step 2)" />

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/github-create-repo-03.png" alt="Creating a Repository on GitHub (Step 3)" />

This effectively does the following on GitHub's servers:

~~~
$ mkdir planets

$ cd planets

$ git init --bare
~~~


Connect a Local Repository with the Remote one 
---------------------------------------------------

Our local repository still contains our earlier work on `mars.txt`,
but the remote repository on GitHub doesn't contain any files yet:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/git-freshly-made-github-repo.png" alt="Freshly-Made GitHub Repository" />

The next step is to connect the two repositories.
We do this by making the GitHub repository a [remote](../gloss.html#repository-remote)
for the local repository.
The home page of the repository on GitHub includes
the string we need to identify it:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/github-find-repo-string.png" alt="Where to Find Repository URL on GitHub" />

For now,
we'll use the 'http' [protocol](../../gloss.html#protocol)
(which is also used by web browsers)
since it requires the least setup.
Copy that URL from the browser,
go into the local `planets` repository,
and run this command:

~~~
$ git remote add origin https://github.com/vlad/planets
~~~

(using your GitHub ID instead of `vlad`).
We can check that the command has worked by running `git remote -v`:

~~~
$ git remote -v
origin   https://github.com/vlad/planets.git (push)
origin   https://github.com/vlad/planets.git (fetch)
~~~

There's nothing magic about the name `origin`,
but we'll see in a moment why it's a sensible choice.
Once this is set up,
this command will push the changes from our local repository
to the repository on GitHub:

~~~
$ git push -u origin master
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 821 bytes, done.
Total 9 (delta 2), reused 0 (delta 0)
To https://github.com/vlad/planets
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
~~~

Our local and remote repositories are now in this state:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/github-repo-after-first-push.png" alt="GitHub Repository After First Push" />

### The '-u' Flag 

 You may see a `-u` option used with `git push`.
 This tells Git what [branch](../../gloss.html#branch) to use
 in the repository you're pushing to.
 We discuss branches and branching in our intermediate-level lessons.

We can pull changes from the remote repository to the local one as well:

~~~
$ git pull origin master
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Already up-to-date.
~~~

Pulling has no effect in this case
because the two repositories are already synchronized.
If someone else had pushed some changes,
though,
this command would download them to our local repository.
We can simulate this by going to another directory&mdash;for example, `/tmp`&mdash;and
[cloning](../gloss.html#repository-clone) our GitHub repository:

~~~
$ cd /tmp
$ git clone https://github.com/vlad/planets.git
~~~

`git clone` creates a fresh local copy of a remote repository.
(We did it in `/tmp` or some other directory so that we don't overwrite our existing `planets` directory.)
Our computer now has two copies of the repository:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/git-after-duplicate-clone.png" alt="After Creating Duplicate Clone of Repository" />

Let's make a change in the copy in `/tmp/planets`:

~~~
$ cd /tmp/planets

$ nano pluto.txt

$ cat pluto.txt
It is so a planet!

$ git add pluto.txt

$ git commit -m "Some notes about Pluto"
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
~~~

then push the change to GitHub:

~~~
$ git push origin master
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 306 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/vlad/planets.git
   9272da5..29aba7c  master -> master
~~~

Our three repositories now look like this:

<img src="http://raw.github.com/thehackerwithin/berkeley/master/git/img/git-after-change-to-duplicate-repo.png" alt="After Pushing Change from Duplicate Repository" />

We can now download changes into the original repository on our machine:

~~~
$ cd ~/planets

$ git pull origin master
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Updating 9272da5..29aba7c
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
~~~

In practice,
we would probably never have two copies of the same remote repository
on our laptop at once.
Instead,
one of those copies would be on our laptop,
and the other on a lab machine,
or on someone else's computer.
Pushing and pulling changes gives us a reliable way
to share work between different people and machines.


Steps for Forking a Repository
---------------------------------

A key step to interacting with an online repository that you have forked
is adding the original as a remote repository. By adding the remote
repository, you inform git of a new option for fetching updates and
pushing commits.

The **git remote** command allows you to add, name, rename, list, and
delete repositories such as the original one **upstream** from your
fork, others that may be **parallel** to your fork, and so on.

### Exercise : Fork Our GitHub Repository

In step 1, you will make a copy "fork" of our thehackerwithin/berkeley 
repository on github.  This gives you a copy of this repository that you 
control.

In step 2, you will make a copy of **your** fork of the repository on your 
hard drive.

In step 3, you will let git know that in addition to your local copy and 
your fork on github, there is another github repository (called "upstream") 
that you might want to get updates from.

Step 1 : Go to our
[repository](https://github.com/thehackerwithin/berkeley)
from your browser, and click on the Fork button. Choose to fork it to your
username rather than any organizations.

Step 2 : Clone it. From your terminal :

    $ git clone https://github.com/YOU/berkeley.git
    $ cd berkeley

Note: YOU is a placeholder for YOUR github username.  If git asks you for 
a password here, it probably means you have mis-typed the url for the 
repository. 

Step 3 : 

    $ git remote add upstream https://github.com/thehackerwithin/berkeley.git
    $ git remote -v
    origin  https://github.com/YOU/berkeley.git (fetch)
    origin  https://github.com/YOU/berkeley.git (push)
    upstream        https://github.com/thehackerwithin/berkeley.git (fetch)
    upstream        https://github.com/thehackerwithin/berkeley.git (push)
    $

All repositories that are clones begin with a remote called origin.

### What's going on here?
The **git remote add** merely defines a nickname and a location that 
git will be able to communicate with for making copies of your 
repository.  "origin" and "upstream" are nicknames for your fork of 
berkeley and the "original" berkeley, respectively.

git fetch : Fetching the contents of a remote
------------------------------------------------

Now that you have alerted your repository to the presence of others, it
is able to pull in updates from those repositories. In this case, if you
want your master branch to track updates in the original berkeley
repository, you simply **git fetch** that repository into the master
branch of your current repository.

The fetch command alone merely pulls down information recent changes
from the original master (upstream) repository. By itself, the fetch
command does not change your local working copy. To update your local
working copy to include recent changes in the original (upstream)
repository, it is necessary to also merge.

git merge : Merging the contents of a remote
------------------------------------------------

To incorporate upstream changes from the original master repository (in
this case thehackerwithin/berkeley) into your local working copy, you
must both fetch and merge. The process of merging may result in
conflicts, so pay attention. This is where version control is both at
its most powerful and its most complicated.

### Exercise : Fetch and Merge the Contents of Our GitHub Repository

Step 1 : Fetch the recent remote repository history

    $ git fetch upstream

Step 2 : Make certain you are in the master branch and merge the
upstream master branch into your master branch

    $ git checkout master
    $ git merge upstream/master

Step 3 : Check out what happened by browsing the directory.

git pull : Pull = Fetch + Merge
------------------------------------------------

The command **git pull** is the same as executing **git fetch** followed
by **git merge**. Though it is not recommened for cases in which there
are many branches to consider, the pull command is shorter and simpler
than fetching and merging as it automates the branch matching.
Specificially, to perform the same task as we did in the previous
exercise, the pull command would be :

    $ git pull upstream
    Already up-to-date.

When there have been remote changes, the pull will apply those changes
to your local branch, unless there are conflicts with your local
changes.

git push : Sending Your Commits to Remote Repositories
------------------------------------------------------------

The **git push** command pushes commits in a local working copy to a
remote repository. The syntax is git push \[remote\] \[local branch\].
Before pushing, a developer should always pull (or fetch + merge), so
that there is an opportunity to resolve conflicts before pushing to the
remote.

### Exercise : Push a change to github
We'll talk about conflicts later, but first, let's make a small change
that won't have any conflicts and send our changes to
your fork, the "origin."

1. Create a file in the `messages` directory whose filename is your github
id.  (This is to ensure no conflicts just yet!)  Add a line of text, perhaps a
description of how you use, or expect to use, programming in your
work.

2.  commit your change with `git add YOU` and `git commit -m "Commit message"`

3.  Update your fork ("origin") with your new changes:

    $ git push origin master

This will update your github fork with any changes you've committed.
Once you do this, you can see your changes on the github web interface
to your repository, along with the time you made the change and
your commit message.

If you have permission to push to the upstream repository, sending
commits to that remote is exactly analagous.

    $ git push upstream master

In the case of the upstream push, new developer accounts will not allow
this push to succeed. You're welcome to try it though.

There is now a hierarchy of git repositories.  There was the upstream
repository that you can't write to, there is your fork of that repository
that you have updated, and there is the local copy on your hard drive.

In the berkeley code, you'll find various files called readme.md. This is a
standard documentation file that appears rendered on the landing page
for the repository and in github. This very file is a readme file in the 
  git/partII directory. To see the rendered version, visit your
fork on github, (https://github.com/YOU/berkeley/git/partII/readme.md).

github pull requests 
--------------------------

One protocol for updating repositories that we use at Software Carpentry
is the "pull request."   This is a bundle of updates to the repository
that can be accepted and merged into the upstream repository or rejected
and not merged.  If you would like to share your changes with the
upstream repository, click the green "compare and review" button, and
github will show you a summary of your commits.  If you then
click on "Click to create a pull request for this comparison," your
request will be sent to the upstream repository for acceptance or
rejection.

git merge : Conflicts
--------------------------

This is the trickiest part of version control, so let's take it very
carefully.

Conflicts happen when git tries to combine changes from two different
branches (local and remote, development and master) but finds that 
changes in the two branches interfere with each other and can't be
automatically merged.

Branches are a tool that git uses to facilitate managing changes.
They allow us to switch between states of the repository and refer to
states that we desire to merge.

You'll often want to start a new branch for development, make your changes there,
and then merge these changes into your main branch. It's a good convention
to think of your master branch as
the "production branch," typically by keeping that branch clean of your
local edits until they are ready for release. Developers typically use the
master branch of their local fork to track other developers' changes in the
remote repository until their own local development branch changes are
ready for production.

### Exercise : Experience a Conflict

Step 1 : Make a new branch, edit the readme file in that branch, and
commit your changes.

    $ git branch development
    $ git checkout development
    Switched to branch 'development'
    $ cd git/partII
    $ nano readme.md &
    <edit the readme file and exit nano>
    $ git commit -am "Changed the Readme message to ... "

Step 2 : Mirror the remote upstream repository in your master branch 
by pulling down my changes

    $ git checkout master
    Switched to branch 'master'
    $ git fetch upstream
    $ git merge upstream/master
    Updating 43844ea..3b36a87
    Fast-forward
     Readme.md |   2 +-
     1 files changed, 1 insertions(+), 1 deletions(-)

Step 3 : You want to push it to the internet eventually, so you pull
updates from the upstream repository, but will experience a conflict.

    $ git merge development
    Auto-merging readme.md
    CONFLICT (content): Merge conflict in readme.md
    Automatic merge failed; fix conflicts and then commit the result.

git resolve : Resolving Conflicts
---------------------------------------

Now what?

Git has paused the merge. You can see this with the **git status**
command.

    # On branch master
    # Unmerged paths:
    #   (use "git add/rm <file>..." as appropriate to mark resolution)
    #
    #       unmerged:      readme.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

The only thing that has changed is the readme.md file. Opening it,
you'll see something like this at the beginning of the file.

    =====================
    <<<<<<< HEAD
    Howdy
    =======
    Willkommen
    >>>>>>> development
    =====================

The intent is for you to edit the file and determine how to combine 
the variants from the two branches before committing the result.
Decisions like this
must be made by a human.  Differences that can be automatically merged
usually are, so humans are involved only when different edits touch
the same piece of the repository. 

    Howdy and Willkommen

This results in a status To alert git that you have made appropriate
alterations,

    $ git add Readme.md
    $ git commit
    Merge branch 'development'

    Conflicts:
      readme.md
    #
    # It looks like you may be committing a MERGE.
    # If this is not correct, please remove the file
    # .git/MERGE_HEAD
    # and try again.
    #
    $ git push origin master
    Counting objects: 10, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 762 bytes, done.
    Total 6 (delta 2), reused 0 (delta 0)
    To git@github.com:username/berkeley.git

Synchronizing 
--------------------------
Now that lots of us created files and put in pull requests,
we begin to suspect that the upstream repository might have
new content and we are out of date. Try

    $ git pull upstream master

to fetch, merge, and commit the changes from upstream repository--
including other people's changes that have been added to upstream.
In this way we can all get updates of what the rest of us are
working on.

But now our forks -- on github -- are out of date.  We can push
to update those

    $ git push origin master

And all is synchronized.

What about Berkelium?
----------------------

### Starting with code on Bk

Let's say you have a directory full of code on your Bk user space. You want to 
have a copy on your laptop that you can sync with it, but you don't want to put 
it on github. This is easy. Let's go through the steps. 


    you@laptop$ ssh you@berkelium.nuc.berkeley.edu
    you@berkelium.nuc.berkeley.edu's password: 
    you@berkelium$ cd good_science
    you@berkelium$ git init
    you@berkelium$ git add *
    you@berkelium$ git commit -am "adds all the code"
    you@berkelium$ exit
    logout
    Connection to berkelium.nuc.berkeley.edu closed.
    you@laptop$ git clone you@berkelium.nuc.berkeley.edu:~/good_science
    Cloning into 'good_science'...
    you@berkelium.nuc.berkeley.edu's password: 
    remote: Counting objects: 150, done.
    remote: Compressing objects: 100% (78/78), done.
    remote: Total 150 (delta 60), reused 147 (delta 60)
    Receiving objects: 100% (150/150), 4.29 MiB, done.
    Resolving deltas: 100% (60/60), done.
    you@laptop$ cd good_science


### Starting with code on your laptop

Let's say you have a directory full of code on your computer. You want to sync 
it with Berkelium, but you don't want to put it on github. It's possible but 
slightly more complex because your laptop probably doesn't have a static IP. Let's 
go through the steps. 


    you@laptop$ cd good_science
    you@laptop$ git init
    you@laptop$ git add *
    you@laptop$ git commit -am "adds all the code"
    you@laptop$ ssh you@berkelium.nuc.berkeley.edu
    you@berkelium.nuc.berkeley.edu's password: 
    you@berkelium$ mkdir good_science.git
    you@berkelium$ cd good_science.git
    you@berkelium$ git init --bare
    you@berkelium$ exit
    logout
    Connection to berkelium.nuc.berkeley.edu closed.
    you@laptop$ git remote add bk you@berkelium.nuc.berkeley.edu:~/good_science.git
    you@laptop$ git push -u bk
    you@laptop$ ssh you@berkelium.nuc.berkeley.edu
    you@berkelium.nuc.berkeley.edu's password: 
    you@berkelium$ git clone file://~/good_science.git good_science

