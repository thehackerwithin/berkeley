#!/usr/bin/python

# import any needed modules
import pdb
import numpy as np
import math
import copy
import re
import sys

class GridSet(object):
    """GridSet class: holds each grid, reads data, smooths, prolongs, and restricts"""
    def __init__(self, G, H, phi, q, Tname, Sname):
    # Read in Cross section data. Put the data, initial guess, and source on the finest
    # grid. Initilize the remiander of the grids by inserting the restricted cross
    # sections and zeros for phi and q.

        # Get initial data and make initial guess: 
        # total cross sections
        T = np.zeros((G,G))
        f = open(Tname)
        for j,line in enumerate(f):
	    vals = line.split()
	    for i,val in enumerate(vals):
                T[j,i] = val
        f.close()

        # scattering cross sections
        S = np.zeros((G,G))
        f = open(Sname)
        for j,line in enumerate(f):
	    vals = line.split()
	    for i,val in enumerate(vals):
                S[j,i] = val
        f.close()

        # Create an array of Grids that will hold all of the data at all of the levels
        # the finest mesh = 1, the coarsest = H; put data in finest level
        self.grids = np.zeros(H + 1, dtype=Grid)
        self.grids[0] = Grid(T, S, phi, q)
        self.previous = copy.deepcopy(self.grids[0].phi) # for convergence testing later. 

        # Now go on to initialize the remainder of the grids with restricted cross sections, 
        # initial guess for "phi", and a holder for q (to be computed in residual).
        for level in range(H):
	        init_guess = self.restrict(np.zeros(np.size(self.grids[level].T, 0)))

	        self.grids[level+1] = Grid(self.restrictMat(self.grids[level].T), \
                 self.restrictMat(self.grids[level].S), init_guess, init_guess)


    # this prints data of interest
    def prnt_data(self,level):
	    """prnt_data: prints the value of phi for a given level"""
	    print self.grids[level].phi


    # Functions used in the multigrid solve
    def relax(self, nu, omega, level):
	"""relax: apply the iteration method"""
    	T = self.grids[level].T
    	S = self.grids[level].S
    	q = self.grids[level].q
    	if level == 0:
    	    phi_new = copy.deepcopy(self.grids[level].phi)
        else: # other levels solving residual eqn w/ initial guess zero
    	    phi_new = np.zeros(np.size(q))
    
    	for k in range(nu):
    	    phi_old = copy.deepcopy(phi_new)
            
            for g in range(np.size(phi_new, 0)):
                down = 0
    		    up = 0
    		    for gp in range(g):
    		        down = down + S[g, gp] * phi_new[gp]
    		    for gp in range(g + 1, np.size(phi_new)):
    		        up = up + S[g, gp] * phi_old[gp]
    
                D = (T[g, g] - S[g, g])
                phi_new[g] = 1 / (D) * (omega * (up + down) + omega * q[g] + \
    		                    (1 - omega) * D * phi_old[g])
                
            self.grids[level].phi = copy.deepcopy(phi_new)



    def prolong(self, data, level):
        """prolong: interpolates a vector from coarse to fine grids"""
        num_coarse = np.size(data,0)
	    indx_coarse = num_coarse - 1
        num_fine = np.size(self.grids[level-1].phi, 0)
        indx_fine = num_fine - 1

        data_out = np.zeros(num_fine)
	    for j in range(num_coarse):
            data_out[2*j] = data[j]

	    for j in range(indx_coarse):
            data_out[2*j+1] = 0.5*(data[j] + data[j+1])

	    if indx_fine%2 != 0:
	        data_out[indx_fine] = 0.5*data[indx_coarse]

	    return data_out


    def restrictMat(self, data):
	"""restrictMat: restricts a matrix from fine to coarse grids"""
        # this uses the full weighting method to restrict to half as many grid points

        # num is used to denote the number of elements in a dimension
	    # indx is used to denote the highest counting index in a dimension
	    # these distinctions are to account for starting at 0
        num_fine = np.size(data,0) 
	    indx_fine = num_fine - 1   
	
	    indx_coarse = int(math.floor(indx_fine/2)) 
	    num_coarse = indx_coarse + 1
        data_tmp = np.zeros((num_coarse, num_fine)) 
	    # average in one direction into temporary matrix 
	
	    # behavior for last entry based on even or odd gridpoints
        if indx_fine%2 == 0: # odd number of points
	        data_tmp[indx_coarse,:] = data[indx_fine,:]
        else:                # even number of points
            data_tmp[indx_coarse,:] = 0.5*(data[indx_fine - 1,:] + data[indx_fine,:])
 
	    # loop over remaining grid
        for j in range(indx_coarse):
            data_tmp[j,:] = 0.5*(data[2*j,:] + data[2*j+1,:])

        # now go in the other direction to get final data
	    data_out = np.zeros((num_coarse, num_coarse))
        if indx_fine%2 == 0: # odd number of points
	        data_out[:,indx_coarse] = data_tmp[:,indx_fine]
	    else:                # even number of points
	        data_out[:,indx_coarse] = 0.5*(data_tmp[:,indx_fine - 1] + \
			                   data_tmp[:,indx_fine])	
        # loop over remaining grid
        for j in range(indx_coarse):
		    data_out[:,j] = 0.5*(data_tmp[:,2*j] + data_tmp[:,2*j+1])

	    return data_out


    def restrict(self, data):
	"""restrict: restricts a vector from fine to coarse grids"""
	# this averages to restrict to half as many grid points

        # num is used to denote the number of elements in a dimension
	    # indx is used to denote the highest counting index in a dimension
	    # these distinctions are to account for starting at 0
        num_fine = np.size(data,0) 
	    indx_fine = num_fine - 1   
	
	    indx_coarse = int(math.floor(indx_fine/2)) 
	    num_coarse = indx_coarse + 1
        data_out = np.zeros(num_coarse)
        
        # behavior of last entry based on even or odd gridpoints
	    if indx_fine%2 == 0: # odd number of points
	        data_out[indx_coarse] = data[indx_fine]
        else:              # even number of points
	        data_out[indx_coarse] = 0.5*(data[indx_fine] + data[indx_fine-1])

	    # loop over remaining grid
	    for j in range(0, indx_coarse):
	        data_out[j] = 0.5*(data[2*j] + data[2*j+1])

        return data_out


    def residual(self, level):
	"""residual: puts the residual into the next level source vector"""
    	lhs = np.dot((self.grids[level].T - self.grids[level].S), self.grids[level].phi)
    	r   = self.grids[level].q - lhs
    	self.grids[level+1].q = copy.deepcopy(self.restrict(r))


    def correct(self, level):
	"""correct: corrects and updates the solution on the previous level"""
    	correction    = self.prolong(self.grids[level].phi, level)
    	corrected_phi = self.grids[level-1].phi + correction
    	self.grids[level-1].phi = copy.deepcopy(corrected_phi)


    def direct(self, level):
	"""direct: directly solves the problem on the coarsest grid"""
	    self.grids[level].phi = np.linalg.solve((self.grids[level].T - self.grids[level].S), \
			                         self.grids[level].q)

    def test_convergence(self, tol):
	"""test_convergence: test if the system has converged"""
         
	# compute the 2-norm of the difference between this guess and the 
        # previous. Compare to the tolerance to test convergnece.
	error = np.linalg.norm(self.previous - self.grids[0].phi)
	if (error < tol):
	    return 1
    else:
	    self.previous = copy.deepcopy(self.grids[0].phi)
	    return 0



