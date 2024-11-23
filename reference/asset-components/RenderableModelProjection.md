



(spacecraftinstruments_renderablemodelprojection)=
# RenderableModelProjection

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

*   - `GeometryFile`
    - The file or files that should be loaded, that specifies the model to load. The file can contain filesystem tokens or can be specified relative to the location of the asset file.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Projection`
    - Contains information about projecting onto this planet.
    - `Table`
    
    - [ProjectionComponent](#spacecraftinstruments_projectioncomponent)
    
    - {bdg-info}`No`
    
*   - `InvertModelScale`
    - By default the given `ModelScale` is used to scale down the model. By setting this setting to true the scaling is inverted to that the model is instead scaled up with the given `ModelScale`.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ModelScale`
    - The scale of the model. For example if the model is in centimeters then `ModelScale = "Centimeter"` or `ModelScale = 0.01`.
    - `String, or Double`
    
    - In list { Nanometer, Micrometer, Millimeter, Centimeter, Decimeter, Meter, Kilometer, Thou, Inch, Foot, Yard, Chain, Furlong, Mile }, or Value of type 'Double' 
    
    - Yes
    
*   - `PerformShading`
    - If true, the model will be shaded based on the location of the Sun. If false, shading is disabled and the model is fully illuminated.
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
















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 42
local transforms = asset.require("./transforms")
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")
local kernels = asset.require("./kernels")
local coreKernels = asset.require("spice/core")



local models = asset.resource({
  Name = "Bennu Models",
  Type = "HttpSynchronization",
  Identifier = "bennu_models",
  Version = 2
})

local images = asset.resource({
  Name = "Bennu Images Approach",
  Type = "HttpSynchronization",
  Identifier = "osirisrex_bennu_images_approach",
  Version = 1
})

local imagesA = asset.resource({
  Name = "Bennu Images A",
  Type = "HttpSynchronization",
  Identifier = "osirisrex_bennu_images_orbit_a",
  Version = 1
})


local BennuProjection = {
  Identifier = "BennuProjection",
  Parent = transforms.BennuBarycenter.Identifier,
  Transform = {
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = kernels.Frame.Bennu,
      DestinationFrame = coreKernels.Frame.Galactic
    }
  },
  Renderable = {
    Enabled = true,
    Type = "RenderableModelProjection",
    Body = kernels.ID.Bennu,
    GeometryFile = models .. "Bennu_v20_200k_an.obj",
    Projection = {
      Sequence = { images, imagesA },
      SequenceType = "image-sequence",
      Observer = kernels.ID.OsirisRex,
      Target = kernels.ID.Bennu,
      Aberration = "NONE",
      TextureMap = true,
      DataInputTranslation = {
        Instruments = {
          ORX_OCAMS_POLYCAM = {
            DetectorType = "Camera",
            Spice = { kernels.Frame.Polycam },
          },
        },
        Target = {
          Read = {
            "TARGET_NAME",
            "INSTRUMENT_HOST_NAME",
            "INSTRUMENT_ID",
            "START_TIME",
            "STOP_TIME"
          },
          Convert = {
            ["2101955"] = { "2101955" },
            ["OSIRIS-REX"] = { "OSIRIS-REX" },
            ["ORX_OCAMS_POLYCAM"] = { "ORX_OCAMS_POLYCAM" },
          }
        }
      },
      Instrument = { -- INVALID DATA - JUST FOR TESTING
        Name = kernels.Frame.Polycam,
        Method = "ELLIPSOID",
        Aberration = "NONE",
        Fovy = 0.792,
        Aspect = 1,
        Near = 0.01,
        Far = 1000000
      }
    }
  },
  GUI = {
    Name = "Bennu Projection",
    Path = "/Solar System/Asteroid"
  }
}

local BennuTrail = {
  Identifier = "BennuTrail",
  Parent = sunTransforms.SolarSystemBarycenter.Identifier,
  Renderable = {
    Type = "RenderableTrailTrajectory",
    Translation = {
      Type = "SpiceTranslation",
      Target = kernels.ID.Bennu,
      Observer = coreKernels.ID.SolarSystemBarycenter
    },
    Color = { 0.4, 0.0, 0.7 },
    StartTime = "2015 JAN 01 00:00:00.000",
    EndTime = "2023 MAY 31 00:00:00.000",
    SampleInterval = 3600
  },
  GUI = {
    Name = "Bennu Trail",
    Path = "/Solar System/Asteroid"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(BennuProjection)
  openspace.addSceneGraphNode(BennuTrail)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(BennuTrail)
  openspace.removeSceneGraphNode(BennuProjection)
end)

asset.export(BennuProjection)
asset.export(BennuTrail)

:::
:::


