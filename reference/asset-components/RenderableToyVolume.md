



(renderabletoyvolume-identifier )=
# RenderableToyVolume

_Inherits [Renderable](#renderable)_




## Members




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
:emphasize-lines: 9
local transforms = asset.require("scene/solarsystem/sun/transforms")



local ToyVolume = {
  Identifier = "RenderableToyVolume",
  Parent = transforms.SolarSystemBarycenter.Identifier,
  Renderable = {
    Type = "RenderableToyVolume",
    Size = { 5, 5, 5 },
    ScalingExponent = 11,
    StepSize = 0.01,
    Color = { 1.0, 0.0, 0.0 }
  },
  GUI = {
    Path = "/Examples"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(ToyVolume)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(ToyVolume)
end)

asset.export(ToyVolume)

:::
:::


