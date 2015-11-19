---
layout: post
title: scikit-learn - Ross Barnowski and Shannon McCurdy
comments: true
category: posts
tags: meeting python data
---

## Attending

- Anyone is welcome. We hope you'll join us!

## Meeting Info

- When: 4:00pm - 5:30pm
- Where: [BIDS, Room 190 of Doe Library](https://bids.berkeley.edu).
- Who: Anyone interested in software development best practices is welcome to come to our meetings.
- How: A predetermined main topic (45 minutes) will be followed by impromptu lightning talks (5 minutes each)

## Ross Barnowski

Ross is a Nuclear Engineering PhD student in Kai Vetter's group.

## Shannon McCurdy

Shannon is a postdoc in computational biology.  

## Discussion: scikit-learn

**Ross** walked us through a demo notebook which can be found 
[here](https://github.ocm/thehackerwithin/berkeley/tree/master/sklearn/sklearn_intro.ipynb). 
You can clone it from github.com/thehackerwithin/berkeley.

**Shannon** walked us through some useful resources. The documentation for sklearn 
seems to parallel a book called [The Elements of Statistical 
Learning](statweb.stanford.edu/~tibs/ElemStatLearn), and Shannon recommends 
this as a resource.

### Linear Regression

If y is nx1 and x i nxp, we have an unknown coefficient matrix W, which is px1. 
The error term is then nx1. The assumption is that x and y are linearly 
related. The fit, W, minimizes the vertical error. The least squares cost 
function, which comes up in regression in this way, is a model for the error.

Note that in this example, when p>n, we enter a danger zone for validity of 
this model. Shannon wanted us to note, in this context, scikit-learn doesn't 
necessarily warn you when this happens. So, don't trust that scikit-learn will 
always warn you if you aren't using the models in the appropriate regime.

### Shrinkage Models

A bunch of different shrinkage models are included in scikit-learn. One that 
Shannon uses in her work is Lasso.

The idea, functionally, is that we add a penalty to the least squares cost 
function. The penalty is related to the magnitude of each coefficient. That is, 
if you are going to add some nonzero element in the matrix, it must contribute 
well to the fit with y. This is a parsimony metric which enforces sparsity in 
the solution vector. This helps with interpretability because it emphasizes 
the most important coefficients. 

### In the Wild

Shannon has encountered least squares and lasso in two different problems in 
her work. 

Example: In her research she looks into event times, where only a subset 
(half) of the events are recorded. Using an exponential probability and an 
indicator (whether or not an event was recorded), she can describe the 
probability of an event happening. Given this, she can separate the probability 
into a maximum likelihood problem which can be minimized (using exponential 
regression) to determine the least squares soluation and she can reframe the 
Newton-Raphson step into an ordinary least squares lasso situation. If you 
didn't follow this completely, check out [Tibshirani's website on the general 
topic of lasso models](http://statweb.stanford.edu/~tibs/lasso.html).


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
