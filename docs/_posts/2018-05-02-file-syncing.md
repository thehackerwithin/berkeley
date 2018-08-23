---
layout: post
title: Tim Howes -- File syncing tools - syncthing, dat, git-annex
comments: true
category: previous
tags: meeting
---

## File syncing tools

I will discuss open source tools that you can use to sync files directly between
computers, rather than relying on paid cloud services such as dropbox.  These
can be especially useful when dealing with large scientific datasets, which may
be impractical to sync to the cloud, and for which you may want more control over
versioning information.  If you want something similar to a cloud service, but
with more control, you can set up these tools in your own virtual private server.

### syncthing
[syncthing](https://syncthing.net) is a cross-platform tool that can be used to
keep folders in sync between your own devices or to share with collaborators.
The settings can be customized to ignore certain files or sub-directories on
specific machines, and there are different options available for keeping copies
of old versions of files.

### dat
[Dat](https://datproject.org) is a protocol for peer-to-peer sharing of collections of files.  This has
similar advantages to sharing files using bittorrent, but it also includes the
ability to update the files in an archive and track the version history.

### git-annex
[git-annex](https://git-annex.branchable.com) is a tool that allows you to track large files within your git
repositories, and it gives you a high level of control over which clones of the
repository actually get the full file contents and which get only small placeholder
files.  This means that you can view and organize the full directory tree on your
local machine without having to actually download all the files, and you can download
the contents of individual files when needed using "git-annex get".  A special
git-annex branch tracks the locations of the file contents and ensures that the
correct number of copies exist on other machines before "dropping" the local file.


## Usage notes

### syncthing

Syncthing keeps folders in sync between machines by making a secure, direct connection between the machines (or optionally by using relay servers if a direct connection is not possible). It is a simple tool that can be started at the command line, run in the background, and viewed/controlled via a web browser.

#### Installation

https://docs.syncthing.net/intro/getting-started.html
https://docs.syncthing.net/users/autostart.html

Install and enable on Ubuntu:
```bash
sudo apt install syncthing

# Enable as automatic background service
# replace 'myuser' with your username
sudo systemctl enable syncthing@myuser.service
sudo systemctl start syncthing@myuser.service

# or run `syncthing` manually on the command line
```

Check status on Ubuntu:
```bash
#Check service status
sudo systemctl status syncthing@myuser.service

#Check logs
sudo journalctl -e -u syncthing@myuser.service
```

Install and enable on macOS: <br>
(First install homebrew: https://brew.sh/)
```bash
brew install syncthing

#Enable as automatic background service
cp /usr/local/Cellar/syncthing/latest/homebrew.mxcl.syncthing.plist ~/Library/LaunchAgents/syncthing.plist
launchctl load ~/Library/LaunchAgents/syncthing.plist

# run `syncthing` manually on the command line
```

You may need to adjust firewall settings to allow incoming connections. On Mac, you will usually be prompted to allow this the first time you start syncthing.

https://docs.syncthing.net/users/firewall.html


#### Connect to a new machine

Vist http://localhost:8384 to view the GUI for your running syncthing.

Click "Add remote device" and enter the device's long unique ID. If you're on the same local network as the other device, it will show up as a suggestion so you don't have to type it.

Give the device whatever nickname you like. Specify the IP address (if it is stable) or leave as 'dynamic' to find the device automatically based on the ID. Choose which folders to share with the device. Choose 'introducer' if you would like to receive other folders automatically from the device.

https://docs.syncthing.net/intro/getting-started.html#configuring

#### Set up a new folder

#### Ignore files

https://docs.syncthing.net/users/ignoring.html

#### Keep old versions

https://docs.syncthing.net/users/versioning.html

#### other tips

* Set up a virtual private server on a cloud provider if you want to have an always-on machine that can act as the central hub.

* If syncing files between Mac and Linux, you might need to watch out for case sensitivity (Linux filesystems are case-sensitive, Mac by default is not). You can create a new APFS volume on your Mac hard drive with case sensitivity enabled, and put your sync folders there to avoid issues.

* If running on a server where you don't have root access, download and run `syncthing` manually or enable as a user service.

https://docs.syncthing.net/users/autostart.html#using-systemd

* See also the syncthing forum: https://forum.syncthing.net/

### dat

https://docs.datproject.org/tutorial

Resources for data sharing with dat:
https://datbase.org/
https://blog.datproject.org/tag/science/

Beaker, a web browser based on dat that enables peer-to-peer, editable websites:
https://beakerbrowser.com/
https://beakerbrowser.com/2017/06/14/forking-websites-on-the-p2p-web.html

### git-annex

http://git-annex.branchable.com/walkthrough

#### Example setup

Initialize a repository:
```bash
mkdir project
cd project
git init
git annex init --version=6 "My desktop"
```

Add files:
```bash
cp ~/Downloads/ubuntu.iso .
git annex add ubuntu.iso
git commit -a -m "Added a file"
```

Clone on another folder on the same computer (could be a removable drive):
```bash
cd /media/usb
git clone ~/project
cd project
git annex init --version=6 "Portable drive"
```

Sync between clones (takes care of commiting, pushing, and pulling):
```bash
cd /media/usb/annex
git annex sync

# To get the content of large files in this step, use --content
git annex sync --content
```

#### Get and drop files

#### Special remotes

#### git-annex assistant

Automated sync tool with a GUI

https://git-annex.branchable.com/assistant/
