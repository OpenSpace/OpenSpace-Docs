



(base_renderable_prism)=
# RenderablePrism

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

*   - `Segments`
    - The number of segments the shape of the prism should have.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `BaseRadius`
    - The radius of the base of the prism's shape, in meters. By default it is given the same radius as the outer shape.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Color`
    - The RGB color of the line.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Length`
    - The length of the prism in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Lines`
    - The number of lines connecting the two shapes of the prism. They will be evenly distributed around the bounding circle that makes up the shape of the prism.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LineWidth`
    - The width of the lines. The larger number, the thicker the lines.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Radius`
    - The radius of the prism's shape in meters.
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
:emphasize-lines: 14
local transforms = asset.require("./transforms")
local model = asset.require("./model")



local JWSTFov = {
  Identifier = "JWSTFov",
  Parent = model.JWSTModel.Identifier,
  TimeFrame = {
    Type = "TimeFrameInterval",
    Start = transforms.LaunchTime
  },
  Renderable = {
    Type = "RenderablePrism",
    Enabled = asset.enabled,
    Segments = 6,
    Lines = 3,
    Radius = 3.25,
    LineWidth = 1.0,
    Color = { 1.0, 1.0, 1.0 },
    Length = 9.2E15
  },
  Transform = {
    Rotation = {
      Type = "StaticRotation",
      Rotation = { 0, 0, math.rad(30) }
    }
  },
  Tag = { "mission_jwst_fov" },
  GUI = {
    Name = "JWST Field of View",
    Path = "/Solar System/Telescopes/JWST",
    Description = [[
      The field of view for the James Webb Space Telescope at its current position.
    ]]
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(JWSTFov)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(JWSTFov)
end)

asset.export(JWSTFov)



asset.meta = {
  Name = "JWST Field of View",
  Description = [[
    The field of view for the James Webb Space Telescope at its current position.
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


