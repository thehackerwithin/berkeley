---
layout: post
title: Visualization - John Naulty, Ross Barnowski, Biye Jiang, Jennifer Jones
comments: true
category: posts
tags: meeting plotting python r 
---

## Attending

- Anyone is welcome. We hope you'll join us!

## Meeting Info

- When: 4:00pm - 5:30pm
- Where: [BIDS, Room 190 of Doe Library](https://bids.berkeley.edu).
- Who: Anyone interested in software development best practices is welcome to come to our meetings.
- How: A predetermined main topic (45 minutes) will be followed by impromptu lightning talks (5 minutes each)

## John Naulty

Bio

## Ross Barnowski

... likes computers

### pyqtgraph
Install: `pip install pyqtgraph`

Demo: `python -m pyqtgraph.examples`

[Description of pyqtgraph](http://www.pyqtgraph.org/)

My Take: pyqtgraph is less user-friendly than matplotlib (esp. the 
documentation; the gallery contains far fewer examples and doesn't do a good
job of covering all of the possible features and uses of pyqtgraph), but is very
feature-rich and more performance-oriented, despite still being pure python.
There are several scenarios in which pyqtgraph is definitely worth looking into:

 - **The need for speed**: pyqtgraph is in many cases *much* faster than
   matplotlib (see demo). Also has built-in support for remote plot updating.
 - **Volumetric rendering**: If you need to visualize in 3D, pyqtgraph has a lot
   to offer. The other de-facto python 3D-visualization library is `mayavi` ---
   I would say pyqtgraph has a slightly steeper learning curve and is a little
   less pretty, but again is much faster than mayavi. I don't have enough
   experience with `yt` to say how it compares.
 - **Building Qt Applications**: If you're using python-ized Qt (either PySide
   or PyQt) to build a GUI, pyqtgraph integrates very nicely. It is built with
   the same tools!
 - **Beyond Visualization**: The author(s) of pyqtgraph had the goal of making
   it a general science/engineering tool. There are a lot of built-in features
   designed to aid in analyzing data visually and interactively. See the 
   Data Slicing and Image Analysis examples to get a feel for this.


## Jennifer Jones

This is my Bio

## [Biye Jiang](http://byeah.github.io/)

[I](http://byeah.github.io/) am a third year CS PhD at Cal, working with Prof. [John Canny](http://www.eecs.berkeley.edu/~jfc/), 
on topics like making machine learing more easier to use. Checkout our [BIDMach](http://bid2.berkeley.edu/bid-data-project/) project.

[Here](https://www.dropbox.com/s/c30gyw7p88rikkf/viz.ipynb?dl=0) is the ipython notebook I will use in the talk.
This will be similar to our data science [class](https://bcourses.berkeley.edu/courses/1377158/).

## Discussion: Topic Description

Please insert your topic description here. **Bold** text, _italic_ text, 
[hyperlinks](www.google.com), and other markup follow markdown syntax. 

Please place any tutorial materials in the 
[master branch of this repository](https://github.com/thehackerwithin/berkeley/tree/master) 
and link to them from this post 
[like so](https://github.com/thehackerwithin/berkeley/tree/master/IPython). 
For help 
and questions, please 
[file an issue](https://github.com/thehackerwithin/berkeley/issues/new) 
or email Katy.


## Lightning Talks

Finally, there will be a time for a couple of **Lightning Talks**, which are 
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
