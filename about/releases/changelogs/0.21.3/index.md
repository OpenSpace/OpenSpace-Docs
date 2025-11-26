This patch fixes a number of issues with existing layers, the rendering on laptop computers, issues with the user interface in very heavy profiles, and more.

If you have created your own `RenderableSphericalGrid`, see the breaking changes list at the bottom.

# Features
## Launcher
  - The edit button in the Launcher is now correctly disabled if a built-in profile is selected at startup

## UI
  - Used a more user-friendly "Default Properties" instead of "DefaultProperties" for the GeoJSON layers

# Content
## Updates to existing Assets/Profiles
  - Increased the maximum tile level for the ESRI World Imagery from 19 to 21

### Lua
  - The `openspace.time.SPICE` function now takes an additional argument to control the formatting of the returned date string
  - The `openspace.downloadFile` function now takes an additional argument controlling whether a file should be downloaded if it already exists

# Bug Fixes
  - Height layers on Earth would disappear when requesting the highest available detail (#3791)
  - The _OpenSpace Helper_ that renders the user interface now also correctly requests a dedicated graphics card, causing the application to no longer crash
  - The user interface became unresponsive when displaying a large amount of data
  - Disabling _Perform shading_ on globes would create a warning message for every frame (#3770)
  - The action to add a sun trail behaved inconsistently for different dates (#3817)
  - Restore the erroneously removed barycentric trail for the Pluto system
  - The shadows on a ring system would not render correctly in fisheye mode (#3776)
  - The action to toggle planet and moon trails was not working correctly
  - The Lua console would result in an infinite loop when minimizing OpenSpace while the console was open
  - The fieldlines in the _Today's Sun_ profile would not be colored correctly when switching days (#3786)
  - Spherical grids rendered incorrectly when their opacity was not completely full
  - The Night Sky version of Saturn was missing the correct scale factors
  - The Minor Planet Center asset contained an error causing it to fail to load
  - The period of asteroids retrieved from the Minor Planet Center was calculated incorrectly (#3804)
  - OpenSpace would crash when deinitializing a ScreenSpaceRenderableRenderable
  - The base folder was detected incorrectly when providing the path to a `openspace.cfg` file that lived in a different folder (#3806)
  - The camera position could become unreliable when focussing on an object with a degenerate model transform (#3177)
  - Correctly set sandboxing settings for Chromium Embedded Framework on Linux (#3711)

# Breaking changes
Note that due to one of the fixes that addressed flickering in spherical grids when they are rendered not at full opacity, the behavior of segments has changed. The number of segments along the latitude rings of a grid was incorrectly specified, resulting in only half -1 the number of segments as desired.  Previously specifying 36 segments would result in 36 longitudinal segments but 17 latitudinal. This buggy behavior was fixed, but that causes existing `RenderableSphericalGrid` specifications to be adapted.

*Mitigation*:  In an asset that creates a grid replace `Segments = N` (for any N) with `LongSegments = N, LatSegments = N/2-1`

