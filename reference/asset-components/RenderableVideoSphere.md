



(video_renderablevideosphere)=
# RenderableVideoSphere

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

*   - `Video`
    - The video file that is played.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `DisableFadeInOut`
    - Enables/Disables the fade in and out effects.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EndTime`
    - The date and time that the video should end in the format 'YYYY MM DD hh:mm:ss'.
    - `Date and time`
    
    - Value of type 'Date and time' 
    
    - Yes
    
*   - `FadeInThreshold`
    - The distance from the center of the Milky Way at which the sphere should start to fade in, given as a percentage of the size of the object. A value of zero means that no fading in will happen.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `FadeOutThreshold`
    - A threshold for when the sphere should start fading out, given as a percentage of how much of the sphere that is visible before the fading should start. A value of zero means that no fading out will happen.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `LoopVideo`
    - If checked, the video is continues playing from the start when it reaches the end of the video.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MirrorTexture`
    - If true, mirror the texture along the x-axis.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Orientation`
    - Specifies whether the texture is applied to the inside of the sphere, the outside of the sphere, or both.
    - `String`
    
    - In list { Outside, Inside, Both } 
    
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
    
*   - `Segments`
    - The number of segments that the sphere is split into.
    - `Integer`
    
    - Greater or equal to: 4 
    
    - Yes
    
*   - `Size`
    - The radius of the sphere in meters.
    - `Double`
    
    - Greater than: 0 
    
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
:emphasize-lines: 7
-- To learn how you can include your own video, see the wiki
-- http://wiki.openspaceproject.com/docs/builders/assets/resources.html

local Sphere = {
  Identifier = "ExampleVideoOnSphere",
  Renderable = {
    Type = "RenderableVideoSphere",
    Size = 100.0,
    Segments = 80,
    Video = asset.resource("examplevideo.mp4"),
    Orientation = "Both"
  },
  GUI = {
    Name = "Video Sphere Example",
    Path = "/Other/Spheres"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Sphere)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Sphere)
end)

asset.export(Sphere)



asset.meta = {
  Name = "Video Player on Sphere Example",
  Description = "An example asset that shows how to include a video on a sphere.",
  Author = "OpenSpace Team",
  URL = "https://openspaceproject.com",
  License = "MIT"
}

:::
:::


