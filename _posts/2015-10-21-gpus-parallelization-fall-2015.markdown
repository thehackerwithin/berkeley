---
layout: post
title: GPUs and Parallelization - Biye Jiang, Aaron Culich 
comments: true
category: posts
tags: meeting hardware hpc
---

## Attending

- Anyone is welcome. We hope you'll join us!

## Meeting Info

- When: 4:00pm - 5:30pm
- Where: [BIDS, Room 190 of Doe Library](https://bids.berkeley.edu).
- Who: Anyone interested in software development best practices is welcome to come to our meetings.
- How: A predetermined main topic (45 minutes) will be followed by impromptu lightning talks (5 minutes each)

## Biye Jiang

[Biye Jiang](https://byeah.github.io/) is a PhD student at UC Berkeley in the 
CS department working with John Canny. 

## Aaron Culich

Aaron is a research computing architect at Berkeley. 

## Discussion: GPUs and Parallelization

Today's topic is about GPUs and parallelism. 

### Survey of Needs and Resources -- Aaron Culich

Aaron referenced a presentation on this topic. It can be found 
[here](http://parlab.eecs.berkeley.edu/sites/all/parlab/files/BootCamp_Computational_Patterns_Demmel_final_12v2.pdf).

Aaron started this presentation with a survey of what the attendees are 
actually using.

- GPUs? 3 folks.
- Other Parallelization? Lots of folks.

### Python Parallelism

It was mentioned that, for some folks, python is the language of choice. The 
Python Multiprocessing module was mentioned. This was the topic of a THW 
session last year. The THW resources on this topic can be found 
[here](https://github.com/thehackerwithin/berkeley/blob/master/python_concurrency). 
That session was not on GPUs, however, the python threading module can be used 
in conjuction with PyCUDA, a python module for GPUs. 

### Research IT -- Krishna Muriki

[Research IT](research-it.berkeley.edu) is available as a resource for 
individuals who would like to test their code on GPU resources. Krishna 
Muriki expresses that there is an institutional shared linux cluster (Savio). 
Within that cluster, there are 6 compute nodes with 4 kepler GPUs each.
Those nodes are in testing and BRC is interested and open to new users.

### Java runtime engine -- Oliver

Oliver at ESPM has a javascript modeling project for agent based population 
models. They are working to make their software scalable from the desktop to 
the level of higher performance computing. The NOVA stack and 
[XSEDE](https://www.xsede.org/) resources 
are core to their efforts. 

### Scala Demo -- Biye Jiang

Biye demonstrated the speed of GPUs by conducting a matrix multiplication using 
GPUs versus conducting the same multiplication using CPUs. 

### GPU Discussion

Biye shared some of the diagrams from [this 
presentation](http://on-demand.gputechconf.com/gtc/2014/presentations/S4811-extreme-machine-learning-with-gpus.pdf).

He noted 

- GPUs give excellent speed, 
- but GPU memory latency is also an issue. 
- So the throughput is high, but so is the memory latency.  
- If you want your GPU code to run quickly, optimize for throughput. 
- Always remember, GPU memory access is slower than computation. 
- Moving data between the GPU and the main memory should be avoided.

### GPU BIDMat demo

Biye presented an ipython notebook to demostrat how BIDMat works. 

The ipython notebook demos are [here](https://github.com/BIDData/BIDMach/blob/master/tutorials/).

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
