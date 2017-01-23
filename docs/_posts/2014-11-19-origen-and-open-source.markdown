---
layout: post
title: ORIGEN and Open Source
comments: true
category: posts
tags: meeting 
---


# Attending

- Max Fratoni
- Katy Huff
- Kelly Rowland
- Alejandra Jolodosky
- Sandra Bogetic
- Madicken Munk
- Dan Wooten
- Tenzing Joshi
- Andrey Mironyuk

# Discussion: ORIGEN - Max Fratoni

Max gave us an overview of ORIGEN, a depletion code.
Max's presentation can be found [here][pres].


## Max Fratoni

Max is a professor in the Department of Nuclear Engineering.

## ORIGEN

- ORIGEN solves the bateman equation
- What you need for the zero dimensional depletion equation to be accurate is 
  simple: accurate cross sections.

ORIGEN-S is within the Scale package and is maintained by the Scale 
maintainers, whereas ORIGEN2 is standalone. ORIGEN-ARP is a graphical interface 
for ORIGEN-S. It's possible to use 3 energy groups in ORIGEN-S and the cross 
sections are kept up-to-date 

- ORIGEN-S tracks depletion for 1946 isotopes. 
- HOWEVER, there are only about 300 isotopes in the ENDF database 

So, how do we run the code? Max went over the various data we need to input
 - material
 - data
 - depletion data
   - power depletion : need power and time
   - flux irradiation : need flux and time
   - decay : need time

They produce:

- activity
- radiotoxicity
- decay heat
- absorption and fission rates
- neutron emmission
- photon emission

Every material you provide must be one of the three groups

- activation product (720)
- actinide (130)
- fission product (850)

Of course these groups overlap.

You also have to provide information about every nuclide (decay constants, 
decay heats, etc.) These **decay data libraries** are plaintext. ORIGEN comes 
packaged with this information.

You also have to provide the **cross section libraries**. ORIGEN comes with 
some of these. The cross section libraries have to be selected carefully. 

The input files are **TAPE** files... because they used to actually be tapes. 



# Dicussion: Open Source Contribution

We intentionally misspelled everyone's names and went through the 
issue-pull-request-review-pull-close workflow seen in many open source 
projects.

[pres]: https://github.com/thehackerwithin/berkeley/tree/master/origen "Presentation" 
