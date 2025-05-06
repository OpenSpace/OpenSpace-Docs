---
authors:
  - name: OpenSpace Team
---

# Angle Calculations
The telemetry types in the [Telemetry Module](index.md) sometimes provide information about angles from the camera to one or more tracked objects in the scene. The angles provide information about the objects' location in relation to the camera. This page covers the details of how those angles are computed.

As briefly mentioned in the [Angle Calculation Mode](./telemetry-types-general.md#angle-calculation-mode) telemetry type on the general telemetry types page, there are two different angle calculation modes: [Horizontal](#horizontal) and [Circular](#circular). The mode can be set in the OpenSpace user interface, and which mode to use depends on the type of display and/or sound environment used, as well as the use case. For example, in the [sonification](./sonification.md#sonification), the angles map sounds to positions in a surround sound system. Depending on the setup of the speakers in a surround sound system, the angle may need to be computed differently. This is why there are two modes. The Horizontal mode is tailored for display environments with a forward-facing direction, such as the Visualization Center dome theater in Norrköping, Sweden, while the Circular mode is designed for omnidirectional planetariums, such as the Hayden Planetarium at the American Museum of Natural History in New York, USA. For an overview of these surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). Each angle calculation mode and its respective use case are explained in more detail below.

Both angle calculation modes will always compute an angle from the camera to the object within a horizontal plane of reference in relation to the camera. However, both modes may also include an optional _elevation angle_ that provides information about the objects' vertical height in relation to the horizontal reference plane.

:::{important}
In a multiple-node display system, where several computers work together to create an immersive display (such as a dome theater or a planetarium), the angles are only calculated on the main display (often the display used by the pilot). Therefore, to ensure that the angles match the surround sound system, it is important that the main display is configured to align with the surround system. For example, if the immersive display has a forward direction at the center of the entire display, then the main display should also have its center as the forward direction. This ensures that the angles calculated for the main display correspond to the object's position in the larger immersive environment, aligning with the surround sound configuration.
:::

:::{note}
Note that in the figures below, none of the vectors that are shown are normalized.
:::

:::::{tab-set}
::::{tab-item} Horizontal
## Horizontal
This angle calculation mode is suitable for flat displays or forward-facing immersive environments, such as the Visualization Center dome theater in Norrköping, Sweden. For more information about surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). This angle determines where the object is placed within a horizontal plane of reference in relation to the camera. How this angle is computed is explained below.

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

Then the angle, {math}`\theta`, between the {math}`Camera_{View}` vector, and the {math}`P_{R}(Object)` vector, is calculated with the {math}`Camera_{Up}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero radians would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` vector, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative, as shown in the figure above.

### Additional Elevation Angle
(additional-elevation-angle-horizontal)=
This angle is optional and is only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to {math}`0.0`. This angle determines where the object is placed within a vertical plane of reference in relation to the camera, i.e the height in relation to the horizontal plane of reference mentioned in the previous section. How this angle is computed is explained below.

The goal is to calculate the elevation angle, {math}`\phi`, from the camera to the object within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The image below shows a figure of these objects and the computations.

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

Then the elevation angle, {math}`\phi`, between the {math}`Camera_{View}` vector, and the {math}`P_{R}(Object)` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` in radians, and zero radians would be directly in the {math}`Camera_{View}` direction. When the object is located above the {math}`Camera_{View}` vector, then the elevation angle will be a positive value, as shown in the figure above. If instead, the object is located below, the elevation angle will become negative.

### Moon Angle
(moon-angle-horizontal)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. It is the angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a horizontal plane of reference in relation to the camera, how this angle is computed is explained below.

The goal is to calculate the angle, {math}`\theta`, from object {math}`A` (the planet) to object {math}`B` (the moon) within a horizontal plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the left direction of the camera (i.e., the negative {math}`Camera_{Right}` vector), with the {math}`Camera_{Up}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-moon.png
:alt: "Moon Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`AToB` vector is the vector from the object {math}`A` to object {math}`B`. The {math}`P_{R}(AToB)` vector is then the {math}`AToB` vector projected onto the reference plane {math}`R`. The {math}`M(Camera_{View})` vector is the {math}`Camera_{View}` vector that has been moved (without changing its direction) to the projected position of {math}`A` onto the reference plane {math}`R`.

