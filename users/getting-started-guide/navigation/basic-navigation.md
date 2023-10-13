# Basic Navigation
## Mouse and Keyboard
The keyboard and mouse interaction works the same way for all focus nodes but can need a more detailed description when it comes to browsing globes since more in-depth navigation is required for browsing across the surface of globes.

### Orbit / Horizontal Movement
Orbiting an object is done by **clicking the left mouse button and dragging**.  This can be done at any distance and will result in a horizontal motion across the surface when the camera is close to the surface.  The angular speed at which the camera is able to orbit around the globe is proportional to the distance to the surface up to a certain distance at which the angular speed will remain constant.  This distance is the same as the distance from the center of the globe to the surface.

### Horizontal Rotation
Rotating the camera along the reference ellipsoid normal is done using **scroll wheel clicking and dragging** or using **Shift while clicking the left mouse button and dragging** along the x-axis of the screen.

### Camera Roll
Rolling the camera around its local z-axis is done by holding **Ctrl while scroll wheel clicking and dragging** or holding **Ctrl + Shift while clicking the left mouse button and dragging**.  This is useful when for example correcting a tilted horizon.

### Free Camera Rotation
Look around freely by holding **Ctrl while clicking the left mouse button and dragging**.  This is useful in free flight to focus in any direction.

### Vertical Motion
The camera can be translated vertically (towards or away from the focus node) by **holding the right mouse button and dragging** along the y-axis of the screen.

## Script Functions
`openspace.globebrowsing.goToGeo()` can be used to go to a geographic location defined by a **latitude**, a **longitude **and alternatively an **altitude**.

`openspace.globebrowsing.goToChunk()` can be used to go to a specific chunk of the globe defined by an **x-coordinate**, a **y-coordinate**, and a **level**

`openspace.navigation.resetCameraDirection()` can be used to set the direction to point at the focus node.

## Properties
When the camera is far from the globe, it will not rotate with it.  When it is close, it will follow along the rotation. The cutting point is set by the property `NavigationHandler.OrbitalNavigator.FollowFocusNodeRotationDifference` which sets the distance in number of radii from the center of the globe.

## Temporal Navigation
To see the effect of temporal datasets, navigation through time is necessary.  The global time step can be changed using the slider of the property for delta time.  Functions to set time are `openspace.time.setTime()` and `openspace.time.setDeltaTime()`, see script documentation for more info. By default, the keybindings for managing time are **space bar** for playing and pausing and the **numerical keys 1-0** along with **Ctrl and Shift** modifiers to set delta time.
