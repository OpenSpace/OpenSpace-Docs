



(space_renderable_rings)=
# RenderableRings

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
    - The radius of the rings in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - The path to a texture on disk that contains a one-dimensional texture to use for these rings.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `ColorFilter`
    - A value that affects the filtering out of part of the rings depending on the color values of the texture. The higher value, the more rings are filtered out.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `NightFactor`
    - A multiplicative factor that is applied to the side of the rings that is facing away from the Sun. If it is 1, no darkening of the night side occurs.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Offset`
    - A value that is used to limit the width of the rings. Each of the two values is a value between 0 and 1, where 0 is the center of the ring and 1 is the maximum extent at the radius. For example, if the value is {0.5, 1.0}, the ring is only shown between radius/2 and radius. It defaults to {0.0, 1.0}.
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















