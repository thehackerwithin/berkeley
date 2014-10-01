A simple discussion of the CROn (command run on) and the secure shell tools set. RadWatch is an example where these tools are employed.

REQUIRED:
- Openssh
- Unix environment

COMPATIBILTY WARNING:
- Refer to your man pages about configuration files! Different *nix systems prefer different file structures, although the commands are mostly the same

HIGHLIGHTS:
- Automated systems can be implemented with *nix tools
- CROn is a very widely used utility for running tasks on a regular schedule
  - Common gotchas include that CROn jobs are run with /bin/sh, this is a pointer to /bin/dash on Ubuntu systems.  
  - Your `env` may be different based on the pointer /bin/sh
  - SSH is a secure, flexible way to administer remote tasks 
  - sshd and ssh are the server and client applications with openssh
  - man ssh reveals that -F can be used to specify a configuration file. If -F is not present ``/etc/.ssh/ssh_config`` (on UBUNTU!) is consulted. Users can uniquely configure their ssh environment by editing ``~/.ssh/config``
  - Save typing by configuring ``~/.ssh/config`` (UBUNTU!). 
- Key-based authentication SSH
  - Asymetric keys can allow for SSH sessions without sending your pw over the internet
  - RSA,DSA choice. RSA is more popular, RSA is faster when encrypting at equal bit depth. I think this is the popular decision because admins of servers may provide many simultaneous connections at once and want to reduce loading of their resources if possible. DSA is fixed at 1024 in length by a NIST Standard FIPS 186-2, man ssh-keygen for more details. Based on this DSA and RSA can't really compete since RSA could simply become 'more secure' by adding more bit depth.
  - ssh-keygen, encrypt your key with a pw and distribute your .pub(lic) key to all servers you want to login to.

