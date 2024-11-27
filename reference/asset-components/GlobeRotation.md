



(globebrowsing_rotation_globerotation)=
# GlobeRotation

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

*   - `Globe`
    - The globe on which the longitude/latitude is specified.
    - `String`
    
    - A valid scene graph node with a RenderableGlobe 
    
    - {bdg-info}`No`
    
*   - `Angle`
    - A rotation angle that can be used to rotate the object around its own y-axis, which will be pointing out of the globe's surface.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Latitude`
    - The latitude of the location on the globe's surface. The value can range from -90 to 90, with negative values representing the southern hemisphere of the globe. The default value is 0.0.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Longitude`
    - The longitude of the location on the globe's surface. The value can range from -180 to 180, with negative values representing the western hemisphere of the globe. The default value is 0.0.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `UseCamera`
    - If this value is 'true', the lat and lon are updated to match the camera.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseHeightmap`
    - If set to true, the heightmap will be used when computing the surface normal. This means that the object will be rotated to lay flat on the surface at the given coordinate and follow the shape of the landscape.
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


















## Asset Examples


:::{dropdown} Angle

This asset creates a rotation that places a coordinate axes on the surface of a
planetary body. The rotation causes the coordinate axes to remain fixed to the surface
of the globe. Additionally, the coordinate axes are rotated around the up-axis by a
fixed amount.
In order for this feature to work properly, the coordinate axes need to be located at
the same place as well, so this example also needs a `GlobeTranslation` applied.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 24, 35

-- The example needs a `RenderableGlobe` as a parent to function
local Globe = {
  Identifier = "GlobeRotation_Example_Angle_Globe",
  Renderable = {
    Type = "RenderableGlobe"
  },
  GUI = {
    Name = "GlobeRotation - Angle (Globe)",
    Path = "/Examples"
  }
}

local Node = {
  Identifier = "GlobeRotation_Example_Angle",
  Parent = "GlobeRotation_Example_Angle_Globe",
  Transform = {
    Translation = {
      Type = "GlobeTranslation",
      Globe = "GlobeRotation_Example_Angle_Globe",
      Latitude = 20.0,
      Longitude = -45.0
    },
    Rotation = {
      Type = "GlobeRotation",
      Globe = "GlobeRotation_Example_Angle_Globe",
      Latitude = 20.0,
      Longitude = -45.0,
      Angle = 45.0
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "GlobeRotation - Angle",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Globe)
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
  openspace.removeSceneGraphNode(Globe)
end)

:::
:::



:::{dropdown} UseCamera

This asset creates a rotation that places a coordinate axes on the surface of a
planetary body. The rotation causes the coordinate axes to remain fixed to the surface
of the globe. In this example, the rotation of the object will be updated based on the
location of the camera. When loading this example, make sure to focus the camera on
the Globe object for the follow-function to work.
In order for this feature to work properly, the coordinate axes need to be located at
the same place as well, so this example also needs a `GlobeTranslation` applied, which
in this case also updated based on the camera location.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 25, 37

-- The example needs a `RenderableGlobe` as a parent to function
local Globe = {
  Identifier = "GlobeRotation_Example_UseCamera_Globe",
  Renderable = {
    Type = "RenderableGlobe"
  },
  GUI = {
    Name = "GlobeRotation - UseCamera (Globe)",
    Path = "/Examples"
  }
}

local Node = {
  Identifier = "GlobeRotation_Example_UseCamera",
  Parent = "GlobeRotation_Example_UseCamera_Globe",
  Transform = {
    Translation = {
      Type = "GlobeTranslation",
      Globe = "GlobeRotation_Example_UseCamera_Globe",
      Latitude = 20.0,
      Longitude = -45.0,
      UseCamera = true
    },
    Rotation = {
      Type = "GlobeRotation",
      Globe = "GlobeRotation_Example_UseCamera_Globe",
      Latitude = 20.0,
      Longitude = -45.0,
      Angle = 45.0,
      UseCamera = true
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "GlobeRotation - UseCamera",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Globe)
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
  openspace.removeSceneGraphNode(Globe)
end)

:::
:::



:::{dropdown} Basic

This asset creates a rotation that places a coordinate axes on the surface of a
planetary body. The rotation causes the coordinate axes to remain fixed to the surface
of the globe.
In order for this feature to work properly, the coordinate axes need to be located at
the same place as well, so this example also needs a `GlobeTranslation` applied.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 24, 34

-- The example needs a `RenderableGlobe` as a parent to function
local Globe = {
  Identifier = "GlobeRotation_Example_Globe",
  Renderable = {
    Type = "RenderableGlobe"
  },
  GUI = {
    Name = "GlobeRotation - Basic (Globe)",
    Path = "/Examples"
  }
}

local Node = {
  Identifier = "GlobeRotation_Example",
  Parent = "GlobeRotation_Example_Globe",
  Transform = {
    Translation = {
      Type = "GlobeTranslation",
      Globe = "GlobeRotation_Example_Globe",
      Latitude = 20.0,
      Longitude = -45.0
    },
    Rotation = {
      Type = "GlobeRotation",
      Globe = "GlobeRotation_Example_Globe",
      Latitude = 20.0,
      Longitude = -45.0
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "GlobeRotation - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Globe)
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
  openspace.removeSceneGraphNode(Globe)
end)

:::
:::


