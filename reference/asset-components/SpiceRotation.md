



(space_transform_rotation_spice)=
# SpiceRotation

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

*   - `SourceFrame`
    - This value specifies the source frame that is used as the basis for the coordinate transformation. This has to be a valid SPICE name.
    - `String`
    
    - A valid SPICE NAIF name or integer 
    
    - {bdg-info}`No`
    
*   - `DestinationFrame`
    - This value specifies the destination frame that is used for the coordinate transformation. This has to be a valid SPICE name. If this value is not specified, a reference frame of 'GALACTIC' is used instead
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `FixedDate`
    - A time to lock the rotation to. Setting this to an empty string will unlock the time and return to rotation based on current simulation time.
    - `String`
    
    - A time to lock the rotation to 
    
    - Yes
    
*   - `TimeFrame`
    - The time frame in which the spice kernels are valid.
    - `Table`
    
    - [TimeFrame](#core_time_frame)
    
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














## Asset Examples


:::{dropdown} Fixed Date

This asset creates a rotation provided by a SPICE kernel and applies it to a
SceneGraphNode that only displays coordinate axes. The rotation of the coordinate axes
are determined by SPICE, in this case pretending that the coordinate axes are rotating
at the same rate as Earth. In this specific example, the orientation is independent of
the actual in-game time in OpenSpace and only uses a fixed date of 2000 JAN 01 instead.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 18

-- Load the default SPICE kernels, which is the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceRotation_Example_FixedDate",
  Transform = {
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = "IAU_EARTH",
      DestinationFrame = "GALACTIC",
      FixedDate = "2000 JAN 01 00:00:00.000"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceRotation - Fixed Date",
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

This asset creates a rotation provided by a SPICE kernel and applies it to a
SceneGraphNode that only displays coordinate axes. The rotation of the coordinate axes
are determined by SPICE, in this case pretending that the coordinate axes are rotating
at the same rate as Earth.
For more information about SPICE see: https://naif.jpl.nasa.gov/naif/

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 17

-- Load the default SPICE kernels, which are the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceRotation_Example",
  Transform = {
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = "IAU_EARTH",
      DestinationFrame = "GALACTIC"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceRotation - Basic",
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



:::{dropdown} TimeFrame

This asset creates a rotation provided by a SPICE kernel and applies it to a
SceneGraphNode that only displays coordinate axes. The rotation of the coordinate axes
are determined by SPICE, in this case pretending that the coordinate axes are rotating
at the same rate as Earth. In this example, the rotation is only calculated between
2000 JAN 01 and 2002 JAN 01 to exemplify a use-case in which the data from the SPICE
kernel is not available for the whole duration.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 22

-- Load the default SPICE kernels, which is the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceRotation_Example_TimeFrame",
  Transform = {
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = "IAU_EARTH",
      DestinationFrame = "GALACTIC",
      TimeFrame = {
        Type = "TimeFrameInterval",
        Start = "2000 JAN 01",
        End = "2002 JAN 01"
      }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceRotation - TimeFrame",
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


