---
layout: post
title: Emailing with Python - Ross Barnowski
comments: true
category: posts
tags: meeting bash shell
---

# Attending

-    Ross Barnowski
-    Katy Huff
-    Ryan Bergmann
-    Professor Rachel Slaybaugh 
-    Kelly Rowland
-    Daniel Wooten
-    Joshua Howland 
-    Madicken Munk
-    ... 

# Lesson: Emailing With Python

Tutorial for sending email using python, smtplib, and the gmail smtp server.

Requires:
-     python (2.6 or greater)
-     Python modules: smtplib, email, getpass, psutil (advanced example)

Example scripts ([examples][examples]):

-    `smtp_simple.py`: Simplest example demonstrating the use of smtplib to send a
                "Hello World" style messge

-    `smtp_mime.py`: A more complicated example demonstrating the use of several MIME
     objects in the email module to construct a message out of 
     formatted text (html) with an image attachment.
-    `simulation_example_` : This folder contains an example python script that
     calls a simulation program (in this case, a plasma calculation from Prof.
     Morse's 281 class). The simulation is launched from the python script, and
     psutil is used to do some rudimentary performance logging. When the calculation
     finishes, the results, simulation output, and performance statistics are all
     attached to an email and sent to the user.

NOTE: The logging in this example is for demonstration only. This simple
logging is probably not the way you'd want to do it if you truly wanted to
track the performance of a running calculation. May not work on all systems.


# Lightning Talk: Rachel on pretty images and Madicken on slow MCNP

Rachel showed an excellent-looking, peacock colored image of the ratio of two 
neutronics solutions. 

Madicken discussed the behavior of MCNP when a single material is replaced by 
a material which causes more neutron scattering. Result: MCNP slows down a whole 
heck of a lot for such materials.

[examples]: https://github.com/thehackerwithin/berkeley/blob/master/python_email   "Tutorial Source" 


