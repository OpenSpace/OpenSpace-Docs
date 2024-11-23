# `openspace.pathnavigation`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`continuePath`](#pathnavigationcontinuePath-target)
    - [Continue playing a paused camera path]{#pathnavigationcontinuePath-list}


*   - [`createPath`](#pathnavigationcreatePath-target)
    - [Create a camera path as described by the instruction in the input argument]{#pathnavigationcreatePath-list}


*   - [`flyTo`](#pathnavigationflyTo-target)
    - [Move the camera to the node with the specified identifier]{#pathnavigationflyTo-list}


*   - [`flyToHeight`](#pathnavigationflyToHeight-target)
    - [Move the camera to the node with the specified identifier]{#pathnavigationflyToHeight-list}


*   - [`flyToNavigationState`](#pathnavigationflyToNavigationState-target)
    - [Create a path to the navigation state described by the input table]{#pathnavigationflyToNavigationState-list}


*   - [`isFlying`](#pathnavigationisFlying-target)
    - [Returns true if a camera path is currently running, and false otherwise]{#pathnavigationisFlying-list}


*   - [`jumpTo`](#pathnavigationjumpTo-target)
    - [Fade rendering to black, jump to the specified navigation state, and then fade in]{#pathnavigationjumpTo-list}


*   - [`jumpToNavigationState`](#pathnavigationjumpToNavigationState-target)
    - [Fade rendering to black, jump to the specified node, and then fade in]{#pathnavigationjumpToNavigationState-list}


*   - [`pausePath`](#pathnavigationpausePath-target)
    - [Pause a playing camera path]{#pathnavigationpausePath-list}


*   - [`skipToEnd`](#pathnavigationskipToEnd-target)
    - [Immediately skips to the end of the current camera path, if one is being played]{#pathnavigationskipToEnd-list}


*   - [`stopPath`](#pathnavigationstopPath-target)
    - [Stops a path, if one is being played]{#pathnavigationstopPath-list}


*   - [`zoomToDistance`](#pathnavigationzoomToDistance-target)
    - [Fly linearly to a specific distance in relation to the focus node]{#pathnavigationzoomToDistance-list}


*   - [`zoomToDistanceRelative`](#pathnavigationzoomToDistanceRelative-target)
    - [Fly linearly to a specific distance in relation to the focus node, given as a relative value based on the size of the object rather than in meters]{#pathnavigationzoomToDistanceRelative-list}


*   - [`zoomToFocus`](#pathnavigationzoomToFocus-target)
    - [Zoom linearly to the current focus node, using the default distance]{#pathnavigationzoomToFocus-list}

:::

## Functions

(pathnavigationcontinuePath-target)=
### [`continuePath`](#pathnavigationcontinuePath-list)
Continue playing a paused camera path.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.continuePath()
:::
___

(pathnavigationcreatePath-target)=
### [`createPath`](#pathnavigationcreatePath-list)
Create a camera path as described by the instruction in the input argument.


:::{card} Parameters


* pathInstruction `Table` 


    * A table representing a [PathInstruction](#core_path_instruction) that describes a camera path to be created
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.createPath(pathInstruction)
:::
___

(pathnavigationflyTo-target)=
### [`flyTo`](#pathnavigationflyTo-list)
Move the camera to the node with the specified identifier. The optional double specifies the duration of the motion, in seconds. If the optional bool is set to true the target up vector for camera is set based on the target node. Either of the optional parameters can be left out.


:::{card} Parameters


* nodeIdentifier `String` 



* useUpFromTargetOrDuration `Boolean | Number?` 



* duration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.flyTo(nodeIdentifier, useUpFromTargetOrDuration, duration)
:::
___

(pathnavigationflyToHeight-target)=
### [`flyToHeight`](#pathnavigationflyToHeight-list)
Move the camera to the node with the specified identifier. The second argument is the desired target height above the target node's bounding sphere, in meters. The optional double specifies the duration of the motion, in seconds. If the optional bool is set to true, the target up vector for camera is set based on the target node. Either of the optional parameters can be left out.


:::{card} Parameters


* nodeIdentifier `String` 



* height `Number` 



* useUpFromTargetOrDuration `Boolean | Number?` 



* duration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.flyToHeight(nodeIdentifier, height, useUpFromTargetOrDuration, duration)
:::
___

(pathnavigationflyToNavigationState-target)=
### [`flyToNavigationState`](#pathnavigationflyToNavigationState-list)
Create a path to the navigation state described by the input table. Note that roll must be included for the target up direction in the navigation state to be taken into account.


:::{card} Parameters


* navigationState `Table` 


    * A [NavigationState](#core_navigation_state) to fly to 

* duration `Number?` 


    * An optional duration for the motion to take, in seconds. For example, a value of 5 means \"fly to this position over a duration of 5 seconds\"
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.flyToNavigationState(navigationState, duration)
:::
___

(pathnavigationisFlying-target)=
### [`isFlying`](#pathnavigationisFlying-list)
Returns true if a camera path is currently running, and false otherwise.


Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.isFlying()
:::
___

(pathnavigationjumpTo-target)=
### [`jumpTo`](#pathnavigationjumpTo-list)
Fade rendering to black, jump to the specified navigation state, and then fade in. This is done by triggering another script that handles the logic.


:::{card} Parameters


* nodeIdentifier `String` 


    * The identifier of the scene graph node to jump to 

* fadeDuration `Number?` 


    * An optional duration for the fading. If not included, the property in Navigation Handler will be used
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.jumpTo(nodeIdentifier, fadeDuration)
:::
___

(pathnavigationjumpToNavigationState-target)=
### [`jumpToNavigationState`](#pathnavigationjumpToNavigationState-list)
Fade rendering to black, jump to the specified node, and then fade in. This is done by triggering another script that handles the logic.


:::{card} Parameters


* navigationState `Table` 


    * A [NavigationState](#core_navigation_state) to jump to 

* fadeDuration `Number?` 


    * An optional duration for the fading. If not included, the property in Navigation Handler will be used
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.jumpToNavigationState(navigationState, fadeDuration)
:::
___

(pathnavigationpausePath-target)=
### [`pausePath`](#pathnavigationpausePath-list)
Pause a playing camera path.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.pausePath()
:::
___

(pathnavigationskipToEnd-target)=
### [`skipToEnd`](#pathnavigationskipToEnd-list)
Immediately skips to the end of the current camera path, if one is being played.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.skipToEnd()
:::
___

(pathnavigationstopPath-target)=
### [`stopPath`](#pathnavigationstopPath-list)
Stops a path, if one is being played.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.stopPath()
:::
___

(pathnavigationzoomToDistance-target)=
### [`zoomToDistance`](#pathnavigationzoomToDistance-list)
Fly linearly to a specific distance in relation to the focus node.


:::{card} Parameters


* distance `Number` 


    * The distance to fly to, in meters above the bounding sphere. 

* duration `Number?` 


    * An optional duration for the motion to take, in seconds.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.zoomToDistance(distance, duration)
:::
___

(pathnavigationzoomToDistanceRelative-target)=
### [`zoomToDistanceRelative`](#pathnavigationzoomToDistanceRelative-list)
Fly linearly to a specific distance in relation to the focus node, given as a relative value based on the size of the object rather than in meters.


:::{card} Parameters


* distance `Number` 


    * The distance to fly to, given as a multiple of the bounding sphere of the current focus node bounding sphere. A value of 1 will result in a position at a distance of one times the size of the bounding sphere away from the object. 

* duration `Number?` 


    * An optional duration for the motion, in seconds.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.zoomToDistanceRelative(distance, duration)
:::
___

(pathnavigationzoomToFocus-target)=
### [`zoomToFocus`](#pathnavigationzoomToFocus-list)
Zoom linearly to the current focus node, using the default distance.


:::{card} Parameters


* duration `Number?` 


    * An optional duration for the motion to take, in seconds. For example, a value of 5 means \"zoom in over 5 seconds\"
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.pathnavigation.zoomToFocus(duration)
:::

