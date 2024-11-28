



(base_renderable_model)=
# RenderableModel

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

*   - `GeometryFile`
    - The file or files that should be loaded in this RenderableModel. The file can contain filesystem tokens. This specifies the model that is rendered by the Renderable.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `AmbientIntensity`
    - A multiplier for ambient lighting.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `AnimationMode`
    - The mode of how the animation should be played back. Default is that the animation is played back once at the start time.
    - `String`
    
    - In list { Once, LoopFromStart, LoopInfinitely, BounceFromStart, BounceInfinitely } 
    
    - Yes
    
*   - `AnimationStartTime`
    - The date and time that the model animation should start. In format `'YYYY MM DD hh:mm:ss'`.
    - `Date and time`
    
    - Value of type 'Date and time' 
    
    - Yes
    
*   - `AnimationTimeScale`
    - The time scale for the animation relative to seconds. For example, if the animation is in milliseconds then `AnimationTimeScale = 0.001` or `AnimationTimeScale = "Millisecond"`.
    - `String, or Double`
    
    - In list { Nanosecond, Microsecond, Millisecond, Second, Minute }, or Value of type 'Double' 
    
    - Yes
    
*   - `BlendingOption`
    - Controls the blending function used to calculate the colors of the model with respect to the opacity.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `DiffuseIntensity`
    - A multiplier for diffuse lighting.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `EnableAnimation`
    - Enable or disable the animation for the model if it has any.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EnableDepthTest`
    - If true, depth testing is enabled for the model. This means that parts of the model that are occluded by other parts will not be rendered. If disabled, the depth of the model part will not be taken into account in rendering and some parts that should be hidden behind a model might be rendered in front.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `EnableFaceCulling`
    - Enable OpenGL automatic face culling optimization.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ForceRenderInvisible`
    - Set if invisible parts (parts with no textures or materials) of the model should be forced to render or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FragmentShader`
    - The path to a fragment shader program to use instead of the default shader.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `InvertModelScale`
    - By default the given `ModelScale` is used to scale down the model. By setting this setting to true the scaling is inverted to that the model is instead scaled up with the given `ModelScale`.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LightSources`
    - A list of light sources that this model should accept light from.
    - `Table`
    
    -   [Table parameters](#RenderableModelLightSources-target) 
    
    - Yes
    
*   - `ModelScale`
    - The scale of the model. For example, if the model is in centimeters then `ModelScale = 'Centimeter'` or `ModelScale = 0.01`. The value that this needs to be in order for the model to be in the correct scale relative to the rest of OpenSpace can be tricky to find. Essentially, it depends on the model software that the model was created with and the original intention of the modeler.
    - `String, or Double`
    
    - In list { Nanometer, Micrometer, Millimeter, Centimeter, Decimeter, Meter, Kilometer, Thou, Inch, Foot, Yard, Chain, Furlong, Mile }, or Value of type 'Double' 
    
    - Yes
    
*   - `ModelTransform`
    - An extra model transform matrix that is applied to the model before all other transformations are applied.
    - `Matrix4x4<double>`
    
    - Value of type 'Matrix4x4<double>' 
    
    - Yes
    
*   - `PerformShading`
    - Determines whether shading should be applied to this model, based on the provided list of light sources. If false, the model will be fully illuminated.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Pivot`
    - A vector that moves the place of origin for the model.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `RotationVector`
    - A rotation vector with Euler angles, specified in degrees.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `SpecularIntensity`
    - A multiplier for specular lighting.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `VertexShader`
    - The path to a vertex shader program to use instead of the default shader.
    - `File`
    
    - Value of type 'File' 
    
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
































(RenderableModelLightSources-target)=
::::{dropdown} Table parameters for `LightSources`
A list of light sources that this model should accept light from.


* Optional: Yes


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
    
    - [LightSource](#core_light_source)
    
    - Yes
    
:::



::::


















## Asset Examples


:::{dropdown} Basic

This example loads a model.

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 19

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",
  },
  GUI = {
    Name = "RenderableModel - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Animation

This example loads a model with an animation. The animation starts at a set time, in
this case "2024 07 09 12:00:00".

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 24

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Animation",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Animation Parameters:
    EnableAnimation = true,
    -- Start the animation and play it once at this time
    AnimationStartTime = "2024 07 09 12:00:00",
  },
  GUI = {
    Name = "RenderableModel - Basic Animation",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Animation Bounce From Start

This example loads a model with an animation. The animation starts at a set time, in
this case "2024 07 09 12:00:00" and is set to bounce after that time (bounce is similar
to a boomerang for videos).

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 26

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Animation_Bounce",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Animation Parameters:
    EnableAnimation = true,
    -- Start the animation and play it once at this time
    AnimationStartTime = "2024 07 09 12:00:00",
    -- Bounce the animation after the set start time
    AnimationMode = "BounceFromStart",
  },
  GUI = {
    Name = "RenderableModel - Animation Bounce From Start",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Animation Bounce Infinitely

This example loads a model with an animation. The animation starts at a set time, in
this case "2024 07 09 12:00:00" and is set to bounce both before and after that time
(bounce is similar to a boomerang for videos).

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 26

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Animation_Bounce_Infinitely",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Animation Parameters:
    EnableAnimation = true,
    -- Start the animation and play it once at this time
    AnimationStartTime = "2024 07 09 12:00:00",
    -- Bounce the animation both before and after the set start time
    AnimationMode = "BounceInfinitely",
  },
  GUI = {
    Name = "RenderableModel - Animation Bounce Infinitely",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Animation Loop From Start

This example loads a model with an animation. The animation starts at a set time, in
this case "2024 07 09 12:00:00" and is set to loop after that time.

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 26

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Animation_Loop",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Animation Parameters:
    EnableAnimation = true,
    -- Start the animation and play it once at this time
    AnimationStartTime = "2024 07 09 12:00:00",
    -- Loop the animation after the set start time
    AnimationMode = "LoopFromStart",
  },
  GUI = {
    Name = "RenderableModel - Animation Loop From Start",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Animation Loop Infinitely

This example loads a model with an animation. The animation starts at a set time, in
this case "2024 07 09 12:00:00" and is set to loop both before and after that time.

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 26

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Animation_Loop_Infinitely",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Animation Parameters:
    EnableAnimation = true,
    -- Start the animation and play it once at this time
    AnimationStartTime = "2024 07 09 12:00:00",
    -- Loop the animation both before and after the set start time
    AnimationMode = "LoopInfinitely",
  },
  GUI = {
    Name = "RenderableModel - Animation Loop Infinitely",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Lighting

This example loads a model and load the Sun to illuminate it.

:::{code-block} lua
:linenos:
:emphasize-lines: 16, 27

-- Load the asset of the Sun to illuminate the model
local sun = asset.require("scene/solarsystem/sun/transforms")

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Animated Box",
  Type = "HttpSynchronization",
  Identifier = "animated_box",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Lighting",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "BoxAnimated.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",

    -- Add the Sun as a light source to illuminate the model
    LightSources = {
      sun.LightSource
    }
  },
  GUI = {
    Name = "RenderableModel - Lighting",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Cesium, https://cesium.com/
  URL = https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0/BoxAnimated
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::



:::{dropdown} Vertex Colors

This example loads a model with vertex colors as material.

:::{code-block} lua
:linenos:
:emphasize-lines: 13, 19

-- Load the example model from OpenSpace servers
-- If you want to use your own model, this block of code can be safely deleted
local model = asset.resource({
  Name = "Vertex Colors Test Model",
  Type = "HttpSynchronization",
  Identifier = "model_vertex_color_test",
  Version = 1
})

local Node = {
  Identifier = "RenderableModel_Example_Vertex_Colors",
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "VertexColorTest.glb",
    -- Use the line below insted of the one above if you want to use your own model
    --GeometryFile = "C:/path/to/model.fbx",
  },
  GUI = {
    Name = "RenderableModel - Vertex Colors",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)


-- Model credit
--[[
  Author = Ed Mackey
  URL = "https://github.com/KhronosGroup/glTF-Sample-Models/tree/main/2.0/VertexColorTest"
  License =
    Creative Commons Attribution 4.0 International License,
    https://creativecommons.org/licenses/by/4.0/
]]

:::
:::