Then the angle, {math}`\theta`, between the {math}`M(Camera_{View})` vector, and the {math}`P_{R}(AToB)` vector, is calculated with the {math}`Camera_{Up}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero radians would be directly in the {math}`M(Camera_{View})` direction. When the object is located towards the left relative to the {math}`M(Camera_{View})` vector, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative, as shown in the figure above.

### Moon Additional Elevation Angle
(moon-additional-elevation-angle-horizontal)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. This angle is also optional and only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to {math}`0.0`. This angle is the elevation angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a vertical plane of reference in relation to the camera, i.e the height in relation to the horizontal plane of reference mentioned in the previous section. How this angle is computed is explained below.

The goal is to calculate the elevation angle, {math}`\phi`, from object {math}`A` (the planet) to object {math}`B` (the moon) within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-moon-vertical.png
:alt: "Moon Elevation Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`AToB` vector is the vector from the object {math}`A` to object {math}`B`. The {math}`P_{R}(AToB)` vector is then the {math}`AToB` vector projected onto the reference plane {math}`R`. The {math}`M(Camera_{View})` vector is the {math}`Camera_{View}` vector that has been moved (without changing its direction) to the projected position of {math}`A` onto the reference plane {math}`R`.

Then the elevation angle, {math}`\phi`, between the {math}`M(Camera_{View})` vector, and the {math}`P_{R}(AToB)` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` in radians, and zero radians would be directly in the {math}`M(Camera_{View})` direction. When the object is located above the {math}`M(Camera_{View})` vector, then the elevation angle will be a positive value, as shown in the figure above. If instead, the object is located below, the elevation angle will become negative.


::::
::::{tab-item} Circular
## Circular
This angle calculation mode is suitable for centered fisheye displays or omnidirectional immersive environments, such as the Hayden Planetarium at the American Museum of Natural History in New York, USA. For more information about surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). This angle determines where the object is placed in a circular space around the center of the screen. The difference in this mode compared to the horizontal one is that this mode calculates the angles in a circular (or radial) manner around the center of the screen. How this angle is computed is explained below.

