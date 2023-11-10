# Deploying Windows

You've got your Visual Studio build running smoothly on your development machine. There's a simple way to deploy OpenSpace to another machine without installing lots of libraries and building it again - you can merely copy the necessary files to a new location.

## Deploy OpenSpace
1. The new machine will still require Visual C++ run-time libraries ("redistributables"). If the target machine is similar to the original development machine then it may already have the same version installed. (To check, go to Control Panel -> Programs -> Programs and Features).
If the correct version of the "redistributables" is not installed, you can download the correct libraries from [Microsoft](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
1. The new machine will also require the Qt6 libraries (or a subset of them).
1. Run the Launcher and 'sync' on your development machine (we recommend this because localizing the Launcher with Qt is more complicated).
1. After you've synced, create a new `openspace` folder. Copy your `openspace.cfg` as well as the `bin`, `config`, `data`, `modules`, `scripts`, and `shaders` directories to it.
1. Drop this directory on your new machine and run `openspace\bin\openspace\<Debug, Release>\OpenSpace.exe`
