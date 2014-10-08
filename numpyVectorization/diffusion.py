''' Functions for comparing vectorization performance of simplified 
    diffusion in 1D and 2D.

    http://en.wikipedia.org/wiki/Finite_difference_method#Example:_The_heat_equation
'''

import numpy as np
from matplotlib import pyplot as plt
plt.ion()

def diff1d_loop( n_iter=200, rate=.5, n_x=100, plotUpdate=True, 
                 showPlots=True ):
    ''' A simple finite difference diffusion example using for loops. 
        This is the slow version. 
        The inputs are: 
        n_iter - the number of diffusion iterations
        rate - the diffusion rate
        n_x  - number of grid points 
        plotUpdate - if the plot should be updated at each iteration. this will 
                     slow the computation
    '''
    x = np.linspace(-30,30, n_x)
    # set the initial conditions for the diffusion
    y_init = np.zeros(n_x)
    # y_init[n_x/2] = 1
    y_init[1] = 1
    y_init[-1] = 1

    y_all = np.zeros((n_x, n_iter))

    if plotUpdate:
        fig = plt.figure()
        lines = plt.step(x, y_init)
        plt.show()

    y_next = y_init.copy()
    for i in range(n_iter):
        y_last = y_next.copy()
        y_all[:,i] = y_next
        for j in range(1,n_x-1):
            y_next[j] = rate*.5*(y_last[j+1] + y_last[j-1]) + (1-rate)*y_last[j]

        y_next[y_init>0] = y_init[y_init>0]
        if plotUpdate:
            lines[0].set_data( x, y_next)
            fig.canvas.draw()

def diff1d_vec( n_iter=200, rate=.5, n_x=100, plotUpdate=True, 
                showPlots=True ):
    ''' A simple finite difference diffusion example using numpy vecorization.
        
        The inputs are: 
        n_iter - the number of diffusion iterations
        rate - the diffusion rate
        n_x  - number of grid points 
        plotUpdate - if the plot should be updated at each iteration. this will 
                     slow the computation
    '''
    x = np.linspace(-30,30, n_x)
    # set the initial conditions for the diffusion
    y_init = np.zeros(n_x)
# y_init[n_x/2] = 1
    y_init[1] = 1
    y_init[-1] = 1

    y_all = np.zeros((n_x, n_iter))

    if plotUpdate:
        fig = plt.figure()
        lines = plt.step(x, y_init)
        plt.show()

    y_next = y_init.copy()
    for i in range(n_iter):
        y_all[:,i] = y_next

        y_next[1:-1] = rate*(y_next[2:] + y_next[:-2]) + \
                      (1-2*rate)*y_next[1:-1]
#y_next[1:-1] = rate*.5*(y_next[2:] + y_next[:-2]) + \
#(1-rate)*y_next[1:-1]
#y_next[0] = rate*y_next[1] + (1-rate)*y_next[0]
#y_next[-1] = rate*y_next[-2] + (1-rate)*y_next[-1]

        y_next[y_init>0] = y_init[y_init>0]

        if plotUpdate:
            lines[0].set_data( x, y_next)
            fig.canvas.draw()

    if showPlots and not plotUpdate:
        fig = plt.figure()
        lines = plt.step(x, y_next)
        plt.show()

    return y_all

def diff2d_loop( n_iter = 100, rate = .5, n_x = 100, plotUpdate=True, 
                showPlots=True ):
    ''' A 2-D finite difference diffusion example using numpy vecorization.
        
        The inputs are: 
        n_iter - the number of diffusion iterations
        rate - the diffusion rate
        n_x  - number of grid points 
        plotUpdate - if the plot should be updated at each iteration. this will 
                     slow the computation
    '''
    
    y_init = np.zeros((n_x, n_x))
    # set the initial conditions 
    # y_init[n_x/2, n_x/2] = 1
    y_init[n_x/2,] = 1

    if plotUpdate:
        fig = plt.figure()
        im = plt.imshow(y_init)
        plt.show()

    y_next = y_init.copy()
    for i in range(n_iter):
        for j in range(1,n_x-1):
            for k in range(1,n_x-1):
                y_next[j,k] = rate*.25*(y_next[j-1,k] + y_next[j+1,k] +\
                                    y_next[j, k+1] + y_next[j, k-1]) +\
                              (1-rate)*y_next[j, k]
        y_next[y_init>0] = y_init[y_init>0]
        # y_next[50, 50] = 1
        if plotUpdate:
            im.set_data( y_next)
            fig.canvas.draw()
    return y_next

    if showPlots and not plotUpdate:
        fig = plt.figure()
        im = plt.imshow(y_next)
        plt.show()
    return y_next

def diff2d_vec( n_iter = 100, rate = .5, n_x = 100, plotUpdate=True, 
                showPlots=True ):
    ''' A 2-D finite difference diffusion example using numpy vecorization.
        
        The inputs are: 
        n_iter - the number of diffusion iterations
        rate - the diffusion rate
        n_x  - number of grid points 
        plotUpdate - if the plot should be updated at each iteration. this will 
                     slow the computation
    '''
    
    y_init = np.zeros((n_x, n_x))
    # set the initial conditions 
    # y_init[n_x/2, n_x/2] = 1
    y_init[n_x/2,] = 1

    if plotUpdate:
        fig = plt.figure()
        im = plt.imshow(y_init)
        plt.show()

    y_next = y_init.copy()
    for i in range(n_iter):
        y_next[1:-1, 1:-1] = rate*.25*(y_next[2:,1:-1] + y_next[:-2,1:-1] +\
                                   y_next[1:-1, 2:] + y_next[1:-1, :-2]) +\
                             (1-rate)*y_next[1:-1, 1:-1]
        y_next[y_init>0] = y_init[y_init>0]
        # y_next[50, 50] = 1
        if plotUpdate:
            im.set_data( y_next)
            fig.canvas.draw()

    if showPlots and not plotUpdate:
        fig = plt.figure()
        im = plt.imshow(y_next)
        plt.show()
    return y_next
