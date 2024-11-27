



(globebrowsing_imagesequencetileprovider)=
# ImageSequenceTileProvider

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

*   - `FolderPath`
    - The path that is used to look for images for this image provider. The path must point to an existing folder that contains images.
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
*   - `Index`
    - The index into the list of images that is used to pick the currently displayed image.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
:::











## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 26
local globe = asset.require("../../earth")



local Name = "Land to Sea Ratio"
local Identifier = "noaa-sos-land-land_ratio"
local Description = [[In this dataset, we witness the world map transform into a graph
that shows the ratio of land and sea at different latitudes]]
local URL = "https://sos.noaa.gov/catalog/datasets/land-to-sea-ratio/"


local syncedDirectory = asset.resource({
  Name = Name,
  Type = "HttpSynchronization",
  Identifier = Identifier,
  Version = 1,
  UnzipFiles = true
})


local Layer = {
  Identifier = Identifier,
  Name = Name,
  Enabled = asset.enabled,
  ZIndex = 100,
  Type = "ImageSequenceTileProvider",
  FolderPath = syncedDirectory .. "4096",
  Description = Description
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(globe.Earth.Identifier, "ColorLayers", Layer)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(globe.Earth.Identifier, "ColorLayers", Layer)
end)

asset.export(Layer)



asset.meta = {
  Name = Name,
  Description = Description .. "Data provided by the National Oceanic and Atmospheric Administration",
  Author = "National Oceanic and Atmospheric Administration",
  URL = URL,
  License = "https://sos.noaa.gov/copyright/"
}

:::
:::


