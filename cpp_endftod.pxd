#This is a cython include file it imports symbols form a C++ header


cdef extern from "endftod.h":
    double endftod_cpp(char * s) except +
    double endftod_f(char * s) except +


# or we could do this sans header

#cdef extern double endftod_cpp(char * s) except +
#cdef extern double endftod_cpp(char * s) except +
