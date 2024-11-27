



(globebrowsing_rings_component)=
# RingsComponent




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

*   - `ColorFilter`
    - This value affects the filtering out of part of the rings depending on the color values of the texture. The higher value, the more rings are filtered out.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Enabled`
    - Enable/Disable Rings.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `NightFactor`
    - This value is a multiplicative factor that is applied to the side of the rings that is facing away from the Sun. If this value is equal to '1', no darkening of the night side occurs.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `NumberShadowSamples`
    - The number of samples used during shadow mapping calculation (Percentage Closer Filtering).
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `Offset`
    - This value is used to limit the width of the rings. Each of the two values is a value between 0 and 1, where 0 is the center of the ring and 1 is the maximum extent at the radius. For example, if the value is {0.5, 1.0}, the ring is only shown between radius/2 and radius. It defaults to {0.0, 1.0}.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the overall opacity of the rings
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `Size`
    - This value specifies the radius of the rings in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Texture`
    - This value is the path to a texture on disk that contains a one-dimensional texture which is used for these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `TextureBckwrd`
    - This value is the path to a texture on disk that contains a one-dimensional texture which is used for backward scattering light in these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `TextureColor`
    - This value is the path to a texture on disk that contains a one-dimensional texture color which is used for unlit part in these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `TextureFwrd`
    - This value is the path to a texture on disk that contains a one-dimensional texture which is used for forward scattering light in these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `TextureTransparency`
    - This value is the path to a texture on disk that contains a one-dimensional texture transparency which is used for unlit part in these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `TextureUnlit`
    - This value is the path to a texture on disk that contains a one-dimensional texture which is used for unlit part in these rings.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `ZFightingPercentage`
    - The percentage of the correct distance to the surface being shadowed. Possible values: [0.0, 1.0].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::


































