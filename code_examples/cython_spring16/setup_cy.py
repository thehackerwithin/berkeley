#!/usr/bin/env python
from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("geometry_cy.pyx"),
      include_dirs=[numpy.get_include()])

# hack to copy build extension into this directory so we can use it without
# setting paths.
import glob
import shutil
for src in glob.glob("build/lib*/*"):
    shutil.copy(src, ".")
