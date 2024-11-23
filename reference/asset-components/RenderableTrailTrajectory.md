



(base_renderable_renderabletrailtrajectory)=
# RenderableTrailTrajectory

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

*   - `Color`
    - This value determines the RGB main color for the lines and points of the trail.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - {bdg-info}`No`
    
*   - `EndTime`
    - The end time for the range of this trajectory. The date must be in ISO 8601 format: YYYY MM DD HH:mm:ss.xxx.
    - `String`
    
    - A valid date in ISO 8601 format 
    
    - {bdg-info}`No`
    
*   - `SampleInterval`
    - The interval between samples of the trajectory. This value (together with 'TimeStampSubsampleFactor') determines how far apart (in time) the samples are spaced along the trajectory. The time interval between 'StartTime' and 'EndTime' is split into 'SampleInterval' * 'TimeStampSubsampleFactor' segments.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `StartTime`
    - The start time for the range of this trajectory. The date must be in ISO 8601 format: YYYY MM DD HH:mm:ss.xxx.
    - `String`
    
    - A valid date in ISO 8601 format 
    
    - {bdg-info}`No`
    
*   - `Translation`
    - A translation used to compute locations along the path.
    - `Table`
    
    - [Translation](#core_transform_translation)
    
    - {bdg-info}`No`
    
*   - `AccurateTrailPositions`
    - The number of vertices, each side of the object, that will be recalculated for greater accuracy. This also ensures that the object connects with the trail.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `EnableFade`
    - Toggles whether the trail should fade older points out. If this value is true, the 'Fade' parameter determines the speed of fading. If this value is false, the entire trail is rendered at full opacity and color.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EnableSweepChunking`
    - The number of vertices that will be calculated each frame whenever the trail needs to be recalculated. A greater value will result in more calculations per frame.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LineFadeAmount`
    - The amount of the trail that should be faded. If the value is 0 then the trail will have no fading applied. A value of 0.6 will result in a trail where 60% of the extent of the trail will have fading applied to it. In otherwords, the 40% closest to the head of the trail will be solid and the rest will fade until completely transparent at the end of the trail. A value of 1 will result in a trail that starts fading immediately, becoming fully transparent by the end of the trail. This setting only applies if the 'EnableFade' value is true. If it is false, this setting has no effect.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineLength`
    - The extent of the rendered trail. A value of 0 will result in no trail and a value of 1 will result in a trail that covers the entire extent. The setting only applies if 'EnableFade' is true. If it is false, this setting has no effect.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineWidth`
    - Specifies the line width of the trail lines, if the selected rendering method includes lines. If the rendering mode is Points, this value is ignored.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PointSize`
    - Specifies the base size of the points along the line, if the selected rendering method includes points. If the rendering mode is Lines, this value is ignored. If a subsampling of the values is performed, the subsampled values are half this size.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `Rendering`
    - Determines how the trail should be rendered. If 'Lines' is selected, only the line part is visible, if 'Points' is selected, only the corresponding points (and subpoints) are shown. 'Lines+Points' shows both parts.
    - `String`
    
    - In list { Lines, Points, Lines+Points, Lines+Points } 
    
    - Yes
    
*   - `ShowFullTrail`
    - If true, the entire trail will be rendered. If false, only the trail until the current time in the application will be shown.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `SweepChunkSize`
    - The number of vertices that will be calculated each frame whenever the trail needs to be recalculated. A greater value will result in more calculations per frame.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `TimeStampSubsampleFactor`
    - The factor that is used to create subsamples along the trajectory. This value (together with 'SampleInterval') determines how far apart (in time) the samples are spaced along the trajectory. The time interval between 'StartTime' and 'EndTime' is split into 'SampleInterval' * 'TimeStampSubsampleFactor' segments.
    - `Integer`
    
    - Value of type 'Integer' 
    
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
:emphasize-lines: 10
local transforms = asset.require("./transforms")
local kernels = asset.require("./kernels")



local TrailAtPluto = {
  Identifier = "NewHorizonsTrailPluto",
  Parent = transforms.PlutoBarycenterAccurate.Identifier,
  Renderable = {
    Type = "RenderableTrailTrajectory",
    Translation = {
      Type = "SpiceTranslation",
      Target = kernels.ID.NewHorizons,
      Observer = kernels.ID.PlutoBarycenter
    },
    Color = { 1.0, 0.8, 0.4 },
    ShowFullTrail = true,
    StartTime = "2015 JUL 07 12:00:00",
    EndTime = "2015 JUL 17 12:00:00",
    PointSize = 5,
    SampleInterval = 100,
    TimeStampSubsampleFactor = 4,
    EnableFade = false,
    Rendering = "Lines+Points"
  },
  GUI = {
    Name = "New Horizons Trail Pluto",
    Path = "/Solar System/Missions/New Horizons"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(TrailAtPluto)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(TrailAtPluto)
end)

asset.export(TrailAtPluto)

:::
:::


