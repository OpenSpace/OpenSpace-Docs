---
authors:
  - name: OpenSpace Team
---

# Angle Calculations
The telemetry types in the [Telemetry Module](index.md) sometimes provide angles from the camera to one or more tracked objects in the scene. The angles provide information about the objects' location in relation to the viewer (camera). This page covers the details of how those angles are computed. 

As briefly mentioned in the [Angle Calculation Mode](./telemetry-types-general.md#angle-calculation-mode) telemetry type on the general telemetry types page, there are two different angle calculation modes: [Horizontal](#horizontal) and [Circular](#circular). The mode can be set in the OpenSpace user interface and which mode to use depends on the type of display and/or sound environment used, as well as the use case. For example, in the [sonification](./sonification.md#sonification), the angles map sounds to positions in a surround sound system. Depending on the setup of the speakers in a surround sound system, the angle may need to be computed differently. This is why there are two modes. The Horizontal mode is tailored for display environments with a forward-facing direction, like the Visualization Center dome theater in Norrköping, Sweden. While the Circular mode is designed for omnidirectional planetariums, like the Hayden Planetarium at the American Museum of Natural History in New York, USA. For an overview of these surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). Each angle calculation mode and its respective use case is explained in more detail below.

Both angle calculation modes will always compute an angle from the camera to the object within a horizontal plane of reference in relation to the camera. However, both modes may also include an optional _elevation angle_ that provides information about the objects' vertical height in relation to the reference plane.

:::{note}
Note that in a multiple node display system, where several computers work together to create an immersive display (such as a dome theater or a planetarium), the angles are only calculated on the main display (often the display used by the pilot). Therefore, to ensure that the angles match the surround sound system, it is important that the main display is configured to align with the surround system. For example, if the immersive display has a forward direction at the center of the entire display, then the main display should also have its center as the forward direction. This ensures that the angles calculated for the main display correspond to the object's position in the larger immersive environment, aligning with the surround sound configuration.
:::

:::::{tab-set}
::::{tab-item} Horizontal
## Horizontal
This angle calculation mode is suitable for flat displays or forward-facing immersive environments, such as the Visualization Center dome theater in Norrköping, Sweden. For more information about surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). This angle determines where the object is placed within a horizontal plane of reference in relation to the camera, how this angle is computed is explained below.

The goal is to calculate the angle, {math}`\theta`, from the camera to the object within a horizontal plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the left direction of the camera (i.e., the negative {math}`Camera_{Right}` vector), with the {math}`Camera_{Up}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal.png
:alt: "Horizontal Angle Calculation Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`CameraToObject` vector is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above). The {math}`P_{R}(Object)` vector is then the {math}`CameraToObject` vector projected onto the reference plane {math}`R`. The {math}`P_{Up}(Object)` vector is the {math}`CameraToObject` vector projected onto the {math}`Camera_{Up}` vector (i.e., the normal of plane {math}`R`). This gives the formula to calculate the {math}`P_{R}(Object)` vector as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{Up}(Object)
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{View}` vector, and the {math}`P_{R}(Object)` vector, is calculated with the {math}`Camera_{Up}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero degrees would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` vector, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative, as shown in the figure above.

### Additional Elevation Angle (Horizontal)
This angle is optional and is only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to {math}`0.0`. This angle determines where the object is placed within a vertical plane of reference in relation to the camera, i.e the height in relation to the horizontal plane of reference mentioned in the previous section. How this angle is computed is explained below.

The goal is to calculate the elevation angle, {math}`\psi`, from the camera to the object within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-vertical.png
:alt: "Elevation Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`CameraToObject` vector is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above). The {math}`P_{R}(Object)` vector is then the {math}`CameraToObject` vector projected onto the reference plane {math}`R`. The {math}`P_{Right}(Object)` vector is the {math}`CameraToObject` vector projected onto the {math}`Camera_{Right}` vector (i.e., the normal of the plane {math}`R`). This gives the formula to calculate the {math}`P_{R}(Object)` vector as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{Right}(Object)
:::

