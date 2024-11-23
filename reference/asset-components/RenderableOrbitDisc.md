



(exoplanets_renderableorbitdisc)=
# RenderableOrbitDisc

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

*   - `Eccentricity`
    - The eccentricity of the orbit, which is the deviation from a perfect circle.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Size`
    - The size of the semi-major axis of the orbit in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - The path to a file with a one-dimensional texture to be used for the disc color. The leftmost color will be innermost color when rendering the disc, and the rightmost color will be the outermost color.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `MultiplyColor`
    - If set, the disc's texture is multiplied with this color. Useful for applying a color grayscale images.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Offset`
    - The width of the disc, given as two values that specify the lower and upper deviation from the semi major axis, respectively. The values are relative to the size of the semi-major axis. That is, 0 means no deviation from the semi-major axis and 1 is a whole semi-major axis's worth of deviation.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
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















