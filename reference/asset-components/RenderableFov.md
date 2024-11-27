



(spacecraftinstruments_renderablefieldofview)=
# RenderableFov

_Inherits [Renderable](#renderable)_

Needs support for std::map first for the frameConversions


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

*   - `Body`
    - The SPICE name of the source body for which the field of view should be rendered.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Frame`
    - The SPICE name of the source body's frame in which the field of view should be rendered.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Instrument`
    - A table describing the instrument whose field of view should be rendered.
    - `Table`
    
    -   [Table parameters](#RenderableFovInstrument-target) 
    
    - {bdg-info}`No`
    
*   - `PotentialTargets`
    - A list of potential targets (specified as SPICE names) that the field of view should be tested against.
    - `Table`
    
    -   [Table parameters](#RenderableFovPotentialTargets-target) 
    
    - {bdg-info}`No`
    
*   - `AlwaysDrawFov`
    - If enabled, the field of view will always be drawn, regardless of whether image information is currently available or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FrameConversions`
    - A list of frame conversions that should be registered with the SpiceManager.
    - `Table`
    
    -   [Table parameters](#RenderableFovFrameConversions-target) 
    
    - Yes
    
*   - `LineWidth`
    - The width of the lines that connect the instrument to the corners of the field of view.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `SimplifyBounds`
    - If true, the field of view's bounds values will be simplified on load. Bound vectors will be removed if they are the strict linear interpolation between the two neighboring vectors. This value is disabled by default.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `StandOffDistance`
    - A standoff distance factor which influences the distance of the plane to the focus object. If the value is 1, the field of view will be rendered exactly on the surface of, for example, a planet. With a value of smaller than 1, the field of view will hover of the surface, thus making it more visible.
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










(RenderableFovInstrument-target)=
::::{dropdown} Table parameters for `Instrument`
A table describing the instrument whose field of view should be rendered.


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

*   - `Aberration`
    - The aberration correction that is used for this field of view. The default is 'NONE'.
    - `String`
    
    - In list { NONE, LT, LT+S, CN, CN+S, XLT, XLT+S, XCN, XCN+S } 
    
    - Yes
    
*   - `Name`
    - The SPICE name of the instrument that is rendered.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



::::




(RenderableFovPotentialTargets-target)=
::::{dropdown} Table parameters for `PotentialTargets`
A list of potential targets (specified as SPICE names) that the field of view should be tested against.


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






(RenderableFovFrameConversions-target)=
::::{dropdown} Table parameters for `FrameConversions`
A list of frame conversions that should be registered with the SpiceManager.


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
    
    - {bdg-info}`No`
    
:::



::::










## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 10
local transforms = asset.require("../model")
local kernels = asset.require("../kernels")



local HGA = {
  Identifier = "BepiColomboMPO_HGA",
  Parent = transforms.BepiColombo.Identifier,
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.MPO,
    Frame = kernels.Frame.HGA,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = "MPO_HGA",
      Method = "CIRCLE",
      Aberration = "NONE"
    },
    AlwaysDrawFov = true,
    PotentialTargets = { "MERCURY", "EARTH", "VENUS" }
  },
  GUI = {
    Name = "MPO HGA",
    Path = "/Solar System/Missions/BepiColombo/Instruments",
  }
}


asset.onInitialize(function()
  -- Circle shapes are currently not supported
  -- openspace.addSceneGraphNode(HGA)
end)

asset.onDeinitialize(function()
  -- openspace.removeSceneGraphNode(HGA)
end)



asset.meta = {
  Name = "HGA",
  Description = "Shows the field-view for the High Gain Antenna of the MPO spacecraft.",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


