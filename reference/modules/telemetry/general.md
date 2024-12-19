---
authors:
  - name: OpenSpace Team
---

# General Telemetry Types
The general telemetry types in the Telemetry Module monitor the general state of OpenSpace and send that information over the OSC connection. There are several types that monitor different aspects, and each of them is explained in more detail in the sections below.

All the general telemetry types that are available in OpenSpace:
- Angle Calculation Mode
- Camera Information
- Focus
- Customized Nodes Information
- Time Information

## Angle Calculation Mode
For some telemetry types, such as the [Customized Nodes Information](#customized-nodes-information) and the specialized [Planets Sonification](./specialized.md#planets-sonification), one part of the information that is sent is two angles that describes where an object is placed on the screen. This telemetry type monitors which method has been used to calculate those angles, more informaiton about how these angle calculations are done can be found in [Angle Calculations Explanation](#angle-calculations-explanation). The OSC messages from this telemetry type goes under the OSC label `/Mode` and contains two items, explained in detail below:

  1. The first item is an integer value that specifies what method was used to calculate the angles. If the value is 0, then the method used was the [Horizontal](#horiozontal) angle calculation mode. In the case where tha value is 1, then the [Circular](#circular) angle calculation mode was used.
  2. The second value is an integer that is either 0 or 1 that detemines if the additional elevation angle is used or not. If the value is 0 then the elevation angle is always set to {math}`0.0`, if the value is 1 then the additional elevaiton angle is calculated.

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Mode, 0, 1 ]
:::

In the example above, the used angle calculation mode is Horizontal and the additional elevation angle is calculated.

## Camera Information
This telemetry type monitors the camera and sends that information over the OSC connection. The OSC messages from this telemetry type goes under the OSC label `/Camera` and contains nine items, explained in detail below:

  1. The following three items describe the {math}`x`, {math}`y`, and {math}`z` positions of the camera in the world, specified in relation to the Solar System barycenter. This is the {math}`x` position of the camera in the world.
  2. The {math}`y` position of the camera in the world.
  3. The {math}`z` position of the camera in the world.
  4. The next four items are the quaternion rotation of the camera. This first item is the angle {math}`w` in radians for the quaternion rotation of the camera.
  5. The next three items are the axis of the quaternion rotation of the camera. This is the {math}`x` component of the unit rotation axis in the quaternion rotation of the camera.
  6. The {math}`y` component of the rotation axis in the quaternion rotation.
  7. The {math}`z` component of the rotation axis in the quaternion rotation.
  8. The speed of the camera, specified in the selected distance unit per second.
  9. The selected distance unit for the speed of the camera, as a string in singular form with the first letter capitalised.

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Camera, -144982761635.78, -4673195479.6344, -19947642284.929, -0.016136366108094, 0.046858848656595, -0.62388829681315, -0.77994054843366, 34.074930097613, Kilometer ]
:::

In the example above, the position of the camera relative to the Solar System Barycenter is {math}`(-144982761635.78, -4673195479.6344, -19947642284.929)`. The camera is rotated {math}`0.016136366108094` radians around the unit axis {math}`(0.046858848656595, -0.62388829681315, -0.77994054843366)`. Lastly, the camera moves with a speed of {math}`34.074930097613` kilometers per second.

## Focus
This telemetry type sends out a message every time the focus is changed in OpenSpace. The OSC messages from this telemetry type goes under the OSC label `/Focus` and contains only one item, explained in detail below:

  1. The name of the set focus in OpenSpace as a string.

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Focus, Earth ]
:::

In the example above, the current focus in OpenSpace is the Earth.

## Customized Nodes Information

## Time Information
This telemetry type monitors the time in OpenSpace and sends that information over the OSC connection. The OSC messages from this telemetry type goes under the OSC label `/Time` and contains 3 items, explained in detail below:

  1. The speed of the simulation time, specified in the selected time unit in the simulation per real-life second.
  2. The selected time unit for the speed of simulation time, as a string (text) with the first letter capitalized.
  3. The current simulation time in OpenSpace specified in J2000 seconds. J2000 seconds are the number of seconds past the J2000 epoch (i.e. January 1, 2000 12:00:00 TT)

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Time, 30.0, Minute, 787312539.37412 ]
:::

In the example above, the simulation time in OpenSpace progresses {math}`30.0` minutes per real life second, and the current time is{math}`787312539.37412` number of seconds past the J2000 epoch.

