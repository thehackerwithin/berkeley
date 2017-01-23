---
layout: post
title: Raspberry Pi Hacking - Ryan Pavlovsky
comments: true
category: posts
tags: meeting
---



# Attending

- Ryan Pavlovsky
- Katy Huff
- Ryan Bergmann
- Josh Howland
- Prof. Rachel Slaybaugh
- Kelly Rowland
- Ross Barnowski
- Tomi Akindele

# Lesson: Raspberry Pi

Ryan Pavlovsky, a student in Kai Vetter's research group, gave an excellent 
presentation about what he's done with the raspberry pi. 

Stuff that we discussed : 

- How did you get this?
- What are the peripherals that work with it?

  - gpu/cpu
  - broadcomm video card
  - ARM processor, 700 MHz
  - 512 MB memory
  - JTag header?
  - USB/Ethernet
  - SD card additional memory
  - Raspbian operating system

- What example projects are cool?

  - smart kegerator (monitors flow rates, temperatures, accounting, facial 
    detection)
  - Quake III 
  - cluster of pis. built mpi on it. rack made of legos!

- Demos!

  - pong, a ping sensor. Sends a ping, measures time to return.
  - ping, a program that acquires pong senses over time.
  - simon says, computer tells you what to do, based on ping
  - GEANT4 

    - 4.10 C++ implementation
    - networked raspberry pi
    - edited ~/.bashrc for data

Code examples for the demo can be found [here][code].

# Lightning Talks 

We talked, in an ad hoc fashion about the hearbleed OpenSSL bug. 


[code]: https://github.com/thehackerwithin/berkeley/tree/master/raspi "Code Examples" 
