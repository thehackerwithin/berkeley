from distutils.core import setup, Extension
import numpy as np

ext_modules = [Extension('c_version', ['src/my_function.c', 'src/pywrapper.c'],
                         include_dirs=[np.get_include(), 'include'],
                         extra_compile_args=["-O3", "-std=c99"],
                         extra_link_args=["-O3"],)]
                         

setup(
    name='c_version',
    description='c-version of find_potential_event_ptrs',
    ext_modules=ext_modules
    )
