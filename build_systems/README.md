## Build Systems

![XKCD compiling](https://imgs.xkcd.com/comics/compiling.png)

The example C libraries here are linked here via [git submodules](https://git-scm.com/docs/git-submodule).
Submodules can be a little confusing.

Run
```
git submodule init && git submodule update
```
from within this repository to get the code (or follow the links on github and download manually).

We're going to look at a few common build systems for C, C++, and Fortran libraries.
If you have a really small library with just a handful of C source files and no complicated
dependencies, then compiling it might be as simple as
```sh
# compile .c sources into .o binary files
gcc -fPIC -c source/*.c source/internal/*.c -Iinclude/utf8rewind
# create static library
ar rcs libutf8rewind.a *.o
# create shared library (.so for linux, .dylib for mac, .dll for windows)
gcc -shared -o libutf8rewind.so *.o
```

This gets tedious to do by hand repeatedly, so we'll often write a Makefile like the following:
```Makefile
# allow easily using a different compiler by setting CC
CC ?= gcc
LIBNAME := libutf8rewind

ifeq ($(OS), Windows_NT)
SHLIB_EXT = dll
FPIC =
else ifeq ($(shell uname), Darwin)
SHLIB_EXT = dylib
FPIC = -fPIC
else
SHLIB_EXT = so
FPIC = -fPIC
endif

OBJS = source/internal/casemapping.o \
       source/internal/codepoint.o \
       source/internal/composition.o \
       source/internal/database.o \
       source/internal/decomposition.o \
       source/internal/seeking.o \
       source/internal/streaming.o \
       source/unicodedatabase.o \
       source/utf8rewind.o

.PHONY : all objects clean

.DEFAULT_GOAL := all

all: $(LIBNAME).a $(LIBNAME).$(SHLIB_EXT)

# magic makefile variables, see
# https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
%.o : %.c
	$(CC) $(FPIC) -Iinclude/utf8rewind -c $< -o $@

objects: $(OBJS)

# static library
$(LIBNAME).a: $(OBJS)
	ar rcs $(LIBNAME).a $(OBJS)

# shared library
$(LIBNAME).$(SHLIB_EXT): $(OBJS)
	$(CC) -shared -o $(LIBNAME).$(SHLIB_EXT) $(OBJS)

clean:
	rm -f $(OBJS) $(LIBNAME).a $(LIBNAME).$(SHLIB_EXT)
```

Makefiles can get really complicated and could be the subject of several talks on their own.
Makefiles let you express dependencies between different compilation tasks, but get messy
once you try to encode complicated logic or platform differences in compiler flags, which
source files to build, output file names to use, etc. They also don't handle detecting
properties of the system you run them on, or finding dependency tools or libraries that
may be needed during the build process. So many projects beyond a certain size use a
higher-level build system, most of which automatically generate makefiles for you.

The oldest and most commonly used higher-level build system is the GNU Autotools.
It is a collection of tools: `autoconf` takes a `configure.ac` file and autogenerates
a `configure` shell script, and `automake` takes a `Makefile.am` file and autogenerates
a `Makefile.in` template. When the user runs `configure` it detects properties of their
system, what OS and compiler they are using, what capabilities and libraries are available
with a series of small tests called "probes." When `configure` is done it populates a
`Makefile` from the `Makefile.in` template but with the specific information from the
user's system filled in. There's also `libtool` which can be used at build time to
assist in creating shared libraries, which used to be more complicated when people
were using dozens of different Unix variations.

![Handy flow chart](https://upload.wikimedia.org/wikipedia/commons/8/84/Autoconf-automake-process.svg)

I wouldn't recommend using Autotools in a new project since it's very confusing and
many of the things it's checking for are no longer all that relevant. But so many
established projects use it that it's worth practicing using it, how you can set
different variables and flags to configure (e.g. `--enable-shared` and `--enable-static`
to respectively build shared and static libraries), and where to look for more debugging
information when things go wrong (`config.log` contains all the detailed output of
all the probe tests `configure` runs).

[CMake](https://cmake.org) is a more modern alternative. Instead of a configure script,
you run the `cmake` program which reads a `CMakeLists.txt` file and then generates a
`Makefile` (or alternative output formats like XCode or Visual Studio project files,
or inputs for a modern make-like tool called [ninja](https://ninja-build.org/)).
The `CMakeLists.txt` file uses its own custom language for declaring source files,
library dependencies, and custom build tasks. In the simple case above it looks like
```cmake
cmake_minimum_required (VERSION 2.8.11)

project (utf8rewind C)

add_library (utf8rewind
  source/internal/casemapping.c
  source/internal/codepoint.c
  source/internal/composition.c
  source/internal/database.c
  source/internal/decomposition.c
  source/internal/seeking.c
  source/internal/streaming.c
  source/unicodedatabase.c
  source/utf8rewind.c
)

target_include_directories (utf8rewind PUBLIC
  include/utf8rewind
)

set_target_properties (utf8rewind PROPERTIES
  POSITION_INDEPENDENT_CODE ON
)
```

CMake has very extensive [documentation](https://cmake.org/cmake/help/latest/) and
can be customized in many ways for advanced use, either by command line flags such as
`-DBUILD_SHARED_LIBS=ON` or by custom commands in the CMakeLists scripting language
such as `find_library` and `add_custom_command`.

Lastly there is [gyp](https://gyp.gsrc.io/) (generate your projects) which was developed
for building Chrome. It's being phased out by its original developers for Chrome and it's
very sparsely documented, but still gets used fairly often in the Node.js world. It is
a Python-based build tool that reads `.gyp` files and is focused on outputting more
human-readable IDE project files than what CMake would generate. The author of this
particular example library utf8rewind happens to prefer it.
