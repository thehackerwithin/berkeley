cy_advanced
===========

Advanced Cython examples and notebooks:

 * Start by running make to build everything (linux users will need to change
   how the python library is linked)
 * After building go through `cython.ipynb`:
  * The first example compares the same prime number finder in cython and python
  * The second example shows how to wrap C++ and Fortran using cython
 * The memoryviews section is in `memview_bench.ipynb` (credit to @jakevdp)
 * More memoryviews benchmarks are in `memview_bench_2.ipynb`
 * The final cython code in the markdown section of `cython.ipynb` can be linked
   against the included code in `trapfilter.c`. This is meant to be instructive
   for situations where passing array data to C/C++ is desirable.
