



(base_renderable_grid)=
# RenderableGrid

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

*   - `Color`
    - The color of the grid lines.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `HighlightColor`
    - The color of the highlighted lines in the grid.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `HighlightLineWidth`
    - The width of the highlighted grid lines. The larger number, the thicker the lines.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `HighlightRate`
    - The rate that the columns and rows are highlighted, counted with respect to the center of the grid. If the number of segments in the grid is odd, the highlighting might be offset from the center.
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
    
*   - `Segments`
    - The number of segments to split the grid into, in each direction (x and y).
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `Size`
    - The size of the grid (in the x and y direction), given in meters.
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
:emphasize-lines: 36
local AU = 149597870700 -- 1 AU

local RadialGrid = {
  Identifier = "ExampleRadialGrid",
  Parent = "Root",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = AU
    }
  },
  Renderable = {
    Type = "RenderableRadialGrid",
    Opacity = 0.8,
    Color = { 0.6, 1.0, 0.7 },
    LineWidth = 3.0,
    GridSegments = { 3, 4 },
    Radii = { 0.2, 1.0 }
  },
  GUI = {
    Name = "Example Radial Grid",
    Description = "A circular 2D grid, with segments based on the radius and angle.",
    Path = "/Examples/Grids"
  }
}

local PlanarGrid = {
  Identifier = "ExampleGrid",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = AU
    }
  },
  Renderable = {
    Type = "RenderableGrid",
    Color = { 0.0, 1.0, 0.8 },
    LineWidth = 2.0,
    Segments = { 6, 10 },
    Size = { 1, 2 },
    HighlightColor = { 1.0, 0.8, 0.0 },
    HighlightLineWidth = 3.2,
    HighlightRate = { 3, 3 }
  },
  GUI = {
    Name = "Example Grid",
    Description = "A basic 2D grid, with a given size and number of segments.",
    Path = "/Examples/Grids"
  }
}

local SphericalGrid = {
  Identifier = "ExampleSphericalGrid",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = AU
    }
  },
  Renderable = {
    Type = "RenderableSphericalGrid",
    Color = { 1.0, 0.5, 0.2 },
    LineWidth = 2.0,
    Segments = 40
  },
  GUI = {
    Name = "Example Spherical Grid",
    Description = "A grid in the form of a 3D sphere.",
    Path = "/Examples/Grids"
  }
}

local BoxGrid = {
  Identifier = "ExampleBoxGrid",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = AU
    }
  },
  Renderable = {
    Type = "RenderableBoxGrid",
    Enabled = false,
    Color = { 0.5, 0.0, 1.0 },
    LineWidth = 2.0,
    Size = { 2, 2, 2 },
  },
  GUI = {
    Name = "Example Box Grid",
    Description = "A grid in the form of a 3D box.",
    Path = "/Examples/Grids"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(RadialGrid)
  openspace.addSceneGraphNode(PlanarGrid)
  openspace.addSceneGraphNode(SphericalGrid)
  openspace.addSceneGraphNode(BoxGrid)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(BoxGrid)
  openspace.removeSceneGraphNode(SphericalGrid)
  openspace.removeSceneGraphNode(PlanarGrid)
  openspace.removeSceneGraphNode(RadialGrid)
end)

asset.export(RadialGrid)
asset.export(PlanarGrid)
asset.export(SphericalGrid)
asset.export(BoxGrid)



asset.meta = {
  Name = "Example Grids",
  Description = [[Examples of different types of rendered grids.]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


