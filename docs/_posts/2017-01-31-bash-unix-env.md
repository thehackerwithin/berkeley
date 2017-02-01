---
layout: post
title: Navigating bash and UNIX environments -- Akos, Mitch, and Matthias
comments: true
category: posts
tags: meeting <+ tags +>
---

# Topics

- UNIX intro (some history, UNIX in society)
- UNIX design principles, or at least some of them, briefly
- Shells and command-line interface
- Shell scripting basics
- Cool tricks


# System requirements

Do you have a Mac? Open the **Terminal** app. You're done.

Do you run Linux? Open your computer. You're done.

Do you run Windows? See next section.

# How to get bash or a Unix-like environment on Windows

1. Install [Git Bash](https://git-for-windows.github.io). (Instructions copied from [here](https://github.com/dlab-berkeley/programming-fundamentals).)

  Download the Git for Windows installer. Run the installer and follow the steps bellow:

  * Click on "Next". (5 times)
  * Select "Use Git from the Windows Command Prompt" and click on "Next". If you forgot to do this programs that you need for the workshop will not work properly. If this happens rerun the installer and select the appropriate option.
  * Click on "Next". Keep "Checkout Windows-style, commit Unix-style line endings" selected.
  * Select "Use Windows' default console window" and click on "Next".
  * Click on "Next".
  * Click on "Finish".

  This will provide you with both Git and Bash in the Git Bash program.

2. Run Linux on a virtual machine, e.g., [VirtualBox](https://www.virtualbox.org/), or in a container, e.g., [Docker](https://docs.docker.com/engine/getstarted/step_one/).

3. Run Linux from an external USB storage device, e.g., [live USB instructions for Ubuntu](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows).

4. If you don't want to do any of that
  - Open a bash terminal at [try.jupyter.org](http://try.jupyter.org/)
  - If you have a GitHub account and can use `ssh`, https://dply.co provides 2 hours free server time. Set that up by yourself though.


# Learning resources

For those desiring something more structured, thoughtful, and professional...

- [List of Unix Commands](https://en.wikipedia.org/wiki/List_of_Unix_commands)
- Software Carpentry [Unix Shell Lessons](http://swcarpentry.github.io/shell-novice/)
- [The Command Line Murders](https://github.com/veltman/clmystery), a game to teach yourself the Unix CLI.
- [Advanced Bash-Scripting Guide](http://www.thehackerwithin.org/berkeley/upcoming.html) from The Linux Documentation Project
- O'Reilly [books on Unix & shell topics](https://ssearch.oreilly.com/?q=unix+shell)
- [How to find files](http://i.imgur.com/XUhbf2D.gif) hidden inside a computer
