



(space_renderableeclipsecone)=
# RenderableEclipseCone

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

*   - `LightSource`
    - The SPICE name of the object that is used as the illuminator when computing the shadow cylinder.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `LightSourceFrame`
    - The SPICE name of the body-fixed reference frame for the light source.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Shadowee`
    - The SPICE name of object that is receiving the shadow from the shadower.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Shadower`
    - The SPICE name of the object that is casting the shadow on the shadowee.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `ShadowerFrame`
    - The SPICE name of the body-fixed reference frame for the shadower.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `NumberOfPoints`
    - The number of control points used for constructing the shadow geometry. The higher this number, the more detailed the shadow is. However, it will have a negative impact on the performance. Also note that rendering errors will occur if this value is an even number.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `PenumbralShadowColor`
    - The color for the shadow cylinder that represents the penumbral shadow.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `ShadowLength`
    - A factor that controls the length of the rendered shadow cone. The total length will be the distance from the shadower to the shadowee multiplied by this value.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ShowPenumbralShadow`
    - Decides whether the penumbral portion of the shadow should be shown.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ShowUmbralShadow`
    - Decides whether the umbral portion of the shadow should be shown.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UmbralShadowColor`
    - The color for the shadow cylinder that represents the umbral shadow.
    - `Color4`
    
    - Value of type 'Color4' 
    
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
:emphasize-lines: 10
local transforms = asset.require("scene/solarsystem/planets/earth/moon/moon")
local coreKernels = asset.require("spice/core")



local EarthMoonShadow = {
  Identifier = "EarthMoonShadow",
  Parent = transforms.Moon.Identifier,
  Renderable = {
    Type = "RenderableEclipseCone",
    Opacity = 1.0,
    ShadowLength = 1.0,
    UmbralShadowColor = { 0.85, 1.0, 1.0, 0.20 },
    PenumbralShadowColor = { 0.35, 0.35, 0.35, 0.29 },
    LightSource = coreKernels.ID.Sun,
    LightSourceFrame = coreKernels.Frame.Sun,
    Shadower = coreKernels.ID.Moon,
    ShadowerFrame = coreKernels.Frame.Moon,
    Shadowee = coreKernels.ID.Earth
  },
  GUI = {
    Name = "Earth/Moon Shadow",
    Path = "/Solar System/Planets/Earth"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(EarthMoonShadow)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(EarthMoonShadow)
end)

asset.export(EarthMoonShadow)



asset.meta = {
  Name = "Eclipse Shadow",
  Description = "The penumbral and umbral shadow eclipses for the Earth-Moon system",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


