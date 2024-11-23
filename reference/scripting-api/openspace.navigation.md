# `openspace.navigation`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addGlobalRoll`](#navigationaddGlobalRoll-target)
    - [Directly adds to the global roll of the camera]{#navigationaddGlobalRoll-list}


*   - [`addGlobalRotation`](#navigationaddGlobalRotation-target)
    - [Directly add to the global rotation of the camera (around the focus node)]{#navigationaddGlobalRotation-list}


*   - [`addLocalRoll`](#navigationaddLocalRoll-target)
    - [Directly adds to the local roll of the camera]{#navigationaddLocalRoll-list}


*   - [`addLocalRotation`](#navigationaddLocalRotation-target)
    - [Directly adds to the local rotation of the camera (around the camera's current position)]{#navigationaddLocalRotation-list}


*   - [`addTruckMovement`](#navigationaddTruckMovement-target)
    - [Directly adds to the truck movement of the camera]{#navigationaddTruckMovement-list}


*   - [`axisDeadzone`](#navigationaxisDeadzone-target)
    - [Returns the deadzone for the desired axis of the provided joystick]{#navigationaxisDeadzone-list}


*   - [`bindJoystickAxis`](#navigationbindJoystickAxis-target)
    - [Bind an axis of a joystick to be used as a certain type, and optionally define detailed settings for the axis]{#navigationbindJoystickAxis-list}


*   - [`bindJoystickAxisProperty`](#navigationbindJoystickAxisProperty-target)
    - [Binds an axis of a joystick to a numerical property value in OpenSpace]{#navigationbindJoystickAxisProperty-list}


*   - [`bindJoystickButton`](#navigationbindJoystickButton-target)
    - [Bind a Lua script to one of the buttons for a joystick]{#navigationbindJoystickButton-list}


*   - [`clearJoystickButton`](#navigationclearJoystickButton-target)
    - [Remove all commands that are currently bound to a button of a joystick or game controller]{#navigationclearJoystickButton-list}


*   - [`distanceToFocus`](#navigationdistanceToFocus-target)
    - [Return the distance to the current focus node]{#navigationdistanceToFocus-list}


*   - [`distanceToFocusBoundingSphere`](#navigationdistanceToFocusBoundingSphere-target)
    - [Return the distance to the current focus node's bounding sphere]{#navigationdistanceToFocusBoundingSphere-list}


*   - [`distanceToFocusInteractionSphere`](#navigationdistanceToFocusInteractionSphere-target)
    - [Return the distance to the current focus node's interaction sphere]{#navigationdistanceToFocusInteractionSphere-list}


*   - [`getNavigationState`](#navigationgetNavigationState-target)
    - [Return the current [NavigationState](#core_navigation_state) as a Lua table]{#navigationgetNavigationState-list}


*   - [`joystickAxis`](#navigationjoystickAxis-target)
    - [Return all the information bound to a certain joystick axis]{#navigationjoystickAxis-list}


*   - [`joystickButton`](#navigationjoystickButton-target)
    - [Get the Lua script that is currently bound to be executed when the provided button is pressed/triggered]{#navigationjoystickButton-list}


*   - [`listAllJoysticks`](#navigationlistAllJoysticks-target)
    - [Return the complete list of connected joysticks]{#navigationlistAllJoysticks-list}


*   - [`loadNavigationState`](#navigationloadNavigationState-target)
    - [Set the camera position by loading a [NavigationState](#core_navigation_state) from file]{#navigationloadNavigationState-list}


*   - [`retargetAim`](#navigationretargetAim-target)
    - [Reset the camera direction to point at the aim node]{#navigationretargetAim-list}


*   - [`retargetAnchor`](#navigationretargetAnchor-target)
    - [Reset the camera direction to point at the anchor node]{#navigationretargetAnchor-list}


*   - [`saveNavigationState`](#navigationsaveNavigationState-target)
    - [Save the current [NavigationState](#core_navigation_state) to a file with the path given by the first argument]{#navigationsaveNavigationState-list}


*   - [`setAxisDeadZone`](#navigationsetAxisDeadZone-target)
    - [Set the deadzone value for a particular joystick axis, which means that any input less than this value is completely ignored]{#navigationsetAxisDeadZone-list}


*   - [`setNavigationState`](#navigationsetNavigationState-target)
    - [Set the camera position from a provided [NavigationState](#core_navigation_state)]{#navigationsetNavigationState-list}


*   - [`targetNextInterestingAnchor`](#navigationtargetNextInterestingAnchor-target)
    - [Picks the next node from the interesting nodes out of the profile and selects that]{#navigationtargetNextInterestingAnchor-list}


*   - [`targetPreviousInterestingAnchor`](#navigationtargetPreviousInterestingAnchor-target)
    - [Picks the previous node from the interesting nodes out of the profile and selects that]{#navigationtargetPreviousInterestingAnchor-list}


*   - [`triggerIdleBehavior`](#navigationtriggerIdleBehavior-target)
    - [Immediately start applying the chosen IdleBehavior]{#navigationtriggerIdleBehavior-list}

:::

## Functions

(navigationaddGlobalRoll-target)=
### [`addGlobalRoll`](#navigationaddGlobalRoll-list)
Directly adds to the global roll of the camera. This is a rotation around the line between the focus node and the camera (not always the same as the camera view direction)


:::{card} Parameters


* value `Number` 


    * the value to add
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.addGlobalRoll(value)
:::
___

(navigationaddGlobalRotation-target)=
### [`addGlobalRotation`](#navigationaddGlobalRotation-list)
Directly add to the global rotation of the camera (around the focus node).


:::{card} Parameters


* xValue `Number` 


    * the value to add in the x-direction (a positive value rotates to the right and a negative value to the left) 

* yValue `Number` 


    * the value to add in the y-direction (a positive value rotates the focus upwards and a negative value downwards)
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.addGlobalRotation(xValue, yValue)
:::
___

(navigationaddLocalRoll-target)=
### [`addLocalRoll`](#navigationaddLocalRoll-list)
Directly adds to the local roll of the camera. This is the rotation around the camera's forward/view direction.


:::{card} Parameters


* value `Number` 


    * the value to add
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.addLocalRoll(value)
:::
___

(navigationaddLocalRotation-target)=
### [`addLocalRotation`](#navigationaddLocalRotation-list)
Directly adds to the local rotation of the camera (around the camera's current position).


:::{card} Parameters


* xValue `Number` 


    * the value to add in the x-direction (a positive value rotates to the left and a negative value to the right) 

* yValue `Number` 


    * the value to add in the y-direction (a positive value rotates the camera upwards and a negative value downwards)
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.addLocalRotation(xValue, yValue)
:::
___

(navigationaddTruckMovement-target)=
### [`addTruckMovement`](#navigationaddTruckMovement-list)
Directly adds to the truck movement of the camera. This is the movement along the line from the camera to the focus node.

A positive value moves the camera closer to the focus, and a negative value moves the camera further away.


:::{card} Parameters


* value `Number` 


    * the value to add
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.addTruckMovement(value)
:::
___

(navigationaxisDeadzone-target)=
### [`axisDeadzone`](#navigationaxisDeadzone-list)
Returns the deadzone for the desired axis of the provided joystick.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller which information should be returned 

* axis `Integer` 


    * the joystick axis for which to get the deadzone value


:::

Return type: `Number`  the deadzone value

:::{code-block} lua
:caption: Signature
openspace.navigation.axisDeadzone(joystickName, axis)
:::
___

(navigationbindJoystickAxis-target)=
### [`bindJoystickAxis`](#navigationbindJoystickAxis-list)
Bind an axis of a joystick to be used as a certain type, and optionally define detailed settings for the axis.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller that should be bound 

* axis `Integer` 


    * the axis of the joystick that should be bound 

* axisType `String` 


    * the type of movement that the axis should be mapped to 

* shouldInvert `Boolean?` - Default value: `false` 


    * decides if the joystick axis movement should be inverted or not 

* joystickType `String?` - Default value: `"JoystickLike"` 


    * what type of joystick or axis this is. Decides if the joystick behaves more like a joystick or a trigger. Either `\"JoystickLike\"` or `\"TriggerLike\"`, where `\"JoystickLike\"` is default 

* isSticky `Boolean?` - Default value: `false` 


    * if true, the value is calculated relative to the previous value. If false, the value is used as is 

* shouldFlip `Boolean?` - Default value: `false` 


    * reverses the movement of the camera that the joystick produces 

* sensitivity `Number?` - Default value: `0.0` 


    * sensitivity for this axis, in addition to the global sensitivity
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.bindJoystickAxis(joystickName, axis, axisType, shouldInvert, joystickType, isSticky, shouldFlip, sensitivity)
:::
___

(navigationbindJoystickAxisProperty-target)=
### [`bindJoystickAxisProperty`](#navigationbindJoystickAxisProperty-list)
Binds an axis of a joystick to a numerical property value in OpenSpace. This means that interacting with the joystick will change the property value, within a given min-max range.

The axis value will be rescaled from [-1, 1] to the provided [min, max] range (default is [0, 1]).


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller that should be bound 

* axis `Integer` 


    * the axis of the joystick that should be bound 

* propertyUri `String` 


    * the identifier (URI) of the property that this joystick axis should modify 

* min `Number?` - Default value: `0.f` 


    * the minimum value that this axis can set for the property 

* max `Number?` - Default value: `1.f` 


    * the maximum value that this axis can set for the property 

* shouldInvert `Boolean?` - Default value: `false` 


    * if the joystick movement should be inverted or not 

* isRemote `Boolean?` - Default value: `true` 


    * if true, the property change will also be executed on connected nodes. If false, the property change will only affect the master node
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.bindJoystickAxisProperty(joystickName, axis, propertyUri, min, max, shouldInvert, isRemote)
:::
___

(navigationbindJoystickButton-target)=
### [`bindJoystickButton`](#navigationbindJoystickButton-list)
Bind a Lua script to one of the buttons for a joystick.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller 

* button `Integer` 


    * the button to which to bind the script 

* command `String` 


    * the script that should be executed on button trigger 

* documentation `String` 


    * the documentation for the provided script/command 

* action `String?` - Default value: `"Press"` 


    * the action for when the script should be executed. This defaults to `\"Press\"`, which means that the script is run when the user presses the button. Alternatives are `\"Idle\"` (if the button is unpressed and has been unpressed since the last frame), `\"Repeat\"` (if the button has been pressed since longer than the last frame), and `\"Release\"` (if the button was released since the last frame) 

* isRemote `Boolean?` - Default value: `true` 


    * a value saying whether the command is going to be executable locally or remotely, where the latter is the default
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.bindJoystickButton(joystickName, button, command, documentation, action, isRemote)
:::
___

(navigationclearJoystickButton-target)=
### [`clearJoystickButton`](#navigationclearJoystickButton-list)
Remove all commands that are currently bound to a button of a joystick or game controller


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller 

* button `Integer` 


    * the button for which to clear the commands
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.clearJoystickButton(joystickName, button)
:::
___

(navigationdistanceToFocus-target)=
### [`distanceToFocus`](#navigationdistanceToFocus-list)
Return the distance to the current focus node.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.navigation.distanceToFocus()
:::
___

(navigationdistanceToFocusBoundingSphere-target)=
### [`distanceToFocusBoundingSphere`](#navigationdistanceToFocusBoundingSphere-list)
Return the distance to the current focus node's bounding sphere.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.navigation.distanceToFocusBoundingSphere()
:::
___

(navigationdistanceToFocusInteractionSphere-target)=
### [`distanceToFocusInteractionSphere`](#navigationdistanceToFocusInteractionSphere-list)
Return the distance to the current focus node's interaction sphere.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.navigation.distanceToFocusInteractionSphere()
:::
___

(navigationgetNavigationState-target)=
### [`getNavigationState`](#navigationgetNavigationState-list)
Return the current [NavigationState](#core_navigation_state) as a Lua table.

By default, the reference frame will be picked based on whether the orbital navigator is currently following the anchor node rotation. If it is, the anchor will be chosen as reference frame. If not, the reference frame will be set to the scene graph root.


:::{card} Parameters


* frame `String?` 


    * the identifier of an optional scene graph node to use as reference frame for the NavigationState


:::

Return type: `Table`  a Lua table representing the current NavigationState of the camera

:::{code-block} lua
:caption: Signature
openspace.navigation.getNavigationState(frame)
:::
___

(navigationjoystickAxis-target)=
### [`joystickAxis`](#navigationjoystickAxis-list)
Return all the information bound to a certain joystick axis.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller with the axis for which to find the information 

* axis `Integer` 


    * the joystick axis for which to find the information


:::

Return type: `Table`  an object with information about the joystick axis

:::{code-block} lua
:caption: Signature
openspace.navigation.joystickAxis(joystickName, axis)
:::
___

(navigationjoystickButton-target)=
### [`joystickButton`](#navigationjoystickButton-list)
Get the Lua script that is currently bound to be executed when the provided button is pressed/triggered.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller 

* button `Integer` 


    * the button for which to get the command


:::

Return type: `String`  the currently bound Lua script

:::{code-block} lua
:caption: Signature
openspace.navigation.joystickButton(joystickName, button)
:::
___

(navigationlistAllJoysticks-target)=
### [`listAllJoysticks`](#navigationlistAllJoysticks-list)
Return the complete list of connected joysticks.


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.navigation.listAllJoysticks()
:::
___

(navigationloadNavigationState-target)=
### [`loadNavigationState`](#navigationloadNavigationState-list)
Set the camera position by loading a [NavigationState](#core_navigation_state) from file. The file should be in json format, such as the output files of `saveNavigationState`.


:::{card} Parameters


* filePath `String` 


    * the path to the file, including the file name (and extension, if it is anything other than `.navstate`) 

* useTimeStamp `Boolean?` - Default value: `false` 


    * if true, and the provided NavigationState includes a timestamp, the time will be set as well.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.loadNavigationState(filePath, useTimeStamp)
:::
___

(navigationretargetAim-target)=
### [`retargetAim`](#navigationretargetAim-list)
Reset the camera direction to point at the aim node.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.retargetAim()
:::
___

(navigationretargetAnchor-target)=
### [`retargetAnchor`](#navigationretargetAnchor-list)
Reset the camera direction to point at the anchor node.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.retargetAnchor()
:::
___

(navigationsaveNavigationState-target)=
### [`saveNavigationState`](#navigationsaveNavigationState-list)
Save the current [NavigationState](#core_navigation_state) to a file with the path given by the first argument.

By default, the reference frame will be picked based on whether the orbital navigator is currently following the anchor node rotation. If it is, the anchor will be chosen as reference frame. If not, the reference frame will be set to the scene graph root.


:::{card} Parameters


* path `String` 


    * the file path for where to save the NavigationState, including the file name. If no extension is added, the file is saved as a `.navstate` file. 

* frame `String?` - Default value: `""` 


    * the identifier of the scene graph node which coordinate system should be used as a reference frame for the NavigationState.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.saveNavigationState(path, frame)
:::
___

(navigationsetAxisDeadZone-target)=
### [`setAxisDeadZone`](#navigationsetAxisDeadZone-list)
Set the deadzone value for a particular joystick axis, which means that any input less than this value is completely ignored.


:::{card} Parameters


* joystickName `String` 


    * the name for the joystick or game controller 

* axis `Integer` 


    * the joystick axis for which to set the deadzone 

* deadzone `Number` 


    * the new deadzone value
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.setAxisDeadZone(joystickName, axis, deadzone)
:::
___

(navigationsetNavigationState-target)=
### [`setNavigationState`](#navigationsetNavigationState-list)
Set the camera position from a provided [NavigationState](#core_navigation_state).


:::{card} Parameters


* navigationState `Table` 


    * a table describing the NavigationState to set 

* useTimeStamp `Boolean?` - Default value: `false` 


    * if true, and the provided NavigationState includes a timestamp, the time will be set as well
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.setNavigationState(navigationState, useTimeStamp)
:::
___

(navigationtargetNextInterestingAnchor-target)=
### [`targetNextInterestingAnchor`](#navigationtargetNextInterestingAnchor-list)
Picks the next node from the interesting nodes out of the profile and selects that. If the current anchor is not an interesting node, the first node in the list will be selected.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.targetNextInterestingAnchor()
:::
___

(navigationtargetPreviousInterestingAnchor-target)=
### [`targetPreviousInterestingAnchor`](#navigationtargetPreviousInterestingAnchor-list)
Picks the previous node from the interesting nodes out of the profile and selects that. If the current anchor is not an interesting node, the first node in the list will be selected.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.targetPreviousInterestingAnchor()
:::
___

(navigationtriggerIdleBehavior-target)=
### [`triggerIdleBehavior`](#navigationtriggerIdleBehavior-list)
Immediately start applying the chosen IdleBehavior. If none is specified, use the one set to default in the OrbitalNavigator.


:::{card} Parameters


* choice `String?` - Default value: `""` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.navigation.triggerIdleBehavior(choice)
:::

