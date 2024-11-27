



(volume_renderable_timevaryingvolume)=
# RenderableTimeVaryingVolume

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

*   - `SecondsAfter`
    - The number of seconds to show the the last timestep after its actual time.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `SourceDirectory`
    - A directory from where to load the data files for the different time steps.
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
*   - `TransferFunction`
    - The path to the transfer function file.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Brightness`
    - A value that affects the general brightness of the volume rendering.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ClipPlanes`
    - @TODO Missing documentation
    - `Table`
    
    -  
    
    - Yes
    
*   - `GridType`
    - The grid type to use for the volume.
    - `String`
    
    - In list { Spherical, Cartesian } 
    
    - Yes
    
*   - `InvertDataAtZ`
    - If true, the volume data will be inverted at its z-axis.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `SecondsBefore`
    - The number of seconds to show the first timestep before its actual time.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `StepSize`
    - Specifies how often to sample during raycasting. Lower step size leads to higher resolution.
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
























## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 21
-- Before using this example,
-- the volume data itself needs to be generated,
-- using the task 'data/tasks/volume/generate_cartesian.task'

local transforms = asset.require("scene/solarsystem/sun/transforms")



local SunRadius = 695508000

local Volume = {
  Identifier = "GeneratedVolumeCartesian",
  Parent = transforms.SolarSystemBarycenter.Identifier,
  Transform = {
    Scale = {
        Type = "StaticScale",
        Scale = 1000 * SunRadius
    }
  },
  Renderable = {
    Type = "RenderableTimeVaryingVolume",
    SourceDirectory = asset.resource("cartesian"),
    TransferFunction = asset.resource("../transferfunction.txt"),
    StepSize = 0.01,
    MinValue = 0,
    MaxValue = 1,
    GridType = "Cartesian",
    SecondsBefore = 50 * openspace.time.secondsPerYear(), -- 50 years before
    SecondsAfter = 50 * openspace.time.secondsPerYear() -- 50 years after
  },
  GUI = {
    Path = "/Examples"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Volume)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Volume)
end)

asset.export(Volume)

:::
:::


