# Folder Layout

## Source Code
The codebase is separated into source files (`*.cpp`), which are in located the `src` directory, and header files (`*.h`), which are located in the `include/openspace` directory. The internal directory structure of those two locations should always be the same. Potential inline header files (`*.inl`) should be stored in the same directory as the corresponding header file.

UnitTest files are stored in the `tests` directory, and every file that is needed to execute the tests should be stored in a directory with the same name as the test case. Files necessary to execute tests should be kept as small as possible, as it otherwise increases the clone time.

External libraries global to OpenSpace should be placed in the `ext` directory and, if possible, be compiled on the fly, rather than providing pre-compiled binaries for each possible OS.

## Settings
`openspace.cfg` is the main configuration file, which controls the configuration of base paths, which scene-file to load, and which SGCT configuration file to use. The configuration file has one path `${BASE}` predefined which always points to the directory in which the `openspace.cfg` was found. The OpenSpaceEngine will automatically start to search from the location of the binary and append `{{{..}}}` to the path until the file was found (success) or the root was reached (failure).

## Scene Description
The scene that should be loaded is determined by the value of the `Asset` key in the `openspace.cfg` file. It points to a master scene description file, which enumerates all the modules that should be loaded when this scene is used. See [Scene Files]({{ site.url }}/docs/users/scene-files) for more details on this file.
