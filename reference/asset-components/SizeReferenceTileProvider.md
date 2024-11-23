



(globebrowsing_sizereferencetileprovider)=
# SizeReferenceTileProvider

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

*   - `Radii`
    - 
    - `Vector3<double>, or Double`
    
    - Value of type 'Vector3<double>', or Value of type 'Double' 
    
    - Yes
    
:::









## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 9
local globe = asset.require("../../moon")



local Layer = {
  Identifier = "Size_Reference",
  Name = "Size Reference",
  Enabled = asset.enabled,
  Type = "SizeReferenceTileProvider",
  Radii = globe.Moon.Renderable.Radii
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(globe.Moon.Identifier, "Overlays", Layer)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(globe.Moon.Identifier, "Overlays", Layer)
end)

asset.export("layer", Layer)



asset.meta = {
  Name = "Moon Size Reference",
  Description = "Size reference layer for Moon globe",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


