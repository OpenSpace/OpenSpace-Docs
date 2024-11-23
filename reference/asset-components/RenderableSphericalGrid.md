



(base_renderable_sphericalgrid)=
# RenderableSphericalGrid

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
    - The number of segments the sphere is split into. Determines the resolution of the rendered sphere. Should be an even value (if an odd value is provided, the value will be set to the new value minus one).
    - `Integer`
    
    - Value of type 'Integer' 
    
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
:emphasize-lines: 15
-- Ellipsoid
-- This asset creates a SceneGraphNode that is rendering a sphere which is adjust to an
-- ellipsoidal shape by using a non-uniform scaling. In particular, the second axis is
-- half as long as the first, and the third axis is a third as long.

local Node = {
  Identifier = "NonUniformStaticScale_Example_Ellipsoid",
  Transform = {
    Scale = {
      Type = "NonUniformStaticScale",
      Scale = { 149597870700, 149597870700 / 2, 149597870700 / 3 }
    }
  },
  Renderable = {
    Type = "RenderableSphericalGrid"
  },
  GUI = {
    Name = "NonUniformStaticScale - Ellipsoid",
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


