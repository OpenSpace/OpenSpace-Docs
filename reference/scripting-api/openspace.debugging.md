# `openspace.debugging`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addCartesianAxes`](#debuggingaddCartesianAxes-target)
    - [Adds a set of Cartesian axes to the scene graph node identified by the first string, to illustrate its local coordinate system]{#debuggingaddCartesianAxes-list}


*   - [`removePathControlPoints`](#debuggingremovePathControlPoints-target)
    - [Removes the rendered control points]{#debuggingremovePathControlPoints-list}


*   - [`removeRenderedCameraPath`](#debuggingremoveRenderedCameraPath-target)
    - [Removes the currently rendered camera path if there is one]{#debuggingremoveRenderedCameraPath-list}


*   - [`renderCameraPath`](#debuggingrenderCameraPath-target)
    - [Render the current camera path from the path navigation system]{#debuggingrenderCameraPath-list}


*   - [`renderPathControlPoints`](#debuggingrenderPathControlPoints-target)
    - [Render the control points for the camera path spline as spheres]{#debuggingrenderPathControlPoints-list}

:::

## Functions

(debuggingaddCartesianAxes-target)=
### [`addCartesianAxes`](#debuggingaddCartesianAxes-list)
Adds a set of Cartesian axes to the scene graph node identified by the first string, to illustrate its local coordinate system. The second (optional) argument is a scale value, in meters.


:::{card} Parameters


* nodeIdentifier `String` 



* scale `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.debugging.addCartesianAxes(nodeIdentifier, scale)
:::
___

(debuggingremovePathControlPoints-target)=
### [`removePathControlPoints`](#debuggingremovePathControlPoints-list)
Removes the rendered control points.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.debugging.removePathControlPoints()
:::
___

(debuggingremoveRenderedCameraPath-target)=
### [`removeRenderedCameraPath`](#debuggingremoveRenderedCameraPath-list)
Removes the currently rendered camera path if there is one.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.debugging.removeRenderedCameraPath()
:::
___

(debuggingrenderCameraPath-target)=
### [`renderCameraPath`](#debuggingrenderCameraPath-list)
Render the current camera path from the path navigation system. The first optional argument is the number of samples to take along the path (defaults to 100). If a second optional argument is included and set to true, a line indicating the camera view direction along the path will also be rendered. This can be useful when debugging camera orientations. Finally, the third optional argument can be used to set the length (in meter) of the view direction lines.


:::{card} Parameters


* nSteps `Integer?` - Default value: `100` 



* renderDirections `Boolean?` - Default value: `false` 



* directionLineLength `Number?` - Default value: `6e7` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.debugging.renderCameraPath(nSteps, renderDirections, directionLineLength)
:::
___

(debuggingrenderPathControlPoints-target)=
### [`renderPathControlPoints`](#debuggingrenderPathControlPoints-list)
Render the control points for the camera path spline as spheres. The optional argument can be used to set the radius of the created spheres.


:::{card} Parameters


* radius `Number?` - Default value: `2000000.0` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.debugging.renderPathControlPoints(radius)
:::

