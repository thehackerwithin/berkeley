---
layout: post
title: Mark Mikofski -- SQL and relational databases
comments: true
category: upcoming
tags: meeting
---

# Agenda
1. [Requirements](#requirements)
1. [Objectives](#objectives)
2. [SQL Examples](#sql-examples)
3. [Relational Databases](#relational-databases)
4. Summary

## [XKCD 327: Exploits of Mom](https://xkcd.com/327/)
![XKCD 327: Exploits of a Mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

## Requirements
To prepare for this tutorial make sure you have the following:

1. We're going to use some Python, so make sure you have it installed on a laptop,
and of course, don't forget to bring your laptop to the tutorial.
2. We're going to use an example database and a Jupyter notebook with some code
examples, so make sure your computer has working internet access. AFAIK anyone can
use the Cal AirBears WiFi connection for free.
3. A willingness to participate, try new things, make mistakes, learn and have fun!

## Objectives

At the end of this tutorial you will be able to do the following:

* define what a database is
* describe the difference between a relational database and no-SQL databases
* write SQL code to
    - create a database, add a table to a database, and add a row
      to a table
    - query a database by selecting fields that satisfy a condition
    - join two or more tables along a common field
* name some common relational databases
* explain some common usage patterns for databases

## SQL Examples
We're going to use the examples from
[`code_examples/SQL`](https://github.com/thehackerwithin/berkeley/tree/master/code_examples/SQL),
so point your browser to this link or clone The Hacker Within - Berkeley and
navigate to this folder.


## Relational Databases
A database is ...

A relational database is ...

There are several popular relational databases ...

### Interfaces
Interfacing with SQL database can be done using command line, GUI, Python binding, ...

#### Python Bindings
there are so many!
* [psycopg2](http://initd.org/psycopg/)
* [pymssql](http://www.pymssql.org/en/stable/)
* [mysqlclient](https://mysqlclient.readthedocs.io/)
* [Oracle MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/)

### Extra SQL commands
When setting up a SQL database server, _eg_ PostgreSQL, you will also need to
create a user, set a password, and create a database.

Explain how to create a user ...
    CREATE USER

Explain how to create a database ...
    CREATE DATABASE
