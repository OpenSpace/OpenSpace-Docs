



(space_transform_gp)=
# GPTranslation

_Inherits [Translation](#core_transform_translation)_




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

*   - `File`
    - Specifies the filename of the general pertubation file
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Format`
    - A NORAD-style Two-Line element Orbit Mean-Elements Message in the KVN notation JPL's Small Bodies Database The file format that is contained in the file
    - `String`
    
    - In list { TLE, OMM, SBDB } 
    
    - {bdg-info}`No`
    
*   - `Element`
    - Specifies the element within the file that should be used in case the file provides multiple general pertubation elements. Defaults to 1.
    - `Integer`
    
    - Greater than: 0 
    
    - Yes
    
:::



### Inherited members from [Translation](#core_transform_translation)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - The type of translation that is described in this element. The available types of translations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Translation type 
    
    - {bdg-info}`No`
    
:::












## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 21, 46
local transforms = asset.require("scene/solarsystem/planets/earth/transforms")
local coreKernels = asset.require("spice/core")



local omm = asset.resource({
  Name = "Satellite OMM Data (Hubble)",
  Type = "UrlSynchronization",
  Identifier = "satellite_omm_data_hst",
  Url = "https://www.celestrak.com/NORAD/elements/gp.php?CATNR=20580&FORMAT=kvn",
  Filename = "hst.txt",
  SecondsUntilResync = openspace.time.secondsPerDay()
})


local HubblePosition = {
  Identifier = "HubblePosition",
  Parent = transforms.EarthInertial.Identifier,
  Transform = {
    Translation = {
      Type = "GPTranslation",
      Observer = transforms.EarthInertial.Identifier,
      File = omm .. "hst.txt",
      Format = "OMM"
    },
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = coreKernels.Frame.Galactic,
      DestinationFrame = coreKernels.Frame.J2000
    }
  },
  Tag = { "earth_satellite", "hubble" },
  GUI = {
    Name = "Hubble Position",
    Path = "/Solar System/Planets/Earth/Satellites/Hubble",
    Hidden = true
  }
}

local HubbleTrail = {
  Identifier = "HubbleTrail",
  Parent = transforms.EarthInertial.Identifier,
  Renderable = {
    Type = "RenderableTrailOrbit",
    Translation = {
      Type = "GPTranslation",
      Observer = transforms.EarthInertial.Identifier,
      File = omm .. "hst.txt",
      Format = "OMM"
    },
    RenderBinMode = "PostDeferredTransparent",
    Color = { 0.0, 0.902, 0.6 },
    Fade = 1.5,
    Resolution = 320
  },
  Tag = { "earth_satellite", "hubble" },
  GUI = {
    Name = "Hubble Trail",
    Path = "/Solar System/Planets/Earth/Satellites/Hubble"
  }
}


asset.onInitialize(function()
  local hubble = openspace.space.readKeplerFile(omm .. "hst.txt", "OMM")
  HubbleTrail.Renderable.Period = hubble[1].Period / (60 * 60 * 24)

  openspace.addSceneGraphNode(HubblePosition)
  openspace.addSceneGraphNode(HubbleTrail)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(HubbleTrail)
  openspace.removeSceneGraphNode(HubblePosition)
end)

asset.export(HubblePosition)
asset.export(HubbleTrail)



asset.meta = {
  Name = "Hubble Space Telescope Trail",
  Description = "Position and Trail for Hubble Space Telescope, trail from Celestrak",
  Author = "Dan Tell",
  URL = "www.calacademy.org",
  License = "CC-BY"
}

:::
:::


