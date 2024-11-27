



(core_path_instruction)=
# PathInstruction

A PathInstruction is a table describing the specification for a camera path. It is used as an input to the `openspace.pathnavigation.createPath` function.

There are two types of paths that can be created, as specified by the required TargetType parameter: 'Node' or 'NavigationState'. The difference is what kind of target the path is created for, a scene graph node or a specific navigation state for the camera.

Depending on the type, the parameters that can be specified are a bit different. A 'NavigationState' already contains all details for the camera position, so no other details may be specified. For a 'Node' instruction, only a 'Target' node is required, but a 'Height' or 'Position' may also be specified. If both a position and height is specified, the height value will be ignored.

For 'Node' paths it is also possible to specify whether the target camera state at the end of the flight should take the up direction of the target node into account. Note that for this to give an effect on the path, rolling motions have to be enabled.


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

*   - `TargetType`
    - 
    - `String`
    
    - In list { Node, NavigationState } 
    
    - {bdg-info}`No`
    
*   - `Duration`
    - The desired duration traversing the specified path segment should take
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Height`
    - (Node): An optional height in relation to the target node, in meters
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `NavigationState`
    - (NavigationState): A navigation state that will be the target of the resulting path
    - `Table`
    
    - [NavigationState](#core_navigation_state)
    
    - Yes
    
*   - `PathType`
    - The type of the created path. Affects the shape of the resulting path
    - `String`
    
    - In list { AvoidCollision, ZoomOutOverview, Linear, AvoidCollisionWithLookAt } 
    
    - Yes
    
*   - `Position`
    - (Node): An optional position in relation to the target node, in model coordinates (meters)
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `StartState`
    - A navigation state that determines the start state for the camera path
    - `Table`
    
    - [NavigationState](#core_navigation_state)
    
    - Yes
    
*   - `Target`
    - (Node): The target node of the camera path. Not optional for 'Node' type instructions
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `UseTargetUpDirection`
    - (Node): If true, the up direction of the node is taken into account when computing the wayopoint for this instruction
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::
























