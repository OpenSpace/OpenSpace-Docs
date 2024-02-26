# Details on Breaking Changes
The sections on this page describe some major breaking changes in version 0.20.0, together with instructions on how to adapt to the changes.

## A New Renderable for Point Clouds
The `RenderableBillboardsCloud` class has been removed and replaced with a new Renderable type called `RenderablePointCloud`. This renderable includes some bug fixes as well as updates to the specifications in the asset related to color mapping, fading, and point sizing. These are made more explicit, to make it easier to use, and more understandable compared to its predecessor. The new Renderable also has support for CSV files, in addition to the previous SPECK file format. For full details on the renderable, check out the new [content pages for point data](/manual/content/point-data/index).

The following sections describe [how to convert an asset with a `RenderableBillboardsCloud` to the new format](./conversion.md#how-to-update-an-asset-with-a-renderablebillboardscloud), or how to [update a color map file](./conversion.md#update-color-map-data-format) (the .cmap data format has changed slightly). Finally, there is also a [summary of the updated property names](./conversion.md#summary-of-updated-properties), that can hopefully be useful if you have Lua scripts or actions that require updating due to the use properties that have been updated or removed.

:::{note}
Note that the previously existing `RenderablePoints` renderable has been removed in favor of the new `RenderablePointsCloud`.
:::

### How-to Update an Asset with a `RenderableBillboardsCloud`
Below is a code snippet showing an example of parts of an asset with a `RenderableBillboardsCloud`, before and after the update.
The highlighted lines show the fields whose format or name has changed. See comments in the "After" example below for details.

::::{tab-set}
:::{tab-item} Before
```{literalinclude} files/pointcloud_before.lua
:language: lua
:emphasize-lines: 4, 11-14, 16, 18-20
```
:::

:::{tab-item} After
```{literalinclude} files/pointcloud_after.lua
:language: lua
:emphasize-lines: 4, 11-25, 27-30, 32-36
```
:::
::::

:::{tip}
Note that the `Texture` field is no longer required. If a texture is excluded, the points will be drawn as circles.
:::

#### Compute `ScaleExponent` from `ScaleFactor`
The scaling of the points has been made more intuitive by changing the previous `ScaleFactor` property slightly, to make it more apparent that it affects an exponential scaling. See [details on the point data page](/manual/content/point-data/point-data.md#controlling-the-point-size), but in general, with the new `ScaleExponent` the value is used as the exponent for `10^exponent` to compute the world-scale size of the points.

The new `ScaleExponent` property can be computed from the previous `ScaleFactor` as:
:::{math}
ScaleExponent = \log_{10}(e^{ScaleFactor / 10})
:::

### Update Color Map Data Format
Previously, the first and last color entry in a `.cmap` file was implicitly interpreted as the color to use for values that are lower or higher than the specified range. However, this was not very clear and has been made more explicit in the update by using specific keywords for these colors. Here is an example of a color map before and after this change:

::::{tab-set}
:::{tab-item} Before
```{literalinclude} files/colormap_before.cmap
:language: python
:emphasize-lines: 3, 4, 9
```
:::

:::{tab-item} After
```{literalinclude} files/colormap_after.cmap
:language: python
:emphasize-lines: 3, 4, 9
```
:::
::::

Note that the `belowRange` and `aboveRange` colors do not have to be specified using this capitalization or order. As long as the keywords are spelled correctly, the lines for these colors can be put anywhere in the file.

The color maps that we provide with our default assets have been updated and should work fine. However, any custom color maps need to be updated to comply with the new format.

:::{tip}
Note that with the 0.20.0 release, we do provide an asset with a number of common color maps, accessible by name, that might come in handy. Check out the example files for inspiration on how to use them.
:::

### Summary of Updated Properties
With just a few exceptions, the new `RenderablePointCloud` works very similarly to the previous `RenderableBillboardsCloud`. The behavior of the properties has not changed significantly, but the structuring of them has, and hence the name or URI that a property is accessed by may have to be updated.

Following is a table that summarizes the updated property names/URI:s, which can hopefully be useful if you have Lua scripts or actions that require updating due to the use properties that have been updated or removed.

| RenderableBillboardsCloud (Before) | RenderablePointCloud (After) | Type | Comment |
| --- | --- | --- | --- |
| `Color` | `Coloring.FixedColor` | Color (Vec3) | |
| `ColorMap` | `Coloring.ColorMapping.ColorMap` | String | |
| `UseColorMap` | `Coloring.ColorMapping.Enabled` | Boolean | |
| `ColorOption` | `Coloring.ColorMapping.Parameter` | Integer | |
| `OptionColorRange` | `Coloring.ColorMapping.ValueRange` | Vec2 | |
| `SetRangeFromData` | `Coloring.ColorMapping.SetRangeFromData` | `nil` (Trigger Property)  | |
| `UseLinearFiltering` | (Removed) |  | |
| `SizeOption` | `Sizing.SizeMapping.Parameter` | Integer | |
| `FadeInDistances` | `Fading.FadeInDistances` | Vec2 | Should now be set based on the origin of the dataset, rather than the world-space origin |
| `DisableFadeIn` | `Fading.Enabled` | Boolean | Inverted compared to the prevoius value |
| `EnablePixelSizeControl` | `Sizing.EnableMaxSizeControl` | Boolean |  |
| `BillboardMinMaxSize` | `Sizing.MaxSize` | Float | No longer a pixel value, so the value has to be updated |
| `CorrectionSizeEndDistance` | (Removed) |  | |
| `CorrectionSizeFactor` | (Removed) |  | |
| `ScaleFactor` | `Sizing.ScaleExponent` | Float | Can be computed based on the previous value, as described in the [section above](compute-scaleexponent-from-scalefactor) |

Note that the full property URI would be of the form
`Scene.<IdentifierOfNode>.Renderable.<NameOfPropertyFromTableAbove>`.

Some new features are that the data file can be loaded using a CSV file, and that the fading direction can be inverted. See [the content page on point data](/manual/content/point-data/point-data) for more details.

## Changes in the `openspace.navigation.saveNavigationState` function
The format in which the navigation states are saved to a file on disk from this function has been changed. Prior to 0.20.0, this file was a Lua-file which was coded to return a table. As of 0.20.0, this fileformat is using JSON instead. This change affects both the `openspace.navigation.saveNavigationState` and the `openspace.navigation.loadNavigationState` functions.

If you have a pre 0.20.0 navigation state file that you want to convert, this is best done in a text editor using the following steps:
  1. Remove the leading `return` in the beginning of the file
  1. Replace all `=` with `:`
  1. All words "Position", "Anchor", "ReferenceFrame", "Aim", "Up", "Yaw", and "Pitch" should be surrounded by `"` and be written in lower case
  1. For the "Position" and "Up" entries, prepend the first value with `"x":`, the second value with `"y":`, and the third value with `"z":`
  1. (optional) Rename the file to have a `.navstate` extension

For example a pre 0.20.0 navigation state would be:
```lua
return {Anchor="Earth",Position={11701166.502990872,3397820.0813846793,19951812.217589088},Up={-0.8195835910478171,-0.23799315924271663,0.5211928562814687}}
```

After step 1:
```
{Anchor="Earth",Position={11701166.502990872,3397820.0813846793,19951812.217589088},Up={-0.8195835910478171,-0.23799315924271663,0.5211928562814687}}
```

After step 2:
```
{Anchor:"Earth",Position:{11701166.502990872,3397820.0813846793,19951812.217589088},Up:{-0.8195835910478171,-0.23799315924271663,0.5211928562814687}}
```

After step 3:
```
{"anchor":"Earth","position":{11701166.502990872,3397820.0813846793,19951812.217589088},"up":{-0.8195835910478171,-0.23799315924271663,0.5211928562814687}}
```

After step 4:
```
{"anchor":"Earth","position":{"x":11701166.502990872,"y":3397820.0813846793,"z":19951812.217589088},"up":{"x":-0.8195835910478171,"y":-0.23799315924271663,"z":0.5211928562814687}}
```
