



(base_renderable_renderabletravelspeed)=
# RenderableTravelSpeed

_Inherits [Renderable](#renderable)_

This renderable can be used to visualize a certain travel speed using a line that moves at the provided speed from a start object to a target. The start position will be set from the `Parent` of this scene graph node, and the end position is set from the provided `Target` scene graph node. Per default, the speed is set to the speed of light.

The length of the traveling line is set based on the travel speed and can be used to show more information related to the distance traveled. For example, a length of 1 shows how far an object would move over a duration of one second based on the selected speed.


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

*   - `Target`
    - The identifier of the scene graph node to target with the speed indicator. The speed indicator will travel from the parent node to this scene graph node.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Color`
    - An RGB color for the line.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `FadeLength`
    - The length of the faded tail of the speed indicator, given in seconds. The length of the tail will be computed as the speed times this value. For example, a value of 1 will make it as long as the distance it would travel over one second. A linear fade will be applied over this distance to create the tail.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `IndicatorLength`
    - The length of the speed indicator line, given in seconds. The length will be computed as the speed times this value. For example, a value of 1 will make it as long as the distance it would travel over one second with the specified speed.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `LineWidth`
    - This value specifies the line width.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `TravelSpeed`
    - A value for how fast the speed indicator should travel, in meters per second. The default value is the speed of light.
    - `Double`
    
    - Greater than: 0 
    
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


:::{dropdown} Light Speed Indicator

This example creates a speed indicator; a line that travels with the speed of
light from the parent node (Earth) to the target node (the Moon). By default, the
length of the line is set to match the distance traveled over 1 second.

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 12

local earthAsset = asset.require("scene/solarsystem/planets/earth/earth")
local moonAsset = asset.require("scene/solarsystem/planets/earth/moon/moon")

local Node = {
  Identifier = "RenderableTravelSpeed_Example",
  Parent = earthAsset.Earth.Identifier,
  Renderable = {
    Type = "RenderableTravelSpeed",
    Target = moonAsset.Moon.Identifier
  },
   GUI = {
     Name = "RenderableTravelSpeed - Light Speed Indicator",
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


