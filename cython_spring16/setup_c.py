#!/usr/bin/env python
from distutils.core import setup, Extension
import numpy

setup(ext_modules=[Extension('geometry_c', ['geometry_c.c'])],
      include_dirs=[numpy.get_include()])

# hack to copy build extension into this directory so we can use it without
# setting paths.
import glob
import shutil
for src in glob.glob("build/lib*/*"):
    shutil.copy(src, ".")
