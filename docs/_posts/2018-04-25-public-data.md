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

Application programming interfaces (or APIs) are a set of rules for building application software. In this case it usually refers to accessing and posting data to a specific group of servers. Many government agency APIs for accessing data are catered towards people building web application software.

API documentation usually includes:
* how to format query strings
* what types/formats of data that can be retrieved or posted with a request
* authentication procedures

# What is Data.gov?

[Data.gov](https://www.data.gov/) is mostly a catalog of data sets collected by the agencies of the US Federal Government. It includes information about the agency that collected the data, meta data, landing pages for the project, and links to the web address where data can be retrieved, the format of the data, etc. etc.

## What Data.gov is not

Data.gov doesn't host the data directly, and doesn't have a unified API for accessing data from all government agencies. While Data.gov does have *an* API, the types of information accessed with the API are data on the types of data in the catalog. So you get meta meta data. 

# Exercises

## Getting NOAA precipitation data from an FTP server

The [U.S. Hourly Precipitation data set](https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00313) is hosted on an FTP server and is well documented. Here you'll find that there is a page for downloading data from specific date ranges and location, but if you want to store them on a server then you'll (obviously) need to use FTP.

The [.pdf](ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/dsi3240.pdf) describes the naming scheme and the [readme.txt](ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/readme.txt) instructs how to open a connection to the server and where to find files.

### Exercise: Get precipitation records from CA from 2000-2009

#### According to the docs (don't run this before we discuss)

1. Log into the FTP server

```bash
foo@bar:~$ ftp ftp.ncdc.noaa.gov
```

2. Navigate to the correct directory

```bash
ftp> cd pub/data/hourly_precip-3240/04
```

3. Use `get` to download one file, or `mget` to get multiple files

```bash
ftp> mget 3240_04_200*.tar.Z
```

Just a note, when logging into an FTP server your username and password aren't encrypted. There are ways of doing FTP over SSH or with a secure-socket layer (SSL). 

#### The safer way

`curl` has an option of using FTP with a SSL. We should choose this instead, because it will protect the traffic.

1. Navigate to your preferred directory

2. Use the `--ftp-ssl` flag, the `--user` flag, and the `-o` option

```bash
foo@bar:~$ curl --ftp-ssl --user anonymous:youremail@email.com ftp://ftp.ncdc.nooa.gov/04/3240_04_2000-2000.tar.Z -o ca_2000.tar.Z
```
#### The safer (recursive) way

`curl` doesn't have a built-in method for easily getting multiple files. Write a shell script that will get all the CA precipitation data from 2000-2009.

`wget` has a `-m` option for mirroring sites, that will allow you to download the entire contents of a directory. 

```bash
foo@bar:~$ wget -mc -nH --ftps-implicit --no-ftps-resume-ssl --user=anonymous --password=youremail@email.com ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/04/
```
#### Bonus

1. Write a script for downloading the files you want from the NOAA FTP server with `curl`.

2. FTP isn't super great for transferring large files. How can you tell if the files downloaded by `curl` are identical to the ones you mirrored with `wget` from the command line?

## Getting USGS earthquake data using an API

Skim the docs. Place a query to return GeoJSON records of earthquakes occuring 1) on your birthday, 2) in your favorite region of the world,  3) with a magnitude > 2.5

```bash
foo@bar:~$ curl -O https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=1991-09-21&endtime=1991-09-21&maxlatitude=43.373&minlatitude=25.542&maxlongitude=-101.25&minlongitude=-120.234&minmagnitude=2.5&orderby=time
```
The Python urllib and request libraries are great for formatting query strings and headers for more sophisticated endeavors than the exercise above. (But you can also do fancy things in Bash.)

# Mini-challenge!

(To be posted during the session)

# Resources

## Project Open Data

Project Open Data was an initiative created by the Obama Administration to promote accessibility and visibility of data sets collected and curated by the Federal government. The [Project Open Data policy page](https://project-open-data.cio.gov/) is mostly geared towards government officials wanting to publish agency data, but also includes some resources for harvesting metadata, converting file types, etc. 

There's also a [dashboard](https://labs.data.gov/dashboard/offices/qa) to check out how well each government agency is complying with the Project Open Data policies. 

## NASA

Fonts aside, [NASA](https://api.nasa.gov/) has their crap together. 




