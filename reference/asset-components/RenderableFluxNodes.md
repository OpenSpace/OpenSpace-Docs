



(space_renderable_flux_nodes)=
# RenderableFluxNodes

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

*   - `ColorTablePath`
    - Color Table/Transfer Function to use for 'By Flux Value' coloring.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `SourceFolder`
    - Path to a source folder with the three binary files in it.
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
*   - `ColorTableRange`
    - Valid range for the color table as the exponent, with base 10, of flux values. [Min, Max].
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `EnergyBin`
    - Select which energy bin you want to show. GOES = Geostationary Operational Environmental Satellites. Emin01 is values > 10 MeV, Default is Emin03 where values > 100 MeV.
    - `Integer`
    
    - Value of type 'Integer' 
    
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
:emphasize-lines: 26
local heliosphereTransforms = asset.require("scene/solarsystem/sun/transforms_heliosphere")
local propertyHelper = asset.require("util/property_helper")
local rot = asset.require("./carrington_to_heeq_rotation")



local fluxNodesBinaries = asset.resource({
  Name = "Bastille day Flux nodes binaries",
  Type = "HttpSynchronization",
  Identifier = "bastille_day_streamnodes_binaries",
  Version = 1
})


-- FluxNodes from binaries
local Fluxnodes = {
  Identifier = "MAS-MHD-FluxNodes-bastille-day-2000",
  Parent = heliosphereTransforms.HEEQ180ReferenceFrame.Identifier,
  -- TODO Elon: 21 April 2022. Interaction sphere should not depend on the transform scale.
  -- InteractionSphere = sunAsset.Sun.Renderable.Radii[1] * 1.05,
  InteractionSphere = 695700000.0,
  Transform = {
    Rotation = rot.CarringtonLongitudeToHEEQ180Rotation
  },
  Renderable = {
    Type = "RenderableFluxNodes",
    SourceFolder = fluxNodesBinaries,
    ColorTablePath = asset.resource("transferfunctions/CMR.txt"),
    ColorTableRange = { -2.0, 4.0 }
  },
  GUI = {
    Path = "/Solar System/Heliosphere/Bastille Day 2000",
    Name = "Flux Nodes",
    Description = [[Flux nodes for the bastille day CME event. This asset contains data
      from 2000-07-14 08:38 to 2000-07-14 19:48]]
  }
}

local ToggleFluxnodes = {
  Identifier = "os.bastilleday.fluxnodes.ToggleFluxnodes",
  Name = "Toggle flux nodes",
  Command = [[
    if openspace.propertyValue("Scene.MAS-MHD-FluxNodes-bastille-day-2000.Renderable.Enabled") then
      openspace.setPropertyValueSingle(
        "Scene.MAS-MHD-FluxNodes-bastille-day-2000.Renderable.Fade",
        0.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear",
        'openspace.setPropertyValueSingle("Scene.MAS-MHD-FluxNodes-bastille-day-2000.Renderable.Enabled", false)'
      )
    else
      openspace.setPropertyValueSingle("Scene.MAS-MHD-FluxNodes-bastille-day-2000.Renderable.Enabled", true)
      openspace.setPropertyValueSingle(
        "Scene.MAS-MHD-FluxNodes-bastille-day-2000.Renderable.Fade",
        1.0,
        openspace.propertyValue("OpenSpaceEngine.FadeDuration"),
        "Linear"
      )
    end
  ]],
  Documentation = "Toggle flux node rendering of CME",
  GuiPath = "/Bastille-Day 2000",
  IsLocal = false
}


asset.onInitialize(function()
  openspace.action.registerAction(ToggleFluxnodes)
  openspace.addSceneGraphNode(Fluxnodes)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Fluxnodes)
  openspace.action.removeAction(ToggleFluxnodes)
end)

asset.export(Fluxnodes)
asset.export("ToggleFluxnodes", ToggleFluxnodes.Identifier)



asset.meta = {
  Name = "Predictive Science Inc. Flux nodes Bastille Day",
  Description = "Flux nodes for the bastille day CME event",
  Author = "CCMC, Christian Adamsson, Emilie Ho",
  URL = "https://dx.doi.org/10.3847/1538-4357/aab36d",
  License = "CC-BY"
}

:::
:::


