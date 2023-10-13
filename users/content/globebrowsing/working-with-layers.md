# Working With Layers
This page goes through how to work with layers on a high level.  For more detail on how to create layers to be loaded or to add layers to globes see [Creating a Renderable Globe]({{ site.url }}/docs/builders/globebrowsing/creating-a-renderableglobe) and [Readable Datasets]({{ site.url }}/docs/builders/globebrowsing/readable-datasets).

## Layer Groups
There are five layer groups that are used for different purposes:
- **HeightLayers** -- Elevation maps used to offset the terrain of the globe. These layers are single-channeled.
- **ColorLayers** -- Sets the texture of the globe before shading.
- **Overlays** -- Sets the texture of the globe after shading is performed.
- **NightLayers** -- Visible only on the night side of the globe. Mainly useful for adding city lights to Earth.
- **WaterMasks** -- Used as reflectance maps to reflect the light from the sun.

Each layer group can contain many layers which have their own separate properties.  These layers are stacked top to bottom and will blend together to produce the final globe image.  For each layer group it is possible to enable or disable **level blending**, this aids in avoiding popping artifacts when switching between levels.

## Layer Types
Each layer has a fixed type:
- **DefaultTileLayer** -- One image dataset covering the full geographic extent of the globe.
- **SingleImageTileLayer** -- One image used for every individual tile.
- **SizeReferenceTileLayer** -- Size reference which shows the latitudinal length of every tile in kilometers and meters.
- **TemporalTileLayer** -- Time-varying dataset which opens a new image dataset for each time interval defined for the layer.  For example, a temporal version of the VIIRS corrected reflectance dataset of Earth can be used to show the reflectance for each day. The dataset is updated when scrubbing through the global OpenSpace time.
- **TileIndexTileLayer** -- Displays the tile index (chunk index) of every chunk. Mainly used for debugging.
- **ByIndexTileLayer** -- Shows specific tile layers only at specific tile indices.
- **ByLevelTileLayer** -- One or more image datasets bound by given maximum levels.  Having different datasets for different levels makes it possible to, for example, have a cloud-covered layer for Earth at low levels and replace it with a clear image layer for higher levels.
- **SolidColor** -- This layer type does not make use of tiles.  A solid color defines the resulting color.

## Tile Provider
The tile providers provide an interface between the dataset in the form of tiles given a tile index.  Only tile layers make use of tile providers and they have their corresponding types, **DefaultTileProvider**, **SingleImageTileProvider**, **SizeReferenceTileProvider**, **TemporalTileProvider**, **TileIndexTileProvider**, **ByIndexTileProvider**, and **ByLevelTileProvider**.

The type of a layer can not be changed for an already created layer.

## Layer Settings
Each layer has its own settings which can be used to modify its values.  Settings are **Opacity**, **Gamma**, **Multiplier**, and **Offset**.

## Layer Adjustment
Layer adjustments are used to remap raster channels.  The current only adjustment is **ChromaKey** which can be used to set the transparency threshold of a layer given a chroma key.  This is useful if a layer source does not support transparency but a certain color represents full transparency.

## Blend Mode
Each layer has its own blend mode.  It defines how the layer will be blended on top of underlying layers:
- **Normal** -- Simple alpha blending
- **Multiply** -- Multiplies the RGB components with the underlying color
- **Add** -- Adds the RGB components to the underlying color
- **Subtract** -- Subtracts the RGB components from the underlying color
- **Color** -- Converts the underlying color from RGB to HDV and sets the V value from the grayscale representation of this layer, then converts it back to RGB.

## Add or Remove Layers
Layers can be added by calling the function `openspace.globebrowsing.addLayer()` or removed by calling the function `openspace.globebrowsing.deleteLayer()`.  See documentation for more info, also see [Creating a Renderable Globe]({{ site.url }}/docs/builders/globebrowsing/creating-a-renderableglobe) for information about how layers are defined as lua tables.
