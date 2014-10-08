import numpy as np
from matplotlib import pyplot as plt
plt.ion()

def simulateParticles_loop( n=50, n_gen=100, showPlots=True):
    ''' simulate gaussian motion of n particles for n_gen steps each
    '''
    # store the value of each particle at every step
    f_all = np.zeros((n,n_gen))
    
    for i in range(n):
        y = 0
        f_all[i,0] = y
        for j in range(1,n_gen):
            y += np.random.randn()
            f_all[i,j] = y

    x_grid, y_grid = np.mgrid[0:n, 0:n_gen]

    if showPlots:
        plt.figure()
        plt.plot(y_grid.T, f_all.T, alpha=.2)

        plt.figure()
        plt.hist2d(y_grid.ravel(), f_all.ravel(), bins=(n_gen, 50))

        plt.show()

    return y_grid, f_all

def simulateParticles_vec( n=50, n_gen=100, showPlots=True):
    ''' simulate gaussian motion of n particles for n_gen steps each
    '''
    f_0 = np.zeros(n)
    f_diff = np.random.randn(n, n_gen)
    f_diff[:,0] = 0
    f_all = f_0[:,np.newaxis] + f_diff.cumsum(1)

    x_grid, y_grid = np.mgrid[0:n, 0:n_gen]

    if showPlots:
        plt.figure()
        plt.plot(y_grid.T, f_all.T, alpha=.2)

        plt.figure()
        plt.hist2d(y_grid.ravel(), f_all.ravel(), bins=(n_gen,50))

        plt.show()

    return y_grid, f_all

def rotateParticles(n=50, n_gen=100):
    ''' simulate gaussian motion of n particles for n_gen steps each
        and then rotate all the particles paths
    '''
    y_grid, f_all = simulateParticles_vec(n=n, n_gen=n_gen)

    ang = 0./180.*np.pi
    xy = np.array([y_grid.ravel(), f_all.ravel()])
    R = np.array( [[np.cos(ang), -np.sin(ang)],[np.sin(ang), np.cos(ang)]])
    xy_rot = R.dot(xy)
    fig = plt.figure()
    lines = plt.plot(xy_rot[0].reshape(f_all.shape).T, 
                     xy_rot[1].reshape(f_all.shape).T, alpha=.2)

    for ang in np.linspace(-np.pi/4,np.pi/4., 45):
        R = np.array( [[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
        xy_rot = R.dot(xy)

        xy_2d = xy_rot.reshape((2, n, n_gen))

        for i in range(n):
            lines[i].set_data( xy_2d[0,i], xy_2d[1,i]) 

        fig.canvas.draw()

