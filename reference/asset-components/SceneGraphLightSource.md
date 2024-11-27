



(base_scene_graph_light_source)=
# SceneGraphLightSource

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

*   - `Node`
    - The identifier of the scene graph node to follow.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
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
:emphasize-lines: 34
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")
local transforms = asset.require("./transforms")



local model = asset.resource({
  Name = "JUICE Model",
  Type = "HttpSynchronization",
  Identifier = "juice_models",
  Version = 1
})


local JuiceModel = {
  Identifier = "JuiceModel",
  Parent = transforms.Juice.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      -- Offset numbers found by eyeballing
      Position = { 4.5, 0.0, -1.0 }
    },
    Rotation = {
      Type = "StaticRotation",
      Rotation = { math.pi / 2.0, 0.0, 0.0 }
    }
  },
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "juice.fbx",
    ModelScale = "Centimeter",
    LightSources = {
      {
        Type = "SceneGraphLightSource",
        Identifier = "Sun",
        Node = sunTransforms.SolarSystemBarycenter.Identifier,
        Intensity = 0.6
      },
      {
        Identifier = "Camera",
        Type = "CameraLightSource",
        Intensity = 0.4,
        Enabled = false
      }
    }
  },
  GUI = {
    Name = "Juice Model",
    Path = "/Solar System/Missions/Juice",
    Description = "The model of the JUICE spacecraft"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(JuiceModel)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(JuiceModel)
end)

asset.export(JuiceModel)



asset.meta = {
  Name = "Juice Model",
  Description = [[
    The model of the JUICE spacecraft. The model file was taken from
    https://www.cosmos.esa.int/web/esac-cmso/scifleet.
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