Then the elevation angle, {math}`\psi`, between the {math}`Camera_{View}` vector, and the {math}`P_{R}(Object)` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` in radians, and zero degrees would be directly in the {math}`Camera_{View}` direction. When the object is located above the {math}`Camera_{View}` vector, then the elevation angle will be a positive value, as shown in the figure above. If instead, the object is located below, the elevation angle will become negative.

<!-- @TODO Add an explanation that the angles for the moons are calculated in another manner and add figures for that too. -->
::::

::::{tab-item} Circular
## Circular
This angle calculation mode is suitable for centered fisheye displays or omnidirectional immersive environments, such as the Hayden Planetarium at the American Museum of Natural History in New York, USA. For more information about surround sound configurations see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). This angle determines where the object is placed in a circular space around the center of the screen.

Calculate the angle, {math}`\theta`, to the object in circular space around the center point in the {math}`CameraViewPlane`. The {math}`CameraViewPlane` is the plane with the {math}`Camera_{Up}` direction and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` direction), with the negative {math}`Camera_{View}` direction as the normal. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero degrees would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` direction, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative (as the case in the figure below shows).

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular.png
:alt: "Circular Angle Calculation Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`CameraToObject` vector is the vector from the {math}`Camera` to the {math}`Object`. The {math}`Radius` vector is then the {math}`CameraToObject` vector projected to the {math}`CameraViewPlane`. The {math}`P_{View}(Object)` vector is the {math}`CameraToObject` vector projected onto the {math}`Camera_{View}` direction (which is the negative normal of the {math}`CameraViewPlane`). This gives the formula to calculate the {math}`Radius` vector as follows:

:::{math}
  Radius = CameraToObject - P_{View}(Object)
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{Up}` direction, and the {math}`Radius` vector, is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the {math}`CameraViewPlane`) used as the reference axis.

### Additional Elevation Angle (Circular)
This angle determines how far away from the center of the screen the object is.

An additional elevation angle, {math}`\psi`, in the vertical direction within the {math}`Camera View + Up Plane` can be added to the calculations. This is enabled with a setting in the [Telemetry Module](index). The {math}`Camera View + Up Plane` is the plane with the {math}`Camera_{View}` direction and the {math}`Camera_{Up}` direction, with the {math}`Camera_{Right}` direction as the normal. The elevation angle goes from {math}`-\dfrac{\pi}{2}` to {math}`\dfrac{\pi}{2}` in radians and zero degrees is directly in the {math}`Camera_{View}` direction. Positive elevation angles is in the {math}`Camera_{Up}` direction, and negative angles are in the down direction of the camera.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-vertical.png
:alt: "Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
:class: only-light
:::

To calculate the elevation angle, {math}`\psi`, in the case of the circular angle calculation mode, several steps needs to be taken.
In the first step, the vector from the {math}`Camera` to the {math}`Object`, i.e. {math}`CameraToObject`, is projected to the {math}`CameraViewPlane`. The {math}`Radius` vector, is then the {math}`CameraToObject` vector projected to the {math}`CameraViewPlane`. The {math}`P_{View}(Object)` vector, is the {math}`CameraToObject` vector projected on to the {math}`Camera_{View}` direction (which is the negative normal of the {math}`CameraViewPlane`). This gives the formula to calculate the {math}`Radius` vector as follows:

:::{math}
  Radius = CameraToObject - P_{View}(Object)
:::

In the next step, the angle {math}`\theta`, between the {math}`Camera_{Up}` direction, and the {math}`Radius` vector, is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the {math}`CameraViewPlane`) used as the reference axis.

The next step is to counter-rotate the {math}`CameraToObject` vector with the angle {math}`\theta` from the previous step. The result is that the {math}`CameraToObject_{Rotated}` vector is now located within the {math}`Camera View + Up Plane`.

Lastly, the elavation angle, {math}`\psi`, between the {math}`Camera_{View}` direction, and the {math}`CameraToObject_{Rotated}` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of the {math}`Camera View + Up Plane`) used as the reference axis.

<!-- @TODO Add an explanation that the angles for the moons are calculated in another manner and add figures for that too. -->
::::
:::::
