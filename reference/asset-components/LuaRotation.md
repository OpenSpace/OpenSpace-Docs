



(base_transform_rotation_lua)=
# LuaRotation

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

*   - `Script`
    - This value is the path to the Lua script that will be executed to compute the rotation for this transformation. The script needs to define a function 'rotation' that takes the current simulation time in seconds past the J2000 epoch as the first argument, the simulation time in seconds past the J2000 epoch of the last frame as the second argument, and the current wall time as milliseconds past the J2000 epoch as the third argument. It computes the rotation value factors returned as a table containing the 9 values that make up the resulting rotation matrix.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
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

This asset creates a SceneGraphNode that only displays coordinate axes. The rotation of
coordinate axes are determined by executing a Lua file that returns the rotation matrix
to be used.
```{literalinclude}  /reference/asset_examples/data/assets/examples/rotation/luarotation/example.lua
:language: lua
:caption: The script file that is used in this example
```

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "LuaRotation_Example",
  Transform = {
    Rotation = {
      Type = "LuaRotation",
      Script = asset.resource("example.lua")
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "LuaRotation - Basic",
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


