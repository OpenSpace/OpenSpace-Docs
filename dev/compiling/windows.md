# Windows
This page began as the Few-Frills How-To for building on Windows 10, but now we are trying to fill it in with more details.  Please help give us feedback on what needs to be improved.

Quick summary:
1. [Development Tools](#development-tools)
   1. Git client
   1. [CMake](#cmake)
   1. [Visual Studio](#visual-studio-2022)
1. [Build/Install Libraries](#buildinstall-libraries)
1. [Build OpenSpace](#build-openspace)
1. [Notes](#notes)

## Development Tools
### Git Client
The source code for OpenSpace is distributed via GitHub, and so you will need a [Git](https://github.com/OpenSpace/OpenSpace/wiki/Git) client to obtain a copy of the source code.  OpenSpace uses git submodules, so a client which can handle these gracefully is preferred.

### Visual Studio 2022
[Visual Studio 2022](http://www.visualstudio.com) is the standard Interactive Development Environment (IDE) for Windows.  The "community" version is a free download.  When you install it, be sure to select "Custom" configuration and select the C++ compiler -- it is not included by default.  You can also select a git client here ("Git GUI").  Installation could take a while (like an hour or so, depending on the machine).  We are following the development of the C++ language quite closely, so there are more and more features that are no longer supported in Visual Studio 2017.

### CMake
- Download and run the [CMake installer](https://cmake.org/download/)
- If you are upgrading from version 3.4 or earlier, uninstall first.  We require CMake 3.12 or newer.

## Build/Install Libraries
### Advice on directory structure
Building OpenSpace will be easier if you follow a few guidelines about where you put the source code and where you build OpenSpace the the libraries it needs.
OpenSpace depends on several other software components, which are loaded as git submodules when you do a recursive clone.  These are all in the `ext/` subdirectory.   One of these is a library called Ghoul, and Ghoul has its own submodules, in `ext/Ghoul/ext/`.

## Build OpenSpace
### Get via Git
Checkout OpenSpace **recursively** using SourceTree, SmartGit, or the command line.  The command line git command is:
    `git clone --recurse-submodules https://github.com/OpenSpace/OpenSpace`

### Building
1. Open CMake and set "Where is the source code:" to the directory you just cloned from GitHub, for example `develop/OpenSpace`.
1. Set "Where to build the binaries:" to the `build` subdirectory, for example: `develop/OpenSpace/build`
1. Set CMake variables to enable or disable specific modules
1. Create an environment variable in your Windows system for the path to the Qt directory. Do this by searching for `Edit the system environment variables` in the Windows search box and open it. Open `Environment variables...`. In `System variables`, click on `Path` and `Edit` and add the path to the folder where the Qt binaries are stored. For example, the path might look something like: `C:/Qt/6.2.0/msvc2019_64/bin`. In CMake, the `Qt6_DIR` should now be automatically set. It may be necessary to manually set this to the location of your Qt installation if it does not show up.
1. Press the `Configure` button in CMake.  Expect errors, which you will then correct:
    - The first time you press `Configure` you are asked to select a "generator" for the project.  Select "Visual Studio 16 2022 Win64" (the Win64 is the important part)
    - Configure again, as needed, until you resolve all the errors (except anything that says "this warning is for project developers")
    - You can start over by pulling down "File->Delete Cache".
1. Press the `Generate` button.  This creates the Visual Studio Solution (`.sln`) file and supporting Project (`.vcxproj`) files.  
1. The generated solution file can be opened via `Open Project`.  Otherwise, navigate to the build directory and open the main Solution file, called `OpenSpace.sln`
1. Select the "OpenSpace" project as a startup project via right click in the "Solution Explorer" and build them
1. You can start either application from within Visual Studio or by navigating to `OpenSpace/bin/openspace`

### Compiling Boost
Some of the optional modules have Boost as a dependency, which will need to be compiled separately. See [boost.org](https://www.boost.org) for a complete compilation instructions.
1. Download the newest version of the source from [here](https://www.boost.org/users/download/).
1. Unpack the boost folder to its final destination
1. Start the Visual Studio x64 native tools command prompt and navigate to the folder
1. In the boost folder, run `bootstrap.bat` and wait
1. Run the `b2` command
1. Add the boost folder as the `BOOST_ROOT` environment variable

## Notes
### CMake build folder
- Create your build directory to store the configuration files anywhere outside the source files.  It's not required to be named `build` but that's common. You can keep it in the top level of your repository.
- When in doubt File -> Delete Cache and start again.
- To execute cmake from visual studio command line, cmake args must be passed with -D<cmake flag>:
```
        cd develop/OpenSpace
        mkdir build & pushd build
        cmake -DCMAKE_BUILD_TYPE=Release -G "Visual Studio 16 2022 Win64" ..
        popd
        cmake --build build --config Release
```

### Git
- You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub.
- If you use the command line interface for `git`, remember that OpenSpace has many submodules.  You'll want to `git clone --recursive` and/or use the `git submodule` commands. The `submodule` commands will need to be run in both the main repository and `ext/ghoul`.

### Visual Studio
- When switching between `Release` and `Debug` configuration in Visual Studio, there has been cases where some targets aren't getting rebuilt properly. Therefore, highlight `tinyxml2static` and `VRPN` in the solution, right click and select `Rebuild Selection` _after_ changing build configuration.

### FAQ
If Windows is complaining that it cannot find the `VCOMP120.dll`, download https://www.microsoft.com/en-us/download/details.aspx?id=40784 the Visual Studio 2013 Redistributable.  On Windows 10, this is not installed by default anymore.
