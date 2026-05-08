# Idle Motion
Idle Motion is a feature of the OrbitalNavigator that can be used to trigger automatic camera motion in relation to a scene graph node, such as orbiting around an object.
The settings for Idle Motion can be found in the settings menu under {menuselection}`Settings --> Navigation Handler --> Orbital Navigator --> Idle Motion`.

An Idle Motion can be triggered in a few different ways:

1. Using the button in the top bar, next to the friction controls
1. By enabling the "Apply idle motion" property in the settings
1. After no camera interaction has been performed for a certain number of seconds, i.e., when the software is "idle". This is done by enabling the "Should trigger when idle" property. There is also a property to control how long the software waits before triggering the motion.
1. Through a Lua script, using the helper function `openspace.navigation.triggerIdleMotion`

The default motion is a simple orbiting motion around the focus object, but it can easily be changed in the UI or passed as a parameter to the helper function. As of version 0.18.0, three different types of orbiting motion are available:

| Motion | Description |
| -------- | ----------- |
| `Orbit` | Orbit around the current anchor node, using a rightward rotation |
| `OrbitAtConstantLatitude` | Orbit the anchor so that the camera is always located over a constant latitude band. In practice, this means orbiting around the Z-vector of the object's local coordinate system (which corresponds to "North" for Earth) |
| `OrbitAroundUpVector` | Orbit around the Y-vector of the object. This often corresponds to the up-vector for models, etc. |

Which motion to choose depends on the desired outcome and the orientation of the object within its local coordinate system[^1]. Often, the default orbit is most suitable. However, special motion can be achieved using the other options. For example, `OrbitAroundUpVector` can be used to orbit around a model on the surface of a planet in a helicopter-like motion. Also, `OrbitAtConstantLatitude` can be used to orbit a planet without changing which direction is North.

The speed of the motion can be adjusted using the "Speed Factor" property in the settings panel. By default, idle motion is aborted when any camera interaction happens, for example by navigating manually with the mouse or triggering a camera path. There is a setting to disable this, if desired, in which case the triggered motion will keep running after the interaction has happened.


[^1]: Tip: The debugging module contains a helper function to render the local coordinate system axes for an object. For Earth, the command is `openspace.debugging.addCartesianAxes("Earth");`.
