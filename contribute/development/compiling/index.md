# Compiling
This page outlines the steps and resources required to compile OpenSpace from scratch on all platforms. Please read this page first, since it contains details that apply to all platforms. The links to the platform-specific pages can be found in the sidebar to the left or here:

## 0. Hardware requirements
  - Dedicated graphics card that supports OpenGL 4.6. Most new graphics cards have this capability, but sometimes you need to update your drivers. Nvidia graphics cards work best, but AMD cards will work (but currently have some known [issues](https://github.com/OpenSpace/OpenSpace/labels/GPU%3A%20AMD))
  - A mouse makes navigation easier than using a trackpad, since you need left, right, and middle mouse buttons
  - Enough disk space (all numbers approximate):
    - 1 GB of disk space to clone the GitHub repository
    - A minimum of 15 GB of additional disk space to build OpenSpace (more might be required depending on number of configurations and modules)
    - 10+ GB of disk space to hold the current OpenSpace dataset. Expect that to grow as time goes on


## 1. Development Tools
To compile OpenSpace on any platform you will need a Git client, CMake, and a C++ compiler that supports at least C++20.

### Git Client
OpenSpace uses Git submodules, which are not supported on all clients. Here are some suggestions for applications that have been used by members of the development team:
  1. [Fork](https://git-fork.com) A pay-if-you-will Git client for Windows
  1. [SourceTree](http://www.sourcetreeapp.com) A free and powerful Git client usable on Windows
  1. [GitKraken](https://www.gitkraken.com) A free GUI for Windows and Linux
  1. [SmartGit](http://www.syntevo.com/smartgit/) Another GUI Git client which runs on Windows

Please ensure that, specifially on Windows, to enable automatic line-ending conversion when checking out a repository (see information [here](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)) as some of the shader files in OpenSpace are sensitive to using the native line endings.

[Learning Git](http://pcottle.github.io/learnGitBranching) is a good, interactive webpage to learn the basics of using Git.

You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub


### CMake
[CMake](http://www.cmake.org) is a multi-platform project-generation tool. OpenSpace uses CMake so that we can more easily configure and compile OpenSpace on various platforms. We require CMake version 4.0 or above.

If you favor the commandline you can use the `cmake` command, but you might also like to know that you can use `ccmake`, which is CMake with an interactive curses interface.
  - Press `c` to configure your CMake files. Some configurations will require you to run the configure multiple times before you can generate.
  - Scroll up and down using the arrow keys, press Enter/Return to toggle or edit a value, again to confirm it.
  - When you make changes, confgure with `c` again: you won't be able to generate the build files until you do.
  - `t` will toggle advanced mode.
  - `g` will generate the files.
  - `e` to exit the errors/warning/help screen and take you back to the configuration so you can update it as necessary.
  - `q` will quit without generating changes.
  - When in doubt, `rm` in your CMake build directory and start again.


### Compiler / IDE
The platform specific pages found in the menu on the left contain more detailed information about the compilation platforms for each operating system. OpenSpace is written in C++20/C++23 and thus requires compiler versions that support a large portion of that standard. Thus we require the following versions of the compiler:
  - Windows: MSVC 19.50 (Visual Studio 2026, from version 18.2)
  - Linux: GCC 13 or Clang 17


## 2. Dependencies
Almost all dependencies in OpenSpace are handled via [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), which means that when cloning the GitHub repository, you should ensure that the `--recursive` flag is passed to the command.

The one dependency that is not included via submodules and that needs to be installed manually due to licensing reasons is [Qt](https://www.qt.io/download), which is used for the Launcher and profile editor GUI. Qt version 6.9 or higher is required. The open-source version of Qt, if applicable to you from a licensing point of view, can be obtained here: <https://www.qt.io/download-qt-installer>. As of 2020, this installer unfortunately needs a valid Qt user account. Select the `Custom installation` and select the newest version and any optional additional packages. Only the core Qt installation (e.g. `Qt 6.9.0`) is needed to run OpenSpace -- no additional Qt packages are required.

On Linux the [GDAL](http://www.gdal.org/) library also requires a manual install, for Windows, this library is contained in the repository, otherwise it is available via your package manager. Suggested version: 2.4.1 or above


## 3. Compiling
Roughly speaking, the following steps are taken on any platform:

  1. Clone the Git repository including all submodules. If you use the commandline for this, a standard command would be: `git clone --recursive --branch master https://github.com/OpenSpace/OpenSpace`. This example specifies the `master` branch, but another branch name can be substituted (read [Branching Model](http://nvie.com/posts/a-successful-git-branching-model) for more information about Git branches).
  1. Start CMake and drag in the `CMakeLists.txt` file from the OpenSpace folder
  1. Under "Where to build the binaries:" add a `/build` to the end of the path. Out-of-source builds are not supported.
  1. Press the "Configure" button and select the generator for your platform. In general, the option provided by default should be the correct one
  1. Press the "Generate" button and wait for it to finish
  1. Depending on the operating system, you can use the "Open Project" button to open the project in your IDE
  1. Compile

If there are any elements of these instructions that are unclear, feel free to suggest a change against this [repository](https://github.com/OpenSpace/OpenSpace-Docs) or join us in the #compiling channel on the [OpenSpace Slack](https://openspacesupport.slack.com).

Operating System specific commands
::::::{tab-set}
:::::{tab-item} Windows
### Windows
#### Development Tools
[Visual Studio 2026](http://www.visualstudio.com) is the standard Interactive Development Environment (IDE) for Windows. The "community" version is a free download for open-source projects. When you install it, be sure to select "Custom" configuration and select the C++ compiler -- it might not be included by default. You can also select a git client here ("Git GUI"). Installation could take a while (like an hour or so, depending on the machine).

:::{note}
The `Release` mode currently does not run correctly due to an [issue](https://github.com/OpenSpace/OpenSpace/issues/1657) with dependent libraries. Instead, use the `RelWithDebInfo` which has almost identical performance as the `Release` mode, but also provides information to debug potential crashes.
:::

#### Dependencies
Make sure to install the [Qt](https://www.qt.io/download) version that is called `MSVC 2019 64-bit`. After installing you should add the `bin` folder from the installation to your `PATH` environment variable, and it is highly recommended to have only one Qt `bin` folder in this variable (e.g. no different versions). It is possible to copy specific Qt .dll files from the Qt `bin` folder to the OpenSpace `bin` folder, but this is discouraged. Having both the Qt `bin` folder set in path **and** the dll files copied to OpenSpace `bin` might cause the program to crash.

#### Deploying
If you want to build OpenSpace to deploy to a third party that does not have a development environment, you can use the `deploy.bat` file found in the `support` folder. When starting this batch file, it will automatically build a fresh version of OpenSpace that includes the `sync` and `user` folder. The result of the deployment is a `.zip` file that can be shared with other computers that are then able to extract the file and run the application directly.

#### FAQ
If Windows is complaining that it cannot find the `VCOMP120.dll`, download the [Visual Studio Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe). On Windows 10 and up, this is not installed by default anymore. In general, this shouldn't be an issue if you have Visual Studio installed correctly, but it will be necessary to install on other computers that do not have the IDE installed.
:::::

:::::{tab-item} Ubuntu
### Ubuntu
OpenSpace requires the latest LTS version (22.04) as the Qt6 dependency is not available for 20.04 and before. For details on older versions of Ubuntu, see the "Outdated Versions" section below.

#### Development Tools
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

#### Dependencies
You can install all of the necessary dependencies through `apt`:

```bash
sudo apt install glew-utils libpng-dev freeglut3-dev git libxrandr-dev libxinerama-dev xorg-dev libxcursor-dev libcurl4-openssl-dev libxi-dev libasound2-dev libgdal-dev qt6-base-dev libmpv-dev libvulkan-dev
```

Also for Ubuntu 22.04, you'll also need to install gcc 13 (requires ubuntu-toolchain-r/test ppa):

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt install gcc-13 g++-13
```

#### Compiling
```bash
openSpaceHome="$HOME/source/OpenSpace"

git clone --recursive https://github.com/OpenSpace/OpenSpace "$openSpaceHome"

mkdir -p "$openSpaceHome/build"
cd "$openSpaceHome/build" || exit

cmake \
-DCMAKE_BUILD_TYPE:STRING="Release" \
-DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++-13 \
-DCMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc-13 \
-DCMAKE_CXX_STANDARD=20 \
-DASSIMP_BUILD_MINIZIP=1 "$openSpaceHome"

make -j
```

#### Outdated Versions of Ubuntu
Currently, pre-22.04 versions of Ubuntu use versions of `libmpv-dev` that are too old. An up-to-date debian package for mpv installation can be downloaded from [here](https://mpv.io/installation/), which would install an updated version of `libmpv-dev`.

Similarly, `qt6-base-dev` is not available but can be installed through other means such as [aqtinstall](https://github.com/miurahr/aqtinstall).

You can install gcc-13 using the following commands in case it is not supported:
The final commands configure Ubuntu's "update-alternatives", which allows a user to select among multiple installations of gcc:
```bash
sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get autoclean && sudo apt-get autoremove
```
reboot in case there are kernel changes

```bash
sudo apt-get install build-essential software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-13 g++-13
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 60 --slave /usr/bin/g++ g++ /usr/bin/g++-13
sudo update-alternatives --config gcc
```

If you don't want to install GCC 13 globally, you can overwrite the CMake options instead:
```text
CMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++-13
CMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc-13
```

If you do want to change the defaults you can find the information for it [here](https://stackoverflow.com/questions/7832892/how-to-change-the-default-gcc-compiler-in-ubuntu)


#### Troubleshooting
Make sure that you are using the correct version of gcc/g++
  - Double check `CMAKE_CXX_COMPILER` and `/usr/bin/c++ --version` to be sure. It should be at least 13.0

Error: libstdc++.so.6: could not read symbols: Missing DSO from command line
  - Try using g++ instead of gcc.

Error: GLSL 3.00 is not supported. Supported versions are: 1.10, 1.20, 1.30, 1.00 ES, and 3.00 ES
  - Enter the following line in the terminal before running, or add this to `~/.bashrc` or `~/.profile`:
 `export MESA_GL_VERSION_OVERRIDE=4.3`

Set a number format on your system that uses the dot as decimal separator. Otherwise you might see errors like this from OpenGL complaining about invalid numbers, e.g. `error: syntax error, unexpected INTCONSTANT, expecting IDENTIFIER or TYPE_IDENTIFIER or NEW_IDENTIFIER`.
  - Before launching, set the system locale to `en_US` or similar: `export LC_NUMERIC="en_US.UTF-8"`
:::::

:::::{tab-item} FreeBSD
### FreeBSD

#### Developer Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 13+ or Clang17+
  - CMake 3.25+

You can install gcc13 by executing: `sudo pkg install gcc13-devel`

You will need to set environment variables as follows (for sh, bash, zsh):
```bash
CC=gcc13; export CC
CXX=g++13; export CXX
CPP=c++13; export CPP
CXXFLAGS=-std=gnu++20; export CXXFLAGS
```

#### Dependencies
Install the following libraries:
  - libGL (`sudo pkg install libGL`)
  - GLEW (`sudo pkg install glew`)
  - Freeimage (`sudo pkg install freeimage`)
  - libsysinfo (`sudo pkg install libsysinfo`)
  - libinotify (`sudo pkg install libinotify`)
  - GDAL (`sudo pkg install gdal`)

Some other libraries will be needed....
:::::

:::::{tab-item} Fedora
### Fedora
OpenSpace has been tested on Fedora 33.

#### Development Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 13+
  - CMake 3.25+

#### Dependencies
Install the following dependencies using `dnf`:

```bash
sudo dnf install glfw-devel libXi-devel libXinerama-devel libXrandr-devel libXxf86vm-devel libcurl-devel mesa-libGLU-devel qt5-qtbase-devel gdal-devel harfbuzz-devel zziplib-devel
```

#### Compile OpenSpace
```bash
openSpaceHome="$HOME/source/OpenSpace"
git clone --recursive https://github.com/OpenSpace/OpenSpace "$openSpaceHome"
mkdir -p "$openSpaceHome/build"
cd "$openSpaceHome/build"

cmake \
-DCMAKE_BUILD_TYPE:STRING="Release" \
-DCMAKE_CXX_FLAGS:STRING="-DGLM_ENABLE_EXPERIMENTAL" \
-DOpenGL_GL_PREFERENCE:STRING=GLVND "$openSpaceHome"

make
```

##### clang
It could also be possible to build with clang. Then you have to install these packages:

```bash
sudo dnf install clang libcxx-devel
```

and use this `cmake` command

```bash
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE:STRING="Release" -DCMAKE_CXX_FLAGS:STRING="-DGLM_ENABLE_EXPERIMENTAL" -DOpenGL_GL_PREFERENCE:STRING=GLVND "$openSpaceHome"
```

#### Planet images not loading
The site `gibs.earthdata.nasa.gov` and possiby other data sources used by OpenSpace uses old TLS settings, see <https://www.ssllabs.com/ssltest/analyze.html?d=gibs.earthdata.nasa.gov&s=198.118.199.5>. The workaround is to run `sudo update-crypto-policies --set LEGACY` . See also <https://fedoraproject.org/wiki/Changes/StrongCryptoSettings2>
:::::
:::::{tab-item} Arch
### Arch

#### Development Tools
Install the following tools if they are not already available on your system:
  - Git 2.7+
  - GCC 13+
  - CMake 3.25+

#### Dependencies
```bash
pacman -S git gcc ninja vulkan-headers vulkan-icd-loader libglvnd gdal mpv libxinerama libxi
```
:::::
::::::


## 4. After compiling
The OpenSpace executable will be build in the `bin` folder (or `bin/Debug`/`bin/RelWithDebInfo` on Windows) and can be started from there. If everything succeeded you should see the Launcher window appearing:

:::{figure} launcher.png
:align: center
:width: 50%
The first window showing OpenSpace
:::

  - See [Getting Started](/getting-started/index) page for how to get started with running and using OpenSpace
  - The [Coding Style](../coding-style) describe the general coding guidelines that are applicable to the Ghoul, SGCT, and OpenSpace repository
  - See the [OpenSpace Layout](../folder-layout) page for more information about the structure of OpenSpace directories
  - See the [Deploy to a Windows Machine](../deploying-windows) page for additional information about what goes where on Windows (and how to copy from one machine to another).
  - The source code is written in C++20/C++23 with the feature set supported by Visual Studio 2026. The available features are detailed [here](https://docs.microsoft.com/en-us/cpp/visual-cpp-language-conformance)
  - Developers, before committing to the repository, read the post about [Structuring commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html). In general you can push to the feature branch you have been working on, but do not push directly to the `master` branch. For the `master` branch, a Pull Request should be used
  - Some useful information about C++ can be found in the form of [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md) and [Exception Handling](https://isocpp.org/wiki/faq/exceptions)


## 5. FAQ
**Q**:
```text
CMake Error at ext/ghoul/CMakeLists.txt:74 (include):
 include could not find load file:

   src/CMakeLists.txt


You have called ADD_LIBRARY for library Ghoul without any source files. This typically indicates a problem with your CMakeLists.txt file
CMake Error at ext/ghoul/CMakeLists.txt:304 (find_package):
 By not providing \"FindGLM.cmake\" in CMAKE_MODULE_PATH this project has
 asked CMake to find a package configuration file provided by \"GLM\", but
 CMake did not find one.

 Could not find a package configuration file provided by \"GLM\" with any of
 the following names:

   GLMConfig.cmake
   glm-config.cmake

 Add the installation prefix of \"GLM\" to CMAKE_PREFIX_PATH or set \"GLM_DIR\"
 to a directory containing one of the above files. If \"GLM\" provides a
 separate development package or SDK, be sure it has been installed.
```

**A**: The Git clone was not done recursively and thus the Ghoul CMakeLists.txt file is missing. Please reclone the repository using the `--recursive` flag
