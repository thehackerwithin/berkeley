#This is a cython include file it imports symbols form a C++ header


cdef extern from "endftod.h":
    double endftod_cpp(char * s) except +
    double endftod_f(char * s) except +
