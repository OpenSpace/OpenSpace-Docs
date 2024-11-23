



(video_videotileprovider)=
# VideoTileProvider

_Inherits [TileProvider](#TileProvider)_




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



















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 12
-- To learn how you can include your own video, see the wiki
-- http://wiki.openspaceproject.com/docs/builders/assets/resources.html

local earth = asset.require("scene/solarsystem/planets/earth/earth")



local Layer = {
  Name = "Globe Video Loop Example",
  Identifier = "GlobeVideoLoopExample",
  Enabled = true,
  Type = "VideoTileProvider",
  Video = asset.resource("examplevideo.mp4"),
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(earth.Earth.Identifier, "ColorLayers", Layer)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(earth.Earth.Identifier, "ColorLayers", Layer)
end)

asset.export("layer", Layer)



asset.meta = {
  Name = "Video Player on Globe Example",
  Description = "An example asset that shows how to include a video on Earth.",
  Author = "OpenSpace Team",
  URL = "https://openspaceproject.com",
  License = "MIT"
}

:::
:::


