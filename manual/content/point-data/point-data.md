# Point Data
A commonly used type of dataset is those containing a set of 3D positions. These can be used to spatially represent a vast variety of object types, where each object is represented by a point in space.

In OpenSpace, such datasets are referred to as *point clouds* and include a set of features like: coloring, adjusting the point size, fading in and out based on the camera distance, and attaching text labels to the positions. Coloring includes color mapping based on data columns, and there is also support for handling missing values.

This page describes how to load a point dataset and the options for controlling the visual of the points. It is also possible to add text labels to the points. See the separate [Labels page](./labels.md) for more details on labels.

:::{figure} sdss.png
:align: center
*One example of a point cloud dataset is the Sloan Digital Sky Survey in the Default profile.*
:::

## Loading Point Datasets
In the simplest case, a point cloud is created by just loading a [CSV](./data-formats.md#csv) or [SPECK](./data-formats.md#speck-speck) file using a renderable of the type `RenderablePointCloud`. The example below shows a minimal asset to load a point cloud from a CSV file.

```lua
local Node = {
  Identifier = "ExamplePoints",
  Renderable = {
    Type = "RenderablePointCloud",
    -- Load the data file (must have an x, y and z column)
    File = asset.resource("path/to/dataset.csv")
  },
  GUI = {
    Name = "Example Points",
    Path = "/Example/Point Clouds",
  }
}

-- Additional functions required for the asset, such as onInitialize and onDeinitialize
-- are excluded here, to focus on the aspects specific to the point clouds. See Asset wiki
-- page for general information about the structure on an asset
...
```

However, you will most likely want to update the size and coloring of the points, for example using a color map or by adding a sprite texture to use for rendering the points. See upcoming sections for details on how to configure the rendering and visuals of the points.

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

@TODO

## Coloring
The points can be colored either using a fixed color or by a color map ([see separate page](./data-formats.md#color-maps-cmap) for details about color map data formats). These are set by adding a `Coloring` component to the Renderable specification:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    -- Add a component for controlling the coloring
    Coloring = {
      -- Specify a fixed color for all the points:
      FixedColor = { 1.0, 0.0, 0.0 }, -- red
      -- Or apply a color map:
      ColorMapping = {
        File = asset.resource("path/to/colormap.cmap"),
        -- Any other settings...
      }
    }
  },
  ...
```

If a color map is added, it will be enabled by default. But it can also be disabled either in the asset or during runtime.

### Color Mapping
Alternatively, each point can be colored using a selected data variable and a color map. This is done by adding a `ColorMapping` table in the asset, as shown above. With that setup, the point cloud dataset can be interactively colored by any data value in the dataset, which is useful when exploring or creating a new visualization. However, it is also possible to prepare a set of parameters and data ranges to choose from (see below).

The coloring is performed based on a _color map_, a choice of data _parameter_ and a _value range_. Points with values within the range will be colored based on the normalized value of their datapoint, where the minimum value corresponds to the first color in the color map and the max value corresponds to the last color.

:::{admonition} Default behavior
:class: note
By default, values outside the range will be clamped to either the first or last color, and missing values are excluded from the rendering. However, as explained below, there are settings to control the visual outcome for these cases.

The data parameter used for coloring at startup will be the last one that is loaded.
:::


#### Predefine color parameters and value ranges

By default, all the variables in the dataset are loaded as possible options for color mapping, and the value range to use for the is generated. However, it is also possible to predefine a set of parameters that can be used for coloring, together with predefined value ranges that should be applied when selecting a parameter among the provided options.

```lua
  ...
  Renderable = {
    ...
    Coloring = {
      ColorMapping = {
        File = asset.resource("path/to/colormap.cmap"),
        -- Add a few parameter options, that will be the available options in the drop down
        -- menu in the user interface
        ParameterOptions = {
          -- Add a parameter with a predefined value range that should be used
          -- when this option is chosen
          { Key = "name of parameter", Range = { 1.0, 30.0 } },
          -- Add another parameter, but with no specific range. The range used
          -- when changing parameter will me the min and max value in the dataset
          { Key = "name of another parameter" }
        },

        -- Per default, the chosen parameter is set to the last one in the list above.
        -- However, you can also set the default parameter in the asset
        Parameter = "name of parameter",
        -- It is also possible to set a value range that is different compared to the
        -- one for the parameter option. This will be used at startup, but overwritten
        -- if the parameter option is changed
        ValueRange = { 5.0, 10.0 }
    }
  },
  ...
```

:::{figure} colormap_ui_annotated.png
:align: center
*The chosen set of parameters will be available in the user interface. Here we see the chosen parameter (A), which can be changed through a drop-down menu, and the currently selected value range (B). The value range (B) will automatically update when a parameter (A) is chosen, but it is also possible to set it explicitly. There is also a button for setting the range to the min and max value in the dataset (C).*
:::

#### Missing values (NaN) and Values outside the range

Finally, it is also possible to color points outside the specified value range differently compared to the ones within the range, as well as showing missing data points in a specific color.

We refer to our example assets for more details on how to customize these color map settings, but here follows a summary of the properties for controlling what happens outside the data range or for missing values. All of these are optional but can be added to the `ColorMapping` table in the asset.

| Properties| Description | Type |
| :--- | :--- | :--- |
| `NoDataColor`*, `ShowMissingData` | Show missing data points in a specific color | `vec4`, `bool` |
| `HideValuesOutsideRange` | Hide any value that is outside the provided value range | `bool` |
| `AboveRangeColor`*, `UseAboveRangeColor` | Show points with values larger than the max value in the range in a specific color | `vec4`, `bool` |
| `BelowRangeColor`*, `UseBelowRangeColor` | Show points with values below than the min value range in a specific color | `vec4`, `bool` |

\* Note that these colors can also be set in the color map file itself. See [the page on color map files](./data-formats.md#color-maps-cmap) for more details.

## Adding a Texture

A sprite texture (i.e. an image) can be used to decide the shape of the points. To add a texture, simply provide a path to the image you want to use in the asset file:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    -- Add a texture to the points (a variety of image formats are supported, not only .png)
    Texture = asset.resource("path/to/texture.png")
  },
  ...
```

The points will look the best with textures that have a transparent background. Below is an example of a point cloud with a star shape. Also, if you want to apply a color to your point using a color map or fixed color, we recommend using texture in white or bright grayscale.

:::{figure} texture_star.png
:align: center
:width: 90%
:::

### Textures and Colors
Textures also work with color maps. In that case, the color of the texture is multiplied by that of the color. The same goes if a fixed color is applied to the points. See example below. Note that here we have also disabled the additive blending by setting the `UseAdditiveBlending` property to `false`, so that the color of overlapping points is not added and blended (which is the default behavior).

:::{figure} textures.png
:align: center
:::

:::{admonition} A note about filepaths
:class: note
`asset.resource` can be used to specify a relative or full path to a datafile. However, it is also possible to use the `openspace.absPath` script to use some of the path tokens that are provided with OpenSpace. For example, the cat texture above is a test image that exists in the "OpenSpace/data" folder. To use this in your asset and avoid having to specify a path that is based on your file location, you can use the provided file token to the data folder to get the absolute path to the location of the file: `openspace.absPath("${DATA}/test3.jpg")`.

The list of available path tokens and their corresponding locations are found in the openspace.cfg file.
:::

## Controlling the Point Size

@TODO

## Fading

A point cloud can also be set up so that it fades in and out based on the distance to the camera. The distance is computed based on the origin of the dataset.

To configure the fading for the point cloud, specify the distance over which the fading should occur in the asset file:

@TODO

## Specializations of RenderablePointCloud

There are also other specializations of the `RenderablePointCloud` type, that adds one or more specialized feature for the points. However, `RenderablePointCloud` type renderable should be enough for most use cases.

| Renderable type | Description |
| :--- | :--- |
| RenderablePolygonCloud | A point cloud where each point is represented by a dynamically created uniform polygon (such as a triangle, hexagon, octagon, etc.). The number of sides of the polygon is configured in the asset. |