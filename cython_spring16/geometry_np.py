import math
import numpy as np

def sum_circle(data, x, y, r):
    """Sum array values that fall within the given circle.

    Parameters
    ----------
    data : numpy.ndarray
        The array to sum.
    x, y, r : float
        The center and radius of circle, in array coordinates.
    """
    
    imin = math.floor((x - r) + 0.5)
    imax = math.floor((x + r) + 0.5)
    jmin = math.floor((y - r) + 0.5)
    jmax = math.floor((y + r) + 0.5)

    irange = range(imin, imax+1)
    jrange = range(jmin, jmax+1)

    data_stamp = data[jmin:jmax+1, imin:imax+1]

    X, Y = np.meshgrid(irange, jrange)
    mask = (X - x)**2 + (Y - y)**2 < r**2
    
    return np.sum(data_stamp[mask])
