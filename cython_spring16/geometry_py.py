import math


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

    r2 = r * r

    sum = 0.0
    for j in range(jmin, jmax+1):
        for i in range(imin, imax+1):
            if (i - x)**2 + (j - y)**2 < r2:
                sum += data[j, i]

    return sum
