



(space_renderablehabitablezone)=
# RenderableHabitableZone

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

*   - `EffectiveTemperature`
    - The effective temperature of the corresponding star, in Kelvin. Used to compute the width and size of the disc.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Luminosity`
    - The luminosity of the corresponding star, in units of solar luminosities. Used to compute the width and size of the disc.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - The path to a file with a one-dimensional texture to be used for the disc color. The leftmost color will be innermost color when rendering the disc, and the rightmost color will be the outermost color.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `KopparapuTeffInterval`
    - The effective temperature interval for which Kopparapu's formula is used for the habitable zone computation. For stars with temperatures outside the range, a simpler method by Tom E. Harris is used. This method only uses the star luminosity and does not include computation of the optimistic boundaries.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `Optimistic`
    - If true, the habitable zone disc is rendered with the optimistic boundaries rather than the conservative ones.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
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
:emphasize-lines: 10
local transforms = asset.require("./transforms")
local textures = asset.require("scene/milkyway/habitable_zones/habitable_zone_textures")



local HabitableZone = {
  Identifier = "SunHabitableZone",
  Parent = transforms.SunEclipJ2000.Identifier,
  Renderable = {
    Type = "RenderableHabitableZone",
    Enabled = false,
    Texture = textures.TexturesPath .. "hot_to_cold_faded.png",
    EffectiveTemperature = 5780, -- Kelvin
    Luminosity = 1, -- solar
    Opacity = 0.1,
    Optimistic = true
  },
  GUI = {
    Name = "Sun Habitable Zone",
    Path = "/Solar System/Sun",
    Description = "Habitable zone for the sun in our solar system"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(HabitableZone)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(HabitableZone)
end)

asset.export(HabitableZone)



asset.meta = {
  Name = "Sun Habitable Zone",
  Description = [[The habitable zone around our sun, computed using formula and
    coefficients by Kopparapu et al. (2015) https://arxiv.org/abs/1404.5292]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


