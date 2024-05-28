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
      ScaleExponent = 21.9, -- OBS! Recomputed based on previous ScaleFactor! See next section
      MaxSize = 0.3, -- No longer in pixels! Use a value that looks good to you
      EnableMaxSizeControl = true
    }
  },
  ...
}
