



(base_renderable_cartesianaxes)=
# RenderableCartesianAxes

_Inherits [Renderable](#renderable)_

The RenderableCartesianAxes can be used to render the local Cartesian coordinate system, or reference frame, of another scene graph node. The colors of the axes can be customized but are per default set to Red, Green and Blue, for the X-, Y- and Z-axis, respectively.

To add the axes, create a scene graph node with the RenderableCartesianAxes renderable and add it as a child to the other scene graph node, i.e. specify the other node as the Parent of the node with this renderable. Also, the axes have to be scaled to match the parent object for the axes to be visible in the scene, for example using a StaticScale.


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

*   - `XColor`
    - The color of the x-axis.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `YColor`
    - The color of the y-axis.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `ZColor`
    - The color of the z-axis.
    - `Color3`
    
    - Value of type 'Color3' 
    
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


:::{dropdown} Basic

This asset creates a SceneGraphNode that only displays coordinate axes. The
parent is not set which defaults to placing the axes at the center the Sun.

:::{code-block} lua
:linenos:
:emphasize-lines: 10, 13

local Node = {
  Identifier = "RenderableCartesianAxes_Example",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = 30000000
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "RenderableCartesianAxes - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::


