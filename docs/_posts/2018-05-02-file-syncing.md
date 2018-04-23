---
layout: post
title: Tim Howes -- File syncing tools - syncthing, dat, git-annex
comments: true
category: upcoming
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
