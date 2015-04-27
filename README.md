# THW@Brkeley

The Hacker Within at the University of California - Berkeley is a skill-sharing 
meeting for researchers in scientific computing.

For meeting information and other resources,
go to our blog at [thehackerwithin.github.io/berkeley](http://thehackerwithin.github.io/berkeley).

For example code, consider cloning the master branch of this reposiory.

## How To Be The Speaker

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


Now you're done adding code example files! 

Rather than preparing a slideshow, please consider leading as interactive a session as possible. This is often done by leading the audience through whatever code examples you pushed to the master branch. Supportive text can be added to the markdown file holding the blog post for your talk. To add text to that file and to edit your bio :

1. Navigate in your repository to the gh-pages branch with `git checkout gh-pages`
2. Then, navigate to to `_posts/2015-04-22-c++-and-object-orientation.markdown` 
3. Open that file,
4. Edit it, 
5. git add it, 
6. and git push it to origin gh-pages.

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

