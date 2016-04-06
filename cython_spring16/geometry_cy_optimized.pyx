cimport numpy as np
from libc.math cimport floor

#@cython.boundscheck(False)
#@cython.wraparound(False)
def sum_circle(double[:,:] data not None, double x, double y,
               double r):
    """sum_circle(data, x, y, r)

    Sum array values that fall within the given circle.

    Parameters
    ----------
    data : numpy.ndarray
        The array to sum.
    x, y, r : float
        The center and radius of circle, in array coordinates.
    """
   
    cdef double r2, sum
    cdef size_t i, j, imin, imax, jmin, jmax

    imin = <size_t>floor((x - r) + 0.5)
    imax = <size_t>floor((x + r) + 0.5)
    jmin = <size_t>floor((y - r) + 0.5)
    jmax = <size_t>floor((y + r) + 0.5)

    r2 = r * r

    sum = 0.0
    for j in range(jmin, jmax+1):
        for i in range(imin, imax+1):
            if (i - x)**2 + (j - y)**2 < r2:
                sum += data[j, i]

    return sum
