



(spacecraftinstruments_renderableplanetprojection)=
# RenderablePlanetProjection

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

*   - `ColorTexturePaths`
    - The texture path selected in this property is used as the base texture that is applied to the planet prior to any image projections. This menu always contains an empty option for not using a color map. If this value is specified in an asset, the last texture is used.
    - `Table`
    
    -   [Table parameters](#RenderablePlanetProjectionColorTexturePaths-target) 
    
    - {bdg-info}`No`
    
*   - `HeightTexturePaths`
    - The texture path selected in this property is used as the height map on the planet. This menu always contains an empty option for not using a heightmap. If this value is specified in an asset, the last texture is used.
    - `Table`
    
    -   [Table parameters](#RenderablePlanetProjectionHeightTexturePaths-target) 
    
    - {bdg-info}`No`
    
*   - `Projection`
    - Contains information about projecting onto this planet.
    - `Table`
    
    - [ProjectionComponent](#spacecraftinstruments_projectioncomponent)
    
    - {bdg-info}`No`
    
*   - `Radius`
    - This value specifies the radius of this sphere in meters.
    - `Double, or Vector3<double>`
    
    - Value of type 'Double', or Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `Segments`
    - This value specifies the number of segments that this sphere is split into.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `AmbientBrightness`
    - This value determines the ambient brightness of the dark side of the planet.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `HeightExaggeration`
    - This value determines the level of height exaggeration that is applied to a potential height field. A value of '0' inhibits the height field, whereas a value of '1' uses the measured height field.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MaxProjectionsPerFrame`
    - The maximum number of image projections to perform per frame. Useful to avoid freezing the system for large delta times.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `MeridianShift`
    - If this value is enabled, a shift of the meridian by 180 degrees is performed. This is a fix especially for Pluto height maps, where the definition of the meridian has changed through the New Horizons mission and this requires this shift.
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






(RenderablePlanetProjectionColorTexturePaths-target)=
::::{dropdown} Table parameters for `ColorTexturePaths`
The texture path selected in this property is used as the base texture that is applied to the planet prior to any image projections. This menu always contains an empty option for not using a color map. If this value is specified in an asset, the last texture is used.


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

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::




(RenderablePlanetProjectionHeightTexturePaths-target)=
::::{dropdown} Table parameters for `HeightTexturePaths`
The texture path selected in this property is used as the height map on the planet. This menu always contains an empty option for not using a heightmap. If this value is specified in an asset, the last texture is used.


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

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::


















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 34
local transforms = asset.require("./transforms")
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")
local kernels = asset.require("./kernels")
local coreKernels = asset.require("spice/core")



local textures = asset.resource({
  Name = "Charon Textures",
  Type = "HttpSynchronization",
  Identifier = "charon_textures",
  Version = 3
})


local CharonRadius = 603500

local CharonProjection = {
  Identifier = "CharonProjection",
  Parent = transforms.PlutoBarycenterAccurate.Identifier,
  Transform = {
    Translation = {
      Type = "SpiceTranslation",
      Target = kernels.ID.Charon,
      Observer = kernels.ID.PlutoBarycenter
    },
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = kernels.Frame.Charon,
      DestinationFrame = coreKernels.Frame.Galactic
    }
  },
  Renderable = {
    Type = "RenderablePlanetProjection",
    Radius = CharonRadius,
    Segments = 350,
    ColorTexturePaths = {
      textures .. "NH_Charon_mosaic.png",
      textures .. "NH_Charon_mosaic_8192.png"
    },
    HeightTexturePaths = {
      textures .. "NH_Charon_DTM.png",
      textures .. "NH_Charon_DTM_8192.png"
    },
    MeridianShift = true,
    Projection = {
      Observer = kernels.ID.NewHorizons,
      Target = kernels.ID.Charon,
      Aberration = "NONE",
      AspectRatio = 2,
      Instrument = {
        Name = kernels.Frame.Lorri,
        Method = "ELLIPSOID",
        Aberration = "NONE",
        Fovy = 0.2907,
        Aspect = 1,
        Near = 0.2,
        Far = 10000
      },
      PotentialTargets = {
        kernels.ID.Pluto,
        kernels.ID.Charon
      }
    }
  },
  GUI = {
    Path = "/Solar System/Dwarf Planets/Pluto",
    Name = "Charon Projection"
  }
}

local CharonText = {
  Identifier = "CharonText",
  Parent = CharonProjection.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = { 0, -1000000.0, 0 }
    }
  },
  Renderable = {
    Type = "RenderablePlaneImageLocal",
    Size = 19952623.15,
    Origin = "Center",
    Billboard = true,
    Texture = textures .. "Charon-Text.png",
    BlendMode = "Additive"
  },
  GUI = {
    Name = "Charon Text",
    Path = "/Solar System/Dwarf Planets/Pluto"
  }
}

local CharonShadow = {
  Identifier = "CharonShadow",
  Parent = CharonProjection.Identifier,
  Renderable = {
    Type = "RenderableShadowCylinder",
    Opacity = 0.25,
    TerminatorType = "PENUMBRAL",
    LightSource = coreKernels.ID.Sun,
    Observer = kernels.ID.NewHorizons,
    Body = kernels.ID.Charon,
    BodyFrame = kernels.Frame.Charon,
    Aberration = "NONE"
  },
  GUI = {
    Name = "Charon Shadow",
    Path = "/Solar System/Dwarf Planets/Pluto"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(CharonProjection)
  openspace.addSceneGraphNode(CharonText)
  openspace.addSceneGraphNode(CharonShadow)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(CharonShadow)
  openspace.removeSceneGraphNode(CharonText)
  openspace.removeSceneGraphNode(CharonProjection)
end)

asset.export(CharonProjection)
asset.export(CharonText)
asset.export(CharonShadow)

:::
:::


