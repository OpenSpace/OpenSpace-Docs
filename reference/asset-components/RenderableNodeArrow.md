



(base_renderable_renderablenodearrow)=
# RenderableNodeArrow

_Inherits [Renderable](#renderable)_

A RenderableNodeArrow can be used to create a 3D arrow pointing in the direction of one scene graph node to another.

The arrow will be placed at the `StartNode` at a distance of the provided `Offset` value. Per default, the `Length` and `Offset` of the arrow is specified in meters, but they may also be specified as a multiplier of the bounding sphere of the `StartNode`. The look of the arrow can be customized to change the width and length of both the arrow body and head.


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

*   - `EndNode`
    - The identifier of the node the arrow should point towards.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `StartNode`
    - The identifier of the node the arrow starts from.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `AmbientIntensity`
    - A multiplier for ambient lighting for the shading of the arrow.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `ArrowHeadSize`
    - The length of the arrow head, given in relative value of the entire length of the arrow. For example, 0.1 makes the arrow head length be 10% of the full arrow length.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `ArrowHeadWidthFactor`
    - A factor that is multiplied with the width, or the arrow itself, to determine the width of the base of the arrow head.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `Color`
    - The RGB color for the arrow.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `DiffuseIntensity`
    - A multiplier for diffuse lighting for the shading of the arrow.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `Invert`
    - If true, the arrow direction is inverted so that it points to the start node instead of the end node.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Length`
    - The length of the arrow, given either in meters or as a factor to be multiplied with the bounding sphere of the start node (if 'UseRelativeLength' is true).
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `Offset`
    - The distance from the center of the start node where the arrow starts. If 'UseRelativeOffset' is true, the value should be given as a factor to multiply with the bounding sphere of the node. Otherwise, the value is specified in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PerformShading`
    - Determines whether shading should be applied to the arrow model.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Segments`
    - The number of segments that the shapes of the arrow are divided into. A higher number leads to a higher resolution and smoother shape.
    - `Integer`
    
    - Greater or equal to: 3 
    
    - Yes
    
*   - `SpecularIntensity`
    - A multiplier for specular lighting for the shading of the arrow.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `UseRelativeLength`
    - Decides whether to use relative size for the length of the arrow. This means that the arrow length will be computed as the provided 'Length' value times the bounding sphere of the start node. If false, meters is used.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseRelativeOffset`
    - Decides whether to use relative distances for the offset distance. This means that the offset distance will be computed as the provided 'Offset' value times the bounding sphere of the start node. If false, meters is used.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Width`
    - The width of the arrow, in meters.
    - `Double`
    
    - Greater or equal to: 0 
    
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

This example shows an arrow pointing from one scene graph node in the direction of
another. Here, it points from Earth to Mars.
Note that the arrows are generated as objects in 3D space and need to have a size
that is suitable for the scene graph nodes they refer to. Here it is set based on
the size of the Earth.

:::{code-block} lua
:linenos:
:emphasize-lines: 9, 20

local earth = asset.require("scene/solarsystem/planets/earth/earth")
local mars = asset.require("scene/solarsystem/planets/mars/mars")

local Node = {
  Identifier = "RenderableNodeArrow_Example",
  -- Parent to the start node, so that when we focus on the arrow this is where we end up
  Parent = earth.Earth.Identifier,
  Renderable = {
    Type = "RenderableNodeArrow",
    StartNode = earth.Earth.Identifier,
    EndNode = mars.Mars.Identifier,
    -- How far away from the start node should the arrow start (meters)
    Offset = 2 * 6371000.0,
    -- How long should the arrow be (meters)
    Length = 5 * 6371000.0,
    -- How wide should the arrow be (meters)
    Width = 900000.0
  },
  GUI = {
    Name = "RenderableNodeArrow - Basic",
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



:::{dropdown} Relative Units for Offset and Length

This example shows an arrow pointing from one scene graph node in the direction of
another, but where the size is specified using relative values (based on the bounding
sphere of the start node). Here it points from Earth to the Moon.
Note that the arrows are generated as objects in 3D space and need to have a size
that is suitable for the scene graph nodes they refer to. Here it is set based on
the size of the start node, i.e. Earth.

:::{code-block} lua
:linenos:
:emphasize-lines: 9, 22

local earth = asset.require("scene/solarsystem/planets/earth/earth")
local moon = asset.require("scene/solarsystem/planets/earth/moon/moon")

local Node = {
  Identifier = "RenderableNodeArrow_Example_Relative",
  -- Parent to the start node, so that when we focus on the arrow this is where we end up
  Parent = earth.Earth.Identifier,
  Renderable = {
    Type = "RenderableNodeArrow",
    StartNode = earth.Earth.Identifier,
    EndNode = moon.Moon.Identifier,
    -- Use relative values for offset and length
    UseRelativeOffset = true,
    UseRelativeLength = true,
    -- Specify relative values (times the size of Earth, in this case)
    Offset = 2.0,
    Length = 5.0,
    -- Width is in meters
    Width = 900000.0
  },
  GUI = {
    Name = "RenderableNodeArrow - Relative Units",
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



:::{dropdown} Custom Appearance (Colored & Inverted)

This example shows an arrow pointing from one scene graph node in the direction of
another. Here, it is created with the Solar System barycenter as start node and
Earth as end node, but the arrow direction is inverted so that it points towards
the Solar System barycenter. Some appearance related properties are also changed to
customize the look of the arrow, but default values are used for its size.

:::{code-block} lua
:linenos:
:emphasize-lines: 9, 23

local earth = asset.require("scene/solarsystem/planets/earth/earth")
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")

local Node = {
  Identifier = "RenderableNodeArrow_Example_Appearance",
  -- Parent to the start node, so that when we focus on the arrow this is where we end up
  Parent = sunTransforms.SolarSystemBarycenter.Identifier,
  Renderable = {
    Type = "RenderableNodeArrow",
    StartNode = sunTransforms.SolarSystemBarycenter.Identifier,
    EndNode = earth.Earth.Identifier,
    -- Point to start node instead of end node
    Invert = true,
    -- Give the arrow a custom color (here a dark red)
    Color = { 0.5, 0.0, 0.0 },
    -- Set the arrow head size so that it takes up a quarter (25%) of the full length of
    -- the arrow
    ArrowHeadSize = 0.25,
    -- Set the arrow head width. A value of 1 makes it as wide as the body of the arrow
    ArrowHeadWidthFactor = 1.0
  },
  GUI = {
    Name = "RenderableNodeArrow - Custom Appearance (Colored & Inverted)",
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


