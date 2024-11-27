



(space_renderableorbitalkepler)=
# RenderableOrbitalKepler

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
    - The RGB main color for the trails and points.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - {bdg-info}`No`
    
*   - `Format`
    - A NORAD-style Two-Line element. Orbit Mean-Elements Message in the KVN notation. JPL's Small Bodies Database. The file format that is contained in the file.
    - `String`
    
    - In list { TLE, OMM, SBDB } 
    
    - {bdg-info}`No`
    
*   - `Path`
    - The file path to the data file to read.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `SegmentQuality`
    - A segment quality value for the orbital trail. A value from 1 (lowest) to 10 (highest) that controls the number of line segments in the rendering of the orbital trail. This does not control the direct number of segments because these automatically increase according to the eccentricity of the orbit.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `ContiguousMode`
    - If enabled, the contiguous set of objects starting from StartRenderIdx of size RenderSize will be rendered. If disabled, the number of objects defined by UpperLimit will rendered from an evenly dispersed sample of the full length of the data file.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EnableMaxSize`
    - If true, the Max Size property will be used as an upper limit for the size of the point. This reduces the size of the points when approaching them, so that they stick to a maximum visual size depending on the Max Size value.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EnableOutline`
    - Determines if the points should be rendered with an outline or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MaxSize`
    - Controls the maximum allowed size for the points, when the max size control feature is enabled. This limits the visual size of the points based on the distance to the camera. The larger the value, the larger the points are allowed to be. In the background, the computations are made to limit the size of the angle between the CameraToPointMid and CameraToPointEdge vectors.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `OutlineColor`
    - The color of the outline.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `OutlineWidth`
    - Determines the thickness of the outline. A value of 0 will not show any outline, while a value of 1 will cover the whole point.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PointSizeExponent`
    - An exponential scale value to set the absolute size of the point.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Rendering`
    - Determines how the trail should be rendered. If 'Trail' is selected, only the line part is visible, if 'Point' is selected, only the current satellite/debris point is visible.
    - `String`
    
    - In list { Trail, Point, PointsTrails } 
    
    - Yes
    
*   - `RenderSize`
    - Number of objects to render sequentially from StartRenderIdx.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `StartRenderIdx`
    - Index of the first object in the block to render (all prior objects will be ignored). The block of objects to render will be determined by StartRenderIdx and RenderSize.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `TrailFade`
    - Determines how fast the trail fades out. A smaller number shows less of the trail and a larger number shows more.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `TrailWidth`
    - The line width used for the trail, if the selected rendering method includes lines. If the rendering mode is set to Points, this value is ignored.
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
:emphasize-lines: 19
local transforms = asset.require("scene/solarsystem/planets/earth/transforms")



local omm = asset.resource({
  Name = "Satellite OMM Data (ARGOS)",
  Type = "UrlSynchronization",
  Identifier = "satellite_omm_data_argos",
  Url = "https://www.celestrak.com/NORAD/elements/gp.php?GROUP=argos&FORMAT=kvn",
  Filename = "argos.txt",
  SecondsUntilResync = openspace.time.secondsPerDay()
})


local Argos = {
  Identifier = "Argos",
  Parent = transforms.EarthInertial.Identifier,
  Renderable = {
    Type = "RenderableOrbitalKepler",
    Path = omm .. "argos.txt",
    Format = "OMM",
    SegmentQuality = 3,
    Color = { 0.75, 0.75, 0.35 },
    TrailFade = 17,
    PointSizeExponent = 5.0,
    RenderBinMode = "PostDeferredTransparent"
  },
  Tag = { "earth_satellites" },
  GUI = {
    Name = "ARGOS",
    Path = "/Solar System/Planets/Earth/Satellites"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Argos)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Argos)
end)

asset.export(Argos)



asset.meta = {
  Name = "Satellites Weather - ARGOS",
  Description = "Satellites asset for Weather - ARGOS. Data from Celestrak",
  Author = "OpenSpace Team",
  URL = "https://celestrak.com/NORAD/elements/",
  License = "Celestrak"
}

:::
:::


