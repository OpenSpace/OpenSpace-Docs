# Point Data
A commonly used type of dataset is those containing a set of 3D positions. These can be used to spatially represent a vast variety of object types, where each object is represented by a point in space.

In OpenSpace, such datasets are referred to as *point clouds* and include a set of features like: coloring, adjusting the point size, fading in and out based on the camera distance, and attaching text labels to the positions. Coloring includes color mapping based on data columns, and there is also support for handling missing values.

This page describes how to load a point dataset and the options for controlling the visual of the points. It is also possible to add text labels to the points. See the separate [Labels page](./labels.md) for more details on labels.

:::{figure} sdss.png
:align: center
*One example of a point cloud dataset is the Sloan Digital Sky Survey in the Default profile.*
:::

## Loading Point Datasets
In the simplest case, a point cloud is created by just loading a [CSV](./data-formats.md#csv) or [SPECK](./data-formats.md#speck-speck) file using a renderable of the type `RenderablePointCloud`. The example below shows a minimal scene graph node specification for an asset to load a point cloud from a CSV file, with default values for all the visual properties.

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

-- asset.onInitialize and asset.onDeinitialize... See page about Assets for details
...
```

However, you will most likely want to update the size and coloring of the points, for example using a color map or by adding a sprite texture to use for rendering the points. See upcoming sections for details on how to configure the rendering and visuals of the points.

:::{admonition} Data caching
Per default, the first time any dataset is loaded it will be cached in a version that is faster to load at the next startup. This may lead to changes in the dataset not being registered unless you first remove the cached version of the file from the OpenSpace/cache folder.

We recommend keeping caching on as it greatly speeds up the loading of the assets. However, if you want to temporarily disable caching you can use the setting `UseCaching = false` in the renderable. That way, a fresh load will be done for the dataset every time the renderable is created.
:::

### Units

Per default, the X, Y and Z positions of the points are interpreted in meters, but it is also possible to specify a specific unit to match the one in the dataset. For example, if the positions in the data file are to be interpreted in parsec, add `Unit = "pc"` to the Renderable specification, like so:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Unit = "pc" -- short for "parsec"
  },
  ...
```

Other options are for example `"Mpc"` for Megaparsec, or `Km` for kilometers. See `RenderablePointCloud` documentation for a list of supported units.

### Data Mapping

There are cases where we need control of certain parameters in the data loading. One example is that for CSV files, we might want to specify what data columns to use for the X, Y and Z components of the position, rather than renaming the columns. Or, we might want to specify other details about the data loading, such as columns that are not relevant and can be excluded. This is done by providing a `DataMapping` table in the asset when loading the dataset:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    DataMapping = {
      -- Using the DataMapping, we can specify the name of the columns to use for the X,
      -- Y and Z values of the point, without changing the dataset used for the rendering
      X = "column name for X",
      Y = "column name for Y",
      Z = "column name for Z",
      -- It is also possible to specify a numeric value that corresponds to missing
      -- values in the dataset. These will be interpreted as NaN values
      MissingDataValue = -9999,
      -- And the names of some columns that we do not want to include in the loading
      ExcludeColumns = { "IdontWantThisColumn", "this is not relevant either" }
    }
  },
  ...
```
:::{note}
Note that updating the data mapping leads to another version of the data file being loaded and cached on disk.
:::

### Labels
Labels can either be added using an explicit labels file, as explained on [this page](./labels.md), or directly from a column in a CSV file. To add labels from a column in the file, specify the name of that column in the data mapping:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    DataMapping = {
      Name = "column name for Labels column"
    }
  },
  ...
```

it is also possible to control the size and color of the labels by adding a `Labels` group in the asset. See [Labels page](./labels.md) for more details. Note that no `File` property is required in the `Labels` group when loading labels directly from the CSV file.

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

If a color map is added, it will be enabled by default. But it can also be disabled either in the asset or during runtime. If both a `FixedColor` and `ColorMapping` is specified, the color mapping will be used (as long as it is enabled).

### Color Mapping
Alternatively, each point can be colored using a selected data variable and a color map. This is done by adding a `ColorMapping` table in the asset, as shown above. With that setup, the point cloud dataset can be interactively colored by any data value in the dataset, which is useful when exploring or creating a new visualization. However, it is also possible to prepare a set of parameters and data ranges to choose from (see below).

