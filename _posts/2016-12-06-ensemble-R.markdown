---
layout: post
title: Ensemble (Machine) Learning with Super Learner and H2O in R -- Nima Hejazi and Evan Muzzall
comments: true
category: posts
tags: meeting <+ tags +>
---

## Nima Hejazi & Evan Muzzall

Nima is a graduate student in the Division of Biostatistics. His research
combines aspects of causal inference, statistical machine learning, and
nonparametric statistics, with a focus on the development of robust methods for
addressing inference problems arising in precision medicine, computational
biology, and clinical trials.

Evan earned his Ph.D. in Biological Anthropology from Southern Illinois
University Carbondale where he focused on spatial patterns of skeletal and
dental variation in two large necropoles of Iron Age Central Italy (1st
millennium BC). He is currently R Lead Instructor, co-founder of the Machine Learning Working Group, and Research Associate in the D-Lab.

## Ensemble (Machine) Learning with Super Learner and H2O in R

This presentation covers methods for performing ensemble machine learning with the [Super
Learner](https://cran.r-project.org/web/packages/SuperLearner/index.html) R
package and [H2O](http://www.h2o.ai) software platform, using the [R language
for statistical computing](https://www.r-project.org).

__Materials for this presentation are available on GitHub
[here](https://github.com/nhejazi/talk-h2oSL-THW-2016)__.

### R & RStudio Installation
* You can download R and RStudio
  [here](https://www.rstudio.com/products/rstudio/download/).

### Jupyter R Kernel Installation
* Please follow the instructions
   [here](https://irkernel.github.io/installation/) to install an R kernel for
   Jupyter notebooks.

### SuperLearner Installation
```r
require("devtools")
devtools::install_github("ecpolley/SuperLearner")
```

### H2O Installation
These installations are required to make H2O work in RStudio. Click the links
to visit the download pages.

1. [Download RStudio](https://www.rstudio.com/products/rstudio/download/)

2. [Download Java Runtime
    Environment](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)

3. [Download H2O for R and dependencies (click the "Use H2O directly from R"
    tab and follow the copy/paste   instructions)](http://h2o-release.s3.amazonaws.com/h2o/rel-turing/10/index.html)

4. Install the `devtools` and `h2oEnsemble` R packages.

```r
# The following two commands remove any previously installed H2O packages for R.
if ("package:h2o" %in% search()) { detach("package:h2o", unload=TRUE) }
if ("h2o" %in% rownames(installed.packages())) { remove.packages("h2o") }

# Next, we download packages that H2O depends on.
pkgs <- c("methods","statmod","stats","graphics","RCurl","jsonlite","tools","utils")
for (pkg in pkgs) {
if (! (pkg %in% rownames(installed.packages()))) { install.packages(pkg, repos = "http://cran.rstudio.com/") }
}

# Now we download, install and call the H2O package for R.
install.packages("h2o", type="source", repos=(c("http://h2o-release.s3.amazonaws.com/h2o/rel-turing/10/R")))

# Install the "devtools" R package.
install.packages(c("devtools"))

# Install the "h2oEnsemble" R package.
install_github("h2oai/h2o-3/h2o-r/ensemble/h2oEnsemble-package")

# Load packages
library(h2o)
library(devtools)
library(h2oEnsemble)
```

## Lightning Talks

## <+ person +> : <+ topic +>

## <+ person +> : <+ topic +>
