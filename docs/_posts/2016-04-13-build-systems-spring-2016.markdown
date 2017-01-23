---
layout: post
title: Build Systems - Tony Kelman
comments: true
category: posts 
tags: meeting make reproducibility
---


## Attending

- lots!


## Tony Kelman

Tony is a lecturer in Mechanical Engineering, and a core contributor to the Julia language. He likes building things, including scientific software.

## Build systems

Yay open source! So there's some cool library you want to use, and its author was kind enough to share the source code with the world. But maybe that's all that they provided? Or you want to change something, fix a bug, add a feature, etc. For libraries written in compiled languages like C, C++, Fortran, etc, compilation and dependencies can be hard. There are a variety of build systems commonly used by open-source projects to assist in building libraries and managing dependencies across various platforms. I'll talk about the [GNU autotools][autotools] (and Make), [CMake][cmake], and briefly mention [gyp][gyp]. I'll work through an example using a small but nontrivial C library.

Code examples can be found [here][code].


[code]: https://github.com/thehackerwithin/berkeley/tree/master/build_systems "Code Examples" 
[autotools]: https://en.wikipedia.org/wiki/GNU_Build_System "Autotools"
[cmake]: https://cmake.org/ "CMake"
[gyp]: https://gyp.gsrc.io/ "gyp"
