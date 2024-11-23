



(labelscomponent)=
# LabelsComponent




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
    - The color of the labels.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Enabled`
    - This setting determines whether the labels will be visible or not. They are disabled per default.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FaceCamera`
    - If enabled, the labels will be rotated to face the camera. For non-linear display rendering (for example fisheye) this should be set to false.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `File`
    - The speck label file with the data for the labels.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `FontSize`
    - Font size for the labels. This is different from the text size.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MinMaxSize`
    - The minimum and maximum size (in pixels) of the labels.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `Opacity`
    - The opacity of the labels
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `Size`
    - The size of the labels in pixels.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `TransformationMatrix`
    - Transformation matrix to be applied to the labels.
    - `Matrix4x4<double>`
    
    - Value of type 'Matrix4x4<double>' 
    
    - Yes
    
*   - `Unit`
    - 
    - `String`
    
    - In list { m, Km, pc, Kpc, Mpc, Gpc, Gly } 
    
    - Yes
    
*   - `UseCaching`
    - If true (default), the loaded labels file will be cached so that it can be loaded faster at a later time. Note that this also means that changes in the file will not be registered until the cached file is deleted. Set to false to disable chaching and always do a fresh load of the label file
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::




























