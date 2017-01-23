# The Hacker Within

This is the website that keeps the blog posts for each THW meeting at the
University of California - Berkeley. The rendered website can be found
[here](http://thehackerwithin.github.io/berkeley).


## How To Be The Speaker

One very common reason that folks want to contribute to this repository is that 
they are planning to give the main skill sharing session for some week at THW. 
To be the speaker, you'll need to sign up, set up, show up, and speak up.

### Sign Up

We try to decide the semester meeting topics at the beginning of the session. 
So, if you have a topic you'd like to talk about, please suggest it over the 
listhost before the semester starts or show up to the first meeting of the 
semester.

### Set Up


We love sessions that have example code! If you have example code, please place 
it in an appropriately named directory in the master branch of this GitHub 
repository. Make a [pull 
request](https://help.github.com/articles/creating-a-pull-request/) or push your branch to the
[thehackerwithin/berkeley](http://github.com/thehackerwithin.berkeley) fork. 
If you know how to do that, please go right ahead. If you aren't sure about 
forks and pull requests, here are some detailed instructions:

#### Uploading Example Code

1. Go here: 
[https://github.com/thehackerwithin/berkeley](https://github.com/thehackerwithin/berkeley)
2. Press the Fork button ([you'll need a github account](https://github.com/signup))
3. In your terminal, execute `git clone https://github.com/YOURUSERNAME/berkeley.git`
4. Enter the new directory with `cd berkeley`
5. Add the THW remote with `git remote add thw https://github.com/thehackerwithin/berkeley.git`
6. Fetch information about the THW remote with `git fetch thw`
7. Now, you need to check what branch you're in `git branch`
8. If you're in the master branch, move the important files to an appropriately named directory there. (Browse the directory for examples of other's additions.)
9. Add the files to the repo: `git add <path to your new files>`
10. Commit them. `git commit -am "I added files for the tutorial on my 
    topic.."`
11. Git push to your origin with `git push origin master`
12. Navigate in your browser to https://github.com/YOURUSERNAME/berkeley and press the pull request button

Now you're done adding code example files! You'll need to edit the post related
to your talk.

#### Add Your Tutorial to the Site

Rather than preparing a slideshow, please consider leading as interactive a session as possible. This is often done by leading the audience through whatever code examples you pushed to the master branch. Supportive text can be added to the markdown file holding the blog post for your talk. To add text to that file and to edit your bio, switch branches to the gh-pages branch, where the website it held. There, you may need to both create and modify the post.

1. Navigate in your repository to the gh-pages branch with `git checkout gh-pages`
2. Then, create and modify the post as in the sections below.

#### Creating a Post

In the directory that you just cloned (berkeley), you'll notice a `_posts`
directory. The post related to the day and topic of your talk may already
exist. If so, skip ahead to "Modifying a Post." 

If not, you'll need to create it. Thankfully, you'll also notice a
`_drafts` directory. In the drafts directory, you'll find an empty template for
meeting minutes `YYYY-MM-DD-subject.markdown`. If you're preparing for a
special holiday meeting on March 1, 2015, then the proper name for the file
you're creating should be something like 2015-03-01-katysbirthday.markdown.

- In the berkeley directory, execute `cp _drafts/YYYY-MM-DD-subject.markdown
  _posts/2015-03-01-katysbirthday.markdown`
- Then, edit that file as you see fit
- Add that file to the repository `git add _posts/2015-03-01-katysbirthday.markdown`
- Commit it: `git commit -am "adds a post for march 1"`
- Push it to your fork `git push origin gh-pages`
- Check if it worked at https://YOUR-USER.github.io/berkeley .
- Iterate on this until you're happy
- and then either push to the upstream gh-pages remote branch or make a pull request.

#### Modifying a Post

This is very similar to creating a post:

- if the file for your date is YYYY-MM-DD-tbd.markdown, rename the file replacing "tbd" with your topic 
- edit the post
- Commit it: `git commit -am "adds a post for march 1"
- Push it to your fork `git push origin gh-pages`
- Check if it worked at https://YOUR-USER.github.io/berkeley .
- Iterate on this until you're happy
- and then either push to the upstream gh-pages remote branch or make a pull request.

#### Build the site locally

If you'd like to test the post before pushing or making a PR, you can build the 
site locally:

- Install Jekyll: `gem install jekyll`
- Run the jekyll server: `jekyll --server`

You should have a server up and running locally at <http://localhost:4000>.

### Show Up

Please arrive 10-15 minutes before the start time so that you can set up your 
computer and test out the projector. Please figure out how to zoom in on text 
that might be too small from the back. Try command-plus-plus in the terminal 
and other applications. If you're an emacs user on a mac, you may need [accessibility 
zoom enabled.](https://www.apple.com/accessibility/osx/).

### Speak Up

The Hacker Within isn't a class and no one is required to attend. We show up to 
have fun and to learn. Hopefully, your tutorial will teach something **useful** 
in a way that is **enjoyable.** To do this, please consider bringing your 
A-game. That is, find the enthusiastic tinkering problem-solver inside yourself 
(The Hacker Within yourself) and bring that version of yourself to share that 
enthusiasm with us. Enthusiasm is infectious!  


## About this website.

It's all based on something @katyhuff forked. It's called Left.  It uses
jekyll.  It was extracted from [zachholman.com](http://zachholman.com/). That
is, we use Left to lay out this jekyll. 

Left is a clean, whitespace-happy layout for
[Jekyll](https://github.com/mojombo/jekyll).


### Content Licensing

The content of this blog is liberally licensed to The Hacker Within and to the
individual authors of each blog post.  Additionally, you're welcome to reshare
the content with attribution, because it is [CC-BY-3.0
licensed](http://creativecommons.org/licenses/by/3.0/)

Except where otherwise noted, content on this site is licensed under a Creative
Commons Attribution 3.0 Unported License. Copyright 2013-2015 The Hacker
Within.

Please attribute any work with a link to its original appearance on this
domain (i.e., "from The Hacker Within's blog entry 'Segmentation Fault' at
[thehackerwithin.github.io/blog/posts/segmentation-fault](thehackerwithin.github.io/blog/posts/segmentation-fault) ").

### Left Licensing

The Left layout is [MIT](https://github.com/holman/left/blob/master/LICENSE) with no
added caveats. Left is the work of Zach Holman [@holman](https://twitter.com/holman).

![Left](http://cl.ly/image/3S2r1p2C0E2B/content)

