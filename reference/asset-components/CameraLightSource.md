



(base_camera_light_source)=
# CameraLightSource

_Inherits [LightSource](#core_light_source)_




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

*   - `Intensity`
    - The intensity of this light source.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



### Inherited members from [LightSource](#core_light_source)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Identifier`
    - The identifier of the light source
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Type`
    - The type of the light source that is described in this element. The available types of light sources depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid LightSource type 
    
    - {bdg-info}`No`
    
*   - `Enabled`
    - Whether the light source is enabled or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::








## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 20
local sun = asset.require("scene/solarsystem/sun/transforms")



local modelFolder = asset.resource({
  Name = "Pioneer 10/11 Models",
  Type = "HttpSynchronization",
  Identifier = "pioneer_10_11_model",
  Version = 3
})


local ModelRenderable = {
  Type = "RenderableModel",
  GeometryFile = modelFolder .. "pioneer.fbx",
  LightSources = {
    sun.LightSource,
    {
      Identifier = "Camera",
      Type = "CameraLightSource",
      Intensity = 0.5
    }
  }
}

asset.export("PioneerModel", ModelRenderable)



asset.meta = {
  Name = "Pioneer Model",
  Description = [[Pioneer model asset. Used by both pioneer 10 and pioneer 11 asset.
    Untextured version of model from NASA 3D resources]],
  Author = "NASA",
  URL = "https://nasa3d.arc.nasa.gov/detail/eoss-pioneer",
  License = "NASA"
}

:::
:::


