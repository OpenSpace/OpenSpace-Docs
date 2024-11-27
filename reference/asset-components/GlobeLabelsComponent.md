



(globebrowsing_globelabelscomponent)=
# GlobeLabelsComponent




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

*   - `AlignmentOption`
    - Labels are aligned horizontally or circularly related to the planet.
    - `String`
    
    - In list { Horizontally, Circularly } 
    
    - Yes
    
*   - `Color`
    - The text color of the labels.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `DisableCulling`
    - Labels culling disabled.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `DistanceEPS`
    - Labels culling distance from globe's center.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Enabled`
    - Enables and disables labels' rendering.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeDistances`
    - The distances above the globe's surface at which the labels start fading in or out, given in meters. The final distances are also adjusted by the specified height offset.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FadeInEnabled`
    - Sets whether the labels fade in when approaching the globe from a distance. If false, no fading happens and the labels immediately has full opacity.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeOutEnabled`
    - Sets whether the labels fade out when approaching the surface of the globe. If false, no fading happens and the labels stays in full opacity.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FileName`
    - The path to the labels file
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `FontSize`
    - Font size for the rendering labels. This is different fromt text size.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `HeightOffset`
    - This value moves the label away from the globe surface by the specified distance (in meters).
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MinMaxSize`
    - Minimum and maximum label size, in pixels.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of the labels
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `Size`
    - This value affects the size scale of the labels.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::


































