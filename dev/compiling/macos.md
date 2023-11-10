# MacOS
This page describes the details of how to compile OpenSpace on macOS. For a more general overview for all platforms, see [Getting Started Guide: Compiling OpenSpace](https://github.com/OpenSpace/OpenSpace/wiki/Compiling)

Quick summary:
1. Install the [Development Tools](#development-tools)
   1. Git client (one of SourceTree, Git Kraken, or commandline)
   1. [CMake](#configure-with-cmake) to build Xcode configuration file
   1. [Homebrew](#homebrew) to install libraries and other tools
   1. [Xcode](#xcode) is the compiler and IDE on Mac
1. Install or build the Libraries
   1. Boost, (only required if you are building with the module Kameleon, which is not enabled by default)
1. [Build OpenSpace](#build)

## Development Tools
### Git Client
The source code for OpenSpace is distributed via GitHub, and so you will need a Git client to obtain a copy of the source code. OpenSpace uses git submodules, so a client which can handle these gracefully is preferred.

Xcode includes git, but the Xcode IDE cannot deal with recursive submodules. Once Xcode is installed, you can also use git via the command line in the Terminal app.

## Homebrew
Homebrew is billed as "the missing package manager" for macOS. Homewbrew installs the stuff you need that Apple didn't. It's easy to install and uninstall packages with Homebrew. See [http://brew.sh](http://brew.sh/) for instructions and to download and install Homebrew.

Once you have installed homebrew you can use it to install other useful utilities and libraries. Specifically, to build OpenSpace you will need to do the following:
```
  brew install glew
  brew install freeimage
  brew install mpv
  brew install vulkan-headers
  brew install vulkan-loader
  brew install brotli
  brew install gdal
```

Additionally, only if you are compiling with Kameleon:
```
  brew install boost
```

Please make use that the correct GDAL version is installed, as OpenSpace uses some recent features. We recommend a version that is newer than `2.2`.

For MacPorts: `port install glew boost freeimage gdal +curl`
See below for more information about freeimage[<sup>3</sup>](#freeimage).

## Xcode
Xcode is the Interactive Development Environment (IDE) tool for Mac. It's how you compile code on a Mac. It's a free install from the Mac App Store.

## OpenSpace
### Get the source with Git
Checkout OpenSpace/OpenSpace recursively using git.[<sup>1</sup>](#git). You probably want the `master` branch. If you are using `git` via the command line the command is:

```
  git clone --recurse-submodules  https://github.com/OpenSpace/OpenSpace
```

If you forget to clone with `--recursive` you can recover with a set of git commands (once only) to initialize and update (clone, the first time) the appropriate submodules. The command (starting from the top level directory) is:

```
  git submodule update --init --recursive
```

You only need to `--init` once, but you should do the recursive update anytime you checkout a different branch from the repository. (You also should do the `git submodule --init` if/when the submodules on which OpenSpace relies change (eg. a new one is added).)

### Configure with CMake
Change to the OpenSpace directory just created by cloning the git repo, and create a `build` directory (Your Xcode project file will live there). Run the CMake utility, which will eventually generate the Xcode project file. There are actually two ways you can do this:

  1. Run the GUI version of CMake (the CMake App that you installed from http://www.cmake.org). Set the Build directory to the subdirectory you just created, and set the Source directory to the directory just above it. Press the "Configure" button, and deal with any problems.
  1. Run the command line version of CMake which uses the curses library<sup>5</sup>(#curses), called `ccmake` (note the extra letter 'c'). In the Terminal app, change to the OpenSpace/build subdirectory and give the command `ccmake`, passing it the path to the source directory (which is just the directory above, aka the ".." directory). You also want to tell it you will use Xcode as the generator (otherwise the default is to create Unix Makefiles). Thus:

    `ccmake -G Xcode ..`

- If you built Boost from source then you need to tell CMake where it is.
- Do the "configure" step in CMake. For the GUI version simply press the "Configure" button. For the curses CLI version press "c".
- Fix any other configuration errors. You may have to tweak and adjust and re-run the configure step several times.

### Generate with CMake
- Do the "generate" step in CMake. This will create the Xcode project file, in the build subdirectory. Using the GUI version simply press the "Generate" button. For the curses CLI version press "g".

### Build
- Open the Xcode OpenSpace project `build/OpenSpace.xcodeproj`. Since you are already doing so much with the CLI you can do this with `open OpenSpace.xcodeproj`

- Select the target/scheme `ALL_BUILD` (if it isn't already) and build it (pull down Product -> Build)
- Verify build type (`Release` | `Debug`) by browsing to Product -> Scheme -> Edit Scheme -> Info tab -> Build Configuration.
- Your source code and bin directory will be in the top-level OpenSpace directory (just above the build subdirectory)
- Run `open -n OpenSpace.app <args>` from `OpenSpace/bin/openspace/Release/`


## Notes
### Git
 - You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub .
 - If you use the command line interface for `git`, remember that OpenSpace has many submodules. You'll want to `git clone --recursive` and/or use the `git submodule` commands. The `submodule` commands will need to be run in both the main repository and `ext/ghoul`.
 - Feel free to use a git client app instead, like Xcode or [SourceTree](https://www.sourcetreeapp.com/). Make sure you get your submodules though.
 - Did I mention to make sure you get your submodules?

### ccmake
 - `ccmake` is the curses interface to CMake.
 -  Create a build directory to store the configuration files anywhere outside the source files. This is where the Xcode project file will be generated by CMake. It's not required to be named `build` but that's common. You can keep it in the top level of your repository.
 -  It's easiest to run `ccmake` in the build directory, like so: `cd <build dir>; ccmake -G Xcode <repo dir>`
 -  Press `c` to configure your CMake files. Some configurations will require you to run the configure multiple times before you can generate.
 -  Scroll up and down using the arrow keys, press Enter/Return to toggle or edit a value, again to confirm it.
 -  When you make changes, confgure with `c` again: you won't be able to generate the build files until you do.
 -  `t` will toggle advanced mode.
 -  `g` will generate the files.
 -  `e` to exit the errors/warning/help screen and take you back to the configuration so you can update it as necessary.
 -  `q` will quit without generating changes.
 -  When in doubt, `rm` in your CMake build directory and start again.

### FreeImage
You could also `brew` [DevIL](http://openil.sourceforge.net/) or install [SOIL](http://www.lonesock.net/soil.html), but [FreeImage](http://freeimage.sourceforge.net/) is most actively maintained

### Curses
Curses is the Unix "cursor functions" library, which can be used to create a sort of Graphical User Interface (GUI) in a terminal environment. Thus the `ccmake` version of CMake acts like the full GUI App, but runs in a terminal window.