The goal is to calculate the angle, {math}`\theta`, to the object in a circular space around the center of the screen within a plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{Up}` vector and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` vector), with the negative {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular.png
:alt: "Circular Angle Calculation Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`CameraToObject` vector is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above). The {math}`P_{R}(Object)` vector is then the {math}`CameraToObject` vector projected onto the reference plane {math}`R`. The {math}`P_{View}(Object)` vector (not shown in the figure above) is the {math}`CameraToObject` vector projected onto the {math}`Camera_{View}` vector (i.e., the negative normal of plane {math}`R`). This gives the formula to calculate the {math}`P_{R}(Object)` vector as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{View}(Object)
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{Up}` vector, and the {math}`P_{R}(Object)` vector, is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero radians would be directly in the {math}`Camera_{View}` direction. When the object is located towards the left relative to the {math}`Camera_{View}` vector, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative, as shown in the figure above.

### Additional Elevation Angle
(additional-elevation-angle-circular)=
This angle is optional and is only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to {math}`0.0`. This angle determines how far away from the center of the screen the object is located. How this angle is computed is explained below.

The goal is to calculate the elevation angle, {math}`\phi`, from the camera to the object within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The plane {math}`A` is also gonna be needed and is the plane spanned by the {math}`Camera_{Up}` vector and the {math}`Camera_{Right}` vector, with the {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-vertical.png
:alt: "Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
:class: only-light
:::

To calculate the elevation angle, {math}`\phi`, in the case of the circular angle calculation mode, several steps need to be taken.
In the first step, the {math}`CameraToObject` vector, which is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above), is projected onto the plane {math}`A`, creating the vector {math}`P_{A}(Object)`. The {math}`P_{View}(Object)` vector is the {math}`CameraToObject` vector projected onto the {math}`Camera_{View}` vector (which is the normal of the plane {math}`A`). This gives the formula to calculate the {math}`P_{A}(Object)` vector as follows:

:::{math}
  P_{A}(Object) = CameraToObject - P_{View}(Object)
:::

In the next step, the angle {math}`\theta`, between the {math}`Camera_{Up}` vector, and the {math}`P_{A}(Object)` vector, is calculated with the {math}`Camera_{View}` vector (i.e. the normal of the plane {math}`A`) used as the reference axis. The next step is to counter-rotate the {math}`CameraToObject` vector with this angle {math}`\theta` to the {math}`Camera_{Up}` vector. The resulting vector {math}`R_{R}(P_{A}(Object))` is now located within the reference plane {math}`R`.

Lastly, the elevation angle, {math}`\phi`, between the {math}`Camera_{View}` vector, and the {math}`R_{R}(P_{A}(Object))` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of the reference plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\dfrac{\pi}{2}` to {math}`\dfrac{\pi}{2}` in radians, and zero radians would be directly in the {math}`Camera_{View}` direction. When the object is located above the {math}`Camera_{View}` vector, then the elevation angle will be a positive value, as shown in the figure above. If instead, the object is located below, the elevation angle will become negative.

### Moon Angle
(moon-angle-circular)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. It is the angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a circular space around the center of the screen, how this angle is computed is explained below.

The goal is to calculate the angle, {math}`\theta`, from object {math}`A` (the planet) to object {math}`B` (the moon) within a plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{Up}` vector and {math}`Camera_{Right}` vector, with the {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-moon.png
:alt: "Moon Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
:class: only-light
:::

The {math}`AToB` vector is the vector from the object {math}`A` to object {math}`B`. The {math}`P_{R}(AToB)` vector is then the {math}`AToB` vector projected onto the reference plane {math}`R`.

:::{note}
Note that in the case shown in the figure above, both objects {math}`A` and {math}`B` are already located within the reference plane {math}`R`. Therefore {math}`P_{R}(AToB) = AToB`.
:::

Then the angle, {math}`\theta`, between the {math}`Camera_{Up}` vector, and the {math}`P_{R}(AToB)` vector, is calculated with the {math}`Camera_{View}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle goes from {math}`-\pi` to {math}`\pi` in radians, and zero radians would be directly in the {math}`Camera_{Up}` direction from point {math}`A`. When the object is located towards the left relative to the {math}`Camera_{Up}` direction from point {math}`A`, then the angle will be a positive value. If instead, the object is located towards the right, the angle will become negative, as shown in the figure above.

<!-- @TODO Change this to be correct for the Circular mode -->
### Moon Additional Elevation Angle
(moon-additional-elevation-angle-circular)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. This angle is also optional and only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to {math}`0.0`. It is the elevation angle from the planet, {math}`A`, to one of its moons, {math}`B`, which determines how far away from the planet, {math}`A`, the moon, {math}`B`, is located in a circular space around the planet, {math}`A`. How this angle is computed is explained below.

The goal is to calculate the elevation angle, {math}`\phi`, from object {math}`A` (the planet) to object {math}`B` (the moon) within a plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The plane {math}`C` is also gonna be needed and is the plane spanned by the {math}`Camera_{Up}` vector and the {math}`Camera_{Right}` vector, with the {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-moon-vertical.png
:alt: "Moon Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
:class: only-light
:::

To calculate the elevation angle, {math}`\phi`, from the object {math}`A` to object {math}`B` in the case of the circular angle calculation mode, several steps need to be taken. In the first step, the {math}`AToB` vector, which is the vector from the object {math}`A` to object {math}`B`, is projected onto the plane {math}`C`, creating the vector {math}`P_{C}(AToB)`. The {math}`M(Camera_{Up})` vector is the {math}`Camera_{Up}` vector that has been moved (without changing its direction) to the projected position of {math}`A` onto the plane {math}`C`. Also, the {math}`M(Camera_{View})` vector is the {math}`Camera_{View}` vector that has been moved (without changing its direction) to end at the projected position of {math}`A` onto the reference plane {math}`R`.

:::{note}
Note that in the case shown in the figure above, both objects {math}`A` and {math}`B` are already located within the plane {math}`C`. Therefore {math}`P_{C}(AToB) = AToB`.
:::

In the next step, the angle {math}`\theta`, between the {math}`M(Camera_{Up})` vector, and the {math}`P_{C}(AToB)` vector, is calculated with the {math}`Camera_{View}` vector (i.e. the normal of the plane {math}`C`) used as the reference axis. The next step is to counter-rotate the {math}`AToB` vector with this angle {math}`\theta` to the {math}`M(Camera_{Up})` vector, resulting in the vector {math}`R_{Up}(AToB)`. This resulting vector is then projected onto the {math}`Camera_{Up}` vector. The final {math}`P_{R}(R_{Up}(AToB))` vector is then the vector from the start of {math}`M(Camera_{View})` vector to the end of the {math}`R_{Up}(AToB)` vector.

Then the elevation angle, {math}`\phi`, between the {math}`M(Camera_{View})` vector, and the {math}`P_{R}(R_{Up}(AToB))` vector is calculated, with the {math}`Camera_{Right}` vector (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` in radians, and zero radians would be directly in the {math}`M(Camera_{View})` direction. When the object is located above the {math}`M(Camera_{View})` vector, then the elevation angle will be a positive value, as shown in the figure above. If instead, the object is located below, the elevation angle will become negative.

::::
:::::
