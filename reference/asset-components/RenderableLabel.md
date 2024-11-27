



(base_renderable_labels)=
# RenderableLabel

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

*   - `BlendMode`
    - This determines the blending mode that is applied to the renderable.
    - `String`
    
    - In list { Normal, Additive } 
    
    - Yes
    
*   - `Color`
    - The label text color.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `EnableFading`
    - Enable/Disable the Fade-in effect.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeDistances`
    - The distance range in which the labels should be fully opaque, specified in the chosen unit. The distance from the position of the label to the camera.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FadeUnit`
    - Distance unit for fade-in/-out distance calculations. Defaults to "au".
    - `String`
    
    - In list { m, Km, Mm, Gm, Tm, Pm, au, pc, Kpc, Mpc, Gpc, Gly } 
    
    - Yes
    
*   - `FadeWidths`
    - The distances over which the fading takes place, given in the specified unit. The first value is the distance before the closest distance and the second the one after the furthest distance. For example, with the unit Parsec (pc), a value of {1, 2} will make the label being fully faded out 1 Parsec before the closest distance and 2 Parsec away from the furthest distance.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FontSize`
    - The font size (in points) for the label.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MinMaxSize`
    - The minimum and maximum size (in pixels) of the label.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `OrientationOption`
    - Label orientation rendering mode.
    - `String`
    
    - In list { Camera View Direction, Camera Position Normal } 
    
    - Yes
    
*   - `Size`
    - Scales the size of the label, exponentially. The value is used as the exponent in a 10^x computation to scale the label size.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Text`
    - The text that will be displayed on screen.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `TransformationMatrix`
    - Transformation matrix to be applied to the label.
    - `Matrix4x4<double>`
    
    - Value of type 'Matrix4x4<double>' 
    
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
:emphasize-lines: 13
local transforms = asset.require("./transforms")



local JWSTLabel = {
  Identifier = "JWSTLabel",
  Parent = transforms.JWSTPosition.Identifier,
  TimeFrame = {
    Type = "TimeFrameInterval",
    Start = transforms.LaunchTime
  },
  Renderable = {
    Type = "RenderableLabel",
    Enabled = asset.enabled,
    Text = "JWST",
    FontSize = 50,
    Size = 6.5,
    MinMaxSize = { 4.0, 30.0 },
    OrientationOption = "Camera View Direction",
    BlendMode = "Normal",
    EnableFading = false
  },
  GUI = {
    Name = "JWST Label",
    Path = "/Solar System/Telescopes/JWST",
    Description = "Main label for the James Webb Space Telescope."
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(JWSTLabel)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(JWSTLabel)
end)

asset.export(JWSTLabel)



asset.meta = {
  Name = "JWST Label",
  Description = "Main label for the James Webb Space Telescope",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


