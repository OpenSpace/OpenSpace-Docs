# Automatic Flight Paths
OpenSpace includes a system that automatically steers the camera to a target object or position. It reduces the amount of manual navigation needed when moving between objects in the scene.

The system is based on a thesis work by Ingela Rossing and Emma Broman, done in 2020, and has continued to evolve in later OpenSpace releases.


## Flying to a Target
The Navigation menu includes a fly-to action for targets in the list. Click one of the icons listed below to start an automatic camera path to that target. The same options are also avialble in the context menu for focusable nodes in the Scene menu.

| Icon | Name | Description |
| ---- | ------ | ----------- |
| ![Fly-to icon](flyto_icon.png) | Fly-to | Fly to the target using the current default *path type*, see [below](#about-path-types) |
| ![Refocus icon](refocus_icon.png) | Zoom-to / Frame | Linear motion to center the target in view |

The path system determines the route based on the current situation and the selected path type (see below). By default, it tries to:

  - Move the camera smoothly to a useful viewing position, approaching the target from a reasonable direction
  - Avoid collisions with scene objects when relevant
  - Prefer a sunlit position if the Sun is part of the scene

## Aborting a Path

:::{image} cancel-flight-button.png
:alt: Cancel button in the toolbar menu
:align: right
:::

A camera path can be aborted at any time by clicking the cancel button in the toolbar menu, which appears when a path is playing. This button also shows the current anchor node, which becomes the focus if a path if the path is aborted.

## Caveats
The path system has some limitations that are good to be aware of:
  - Simulation time is paused when a path starts and resumed when it finishes. For best results, pause time manually or use a slow simulation speed before starting a path.
  - If the distance traveled is very far, or if the camera starts inside the target's bounding sphere, a linear path is often used instead of the default type. An info message is shown in the log when this happens.
  - The system assumes that all fly-to targets have a valid bounding sphere. Missing bounding sphere data can lead to unexpected behavior.

(camera-paths-settings)=
## Settings
The settings for the gerenated camera paths can be found in the settings menu under {menuselection}`Navigation handler --> Path Navigator`. Some useful settings are:

| Property | Description |
| -------- | ----------- |
| {menuselection}`Default path type` | The path type that is used when generating a new fly-to path. |
| {menuselection}`Speed scale` | Can be used to increase or decrease the traversal speed. |
| {menuselection}`Arrival distance factor` | Determines how far from the target the camera should stop. The factor is multiplied by the target's bounding sphere to compute the final arrival distance. |
| {menuselection}`Apply idle motion on finish` | If enabled, the selected [Idle Motion](idle-motion) starts when the path finishes. This can be used to begin a rotation around the target automatically. |
| {menuselection}`Relevant node tags` | Tags used to identify nodes that are relevant for path generation and collision handling. Try changing this if the camera is colliding with objects in your scene. |
| {menuselection}`Include roll` | If false, any roll is removed from the rotation interpolation. This is disabled by default as it might introduce fast rotations that are unconfortable for a viewer. You might however want to enable this if you need the camera to have a specific orientation at the end of the path, such as when flying to a navigation state. |

### About Path Types
The resulting path depends on the selected *path type*. The default type, `AvoidCollision`, avoids nearby objects and rotates the camera as little as possible. It works well when moving between targets that are already centered in view.

If the starting view is not centered on the object being left, `ZoomOutOverview` can be a better choice. It tries to keep the relevant target in view for as long as possible and gives a better sense of the spatial relation between objects, but it may introduce stronger rotations.

Here is a short description of the different available path type options:

| Path type | Description |
| --------- | ----------- |
| `AvoidCollision` (default) | Avoids nearby scene graph nodes and follows a mostly direct path to the target. Uses spherical interpolation of rotation and does not actively keep the target centered. Works well when both the start and end views are already reasonable. |
| `ZoomOutOverview` | Moves the camera out to a point where the relevant targets are visible, then approaches the destination. Gives a better overview of the spatial relation between objects. No collision detection is performed. |
| `Linear` | A straight-line path from the start point to the end point. |
| `AvoidCollisionWithLookAt` | A temporary type that avoids collisions while trying to keep the target in view as much as possible. It can produce fast rotations in some situations. |

For now, the desired path type must be chosen using the {menuselection}`Path Navigator -> Default path type` setting. In the future, the system may choose the path type automatically based on the current situation. The available path types may still change in later releases.

:::{note}
The linear path type is also used as a fallback when the system cannot find a suitable path using the other types. This can happen if the path is very long or if the camera starts inside the target's bounding sphere. In these cases, a linear path is used to ensure that the camera reaches the target without issues related to risks of numerical instability or other issues.
:::

## Scripting
The path system can also be controlled using the scripting API, which also allows for more complex and customized camera movements such as flying to specific positions. The available functions are described in the [Camera Paths Using Scripting](camera-paths-scripting) page.

:::{toctree}
:maxdepth: 1
:hidden:

camera-paths-scripting
:::
