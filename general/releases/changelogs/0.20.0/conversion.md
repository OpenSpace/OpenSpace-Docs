# Details on Breaking Changes

The sections on this page describe some major breaking changes in version 0.20.0, together with instructions on how to adapt to the changes.

## A New Renderable for Point Clouds

`RenderableBillboardsCloud` has been removed and replaced with a new renderable type called `RenderablePointCloud`. This renderable includes some bug fixes as well as updates to the specifications in the asset related to color mapping, fading and point sizing. These are made more explicit, to make it easier to use and more understandable compared to its predecessor. For full details on the renderable, check out the new [content pages for point data](/manual/content/point-data/index).

If you have an asset with a `RenderableBillboardsCloud` that you need to convert to the new format, check out the sections below. Also, note that the format of the color map files (.cmap) has changed slightly.

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

@TODO: Summarise updated properties... (so scripts etc can be updated)

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

Any custom color maps needs to be updated...
@TODO



