# Dependencies
The vast majority of dependencies in OpenSpace are handled though [vcpkg](https://vcpkg.io/en/). These pages describe how to add new and update existing dependencies.

## Adding a new dependency

### Dependency exists in vcpkg repository
Check [https://vcpkg.io/en/packages?query=](https://vcpkg.io/en/packages?query=) if the package that should be added already exists in the repository. It will also list the version number of that dependency, which might not always be the newest version available. If the package is available and the version number is acceptable, it is as easy as adding it to the `"dependencies"` group in the `vcpkg.json`. We keep that list alphabetically sorted. Note that many vcpkg ports also define features that can be enabled or disabled depending on the need.

### Dependency does not exist in vcpkg repository
If a required dependency is not part of the vcpkg repository, there are two alternatives. The more common variant is to provide an *overlay port*. In OpenSpace, these are located in `support/vcpkg/ports`. Each folder defines a new dependency with its own `vcpkg.json` file to define local dependencies as well as a `portfile.cmake` that does all of the work of including the port. The [vcpkg documentation](https://learn.microsoft.com/en-us/vcpkg/) contains information on how these port files should be written.

The less commonly used option is for very large dependencies that we don't want to recompile as often. Right now, only [CEF](cef) and [libMPV]([libmpv) fall into that category and it should stay the exception to include libraries directly. For CEF and libMPV the reason is that these are dependencies that each take hours to compile from scratch and involve many dependencies on their own.

### Updating dependencies
Depending on whether a dependency comes from the vcpkg repository or from a local port file, the process for updating it differs.

### Dependency comes from the vcpkg repository
We update all of the dependencies from the vcpkg repository in one go. To do this, we change the `baseline` value in `vcpkg.json` (under `vcpkg-configuration.default-registry`). This value is the hash of a specific commit in the [vcpkg repository](https://github.com/microsoft/vcpkg). Once we point it at a newer commit, OpenSpace uses the package versions from that commit. This keeps all dependencies in sync with each other.


### Dependency has a local port file
Almost all local port files will have a command at the top to download a GitHub repository to get the source code and compile it locally:

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

Then, copy and paste the new SHA512 hash into the SHA512 and configure again to finalize the update.


:::{toctree}
:maxdepth: 1
:caption: Compiling

cef
libmpv
:::
