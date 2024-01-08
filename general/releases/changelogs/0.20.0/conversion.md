# Details on Breaking Changes

The sections on this page describe some major breaking changes in version 0.20.0, together with instructions on how to adapt to the changes.

## A New Renderable for Point Clouds

`RenderableBillboardsCloud` has been removed and replaced with a new renderable type called `RenderablePointCloud`. This renderable includes some bug fixes as well as updates to the specifications in the asset related to color mapping, fading and point sizing. These are made more explicit, to make it easier to use and more understandable compared to its predecessor. The new Renderable also has support for CSV files, in addition to the previous SPECK file format. For full details on the renderable, check out the new [content pages for point data](/manual/content/point-data/index).

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

:::{admonition} Compute `ScaleExponent` from `ScaleFactor`
:class: note
The scaling of the points has been made more intuitive by changing the previous `ScaleFactor` property slightly, to make it more apparent that it affects an exponential scaling. See [details on the point data page](/manual/content/point-data/point-data.md#controlling-the-point-size), but in general, with the new `ScaleExponent` the value is used as the exponent for `10^exponent` to compute the world-scale size of the points.

The new `ScaleExponent` property can be computed from the previous `ScaleFactor` as:
:::{math}
ScaleExponent = \log_{10}(e^{ScaleFactor / 10})
:::
:::

:::{tip}
Note that the `Texture` field is no longer required. If a texture is excluded, the points will be drawn as circles.
:::


### Update Color Map Data Format

Previously, the first and last color entry in a .cmap file was implicitly interpreted as the color to use for values that are lower or higher than the specified range. However, this was in no way clear, and has been made more explicit in the update by using specific keyworkds for these colors. Here is an example of a color map before and after this change:

::::{tab-set}
:::{tab-item} Before
```{literalinclude} files/before.cmap
:language: python
:emphasize-lines: 3, 4, 9
```
:::

:::{tab-item} After
```{literalinclude} files/after.cmap
:language: python
:emphasize-lines: 3, 4, 9
```
:::
::::

Note that the `belowRange` and `aboveRange` colors do not have to be specified in this exact way or order. Using the keywords, the lines for these colors can be put anywhere in the file.

The color maps that we provide with our default assets have been updated and should work fine. However, any custom color maps need to be updated to comply with the new format.

:::{tip}
Note that with the 0.20.0 release, we do provide an asset with a number of common color maps, accessible by name, that might come in handy. Check out the example files for inspiration on how to use them.
:::

### Summary of Updated Properties

With just a few exceptions, the new `RenderablePointCloud` works very similarly to the previous `RenderableBillboardsCloud`. The behavior of the properites has not changed significantly, but the structuring of then has, and hence the name or URI that a property is accessed by may have to be updated.

Following is a table that summarize the updated property names/URI:s, that can hopefully be useful if you have Lua scripts or actions that require updating due to the use properties that have been updated or removed.

| RenderableBillboardsCloud (Before) | RenderablePointCloud (After) | Type |
| --- | --- | --- |
| `Color` | `ColorMapping.Color` | Color (Vec3) |
| `ColorMap ` | `ColorMapping.ColorMap` | String |
@TODO: Finish list


Note that the full property URI would be something like:
`Scene.<IdentifierOfNode>.Renderable.<NameOfPropertyFromTableAbove>`.