The coloring is performed based on a _color map_, a choice of data _parameter_ and a _value range_. Points with values within the range will be colored based on the normalized value of their datapoint, where the minimum value corresponds to the first color in the color map and the max value corresponds to the last color. Any color in between will be determined in a nearest-neighbor fashion.

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
        -- menu in the user interface. The "name of parameter" is the name of the corresponding
        -- column in the dataset
        ParameterOptions = {
          -- Add a parameter with a predefined value range that should be used
          -- when this option is chosen
          { Key = "name of parameter", Range = { 1.0, 30.0 } },
          -- Add another parameter, but with no specific range. The range used
          -- when changing parameter will me the min and max value in the dataset
          { Key = "name of another parameter" }
        },

        -- Per default, the chosen parameter is set to the first one in the list above.
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

### Blending
Per default, the colors of points that overlap are blended additively, resulting in a brighter color in the overlapping areas. This behavior is not always desired, as it might result in distorted colors in the overlaps. To disable the blending, set `UseAdditiveBlending` to `false` under `Coloring` in the asset:

```lua
 ...
  Renderable = {
    ...
    Coloring = {
      -- Disable additive blending, so that points will be rendered with their actual color.
      -- Overlapping points will be sorted by depth
      UseAdditiveBlending = false
    }
  },
  ...
```

This means that the point will be rendered without any blending and the point that is closest to the camera will be rendered on top.

:::{figure} blending.png
:align: center
:width: 80%
*Example of points with (right) and without (left) additive blending enabled. Note how the points to the right appear brighter in the overlapping areas, while the left set of points preserve their actual color. In the overlaps, the point that is closer to the camera will be the visible one.*
:::

:::{attention}
Note disabling the blending does not work very well together with transparency. We therefore recommend using an opacity of 1 for the renderable whenever blending is disabled.
:::

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

The points will look the best with textures that have a transparent background, i.e. with an alpha value of zero. Below is an example of a point cloud with a filled star shape. However, shapes that are transparent in the center (for example, a ring), or have more than one color would work as well. Note however that if you want to apply a color to your point using a color map or fixed color, we recommend using texture in white or bright grayscale.

:::{figure} texture_star.png
:align: center
:width: 90%
:::

### Textures and Colors
Textures also work with color maps. In that case, the color of the texture is multiplied by that of the color. The same goes if a fixed color is applied to the points. See example below. Note that here we have also disabled the additive blending by setting the `UseAdditiveBlending` property to `false`, so that the color of overlapping points is not added and blended.

:::{figure} textures.png
:align: center
:::

:::{admonition} A note about file paths
:class: note
`asset.resource` can be used to specify a relative or full path to a data file. However, it is also possible to use the `openspace.absPath` script to use some of the path tokens that are provided with OpenSpace. For example, the cat texture above is a test image that exists in the "OpenSpace/data" folder. To use this in your asset and avoid having to specify a path that is based on your file location, you can use the provided file token to the data folder to get the absolute path to the location of the file: `openspace.absPath("${DATA}/test3.jpg")`.

The list of available path tokens and their corresponding locations are found in the openspace.cfg file.
:::

## Controlling the Point Size

At the core, the size of the points is computed based on one parameter: a logarithmic exponent that decides the absolute size of the point. The exponential component exists to allow creating point clouds over very different scales and distances and should be set to match the scale of the dataset. It is used to compute the actual world scale size of the points, at their position in the 3D scene. For example, an exponent of 3 will lead to points with a size in the order of 1000 meters, while an exponent of 10 will lead to points with a size of about 10^10 = 100'000'000 meters.

If not included in the asset, a default exponent is computed based on the positional information in the dataset. However, this should be seen as a starting point and you will likely want to modify it so that the scale of the points looks good based on the density, number of points and the spread of your particular dataset, as well as the use case for which it is to be shown.

Secondly, a multiplicative factor that can be used to increase or decrease the *visual* size of the points also exists. This factor can be seen as a tool to quickly increase or decrease the appeared size of all points equally. This factor is applied at the last step, after the exponential scaling and any max size effects.

To update the scaling in the points, add a `SizeSettings` table to your asset specification. See example:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    SizeSettings = {
      -- Control the world-scale size of the points, here in the order of 10^15
      ScaleExponent = 15.0,
      -- Visually make all the points twice as large
      ScaleFactor = 2.0
    }
  },
  ...
