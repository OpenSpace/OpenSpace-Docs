



(video_renderablevideoplane)=
# RenderableVideoPlane

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
    
*   - `Video`
    - The video file that is played.
    - `File`
    
    - Value of type 'File' 
    
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
    
*   - `EndTime`
    - The date and time that the video should end in the format 'YYYY MM DD hh:mm:ss'.
    - `Date and time`
    
    - Value of type 'Date and time' 
    
    - Yes
    
*   - `LoopVideo`
    - If checked, the video is continues playing from the start when it reaches the end of the video.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
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
    
*   - `PlayAudio`
    - Play audio.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `PlaybackMode`
    - The mode of how the video should be played back. Default is video is played back according to the set start and end times.
    - `String`
    
    - In list { MapToSimulationTime, RealTimeLoop } 
    
    - Yes
    
*   - `StartTime`
    - The date and time that the video should start in the format 'YYYY MM DD hh:mm:ss'.
    - `Date and time`
    
    - Value of type 'Date and time' 
    
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
:emphasize-lines: 18
-- To learn how you can include your own video, see the wiki
-- http://wiki.openspaceproject.com/docs/builders/assets/resources.html

local transforms = asset.require("scene/solarsystem/planets/earth/transforms")



local Plane = {
  Identifier = "VideoPlaneExample",
  Parent = transforms.EarthCenter.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = { 0.0, -11E7, 0.0 }
    }
  },
  Renderable = {
    Type = "RenderableVideoPlane",
    MirrorBackside = true,
    Size = 3E7,
    Video = asset.resource("examplevideo.mp4"),
  },
  GUI = {
    Name = "Video Plane Example",
    Path = "/Other/Planes"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Plane)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Plane)
end)

asset.export(Plane)



asset.meta = {
  Name = "Video Plane Example",
  Description = "An example asset that shows how to include a video on a plane.",
  Author = "OpenSpace Team",
  URL = "https://openspaceproject.com",
  License = "MIT"
}

:::
:::


