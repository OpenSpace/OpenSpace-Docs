



(spacecraftinstruments_renderableplaneprojection)=
# RenderablePlaneProjection

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

*   - `Instrument`
    - The SPICE name of the instrument that is used to project the image onto this `RenderablePlaneProjection`.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Spacecraft`
    - The SPICE name of the spacecraft from which the projection is performed.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `DefaultTarget`
    - The SPICE name of the default target that is imaged by this instrument (used when no target is identified by the `ImageSequencer`).
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Texture`
    - The image that is used on this plane before any image is loaded from the `ImageSequencer`.
    - `String`
    
    - Value of type 'String' 
    
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
:emphasize-lines: 20
local transforms = asset.require("./transforms")
local kernels = asset.require("./kernels")



local textures = asset.resource({
  Name = "Bennu Textures",
  Type = "HttpSynchronization",
  Identifier = "bennu_textures",
  Version = 1
})


local BennuBodyId = "2101955"

local ImagePlane = {
  Identifier = "ImagePlaneBennu",
  Parent = transforms.BennuBarycenter.Identifier,
  Renderable = {
    Type = "RenderablePlaneProjection",
    Frame = kernels.Frame.Bennu,
    DefaultTarget = BennuBodyId,
    Spacecraft = kernels.ID.OsirisRex,
    Instrument = kernels.Frame.Polycam,
    Moving = false,
    Texture = textures .. "defaultProj.png"
  },
  GUI = {
    Name = "OsirisREx Image Plane",
    Path = "/Solar System/Missions/OSIRIS REx"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(ImagePlane)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(ImagePlane)
end)

asset.export(ImagePlane)

:::
:::


