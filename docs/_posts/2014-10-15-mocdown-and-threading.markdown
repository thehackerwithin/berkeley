---
layout: post
title: MocDown and Python Threading - George Zhang, Phil Gorman, Ross Barnowski
comments: true
category: posts
tags: meeting mocdown python
---


# Attending

- George Zhang
- Phil Gorman
- Chick Markley
- Max Fratoni
- Aaron Culich
- Xiao Fan
- Kyle Barbary
- Madicken Munk
- Alejandra Jolodosky
- Denia Djokic
- Ross Barnowski
- Katy Huff
- Joey Curtis
- Kelly Rowland
- Andy Haefner
- Caroline

## Discussion: MocDown

### George Zhang and Phil Gorman

George and Phil are both PhD students in the Berkeley neutronics group. 


### MocDown

[MocDown](http://ucb-rdn.github.io/projects/mocdown/mocdown.html) is a neutron 
transport, transmutation, thermal fluids, and equilibrium search tool developed 
here at Berkeley primarily by Jeffrey Seifried.

George and Phil covered :

- What does MocDown do?
- What is going on in the input files?

Code examples and documentation can be found at [the homepage](https://jeffseif.github.io/MocDown).

## Discussion: Threading with Python

### Ross Barnowski

Ross Barnowski is a PhD student in Kai Vetter's research group. His work 
focuses on nuclear instrumentation, including a 3D gamma ray imaging cart 
called the [Compact Compton Imager II](https://conference.scipy.org/scipy2014/schedule/presentation/1714/). 


### Threading in Python

Ross gave a talk that covered the concept of concurrency as well as how to make 
it happen in Python. 

Code examples can be found [here][threading].

To see the ipython notebook in the notebook viewer try this link: [Concurrency 
  Notebook](http://nbviewer.ipython.org/github/thehackerwithin/berkeley/blob/master/python_concurrency/Concurrency%20in%20Python.ipynb).


# Lightning Talks 

## Kelly : Test Your Code

Kelly, after having dedicated a ton of time this summer to building tests for 
the WARP code, now has a test suite for it. When her colleague, the main WARP 
developer, made an update to the API, her tests caught it (by failing) and she 
was alerted to the global effects of the change. Moral of the story: test your 
code!


## Aaron Culich : BRC 

Aside: One of the places where tests break down is in concurrency, actually! Aaron 
recommends a paper ["The Problem With Threads" by Edward
Lee](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf). He also
offers us some choice quotes:

> "...non-trivial multi-threaded programs are incomprehensible to humans."

and

> "Threads must be relegated to the engine room of computing, to be suffered
> only by expert technology providers."

Aaron also passed out a little handout about BRC. He encourages folks to reach out 
to him (as part of the Consulting and Community initiative). One of the ways 
for him to help out is here with THW, where he wants to hear our needs and 
feedback. 

They've already benefitted from our feedback concerning Savio 
[here](https://github.com/thehackerwithin/berkeley/tree/master/brc). Please 
feel free to add more information to that file with a pull request. 

- In response to the need for a simpler Pledge setup documentation, they've 
created better docs 
[here](https://github.com/ucberkeley/brc-draft-documentation/wiki/Logging-into-Savio). 

- In response for the need for example run files, they've created a repository 
[here](https://github.com/ucberkeley/brc-draft-documentation)!

[threading]: https://github.com/thehackerwithin/berkeley/tree/master/python_concurrency "Threading Code Examples"


