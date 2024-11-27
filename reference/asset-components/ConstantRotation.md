



(base_transform_rotation_constant)=
# ConstantRotation

_Inherits [Rotation](#core_transform_rotation)_




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

*   - `RotationAxis`
    - This value is the rotation axis around which the object will rotate.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `RotationRate`
    - This value determines the number of revolutions per in-game second.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



### Inherited members from [Rotation](#core_transform_rotation)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - The type of the rotation that is described in this element. The available types of rotations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Rotation type 
    
    - {bdg-info}`No`
    
:::










## Asset Examples


:::{dropdown} Basic

This asset applies a rotation to a set of coordinate axes that makes them rotate at a 
constant rate of one revolution around the z-axis every 2 seconds.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 14

local Node = {
  Identifier = "ConstantRotation_Example",
  Transform = {
    Rotation = {
      Type = "ConstantRotation",
      RotationAxis = { 0.0, 0.0, 1.0 },
      RotationRate = 0.5
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "ConstantRotation - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::


