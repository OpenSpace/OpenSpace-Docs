



(core_scene_node)=
# SceneGraphNode




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

*   - `Identifier`
    - The identifier of this scene graph node. This name must be unique among all scene graph nodes that are loaded in a specific scene. If a duplicate is detected the loading of the node will fail, as will all childing that depend on the node.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `ApproachFactor`
    - This value is a multiplication factor for the interaction sphere that determines when the camera is 'approaching' the scene graph node. If this value is not specified, a default value of 5 is used instead. This value must be larger than the reachFactor or unexpected things might happen
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `BoundingSphere`
    - The bounding sphere of the scene graph node meaning that everything that this scene graph node renders must be contained within this sphere. This value is only used as an override to the bounding sphere calculated by the Renderable, if present. If this value is -1, the Renderable's computed bounding sphere is used.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `GUI`
    - Additional information that is passed to GUI applications. These are all hints and do not have any impact on the actual function of the scene graph node
    - `Table`
    
    -   [Table parameters](#SceneGraphNodeGUI-target) 
    
    - Yes
    
*   - `InteractionSphere`
    - The minimum radius that the camera is allowed to get close to this scene graph node. This value is only used as an override to the bounding sphere calculated by the Renderable, if present. If this value is -1, the Renderable's computed interaction sphere is used.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `OnApproach`
    - One or multiple actions that are executed whenever the camera is focused on this scene graph node and if it enters the interaction sphere of the node
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `OnExit`
    - One or multiple actions that are executed whenever the camera is focused on this scene graph node and if it exits the interaction sphere of the node
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `OnReach`
    - One or multiple actions that are executed whenever the camera is focused on this scene graph node and if it transitions from the approach distance to the reach distance of the node
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `OnRecede`
    - One or multiple actions that are executed whenever the camera is focused on this scene graph node and if it transitions from the reach distance to the approach distance of the node
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `Parent`
    - This names the parent of the currently specified scene graph node. The parent must already exist in the scene graph. If not specified, the node will be attached to the root of the scene graph
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - Yes
    
*   - `ReachFactor`
    - This value is a multiplication factor for the interaction sphere that determines when the camera has 'reached' the scene graph node. If this value is not specified, a default value of 1.25 is used instead. This value must be smaller than the approachFactor or unexpected things might happen
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `Renderable`
    - The renderable that is to be created for this scene graph node. A renderable is a component of a scene graph node that will lead to some visual result on the screen. The specifics heavily depend on the 'Type' of the renderable. If no Renderable is specified, this scene graph node is an internal node and can be used for either group children, or apply common transformations to a group of children
    - `Table`
    
    - [Renderable](#renderable)
    
    - Yes
    
*   - `SupportsDirectInteraction`
    - Only relevant when using touch interaction. If true, the 'direct manipulation' scheme will be used when interacting with this scene graph node, meaning that the positions on the interaction sphere that intersects with the touch points will directly follow the motion of the touch points. Works best for objects that have an interaction sphere of about the same size as the bounding sphere, and that are somewhat spherical. Note that using this feature might significalty reduce the performance.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Tag`
    - A tag or list of tags that can be used to reference to a group of scene graph nodes.
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `TimeFrame`
    - Specifies the time frame for when this node should be active
    - `Table`
    
    - [TimeFrame](#core_time_frame)
    
    - Yes
    
*   - `Transform`
    - This describes a set of transformations that are applied to this scene graph node and all of its children. There are only three possible values corresponding to a 'Translation', a 'Rotation', and a 'Scale'
    - `Table`
    
    -   [Table parameters](#SceneGraphNodeTransform-target) 
    
    - Yes
    
:::













(SceneGraphNodeGUI-target)=
::::{dropdown} Table parameters for `GUI`
Additional information that is passed to GUI applications. These are all hints and do not have any impact on the actual function of the scene graph node


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Description`
    - A user-facing description about this scene graph node
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Hidden`
    - If this value is specified, GUI applications are incouraged to ignore this scene graph node. This is most useful to trim collective lists of nodes and not display, for example, barycenters
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Name`
    - An optional user-facing name for this SceneGraphNode, which does not have to be unique, though it is recommended, and can contain any characters
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Path`
    - If this value is specified, this '/' separated URI specifies the location of this scene graph node in a GUI representation, for instance '/SolarSystem/Earth/Moon'
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::


























(SceneGraphNodeTransform-target)=
::::{dropdown} Table parameters for `Transform`
This describes a set of transformations that are applied to this scene graph node and all of its children. There are only three possible values corresponding to a 'Translation', a 'Rotation', and a 'Scale'


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Rotation`
    - This nodes describes a rotation that is applied to the scene graph node and all its children. Depending on the 'Type' of the rotation, this can either be a static rotation or a time-varying one
    - `Table`
    
    - [Rotation](#core_transform_rotation)
    
    - Yes
    
*   - `Scale`
    - This node describes a scaling that is applied to the scene graph node and all its children. Depending on the 'Type' of the scaling, this can either be a static scaling or a time-varying one
    - `Table`
    
    - [Scale](#core_transform_scaling)
    
    - Yes
    
*   - `Translation`
    - This node describes a translation that is applied to the scene graph node and all its children. Depending on the 'Type' of the translation, this can either be a static translation or a time-varying one
    - `Table`
    
    - [Translation](#core_transform_translation)
    
    - Yes
    
:::



::::



