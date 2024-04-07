# Ubuntu
This page contains specific information necessary to compile OpenSpace on Ubuntu. This page has the [general instructions](index) as a required reading.

OpenSpace requires the latest LTS version (22.04) as the Qt6 dependency is not available for 20.04 and before. For details on older versions of Ubuntu, see the "Outdated Versions" section below.

## Development Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 13+
  - CMake 3.25+

If it not provided through `apt`, you can install CMake version 3.25 through the following commands:
  1. `wget https://github.com/Kitware/CMake/releases/download/v3.25.0/cmake-3.25.0-linux-x86_64.sh -q -O /tmp/cmake-install.sh`
  1. `chmod u+x /tmp/cmake-install.sh`
  1. `mkdir /opt/cmake`
  1. `/tmp/cmake-install.sh --skip-license --prefix=/opt/cmake`
  1. `ln -s /opt/cmake/bin/* /usr/local/bin`

There are specific CMake variables that need to be set. See the "Compile OpenSpace" section below for specific commandline arguments to CMake, including `CMAKE_BUILD_TYPE`, `CMAKE_CXX_FLAGS`, `OpenGL_GL_PREFERENCE`, etc. If using the CMake GUI, these will need to be set manually.


## Dependencies
You can install all of the necessary dependencies through `apt`:

`sudo apt install glew-utils libpng-dev freeglut3-dev git libxrandr-dev libxinerama-dev xorg-dev libxcursor-dev libcurl4-openssl-dev libxi-dev libasound2-dev libgdal-dev libboost1.74-dev qt6-base-dev libmpv-dev libvulkan-dev`


## Compile OpenSpace
```bash
openSpaceHome="$HOME/source/OpenSpace"

git clone --recursive https://github.com/OpenSpace/OpenSpace "$openSpaceHome"

mkdir -p "$openSpaceHome/build"
cd "$openSpaceHome/build" || exit

cmake \
-DCMAKE_BUILD_TYPE:STRING="Release" \
-DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++-11 \
-DCMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc-11 \
-DASSIMP_BUILD_MINIZIP=1 "$openSpaceHome"

make -j
```


## Outdated Versions of Ubuntu
Currently, pre-22.04 versions of Ubuntu use versions of `libmpv-dev` that are too old. An up-to-date debian package for mpv installation can be downloaded from [here](https://mpv.io/installation/), which would install an updated version of `libmpv-dev`.

Similarly, `qt6-base-dev` is not available but can be installed through other means such as [aqtinstall](https://github.com/miurahr/aqtinstall)

You can install gcc-13 using the following commands in case it is not supported:
The final commands configure Ubuntu's "update-alternatives", which allows a user to select among multiple installations of gcc:
```
sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get autoclean && sudo apt-get autoremove
```
reboot in case there are kernel changes

```
sudo apt-get install build-essential software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-13 g++-13
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 60 --slave /usr/bin/g++ g++ /usr/bin/g++-13
sudo update-alternatives --config gcc
```

If you don't want to install GCC 13 globally, you can overwrite the CMake options instead:
```
CMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++-13
CMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc-13
```

If you do want to change the defaults you can find the information for it [here](https://stackoverflow.com/questions/7832892/how-to-change-the-default-gcc-compiler-in-ubuntu)


## Troubleshooting
Make sure that you are using the correct version of gcc/g++
 - Double check `CMAKE_CXX_COMPILER` and `/usr/bin/c++ --version` to be sure. It should be at least 11.0

Error: libstdc++.so.6: could not read symbols: Missing DSO from command line
 - Try using g++ instead of gcc.

Error: GLSL 3.00 is not supported. Supported versions are: 1.10, 1.20, 1.30, 1.00 ES, and 3.00 ES
 - Enter the following line in the terminal before running, or add this to `~/.bashrc` or `~/.profile`:
 `export MESA_GL_VERSION_OVERRIDE=4.3`

Set a number format on your system that uses the dot as decimal separator. Otherwise you might see errors like this from OpenGL complaining about invalid numbers, e.g. `error: syntax error, unexpected INTCONSTANT, expecting IDENTIFIER or TYPE_IDENTIFIER or NEW_IDENTIFIER`.
 - Before launching, set the system locale to `en_US` or similar: `export LC_NUMERIC="en_US.UTF-8"`
