import matplotlib.pyplot as plt
import numpy as np
import math

def generateChirikovMaps(ks, numInits, numParticles):
  '''Given four values for the "kick" intensity, this function plots
     a Chirikov-Taylor map for each KI value in the same window for
     easy comparison.

     Recommended Values:
     ks = (.5,.75,.95,1.0)
     numInits = 20
     numParticles = 10000

     For more information on the standard map, see:
     http://en.wikipedia.org/wiki/Standard_map ''' 
  f, ax = plt.subplots(2, 2)
  kin = 0
  
  # Check to make sure the input length is 4, as expected
  if len(ks) != 4:
    print "Must have 4 and only 4 k values. Exiting..."
    return 1

  # The outer 2 loops (j,l) handle the plotting for each axis
  for j in range( 0,len(ax) ):
    for l in range( 0,len(ax) ):
      # Run the simulation for numInits # of initial points
      print 'Simulating k = %s with %s particles...' %(k[kin], numInits)
      for i in range(1,numInits):
        temp = np.zeros( (2, numParticles) )
        x = temp[0,:]
        p = temp[1,:]
        # Pick a starting point at random in p-phase space
        x[0] = np.random.rand()*2*math.pi
        p[0] = np.random.rand()*2*math.pi
        # Follow the trajectory of the random point in phase space according
        # to the chirikov-taylor relation
        for n in range(1,numParticles):
          p[n] = ( p[n-1] + ks[kin]*math.sin( x[n-1] ) ) % (2*math.pi)
          x[n] = ( x[n-1] + p[n] ) % (2*math.pi)
        # Plot each of the numInits trajectories on the same plot
        ax[j][l].plot( x/(2*math.pi), p/(2*math.pi), 'b.', ms=1)
      ax[j][l].set_title('Chirikov Map, K = %s' %(ks[kin]) )
      ax[j][l].set_xlabel(r'$\frac{x}{2\pi}$')
      ax[j][l].set_ylabel(r'$\frac{p}{2\pi}$')
      kin += 1
  plt.savefig('chirikov_results.png')
  return ax

if __name__ == '__main__':
  k = [0.5, 0.75, 0.9, 1.0]
  generateChirikovMaps(k, 20, 50000)
