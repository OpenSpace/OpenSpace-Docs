---
authors:
  - name: OpenSpace Team
---

# Angle Calculations
The telemetry types in the [Telemetry Module](index.md) sometimes include information about angles from the camera to one or more tracked objects in the scene. The angles provide information about the objects' location in relation to the camera. This page covers the details of how those angles are computed.

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
This angle calculation mode is suitable for flat displays or forward-facing immersive environments. For more information about surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). This angle determines where the object is placed within a horizontal plane of reference in relation to the camera. How this angle is computed is explained below.

The angle {math}`\theta` is here defined as the angle from the camera to the object within a horizontal plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` vector), with the {math}`Camera_{Up}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal.png
:alt: "Horizontal Angle Calculation Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

The {math}`CameraToObject` vector points from the {math}`Camera` to the {math}`Object` (not shown in the figure above). {math}`P_{R}(Object)` is {math}`CameraToObject` projected onto the reference plane {math}`R`. {math}`P_{Up}(Object)` is {math}`CameraToObject` projected onto {math}`Camera_{Up}` (i.e. the normal of plane {math}`R`). This gives the formula to calculate {math}`P_{R}(Object)` as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{Up}(Object)
:::

Then the angle, {math}`\theta`, between {math}`Camera_{View}` and {math}`P_{R}(Object)` is calculated with {math}`Camera_{Up}` (i.e. the normal of the plane {math}`R`) as the reference axis. The angle ranges from {math}`-\pi` to {math}`\pi` radians, with zero pointing in the {math}`Camera_{View}` direction. If the object is to the left of this direction, the angle is positive; if it's to the right (as in the example above), the angle is negative.

### Additional Elevation Angle
(additional-elevation-angle-horizontal)=
This angle is optional and is only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to `0.0`. This angle determines where the object is placed within a vertical plane of reference in relation to the camera, i.e the height in relation to the horizontal plane of reference mentioned in the previous section. How this angle is computed is explained below.

The elevation angle {math}`\phi` is here defined as the angle from the camera to the object within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-vertical.png
:alt: "Elevation Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

{math}`CameraToObject` is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above). {math}`P_{R}(Object)` is then {math}`CameraToObject` projected onto the reference plane {math}`R`. {math}`P_{Right}(Object)` is {math}`CameraToObject` projected onto {math}`Camera_{Right}` (i.e. the normal of the plane {math}`R`). This gives the formula to calculate {math}`P_{R}(Object)` as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{Right}(Object)
:::

Then the elevation angle, {math}`\phi`, between {math}`Camera_{View}` and {math}`P_{R}(Object)` is calculated with {math}`Camera_{Right}` (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle ranges from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` radians, with zero pointing in the {math}`Camera_{View}` direction. If the object is located above the {math}`Camera_{View}` vector (as shown in the figure above), the elevation angle is positive; if it's instead located below, the elevation angle will be negative.

### Moon Angle
(moon-angle-horizontal)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. It is the angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a horizontal plane of reference in relation to the camera.

The angle {math}`\theta` is here defined as the angle from object {math}`A` (the planet) to object {math}`B` (the moon) within a horizontal plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` vector), with the {math}`Camera_{Up}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-moon.png
:alt: "Moon Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

{math}`AToB` is the vector from the object {math}`A` to object {math}`B`. {math}`P_{R}(AToB)` is then {math}`AToB` projected onto the reference plane {math}`R`. {math}`M(Camera_{View})` is {math}`Camera_{View}` that has been moved (without changing its direction) to the projected position of {math}`A` onto the reference plane {math}`R`.

Then the angle, {math}`\theta`, between {math}`M(Camera_{View})` and {math}`P_{R}(AToB)` is calculated with {math}`Camera_{Up}` (i.e. the normal of the plane {math}`R`) as the reference axis. The angle ranges from {math}`-\pi` to {math}`\pi` radians, with zero pointing in the {math}`M(Camera_{View})` direction. If the object is located to the left of this direction, the angle is positive; if to the right (as shown in the figure above), it is negative.

### Moon Additional Elevation Angle
(moon-additional-elevation-angle-horizontal)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. This angle is also optional and only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, then this angle is always set to `0.0`. This angle is the elevation angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a vertical plane of reference in relation to the camera, i.e the height in relation to the horizontal plane of reference mentioned in the previous section. How this angle is computed is explained below.

The elevation angle {math}`\phi` is here defined as the angle from object {math}`A` (the planet) to object {math}`B` (the moon) within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/horizontal-moon-vertical.png
:alt: "Moon Elevation Angle Calculation (Horizontal) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

{math}`AToB` is the vector from the object {math}`A` to object {math}`B`. {math}`P_{R}(AToB)` is then {math}`AToB` projected onto the reference plane {math}`R`. {math}`M(Camera_{View})` is {math}`Camera_{View}` that has been moved (without changing its direction) to the projected position of {math}`A` onto the reference plane {math}`R`.

Then the elevation angle, {math}`\phi`, between {math}`M(Camera_{View})` and {math}`P_{R}(AToB)` is calculated with {math}`Camera_{Right}` (i.e. the normal of plane {math}`R`) as the reference axis. The elevation angle ranges from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` radians, with zero pointing in the {math}`M(Camera_{View})` direction. If the object is located above this direction (as shown in the figure above), the elevation angle is positive, and if below, it is negative.


