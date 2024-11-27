



(base_renderable_time_varying_sphere)=
# RenderableTimeVaryingSphere

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

*   - `TextureSource`
    - A directory containing images that are loaded from disk and used for texturing the sphere. The images are expected to be equirectangular projections.
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
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
:emphasize-lines: 21
local propertyHelper = asset.require("util/property_helper")
local transforms = asset.require("./transforms")



local textureSourcePath = asset.resource({
  Type = "HttpSynchronization",
  Name = "euv_textures_bastille_event",
  Identifier = "euv_textures_bastille_event",
  Version = 1
})


local EUVLayer = {
  Identifier = "EUV-Layer-bastille-day-2000",
  Parent = transforms.SunIAU.Identifier,
  -- TODO Elon: 21 April 2022. Interaction sphere should not depend on the transform scale.
  -- InteractionSphere = sunAsset.Sun.Renderable.Radii[1] * 1.05,
  InteractionSphere = 696000000,
  Renderable = {
    Type = "RenderableTimeVaryingSphere",
    Size = 6.96E8, -- Slightly bigger than the sun renderable,
    Enabled = true,
    TextureSource = textureSourcePath,
    Opacity = 1,
    Segments = 132
  },
  GUI = {
    Name = "EUV Layer",
    Path = "/Solar System/Sun",
    Description = [[Texture sequence of an extreme ultra violet (EUV) simulation, during
      the CME. This asset contains data from 2000-07-14 08:38 to 2000-07-14 19:48]]
  }
}

local ToggleEuv = {
  Identifier = "os.solarsystem.ToggleEuv",
  Name = "Toggle EUV layer",
  Command = [[
    if openspace.propertyValue("Scene.EUV-Layer-bastille-day-2000.Renderable.Enabled") then
      openspace.setPropertyValueSingle(
        "Scene.EUV-Layer-bastille-day-2000.Renderable.Fade",
        0.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear",
        'openspace.setPropertyValueSingle("Scene.EUV-Layer-bastille-day-2000.Renderable.Enabled", false)'
      )
    else
      openspace.setPropertyValueSingle("Scene.EUV-Layer-bastille-day-2000.Renderable.Enabled", true)
      openspace.setPropertyValueSingle(
        "Scene.EUV-Layer-bastille-day-2000.Renderable.Fade",
        1.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear"
      )
    end
  ]],
  Documentation = "Toggle EUV layer of sun",
  GuiPath = "/Bastille-Day 2000",
  IsLocal = false
}


asset.onInitialize(function()
  openspace.action.registerAction(ToggleEuv)
  openspace.addSceneGraphNode(EUVLayer)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(EUVLayer)
  openspace.action.removeAction(ToggleEuv)
end)

asset.export("ToggleEuv", ToggleEuv.Identifier)
asset.export(EUVLayer)



asset.meta = {
  Name = "Predictive Science Inc. EUV texture sequence Bastille Days",
  Description = [[Texture sequence of an extreme ultraviolet (EUV) simulation during the CME]],
  Author = "CCMC, OpenSpace team",
  URL = "https://dx.doi.org/10.3847/1538-4357/aab36d",
  License = "CC-BY"
}

:::
:::


