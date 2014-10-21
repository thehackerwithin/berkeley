
# The Hacker Within 

This is the website that keeps the blog posts for each THW meeting at the 
University of California - Berkeley. The rendered website can be found 
[here](http://thehackerwithin.github.io/berkeley).

## How to Contribute

- [Fork this repository](https://github.com/thehackerwithin/berkeley)
- Clone it: `git clone https://github.com/YOUR-USER/berkeley`
- change branches into the gh-pages branch `git checkout gh-pages`
- **Optional:** Add the THW remote `cd berkeley&&git remote add upstream 
  git@github.com:thehackerwithin/berkeley`


### Creating a Post

In the directory that you just cloned (berkeley), you'll notice a `_posts` 
directory. You'll also notice a `_drafts` directory. In the drafts directory, 
you'll find an empty template for meeting minutes 
`YYYY-MM-DD-subject.markdown`. If you're preparing for a special holiday meeting 
on March 1, 2015, then the proper name for the file you're creating should be 
something like 2015-03-01-katysbirthday.markdown.

- In the berkeley directory, execute `cp _drafts/YYYY-MM-DD-subject.markdown 
  _posts/2015-03-01-katysbirthday.markdown
- Then, edit that file as you see fit
- Add that file to the repository `git add _posts/2015-03-01-katysbirthday.markdown`
- Commit it: `git commit -am "adds a post for march 1"`
- Push it to your fork `git push origin gh-pages`
- Check if it worked at https://YOUR-USER.github.io/berkeley .
- Iterate on this until you're happy 
- and then either push to the upstream gh-pages remote branch or make a pull request.

### Modifying a Post

This is very similar to creating a post:

- edit the post
- Commit it: `git commit -am "adds a post for march 1"
- Push it to your fork `git push origin gh-pages`
- Check if it worked at https://YOUR-USER.github.io/berkeley .
- Iterate on this until you're happy 
- and then either push to the upstream gh-pages remote branch or make a pull request.

### Build the site locally

- Install Jekyll: `gem install jekyll`
- Run the jekyll server: `jekyll --server`

You should have a server up and running locally at <http://localhost:4000>.

## We use Left to lay out this jekyll

It's all based on something @katyhugg forked. It's called Left.  It uses jekyll.  It was
extracted from [zachholman.com](http://zachholman.com/).

Left is a clean, whitespace-happy layout for [Jekyll](https://github.com/mojombo/jekyll).


### Content Licesing

The content of this blog is liberally licensed to The Hacker Within and to the 
individual authors of each blog post.  Additionally, you're welcome to reshare the content with attribution,
because it is [CC-BY-3.0 licensed](http://creativecommons.org/licenses/by/3.0/)

Except where otherwise noted, content on this site is licensed under a Creative
Commons Attribution 3.0 Unported License. Copyright 2013-2014 The Hacker 
Within.

Please attribute any work with a link to its original appearance on this
domain (i.e., "from The Hacker Within's blog entry 'Segmentation Fault' at
[thehackerwithin.github.io/blog/posts/segmentation-fault](thehackerwithin.github.io/blog/posts/segmentation-fault)
").

### Left Licensing

The Left layout is [MIT](https://github.com/holman/left/blob/master/LICENSE) with no
added caveats, so feel free to use this on your site without linking back to
me or using a disclaimer or anything silly like that.

If you'd like give me credit somewhere on your blog or tweet a shout out to
[@holman](https://twitter.com/holman), well hey, I'll take it.

![Left](http://cl.ly/image/3S2r1p2C0E2B/content)
