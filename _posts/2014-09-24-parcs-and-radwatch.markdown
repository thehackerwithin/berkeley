---
layout: post
title: PARCS and RadWatch (without the physics) - Sandra Bogetic and Ryan Pavlovsky 
comments: true
category: posts
tags: meeting parcs shell
---


# Attending

- Sandra Bogetic
- Christian DiSanzo
- Alejandra Jolodosky
- James
- Kelly Rowland
- Jasmina Vujic
- Rachel Slaybaugh
- Massimiliano Fratoni
- Katy Huff
- Dan Wooten
- Aaron Culich
- Madicken Munk
- Kedar Kolluri
- James Bevins

# Discussion: PARCS

## Sandra Bogetic

Sandra Bogetic is a first year graduate student in the Nuclear Engineering 
Department. 

## PARCS

PARCS is a powerful tool, but it seems to have struggles with version control, 
and would strongly benefit from a more transparent and controlled release 
procedure.

Since it is an NQA-1 code.... its surprising that it is not under version 
control.

### Input Files

- Generation of cross sections can be done in various ways. These include 
  CASMO, HELIOS, and TRITON 
- The input for thermal hydraulic behavior can be enered into PARCS or coupled 
  using PATH, TRACE, and/or RELAP. For a PWR, you can do it in TH. 
- Depletion can be done by PARCS, but sometimes you don't want to do it with 
  PARCS because perhaps you have done depletion in some other code (such as 
  SIMULATE). PARCS allows you to input this external data.
- The input file formatting is in blocks.
  - CNTL, XSEC, GEOM, PARAM, TH, TRAN, etc.
  - ata can be repeated using an asterisk
  - Input ends with a .
  - etc.


### Options

There are many options that can or should be specified. The core type, core 
power, simulation behavior concerning Xe and Sm (will you input the values, do 
you want them to be at equilibrium, transient, etc), control rod banking 
positions, external thermal hydraulics linkages, print options, whether or not 
to conduct depletion, etc.

Additionally, there is a tree variable for cross section definitions.

The geometry card of course is very important. The core compositions are all 
defined for the assemblies, reflector, etc. Typical boundary conditions are 
available.

### Running the input


### Examples

Examples can be found in the presentation, but will not be shared online. 

# Discussion: RadWatch (without all the physics)

## Ryan Pavlovsky

Ryan is a graduate student in the Nuclear Engineering Department. 

## Linux and Unix tools within RadWatch 

### The stack

Sensor input, python, smpt, datetime, python, cron, scp, ssh, ssh-agent, pytables, 
matplotlib, scp, yes, drupal, jquery

### CROn

CROn is for scheduling jobs. 

Crontab -e can be used to edit the cron file for your user space. Don't freak 
out if it's empty. Just use a template from your toplevel cron file or find a 
template on the internet to fill out. 

Ryan reminds us of the importance of the man page. If you need more help with 
the crontab command, try man crontab in your terminal to figure out its 
secrets. (Man pages are opened in a program called less. So, to get out of the 
man page, type "q".)

Note that your system may have a cron.allow file. That file, if it exists, 
names the people allowed to create cron jobs.

### SSH

Ryan points out that there are two versions of ssh (client and server). They 
have their own configuration files!

Note the config file located in `/etc/ssh/ssh_config`, but also, note the one 
in your home directory `~/.ssh/config` and the one for server daemon 
configuration `/etc/ssh/sshd_config`. NOTE: on MACOSX, there may not be an 
additional ssh directory layer in etc. So, find those files at 
`/etc/ssh_config` and `/etc/sshd_config`.

**Fun Fact** DSA has a stronger random number generator than RSA, but RSA is 
used more widely. This is likely because RSA encription is faster and (more 
compressed?) than DSA.


Code examples from Ryan's talk can be found [here in the master 
branch](https://github.com/thehackerwithin/berkeley/tree/master/cron_ssh).


