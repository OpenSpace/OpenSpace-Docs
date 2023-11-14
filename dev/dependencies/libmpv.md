# LibMPV
1. `git clone` the media-autobuild-suite https://github.com/m-ab-s/media-autobuild_suite
1. Run the bat script `media-autobuild_suite.bat`
1. Press `2` to say no to all of the packages, except for ffmpeg. When ffmpeg comes around choose option `4) shared`
1. Let it finish building. It will take a good while.
1. Locate the file `mpv-2.dll`. It should be located in `local64/bin-video`
1. Locate the file  `mpv.def`.  It should be in `C:/a/media-autobuild_suite/build/mpv-git/libmpv` or in `C:/a/media-autobuild_suite/build/mpv-git/build`.
1. Locate the folder  `include/mpv` with the header files for mpv. It should be in `local64`
1. Create a new directory called `libmpv`. In `libmpv`, create another directory called `lib`. Copy the `dll` and the `def` there. 
1. In `libmpv`, create a new directory called `include`. Copy the header files there.

1. Edit the `mpv.def` file. Add these two lines to the top of the file:

    ```
    LIBRARY MPV-2
    EXPORTS
    ```

1. Open a command line window in the `lib` folder.
1. Run `CALL "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64` in the command line. If your `vcvarsall.bat` script is located somewhere else, change the file path.
1. Run `lib /def:mpv.def /name:mpv-2.dll /out:mpv.lib /MACHINE:X64`
1. Now you have created `mpv.lib`! Use the lib file, the include folder and the dll file to link with OpenSpace.
1. Libmpv is dependent on another dll called `libopenh264`. To use libmpv with OpenSpace, locate the file `libopenh264.dll` and put it in the bin folder.
