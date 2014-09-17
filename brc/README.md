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
