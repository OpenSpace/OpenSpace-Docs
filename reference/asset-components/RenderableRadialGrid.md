



(base_renderable_radialgrid)=
# RenderableRadialGrid

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

*   - `CircleSegments`
    - The number of segments that is used to render each circle in the grid.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `Color`
    - The color used for the grid lines.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `GridSegments`
    - Specifies the number of segments for the grid, in the radial and angular direction respectively.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `Labels`
    - The labels for the grid.
    - `Table`
    
    - [LabelsComponent](#labelscomponent)
    
    - Yes
    
*   - `LineWidth`
    - The width of the grid lines. The larger number, the thicker the lines.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Radii`
    - The radii values that determine the size of the circular grid. The first value is the radius of the inmost ring and the second is the radius of the outmost ring.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
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
:emphasize-lines: 12, 34
local AU = 149597870700 -- 1 AU

local Circle = {
  Identifier = "ExampleCircle",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = AU
    }
  },
  Renderable = {
    Type = "RenderableRadialGrid",
    Color = { 0.6, 0.6, 0.8 },
    LineWidth = 3.0,
    GridSegments = { 1, 1 },
    CircleSegments = 64,
    Radii = { 0.0, 1.0 }
  },
  GUI = {
    Name = "Example Circle",
    Path = "/Examples/Primitives"
  }
}

local Ellipse = {
  Identifier = "ExampleEllipse",
  Transform = {
    Scale = {
      Type = "NonUniformStaticScale",
      Scale = { 1.5, 1.0, 1.0 }
    }
  },
  Renderable = {
    Type = "RenderableRadialGrid",
    Color = { 0.6, 0.8, 0.6 },
    LineWidth = 3.0,
    GridSegments = { 1, 1 },
    CircleSegments = 64,
    Radii = { 0.0, AU }
  },
  GUI = {
    Name = "Example Ellipse",
    Path = "/Examples/Primitives"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Circle)
  openspace.addSceneGraphNode(Ellipse)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Ellipse)
  openspace.removeSceneGraphNode(Circle)
end)

asset.export(Circle)
asset.export(Ellipse)



asset.meta = {
  Name = "Primitives Example",
  Description = [[Examples of different simple rendered primitives, such as circles
    and ellipses.]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


