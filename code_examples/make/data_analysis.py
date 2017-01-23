from math import cos
import random

files = ['1.dat','2.dat','3.dat']

for name in files:
  f = open(name, 'w')
  scale = random.random()
  for x in range(-20,20):
    s = str(x)+" "+str(cos(scale*x))+"\n"
    f.write(s)

