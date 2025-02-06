---
authors:
  - name: OpenSpace Team
---

# General Telemetry Types
The general telemetry types in the [Telemetry Module](index.md) monitor the general state of OpenSpace and send that information to the OSC receiver. There are several types that monitor different aspects of the software. Each type is explained in more detail in the sections below.

In summary, the general telemetry types available in OpenSpace are:
  - [Camera Information](#camera-information)
  - [Focus](#focus)
  - [Time Information](#time-information)
  - [Customized Nodes Information](#customized-nodes-information)
  - [Angle Calculation Mode](#angle-calculation-mode)

## Camera Information
This telemetry type monitors the camera state and sends that information to the OSC receiver. The OSC messages from this telemetry type go under the OSC label `/Camera` and contain nine items in addition to the label:

  1. The {math}`x` position of the camera in the world.
  1. The {math}`y` position of the camera in the world.
  1. The {math}`z` position of the camera in the world.
  1. The {math}`w` component of the quaternion rotation of the camera.
  1. The {math}`x` component of the quaternion rotation of the camera.
  1. The {math}`y` component of the quaternion rotation of the camera.
  1. The {math}`z` component of the quaternion rotation of the camera.
  1. The movement speed of the camera, in the unit per second specified by the next item.
  1. The distance unit for the movement speed of the camera, as a string in singular form with the first letter capitalized. For example, `Kilometer`.

Note that the first seven items describe the position and orientation of the camera. The first three items specify the {math}`x`, {math}`y`, and {math}`z` positions of the camera in the world, in relation to the Solar System barycenter. The next four items are the quaternion rotation of the camera in the order of {math}`w`, {math}`x`, {math}`y`, and {math}`z`.

A message from this telemetry type can for example look like this:
:::{code-block}
[ /Camera, -144982761635.78, -4673195479.6344, -19947642284.929, -0.016136366108094, 0.046858848656595, -0.62388829681315, -0.77994054843366, 34.074930097613, Kilometer ]
:::

In the example above, the position of the camera relative to the Solar System Barycenter is {math}`(-144982761635.78, -4673195479.6344, -19947642284.929)`. The camera quaternion rotation is `(0.016136366108094, 0.046858848656595, -0.62388829681315, -0.77994054843366)` in the format {math}`(w, x, y, z)`. Lastly, the camera moves with a speed of {math}`34.074930097613` kilometers per second.

## Focus
This telemetry type sends out a message every time the focus is changed in OpenSpace. The OSC messages from this telemetry type go under the OSC label `/Focus` and contain only one item:

  1. The identifier of the new focus in OpenSpace, as a string.

A message from this telemetry type can for example look like this:
:::{code-block}
[ /Focus, Earth ]
:::

In the example above, the current focus in OpenSpace was set to Earth.

## Time Information
This telemetry type monitors the time in OpenSpace and sends that information to the OSC receiver. The OSC messages from this telemetry type go under the OSC label `/Time` and contain three items:

  1. The speed of the simulation time, specified in the selected time unit in the simulation, per real-life second. For example, 10 simulated seconds per real-life second means that the simulation goes 10 times faster than real life.
  1. The selected time unit for the speed of simulation time, as a string in singular form with the first letter capitalized. For example, `Day`.
  1. The current simulation time in OpenSpace specified in J2000 seconds, that is, the number of seconds past the J2000 epoch (i.e. January 1, 2000 12:00:00 TT).

A message from this telemetry type can for example look like this:
:::{code-block}
[ /Time, 30.0, Minute, 787312539.37412 ]
:::

In the example above, the simulation time in OpenSpace progresses {math}`30.0` minutes per real-life second, and the current time is {math}`787312539.37412` seconds past the J2000 epoch.

## Angle Calculation Mode
For some telemetry types, such as the [Customized Nodes Information](#customized-nodes-information) and the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification), part of the information that is sent are two angles that describe where the object is placed on the screen, a _horizontal_ angle and an optional _elevation_ angle. More information about these angles and their calculation can be found in [Angle Calculations](./angle-information.md). This telemetry type monitors which method has been used to calculate those angles. The OSC messages from this telemetry type go under the OSC label `/Mode` and contain two items:

  1. The first item is an integer value that specifies what method was used to calculate the angles. If the value is 0, then the method used was the [Horizontal](./angle-information.md#horizontal) angle calculation mode. In the case where the value is 1, then the [Circular](./angle-information.md#circular) angle calculation mode was used.
  1. The second value is an integer value of either 0 or 1 that determines if the additional elevation angle is used or not. If the value is one, the additional elevation angle is calculated. Otherwise, if zero, the elevation angle is always set to {math}`0.0`.

A message from this telemetry type can for example look like this:
:::{code-block}
[ /Mode, 0, 1 ]
:::

In the example above, the used angle calculation mode is Horizontal and the additional elevation angle is calculated.

## Customized Nodes Information
This telemetry type requires the user to specify with a script which nodes are of interest to monitor, which is what makes it customizable. There is an example file _nodes.asset_ located in _data\assets\examples\sonification_ that adds the ISS and Tiangong to the list of nodes to monitor with this telemetry type. The OSC messages from this telemetry type are split up for each of the nodes that have been added. Using the mentioned example file, the OSC messages would be sent under the OSC labels `/ISS` and `/Tiangong` respectively (i.e. the identifiers of the added nodes). The messages contain four items:

  1. The distance from the camera to the node, in the distance unit specified in the last item.
  1. The horizontal angle to the node, in radians, with the current angle calculation mode taken into account. For more information, see [Angle Calculations](./angle-information.md).
  1. The elevation angle to the node, in radians, with the current angle calculation mode taken into account. Again, see the page [Angle Calculations](./angle-information.md) for details.
  1. The unit for the distance to the camera, as a string in singular form with the first letter capitalized. For example, `Meter`.

A message from this telemetry type can for example look like this:
:::{code-block}
[ /ISS, 23649385.12794, -0.11008636407019, 0.0, Meter ]
[ /Tiangong, 23365224.606017, -0.22186482355859, 0.0, Meter ]
:::

The example above includes two messages. The first message is for ISS and the second is for Tiangong. In this example, the [Horizontal](./angle-information.md#horizontal) angle calculation mode was used without the [elevation angle](./angle-information.md#additional-elevation-angle-horizontal) included. The first message indicates that ISS is located {math}`23649385.12794` meters from the camera, with a horizontal angle of {math}`-0.11008636407019` radians. The elevation angle is {math}`0.0` radians, since the elevation angle was not enabled. The second message shows that Tiangong is {math}`23365224.606017` meters from the camera, with a horizontal angle of {math}`-0.22186482355859` radians and an elevation angle of {math}`0.0` radians.
