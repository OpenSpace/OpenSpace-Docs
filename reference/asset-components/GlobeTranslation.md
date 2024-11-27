



(space_translation_globetranslation)=
# GlobeTranslation

_Inherits [Translation](#core_transform_translation)_




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
    
*   - `Altitude`
    - The altitude in meters. If the 'UseHeightmap' property is 'true', this is an offset from the actual surface of the globe. If not, this is an offset from the reference ellipsoid. The default value is 0.0.
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
    
*   - `UseCameraAltitude`
    - If this value is 'true', the altitude is updated to match the camera.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseHeightmap`
    - If this value is 'true', the altitude specified in 'Altitude' will be treated as an offset from the heightmap. Otherwise, it will be an offset from the globe's reference ellipsoid. The default value is 'false'.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



### Inherited members from [Translation](#core_transform_translation)

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
    - The type of translation that is described in this element. The available types of translations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Translation type 
    
    - {bdg-info}`No`
    
:::




















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 26
-- Basic
-- This asset creates a rotation that places a coordinate axes on the surface of a
-- planetary body. The rotation causes the coordinate axes to remain fixed to the surface
-- of the globe.
--
-- In order for this feature to work properly, the coordinate axes need to be located at
-- the same place as well, so this example also needs a `GlobeTranslation` applied.

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


