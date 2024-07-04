# Dual monitors with fullscreen display
Here is a way of displaying the gui on a primary screen and the OpenSpace render on a secondary screen, for example a dome projector, in full screen. 
It's very important to have the render running in full screen to get rid of the title bar on the dome projector.

First check the virtual monitor layout of your screen in Windows to see how the monitors are aligned relative to each other. Windows has a virtual coordinate system whose origin (0,0) 
is at the top left corner of the "main display". You'll need those to position the windows correctly. For the rest of this I'm assuming you have the monitor that should get the GUI as the main monitor, 
that both screens are `1920x1080`, and that the projector "monitor" is to the right of the main monitor.

In the **single_fisheye_gui.json**
  a. Add `"border": false`, somewhere between line 10 and 17. That will cause the title bar to disappear
  b. In line 15 change `"pos": { "x": 50, "y": 50 },` to `"pos": { "x": 0, "y": 0 },` to have the window start in the top left corner of the main screen
  c. In line 16 change `"size": { "x": 1024, "y": 1024 },` to `"size": { "x": 1920, "y": 1080 },` to make the GUI window full screen
  d. Add `"border": false,` somewhere between line 34 and 36 to make the rendering window also not have a title screen
  e. Add `"pos": { "x": 1920, "y": 0 },` somewhere between line 34 and 36 to make the rendering window start at the top left corner of the second monitor
  f. Change line 37 from `"size": { "x": 1024, "y": 1024 },` to `"size": { "x": 1920, "y": 1080 },` to make it go full screen

## Notes
1. The `border=false` solution is preferable to  `fullscreen=true` as it represents a "non-exclusive" fullscreen, which means you won't get any flickering when you click between applications.
2. In case the two monitors have different resolutions, please put the larger monitor on the "left" (as the main display) and the smaller one on the "right" - doing otherwise would cause some rendering issues.
