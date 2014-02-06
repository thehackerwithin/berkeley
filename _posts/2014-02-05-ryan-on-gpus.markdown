---
layout: post
title: GPUs and CUDA - Ryan Bergmann
comments: true
category: posts
tags: meeting 
---



# Attending

- Ryan Bergmann
- Katy Huff
- Jankai (Jack) YU
- Dan Wooten
- Prof. Max Fratoni
- Sandra Bogetic
- Christian DiSanzo
- Josh Howland
- Prof. Rachel Slaybaugh
- Kelly Rowland
- Nikola Radnovic

# Lesson: GPUs and CUDA

Ryan Bergmann covered various features of GPUs and CUDA. Here is [Ryan's Tutorial][ryanstalk].


Things we learned include:

- **CUDA** stands for Compute Unified Device Architecture.
- **SIMD** stands for Single Instruction Multiple Data.
- GPUs are good for turning compute-bound problems into memory-bound ones.
- **CUDA cores aren't really cores** there are multiple cores per CUDA core.
- You have to use the SIMD lanes in order to get good performance out of a GPU system.
- **Coalesced reading and writing** means that your cores should be accessing 
  adjacent pieces of memory simultaneously.
- The memory latency is higher for GPUs than CPUs, but the GPU hides this better 
  the more threads you're running.
- The **host thread** launches the GPU kernel
- Threads are organized into blocks
- Blocks are organzied into grids 
- The grid is the kernel you have loaded.
- We learned how to launch a kernel for 


# Lightning Talks 

- Katy gave a quick lightning talk on [style guides][styleguides] for code.
- Kelly gave a more in-depth lightning talk on Laser Doppler Vibrometry.


[ryanstalk]: https://github.com/sellitforcache/cuda_tut "Ryan's Tutorial" 

[styleguides]: https://drive.google.com/file/d/0ByP1TmlNKprrcGdpaWJyeUZPb3c/edit?usp=sharing "Style Guides" 


