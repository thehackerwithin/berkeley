---
layout: post
title: Scraping Wikipedia Data - Stuart Geiger
comments: true
category: posts
tags: meeting data web
---

## Attending

About 30 folks!

## Stuart Geiger

I'm a postdoc at [the Berkeley Institute for Data Science](http://bids.berkeley.edu) and I recently completed my Ph.D last December at the UC-Berkeley [School of Information](http://ischool.berkeley.edu) next door. I'm an ethnographer of science and technology, and I study how people produce knowledge. A big focus of my work is about how new technologies change what it means to produce knowledge. In my work, I use many different kinds of methods -- sometimes I look more like an anthropologist, a historian, or a philosopher, while other times I run surveys, experiments, and large-scale data analyses. My Ph.D research was about Wikipedia's volunteer editing community, and I'm now studying the emergence of this thing we like to call data science.

## Scraping Wikipedia data

We'll be using two different resources to query Wikipedia. First, the [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page), which directly queries the text in Wikipedia articles, and second [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), a new project that is trying to store all of the information in Wikipedia articles in a standardized, structured database.

### Things you will need
* A clone of [this directory](https://github.com/thehackerwithin/berkeley/blob/master/scraping_wikipedia/), which has Jupyter notebooks
* Jupyter notebook instance with the python kernel (I'm using python 3)
* Python libraries (can be installed with 'pip install ...'): wikipedia, pywikibot, requests, nltk, pandas
* A Wikipedia account (not required but *highly* recommended. [Register here!](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page&type=signup))

## Lightning Talks 

## Matthias : Hacker Within mybinder

Go checkout mybinder.org. You can run the THW notebooks from your browser.

## Brian : Where is a mountain, anyway

Inspired by the geocoordinates in Stuarts talk, Brian pointed out that putting 
coordinates on a mountain is tricky. Where is a mountain, anyway?

[code]: https://github.com/thehackerwithin/berkeley/blob/master/scraping_wikipedia/ "Code Examples" 
