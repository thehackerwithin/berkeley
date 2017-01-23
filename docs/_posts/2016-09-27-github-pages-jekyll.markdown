---
layout: post
title: Github Pages and Jekyll - Stuart Geiger
comments: true
category: posts
tags: meeting <+ tags +>
---

# Stuart Geiger

I'm a postdoc at [the Berkeley Institute for Data Science](http://bids.berkeley.edu) and I recently completed my Ph.D last December at the UC-Berkeley [School of Information](http://ischool.berkeley.edu) next door. I'm an ethnographer of science and technology, and I study how people produce knowledge. My Ph.D research was about Wikipedia's volunteer editing community, and I'm now studying the emergence of this thing we like to call data science. In my work, I use many different kinds of methods -- sometimes I look more like an anthropologist, a historian, or a philosopher, while other times I run surveys, experiments, and large-scale data analyses. 

# Github Pages and Jekyll

Github Pages is a free web hosting service by Github, which uses Jekyll to generate HTML files from files (themes, layouts, and data) in a special Github repository. Whenever you make a commit to a Github Pages repository, Github's servers run the Jekyll parser on the files in that repository, which generates a set of static HTML and CSS files on a special subdomain. The result can look nearly identical to traditional content management systems (like Wordpress or Drupal) that dynamically process requests from browsers using languages like PHP and querying live databases like MySQL.

## Advantages over the dynamic/CMS approach:

* Fewer moving parts to configure and maintain
* No need to be a systems administrator
* More secure from hackers (the bad kind)
* Uses existing Github infrastructure for logins and collaboration
* Free hosting! (recommended max: 100,000 requests/month)

## What you need

* For most of this session, just a Github account and a web browser
* For a few minutes at the end, I'll walk people through running Jekyll locally. [Install instructions are here](https://jekyllrb.com/docs/installation/) for OS X and Linux (Windows is not officially supported). 

### Repositories to fork
 
* [academicpages/group-meeting](https://github.com/academicpages/group-meeting)
* [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io)
* [academicpages/events](https://github.com/academicpages/events)

## Tips and tricks

* Settings are in the settings tab of your repository, in the "GitHub Pages" section.
  * You can see details about errors here, although they can be misleading / hard to decode
* Jekyll's markdown parser/renderer can be stricter than Github's, and will just print raw markdown if it hits something it won't parse
* Go to the commit list (on your repo) to find the last version Github built with Jekyll.
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built
* YAML is important and easy to mess up (YAML Ain't a Markup Language)
  * [The YAML format](http://symfony.com/doc/current/components/yaml/yaml_format.html)
  * Invalid YAML declarations will cause builds to fail in ways that generate misleading errors
  * Valid YAML declarations will be rendered by Github as a nice, formatted table.
  * YAML uses C-style quote escape sequences
  
## Examples of good/easy/interesting Github Pages sites

### Themes

* [Neo HPSTR theme](https://github.com/aron-bordin/neo-hpstr-jekyll-theme)
* [Made Mistakes](https://github.com/mmistakes/made-mistakes-jekyll)
* [Skinny Bones](https://github.com/mmistakes/skinny-bones-jekyll)
* [Left](https://github.com/holman/left)

### Real world examples

* [ACM Conference on Cloud Computing](http://acmsocc.github.io/2016/) -- [Github repo](https://github.com/acmsocc/2016)
  * Very detailed and polished (and complicated)
  * Uses YAML to generate schedule
* [AstroHackWeek](http://astrohackweek.org/2016/) -- [Github repo](https://github.com/AstroHackWeek/2016)
  * Single page scrolling layout, based on Solid State by HTML5 UP
* [Switch2OSM](http://switch2osm.github.io/) -- [Github repo](https://github.com/switch2osm/switch2osm.github.io)
  * Uses [Neo HPSTR theme](https://github.com/aron-bordin/neo-hpstr-jekyll-theme)

# Lightning talks

## Matthias Bussonnier
[Cross language Jupyter](https://github.com/Carreau/talks/blob/master/2016-09-23-uc-merced-seminar/Cross%20Language%20Integration.ipynb)

## <+ person +> : <+ topic +>
