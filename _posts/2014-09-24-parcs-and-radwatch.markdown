---
layout: post
title: PARCS and RadWatch-\*NIX-fu - Sandra Bogetic and Ryan Pavlovsky 
comments: true
category: posts
tags: meeting parcs unix
---


# Attending

- Sandra Bogetic
- Christian DiSanzo
- Alejandra Jolodosky
- James
- Kelly Rowland
- Jasmina Vujic
- Rachel Slaybaugh
- Massimiliano Fratoni
- Katy Huff
- Dan Wooten
- Aaron Culich
- Madicken Munk
- Kedar Kolluri

# Discussion: PARCS

## Sandra Bogetic

Sandra Bogetic is a first year graduate student in the Nuclear Engineering 
Department. 

## PARCS

PARCS is a powerful tool, but it seems to have struggles with version control, 
and would strongly benefit from a more transparent and controlled release 
procedure.

Since it is an NQA-1 code.... its surprising that it is not under version 
control.

### Input Files

- Generation of cross sections can be done in various ways. These include 
  CASMO, HELIOS, and TRITON 
- The input for thermal hydraulic behavior can be enered into PARCS or coupled 
  using PATH, TRACE, and/or RELAPE. For a PWR, you can do it in TH. 
- Depletion can be done by PARCS, but sometimes you don't want to do it with 
  PARCS because perhaps you have done depletion in some other code (such as 
  SIMULATE). PARCS allows you to input this external data.
- The input file formatting is in blocks.
  - CNTL, XSEC, GEOM, PARAM, TH, TRAN, etc.
  - ata can be repeated using an asterisk
  - Input ends with a .
  - etc.


### Options

There are many options that can or should be specified. The core type, core 
power, simulation behavior concerning Xe and Sm (will you input the values, do 
you want them to be at equilibrium, transient, etc), control rod banking 
positions, external thermal hydraulics linkages, print options, whether or not 
to conduct depletion, etc.

Additionally, there is a tree variable for cross section definitions.

The geometry card of course is very important. The core compositions are all 
defined for the assemblies, reflector, etc. Typical boundary conditions are 
available.

### Running the input


### Examples

Examples can be found int he presentation, but will not be shared online. 

# Discussion: Linux and Unix tools within RadWatch 

## Ryan Pavlovsky

Ryan is a graduate student in the Nuclear Engineering Department. 

## The \*NIX-fu behind RadWatch

<+ notes +>

Code examples can be found [here][code].

# Lightning Talks 

## <+ person +> : <+ topic +>

## <+ person +> : <+ topic +>


[code]: https://github.com/thehackerwithin/berkeley/tree/master/topic "Code Examples" 
