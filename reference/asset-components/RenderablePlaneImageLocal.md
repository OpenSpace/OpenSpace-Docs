



(base_renderable_plane_image_local)=
# RenderablePlaneImageLocal

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

*   - `Size`
    - The size of the plane in meters.
    - `Double, or Vector2<double>`
    
    - Value of type 'Double', or Value of type 'Vector2<double>' 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - A path to an image file to use as a texture for the plane.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `AutoScale`
    - Decides whether the plane should automatically adjust in size to match the aspect ratio of the content. Otherwise it will remain in the given size.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Billboard`
    - Specifies whether the plane should be a billboard, which means that it is always facing the camera. If it is not, it can be oriented using other transformations.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `BlendMode`
    - Determines the blending mode that is applied to this plane.
    - `String`
    
    - In list { Normal, Additive } 
    
    - Yes
    
*   - `LazyLoading`
    - If this value is set to true, the image for this plane will not be loaded at startup but rather when image is shown for the first time. Additionally, if the plane is hidden, the image will automatically be unloaded.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MirrorBackside`
    - If false, the image plane will not be mirrored when viewed from the backside. This is usually desirable when the image shows data at a specific location, but not if it is displaying text for example.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MultiplyColor`
    - An RGB color to multiply with the plane's texture. Useful for applying a color to grayscale images.
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


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 17
local transforms = asset.require("./moon")



local texturesPath = asset.resource({
  Name = "Moon Textures",
  Type = "HttpSynchronization",
  Identifier = "moon_textures",
  Version = 3
})


local MoonMarker = {
  Identifier = "MoonMarker",
  Parent = transforms.Moon.Identifier,
  Renderable = {
    Type = "RenderablePlaneImageLocal",
    Enabled = false,
    Size = 3.0E7,
    Origin = "Center",
    Billboard = true,
    Texture = texturesPath .. "marker.png",
    BlendMode = "Additive"
  },
  GUI = {
    Name = "Moon Marker",
    Path = "/Solar System/Planets/Earth/Moon"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(MoonMarker)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(MoonMarker)
end)

asset.export(MoonMarker)



asset.meta = {
  Name = "Moon marker",
  Description = "Moon marker with name, sized for Earth view",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


