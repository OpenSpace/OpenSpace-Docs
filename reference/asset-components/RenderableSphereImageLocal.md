



(base_renderable_sphere_image_local)=
# RenderableSphereImageLocal

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
    - The path to an image on disk to use as a texture for this sphere. The image is expected to be an equirectangular projection.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `DisableFadeInOut`
    - Enables/Disables the fade in and out effects.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeInThreshold`
    - The distance from the center of the Milky Way at which the sphere should start to fade in, given as a percentage of the size of the object. A value of zero means that no fading in will happen.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `FadeOutThreshold`
    - A threshold for when the sphere should start fading out, given as a percentage of how much of the sphere that is visible before the fading should start. A value of zero means that no fading out will happen.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `LazyLoading`
    - If true, the image for this sphere will not be loaded at startup but rather when the image is shown for the first time. Additionally, if the sphere is disabled, the image will automatically be unloaded.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MirrorTexture`
    - If true, mirror the texture along the x-axis.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Orientation`
    - Specifies whether the texture is applied to the inside of the sphere, the outside of the sphere, or both.
    - `String`
    
    - In list { Outside, Inside, Both } 
    
    - Yes
    
*   - `Segments`
    - The number of segments that the sphere is split into.
    - `Integer`
    
    - Greater or equal to: 4 
    
    - Yes
    
*   - `Size`
    - The radius of the sphere in meters.
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


:::{dropdown} Basic

This example shows a sphere that is covered with an image which is retrieved from
a local file path. The image will be stretched over the entire sphere as an
equirectangular projection.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 8

local Node = {
  Identifier = "RenderableSphereImageLocal_Example",
  Renderable = {
    Type = "RenderableSphereImageLocal",
    Texture = openspace.absPath("${DATA}/test2.jpg")
  },
  GUI = {
    Name = "RenderableSphereImageLocal - Basic",
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


