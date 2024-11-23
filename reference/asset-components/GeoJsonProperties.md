



(globebrowsing_geojsonproperties)=
# GeoJsonProperties




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

*   - `AltitudeMode`
    - The altitude mode decides how any height values of the geo coordinates should be interpreted. Absolute means that the height is interpreted as the height above the reference ellipsoid, while RelativeToGround takes the height map into account. For coordinates with only two values (latitude and longitude), the height is considered to be equal to zero.
    - `String`
    
    - In list { Absolute, RelativeToGround } 
    
    - Yes
    
*   - `Color`
    - The color of the rendered geometry. For points it will be used as a multiplycolor for any provided texture.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Extrude`
    - If true, extrude the geometry to intersect the globe.Lines/polygons will beextruded with polygons,and points with lines.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FillColor`
    - The color of the filled portion of a rendered polygon. Will also be used for extruded features.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `FillOpacity`
    - This value determines the opacity of the filled portion of a polygon. Will also be used for extruded features.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `LineWidth`
    - The width of any rendered lines.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of this object. A value of 0 means completely transparent.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `PerformShading`
    - If true, perform shading on any create meshes, either from polygons or extruded lines. The shading will be computed based on any light sources of the GeoJson component.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `PointSize`
    - The size of any rendered points. The size will be scaled based on the bounding sphere of the globe.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `PointTexture`
    - A texture to be used for rendering points. No value means to use the default texture provided by the GlobeBrowsing module. If no texture is provided there either, the point will be rendered as a plane and colored by the color value.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `PointTextureAnchor`
    - Decides the placement of the point texture in relation to the position. Default is a the bottom of the texture, but it can also be put at the center.
    - `String`
    
    - In list { Bottom, Center } 
    
    - Yes
    
*   - `Tessellation`
    - 
    - `Table`
    
    -   [Table parameters](#GeoJsonPropertiesTessellation-target) 
    
    - Yes
    
:::





























(GeoJsonPropertiesTessellation-target)=
::::{dropdown} Table parameters for `Tessellation`



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

*   - `Enabled`
    - If false, no tessellation to bend the geometry based on the curvature of the planet is performed. This leads to increased performance, but tessellation is neccessary for large geometry that spans a big portion of the globe. Otherwise it may intersect the surface.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `TessellationDistance`
    - Defult distance to use for tessellation of line and polygon geometry. Anything larger than this distance will be automatically subdivided into smaller pieces matching this distance, while anything smaller will not be subdivided. Per default this will be set to a distance corresponding to about 1 degree longitude on the globe.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `TessellationLevel`
    - When manual tessellation is enabled, this value will be used to determine how much tessellation to apply. The resulting distance used for subdividing the geometry will be the 'Tessellation Distance' divided by this value. Zero means to use the 'Tessellation Distance' as is.
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `UseTessellationLevel`
    - If true, use the 'Tessellation Level' to control the level of detail for the tessellation. The distance used will be the 'Tessellation Distance' divided by the 'Tessellation Level', so the higher the level value, the smaller each segment in the geomoetry will be.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



::::



