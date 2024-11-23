



(space_renderable_constellationlines)=
# RenderableConstellationLines

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
    - The path to a SPECK file that contains the data for the constellation lines.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Colors`
    - A list of colors to use for the constellations. A data file may include several groups of constellations, where each group can have a distinct color. The index for the color parameter for each constellation in the data file corresponds to the order of the colors in this list.
    - `Table`
    
    -   [Table parameters](#RenderableConstellationLinesColors-target) 
    
    - Yes
    
*   - `DrawElements`
    - Enables/Disables the drawing of the constellations.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
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
    
    -   [Table parameters](#RenderableConstellationLinesSelection-target) 
    
    - Yes
    
*   - `Unit`
    - The distance unit used for the constellation lines data.
    - `String`
    
    - In list { m, Km, pc, Kpc, Mpc, Gpc, Gly } 
    
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








(RenderableConstellationLinesColors-target)=
::::{dropdown} Table parameters for `Colors`
A list of colors to use for the constellations. A data file may include several groups of constellations, where each group can have a distinct color. The index for the color parameter for each constellation in the data file corresponds to the order of the colors in this list.


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
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
:::



::::












(RenderableConstellationLinesSelection-target)=
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
:emphasize-lines: 12
local speck = asset.resource({
  Name = "Big Dipper Constellation Files",
  Type = "HttpSynchronization",
  Identifier = "digitaluniverse_constellations_bigdipper",
  Version = 1
})


local BigDipper = {
  Identifier = "BigDipperConstellation",
  Renderable = {
    Type = "RenderableConstellationLines",
    Enabled = false,
    Labels = {
      File = speck .. "bigdipper.label",
      Opacity = 0.3,
      Color = { 0.8, 0.8, 0.8 },
      Size = 14.5,
      MinMaxSize = { 8, 170 },
      Unit = "pc"
    },
    Opacity = 0.3,
    File = speck .. "bigdipper.speck",
    NamesFile = speck .. "bigdipper.dat",
    Colors = { { 0.6, 0.4, 0.4 }, { 0.8, 0.0, 0.0 }, { 0.0, 0.3, 0.8 } },
    Unit = "pc",
    DimInAtmosphere = true
  },
  Tag = { "daytime_hidden" },
  GUI = {
    Name = "Big Dipper",
    Path = "/Milky Way/Constellations",
    Description = [[This item only draws the big dipper, and not the rest of the
      lines of the Ursa Major constellation.]]
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(BigDipper)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(BigDipper)
end)

asset.export(BigDipper)



asset.meta = {
  Name = "Big Dipper",
  Description = "Constellation lines for the Big Dipper",
  Author = "OpenSpace Team",
  URL = "https://www.openspaceproject.com",
  License = "MIT"
}

:::
:::