```

:::{note}
Since the exponent affects the physical, world-scale, size of the points, this means that points that are closer to the camera will appear larger than those that are further away, and increasing the exponent also enhances this effect. In contrast, increasing the multiplicative factor will increase the visual size of the points equally for all points. This is because it is applied in the very last step, after the exponential scaling and any max size effects.
:::

### Limit to a Max Size
In addition to the world-size scale, it is also possible to limit the maximum size the points are allowed to take up of the view. This prevents the points from growing larger than a specified size when the camera is approaching the dataset. An example is shown in the images below.

:::{figure} pointsize_close.png
:align: center
:width: 90%
:::
:::{figure} pointsize_far.png
:align: center
:width: 90%
*Example of the point size scaling in action. The green points (left) use regular sizing and the blue points (right) have a limited max size. Note how the green points (left) appear larger up close and smaller at a large distance, while the blue points (right) are scaled to have the same size at both distances.*
:::

To limit the maximum size of the points, add the `EnableMaxSizeControl` and `MaxSize` settings in the `SizeSettings` table:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    SizeSettings = {
      -- Limit the size of the points to a max size
      MaxSize = 1.0, -- A value that looks good to you
      EnableMaxSizeControl = true
    }
  },
  ...
```

The larger the `MaxSize` is, the larger the points are allowed to become when the camera is approaching them. Exactly what the value means is not that important, but if you are interested, see note at the end of this section for an explanation of the meaning behind the value.

At the core, the size of the points is still determined by the exponential scaling. That is, as long as the camera is far enough away so that the points do not exceed the specified max size, the size will still be determined by the provided scale exponent. Also, the multiplicative `ScaleFactor` is applied after the max size scaling. That is, if you specify a `MaxSize` and a `ScaleFactor` of 2, the max size of the points will be twice as large as with a `ScaleFactor` of 1.

:::{dropdown} The `MaxSize` value
When computing the maximum allowed size of the points, the `MaxSize` value is interpreted as __an angle (in degrees)__ that the point is allowed to take up of the view, from the perspective of the camera. In simplified terms, a value of 1 implies that the point is allowed to take up a maximum of 1 degree of the camera's field of view.
:::

### Scale Based on Data

It is also possible to do some simple scaling based on data parameters. The size of the points is then scaled based on the value in the data column.

Similarly to the color mapping, the size mapping is added by specifying a list of options that can be used for setting the size of the points:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    SizeSettings = {
      -- The options for the columns that the points can be scaled by. The first
      -- alternative is chosen per default
      SizeMapping = { "one parameter", "another parameter" },
    }
  },
  ...
```
:::{attention}
The size mapping is currently a bit of an experimental feature. For now, the point size if directly multiplied with the data value is directly multiplied by the data value of the chosen `SizeMapping` column. This is not always suitable though, depending on the range of the data values. The behavior may be subject to change in the future.
:::

### Summary of Final Size Computation

In summary, the order in which the settings affect the size of the points is the following:

1. 10 ^ `ScaleExponent` * Scale From Data => world scale size
2. Limit point size to max size => prevent the points from growing larger than a certain size in view
3. Finally, multiply with `ScaleFactor` to increase or decrease the size, onscreen

## Fading

A point cloud can also be set up so that it fades in and out based on the distance to the camera. The distance is computed based on the origin of the dataset. This can be useful when you want to reduce the visual overload of points when multiple datasets are shown, or when you want to show different datasets depending on the distance. For example, in the Default scene, we use it to make different datasets about the Universe appear and disappear depending on your distance to our Solar System.

To configure the fading for the point cloud, specify the distance over which the fading should occur in the asset file:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Fading = {
      -- Control at what distance the points fade in. The points will be *invisible*
      -- when the camera is closer than the first value, and fully visible when the
      -- camera is further away then the last value. In-between they will linearly
      -- fade in or out
      FadeInDistances = { 100, 1000 },
      -- Optionally, invert the fading. If invert is set to true, the fading is
      -- inverted so that the points are *visible* when the camera is closer than
      -- the first distance and invisble when further away than the second
      Invert = false
    }
  },
  ...
```

:::{note}
The fading distances are specified in the same unit that is used to render the points. So if a `Unit` is set, the
distances should match that unit.
:::

<!-- ## Facing the Camera
@TODO Talk about the render option here, or move this to a special page for spherical/non-planer displays? -->

## Specializations of RenderablePointCloud

There are also other specializations of the `RenderablePointCloud` type, that adds one or more specialized feature for the points. However, `RenderablePointCloud` type renderable should be enough for most use cases.

| Renderable type | Description |
| :--- | :--- |
| RenderablePolygonCloud | A point cloud where each point is represented by a dynamically created uniform polygon (such as a triangle, hexagon, octagon, etc.). The number of sides of the polygon is configured in the asset. |