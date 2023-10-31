# PathNavigation - Simplifying navigation in OpenSpace
As of version 0.18.0, OpenSpace includes a system that simplifies navigation by automatically steering the camera to a desired target. Note that the system is *experimental* and will be subject to change in the future, but it is still useful to reduce the amount of manual navigation needed to control OpenSpace.

The system is based on a thesis work by Ingela Rossing and Emma Broman, done in 2020.

## Flying to a target
The navigation menu in OpenSpace now includes the possibility to fly to a target, by clicking the airplane button that appears when hovering over an item in the list. The camera will move in a smooth motion to a position where the selected target is focused in view. If the Sun is included in the scene, the system will try to find a sunlit position on the object. It will also try to reduce the risk of collisions with other objects in the scene.

In addition to the fly-to button, the current focus node also has "refocus" button. This triggers a linear motion and rotation to center the object in view.

![Refocus icon](/assets/camera-paths/refocus_icon.png) - Refocus (linear motion to center the target in view)

![Refocus icon](/assets/camera-paths/flyto_icon.png) - Fly-to (fly using current default path type, see below)

When a path is playing, the Focus menu button changes to a button that can be used to cancel the path. The button also indicates which the current anchor node is. This will be the focus if a path is aborted.

## Path types
The shape of the resulting path depends on the currently selected *path type*. The default type, called `AvoidCollision`, avoids collisions with objects in the scene and tries to rotate the camera as little as possible to avoid creating disorienting rotations. It works well when flying between two targets, like planets, where both of the objects are centered in view. However, since it does not rotate the camera more than necessary it does not work very well when the object we're departing from is not centered in view; for example, from a position on a surface where we are looking a the horizon. In these cases, the `ZoomOutOverview` path type might give a better result. That path type tries to keep targetted nodes in view when leaving/approaching the node. As a consequece it gives a better understanding of the spatial relation, but might introduce fast rotations if not used with care

See Settings section for more details on path types and how to change the default choice.

### Linear paths

For the "refocus" button, a linear path is used. The camera will then fly in a straight line to the targeted object. This is also the case for any situation that the camera path system might find "troublesome", for example when the path is very long or when the camera starts from a position inside the bounding sphere of the target object.


## Settings
The `PathNavigator` settings are found under `NavigationHandler` in the settings menu and include some other properties to control how a path is being played/created. Some properties that are good to know about are:

| Property      | Description |
| ----------- | ----------- |
| DefaultPathType | The type of path that is going to be created when generating a path (see next table)|
| SpeedScale   | Can be used to increase or decrease the traversal speed |
| ArrivalDistanceFactor   | Decides how far away from a target object the camera should stop. The factor will be multiplied with the bounding sphere of the node and the resulting distance is used to compute the target position when a path is created. |
| ApplyIdleBehaviorOnFinish   | If checked, the currently chosen [Idle Behavior](idle-behavior) is triggered when the path is finished. Can be used to automatically start a rotation around the target when arriving. |
| RelevantNodeTags   | A list of tags of nodes that is relevant for the path generation. Used for example when computing collisions. |
| IncludeRoll   | If false, any rolling rotation is removed from the rotation interpolation. Useful in situations where rolling motions can be uncomfortable for the user. OBS! Disabled per default, and we do not recommend turning it on for any paths apart from the `AvoidCollision` and `Linear`, since it might cause uncomfortable rotations. |

Short description of the different available path types (as of version 0.18.0):

| Path type      | Description |
| ----------- | ----------- |
| AvoidCollision (default) | Does some simple collision avoidance with close scene graph nodes, but otherwise goes reasonably straightly to the target. Linear interpolation (SLERP) of the rotation. That is, does not try to look at the targeted objects. Works well when flying between objects in the scene, as long as the objects are centered in view at the start and end. |
| ZoomOutOverview   | First moves the camera out to a point where both targets are in view, before approaching the desired targets. Provides a better sense of how far away the objects are in relation to each other. Tries to look at either of the targets for as long as possible. However, no collision detection is done. |
| Linear   | Just a linear path from the start to end point |
| AvoidCollisionWithLookAt | *Temporary* type that is useful when moving to objects on the same surface, but sometimes leads to fast undesired rotations when traveling between objects. Avoids collision, and looks at the targets as much as possible. |

For now, the desired path type must be chosen using the `PathNavigator.DefaultPathType` property. Down the line, the system should be able to determine what type to use based on the current situation. Please note that the path types will likely change in future releases of the software.

## Caveats

* If the distance traveled is very far (such as outside of the solar system), or if the camera starts within the bounding sphere on an object, a linear path will often be used instead of the default type. An info message is shown in the log when this happens.

* The simulation time will be paused when a path is started, and unpaused again when it is finished. This can lead to some weird/unexpected behavior for larger simulation speeds and we recommend to pause the time before starting the path (or at least using a slow simulation speed).

* The system assumes that all objects that we fly to have a valid bounding sphere. If a target does not, it can lead to some weird behavior.

## Creating paths through Lua Scripting
The Lua API now also includes functions to create camera paths to specific positions, and to provide more details when flying to a target.

More info on this is coming to another wiki page, soon! (Emma Broman, 2022-04-13)
