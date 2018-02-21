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
4. [Summary](#summary)

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
    - calculate COUNT, MAX, and other aggregate functions
* name some common relational databases
* explain some common usage patterns for databases

## SQL Examples
We're going to use the examples from
[`code_examples/SQL`](https://github.com/thehackerwithin/berkeley/tree/master/code_examples/SQL),
so point your browser to this link or clone The Hacker Within - Berkeley and
navigate to this folder.


## Relational Databases
[Wikipedia defines a database](https://en.wikipedia.org/wiki/Database) as ...

>An organized collection of data. A relational database, more restrictively, is
>a collection of schemas, tables, queries, reports, views, and other elements.
>... the most popular database systems since the 1980s have all supported the
>relational model - generally associated with the SQL language.

The main difference between a *database* and a object model like JSON or an
simple spreadsheet is the size and complexity, necessitating database management
software to quickly create, query, and retrieve data.

The [*relational database*](https://en.wikipedia.org/wiki/Relational_database)
differs from other databases due to its strictly tabular structure consisting
of rows of records and columns of fields. _E.G._:

| primary key | text field | integer field | date field | real field | boolean field |
|------------:|------------|---------------|------------|------------|---------------|
| 1 | foo | 234 | 2018-02-21T1700Z | 5.67E-8 | TRUE |
| 2 | bar | 123 | 2018-02-21T1830Z | 1.6E-19 | FALSE |

Other databases, called [*noSQL*](https://en.wikipedia.org/wiki/NoSQL), have a
more flexible structure, allowing nested relations between keys, values, and
arrays. Some NoSQL databases are more scalable than relational databases and
can handle more data, making them useful for data science. Some examples of
NoSQL databases are: [CouchDB](http://couchdb.apache.org/),
[MongoDB](https://www.mongodb.com/), [Cassandra](http://cassandra.apache.org/),
[AWS DynamoDB](https://aws.amazon.com/dynamodb/), _etc._

### Schema
The [*database schema*](https://en.wikipedia.org/wiki/Database_schema) formerly
describes the structure of a database. For example the database in the table
above could be described as a table with six fields:
1. a unique non-null field called the [*primary key*](https://en.wikipedia.org/wiki/Primary_key).
2. a text field
3. an integer field
4. _etc._

### SQL - A Structured Query Language
The language used to define the database schema, insert data, and make queries
is called [SQL or Structured Query Language](https://en.wikipedia.org/wiki/SQL).

### Database Management Software
Database management typically consists of a server and a client. There are
[several popular relational databases](https://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems):
* [PostgreSQL](https://www.postgresql.org/)
* [MySQL](https://www.mysql.com/)
* [SQLite](https://sqlite.org/index.html)
* [MSSQL](https://www.microsoft.com/en-us/sql-server/)

### Clients and APIs
There are many ways to interface with a SQL database. Most databases come with
a command line client, _e.g._:
[`psql`](https://www.postgresql.org/docs/current/static/app-psql.html) or a GUI,
_e.g._: [pgAdmin](https://www.pgadmin.org/). Most databases also provide an API
for programmatically interaction, _e.g._:
[`libpq`](https://www.postgresql.org/docs/current/static/libpq.html).

#### Python Bindings
There are Python [bindings](https://en.wikipedia.org/wiki/Language_binding) to
most database APIs:
* [psycopg2](http://initd.org/psycopg/)
* [mysqlclient](https://mysqlclient.readthedocs.io/)
* [sqlite3](https://docs.python.org/dev/library/sqlite3.html)
* [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
* [Oracle MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/)
* [pymssql](http://www.pymssql.org/en/stable/)

#### Object Relational Mapping
It also possible to bind the database records directly to objects using
[object relation mapping (ORM)](https://en.wikipedia.org/wiki/Object-relational_mapping)
with software such as [Django](https://www.djangoproject.com/) or
[SQLAlchemy](http://www.sqlalchemy.org/). The advantage of using an ORM is that
instead of using SQL commands, you create objects native to the languange, and
the ORM takes care of creating the corresponding schema in the database.

### Extra SQL commands
When setting up a SQL database server, _eg_ PostgreSQL, you will also need to
create a user, set a password, and create a database. I'll leave these to the
reader to investigate on their own.

## Summary
SQL is not glamorous, and it's been around for a long time, but it's not that
difficult to teach yourself. There are ton of links here and in the
[`code_examples/SQL`](https://github.com/thehackerwithin/berkeley/tree/master/code_examples/SQL)
so I hope this will serve as a good starting point, but there is still so much
more to learn. If you have any suggestions, feel free to comment here or please
send a PR to [The Hacker Within, Berkeley](https://github.com/thehackerwithin/berkeley)

Thanks!
