all: endf simplecy

flags = -O3

simplecy : simplecy.pyx
			python simplesetup.py build_ext --inplace

py_ext = .dylib # change this to .so on linux
py_libl := $(shell python -c "from distutils.sysconfig import PREFIX; print PREFIX")
py_lib = $(py_libl)/lib/libpython2.7$(py_ext)
endf: endftod_f.o endftod_cpp.o endftod_pyx.o
			g++ endftod_f.o endftod_cpp.o endftod_pyx.o -shared -pthread -fPIC -fwrapv -O3 -Wall -fno-strict-aliasing -lgfortran $(py_lib) -o endftod.so

endftod_f.o: endftod.f90
			gfortran $(flags) -c endftod.f90 -o endftod_f.o

endftod_cpp.o: endftod.cpp
			g++ $(flags) -c endftod.cpp -o endftod_cpp.o

py_header := $(shell python -c "from distutils.sysconfig import get_python_inc; print get_python_inc()")
endftod_pyx.o: endftod.pyx
			cython --cplus endftod.pyx -o endftod_pyx.cpp
			g++ $(flags) -c endftod_pyx.cpp -I$(py_header)

clean:
			rm -rf *.o
