



(globebrowsing_tileindextileprovider)=
# TileIndexTileProvider

_Inherits [TileProvider](#TileProvider)_




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

*   - `UniqueBackgroundColors`
    - If 'true' each index tile will have a unique background color assigned to it.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::









## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 7
local globe = asset.require("../../mars")



local Layer = {
  Identifier = "Indices",
  Type = "TileIndexTileProvider",
  Enabled = asset.enabled
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(globe.Mars.Identifier, "Overlays", Layer)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(globe.Mars.Identifier, "Overlays", Layer)
end)

asset.export("layer", Layer)



asset.meta = {
  Name = "Mars Indices",
  Description = "This asset supplies a tile index layer for the Mars globe",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


