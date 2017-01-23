# BRC and NE

## Visit From BRC Representatives Upcoming


Notes from that meeting should go here. 


## Personas

There are many types of people in the BRC user community associated with NE 
and/or THW. To help BRC staff envision the way in which we can be expected to use 
their resources, the following "Personas" attempt to describe the archetypal 
people in our community.

Note that these names are supposed to be informative rather than offensive. 
Each character is actually a composite of many people I have encountered around 
the department and is not intended to target a specific individual.


### Professor Patty Productive 

Professor Productive is an assistant professor with lots of different projects. 

Most importantly, she has access to a couple of export controlled pieces of 
source code created by the X National Laboratory. She'd like to maximize her 
productivity by sharing that code with a few of her graduate students and the 
postdocs who are interested in her work.  She can share the source code freely 
with citizens, as long as she tells X National Lab who they are.  However, 
she'll get in big trouble if she shares the code with non-citizens. Those users 
have to ask explicitly for permission from X Lab. Citizen of certain nations 
are unlikely to ever get approval.  

Professor Productive may want to install some of the software on the cluster 
herself. Often, however, she'll ask her graduate student, Hallie Hacker, do 
the installations and keep track of various users. 

**How can Professor Productive and Hallie Hacker manage this permissions 
quagmire without it becoming a full-time job for either of them?**


### Hallie Hacker

Hallie is a new graduate student who plans ambitious projects on novel 
architectures. She's interested in the cluster, but may spend a lot of her time 
running simulations on GPUs instead. As part of her work for Professor 
Productive, she sometimes needs to install stuff on the cluster and manage the 
permissions. This gives Hallie lots of great UNIX-fu, but because she's 
becoming an expert Hallie often finds herself helping other students use the 
cluster as well.

**Where is the BRC documentation to which Hallie can direct other graduate students in 
order to avoid becoming a one-woman help-desk?**


### Nate Newbie

Nate is a masters' student. Since he only has two years, he needs to get up to 
speed quickly. He's supposed to run some simulations on the cluster with a 
piece of code that is already installed there, but he's not very familiar with 
clusters. This is the first time he's ever used ssh, in fact, and he feels a 
little lost. His MS advisor, Dr. Wisdom, is very helpful with the physics theory, 
but never uses the cluster himself. So, Nate sometimes he asks Hallie for help. 
She doesn't seem to have a lot of time, though, and Nate is afraid to run a 
job on the cluster without advice. He's sure he'll end up misusing it by 
accident, which would really annoy his colleagues. 


**Where can Nate find enough information to confidently run slurm jobs 
correctly?**


### Frank Flux

Frank is a more senior graduate student. His work is very mature, and he's 
planned an ambitious thesis with a parametric analysis over dozens simulation 
parameters with perturbation values ranging across many magnitudes.  He's done 
planning his work, so he'll be spending the next year running as many 
simulations as possible.  He's a self-starter, so he doesn't need much help 
installing things. He's also great asset to cluster managers who like to 
see active cores. However, the length of his average slurm job is around four 
days, so other users sometimes wonder when they'll get a turn at the cores they 
need.

**How can Frank maximize his CPU hours without derailing less-prolific users?**

### Alice Agile

Alice is a postdoc in the department. She works on a lot of open source code 
and tools for nuclear engineers. For this reason, she'd like to install all of 
those tools on the cluster with open-access permissions. The only hiccup for 
Alice is that most of these tools have a fast release cycle, with new stable 
releases every few months. She'd like to make sure that students and professors 
in the department have access to the newest versions as well as older versions 
that they will come to rely on.

**How can Alice create multiple versions of modules every couple of months 
without polluting the module namespace or creating dependency hell for other 
users?**




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

Pledge is for generating time-sensitive one-time-use, two-factor-authentication
passwords. That's awesome. Many of you may have seen or used the passkey
generating RSA keys that are used to log into the national laboratory networks.
How many use google two-factor authentication for their email or something
similar? I do.  [google2factor].

#### Create a Pledge profile

You will only need to create a Pledge profile once for logging into Savio.

 1. Open a browser and navigate to [Pledge Enrollment](https://identity.lbl.gov/PledgeEnrollment/enroll.jsp)
 2. Enter your Savio Cluster username and the 10-digit password given to you by Krishna at LBL for token enrollment. If you do not have this password or have forgotten your password contact the BRC support group by sending email to [brc-hpc-help@lists.berkeley.edu](mailto:brc-hpc-help@lists.berkeley.edu)
 3. Choose the realm as "HPCS"
 4. Click Enroll.
 5. You will be presented with an 8-digit Profile ID that you can enter into the field in the Pledge app on your new device.

#### Installing Pledge on a device

To fully install and configure Pledge on each of your devices you must first download and install the software on your smartphone or computer, and then download onto the device the profile you created in the previous section.

##### On your smartphone or computer install the latest version of the Pledge Software Token (v2.2-29275 as of Feb 5, 2014):

 - [iOS](https://itunes.apple.com/us/app/pledge/id312071093?mt=8)
 - [Android](https://play.google.com/store/apps/details?id=se.nordicedge.pledgeotp)
 - [Mac OS X](http://downloadcenter.mcafee.com/products/McAfee_Pledge/2.2/pledge_2.2-29275_macosx.zip)
 - [Windows 64-bit](http://downloadcenter.mcafee.com/products/McAfee_Pledge/2.2/pledge_2.2-29275_win64.exe)
 - [Linux 64-bit](http://downloadcenter.mcafee.com/products/McAfee_Pledge/2.2/pledge_2.2-29275_lin64.bin)
 - For other platforms, go directly to the [McAfee Pledge downloads](http://www.mcafee.com/us/downloads/otp-pledge-software-token.aspx).

##### Download the profile to your device

 1. In the Pledge window, click the + button to start the process.
 2. Enter the profile ID from the Pledge Enrollment dialog box into the Pledge client and click OK.
 3. Create PIN code and click OK. This PIN is unique to this particular device, and you'll need to enter it each time you use this device to generate a one-time password.
 4. Test this new profile by clicking the Test Pledge Profile link in the Pledge Enrollment window.
 5. Click the Generate one-time password button in the client window to get a randomly generated one-time password.
 6. Enter your PIN code to confirm that it's you doing this.
 7. Enter that password into the appropriate field in the Enrollment dialog box and click the verify button.
 8. You should get a "Success" message.

#### Use Pledge on your device to generate a one-time password to log into Savio

 1. Launch Pledge on the mobile or desktop client that you will be using to generate one-time passwords.
 2. Click the Generate one-time password button.
 3. Enter your PIN code and click OK.
 4. On a mobile device, you might need to touch the "enter" key on the keyboard.
 5. Use the 6-digit one-time password displayed.

Token Lockout (September 2012):
  - On 4 failed OTP attempts, the user's OTP account will be locked for 10 minutes.
  - After 4 more failed OTP attempts, the user's account will be locked for 90 minutes.
  - After 4 more failed attempts, the account will be locked until reset by an administrator.

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


First, I went ot the place where I want to install it. 

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








[google2factor]: https://www.google.com/landing/2step/
