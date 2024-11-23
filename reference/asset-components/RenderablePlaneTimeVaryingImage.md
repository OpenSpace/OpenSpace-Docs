



(base_renderable_plane_time_varying_image)=
# RenderablePlaneTimeVaryingImage

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

*   - `Size`
    - The size of the plane in meters.
    - `Double, or Vector2<double>`
    
    - Value of type 'Double', or Value of type 'Vector2<double>' 
    
    - {bdg-info}`No`
    
*   - `SourceFolder`
    - An image directory that is loaded from disk and contains the textures to use for this plane.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `AutoScale`
    - Decides whether the plane should automatically adjust in size to match the aspect ratio of the content. Otherwise it will remain in the given size.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Billboard`
    - Specifies whether the plane should be a billboard, which means that it is always facing the camera. If it is not, it can be oriented using other transformations.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `BlendMode`
    - Determines the blending mode that is applied to this plane.
    - `String`
    
    - In list { Normal, Additive } 
    
    - Yes
    
*   - `MirrorBackside`
    - If false, the image plane will not be mirrored when viewed from the backside. This is usually desirable when the image shows data at a specific location, but not if it is displaying text for example.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MultiplyColor`
    - An RGB color to multiply with the plane's texture. Useful for applying a color to grayscale images.
    - `Color3`
    
    - Value of type 'Color3' 
    
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
:emphasize-lines: 32, 61
local propertyHelper = asset.require("util/property_helper")
local transforms = asset.require("scene/solarsystem/sun/transforms_heliosphere")
local rot = asset.require("./carrington_to_heeq_rotation")



local TexturesPathEquatorial = asset.resource({
Type = "HttpSynchronization",
  Name = "cutplanes_textures",
  Identifier = "cutplanes_textures",
  Version = 1
})

local TexturesPathMeridial = asset.resource({
  Type = "HttpSynchronization",
  Name = "cutplane_meridial_textures",
  Identifier = "cutplane_meridial_textures",
  Version = 1
})


local EquatorialCutplane = {
  Identifier = "EquatorialCutplane-bastille-day-2000",
  Parent = transforms.HEEQ180ReferenceFrame.Identifier,
  -- TODO Elon: 21 April 2022. Interaction sphere should not depend on the transform scale.
  -- InteractionSphere = sunAsset.Sun.Renderable.Radii[1] * 1.05,
  InteractionSphere = 695700000.0,
  Transform = {
    Rotation = rot.CarringtonLongitudeToHEEQ180Rotation
  },
  Renderable = {
    Type = "RenderablePlaneTimeVaryingImage",
    Size = 157000000000,
    Enabled = true,
    SourceFolder = TexturesPathEquatorial,
    BlendMode = "Normal",
    MirrorBackside = false,
    Opacity = 0.7
  },
  GUI = {
    Name = "Cutplane Equitorial",
    Path = "/Solar System/Heliosphere/Bastille Day 2000",
    Description = [[Equatorial cutplane sequence for the bastille day CME event. This
      asset contains data from 2000-07-14 08:38 to 2000-07-14 12:00]]
  }
}

local MeridialCutplane = {
  Identifier = "MeridialCutplane-bastille-day-2000",
  Parent = transforms.HEEQ180ReferenceFrame.Identifier,
  -- TODO Elon: 21 April 2022. Interaction sphere should not depend on the transform scale.
  -- InteractionSphere = sunAsset.Sun.Renderable.Radii[1] * 1.05,
  InteractionSphere = 695700000,
  Transform = {
    Rotation = {
      Type = "StaticRotation",
      Rotation = { -math.pi/2, -math.pi, 0.0 }
    }
  },
  Renderable = {
    Type = "RenderablePlaneTimeVaryingImage",
    Size = 157000000000,
    Enabled = true,
    SourceFolder = TexturesPathMeridial,
    BlendMode = "Normal",
    MirrorBackside = false,
    Opacity = 0.7
  },
  GUI = {
    Name = "Cutplane Meridial",
    Path = "/Solar System/Heliosphere/Bastille Day 2000",
    Description = [[Meridial cutplane sequence for the bastille day CME event. This asset
      contains data from 2000-07-14 08:38 to 2000-07-14 12:00]]
  }
}

local ToggleEquatorial = {
  Identifier = "os.bastilleday.fluxnodescutplane.ToggleEquatorial",
  Name = "Toggle equatorial cutplane",
  Command = [[
    if openspace.propertyValue("Scene.EquatorialCutplane-bastille-day-2000.Renderable.Enabled") then
      openspace.setPropertyValueSingle(
        "Scene.EquatorialCutplane-bastille-day-2000.Renderable.Fade",
        0.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear",
        'openspace.setPropertyValueSingle("Scene.EquatorialCutplane-bastille-day-2000.Renderable.Enabled", false)'
      )
    else
      openspace.setPropertyValueSingle("Scene.EquatorialCutplane-bastille-day-2000.Renderable.Enabled", true)
      openspace.setPropertyValueSingle(
        "Scene.EquatorialCutplane-bastille-day-2000.Renderable.Fade",
        1.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear"
      )
    end
  ]],
  Documentation = "Toggle equatorial cutplane of CME",
  GuiPath = "/Bastille-Day 2000",
  IsLocal = false
}

local ToggleMeridial = {
  Identifier = "os.bastilleday.fluxnodescutplane.ToggleMeridial",
  Name = "Toggle meridial cutplane",
  Command = [[
    if openspace.propertyValue("Scene.MeridialCutplane-bastille-day-2000.Renderable.Enabled") then
      openspace.setPropertyValueSingle(
        "Scene.MeridialCutplane-bastille-day-2000.Renderable.Fade",
        0.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear",
        'openspace.setPropertyValueSingle("Scene.MeridialCutplane-bastille-day-2000.Renderable.Enabled", false)'
      )
    else
      openspace.setPropertyValueSingle("Scene.MeridialCutplane-bastille-day-2000.Renderable.Enabled", true)
      openspace.setPropertyValueSingle(
        "Scene.MeridialCutplane-bastille-day-2000.Renderable.Fade",
        1.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear"
      )
    end
  ]],
  Documentation = "Toggle meridial cutplane of CME",
  GuiPath = "/Bastille-Day 2000",
  IsLocal = false
}


asset.onInitialize(function()
  openspace.action.registerAction(ToggleEquatorial)
  openspace.action.registerAction(ToggleMeridial)
  openspace.addSceneGraphNode(EquatorialCutplane)
  openspace.addSceneGraphNode(MeridialCutplane)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(MeridialCutplane)
  openspace.removeSceneGraphNode(EquatorialCutplane)
  openspace.action.removeAction(ToggleEquatorial)
  openspace.action.removeAction(ToggleMeridial)
end)

asset.export("ToggleEquatorial", ToggleEquatorial.Identifier)
asset.export("ToggleMeridial", ToggleMeridial.Identifier)
asset.export(EquatorialCutplane)
asset.export(MeridialCutplane)



asset.meta = {
  Name = "Predictive Science Inc. Cutplanes Bastille Days",
  Description = "Cutplanes for the bastille day CME event",
  Author = "CCMC, Christian Adamsson, Emilie Ho",
  URL = "https://dx.doi.org/10.3847/1538-4357/aab36d",
  License = "CC-BY"
}

:::
:::