::::
::::{tab-item} Circular
## Circular
This angle calculation mode is suitable for centered fisheye displays or omnidirectional immersive environments. For more information about surround sound configurations, see [Surround Sound Configurations](./sonification.md#surround-sound-configurations). The computed angle determines the object's position in a circular space around the center of the screen. Compared to the horizontal mode, this mode calculates the angles in a circular (or radial) manner around the center point instead of the deviation from the camera view direction. The angle calculation is explained below.

The angle {math}`\theta` is here defined as the angle to the object in a circular space around the center of the screen within a plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{Up}` vector and the left direction of the camera (i.e. the negative {math}`Camera_{Right}` vector), with the negative {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular.png
:alt: "Circular Angle Calculation Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

{math}`CameraToObject` is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above). {math}`P_{R}(Object)` is then {math}`CameraToObject` projected onto the reference plane {math}`R`. {math}`P_{View}(Object)` (not shown in the figure above) is {math}`CameraToObject` projected onto {math}`Camera_{View}` (i.e. the negative normal of plane {math}`R`). This gives the formula to calculate {math}`P_{R}(Object)` as follows:

:::{math}
  P_{R}(Object) = CameraToObject - P_{View}(Object)
:::

Then the angle, {math}`\theta`, between {math}`Camera_{Up}` and {math}`P_{R}(Object)` is calculated with the negative {math}`Camera_{View}` vector (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle ranges from {math}`-\pi` to {math}`\pi` radians, with zero pointing in the {math}`Camera_{View}` direction. If the object is to the left of this direction, the angle is positive; if it is to the right (as in the figure above), the angle is negative.

### Additional Elevation Angle
(additional-elevation-angle-circular)=
This angle determines how far away from the center of the screen the object is located. It is optional and only calculated if a setting in the [Telemetry Module](index) is enabled. If this setting is not enabled, the angle will always be `0.0`.  The angle calculation is explained below.

The elevation angle, {math}`\phi`, is in this case defined as the angle from the camera to the object within a vertical plane of reference, {math}`R`. The reference plane {math}`R` is the plane spanned by {math}`Camera_{View}` and {math}`Camera_{Up}` with {math}`Camera_{Right}` as the normal. The plane {math}`A` is also gonna be needed and is the plane spanned by {math}`Camera_{Up}` and {math}`Camera_{Right}` with {math}`Camera_{View}` as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-vertical.png
:alt: "Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

Calculating the elevation angle {math}`\phi` in the circular mode is done in multiple steps. First, {math}`CameraToObject`, which is the vector from the {math}`Camera` to the {math}`Object` (not shown in the figure above), is projected onto the plane {math}`A`, creating the vector {math}`P_{A}(Object)`. {math}`P_{View}(Object)` is {math}`CameraToObject` projected onto {math}`Camera_{View}` (which is the normal of the plane {math}`A`). This gives the formula to calculate {math}`P_{A}(Object)` as follows:

:::{math}
  P_{A}(Object) = CameraToObject - P_{View}(Object)
:::

Next, the angle {math}`\theta` between {math}`Camera_{Up}` and {math}`P_{A}(Object)` is calculated, with {math}`Camera_{View}` (i.e. the normal of the plane {math}`A`) as the reference axis. Then, {math}`CameraToObject` is rotated by this angle ({math}`\theta`) to align with {math}`Camera_{Up}`. The resulting {math}`R_{R}(P_{A}(Object))` is now located within the reference plane {math}`R`.

Lastly, the elevation angle, {math}`\phi`, between {math}`Camera_{View}` and {math}`R_{R}(P_{A}(Object))` is calculated with {math}`Camera_{Right}` (i.e. the normal of the reference plane {math}`R`) used as the reference axis. The elevation angle ranges from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` radians, with zero pointing in the {math}`Camera_{View}` direction. If the object is located above this direction (as in the figure above), the elevation angle is positive; if below, the angle is negative.

### Moon Angle
(moon-angle-circular)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. It is the angle from the planet, {math}`A`, to one of its moons, {math}`B`, within a circular space around the center of the screen, how this angle is computed is explained below.

The angle {math}`\theta` is here defined as the angle from object {math}`A` (the planet) to object {math}`B` (the moon) within a plane of reference, {math}`R`, with respect to a direction in relation to the camera. The reference plane {math}`R` is the plane spanned by the {math}`Camera_{Up}` vector and {math}`Camera_{Right}` vector, with the {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-moon.png
:alt: "Moon Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

{math}`AToB` is the vector from the object {math}`A` to object {math}`B`. {math}`P_{R}(AToB)` is then {math}`AToB` projected onto the reference plane {math}`R`.

:::{note}
Note that in the case shown in the figure above, both objects {math}`A` and {math}`B` are already located within the reference plane {math}`R`. Therefore {math}`P_{R}(AToB) = AToB`.
:::

Then the angle, {math}`\theta`, between {math}`Camera_{Up}` and {math}`P_{R}(AToB)` is calculated with {math}`Camera_{View}` (i.e. the normal of the plane {math}`R`) used as the reference axis. The angle ranges from {math}`-\pi` to {math}`\pi` radians, with zero radians pointing in the {math}`Camera_{Up}` direction from point {math}`A`. If the object is to the left of this direction from point {math}`A`, the angle is positive; if to the right (as shown in the figure above), the angle is negative.

### Moon Additional Elevation Angle
(moon-additional-elevation-angle-circular)=
This angle is only calculated for the specialized [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) telemetry type. It is the elevation angle from the planet, {math}`A`, to one of its moons, {math}`B`, which determines how far away from the planet, {math}`A`, the moon, {math}`B`, is located in a circular space around the planet, {math}`A`. This angle is also optional and only calculated if a setting in the [Telemetry Module](./index) is enabled. If this setting is not enabled, then this angle is always set to `0.0`. The angle calculation is explained below.

The elevation angle, {math}`\phi`, is here defined as the angle from object {math}`A` (the planet) to object {math}`B` (the moon) within a plane of reference, {math}`R`, spanned by the {math}`Camera_{View}` vector and the {math}`Camera_{Up}` vector, with the {math}`Camera_{Right}` vector as the normal. Specifically, for this computation, the position for the moon (which is orbiting point {math}`A`) used is the one which is parallel to the reference plane {math}`R`, no matter the current position of object {math}`B`. This transformation requires information about what is here called plane {math}`C`, which is the plane spanned by the {math}`Camera_{Up}` vector and the {math}`Camera_{Right}` vector, with the {math}`Camera_{View}` vector as the normal. The image below shows a figure of these objects and the computations.

<!-- @TODO Generate a dark mode version of this image -->
:::{image} images/circular-moon-vertical.png
:alt: "Moon Elevation Angle Calculation (Circular) Schematic"
:width: 100%
:align: center
<!-- :class: only-light -->
:::

Calculating the elevation angle, {math}`\phi`, from the object {math}`A` to object {math}`B` in this case again requires several steps. First, {math}`AToB`, which is the vector from the object {math}`A` to object {math}`B`, is projected onto the plane {math}`C`, creating {math}`P_{C}(AToB)`. {math}`M(Camera_{Up})` is {math}`Camera_{Up}` that has been moved (without changing its direction) to the projected position of {math}`A` onto the plane {math}`C`. Also, {math}`M(Camera_{View})` is {math}`Camera_{View}` that has been moved (without changing its direction) to end at the projected position of {math}`A` onto the reference plane {math}`R`.

:::{note}
Note that in the case shown in the figure above, both objects {math}`A` and {math}`B` are already located within the plane {math}`C`. Therefore {math}`P_{C}(AToB) = AToB`.
:::

In the next step, the angle {math}`\theta`, between {math}`M(Camera_{Up})` and {math}`P_{C}(AToB)` is calculated with {math}`Camera_{View}` (i.e. the normal of the plane {math}`C`) used as the reference axis. The next step is to rotate {math}`AToB` with this angle {math}`\theta` to align with {math}`M(Camera_{Up})`, resulting in {math}`R_{Up}(AToB)`. This resulting vector is then projected onto {math}`Camera_{Up}`. {math}`P_{R}(R_{Up}(AToB))` is then the vector from the start of {math}`M(Camera_{View})` to the end of {math}`R_{Up}(AToB)`.

Then the elevation angle, {math}`\phi`, between {math}`M(Camera_{View})` and {math}`P_{R}(R_{Up}(AToB))` is calculated with {math}`Camera_{Right}` (i.e. the normal of plane {math}`R`) used as the reference axis. The elevation angle goes from {math}`-\frac{\pi}{2}` to {math}`\frac{\pi}{2}` in radians, and zero radians would be directly in the {math}`M(Camera_{View})` direction. When the object is located above the {math}`M(Camera_{View})` vector (as shown in the figure above), then the elevation angle will be possitive. If instead, the object is located below, the elevation angle is negative.

::::
:::::
