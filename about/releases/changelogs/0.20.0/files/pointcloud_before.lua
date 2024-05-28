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
