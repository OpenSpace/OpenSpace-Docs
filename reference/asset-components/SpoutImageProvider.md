



(spoutimageprovider-identifier )=
# SpoutImageProvider

_Inherits [TileProvider](#TileProvider)_











## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 9
local globe = asset.require("scene/solarsystem/planets/earth/earth")



local Layer = {
  Identifier = "TextureSpout",
  Enabled = asset.enabled,
  SpoutName = "SPOUT_TERRA_RECEIVER",
  Type = "SpoutImageProvider"
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(globe.Earth.Identifier, "ColorLayers", Layer)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(globe.Earth.Identifier, "ColorLayers", Layer)
end)

asset.export("layer", Layer)

:::
:::


