



(core_navigation_state)=
# NavigationState

A NavigationState is an object describing an exact camera position and rotation, in a certain reference frame (per default, the one of the specified Anchor node). It can be used to set the same camera position at a later point in time, or navigating to a specific camera position using the pathnavigation system.

The camera rotation is specified using Euler angles, in radians. It is also possible to specify a node to be used as Aim, but note that this will not affect the actual camera position or view direction.

To get the current navigation state of the camera, use the `openspace.navigation.getNavigationState()` function in the Scripting API.

Note that when loading a NavigationState, the visuals may be different depending on what the simulation timestamp is, as the relative positions of objects in the scene may have changed. The get the exact same visuals as when the NavigationState was saved you need to also set the simulation time to correpsond to the timestamp.


## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Anchor`
    - The identifier of the anchor node
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Position`
    - The position of the camera relative to the anchor node, expressed in meters in the specified reference frame
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `Aim`
    - The identifier of the aim node, if used
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Pitch`
    - The pitch angle in radians. Positive angle means pitching camera upwards
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ReferenceFrame`
    - The identifier of the scene graph node to use as reference frame. If not specified, this will be the same as the anchor
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Timestamp`
    - The timestamp for when the navigation state was captured or is valid. Specified either as seconds past the J2000 epoch, or as a date string in ISO 8601 format: 'YYYY MM DD HH:mm:ss.xxx'
    - `Double, or String`
    
    - Value of type 'Double', or Value of type 'String' 
    
    - Yes
    
*   - `Up`
    - The up vector expressed in the coordinate system of the reference frame
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `Yaw`
    - The yaw angle in radians. Positive angle means yawing camera to the right
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::






















