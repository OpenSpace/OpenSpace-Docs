



(skybrowser_renderableskytarget)=
# RenderableSkyTarget

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

*   - `ApplyRoll`
    - If true, always rotate the target to have its up direction aligned with the up direction of the camera.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `CrossHairSize`
    - The size of the crosshair given as a field of view (in degrees).
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LineWidth`
    - The thickness of the line of the target. The larger number, the thicker line.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `RectangleThreshold`
    - A threshold value for the vertical field of view, in degrees, that decides when a rectangle will be used to visualize the target in addition to the crosshair. When the field of view is smaller than this value, only the crosshair will be shown.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `VerticalFov`
    - The vertical field of view of the target.
    - `Double`
    
    - Value of type 'Double' 
    
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















