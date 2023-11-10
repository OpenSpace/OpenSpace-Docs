# Creating a Renderable Globe
The renderable globe is a type of OpenSpace renderable that can be used for all types of elliptically shaped celestial bodies such as planets, moons, and stars.

The lua table below shows a definition of a simple RenderableGlobe as a Renderable which can be set for a given scene graph node.

```lua
Renderable = {
    Type = "RenderableGlobe",
    Radii = {6378137.0, 6378137.0, 6378137.0}, -- Earth triaxial ellipsoid
    SegmentsPerPatch = 128, -- Number of segments in both s, and t directions of each patch
    Layers = {
        ColorLayers = {
            {
                Name = "SimpleTexture", -- Unique name
                Type = "DefaultTileLayer", -- Defaults to DefaultTileLayer if not set
                FilePath = "path/to/texture.jpg",
                Enabled = true, -- Defaults to false if not set
            },
        },
        NightLayers = { },
        WaterMasks = { },
        Overlays = { },
        HeightLayers = { },
    },
}
```

## Defining Layers
Let's look closer in to what properties can be set for each layer. In the above example, we created a simple layer and put it in the **ColorLayers** layer group. A layer is defined by a Lua table such as the mentioned example:
```lua
{
    Name = "SimpleTexture", -- Unique name
    Type = "DefaultTileLayer", -- Defaults to DefaultTileLayer if not set
    FilePath = "path/to/texture.jpg",
    Enabled = true, -- Defaults to false if not set
},
```
These layers can be put in to any of the layer groups, they will be interpreted differently for the rendering. Depending on the **Type** of the layer, some properties are different. First, let's look at the properties that are used for all layer types.

### None Type Dependent Properties
* **Name** -- A **string** defining the name of the layer. For each layer group and each layer, this must be unique.
* **Type** -- A **string** defining the layer type, must be any of the following: **DefaultTileLayer**, **SingleImageTileLayer**, **SizeReferenceTileLayer**, **TemporalTileLayer**, **TileIndexTileLayer**, **ByIndexTileLayer**, **ByLevelTileLayer**, **SolidColor**.
* **Enabled** (optional) -- A **boolean** value, **true** or **false**, determining if the layer is enabled or not.
* **TilePixelSize** (optional) -- An **integer** value specifying the size in pixels for each tile of the layer. Defaults to 64 for **HeightLayers** and 512 for all other layers.
* **Settings** (optional) -- A **lua table** specifying the render settings for the layer using settings for **Opacity**, **Gamma**, **Multiplier**, and **Offset**. As an example:
```lua
Settings = {
    Opacity = 1.0,
    Gamma = 1.5,
    Multiplier = 15.0,
    Offset = 0.0
},
```
* **Fallback** (optional) -- A fallback layer which will be used in case the reading of the actual layer definition failed for some reason. In case OpenSpace was not compiled with GDAL for example, all georeferenced map types will fail to read, then a simple non georeferenced image can be used as fallback.
* **Adjustment** (optional) -- A **Lua table** defining a layer adjustment.
    * **Type** -- A **string** defining the type of the layer adjustment. Can be any of **None**, **ChromaKey**, and **TransferFunction (to be implemented)**. Defaults to **None**.
    * **ChromaKeyColor** -- If the type is set to **ChromaKey**, this **Lua table** of three components defines the color of the chroma key.
    * **ChromaKeyTolerance** -- If the type is set to **ChromaKey**, this **float** value determines the tolerance of the chroma keying.
* **BlendMode** (optional) -- A **string** defining the blend mode of this layer. Can be any of **Normal**, **Multiply**, **Add**, **Subtract**, and **Color**. Defaults to **Normal**.
* **PadTiles** (optional) -- A **boolean** value used to determine if tiles should be padded or not. If false, tile edges may be more visible but tiles will generally load faster. If padding is enabled, extra pixels will be read along the edges of each tile which might lead to cache misses and extra read requests. Should be set to false if high spatial accuracy is not required but temporal resolution is more desirable, for example for temporal datasets. Defaults to true.

### Type Dependent Properties
* **DefaultTileLayer**
  * **FilePath** -- A **string** defining the path to a file storing the map dataset. It can either be a single local file such as a jpeg, png, or tiff image, a georeferenced file such as a geotiff, or a cube file. It can also be a path to a GDAL wms config for remote reading; finally it is also possible to specify the wms config directly as a string instead of loading a file from disc.
