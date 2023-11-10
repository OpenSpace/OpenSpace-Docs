# Touch Interface
The touch module provides support for a touch-screen interface that uses the TUIO framework (https://www.tuio.org/), which is a common protocol/API for multitouch devices.

## INSTALL
Three main things are needed:
1. **OpenSpace with built-in touch support:**  The build and/or installation of OpenSpace is covered [here](https://github.com/OpenSpace/OpenSpace/wiki/Compiling). The one important detail to add for touch is to enable `OPENSPACE_MODULE_TOUCH` in CMake. It will be necessary to build OpenSpace from source with this module enabled, rather than using a pre-built binary (which as of this writing most likely does not have the touch module built-in).
2. **TUIO Server:**  This is an executable separate from OpenSpace. It was built by Jonathan Bosson (the original developer for the touch interface). A few modifications were made to the "stock" build in order to get it to "hook" with the OpenSpace process. Unfortunately, the source code for this build was not kept, but was based on [this repository](https://github.com/vialab/Touch2Tuio/tree/master/TouchHook). Currently, the TUIO Server binary files work fine for our purposes and reside on the touch table (C:/OpenSpaceTouch/tuioServer). Gene Payne also has a copy.
3. **Script to run both software components together:**  The developer stated that:
> The touchServer finds the process ID by string name (OpenSpace), so to get it to work you'll have to run it after OpenSpace has started. Finding the process ID can by iffy sometimes (either take time or fail), the most fool-proof way to do it is to launch touchServer.exe directly after OpenSpace.exe (while OpenSpace is loading). You'll know it's working when the console window of the touchServer.exe steals OpenSpace's console window. There should also be console outputs that describe the status.

On windows, a batch file runs both OpenSpace and the touch server at the same time, in order to get the startup timing right. Here is the currently used batch file used in the Windows version:
```
     START C:\path\to\OpenSpace.exe
     ping -n 5 127.0.0.1 >nul
     START C:\path\to\tuioServer\touchServer_x64.exe
     @echo off
     echo set WshShell = CreateObject("WScript.Shell") > Activate.vbs
     echo WshShell.AppActivate("OpenSpace") >> Activate.vbs
     wscript Activate.vbs
     del Activate.vbs
```

## USAGE
### Gesture Legend

| Gesture | Description |
|---------|-------------|
|1 finger move | move the camera up/down or left/right along the 2D surface of an orbital shell around the focus node|
|2 finger rotate | rotate the camera clockwise or counter-clockwise while looking at focus node. This is done by pressing and holding one finger, then dragging the other finger around that point|
|2 finger pinch/expand | zooms the camera in or out with respect to the focus node|
|3 finger move | pan the camera around, away from the focus node (disabled by default; needs to be enabled in F3 menu in order to use)|
|1 finger double-tap (tap same spot twice within 0.5 seconds) |<ul><li>If tap is located on an object, it will be set as the camera's new focus node</li><li>If tap is in empty space, the camera will do a quick zoom-in action</li><li>If tap is in the lower-right corner of the screen, the camera will do a quick zoom-out action</li></ul>|

There are two main modes of touch interface control: Normal and Direct-Touch. Normal mode operates as described above, but Direct-Touch mode activates when the camera is brought close to the surface of the focus node object. In this mode, the gesture control is similar, but the movement or rotation of the planet is directly proportional to the actual movement of the finger, as if there was a direct connection between the fingertip and planet's surface. Double-tap does not work in direct-touch mode. Zooming out away from the planet will cause a switch back to normal touch mode.

### Menu Control
It is necessary to press F3 on the keyboard to bring up the on-screen menu (as well as hide). There is also an additional menu component that toggles with F2. Once visible, the touch interface can be used to manipulate the menu controls.

## BASIC DESCRIPTION OF SOURCE CODE
Upon initialization, the touch module registers its callback functions with the OpenSpaceEngine component:
  * `InitializeGL` - initialization for on-screen markers that display with each touch
  * `DeinitializeGL` - de-initialization of the on-screen markers
  * `PreSync` - called at every frame by the openspaceengine component. This callback (in touchmodule.cpp) will process any new touch events received from the TUIO server.
  * `Render` - called along with other OpenSpace render components to render the on-screen touch markers

The instance of the `TouchModule` class contains instances of these classes:
### TuioEar
This is a listener on port 3333 for UDP packets from the TUIO Server, which runs as a separate process. The `getInput` method of this class is called to get any new touch events/coordinates that may have been received since the previous frame.
### TouchMarker
This class renders a visible marker (currently a transparent red circle) with each finger touch. The properties (color, size, transparency) can be modified.
### TouchInteraction
This class interprets the touch events as gestures and determines the resulting interaction in OpenSpace.
With each `PreSync` call, the following calls to `TouchInteraction` are made:
  * `setCamera` (just set the pointer to OpenSpaceEngine's navigation handler camera)
  * `setFocusNode` (just set pointer to OpenSpaceEngine's navigation handler focus node)
  * `updateStateFromInput` (if new touch events have occurred)
  * `resetAfterInput` (if all touch events have been handled, touch properties are reset for the next gesture)
  * `step` (handles gesture and camera behavior based on the time step elapsed since the previous frame)

The `updateStateFromInput` function determines the X,Y position of each touch, and determines if a tap or double-tap has occurred.

`interpretInteraction` is called to determine what gesture the touch event(s) represents. The output of this function can be: *PICK* (tap), *ROT*ate, *ZOOM_OUT*, *ROLL*, or *PINCH* (zoom in/out gesture).

Next, `computeVelocities` is called with the list of touch events. Based on the gesture type & speed from above, a camera velocity is calculated (but not yet applied to the camera). A velocity decay rate is also calculated here for the purpose of determining a smooth decay to zero after the touch gesture is over. This decay time is a property that can be changed.

In the `step` function, the time elapsed since the previous rendering frame is used to update the camera position based on the velocities updated in `computeVelocities`. The components of movement in the roll, pan, orbit, and zoom directions are computed individually. At the end of the function, the camera position is updated with the sum of all velocities.

For gestures in Direct Touch mode, the `directControl` function is used to determine the planet movement in order to match the gestures (to achieve the effect of the planet surface movement directly matching the finger movement).

For double-tap events, the `findSelectedMode` function is used to cast a ray out from the location of the tap to see if it intersects with any objects in an approved list (e.g. planets, moons, Sun). If a match is found, then the focus node is set to the matching SceneGraphNode object.

Finally, the `decelerate` function is called to apply the velocity decay coefficients to the orbit, roll, pan, and zoom velocities.
