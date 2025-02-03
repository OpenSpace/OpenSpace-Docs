---
authors:
  - name: OpenSpace Team
---

# General Telemetry Types
The general telemetry types in the [Telemetry Module](index.md) monitor the general state of OpenSpace and send that information over the OSC connection. There are several types that monitor different aspects of the software. Each type is explained in more detail in the sections below.

In summary, the general telemetry types available in OpenSpace are:
- [Camera Information](#camera-information)
- [Focus](#focus)
- [Time Information](#time-information)
- [Customized Nodes Information](#customized-nodes-information)
- [Angle Calculation Mode](#angle-calculation-mode)

## Camera Information
This telemetry type monitors the camera state and sends that information over the OSC connection. The OSC messages from this telemetry type go under the OSC label `/Camera` and contain nine items in addition to the label:

  1. The following three items describe the {math}`x`, {math}`y`, and {math}`z` positions of the camera in the world, specified in relation to the Solar System barycenter. This is the {math}`x` position of the camera in the world.
  2. The {math}`y` position of the camera in the world.
  3. The {math}`z` position of the camera in the world.
  4. The next four items are the quaternion rotation of the camera. This first item is the angle {math}`w` in radians for the quaternion rotation of the camera.
  5. The next three items are the axis of the quaternion rotation of the camera. This is the {math}`x` component of the unit rotation axis in the quaternion rotation of the camera.
  6. The {math}`y` component of the rotation axis in the quaternion rotation.
  7. The {math}`z` component of the rotation axis in the quaternion rotation.
  8. The speed of the camera, specified in the selected distance unit per second.
  9. The selected distance unit for the speed of the camera, as a string in singular form with the first letter capitalized.

A  message from this telemetry type can for example look like this:
:::{code-block}
[ /Camera, -144982761635.78, -4673195479.6344, -19947642284.929, -0.016136366108094, 0.046858848656595, -0.62388829681315, -0.77994054843366, 34.074930097613, Kilometer ]
:::

In the example above, the position of the camera relative to the Solar System Barycenter is {math}`(-144982761635.78, -4673195479.6344, -19947642284.929)`. The camera is rotated {math}`0.016136366108094` radians around the unit axis {math}`(0.046858848656595, -0.62388829681315, -0.77994054843366)`. Lastly, the camera moves with a speed of {math}`34.074930097613` kilometers per second.

## Focus
This telemetry type sends out a message every time the focus is changed in OpenSpace. The OSC messages from this telemetry type go under the OSC label `/Focus` and contain only one item:

  1. The identifier of the new focus in OpenSpace, as a string.

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Focus, Earth ]
:::

In the example above, the current focus in OpenSpace was set to Earth.

## Time Information
This telemetry type monitors the time in OpenSpace and sends that information over the OSC connection. The OSC messages from this telemetry type go under the OSC label `/Time` and contain three items:

  1. The speed of the simulation time, specified in the selected time unit in the simulation, per real-life second.
  2. The selected time unit for the speed of simulation time, as a string in singular form with the first letter capitalized.
  3. The current simulation time in OpenSpace specified in J2000 seconds, that is, the number of seconds past the J2000 epoch (i.e. January 1, 2000 12:00:00 TT).

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Time, 30.0, Minute, 787312539.37412 ]
:::

In the example above, the simulation time in OpenSpace progresses {math}`30.0` minutes per real-life second, and the current time is{math}`787312539.37412` seconds past the J2000 epoch.

## Customized Nodes Information
This telemetry type requires the user to specify with a script which nodes are of interest to monitor, which is what makes it customizable. There is an example file _nodes.asset_ located in _data\assets\examples\sonification_ that adds the ISS and Tiangong to the list of nodes to monitor with this telemetry type. The OSC messages from this telemetry type are split up for each of the nodes that have been added. Using the mentioned example file, the OSC messages would be sent under the OSC labels `/ISS` and `/Tiangong` respectively (i.e. the identifiers of the added nodes). The messages contain four items:

  1. The distance from the camera to the node, specified in the selected distance unit.
  2. The horizontal angle in radians to the node, with the current angle calculation mode taken into account. For more information see [Angle Calculations Explanation](./angle-information.md#angle-calculations-explanation).
  3. The elevation angle in radians to the node, with the current angle calculation mode taken into account.
  4. The selected distance unit for the distance to the camera, as a string in singular form with the first letter capitalised.

Here is an example of how messages from this telemetry type can look:
:::{code-block}
[ /ISS, 23649385.12794, -0.11008636407019, 0.0, Meter ]
[ /Tiangong, 23365224.606017, -0.22186482355859, 0.0, Meter ]
:::

The example above includes two messages. The first message is for ISS and the second is for Tiangong. The first message indicates that ISS is located {math}`23649385.12794` meters from the camera, with a horizontal angle of {math}`-0.11008636407019` radians and an elevation angle of {math}`0.0` radians (the elevation angle is not enabled). The second message shows that Tiangong is {math}`23365224.606017` meters from the camera, with a horizontal angle of {math}`-0.22186482355859` radians and an elevation angle of {math}`0.0` radians (the elevation angle is not enabled).

## Angle Calculation Mode
For some telemetry types, such as the [Customized Nodes Information](#customized-nodes-information) and the specialized [Planets Sonification](./specialized.md#planets-sonification), one part of the information that is sent is two angles that describes where the object is placed on the screen. This telemetry type monitors which method has been used to calculate those angles, more informaiton about how these angle calculations are done can be found in [Angle Calculations Explanation](./angle-information.md#angle-calculations-explanation). The OSC messages from this telemetry type goes under the OSC label `/Mode` and contains two items, explained in detail below:

  1. The first item is an integer value that specifies what method was used to calculate the angles. If the value is 0, then the method used was the [Horizontal](./angle-information.md#horizontal) angle calculation mode. In the case where tha value is 1, then the [Circular](./angle-information.md#circular) angle calculation mode was used.
  2. The second value is an integer that is either 0 or 1 that detemines if the additional elevation angle is used or not. If the value is 0 then the elevation angle is always set to {math}`0.0`, if the value is 1 then the additional elevation angle is calculated.

Here is an example of how a message from this telemetry type can look like:
:::{code-block}
[ /Mode, 0, 1 ]
:::

In the example above, the used angle calculation mode is Horizontal and the additional elevation angle is calculated.
