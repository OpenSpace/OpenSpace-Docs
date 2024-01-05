# Details on Breaking Changes

The sections on this page describe some major breaking changes in version 0.20.0, together with instructions on how to adapt to the changes.

## A New Renderable for Point Clouds

`RenderableBillboardsCloud` has been removed and replaced with a new renderable type called `RenderablePointCloud`. This renderable includes some bug fixes as well as updates to the specifications in the asset related to color mapping, fading and point sizing. These are made more explicit, to make it easier to use and more understandable compared to its predecessor. For full details on the renderable, check out the new [content pages for point data](/manual/content/point-data/index).

If you have an asset with a `RenderableBillboardsCloud` that you need to convert to the new format, check out the sections below. Also, note that the format of the color map files (.cmap) has changed slightly.

:::{note}
Note that the previously existing `RenderablePoints` renderable has been removed in favor of the new `RenderablePointsCloud`.
:::

### How-to Update an Asset with a `RenderableBillboardsCloud`

Before: (highlighted lines show the fields whose format or name has changed)
:::{code-block} lua
:linenos:
:emphasize-lines: 4, 11-14, 16, 18-20

local TullyGalaxies = {
  Identifier = "TullyGalaxies",
  Renderable = {
    Type = "RenderableBillboardsCloud",
    Labels = { ... },
    File = speck .. "tully.speck",
    Texture = textures .. "point3A.png",
    Unit = "Mpc",
    Opacity = 0.99,
    -- Things related to coloring
    Color = { 1.0, 0.4, 0.2 },
    ColorMap = speck .. "lss.cmap",
    ColorOption = { "prox5Mpc" },
    ColorRange = { { 1.0, 30.0 } },
    -- Fading
    FadeInDistances = { 0.001, 1.0 }, -- Fade in value in the same unit as "Unit"
    -- Things related to the size of the points
    ScaleFactor = 504.0,
    BillboardMinMaxSize = { 0.0, 7.0 }, -- in pixels
    EnablePixelSizeControl = true
  },
  ...
}
:::

After:
:::{code-block} lua
:linenos:
:emphasize-lines: 4, 11-25, 27-30, 32-36

local TullyGalaxies = {
  Identifier = "TullyGalaxies",
  Renderable = {
    Type = "RenderablePointCloud",
    Labels = { ... },
    File = speck .. "tully.speck",
    Texture = textures .. "point3A.png",
    Unit = "Mpc",
    Opacity = 0.99,
    -- Things related to color have been combined into one group
    Coloring = {
      FixedColor = { 1.0, 0.4, 0.2 },
      -- Everything related to color mapping is also one component, which can be
      -- disabled to instead just use the FixedColor. If color mapping is not used
      -- at all in your asset, just skip this
      ColorMapping = {
        Enabled = true, -- Not required
        File = speck .. "lss.cmap",
        -- Combine each entry in ColorOption and ColorRange (line 13 and 14 above) into
        -- one "ParameterOption" per entry
        ParameterOptions = {
          { Key = "prox5Mpc", Range = { 1.0, 30.0 } }
        }
      }
    },
    -- Fading is moved into a separate component, which can also be disabled
    Fading = {
      Enabled = true, -- Not required
      FadeInDistances = { 0.001, 1.0 }, -- Fade in value in the same unit as "Unit"
    }
    -- Things related to the size of the points have been combined into one group
    SizeSettings = {
      ScaleExponent = 21.9, -- OBS! Recomputed based on previous ScaleFactor! See note
      MaxPixelSize = 7.0, -- in pixels
      EnablePixelSizeControl = true
    }
  },
  ...
}
:::

:::{admonition} Compute `ScaleExponent` from `ScaleFactor`
:class: note
The scaling of the points has been made more intuitive by changing the previous `ScaleFactor` property slightly, to make it more apparent that it affects an exponential scaling. See [details on the point data page](/manual/content/point-data/point-data.html#controlling-the-point-size), but in general, with the new `ScaleExponent` the value is used as the exponent for `10^exponent` to compute the world-scale size of the points.

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