* **SingleImageTileLayer**
  * **FilePath** -- A **string** defining the path to a simple, non-georeferenced, image file such as a jpeg or a png.
* **SizeReferenceTileLayer**
  * **Radii** -- A triaxial ellipsoid in the form of a **Lua table**. It should be the same ellipsoid used for the RenderableGlobe. For example `Radii = {6378137.0, 6378137.0, 6378137.0}, -- Earth triaxial ellipsoid`.
* **TemporalTileLayer**
  * **FilePath** -- A **string** defining the path to an OpenSpace temporal tile dataset specification. It can also be a string defining the dataset directly.
* **ByIndexTileLayer**
  * **DefaultProvider** -- A layer definition in the form of a **Lua table** to be used for all indices where no other layer is specified (currently only works for tile layers).
  * **IndexTileProviders** -- A **Lua table** specifying a list of all layers to be used for specific tile indices.
    * **TileIndex** -- A **Lua table** defining a tile index by an x-index, y-index and level, such as `TileIndex = {X=0, Y=0, Level=2}`.
    * **TileProvider** -- The layer definition in the form of a **Lua table** to be used for this tile index (currently only works for tile layers).
  * **PadTiles** -- If PadTiles is set to false for this layer type, it needs to be set to false for all **IndexTileProviders** as well, otherwise padding will be assumed for rendering but not for reading. This causes inaccurate mapping which is visible as edge tearing between tiles.
* **ByLevelTileLayer**
  * **LevelTileProviders** -- A **Lua table** specifying a list of all layers to be used for specific tile levels.
    * **MaxLevel** -- An **integer** value defining a maximum level where this layer should be used.
    * **TileProvider** -- The layer definition in the form of a **Lua table** to be used for these tile levels (currently only works for tile layers).
  * **PadTiles** -- If PadTiles is set to false for this layer type, it needs to be set to false for all **LevelTileProviders** as well, otherwise padding will be assumed for rendering but not for reading. T his causes inaccurate mapping which is visible as edge tearing between tiles.
* **SolidColor**
  * **Color** -- A **vec3** defining a rgb color. For example `Color = {1, 0, 0} -- Red`.

## Layer Support Scripting
The functions `openspace.globebrowsing.createGibsGdalXml()` and `openspace.globebrowsing.createTemporalGibsGdalXml()` can be used to create a GDAL wms configuration for GIBS datasets: [https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers#GIBSAPIforDevelopers-Script-levelAccessviaGDAL](https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers#GIBSAPIforDevelopers-Script-levelAccessviaGDAL). This can then be used to create GIBS layers without the use of wms files. An example of one such layer is:
```lua
{
    Type = "TemporalTileLayer",
    Name = "GHRSST_L4_G1SST_Sea_Surface_Temperature",
    FilePath = openspace.globebrowsing.createTemporalGibsGdalXml(
        "GHRSST_L4_G1SST_Sea_Surface_Temperature",
        "2010-06-21",
        "Yesterday",
        "1d",
        "1km",
        "png")
}
```
See script documentation for more info.

## A Complex Example
Here is an example showing the use of many of the features mentioned above to create a layer used for a renderable globe:

```lua
{
    Name = "ESRI VIIRS Combo",
    Type = "ByLevelTileLayer",
    LevelTileProviders = {
        {
            MaxLevel = 3,
            TileProvider = {
                Name = "Temporal VIIRS SNPP",
                Type = "TemporalTileLayer",
                FilePath = openspace.globebrowsing.createTemporalGibsGdalXml(
                    "VIIRS_SNPP_CorrectedReflectance_TrueColor",
                    "2015-11-24",
                    "Yesterday",
                    "1d",
                    "250m",
                    "jpg"
                ),
                PadTiles = false,
            }
        },
        {
            MaxLevel = 22,
            TileProvider = {
                Name = "ESRI Imagery World 2D",
                FilePath = "map_service_configs/ESRI/ESRI_Imagery_World_2D.wms",
                PadTiles = false,
            }
        },
    },
    Enabled = true,
    PadTiles = false, -- Faster reading but visible tile edges
    Fallback = { -- Simple texture in case the default fails
        Name = "Blue Marble",
        FilePath = "textures/earth_bluemarble.jpg",
        Enabled = true,
    },
    Settings = { -- Just to show how settings can be set. These are default values
        Opacity = 1.0,
        Gamma = 1.0,
        Multiplier = 1.0,
        Offset = 0.0,
    },
}
```