class Grid(object):
    """Grid class: simply makes a grid storing cross section, source, and moment data"""
    def __init__(self, T, S, phi, q):
        self.T = T
        self.S = S
        self.phi = phi
        self.q = q
                  

# lets this be run from the command line
if __name__ == '__main__':

    # get name of input file, open it, and read it.
    input_file = sys.argv[1] 
    f = open(input_file) 
    in_data = {}
    for line in f:
        data = line.split()
        key = data[0]
        if len(data[1:]) == 1:
            if re.search("\d", data[1]):
                if "." in data[1]:
                    value = float(data[1])
                else:
                    value = int(data[1])
            else:
                value = str(data[1])
        else:
            value = [float(item) for item in data[1:]]
        in_data[key] = value    
    f.close()

    G  = in_data["G"]        # number of groups
    H  = in_data["H"]        # number of grids
    nu = in_data["nu"]       # number of steps per relaxation
    omega = in_data["omega"] # relaxation factor
    tol   = in_data["tol"]   # convergence tolerance 
    phi_0 = in_data["phi_0"] # initial guess
    q     = in_data["q"]     # source
    Tname = in_data["Tname"] # file holding total cross sections
    Sname = in_data["Sname"] # file holding scattering cross sections

    # initialize the problem, puts data on finest grid
    # level 0 = finest, level H = coarsest
    soln_grids = GridSet(G, H, phi_0, q, Tname, Sname)

    converged = 0
    itr_cnt = 0
    max_itr = 500
    # multigroup solve until convergence
    while ((converged != 1) and (itr_cnt < max_itr)):
    
	itr_cnt = itr_cnt + 1
	# go down one side of the V
        for level in range(H): 
	    soln_grids.relax(nu, omega, level) 
            soln_grids.residual(level)

        # solve at coarsest level
	soln_grids.direct(H)
        soln_grids.correct(H) 

        # go back up the other side of the V
	for level in range(H-1, 0, -1):
           soln_grids.relax(nu, omega, level)
           soln_grids.correct(level) 

        # solve on finest level
        soln_grids.relax(nu, omega, 0)

        #check for convergence
        converged = soln_grids.test_convergence(tol)
#        print ("iteration ", itr_cnt) 
#        print soln_grids.prnt_data(0)

    soln_grids.prnt_data(0)
    print ("converged in ", itr_cnt, " for tolerance ", tol) 


