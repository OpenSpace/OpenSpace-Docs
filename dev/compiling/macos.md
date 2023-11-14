# MacOS
This page contains specific information necessary to compile OpenSpace on macOS. This page has the [general instructions](index) as a required reading.


## Development Tools
### Xcode
Xcode is the Interactive Development Environment (IDE) tool for Mac. It's how you compile code on a Mac. It's a free install from the Mac App Store.

### Git Client
Xcode includes git, but the Xcode IDE cannot deal with recursive submodules. Once Xcode is installed, you can also use git via the command line in the Terminal app.


## Dependencies
Homebrew is billed as "the missing package manager" for macOS. Homewbrew installs the stuff you need that Apple didn't. It's easy to install and uninstall packages with Homebrew. See [http://brew.sh](http://brew.sh) for instructions and to download and install Homebrew.

Once you have installed homebrew you can use it to install other useful utilities and libraries. Specifically, to build OpenSpace you will need to do the following:
```bash
  brew install glew boost freeimage mpv vulkan-headers vulkan-loader brotli gdal
```

Similarly if you are using MacPorts, the corresponding command is:
```bash
  port install glew boost freeimage mpv vulkan-headers vulkan-loader brotli gdal +curl
```

Please make use that the correct GDAL version is installed, as OpenSpace uses some recent features. We require a version that is newer than `2.4`.

## Compiling
In Xcode, you need to select the target/scheme `ALL_BUILD` (if it isn't already) and build it (pull down {menuselection}`Product --> Build`). Verify the build type (`Release` | `Debug`) by browsing to {menuselection}`Product --> Scheme --> Edit Scheme --> Info tab --> Build Configuration`.

Run `open -n OpenSpace.app <args>` from `OpenSpace/bin/openspace/Release/` to start OpenSpace
