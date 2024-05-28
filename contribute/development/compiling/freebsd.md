# FreeBSD
This page contains specific information necessary to compile OpenSpace on FreeBSD. This page has the [general instructions](index) as a required reading.

## Developer Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 13+ or Clang17+
  - CMake 3.25+

### gcc
You can install gcc13 by executing: `sudo pkg install gcc13-devel`

You will need to set environment variables as follows (for sh, bash, zsh):
```bash
CC=gcc13; export CC
CXX=g++13; export CXX
CPP=c++13; export CPP
CXXFLAGS=-std=gnu++20; export CXXFLAGS
```

## Dependencies
Install the following libraries:
 - libGL (`sudo pkg install libGL`)
 - GLEW (`sudo pkg install glew`)
 - Freeimage (`sudo pkg install freeimage`)
 - libsysinfo (`sudo pkg install libsysinfo`)
 - libinotify (`sudo pkg install libinotify`)
 - GDAL (`sudo pkg install gdal`)

Some other libraries will be needed....
