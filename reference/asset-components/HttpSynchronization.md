



(http_synchronization)=
# HttpSynchronization

_Inherits [ResourceSynchronization](#ResourceSynchronization)_




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
    - The unique identifier for this resource that is used to request a set of files from the synchronization servers
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Version`
    - The version of this resource that should be requested
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `UnzipFiles`
    - Determines whether .zip files that are downloaded should automatically be unzipped. If this value is not specified, no unzipping is performed
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UnzipFilesDestination`
    - The destination for the unzipping. If this value is specified, all zip files contained in the synchronization will be unzipped into the same specified folder. If this value is specified, but 'unzipFiles' is false, no extaction will be performed
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 8
-- Basic
-- This example loads a model.

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",
  },
  GUI = {
    Name = "RenderableModel - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::


