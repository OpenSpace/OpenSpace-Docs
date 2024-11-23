



(base_scale_lua)=
# LuaScale

_Inherits [Scale](#core_transform_scaling)_




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
    - This value is the path to the Lua script that will be executed to compute the scaling factor for this transformation. The script needs to define a function 'scale' that takes the current simulation time in seconds past the J2000 epoch as the first argument, the simulation time in seconds past the J2000 epoch of the last frame as the second argument, and the current wall time as milliseconds past the J2000 epoch the third argument and computes the three scaling factors returned as a table.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [Scale](#core_transform_scaling)

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
    - The type of the scaling that is described in this element. The available types of scaling depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Scale type 
    
    - {bdg-info}`No`
    
:::








## Asset Examples


:::{dropdown} Basic

This asset creates a SceneGraphNode that only displays coordinate axes. The sizes of
coordinate axes are determined by executing a Lua file that returns the scaling
parameters to be used as a table.
```{literalinclude}  /reference/asset_examples/data/assets/examples/scale/luascale/example.lua
:language: lua
:caption: The script file that is used in this example
```

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "LuaScale_Example",
  Transform = {
    Scale = {
      Type = "LuaScale",
      Script = asset.resource("example.lua")
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "LuaScale - Basic",
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


