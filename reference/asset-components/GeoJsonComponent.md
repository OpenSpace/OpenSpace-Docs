



(globebrowsing_geojsoncomponent)=
# GeoJsonComponent




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

*   - `File`
    - Path to the GeoJSON file to base the rendering on.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Identifier`
    - The unique identifier for this layer. May not contain '.' or spaces
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `CoordinateOffset`
    - A latitude and longitude offset value, in decimal degrees. Can be used to move the object on the surface and correct potential mismatches with other renderings. Note that changing it during runtime leads to all positions being recomputed.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `DefaultProperties`
    - These properties will be used as default values for the geoJson rendering, meaning that they will be used when there is no value given for the individual geoJson features
    - `Table`
    
    - [GeoJsonProperties](#globebrowsing_geojsonproperties)
    
    - Yes
    
*   - `Description`
    - A human-readable description of the layer to be used in informational texts presented to the user
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `DrawWireframe`
    - If true, draw the wire frame of the polygons. Used for testing and to investigate tessellation results.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - This setting determines whether this object will be visible or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `HeightOffset`
    - A height offset value, in meters. Useful for moving a feature closer to or farther away from the surface.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `IgnoreHeights`
    - If true, ignore any height values that are given in the file. Coordinates with three values will then be treated as coordinates with only two values
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LightSources`
    - A list of light sources that this object should accept light from
    - `Table`
    
    -   [Table parameters](#GeoJsonComponentLightSources-target) 
    
    - Yes
    
*   - `LineWidthScale`
    - An extra scale value that can be used to increase or decrease the width of any rendered lines in the component, even if a value is set from the GeoJson file. Note that there is a max limit for how wide lines can be.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Name`
    - A human-readable name for the user interface. If this is omitted, the identifier is used instead
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Opacity`
    - The opacity of the component
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `PointRenderMode`
    - Decides how the billboards for the points should be rendered in terms of up direction and whether the plane should face the camera. See details on the different options in the wiki.
    - `String`
    
    - In list { Camera Direction, Camera Position, Globe Normal, Globe Surface } 
    
    - Yes
    
*   - `PointSizeScale`
    - An extra scale value that can be used to increase or decrease the scale of any rendered points in the component, even if a value is set from the GeoJson file.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PreventHeightUpdate`
    - If true, the polygon mesh will not be automatically updated based on the heightmap, even if the 'RelativeToGround' altitude option is set and the heightmap updates. The data can still be force updated.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::

























(GeoJsonComponentLightSources-target)=
::::{dropdown} Table parameters for `LightSources`
A list of light sources that this object should accept light from


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    - [LightSource](#core_light_source)
    
    - Yes
    
:::



::::















