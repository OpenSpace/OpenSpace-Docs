



(base_transform_translation_lua)=
# LuaTranslation

_Inherits [Translation](#core_transform_translation)_




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
    - This value is the path to the Lua script that will be executed to compute the translation for this transformation. The script needs to define a function 'translation' that takes the current simulation time in seconds past the J2000 epoch as the first argument, the simulation time in seconds past the J2000 epoch of the last frame as the second argument, and the current wall time as milliseconds past the J2000 epoch the third argument and computes the three translation values returned as a table.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [Translation](#core_transform_translation)

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
    - The type of translation that is described in this element. The available types of translations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Translation type 
    
    - {bdg-info}`No`
    
:::








## Asset Examples


:::{dropdown} Basic

This asset creates a SceneGraphNode that only displays coordinate axes. The coordinate
axes are translated by a value determined by executing a Lua file that returns the
translation parameters to be used as a table. In order to see the translation, we need
to also have a node that does not move so that we can see the relative movement.
```{literalinclude}  /reference/asset_examples/data/assets/examples/translation/luatranslation/example.lua
:language: lua
:caption: The script file that is used in this example
```

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 14, 22

local NodeFocus = {
  Identifier = "LuaTranslation_Example_Focus",
  GUI = {
    Name = "Basic (Focus)",
    Path = "/Examples/LuaTranslation"
  }
}

local Node = {
  Identifier = "LuaTranslation_Example",
  Parent = NodeFocus.Identifier,
  Transform = {
    Translation = {
      Type = "LuaTranslation",
      Script = asset.resource("example.lua")
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "LuaTranslation - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(NodeFocus)
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
  openspace.removeSceneGraphNode(NodeFocus)
end)

:::
:::


