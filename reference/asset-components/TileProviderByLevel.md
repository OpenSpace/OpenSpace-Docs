



(globebrowsing_tileproviderbylevel)=
# TileProviderByLevel

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

*   - `LevelTileProviders`
    - 
    - `Table`
    
    -   [Table parameters](#TileProviderByLevelLevelTileProviders-target) 
    
    - {bdg-info}`No`
    
:::







(TileProviderByLevelLevelTileProviders-target)=
::::{dropdown} Table parameters for `LevelTileProviders`



* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    -   [Table parameters](#TileProviderByLevelLevelTileProviders*-target) 
    
    - Yes
    
:::



(TileProviderByLevelLevelTileProviders*-target)=
#### Table parameters for `*`



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

*   - `MaxLevel`
    - 
    - `Integer`
    
    - Greater or equal to: 0 
    
    - {bdg-info}`No`
    
*   - `TileProvider`
    - 
    - `Table`
    
    -  
    
    - {bdg-info}`No`
    
:::




::::




## Asset Examples


:::{dropdown} Basic

This example file adds two layers to a globe. The first layer being used is showing
a cloud layer and at higher levels a Blue Marble image is used instead. Recommended
reading for this example is the documentation on the
[DefaultTileProvider](#globebrowsing_defaulttileprovider).

:::{code-block} lua
:linenos:
:emphasize-lines: 12, 45

-- Download some example images that we can use
local images = asset.resource({
  Name = "Earth Textures",
  Type = "HttpSynchronization",
  Identifier = "earth_textures",
  Version = 3
})

-- Define the TileProvider
local TileProvider = {
  Identifier = "Example",
  Type = "TileProviderByLevel",
  Enabled = true,
  LevelTileProviders = {
    {
      -- Show only a cloud layer for the first 3 layers (2, 3, 4)
      MaxLevel = 4,
      TileProvider = {
        Identifier = "Blue_Marble_Clouds",
        FilePath = images .. "earth_clouds.jpg"
      }
    },
    {
      -- Then transition fade into the Blue Marble image representation
      MaxLevel = 22,
      TileProvider = {
        Identifier = "Blue_Marble",
        FilePath = images .. "earth_bluemarble.jpg"
      }
    }
  }
}

-- Define the scene graph node
local Node = {
  Identifier = "TileProviderByLevel_Example",
  Renderable = {
    Type = "RenderableGlobe",
    Layers = {
      -- The globe has exactly one layer, which is the one we defined above
      ColorLayers = { TileProvider }
    }
  },
  GUI = {
    Name = "TileProviderByLevel - Basic",
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


