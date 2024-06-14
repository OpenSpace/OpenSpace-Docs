# 0.20.0
  - Release Date: 2024-XX-XX @TODO
  - Commit: @TODO
  - Full changelog: @TODO

Download version 0.20.0 for Windows and Mac on the OpenSpace website [installation page](https://www.openspaceproject.com/version-0192)(@TODO: update link). Below are notes that highlight new content and bug fixes that will be relevant for OpenSpace users.


## Content
  - ...

## Bug Fixes
  - ...

## Breaking Changes
Below is a list of breaking changes in this release.

- A New Renderable for Point Clouds (`RenderableBillboardsCloud` &rarr; `RenderablePointCloud`) [Details](./conversion.md#a-new-renderable-for-point-clouds)
- `RenderableSphere` &rarr; `RenderableSphereImageOnline` & `RenderableSphereImageLocal` (@TODO: Provide details)
- Property identifier changes
  - RenderableAtmosphere: `EclipseHardShadowsInfo` &rarr; `EclipseHardShadows`
  - RenderableEclipseCone: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderableShadowCylinder: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderableOrbitalKepler: `Appearance.OutlineWeight` &rarr; `Appearance.OutlineWidth`
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
- Changed name of line fade in RenderableTrail from Fade to LineFade
- Added the ability to set individual commandline options at the expense of a generic Lua script
  - Note breaking change: Previously `--config` specified one or more Lua scripts that were executed to update the configuration state, now the `--config` sets the path to the window configuration instead
  - For cases that are not covered by the new commandline options, it is possible to create a `openspace.cfg.override` the content of which overwrites all settings set in the `openspace.cfg` file
  - `data/assets/spice/base.asset` is now called `data/assets/spice/core.asset`
- Removed the ability to implicitly load kernels from `SpiceTranslation` and `SpiceRotations`. Use the `openspace.spice.loadKernel` and `openspace.spice.unloadKernel` functions in the `onInitialize`/`onDeinitialize` functions instead
- Removed support for XML configuration files in SGCT. Convert existing XML files with the converter tool found at https://tools.openspaceproject.com
- Move Sun light source specification from sun.asset to transforms.asset
- Remove the ability to have optional parameters in the beginning of Lua functions (closes #3151). The first parameter for the `goToGeo` and `flyToGeo` functions is now required

:::{toctree}
:maxdepth: 1
:hidden:

conversion
:::
