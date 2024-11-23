



(globebrowsing_tileproviderbyindex)=
# TileProviderByIndex

_Inherits [TileProvider](#TileProvider)_

This TileProvider provides the ability to override the contents for tiles at specific indices. A default tile provider has to be specified that is used by default for the entire globe. If a tile provider is specified for a specific tile, then the default tile provide is used for all other indices and the specialized tile provider `P` is used for the specified index. Any number of specialized tile providers can be provided to overwrite specific locations on the globe.

This tile provider can be used to, for example, show an inset image that is merged with a larger globe-spanning image.


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

*   - `DefaultTileProvider`
    - 
    - `Table`
    
    - [Layer](#globebrowsing_layer)
    
    - {bdg-info}`No`
    
*   - `TileProviders`
    - The list of all TileProviders and the indices at which they are used.
    - `Table`
    
    -   [Table parameters](#TileProviderByIndexTileProviders-target) 
    
    - {bdg-info}`No`
    
:::









(TileProviderByIndexTileProviders-target)=
::::{dropdown} Table parameters for `TileProviders`
The list of all TileProviders and the indices at which they are used.


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
    - An IndexProvider is a tile provider that is only valid for a specific combination of x, y, and level. Whenever a globe tries to render a tile and this tile provider has an IndexProvider of that index, it will use the specialized tile provider instead.
    - `Table`
    
    -   [Table parameters](#TileProviderByIndexTileProviders*-target) 
    
    - Yes
    
:::



(TileProviderByIndexTileProviders*-target)=
#### Table parameters for `*`
An IndexProvider is a tile provider that is only valid for a specific combination of x, y, and level. Whenever a globe tries to render a tile and this tile provider has an IndexProvider of that index, it will use the specialized tile provider instead.


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

*   - `Index`
    - The index for which the provided tile provider is used.
    - `Table`
    
    -   [Table parameters](#TileProviderByIndex*Index-target) 
    
    - {bdg-info}`No`
    
*   - `TileProvider`
    - The dictionary that describes the TileProvider to be used by the provided `index`.
    - `Table`
    
    - [Layer](#globebrowsing_layer)
    
    - {bdg-info}`No`
    
:::



(TileProviderByIndex*Index-target)=
#### Table parameters for `Index`
The index for which the provided tile provider is used.


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

*   - `Level`
    - The z-level which corresponds to the depth of the tile pyramid, which directly impacts the applied resolution of the tileprovider shown here. Not that _in general_ the level would start at 2.
    - `Integer`
    
    - In range: ( 0,23 ) 
    
    - {bdg-info}`No`
    
*   - `X`
    - The x coordinate for this index. This specifies the horizontal direction (longitude) component. Acceptable values for this coordinate have to be smaller than $2 * 2^{level}$.
    - `Integer`
    
    - Greater or equal to: 0 
    
    - {bdg-info}`No`
    
*   - `Y`
    - The y coordinate for this index. This specifies the vertical direction (latitude) component. Acceptable values for this coordinate have to be smaller than $2^{level}$.
    - `Integer`
    
    - Greater or equal to: 0 
    
    - {bdg-info}`No`
    
:::





::::




## Asset Examples


:::{dropdown} Basic

This example file adds a layer to a globe that has a base layer and then replaces one
hemisphere of the planet with a single image. Recommended reading for this example is
the documentation on the DefaultTileProvider.

:::{code-block} lua
:linenos:
:emphasize-lines: 12, 43

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
  Type = "TileProviderByIndex",
  Enabled = true,
  -- The default tile provider that is used for the whole globe
  DefaultTileProvider = {
    Identifier = "Blue_Marble",
    FilePath = images .. "earth_bluemarble.jpg"
  },
  TileProviders = {
    -- We only define one additional tile provider that overwrites the right
    -- hemisphere of the globe
    {
      Index = { X = 0, Y = 0, Level = 2 },
      TileProvider = {
        Identifier = "Blue_Marble_Night",
        FilePath = images .. "earth_night.png"
      }
    }
  }
}

-- Define the scene graph node
local Node = {
  Identifier = "TileProviderByIndex_Example",
  Renderable = {
    Type = "RenderableGlobe",
    Layers = {
      -- The globe has exactly one layer, which is the one we defined above
      ColorLayers = { TileProvider }
    }
  },
  GUI = {
    Name = "TileProviderByIndex - Basic",
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


