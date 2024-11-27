



(base_renderable_renderablenodeline)=
# RenderableNodeLine

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
    - The RGB color for the line.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `EndNode`
    - The identifier of the node the line ends at. Defaults to 'Root' if not specified.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - Yes
    
*   - `EndOffset`
    - A distance to the end node at which the rendered line should end. By default it takes a value in meters, but if 'UseRelativeOffsets' is set to true it is read as a multiplier times the bounding sphere of the node.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineWidth`
    - The width of the line. The larger number, the thicker the line.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `StartNode`
    - The identifier of the node the line starts from. Defaults to 'Root' if not specified.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - Yes
    
*   - `StartOffset`
    - A distance from the start node at which the rendered line should begin. By default it takes a value in meters, but if 'UseRelativeOffsets' is set to true it is read as a multiplier times the bounding sphere of the node.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `UseRelativeOffsets`
    - If true, the offset values are interpreted as relative values to be multiplied with the bounding sphere of the start/end node. If false, the value is interpreted as a distance in meters.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
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
:emphasize-lines: 9
local earth = asset.require("scene/solarsystem/planets/earth/earth")
local mars = asset.require("scene/solarsystem/planets/mars/mars")



local RenderableNodeLineExample = {
  Identifier = "RenderableNodeLineExample",
  Renderable = {
    Type = "RenderableNodeLine",
    StartNode = earth.Earth.Identifier,
    EndNode = mars.Mars.Identifier,
    Color = { 0.5, 0.5, 0.5 },
    LineWidth = 2
  },
  GUI = {
    Name = "RenderableNodeLine - Basic",
    Path = "/Examples",
    Description = "Draws a line between two nodes in the scene."
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(RenderableNodeLineExample)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(RenderableNodeLineExample)
end)

asset.export(RenderableNodeLineExample)



asset.meta = {
  Name = "RenderableNodeLine Example asset",
  Description = [[Example of a RenderableNodeLine, that can be used to draw an line
    between two scene graph nodes.]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


