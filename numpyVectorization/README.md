This contains some examples for using numpy array operations. 
The iPython notebook file is a good starting point. 

The examples include:

- diffusion
- gaussian walk

What's shown below is shown in more detail in the iPython notebook.

## Efficient Numerical Code With Numpy Vectorization

#### C and fortran paradigm: For loops
- Python loops have python overhead 
- Numpy operations are lower level
```
x = 0
for i in range(10):
    x+=1
```

#### Numpy paradigm: Array operations
- Useful when performing the same operation to many numerical pieces of data.
- Ex: Adding all the elements from two lists of numbers

#### Simple operations
- Addition two lists of numbers
- numpy array functions 
  - np.sum(), np.cumsum(), np.exp()

#### Some Numpy version have additional optimizations:
Under the hood, complex operations will automatically be run on multiple 
processors.

- SIMD
- Intel MKL
- To get these benefits in anaconda:

```
conda install mkl
```

#### Some Types of Numerical Data Structures
- Grid data - possibly regularly spaced
- Point data

#### Diffusion Example
- Finite Difference Examples: diffusion.py
  - Grid data
  - Write equation
  - Draw arrays and arrows referencing location to array
- 1-D
  - For loop: diff1d_loop()
  - array version: diff1d_vec()
  - Show 2-d plot of all results to compare to gaussian motion
- 2-D
  - For loop: diff2d_loop()
  - array version: diff2d_vec()
- Draw overlapping boxes to show how slice indexing should work
- lineprofiler: https://github.com/rkern/line_profiler

Basic iPython Usage:

```
run diffusion
# Visualized the 1-D computations
diff1d_vec()

# test the time difference
%timeit diff1d_loop(plotUpdate=Fase)
%timeit diff1d_vec(plotUpdate=Fase)

# Visualized the 2-D computations
diff2d_vec()
# test the time difference
%timeit diff2d_loop(plotUpdate=Fase)
%timeit diff2d_vec(plotUpdate=Fase)
```

#### Monte Carlo Example
- Gaussian motion
- Individual particles

#### Data reshaping
- Array views
- Rotating 2-D grid of points
- Rotating 2-D list of points from gaussian motion

#### More performance
- numexpr
- cython
- pyOpenCl
