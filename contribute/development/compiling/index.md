# Compiling
This page outlines the steps and resources required to compile OpenSpace from scratch on all platforms. First, some one-time-setup information is provided, followed by the guidelines on how to compile OpenSpace for each supported operating system.

OpenSpace has been verified to compile on Windows 11, Ubuntu 26.04, Fedora 44, and Arch Linux. Unfortunately, macOS is not supported as Apple laptops lack support for the required `double` precision accuracy (see the [specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) Section 2.1).


## 0. Hardware requirements
- Dedicated graphics card that supports OpenGL 4.6. All new graphics cards have this capability, but you might need to update your drivers. The intention is to support all graphics card vendors equally, but currently Nvidia graphics cards work best, followed by AMD cards (see the open [issues](https://github.com/OpenSpace/OpenSpace/labels/GPU%3A%20AMD)), followed by Intel Arc cards (see the open [issues](https://github.com/OpenSpace/OpenSpace/issues?q=state%3Aopen%20label%3A%22GPU%3A%20Intel%22))
- A mouse makes navigation easier than using a trackpad, since you need left, right, and middle mouse buttons. Mice with a fourth and fifth mouse button are optimal
- Enough disk space (all numbers approximate):
  - 2 GB of disk space to clone the GitHub repository
  - A minimum of 15 GB of additional disk space to build OpenSpace
  - 10+ GB of disk space to hold the current OpenSpace datasets. Expect that to grow as time goes on


## 1. Development Tools
To compile OpenSpace on any platform you will need a Git client, CMake, and a C++ compiler that supports at least C++23.

### Git Client
Here are some suggestions for applications that have been used by members of the development team:
  1. [Fork](https://git-fork.com) A pay-if-you-will Git client for Windows
  1. [SourceTree](http://www.sourcetreeapp.com) A free and powerful Git client usable on Windows
  1. [GitKraken](https://www.gitkraken.com) A free GUI for Windows and Linux
  1. [SmartGit](http://www.syntevo.com/smartgit/) Another GUI Git client which runs on Windows

Please ensure that, specifially on Windows, to enable automatic line-ending conversion when checking out a repository (see information [here](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)) as some of the shader files in OpenSpace are sensitive to using the native line endings.

[Learning Git](http://pcottle.github.io/learnGitBranching) is a good, interactive webpage to learn the basics of using Git.

You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub.

### CMake
[CMake](http://www.cmake.org) is a multi-platform project-generation tool. OpenSpace uses CMake so that we can more easily configure and compile OpenSpace on various platforms. We require CMake version 4.0 or above.

### Compiler / IDE
OpenSpace is written in C++23 and thus requires compiler versions that support a large portion of that standard:
  - Windows: MSVC 19.50 (Visual Studio 2026, from version 18.2)
  - Linux: GCC 15 or Clang 21

#### Windows
[Visual Studio 2026](http://www.visualstudio.com) is the standard Interactive Development Environment (IDE) for Windows. The "community" version is a free download for open-source projects. When you install it, be sure to select "Custom" configuration and select the C++ compiler -- it might not be included by default. You can also select a git client here ("Git GUI"). Installation could take a while (like an hour or so, depending on the machine).

### vcpkg
Dependencies in OpenSpace are handled via [vcpkg](https://github.com/microsoft/vcpkg). [This page](https://learn.microsoft.com/en-us/vcpkg/get_started/get-started?pivots=shell-powershell) contains detailed information how to install it for different operating systems.

**Note**: It is also advised to define VCPKG_DEFAULT_BINARY_CACHE as an environment variable and point it to a folder on disk that will be used as a vcpkg cache. This setting overrides where compiled dependencies will be cached and we recommend to place that cache next to the vcpkg install (for example, if C:/vcpkg is the vcpkg install directory, use C:/vcpkg-cache).


## 2. Dependencies
The first time the CMake configure step is being run, it will compile all of the dependencies required dependencies and automatically place them into the vcpkg binary cache.

On Linux, an additional list of system dependencies are required. This list is based on the [Docker images](https://github.com/OpenSpace/docker) used to test OpenSpace, which serve as the ground truth.

::::{tab-set}
:::{tab-item} Ubuntu
```bash
sudo apt-get install -y cmake build-essential git ninja-build curl zip unzip autoconf autoconf-archive automake libtool python3 bison flex pkg-config zip rpm dpkg perl libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev libwayland-dev wayland-protocols libx11-dev libxext-dev libxfixes-dev libxcb1-dev libxcb-glx0-dev libxcb-keysyms1-dev libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-xinput-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev libxcb-render-util0-dev libxcb-util-dev libxcb-xinerama0-dev libxcb-xkb-dev libxcb-cursor-dev libegl-dev libgl-dev libdbus-1-dev libatspi2.0-dev libxrandr-dev libxxf86vm-dev libxinerama-dev libxcursor-dev libmpv-dev libnss3 libnspr4
```
:::

:::{tab-item} Fedora
```bash
dnf install -y cmake gcc gcc-c++ git ninja-build curl zip unzip autoconf autoconf-archive automake libtool python3 bison flex pkg-config rpm-build dpkg perl-core mesa-libGL-devel mesa-libGLU-devel libglvnd-devel libxcb-devel xcb-util-devel xcb-util-image-devel xcb-util-keysyms-devel xcb-util-renderutil-devel xcb-util-wm-devel xcb-util-cursor-devel libX11-xcb libXrender-devel libXi-devel libxkbcommon-devel libxkbcommon-x11-devel mesa-libEGL-devel fontconfig-devel freetype-devel wayland-devel wayland-protocols-devel libwayland-client libwayland-cursor libwayland-egl libXxf86vm-devel libXrandr-devel libXfixes-devel libXcomposite-devel libXdamage-devel libXScrnSaver-devel libXinerama-devel libXcursor-devel libX11-devel mpv-devel
```
:::

:::{tab-item} Arch
```bash
pacman -Syu --noconfirm --needed base-devel cmake git ninja curl zip unzip tar autoconf-archive python perl rpm-tools dpkg perl mesa glu libglvnd libxcb xcb-util xcb-util-image xcb-util-keysyms xcb-util-renderutil xcb-util-wm xcb-util-cursor libxrender libxi libxkbcommon libxkbcommon-x11 fontconfig freetype2 wayland wayland-protocols libxxf86vm libxrandr libxfixes libxcomposite libxdamage libxss libxinerama libxcursor libx11 libxext xorgproto vulkan-headers mpv dbus at-spi2-core nss nspr libcups
```
:::
::::


## 3. Compiling
1. Clone the Git repository (`git clone https://github.com/OpenSpace/OpenSpace`). **Note**: Due to some dependencies, the folder in which you check out the repository must not contain any spaces
1. CMake Configure & Generate
   - Option A (commandline)
     1. `cmake --list-presets` to list all of the available presets (for example `windows-msvc` on Windows)
     1. `cmake --preset <preset>` to configure OpenSpace. If this is the first time on the machine, this will take a while, but subsequent configure steps will only take a few seconds
   - Option B (GUI)
     1. Open CMake and drag in the `CMakeLists.txt` file from the OpenSpace folder
     1. Pick one of the Presets (for example "Windows MSVC" on Windows)
     1. Select "Configure" to configure OpenSpace. If this is the first time on the machine, this will take a while, but subsequent configure steps will only take a few seconds
     1. Select "Generate"
1. Compiling
   - Option A (commandline)
     1. `cmake --build --preset <preset>`
   - Option B (GUI / IDE)
     1. Select "Open Project"
     1. Build in the respective IDE

If there are any elements of these instructions that are unclear, feel free to suggest a change against this [repository](https://github.com/OpenSpace/OpenSpace-Docs) or join us in the #compiling channel on the [OpenSpace Slack](https://openspacesupport.slack.com).


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


## FAQ
### 1
If Windows is complaining that it cannot find the `VCOMP120.dll`, download the [Visual Studio Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe). On Windows 10 and up, this is not installed by default anymore. In general, this shouldn't be an issue if you have Visual Studio installed correctly, but it will be necessary to install on other computers that do not have the IDE installed.

### 2
```text
======= CONFIGURING OPENSPACE PROJECT =======
Dependency: Spice
CMake Error at ext/CMakeLists.txt:26 (find_package):
  Could not find a package configuration file provided by "spice" with any of
  the following names:

    spice.cps
    spiceConfig.cmake
    spice-config.cmake

  Add the installation prefix of "spice" to CMAKE_PREFIX_PATH or set
  "spice_DIR" to a directory containing one of the above files.  If "spice"
  provides a separate development package or SDK, be sure it has been
  installed.
```

This means that no preset has been selected in CMake.

## Advanced Section
The information in this section is not needed when just compiling OpenSpace. It covers updating or added new dependencies, for example.

## Adding new dependency
Dependencies are provided through vcpkg in OpenSpace and are loaded through the `vcpkg.json` file in the root folder.

### Dependency exists in vcpkg repository
Check [https://vcpkg.io/en/packages?query=](https://vcpkg.io/en/packages?query=) if the package that should be added already exists in the repository. It will also list the version number of that dependency, which might not always be the newest version available. If the package is available and the version number is acceptable, it is as easy as adding it to the `"dependencies"` group in the `vcpkg.json`. We keep that list alphabetically sorted. Note that many vcpkg ports also define features that can be enabled or disabled depending on the need.

### Dependency does not exist in vcpkg repository
If a required dependency is not part of the vcpkg repository, there are two alternatives. The less common used is for very large dependencies that we don't want to recompile as often. Right now, only CEF falls into that category and it should be kept to an absolute minimum. The more common variant is to provide an *overlay port*. In OpenSpace, these are located in `support/vcpkg/ports`. Each folder defines a new dependency with its own `vcpkg.json` file to define local dependencies as well as a `portfile.cmake` that does all of the work of including the port.

The [vcpkg documentation](https://learn.microsoft.com/en-us/vcpkg/) contains information on how these port files should be written.

## Updating dependencies
Depending on whether a dependency comes from the vcpkg repository or from a local port file, the process is different how to update it.

### Dependency comes from the vcpkg repository
We update all of the dependencies from the vcpkg repository in one go. To do that, the `vcpkg-configuration.default-registry.baseline` value has to be updated to match the hash of the commit in the [https://github.com/microsoft/vcpkg](https://github.com/microsoft/vcpkg) repository that we want to use as the new baseline. From that moment, OpenSpace will then use all of the verison of the packages that are available in that baseline.

### Dependency has a local port file
Almost all local portfiles will have a command at the top to download a GitHub repository to get the source code and compile it locally:

```cmake
vcpkg_from_github(
  OUT_SOURCE_PATH SOURCE_PATH
  REPO OpenSpace/Spice
  REF 00fb7876faff7cac8cb12fa87ba5ddcad1485fbe
  SHA512 76f3d354e5589ceb901ab87241f33101ae80fc69447f21e1ff9b49400b89966ca2177f60c1455e2c6d6d19db3d987602301d3088e9d9828ee944f427203748ca
  HEAD_REF vcpkg
)
```

To update that to a new commit, change the `REF` value to the commit hash of the commit that we want to use in the repo ([https://github.com/OpenSpace/Spice](https://github.com/OpenSpace/Spice) in this example) and change the SHA512 to 0. Then run the CMake Configure step which will fail with an error:

```
error: failing download because the expected SHA512 was all zeros, please change the expected SHA512 to: 76f3d354e5589ceb901ab87241f33101ae80fc69447f21e1ff9b49400b89966ca2177f60c1455e2c6d6d19db3d987602301d3088e9d9828ee944f427203748ca
```

copy and paste the new SHA512 hash into the SHA512 and configure again to finalize the update.
