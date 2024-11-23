



(galaxy_renderablegalaxy)=
# RenderableGalaxy

_Inherits [Renderable](#renderable)_




## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Points`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableGalaxyPoints-target) 
    
    - {bdg-info}`No`
    
*   - `Volume`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableGalaxyVolume-target) 
    
    - {bdg-info}`No`
    
*   - `AbsorptionMultiply`
    - A unit-less scale factor for the probability of dust absorbing a light particle. The amount of absorption determines the spectrum of the light that is emitted from the galaxy.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `EmissionMultiply`
    - A unit-less scale factor for the amount of light being emitted by dust in the galaxy.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `RaycastingShader`
    - If specified, the default raycasting shader is overwritten and the shader at this location is used instead.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `Rotation`
    - The internal rotation of the volume rendering in Euler angles.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `StarRenderingEnabled`
    - Decides whether the point-based star rendering component of the galaxy rendering should be enabled or not. If disabled, the point-based star rendering is skipped.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `StarRenderingMethod`
    - The rendering method used for visualizing the stars.
    - `String`
    
    - In list { Points, Billboards } 
    
    - Yes
    
*   - `StepSizeInfo`
    - Determines the distance between steps taken in the volume rendering. The lower the number is, the better the rendering looks, but also takes more computational resources to render.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `VolumeRenderingEnabled`
    - Decides whether the volume rendering component of the galaxy rendering should be enabled or not. If disabled, the volume rendering is skipped.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



### Inherited members from [Renderable](#renderable)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `DimInAtmosphere`
    - Decides if the object should be dimmed (i.e. faded out) when the camera is in the sunny part of an atmosphere.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - Determines whether this object will be visible or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of this renderable. A value of 0 means completely transparent
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `RenderBinMode`
    - A value that specifies if the renderable should be rendered in the Background, Opaque, Pre-/PostDeferredTransparency, Overlay, or Sticker rendering step.
    - `String`
    
    - In list { Background, Opaque, PreDeferredTransparent, PostDeferredTransparent, Overlay } 
    
    - Yes
    
*   - `Tag`
    - A single tag or a list of tags that this renderable will respond to when setting properties
    - `Table, or String`
    
    - Value of type 'Table', or Value of type 'String' 
    
    - Yes
    
*   - `Type`
    - The type of the renderable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::






(RenderableGalaxyPoints-target)=
::::{dropdown} Table parameters for `Points`



* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `EnabledPointsRatio`
    - The ratio of point-like stars that are rendered to produce the overall galaxy image. At a value of 0, no stars are rendered, at a value of 1 all points contained in the dataset are rendered. The specific value chosen is a compromise between image fidelity and rendering performance.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Filename`
    - 
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - 
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
:::



::::




(RenderableGalaxyVolume-target)=
::::{dropdown} Table parameters for `Volume`



* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Dimensions`
    - 
    - `Vector3<int>`
    
    - Value of type 'Vector3<int>' 
    
    - {bdg-info}`No`
    
*   - `Downscale`
    - The downscaling factor used when rendering the volume.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Filename`
    - 
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Size`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `Steps`
    - The number of integration steps used during the raycasting procedure.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



::::




















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 28
local transforms = asset.require("scene/solarsystem/sun/transforms")



local data = asset.resource({
  Name = "Milkyway Volume Data",
  Type = "HttpSynchronization",
  Identifier = "milkyway_volume_data",
  Version = 1
})


local KiloParsec = 3.086E19

local MilkyWayVolume = {
  Identifier = "MilkyWayVolume_CustomShader",
  Parent = transforms.SolarSystemBarycenter.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      -- The center of the Milky Way is approximately 8 kiloparsec from the Sun.
      -- The x-axis of galactic coordinates points from the sun towards the center
      -- of the galaxy.
      Position = { 8 * KiloParsec, 0, 0 }
    }
  },
  Renderable = {
    Type = "RenderableGalaxy",
    StepSize = 0.01,
    AbsorptionMultiply = 200,
    EmissionMultiply = 250,
    Rotation = { math.pi, 3.1248, 4.45741 },
    RaycastingShader = asset.resource("galaxyraycast.glsl"),
    Volume = {
      Type = "Volume",
      Filename = data .. "MilkyWayRGBAVolume1024x1024x128.raw",
      Dimensions = { 1024, 1024, 128 },
      Size = { 1.2E21, 1.2E21, 0.15E21 },
      Downscale = 0.4
    },
    Points = {
      Type = "Points",
      Filename = data .. "MilkyWayPoints.off",
      EnabledPointsRatio = 0.3,
      Texture = data .. "halo.png"
    }
  },
  GUI = {
    Path = "/Milky Way",
    Name = "Milky Way Volume (Custom Shader)",
    Description = "Volumetric rendering of Milky Way galaxy based on simulation from NAOJ"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(MilkyWayVolume)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(MilkyWayVolume)
end)

asset.export(MilkyWayVolume)



asset.meta = {
  Name = "Milky Way Volume",
  Description = [[Volumetric rendering of Milky Way galaxy based on simulations from "
  "NAOJ with a custom shader]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT License"
}

:::
:::


