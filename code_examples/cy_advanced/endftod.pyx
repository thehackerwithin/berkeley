from __future__ import unicode_literals
cimport cpp_endftod

def endftod_cpp(s):
    """Converts a string from ENDF number format to float64 using the fast cpp

    Parameters
    ----------
    s : char *
    Plain string to convert.

    Returns
    -------
    float64
    """
    cdef char * cs
    if isinstance(s, str):
        s = s.encode()
    cs = s
    return cpp_endftod.endftod_cpp(cs)

def endftod_f(s):
    """Converts a string from ENDF number format to float64 using the slow fortran

    Parameters
    ----------
    s : char *
    Plain string to convert.

    Returns
    -------
    float64
    """
    cdef char * cs
    if isinstance(s, str):
      s = s.encode()
      cs = s
    return cpp_endftod.endftod_f(cs)
