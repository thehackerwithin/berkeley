---
layout: post
title: Accessing public data on .gov websites -- Caroline Cypranowska
comments: true
category: upcoming
tags: meeting
---

# Accessing public data on .gov websites (or how to deal with bureaucrats)

## Prerequisites

Today's exercises will require Bash. If you have a Mac or Linux machine, you're mostly good to go. 

### Windows

Most Windows users in need of a Bash terminal use [Cygwin](https://www.cygwin.com/), a collection of Linux software tools compiled for Windows. Other options include [Git](https://git-scm.com/download/win) and creating a Linux subsystem (for Windows 10). The instructions below provide detailed instructions for installing Cygwin and a few other tools required for this tutorial. 

1. Download Cygwin and run `setup.exe`. Select 'Install from Internet' when prompted by the installation wizard. Choose your root directory and mirror for installation.

2. The installer will also download a list of available packages. Include the default packages, but make sure to search for and include `curl` and `wget`.

3. Add the Cygwin path to the Windows Environment Path Variable, which can be found in the 'Advanced system settings'
menu. Append `;C:\cygwin\bin` to the end of the variable value option (assuming this is where you installed Cygwin). 


### MacOS

The terminal in MacOS has the majority of the tools needed to make requests to government databases, as cURL comes with Macs out of the box. The main advantage of `wget` over `curl` is that it can download recursively. While you can choose to do the exercises without `wget`, it can be easily installed with Homebrew. 

```bash
foo@bar:~$ brew install wget
```

# A brief explanation of networking protocols

In networking, a protocol is a set of rules for communication. Peer-to-peer networks are composed of interconnected computers, but no computer has a privileged position. Client-server networks, on the other hand, are composed of servers that perform functions on behalf of other machines (clients). Both of these systems rely on protocols to send and receive data. 

The set of protocols used on the Internet is called TCP/IP (Transmission Control Protocol/Internet Protocol). The TCP/IP model has a layered structure, and protocols like HTTP, FTP, and SSH run on the highest layer (the application layer). 

HTTP (or hypertext transfer protocol) defines how computers exchange HTML documents, and FTP (or file transfer protocol) defines how computers move files between local and remote file systems. These are the primary tools we will use today to get our data.

HTTP and FTP each have methods for a client to make requests of the server, and for the server to return a response. HTTP requests and responses usually have a header, which contains meta data of the request. 

![alt text](https://imgs.xkcd.com/comics/server_attention_span.png "https://xkcd.com/869/")

# APIs

Application programming interfaces (or APIs) are a set of rules for accessing and posting data to a specific set of servers. Many developers use APIs for developing web applications.

API documentation usually includes:
* how to format query strings
* what types/formats of data that can be retrieved or posted with a request
* authentication procedures

# What is Data.gov?

Data.gov is mostly a catalog of data sets collected by the agencies of the US Federal Government. It includes information about the agency that collected the data, meta data, landing pages for the project, and links to the web address where data can be retrieved, the format of the data, etc. etc.

## What Data.gov is not

Data.gov doesn't host the data directly, and doesn't have a unified API for accessing data from all government agencies. While Data.gov does have *an* API, the types of information accessed with the API are data on the types of data in the catalog. So you get meta meta data. 

# Exercises

## Getting NOAA precipitation data from an FTP server

## Getting USGS earthquake data using an API

# Mini-challenge!

# Resources

## Project Open Data

Project Open Data was an initiative created by the Obama Administration to promote accessibility and visibility of data sets collected and curated by the Federal government. The [Project Open Data policy page](https://project-open-data.cio.gov/) is mostly geared towards government officials wanting to publish agency data, but also includes some resources for harvesting metadata, converting file types, etc. 

There's also a [dashboard](https://labs.data.gov/dashboard/offices/qa) to check out how well each government agency is complying with the Project Open Data policies. 

## NASA





