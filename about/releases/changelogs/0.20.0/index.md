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

- A New Renderable for Point Clouds (`RenderableBillboardsCloud` -> `RenderablePointCloud`) [Details](./conversion.md#a-new-renderable-for-point-clouds)
- `RenderableSphere` &rarr; `RenderableSphereImageOnline` & `RenderableSphereImageLocal` (@TODO: Provide details)
- Property identifier changes
  - RenderableAtmosphere: `EclipseHardShadowsInfo` &rarr; `EclipseHardShadows`
  - RenderableEclipseCone: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderableShadowCylinder: `AmountOfPoints` &rarr; `NumberOfPoints`
  - RenderablePointCloud: `Coloring.OutlineWeight` &rarr; `Coloring.OutlineWidth`
  - RenderableOrbitalKepler: `Appearance.OutlineWeight` &rarr; `Appearance.OutlineWidth`
  - All ScreenSpaceRenderables: `Gamma` -> `GammaOffset`

:::{toctree}
:maxdepth: 1
:hidden:

conversion
:::
