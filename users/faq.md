# FAQ
## Related to usage in Planetariums
1. How do I get a fulldome (fisheye) output from OpenSpace?
When you first start up OpenSpace, you get a screen where you can choose a Profile and choose Window Options. Window Options is where you can choose to use a fisheye configuration. 

2. How can I save screenshots in a resolution higher than my screen resolution? For example, my computer screen can only display 1920x1080, but I want to capture 4096x4096 pngs using the session recording function.
You can choose to display a different resolution, and render at a different resolution. The single.json Window options configuration file is an example which has a display resolution of 1280x720 (the "size" parameter) but renders pngs at 2560x1440 (the "res" parameter). These configuration files are located in the 'config' directory - you can write your own for your desired resolution.

3. How can I get rid of the text and GUI elements in my planetarium display?

There are several ways to do this. For example, you could
  1. press {kbd}`TAB` and {kbd}`SHIFT+TAB` to toggle visibility of the GUI and text elements respectively
  1. create or use a _Window Options_ configuration file which renders the GUI and the data visualization separately on different windows, for example the `single_fisheye_gui.json` configuration file
  1. create a [HTML control page](/how-to/html-controls-setup) and use that to control the navigation, hiding the GUI

4. How do I ensure that all the data sets I need are loaded before playing back a recorded path? Can I play back without an internet connection?
Go into the openspace.cfg file and set ModuleConfigurations->GlobeBrowsing->MRFCacheEnabled to true. Run OpenSpace again it will cache the globebrowsing data for planet/moon locations you visit. Then later, it should use the cached data for those same locations. There is also an Offline profile that you can select from the launcher, and see if that has the content you want.

## Related to running OpenSpace on MacOS, Linux and unsupported hardware 
1. Why do you only provide Intel Mac packages? Why not packages for Apple Silicon Macs?

OpenSpace uses the OpenGL cross-platform library. Unfortunately, Apple does not yet support the latest versions of OpenGL on M1/M2/M3 Macs. Asahi Linux has successfully ported OpenGL to Apple Silicon Macs, so those with Apple Silicon Macs could, if they're feeling adventurous, [install Asahi Fedora remix](https://asahilinux.org/fedora/) and run OpenSpace on their Apple Silicon Macs.

2. Does OpenSpace run on Linux?

Yes. Linux users can compile and run OpenSpace using the MIT licensed code at https://github.com/OpenSpace/OpenSpace 

3. I don't have an NVidia graphics card. Can I still run the Windows executable on my Windows laptop which has integrated Intel graphics?

Yes. The executable will run, but since it uses software emulation for running OpenGL, the frame rate would be very low. Ranging from below 1 frame per second to 5 frames per second if you make the display window smaller. 
