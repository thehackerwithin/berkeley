import numpy as np
import time
from multiprocessing import Pool, cpu_count
import sys
sys.path.append('..')
from numpyVectorization.motion_gauss import simulateParticles_loop

# How do we pass multiple arguments via pool? Use wrapper functions! Note: 
# lambda functions will NOT work for this purpose
def wrapper_fun(args):
    return simulateParticles_loop(*args)

if __name__ == "__main__":
  num_particles = 100000
  num_steps = 100
  num_cpus = cpu_count()
  # Determine how many particles to run on each worker
  num_particles_per_core = int(num_particles / num_cpus)

#  # input arrays
#  inArys = [np.zeros((num_particles_per_core, num_steps)) for i in range(num_cpus)]
#  for ary in inArys: print ary.shape
  
  # Set up our pool
  p = Pool(num_cpus)
  
  # Make our arguments
  args = [(num_particles_per_core, num_steps, False)] * num_cpus
#  from itertools import izip, repeat
#  args = izip(repeat(num_particles_per_core, num_cpus), repeat(num_steps, num_cpus), repeat(False, num_cpus))
  # Send the wrapper function and the iterable args to map
  tic = time.time() # Start time of code running
  result = p.map_async(wrapper_fun, args)
  # Get the result when it's ready
  poolresult = result.get()
  toc = time.time()
  p.close()
  p.join()
  print "%.5f sec to compute %s particles" %((toc-tic), num_particles)

