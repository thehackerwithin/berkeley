## Build Systems

![XKCD compiling](https://imgs.xkcd.com/comics/compiling.png)

The example C library here is linked here via a [git submodule](https://git-scm.com/docs/git-submodule).
Submodules can be a little confusing.

Run
```
git submodule init && git submodule update
```
from within this repository to get the code (or follow the link on github and download manually).

We're going to look at a few common build systems for C, C++, and Fortran libraries.
If you have a really small library with just a handful of C libraries and no complicated dependencies,
then compiling it might be as simple as
```sh
# compile .c sources into .o binary files
gcc -fPIC -c source/*.c source/internal/*.c -Iinclude/utf8rewind
# create static library
ar rcs libutf8rewind.a *.o
# create shared library (.so for linux, .dylib for mac, .dll for windows)
gcc -shared -o libutf8rewind.so *.o
```

This gets tedious to do by hand repeatedly, so we'll often write a Makefile, like the following:
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

Makefiles can get really complicated and can be the subject of several talks on their own.
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
different variables and flags to configure, and where to look for more debugging
information when things go wrong (`config.log` contains all the detailed output of
all the probe tests `configure` runs).

