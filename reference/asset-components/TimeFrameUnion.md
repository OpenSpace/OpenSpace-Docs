



(base_timeframe_union)=
# TimeFrameUnion

_Inherits [TimeFrame](#core_time_frame)_

This TimeFrame class will accept the union of all passed-in TimeFrames. This means that this TimeFrame will be active if at least one of the child TimeFrames is active and it will be inactive if none of the child TimeFrames are active.

This can be used to create more complex TimeFrames that are made up of several, simpler TimeFrames themselves.


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

*   - `TimeFrames`
    - A vector of time frames to combine into one. The time frame is active when any of the contained time frames are, but not in gaps between contained time frames.
    - `Table`
    
    -   [Table parameters](#TimeFrameUnionTimeFrames-target) 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [TimeFrame](#core_time_frame)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - The type of the time frame that is described in this element. The available types of scaling depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid TimeFrame type 
    
    - {bdg-info}`No`
    
:::






(TimeFrameUnionTimeFrames-target)=
::::{dropdown} Table parameters for `TimeFrames`
A vector of time frames to combine into one. The time frame is active when any of the contained time frames are, but not in gaps between contained time frames.


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
    - `Table`
    
    - [TimeFrame](#core_time_frame)
    
    - Yes
    
:::



::::




## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 10
-- Basic
-- This example creates a union out of two simpler TimeFrameIntervals and uses it for a
-- SceneGraphNode. The first TimeFrameInterval covers January 1st, 2000 and the second
-- TimeFrameInterval covers March 1st, 2002. The resulting TimeFrameUnion will cover both
-- January 1st, 2000 and March 1st, 2002.

local Node = {
  Identifier = "TimeFrameUnion_Example",
  TimeFrame = {
    Type = "TimeFrameUnion",
    TimeFrames = {
      -- The first TimeFrameInterval for the first day
      {
        Type = "TimeFrameInterval",
        Start = "2000 JAN 01 00:00:00.000",
        End = "2000 JAN 01 23:59:59.999"
      },
      -- The second TimeFrameInterval for the second day
      {
        Type = "TimeFrameInterval",
        Start = "2002 MAR 01 00:00:00.000",
        End = "2002 MAR 01 23:59:59.999"
      }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "TimeFrameUnion - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::


