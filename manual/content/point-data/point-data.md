# Point Data
A commonly used type of dataset is those containing a set of 3D positions. These can be used to spatially represent a vast variety of object types, where each object is represented by a point in space.

In OpenSpace, such datasets are referred to as *point clouds* and include a set of features like: coloring, adjusting the point size, fading in and out based on the camera distance, and attaching text labels to the positions. Coloring includes color mapping based on data columns, and there is also support for handling missing values.

:::{figure} sdss.png
:align: center
*One example of a point cloud dataset is the Sloan Digital Sky Survey in the Default profile.*
:::

## Loading Point Datasets
In the simplest case, a point cloud is created by just loading a CSV or [SPECK](./data-formats.md#speck-speck) file using a renderable of the type `RenderablePointCloud`. The example below shows a minimal asset to load a point cloud from a CSV file.

```lua
local Node = {
  Identifier = "ExamplePoints",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv") -- load the data file (must have an x, y and z column)
  },
  GUI = {
    Name = "Example Points",
    Path = "/Example/Point Clouds",
  }
}

-- Additional functions required for the asset, such as onInitialize, onDeinitialize and export,
-- are excluded here, to focus on the aspects specific to the point clouds. See Asset wiki
-- page for general information about the structure on an asset
...
```

However, you will most likely want to update the size and coloring of the points, for example using a color map or by adding a sprite texture to use for rendering the points. See upcoming sections for details on how to configure the rendering and visuals of the points.

There are also other specializations of the `RenderablePointCloud` type, that adds one or more specialized feature for the points, but `RenderablePointCloud` type renderable should be enough for most use cases.  See further down for a list of point cloud specializations.

### Units

Per default, the X, Y and Z positions of the points are interpreted in meters, but it is also possible to specify a specific unit to match the one in the dataset.
See `RenderablePointCloud` documentation for a list of supported units.

For example, if the positions in the data file are to be interpreted in parsec, add `Unit = "pc"` to the Renderable specification, like so:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Unit = "pc"
  },
  ...
```

### Data Mapping

## Coloring
The points can be colored either using a fixed color or by a color map. If the points are rendered using a texture, this may also affect the color (see next section).

### Fixed Color

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Coloring = {
        FixedColor = { 1.0, 0.0, 0.0 } -- red
    }
  },
  ...
```

### Color Map
Alternatively, each point can be colored using a selected data variable and a color map.   ... @TODO

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Coloring = {
        ColorMapping = {
            File = asset.resource("path/to/colormap.cmap"),
            -- Any other settings...
        }
    }
  },
  ...
```
With that setup, the point cloud dataset can be interactively colored by any data value in the dataset, which is useful when exploring or creating a new visualization. However, it is also possible to prepare a set of parameters and data ranges to choose from.

**TODO Add example of color parameters**

#### Advanced Settings

The color mapping component includes several
**NaN values (missing values)**:

**Values outside the range**:

We refer to our example assets for more details on how to customize the color map settings, but here is a summary of some properties and their functionality:

| Properties| Description |
| :--- | :--- |
| HideValuesOutsideRange | Hide any value that is outside the provided value range |
| NoDataColor*, ShowMissingData | Show missing data points in a specific color |
| AboveRangeColor*, UseAboveRangeColor | Show points with values larger than the max value in the range in a specific color |
| BeloweRangeColor*, UseBeloweRangeColor | Show points with values below than the min value range in a specific color |

\* Note that these can also be set in the color map file itself. See [the page on color map files](./data-formats.md#color-maps-cmap) for more details.

## Adding a Texture

## Controlling the Point Size

## Fading

## Labels

## Specializations of RenderablePointCloud
| Renderable type | Description |
| :--- | :--- |
| RenderablePolygonCloud | A point cloud where each point is represented by a dynamically created uniform polygon (such as a triangle, hexagon, octagon, etc.). The number of sides of the polygon is configured in the asset. |