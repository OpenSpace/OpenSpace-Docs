# FreeBSD

## Developer Tools
Install the following tools:
 - Git 2.7+
 - GCC 11+ or Clang
 - CMake 3.12+

### Git
You can install git as follows:
`sudo pkg install git`

### CMake
You can install cmake as follows:
`sudo pkg install cmake`
Before version 3.10.0, you will need to modify `/usr/local/share/cmake/Modules/FindPkgConfig.cmake` as follows
```
         endif()
       endif()
+      if(CMAKE_SYSTEM_NAME STREQUAL "FreeBSD" AND NOT CMAKE_CROSSCOMPILING)
+        list(APPEND _lib_dirs "libdata/pkgconfig")
+      endif()
       list(APPEND _lib_dirs "lib/pkgconfig")
       list(APPEND _lib_dirs "share/pkgconfig")
```

### gcc
You can install gcc11 as follows
`sudo pkg install gcc11-devel`

You will need to set environment variables as follows (for sh, bash, zsh):
```
CC=gcc11; export CC
CXX=g++11; export CXX
CPP=c++11; export CPP
CXXFLAGS=-std=gnu++17; export CXXFLAGS
```

## Libraries
Install the following libraries:
 - cspice (compile, install by yourself, and rename cspice.a and csupport.a to libcspice.a and libcsupport.a for convenience.)
 - libGL (`sudo pkg install libGL`)
 - GLEW (`sudo pkg install glew`)
 - Freeimage (`sudo pkg install freeimage`)
 - libsysinfo (`sudo pkg install libsysinfo`)
 - libinotify (`sudo pkg install libinotify`)
 - GDAL (`sudo pkg install gdal`)

Some other libraries will be needed....

## Compilation
### remove minizip line in assimp/CMakeLists.txt.
To avoid linking issues of minizip, remove next line

    use_pkgconfig(UNZIP minizip)

in ext/ghoul/ext/assimp/CMakeLists.txt.

### Background
`use_pkgconfig` macro defined in `cmake-modules/FindPkgMacros.cmake` doesn't work for FreeBSD at now.  `FindPkgMacros.cmake` depends on `FindPkgConfig.cmake` that is contained in cmake distribution, and it doesn't work for FreeBSD because FreeBSD's pkgconfig dir is `${PREFIX}/libdata/pkgconfig` that is different with usual one.  This directory structure is not considered by FindPkgCOnfig.cmake. Thiis issue will be fixed if merge-request is accepted: [Merge request !1108 on gitlab at kitware](https://gitlab.kitware.com/cmake/cmake/merge_requests/1108)