# Angle Calculations Explanation
The following section explains in more depth how the angle calculations work in the different angle calculation modes, as mentioned in [Angle Calculation Mode](#angle-calculation-mode). There are two angle calculation modes, Horizontal and Circular, and each of them can have an additional elevation angle. The angle calculations use the function [`orientedAngle`](https://glm.g-truc.net/0.9.4/api/a00210.html#ga3f15db506641d5f9461259672b7f276c) from the [GLM library](https://glm.g-truc.net/0.9.4/api/index.html).

## Horiozontal
Calculate the angle, {math}`\theta`, to the object in the horizontal direction within the {math}`CameraPlane`. This angle calculation mode is suitable for flat displays or forward-facing immersive environments (such as the Norrköping Visualization Center dome theater). The {math}`CameraPlane` is the plane with the {math}`Camera_{View}` direction and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` direction), with the {math}`Camera_{Up}` direction as the normal. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero degrees would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` direction, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative (as the case in the figure below shows).

:::{image} images/horizontal.png
:alt: "Horizontal Angle Calculation Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`CameraToObject` vector is the vector from the {math}`Camera` to the {math}`Object`. The {math}`CameraToProjectedObject` vector is then the {math}`CameraToObject` vector projected to the {math}`CameraPlane`. The {math}`P_{Up}(Object)` vector is the {math}`CameraToObject` vector projected onto the {math}`Camera_{Up}` direction (which is the normal of the {math}`CameraPlane`). This gives the formula to calculate the {math}`CameraToProjectedObject` vector as follows:

:::{math}
  CameraToProjectedObject = CameraToObject - P_{Up}(Object)
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{View}` direction, and the {math}`CameraToProjectedObject` vector, is calculated with the {math}`Camera_{Up}` vector (i.e. the normal of the {math}`CameraPlane`) used as the reference axis. This is done with the function `orientedAngle`.

### Additional Elevation Angle (Horizontal)
An additional elevation angle, {math}`\psi`, in the vertical direction within the {math}`Camera View + Up Plane` can be added to the calculations. This is enabled with a setting in the [Telemetry Module](index). The {math}`Camera View + Up Plane` is the plane with the {math}`Camera_{View}` direction and the {math}`Camera_{Up}` direction, with the {math}`Camera_{Right}` direction as the normal. The elevation angle goes from {math}`-\dfrac{\pi}{2}` to {math}`\dfrac{\pi}{2}` in radians, and zero degrees is directly in the {math}`Camera_{View}` direction. Positive elevation angles are in the {math}`Camera_{Up}` direction, and negative angles are in the down direction of the camera.

:::{image} images/horizontal-vertical.png
:alt: "Elevation Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`Camera To Object` vector is the vector from the {math}`Camera` to the {math}`Object`. The {math}`Camera To Projected Object` vector is then the {math}`Camera To Object` vector projected to the {math}`Camera View + Up Plane`. The {math}`P_{Right}(Object)` vector is the {math}`Camera To Object` vector projected onto the {math}`Camera_{Right}` direction (which is the normal of the {math}`Camera View + Up Plane`). This gives the formula to calculate the {math}`Camera To Projected Object` vector as follows:

:::{math}
  Camera To Projected Object = Camera To Object - P_{Right}(Object)
:::

Then the angle, {math}`\psi`, between the {math}`Camera_{View}` direction, and the {math}`Camera To Projected Object` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of the {math}`Camera View + Up Plane`) used as the reference axis. This is done with the function `orientedAngle`.

## Circular
Calculate the angle, {math}`\theta`, to the object in circular space around the center point in the {math}`Camera View Plane`. This angle calculation mode is suitable for centered fisheye displays or omnidirectional immersive environments (such as the Hayden planetarium). The {math}`Camera View Plane` is the plane with the {math}`Camera_{Up}` direction and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` direction), with the negative {math}`Camera_{View}` direction as the normal. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero degrees would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` direction, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative (as the case in the figure below shows).

:::{image} images/circular.png
:alt: "Circular Angle Calculation Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`Camera To Object` vector is the vector from the {math}`Camera` to the {math}`Object`. The {math}`Radius` vector is then the {math}`Camera To Object` vector projected to the {math}`Camera View Plane`. The {math}`P_{View}(Object)` vector is the {math}`Camera To Object` vector projected onto the {math}`Camera_{View}` direction (which is the negative normal of the {math}`Camera View Plane`). This gives the formula to calculate the {math}`Radius` vector as follows:

:::{math}
  Radius = Camera To Object - P_{View}(Object)
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{Up}` direction, and the {math}`Radius` vector, is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the {math}`Camera View Plane`) used as the reference axis. This is done with the function `orientedAngle`.

### Additional Elevation Angle (Circular)
An additional elevation angle, {math}`\psi`, in the vertical direction within the {math}`Camera View + Up Plane` can be added to the calculations. This is enabled with a setting in the [Telemetry Module](index). The {math}`Camera View + Up Plane` is the plane with the {math}`Camera_{View}` direction and the {math}`Camera_{Up}` direction, with the {math}`Camera_{Right}` direction as the normal. The elevation angle goes from {math}`-\dfrac{\pi}{2}` to {math}`\dfrac{\pi}{2}` in radians and zero degrees is directly in the {math}`Camera_{View}` direction. Positive elevation angles is in the {math}`Camera_{Up}` direction, and negative angles are in the down direction of the camera.

:::{image} images/circular-vertical.png
:alt: "Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
:class: only-light
:::

To calculate the elevation angle, {math}`\psi`, in the case of the circular angle calculation mode, several steps needs to be taken.
In the first step, the vector from the {math}`Camera` to the {math}`Object`, i.e. {math}`Camera To Object`, is projected to the {math}`Camera View Plane`. The {math}`Radius` vector, is then the {math}`Camera To Object` vector projected to the {math}`Camera View Plane`. The {math}`P_{View}(Object)` vector, is the {math}`Camera To Object` vector projected on to the {math}`Camera_{View}` direction (which is the negative normal of the {math}`Camera View Plane`). This gives the formula to calculate the {math}`Radius` vector as follows:

:::{math}
  Radius = Camera To Object - P_{View}(Object)
:::

In the next step, the angle {math}`\theta`, between the {math}`Camera_{Up}` direction, and the {math}`Radius` vector, is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the {math}`Camera View Plane`) used as the reference axis. This is done with the function `orientedAngle`.

The next step is to counter-rotate the {math}`Camera To Object` vector with the angle {math}`\theta` from the previous step. The result is that the {math}`Camera To Object_{Rotated}` vector is now located within the {math}`Camera View + Up Plane`.

Lastly, the elavation angle, {math}`\psi`, between the {math}`Camera_{View}` direction, and the {math}`Camera To Object_{Rotated}` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of the {math}`Camera View + Up Plane`) used as the reference axis. This is done with the function `orientedAngle`.
