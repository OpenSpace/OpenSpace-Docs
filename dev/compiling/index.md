# General Compiling
This page outlines the steps and resources required to compile OpenSpace from scratch on all platforms.

Please read this page first, since it contains details that apply to all platforms. Links to the platform-specific pages are included at the end of the page.


## 0. Hardware requirements
  - Dedicated graphics card that supports OpenGL 3.3 or higher. Most new graphics cards have this capability, but sometimes you need to update your drivers. Nvidia graphics cards work best, but AMD cards will work (but currently have some known issues).
  - A mouse makes navigation easier than using a trackpad, since you need both left and right mouse buttons
  - Enough disk space (all numbers approximate):
    - 1 GB of disk space to clone the GitHub repository
    - A minimum of 15 GB of additional disk space to build OpenSpace (more might be required depending on number of configurations and modules)
    - 10+ GB of disk space to hold the current OpenSpace dataset. Expect that to grow as time goes on.



## 1. Developer Tools
To compile OpenSpace on any platform you will need a Git client, CMake, and a C++ compiler that supports at least C++20.

### Git Client
See [Git](../git) for information about a Git client. Please ensure that, specifially on Windows, to enable automatic line-ending conversion when checking out a repository (see information [here](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)) as some of the shader files in OpenSpace are sensitive to use the native line endings.

### CMake
[CMake](http://www.cmake.org) is a multi-platform project-generation tool.  OpenSpace uses CMake so that we can more easily configure and compile OpenSpace on various platforms.  We require CMake version 3.25 or above.  If you favor the commandline you can use the `cmake` command, but you might also like to know that you can use `ccmake`, which is CMake with an interactive curses interface.

### Compiler / IDE
- [Visual Studio 2022](http://www.visualstudio.com) is the standard and recommended Interactive Development Environment (IDE) for Windows
- [XCode](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12) is the standard IDE on macOS
- On Linux you can install either `g++` or clang compilers, using either `yum` or `apt-get`, and use any editor of your choice

OpenSpace is written in C++20 and thus requires modern compiler versions that support a large portion of the new standard.  Thus we require the following versions of the compiler:
  - Windows:  MSVC 19.31 (Visual Studio 2022, from Version 17.1)
  - macOS:    AppleClang 13.1.6 (Xcode 13.4.1)
  - Linux:    GCC 11 or Clang 14



## 2. Required libraries
  - [SGCT](https://github.com/sgct/sgct) is the Simple Graphics Cluster Toolkit, which was developed at C-Research, Linköping University.  SGCT is included as a submodule in OpenSpace, so it will automatically be updated and built.
  - [GDAL](http://www.gdal.org/) is the Geospatial Data Abstraction Library.  For **Windows**, this library is contained in the repository, otherwise you it is available via `apt-get` or `homebrew` or MacPorts.  Suggested version: 2.1.2 or above
  - [Qt](https://www.qt.io/download) is used for the launcher / profile editor GUI. Suggested version: 6.0 or above.  The open-source version of Qt, if applicable to you, can be obtained here: https://www.qt.io/download-qt-installer  As of 2020, this installer unfortunately needs a Qt user account. Select the `Custom installation` and select the newest version and any optional additional packages. Only the core Qt installation (e.g. `Qt 6.2.0`) is needed to run OpenSpace - no additional Qt packages are required. For **Windows**, make sure to get the Qt version that is called `MSVC 2019 64-bit`. After installing you should add the `bin` folder from the installation to your `PATH` environment variable, and it is highly recommended to have only one Qt `bin` folder in this variable (e.g. no different versions). It is possible to copy specific Qt .dll files from the Qt `bin` folder to the OpenSpace `bin` folder, but this is discouraged. Having both the Qt `bin` folder set in path **and** the dll files copied to OpenSpace `bin` might cause the program to crash.



## 3. Compiling
Roughly speaking, the following steps are taken on any platform:

1. Clone the Git repository including all submodules.  If you use the commandline for this, a standard command would be: `git clone --recurse-submodules --branch master https://github.com/OpenSpace/OpenSpace`. This example specifies the `master` branch, but another branch name can be substituted (read [Branching Model](http://nvie.com/posts/a-successful-git-branching-model) for more information about Git branches).
1. Start CMake and "Configure" using the `CMakeLists.txt` file in the OpenSpace directory
1. Once you have the configuration set with no errors, use CMake to "generate" a project file
1. Compile

Follow one of the linked instruction pages for your specific platform:
  - [Windows](windows)
  - [macOS](macos)
  - [Ubuntu](ubuntu)
  - [FreeBSD](freebsd)
  - [Fedora](fedora)



## 4. After compiling
- See the [Getting Started Guide: Using OpenSpace](http://wiki.openspaceproject.com/docs/users/getting-started/general) page for how to get started with running and using OpenSpace.
- The [Coding Style](../coding-style) describe the general coding guidelines that are applicable to the Ghoul, SGCT, and OpenSpace repository
- See the [OpenSpace Layout](../folder-layout) page for more information about the structure of OpenSpace directories
- See the [Deploy to a Windows Machine](../deploying-windows) page for additional information about what goes where on Windows (and how to copy from one machine to another).
- The source code is written in C++20 with the feature set supported by Visual Studio 2022.  The available features are detailed [here](https://docs.microsoft.com/en-us/cpp/visual-cpp-language-conformance)
- Developers, before committing to the repository, read the post about [Structuring commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).  In general you can push to the feature branch you have been working on, but do not push directly to the `master` branch.  Instead, send a Pull Request.
- Some useful information about C++ can be found in the form of [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md) and [Exception Handling](https://isocpp.org/wiki/faq/exceptions)

## 5. FAQ
**Q**:
```
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
 to a directory containing one of the above files.  If \"GLM\" provides a
 separate development package or SDK, be sure it has been installed.
```

**A**: The Git clone was not done recursively and thus the Ghoul CMakeLists.txt file is missing.  Please reclone the repository using the `--recursive` flag

## Platform specific instructions
:::{toctree}
:maxdepth: 1
:name: toc-dev-compiling

windows
ubuntu
macos
freebsd
fedora
:::
