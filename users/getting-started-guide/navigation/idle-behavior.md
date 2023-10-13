# Idle Behavior
The Idle Behavior is a new feature of the OrbitalNavigator as of OpenSpace 0.18.0. It can be used to trigger an automatic camera motion in relation to a scene graph node, such as an orbiting motion around the object. 
The settings for the Idle Behavior can be found in the settings menu under `NavigationHandler -> OrbitalNavigator -> IdleBehavior`. 

An Idle Behavior can be triggered in three different ways:
1. Directly, using the "Apply Idle Behavior" property
2. After no camera interaction has been performed for a certain number of seconds, i.e. when the software is "idle". This is done by setting the "Should Trigger When Idle" property to true. There is also a property to control the time the software waits until triggering the behavior. 
3. Directly through a Lua script, using the helper function: `openspace.navigation.triggerIdleBehavior`

The default behavior is a simple orbiting motion, but it can easily be changed in the UI or passed as a parameter to the helper function. 

As of version 0.18.0, three different types of orbiting motions have been provided:

| Behavior      | Description  |
|:-------------:| ------------ |
| `Orbit` |  Simply orbit around the current anchor node, using a rightwards rotation |
| `OrbitAtConstantLatitude`  |  Orbit the anchor so that the camera is always located over a constant latitude band. In practice, this means orbiting around the Z-vector of the object's local coordinate system (which corresponds to "North" for Earth)  |
| `OrbitAroundUp`  |  Orbit around the Y-vector of the object. This often corresponds to the up-vector for models, etc. |

Which behavior to choose depends on the desired outcome and the orientation of the object within its local coordinate system[^1]. Often, the default orbit is most suitable. However, some special behavior can be achieved using the other options. For example, `OrbitAroundUp` can be used to orbit around a model on the surface of a planet in a helicopter like motion. Also, the `OrbitAtConstantLatitude` can be used to orbit a planet without changing which direction is North.

The speed of the motion can be adjusted using the "Speed Factor" property in the settings panel. Per default the idle behavior is aborted when any camera interaction happens, for example by navigating manually with the mouse or triggering a camera path. There is a setting to disable this, if desired, in which case the triggered behavior will keep on playing after the interaction has happened. 


## Footnotes

[^1]: Tip! The debugging module contains a helper function to add a rendering of the local coordinate system axes to an object. For Earth, the command would be: `openspace.debugging.addCartesianAxes("Earth");`
