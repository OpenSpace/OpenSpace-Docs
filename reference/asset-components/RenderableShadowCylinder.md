



(spacecraftinstruments_renderableshadowcylinder)=
# RenderableShadowCylinder

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

*   - `Aberration`
    - The aberration method that is used for computing the shadow cylinder. The options are "NONE", "LT" (Light Time), "LT + S" (Light Time Stellar), "CN" (Converged Newtonian), and "CN + S" (Converged Newtonian Stellar).
    - `String`
    
    - In list { NONE, LT, LT+S, CN, CN+S } 
    
    - {bdg-info}`No`
    
*   - `Body`
    - The SPICE name of target body that is used as the shadow caster.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `BodyFrame`
    - The SPICE name of the reference frame in which the shadow cylinder is expressed.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `LightSource`
    - The SPICE name of the object that is used as the illuminator for computing the shadow cylinder.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Observer`
    - The SPICE name of the object that is the observer.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `TerminatorType`
    - Determines the type of terminator to use for calculating the shadow eclipse.
    - `String`
    
    - In list { UMBRAL, PENUMBRAL } 
    
    - {bdg-info}`No`
    
*   - `NumberOfPoints`
    - The number of control points used for constructing the shadow geometry. The higher this number, the more detailed the shadow is, but it will have a negative impact on the performance.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `ShadowColor`
    - The color used for the shadow cylinder.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `ShadowLength`
    - A factor that controls the length of the shadow that is cast by the target object. The total length of the shadow is equal to the distance from the target to the light source multiplied with this value.
    - `Double`
    
    - Value of type 'Double' 
    
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
:emphasize-lines: 99
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


