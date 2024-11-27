



(base_transform_rotation_keyframe)=
# TimelineRotation

_Inherits [Rotation](#core_transform_rotation)_




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

*   - `Keyframes`
    - A table of keyframes, with keys formatted as YYYY-MM-DDTHH:MM:SS and values that are valid Rotation objects
    - `Table`
    
    -   [Table parameters](#TimelineRotationKeyframes-target) 
    
    - {bdg-info}`No`
    
*   - `ShouldInterpolate`
    - If this value is set to 'true', an interpolation is applied between the given keyframes. If this value is set to 'false', the interpolation is not applied.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



### Inherited members from [Rotation](#core_transform_rotation)

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
    - The type of the rotation that is described in this element. The available types of rotations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Rotation type 
    
    - {bdg-info}`No`
    
:::






(TimelineRotationKeyframes-target)=
::::{dropdown} Table parameters for `Keyframes`
A table of keyframes, with keys formatted as YYYY-MM-DDTHH:MM:SS and values that are valid Rotation objects


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
    
    - [Rotation](#core_transform_rotation)
    
    - {bdg-info}`No`
    
:::



::::






## Asset Examples


:::{dropdown} No Interpolation

This asset creates a SceneGraphNode that only displays coordinate axes. The rotation of
the coordinate axes are determined by a timeline of individual rotations that are used
without interpolating between the timeline entries. These rotations are keyframes that
are used to change between different orientations. This example transitions between
three rotations. In this example, the interpolation between entries is disabled, which
will cause the coordinate axes to change their orientation abruptly when the rotation
changes. If the interpolation were enabled, the orientation of the coordinate axes
would transition seamlessly instead at the provided times. This example will only work
if the in-game time is set to January 1st, 2000.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 30

local Node = {
  Identifier = "TimelineRotation_Example_NoInterpolation",
  Transform = {
    Rotation = {
      Type = "TimelineRotation",
      Keyframes = {
        -- The first timeline entry
        ["2000 JAN 01 00:00:00"] = {
          Type = "StaticRotation",
          Rotation = { math.pi, 0.0, 0.0 }
        },
        -- The second timeline entry
        ["2000 JAN 01 12:00:00"] = {
          Type = "StaticRotation",
          Rotation = { 0.0, 0.0, 0.0 }
        },
        -- The third timeline entry
        ["2000 JAN 01 23:59:59"] = {
          Type = "StaticRotation",
          Rotation = { 0.0, 0.0, math.pi }
        }
      },
      ShouldInterpolate = false
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "TimelineRotation - No Interpolation",
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



:::{dropdown} Basic

This asset creates a SceneGraphNode that only displays coordinate axes. The rotation of
the coordinate axes are determined by a timeline of individual rotations. These rotations
are keyframes that are used to seamlessly change between different orientations. This
example transitions between three rotations over a long time span. This example will
only work if the in-game time is set to January 1st, 2000.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 29

local Node = {
  Identifier = "TimelineRotation_Example",
  Transform = {
    Rotation = {
      Type = "TimelineRotation",
      Keyframes = {
        -- The first timeline entry
        ["2000 JAN 01 00:00:00"] = {
          Type = "StaticRotation",
          Rotation = { math.pi, 0.0, 0.0 }
        },
        -- The second timeline entry
        ["2000 JAN 01 12:00:00"] = {
          Type = "StaticRotation",
          Rotation = { 0.0, 0.0, 0.0 }
        },
        -- The third timeline entry
        ["2000 JAN 01 23:59:59"] = {
          Type = "StaticRotation",
          Rotation = { 0.0, 0.0, math.pi }
        }
      }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "TimelineRotation - Basic",
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


