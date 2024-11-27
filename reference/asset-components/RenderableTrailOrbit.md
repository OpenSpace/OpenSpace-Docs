



(base_renderable_renderabletrailorbit)=
# RenderableTrailOrbit

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
    - This value determines the RGB main color for the lines and points of the trail.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - {bdg-info}`No`
    
*   - `Period`
    - The objects period, i.e. the length of its orbit around the parent object given in (Earth) days. In the case of Earth, this would be a sidereal year (=365.242 days). If this values is specified as multiples of the period, it is possible to show the effects of precession.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Resolution`
    - The number of samples along the orbit. This determines the resolution of the trail; the tradeoff being that a higher resolution is able to resolve more detail, but will take more resources while rendering, too. The higher, the smoother the trail, but also more memory will be used.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `Translation`
    - A translation used to compute locations along the path.
    - `Table`
    
    - [Translation](#core_transform_translation)
    
    - {bdg-info}`No`
    
*   - `EnableFade`
    - Toggles whether the trail should fade older points out. If this value is true, the 'Fade' parameter determines the speed of fading. If this value is false, the entire trail is rendered at full opacity and color.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LineFadeAmount`
    - The amount of the trail that should be faded. If the value is 0 then the trail will have no fading applied. A value of 0.6 will result in a trail where 60% of the extent of the trail will have fading applied to it. In otherwords, the 40% closest to the head of the trail will be solid and the rest will fade until completely transparent at the end of the trail. A value of 1 will result in a trail that starts fading immediately, becoming fully transparent by the end of the trail. This setting only applies if the 'EnableFade' value is true. If it is false, this setting has no effect.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineLength`
    - The extent of the rendered trail. A value of 0 will result in no trail and a value of 1 will result in a trail that covers the entire extent. The setting only applies if 'EnableFade' is true. If it is false, this setting has no effect.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineWidth`
    - Specifies the line width of the trail lines, if the selected rendering method includes lines. If the rendering mode is Points, this value is ignored.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PointSize`
    - Specifies the base size of the points along the line, if the selected rendering method includes points. If the rendering mode is Lines, this value is ignored. If a subsampling of the values is performed, the subsampled values are half this size.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `Rendering`
    - Determines how the trail should be rendered. If 'Lines' is selected, only the line part is visible, if 'Points' is selected, only the corresponding points (and subpoints) are shown. 'Lines+Points' shows both parts.
    - `String`
    
    - In list { Lines, Points, Lines+Points, Lines+Points } 
    
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
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")
local transforms = asset.require("./transforms")



local Trail = {
  Identifier = "ErisTrail",
  Parent = sunTransforms.SunEclipJ2000.Identifier,
  Renderable = {
    Type = "RenderableTrailOrbit",
    Enabled = asset.enabled,
    Translation = transforms.Translation,
    Color = { 0.2, 0.8, 0.3 },
    Period = 205472.1258735657,
    Resolution = 10000,
    Fade = 1.24
  },
  Tag = { "planetTrail_dwarf" },
  GUI = {
    Name = "Eris Trail",
    Path = "/Solar System/Dwarf Planets/Eris"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Trail)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Trail)
end)

asset.export("Trail", Trail)



asset.meta = {
  Name = "Eris Trail",
  Description = [[Trail of Eris]],
  Author = "OpenSpace Team",
  URL = "https://www.openspaceproject.com",
  License = "MIT"
}

:::
:::


