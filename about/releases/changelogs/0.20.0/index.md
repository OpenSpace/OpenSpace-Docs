# 0.20.0
  - Release Date: 2024-06-17
  - Commit: 14cf12d23ebad2e3ea663149c7101be756e98fbd
  - [Full changelog](https://github.com/OpenSpace/OpenSpace/releases/tag/releases%2Fv0.20.0)

Download version 0.20.0 for Windows and Mac on the OpenSpace website [installation page](https://www.openspaceproject.com/version-0200). Below are notes that highlight new content and bug fixes that will be relevant for OpenSpace users.

## New Features
- **Documentation Revamp**: All static information has now been consolidated and relocated to the "Reference" section on the [OpenSpace documentation site](https://docs.openspaceproject.com).
- **User Settings Storage**: Persistent file now saves user settings, including selected profile and configuration file.
- **Keybinding Changes**:
	-   Toggle Trails:
	    -   `T`: Toggles all trails with fade.
	    -   `Shift+T`: Instantly toggles trails.
	-   Blackout Toggle: `B` now toggles the blackout effect instead of `W`.
- **Global Blackout Control**: New property to control the application of the global blackout factor to master rendering.
- **Audio Support**: Playback of local MP3 files is now supported.
- **MPCDI Format Support**: Support for new MPCDI format used by COSM/E&S.
- **Point Cloud Overhaul**:
  - New rendering techniques.
  - Ability to load labels from CSV/SPECK files.
  - Enhanced scaling and outline rendering.
  - Texture and orientation data support.

## Enhancements
- **Trail Rendering**: Improved performance, control over trail length and fading, and better handling of trajectory trails.
- **Star Renderer Update**: Stars are now represented by layered textures for a more customizable appearance.
- **Globe Layer Management**: Explicit layer order and improved layer handling with zIndex parsing that allows users to add their own layers more easily.

## UI Improvements
- **Focus Menu**: New options and buttons for flying and focusing on nodes.
- **Scene Menu**: Enhanced search functionality, better handling of visible and hidden nodes, and a "Quick Access" entry.
- **Geoposition Panel**: Overhauled for better usability.
- **Node Meta Panel**: Clearer information display.
- **New Buttons**: Added buttons for various functionalities including GUI opening in an external browser and jump-to settings.

## Content Creation
- **HttpSynchronization**: Faster resumption of partial downloads.
- **UrlSynchronization**: Option to rate limit downloads, e.g., downloading new satellite trajectories once per day.
- **File Drag-and-Drop**: Video files can be added as ScreenSpaceRenderables via drag-and-drop.
- **Session Recording**: Enhanced capabilities for recording and playing back sessions with new commands and options.
- **Options Overhaul**: More specific command line options and the ability to override the `openspace.cfg` file.

## Content and Assets
- **New Profiles and Assets**:
  - Euclid and BepiColombo mission profiles.
  - Tiangong space station, Big Dipper constellation, historical epicycle concept, and more.
- **Updated Assets**: Updated orientations, datasets, and various mission details.

## Bug Fixes
- **Stability and Performance**: Numerous bug fixes addressing crashes, rendering issues, UI errors, and data handling problems

## Breaking Changes
Below is a list of breaking changes in this release.

- A New Renderable for Point Clouds (`RenderableBillboardsCloud` &rarr; `RenderablePointCloud`) [Details](./conversion.md#a-new-renderable-for-point-clouds)
- `RenderableSphere` &rarr; `RenderableSphereImageOnline` & `RenderableSphereImageLocal`
- Property identifier changes
  - RenderableAtmosphere: `EclipseHardShadowsInfo` &rarr; `EclipseHardShadows`
  - RenderableEclipseCone: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderableShadowCylinder: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderableOrbitalKepler: `Appearance.OutlineWeight` &rarr; `Appearance.OutlineWidth`
  - RernderableTrail: Line fade renamed from `Fade` &rarr; `LineFade`
  - All ScreenSpaceRenderables: `Gamma` &rarr; `GammaOffset`
- The functions `openspace.navigation.addLocalRoll`, `openspace.navigation.addGlobalRoll`, and `openspace.navigation.addTruckMovement`in the [Scripting API](/generated/scripting-api/index.md) now has one input parameter value instead of two. Previously, one of the values was not being used but had to be provided. For details on the functions, see the corresponding page in the [Reference](/generated/scripting-api/openspace.navigation.md).
- The TileLayer classes were renamed to TileProvider. This causes a breaking change in all assets that try to load a layer
  - Type changes:
    - `DefaultTileLayer` &rarr; `DefaultTileProvider`
    - `SingleImageTileLayer` &rarr; `SingleImageProvider`
    - `ImageSequenceTileLayer` &rarr; `ImageSequenceTileProvider`
    - `SpoutImageTileLayer` &rarr; `SpoutImageProvider`
    - `TemporalTileLayer` &rarr; `TemporalTileProvider`
    - `TileIndexTileLayer` &rarr; `TileIndexTileProvider`
    - `SizeReferenceTileLayer` &rarr; `SizeReferenceTileProvider`
    - `ByLevelTileLayer` &rarr; `TileProviderByLevel`
    - `ByIndexTileLayer` &rarr; `TileProviderByIndex`
- Added the ability to set individual commandline options at the expense of a generic Lua script
  - Note breaking change: Previously `--config` specified one or more Lua scripts that were executed to update the configuration state, now the `--config` sets the path to the window configuration instead
  - For cases that are not covered by the new commandline options, it is possible to create a `openspace.cfg.override` the content of which overwrites all settings set in the `openspace.cfg` file
  - `data/assets/spice/base.asset` is now called `data/assets/spice/core.asset`
- Removed the ability to implicitly load kernels from `SpiceTranslation` and `SpiceRotations`. Use the `openspace.spice.loadKernel` and `openspace.spice.unloadKernel` functions in the `onInitialize`/`onDeinitialize` functions instead
- Removed support for XML configuration files in SGCT. Convert existing XML files with the [converter tool](https://tools.openspaceproject.com)
- Move Sun light source specification from sun.asset to transforms.asset
- Remove the ability to have optional parameters in the beginning of Lua functions (#3151). The first parameter for the `goToGeo` and `flyToGeo` functions is now required

:::{toctree}
:maxdepth: 1
:hidden:

conversion
:::
