# Touch Interaction
OpenSpace includes support for touch-based input using the TUIO framework (<https://www.tuio.org/>), which is a common protocol/API for multi-touch devices.

Touch-related settings are found in a few different places:
  - {menuselection}`Settings --> Interaction Handler`: For general settings related to touch input, such as whether touch input should be enabled and whether to render on-screen touch markers.
  - {menuselection}`Settings --> Navigation Handler`: For settings related to the orbital interaction using touch, such as sensitivity and settings for the [Direct Manipulation mode](#direct-manipulation).
  - {menuselection}`Modules --> Touch`: Includes settings related to TUIO support, such as which port to use (by default it uses 3333, which is the TUIO standard).

## Touch Gestures
The following gestures are supported:

| Gesture | Description |
| ------- | ----------- |
| 1 finger move | Rotate around the current focus object |
| 2 finger rotate | Rotate the camera clockwise or counter-clockwise while looking at the focus node. This is done by pressing and holding one finger, then dragging the other finger around that point, or by moving both fingers in a rotating motion around a point. |
| 2 finger pinch/expand | Zoom the camera in or out with respect to the focus node |
| 2 finger move | Pan the camera around, for example to look away from the focus node |
| 1 finger triple-tap | Refocus on the current focus node (this might be useful after panning) |

## Direct Manipulation
In addition to the regular touch control mode described above, orbital navigation in OpenSpace includes a mode called Direct Manipulation. This turns on when the camera is close to the focus node surface and you touch the object you want to manipulate. In this mode, the touched point on the surface follows the position of your finger, making movement feel directly tied to your finger on the planet. Zooming back out switches to Normal mode.

Direct manipulation works best with objects that are relatively spherical, visually. By default, it is only enabled for RenderableGlobes, but this may be changed in the navigation-related settings. It can also be disabled completely if the faster, more direct, motion that it introduces is undesired for your touch use case.
