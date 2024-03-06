# Folder Layout
This page describes the layout of the source code inside the OpenSpace repository.


## Source Code
The codebase is separated into source files (`*.cpp`), which are in located the `src` directory, and header files (`*.h`), which are located in the `include/openspace` directory. The internal directory structure of those two locations should always be the same. Potential inline header files (`*.inl`) should be stored in the same directory as the corresponding header file.

The `modules` folder contains modularized code that comprise the actual functionality of the engine. Each module, in principle, should be able to be toggled off and should be self-contained or explicity reference its dependencies.

The `apps` folder contains the application code that uses OpenSpace as a library. In particular, `apps/OpenSpace` contains the application that most people interact which, when using OpenSpace.

UnitTest files are stored in the `tests` directory, and every file that is needed to execute the tests should be stored in a directory with the same name as the test case. Files necessary to execute tests should be kept as small as possible, as it otherwise increases the clone time.

External libraries are placed in a `ext` directory at the respective level and, if possible, be compiled on the fly, rather than providing pre-compiled binaries for each possible operating system. For global OpenSpace dependencies, the root `ext` contains these libraries, in particularly `Ghoul`, which has its own dependencies. Two other examples are `apps` which have their own dependencies, and `modules` that can each have their own, internal, dependencies.


## Settings
`openspace.cfg` is the main configuration file, which controls the configuration of base paths, which profile to load, and which SGCT configuration file to use. The configuration file has one path `${BASE}` predefined which always points to the directory in which the `openspace.cfg` was found. The OpenSpace engine will automatically start to search from the location of the binary and append `..` to the path until the file was found (success) or the root was reached (failure).
