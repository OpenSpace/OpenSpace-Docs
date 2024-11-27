



(base_transform_translation_keyframe)=
# TimelineTranslation

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

*   - `Keyframes`
    - A table of keyframes, with keys formatted as YYYY-MM-DDTHH:MM:SS and values that are valid Translation objects
    - `Table`
    
    -   [Table parameters](#TimelineTranslationKeyframes-target) 
    
    - {bdg-info}`No`
    
*   - `ShouldInterpolate`
    - If this value is set to 'true', an interpolation is applied between the given keyframes. If this value is set to 'false', the interpolation is not applied.
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






(TimelineTranslationKeyframes-target)=
::::{dropdown} Table parameters for `Keyframes`
A table of keyframes, with keys formatted as YYYY-MM-DDTHH:MM:SS and values that are valid Translation objects


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
    
    - [Translation](#core_transform_translation)
    
    - {bdg-info}`No`
    
:::



::::






## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 87
local trail = asset.require("./trail")
local marsTransforms = asset.require("scene/solarsystem/planets/mars/transforms")
local sun = asset.require("scene/solarsystem/sun/transforms")
local kernels = asset.require("./kernels")
local coreKernels = asset.require("spice/core")



local models = asset.resource({
  Name = "Perseverance Model",
  Type = "HttpSynchronization",
  Identifier = "perseverance_models",
  Version = 2
})


local TranslationKeyframes = {
  ["1850 JAN 01 00:00:00"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars,
    FixedDate = "2020 JUL 17 13:56:43"
  },
  ["2020 JUL 17 13:56:42"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars,
    FixedDate = "2020 JUL 17 13:56:43"
  },
  ["2020 JUL 17 13:56:43"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars
  },
  ["2020 JUL 17 13:56:44"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars
  },
  ["2021 FEB 18 20:43:48"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars
  },
  ["2021 FEB 18 20:43:49"] = {
    Type = "SpiceTranslation",
    Target = kernels.ID.Perseverance,
    Observer = kernels.ID.Mars,
    Frame = kernels.Frame.Mars,
    FixedDate = "2021 FEB 18 20:43:48"
  }
}

local PerseveranceNode = {
  Identifier = "PerseveranceNode",
  Parent = marsTransforms.MarsBarycenter.Identifier,
  Transform = {
    Translation = {
      Type = "SpiceTranslation",
      Target = kernels.ID.Mars,
      Observer = kernels.ID.MarsBarycenter
    },
    Rotation = {
      Type = "SpiceRotation",
      SourceFrame = kernels.Frame.Mars,
      DestinationFrame = coreKernels.Frame.Galactic
    }
  },
  GUI = {
    Name = "Perseverance Node",
    Path = "/Solar System/Missions/Perseverance",
    Hidden = true
  }
}

-- Perseverance Model --
local Perseverance = {
  Identifier = "Perseverance",
  Parent = PerseveranceNode.Identifier,
  Transform = {
    Translation = {
      Type = "TimelineTranslation",
      Keyframes = TranslationKeyframes
    }
  },
  GUI = {
    Name = "Perseverance",
    Path = "/Solar System/Missions/Perseverance"
  }
}

-- Perseverance Model --
local PerseveranceModel = {
  Identifier = "PerseveranceModel",
  Parent = Perseverance.Identifier,
  GUI = {
    Name = "Perseverance Model",
    Path = "/Solar System/Missions/Perseverance",
    Hidden = true
  }
}

-- Perseverance Model Instruments --
local Body = {
  Identifier = "Perseverance_body",
  Parent = PerseveranceModel.Identifier,
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = models .. "Perseverance.obj",
    LightSources = {
      sun.LightSource,
      {
        Identifier = "Camera",
        Type = "CameraLightSource",
        Intensity = 0.5
      }
    },
    RotationVector = { 19.19, 0.0, 348.08 }
  },
  GUI = {
    Name = "Perseverance Model Body",
    Path = "/Solar System/Missions/Perseverance/Model"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(PerseveranceNode)
  openspace.addSceneGraphNode(Perseverance)
  openspace.addSceneGraphNode(PerseveranceModel)
  openspace.addSceneGraphNode(Body)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Body)
  openspace.removeSceneGraphNode(PerseveranceModel)
  openspace.removeSceneGraphNode(Perseverance)
  openspace.removeSceneGraphNode(PerseveranceNode)
end)

asset.export(PerseveranceNode)
asset.export(Perseverance)
asset.export(PerseveranceModel)
asset.export(Body)

:::
:::


