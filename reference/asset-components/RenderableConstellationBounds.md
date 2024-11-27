



(space_renderable_constellationbounds)=
# RenderableConstellationBounds

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

*   - `File`
    - A file that contains the vertex locations of the constellations bounds.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Color`
    - The color of the lines.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Labels`
    - The labels for the constellations.
    - `Table`
    
    - [LabelsComponent](#labelscomponent)
    
    - Yes
    
*   - `LineWidth`
    - The line width of the constellation.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `NamesFile`
    - Specifies the file that contains the mapping between constellation abbreviations and full names of the constellations. If this value is empty, the abbreviations are used as the full names.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `Selection`
    - The constellations that are selected are displayed on the celestial sphere.
    - `Table`
    
    -   [Table parameters](#RenderableConstellationBoundsSelection-target) 
    
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
















(RenderableConstellationBoundsSelection-target)=
::::{dropdown} Table parameters for `Selection`
The constellations that are selected are displayed on the celestial sphere.


* Optional: Yes


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
:emphasize-lines: 20
local coreKernels = asset.require("spice/core")



local data = asset.resource({
  Name = "Constellation Files",
  Type = "HttpSynchronization",
  Identifier = "digitaluniverse_constellations_data",
  Version = 1
})


local zodiacs = {
  "CNC", "TAU", "PSC", "ARI", "LIB", "AQR", "CAP", "SCO", "VIR", "SGR", "GEM", "LEO"
}

local Object = {
  Identifier = "ConstellationBounds",
  Renderable = {
    Type = "RenderableConstellationBounds",
    Enabled = false,
    File = data .. "bound_20.dat",
    NamesFile = data .. "constellations.dat",
    -- Selection = zodiacs
  },
  Transform = {
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = coreKernels.Frame.J2000,
      DestinationFrame = coreKernels.Frame.Galactic
    },
    Scale = {
      Type = "StaticScale",
      Scale = 10e17
    }
  },
  GUI = {
    Name = "Constellation Boundaries",
    Path = "/Milky Way/Constellations",
    Description = [[As a continent is divided into countries, astronomers divide the sky
      into 88 regions called constellations. Every object falls into one of these 88
      regions. The boundaries of these regions are shown in this asset. Use these in
      concert with the constellation labels. Census: 88 constellations.]]
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Object)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Object)
end)

asset.export(Object)



asset.meta = {
  Name = "Constellation Bounds",
  Description = Object.GUI.Description,
  Author = "Brian Abbott (AMNH)",
  URL = "https://www.amnh.org/research/hayden-planetarium/digital-universe",
  License = "AMNH Digital Universe"
}

:::
:::


