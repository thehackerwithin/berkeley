---
layout: post
title: High Performance Python - Chick Markley
comments: true
category: posts
tags: meeting hpc python
---

## Attending

- Anyone is welcome. We hope you'll join us!

## Meeting Info

- When: 4:00pm - 5:30pm
- Where: [BIDS, Room 190 of Doe Library](https://bids.berkeley.edu).
- Who: Anyone interested in software development best practices is welcome to come to our meetings.
- How: A predetermined main topic (45 minutes) will be followed by impromptu lightning talks (5 minutes each)

## Chick Markley

Chick Markley does work with the Aspire lab at UC Berkeley.

## Straw Man High Performance Python Example

First, some aphorisms:

- Programmer hours are more important than cpu hours - cook
- Premature optimization is the root of all evil - Knuth
- etc.

Next, an example of a laplacian.

Chick put his arrays into various data structures (lists, numpy arrays, etc.)

Interestingly, lists performed better than naive numpy arrays, but then once 
you vectorize the numpy arrays, that helps a lot and is much much faster. It's 
of course much much better if you use the built in scipy laplacian (faster 
because it's written in c). You can do well with cython too, but ultimately, 
you get a lot better performance by loading a c library.

We can also parallelize. Parallel operations vary from embarassingly parallel 
to inscrutably parallel. One can do so on many devices (many noces, MIC, GPU...),
many frameworks (pyspark, openmp, opencl, cuda...). But, once must inform the 
compiler which loops to parallelize, etc. 

One can also "roofline" one's system with "shocdriver" or a similar tool to 
benchmark the system. In particular, it shows what kind of performance 
constraints are characteristic of your system. 

Another option is SEJITS, a framework that Chick works on. It selectively 
embeds just in time "specialization" (or, rather, optimization).

Tuning is another option. There's something called OPENTUNER. It will run your 
program numerous times to find the minimum amount of time to run the program. 

Wait - there's more hardware. One can build new hardware to solve your problem. 
Hardware isn't so hard anymore (maybe it should be called easyware.) 

There's an interesting "hardware construction language" that folks at Aspire 
came up with. It's called [Chisel](https://chisel.eecs.berkeley.edu/chisel-dac2012.pdf). 

