# Windows

## Development Tools
### Visual Studio 2022
[Visual Studio 2022](http://www.visualstudio.com) is the standard Interactive Development Environment (IDE)d for Windows. The "community" version is a free download for open-source projects. When you install it, be sure to select "Custom" configuration and select the C++ compiler -- it might not be included by default. You can also select a git client here ("Git GUI"). Installation could take a while (like an hour or so, depending on the machine). We are following the development of the C++ language quite closely, so there are more and more features that are no longer supported in Visual Studio 2019 or earlier versions.

### CMake
Download and run the [CMake installer](https://cmake.org/download/). If you are upgrading from version 3.4 or earlier, uninstall first. OpenSpace requires CMake version 3.25 or newer.


## Dependencies
### Advice on directory structure
Building OpenSpace will be easier if you follow a few guidelines about where you put the source code and where you build OpenSpace the the libraries it needs. OpenSpace depends on several other software components, which are loaded as git submodules when you do a recursive clone. These are all in the `ext/` subdirectory. One of these is a library called [Ghoul](https://github.com/OpenSpace/Ghoul), which has its own submodules, in `ext/Ghoul/ext/`.

### Qt
Make sure to install the [Qt](https://www.qt.io/download) version that is called `MSVC 2019 64-bit`. After installing you should add the `bin` folder from the installation to your `PATH` environment variable, and it is highly recommended to have only one Qt `bin` folder in this variable (e.g. no different versions). It is possible to copy specific Qt .dll files from the Qt `bin` folder to the OpenSpace `bin` folder, but this is discouraged. Having both the Qt `bin` folder set in path **and** the dll files copied to OpenSpace `bin` might cause the program to crash.

### Compiling Boost
Some of the optional modules have Boost as a dependency, which will need to be compiled separately. See [boost.org](https://www.boost.org) for a complete compilation instructions.
  1. Download the newest version of the source from [here](https://www.boost.org/users/download/)
  1. Unpack the boost folder to its final destination
  1. Start the Visual Studio x64 native tools command prompt and navigate to the folder
  1. In the boost folder, run `bootstrap.bat` and wait
  1. Run the `b2` command
  1. Add the boost folder as the `BOOST_ROOT` environment variable in Windows


## Build OpenSpace
### Get via Git
Checkout OpenSpace **recursively** using Fork, SourceTree, SmartGit, or the commandline. The commandline git command is: `git clone --recurse-submodules https://github.com/OpenSpace/OpenSpace`

### Building
  1. Open CMake and set "Where is the source code:" to the directory you just cloned from GitHub, for example `develop/OpenSpace`
  1. Set "Where to build the binaries:" to the `build` subdirectory, for example: `develop/OpenSpace/build`
  1. Set CMake variables to enable or disable specific modules
  1. In CMake, the `Qt6_DIR` should be automatically set. It may be necessary to manually set this to the location of your Qt installation if it does not show up
  1. Press the `Configure` button in CMake. Expect errors, which you will then correct
     - The first time you press `Configure` you are asked to select a "generator" for the project. Select "Visual Studio 16 2022"
     - Configure again, as needed, until you resolve all the errors (you can ignore anything that says "this warning is for project developers")
     - You can start over by selecting {menuselection}`File-->Delete Cache`
  1. Press the `Generate` button. This creates the Visual Studio Solution (`.sln`) file and supporting Project (`.vcxproj`) files
  1. The generated solution file can be opened via `Open Project`. Otherwise, navigate to the build directory and open the main Solution file, called `OpenSpace.sln`
  1. If it isn't already, select the "OpenSpace" project as a startup project via right click in the "Solution Explorer" and build them
  1. You can start either application from within Visual Studio or by navigating to `OpenSpace/bin/openspace`


## Notes
### Git
You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub.

If you use the command line interface for `git`, remember that OpenSpace has many submodules. You'll need to use `git clone --recursive` and/or use the `git submodule` commands. The `submodule` commands will need to be run in both the main repository and `ext/ghoul`.

### Visual Studio
The `Release` mode currently does not run correctly due to an [issue](https://github.com/OpenSpace/OpenSpace/issues/1657) with dependent libraries. Instead, use the `RelWithDebInfo` which has almost identical performance as the `Release` mode, but also provides information to debug potential crashes.

### FAQ
If Windows is complaining that it cannot find the `VCOMP120.dll`, download the [Visual Studio Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe). On Windows 10 and up, this is not installed by default anymore. In general, this shouldn't be an issue if you have Visual Studio installed correctly, but it will be necessary to install on other computers that do not have the IDE installed.
