# Code Examples for SQL

The SQL code examples in this folder were originally meant to compliment
[the tutorial given on SQL and Relational Databases on 2018-02-21](http://www.thehackerwithin.org/berkeley/posts/2018-02-21-SQL-relationaldatabases.html),
although anyone should feel free to add additional SQL code examples here.

# TOC
* [`SQL_Tutorial-0.ipynb`](./SQL_Tutorial-0.ipynb)
* [`SQL_Tutorial-1.ipynb`](./SQL_Tutorial-1.ipynb)
* [`sql_tutorial_2.py`](./sql_tutorial_2.py)

## `SQL_Tutorial-0.ipynb`
This is a Python-3 Jupyter notebook containing examples from the tutorial, which uses Python-3's builtin wrapper for SQLite to create a
database and tables, add data to the tables, and do various queries.

## `SQL_Tutorial-1.ipynb`
This is another Python-3 Jupyter notebook containing the code used to download an IMDB archive of movie title data and upload it to a
PostgreSQL database at https://phppgadmin.alwaysdata.com/ . Please email me (mikofski at berkeley dot edu) if you need the credentials
for this sample database.

## `sql_tutorial_2.py`
This is a Python-2 ( I repeat, **Python-_2_**) script that contains code to download an archive of IMDB people data, create a relational
table to contain foreign keys relating people to the movies they're most known for, and upload the data to the tables. The sample
PostgreSQL database is online at at https://phppgadmin.alwaysdata.com/ . Please email me (mikofski at berkeley dot edu) if you need the
credentials for this sample database.

# SQL samples needed
We still need more SQL code samples either raw `SQL` queries that can demonstrate how various tasks, or language specific examples of
adpaters for various popular relational databases.

`R` is a popular scripting language that also has bindings to popular relational databases. For example
[`RSQLite` v2.0](https://www.rdocumentation.org/packages/RSQLite/versions/2.0) embeds the SQLite database engine into R and provides
DBI-compliant interface.
