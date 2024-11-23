



(base_renderable_disc)=
# RenderableDisc

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

*   - `Texture`
    - The path to a file with a one-dimensional texture to be used for the disc color. The leftmost color will be innermost color when rendering the disc, and the rightmost color will be the outermost color.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Size`
    - The outer radius of the disc, in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Width`
    - The disc width, given as a ratio of the full disc radius. For example, a value of 1 results in a full circle, while 0.5 results in a disc where the inner radius is half of the full radius.
    - `Double`
    
    - In range: ( 0,1 ) 
    
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
:emphasize-lines: 8, 30
-- @TODO (emmbr 2020-02-03) Potential threading issue later on? This will run on the main thread
local cyanTexture = openspace.createSingleColorImage("example_disc_color1", { 0.0, 1.0, 1.0 })
local purpleTexture = openspace.createSingleColorImage("example_disc_color2", { 0.5, 0.0, 0.5 })

local BasicDisc = {
  Identifier = "BasicDisc",
  Renderable = {
    Type = "RenderableDisc",
    Texture = cyanTexture,
    Size = 1e10,
    Width = 0.5
  },
  GUI = {
    Name = "Basic Disc",
    Path = "/Examples/Discs"
  }
}

-- Elliptic discs can be created using a non-uniform scaling
-- For a full disc, use a width of 1.0
local FullEllipticDisc = {
  Identifier = "FullEllipticDisc",
  Transform = {
    Scale = {
      Type = "NonUniformStaticScale",
      Scale = { 2.0, 1.0, 1.0 }
    }
  },
  Renderable = {
    Type = "RenderableDisc",
    Texture = purpleTexture,
    Size = 2e10,
    Width = 1.0
  },
  GUI = {
    Name = "Full Elliptic Disc",
    Path = "/Examples/Discs"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(BasicDisc)
  openspace.addSceneGraphNode(FullEllipticDisc)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(FullEllipticDisc)
  openspace.removeSceneGraphNode(BasicDisc)
end)

asset.export(BasicDisc)
asset.export(FullEllipticDisc)



asset.meta = {
  Name = "Example Discs",
  Description = [[Examples of different types of rendered discs.]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


