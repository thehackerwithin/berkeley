---
layout: post
title: HPC Module Installation and Plotting Tools - Everyone!
comments: true
category: posts
tags: meeting hpc plotting
---


# Attending

- Ross Barnowski
- Sandra Bogetic
- Aaron Culich
- Denia Djokic
- Andy Haeffer
- Jason Hou
- Katy Huff
- Alejandra Jolodosky
- Madicken Munk
- Kelly Rowland
- Rachel Slaybaugh
- Daniel Wooten
- Andy Haefner
- Ryan Pavlovsky
- Cameron Bates
- Ross Barnowski
- Tenzen Joshi
- Dav Clark

# Discussion: Installing Modules on the BRC Savio Cluster

## Katy Huff

[Katy Huff](http://kathuff.github.io) is a postdoctoral scholar with the 
Nuclear Science and Security Constortium and is a fellow with the Berkeley 
Institute for Data Science. 

## Module Installation Tips and Tricks

I spent some time last week installing MOOSE on the cluster. The dream was
this: MOOSE should be a module that anyone can use on the cluster if they
import it. There are a couple of catches to this.

- MOOSE's dependencies can each be compiled with an array of flags, should I
  compile only debug versions, only non-debug versions, both?
- MOOSE has a bunch of associated libraries which do various physics. I would
  also like to install those, but they have varying permissions.



### Logging in

Setting up easy login situaiton is a two step process:

- install pledge
- create aliases for the ssh commands

#### Installing Pledge Somewhere

Pledge is for generating time-sensitive one-time-use, two-factor-authentication
passwords. That's awesome. Many of you may have seen or used the passkey
generating RSA keys that are used to log into the national laboratory networks.
How many use google two-factor authentication for their email or something
similar? I do.  [google2factor].

This is annoying because it takes a long time to get to the final url with
which to install Pledge. But, you will eventually succeed. Use the username and
password given to you by Krishna at LBL.

1. Install Pledge. The easiest is likely to do this on your phone using whatever
 app installation store is appropriate. 
2. Go here (https://identity.lbl.gov/PledgeEnrollment/enroll.jsp), select HPCS 
from the pulldown window, and enter your user name/password that Krishna from 
LBNL sent to you. This should provide an 8 digit profile ID.
3. Open Pledge and click the + button. It should ask for your profile ID (the 
thing you just generated); enter it, and it should download your "Pledge profile."
If you get an error, contact Phil Goorman for trouble shooting advice.
4. Make a pin number.  The pin is specific for that profile.
5. When you log into the savio cluster you will use this app to generate a new
password everytime. 


### Installing Dependencies

Typically, installation requires :

- getting your environment right
- downloading the source code for the dependencies
- following the instructions for each of those

MOOSE relies on two main external dependencies:

- HYPRE
- PETSc

It also relies on one internal dependency, libMesh. LibMesh is independent of
MOOSE, but since MOOSE has added non-standard features to libMesh, they keep
their own flavor of libMesh in the MOOSE framework source code. Clear as mud?

Thankfully, MOOSE is a well-documented open source project. It walks through
the installation of dependencies as well as the framework.


#### Environment

To deal with the environment, I edited ~/.bashrc so that it now looks like:


    # .bashrc

    # Source global definitions
    if [ -f /etc/bashrc ]; then
         . /etc/bashrc
    fi

    # User specific aliases and functions

    export CLUSTER_TEMP=`mktemp -d /tmp/cluster_temp.XXXXXX`

    umask 0022

    export GRP_DIR="/global/home/groups/ac_nuclear"

    export PACKAGES_DIR="$GRP_DIR/MOOSE/moose-compilers”



That makes sure that the packages will be downloaded to the right place
(CLUSTER\_TEMP), installed in the right place (PACKAGES\_DIR), and linked to
the right place (GRP\_DIR).


For this to take effect, the terminal needs to re-initialize itself with :

    source ~/.bashrc

#### Downloading the Dependency Source

This can be done using curl.

    curl -L -O --insecure https://computation.llnl.gov/casc/hypre/download/hypre-2.8.0b.tar.gz
    curl -L -O http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.4.3.tar.gz


#### Installing Hypre


First, I went to the place where I want to install it.

      cd $GRP_DIR


Install Hypre according to the instructions. That went well, creating the
beginning of a module called moose-dev-gcc. Sso there's nothing interesting to
share. The interesting stuff is when things go wrong.


#### Installing PETSc

I started to configure PETSc
Install PETSc - OOOPS - stop installing petsc and install valgrind

load the moose-dev-gcc module that has now been created
load valgrind

configure petsc


    xxx=========================================================================xxx
     Configure stage complete. Now build PETSc libraries with (legacy build):
       make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug all
     or (experimental with python):
       PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug ./config/builder.py
    xxx=========================================================================xxx


Now what?

I read the docs, and chose the legacy build because the moose docs say:

During the configure/build process, you will be prompted to enter the correct make commands. Because this can be different from system to system, I leave that task to the reader. However, I have received better results when following the non-experimental commands.
   make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug all


It worked !

    Completed building libraries
    =========================================
    making shared libraries in /global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3/arch-linux2-c-debug/lib
    building libpetsc.so
    =========================================
    Now to install the libraries do:
    make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug install
    =========================================


So, I did that:

    [huff@ln001 petsc-3.4.3]$ make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug install
    *** Using PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/stack_src/petsc-3.4.3 PETSC_ARCH=arch-linux2-c-debug ***
    *** Installing PETSc at prefix location: /global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt  ***
    ====================================
    Install complete. It is useable with PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt [and no more PETSC_ARCH].
    Now to check if the libraries are working do (in current directory):
    make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt test
    ====================================
    [huff@ln001 petsc-3.4.3]$

So, I ran the tests:

    make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt test

Here’s the output:

    [huff@ln001 petsc-3.4.3]$ make PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt test
    Running test examples to verify correct installation
    Using PETSC_DIR=/global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt and PETSC_ARCH=arch-linux2-c-debug
    Possible error running C/C++ src/snes/examples/tutorials/ex19 with 1 MPI process
    See http://www.mcs.anl.gov/petsc/documentation/faq.html
    --------------------------------------------------------------------------
    WARNING: There is at least non-excluded one OpenFabrics device found,
    but there are no active ports detected (or Open MPI was unable to use
    them).  This is most certainly not what you wanted.  Check your
    cables, subnet manager configuration, etc.  The openib BTL will be
    ignored for this job.

      Local host: ln001.brc
    --------------------------------------------------------------------------
    lid velocity = 0.0016, prandtl # = 1, grashof # = 1
    Number of SNES iterations = 2
    Possible error running C/C++ src/snes/examples/tutorials/ex19 with 2 MPI processes
    See http://www.mcs.anl.gov/petsc/documentation/faq.html
    --------------------------------------------------------------------------
    WARNING: There is at least non-excluded one OpenFabrics device found,
    but there are no active ports detected (or Open MPI was unable to use
    them).  This is most certainly not what you wanted.  Check your
    cables, subnet manager configuration, etc.  The openib BTL will be
    ignored for this job.

      Local host: ln001.brc
    --------------------------------------------------------------------------
    lid velocity = 0.0016, prandtl # = 1, grashof # = 1
    Number of SNES iterations = 2
    [ln001.brc:54921] 1 more process has sent help message help-mpi-btl-openib.txt / no active ports found
    [ln001.brc:54921] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
    egrep: /global/home/groups/ac_nuclear/MOOSE/moose-compilers/petsc/petsc-3.4.3/gcc-opt/arch-linux2-c-debug/include/petscconf.h: No such file or directory
    Possible error running Fortran example src/snes/examples/tutorials/ex5f with 1 MPI process
    See http://www.mcs.anl.gov/petsc/documentation/faq.html
    --------------------------------------------------------------------------
    WARNING: There is at least non-excluded one OpenFabrics device found,
    but there are no active ports detected (or Open MPI was unable to use
    them).  This is most certainly not what you wanted.  Check your
    cables, subnet manager configuration, etc.  The openib BTL will be
    ignored for this job.

      Local host: ln001.brc
    --------------------------------------------------------------------------
    Number of SNES iterations =     4
    Completed test examples




On first glance, maybe it passed, right? WRONG! It failed, yo. *The first rule
of programming is: Google the error.* Googling it, of course, this sends us to
a discussion on the petsc-users list host - exactly what we want - [right
here](http://lists.mcs.anl.gov/pipermail/petsc-users/2014-July/022325.html)
Interestingly, the question comes from someone at LBL. Perhaps it's even on the
same BRC system?  In any case, Barry Smith, who leads the PETSc project, responded...

> Well it is running. It is just producing annoying warning messages. You need
> to talk to your local MPI expert on that system for how to get rid of the
> problem.
> Barry


Since I don’t have any idea who in BRC is the MPI guru willing to solve it, I
guess we just make a note of it and go on with our lives.  So, moving on, I had
to clone moose.

- I hate using github’s ssh protocol, so I set up my ssh keys for
the brc cluster [this is how that works](https://help.github.com/articles/generating-ssh-keys).
- I have a fork of moose (which currently exactly parallels
moose development), so I cloned from that.
- I also fetched the upstream idaholab/moose repo so that I can keep up to date.
- MOOSE likes a clean history, so every time you pull, you have to rebase
  (we all make choices...) ``git pull --rebase upstream master``







# Lightning Talks 

## Ross Barnowski : PyQT

So, pyqtgraph is good for volumetric rendering. There are a lot of example scripts, 
so you can copy those. Additionally it is good for making fast video graphics 
(better than matplotlib).


## Alejandra : MATLAB ternary plots

Alejandra shared a ternary plotting thing. 


## Andrew Hefner : Mayavi

[Mayavi uses vtk, which is pretty powerful, but it's a python interface. 
Additionally, it uses syntax that will be familiar to the matlab users. 

There are various interesting features in Mayavi. Quiver, for example, is a 
really basic function call that generates vector fields. 
http://docs.enthought.com/mayavi/mayavi/

## Ryan Pavlovsky : DyGraph

[Dygraphs](http://dygraphs.com/) is a nice, lightweight, and interactive. So, 
it's great for websites, because you just drop a single javascript file. 

## Katy Huff : yt (and what is plotly?)

Katy likes and is impressed with yt. She is curious but nervous about 
[plotly](http://plot.ly). 

## Dav Clark : Bokeh

It's architected to have a javascript frontend and is meant to be hooked into 
generic data servers. 

It has cool zooming capabilities in the gui and has neato feature like linked 
brushing so that two plots are linked and can be interacted with using a single 
tool in one of the windows.




[code]: https://github.com/thehackerwithin/berkeley/tree/master/topic "Code Examples" 
[google2factor]: https://www.google.com/landing/2step/
