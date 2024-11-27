



(colormappingcomponent)=
# ColorMappingComponent




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

*   - `AboveRangeColor`
    - The color to use for items with values larger than the one in the provided data range, if enabled. This color can also be read from the color map, but setting this value overrides any value in the color map. If a color value for the above range values is provided, the UseAboveRangeColor property will automatically be set to true.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `BelowRangeColor`
    - The color to use for items with values smaller than the one in the provided data range, if enabled. This color can also be read from the color map, but setting this value overrides any value in the color map. If a color value for the below range values is provided, the UseBelowRangeColor property will automatically be set to true.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `Enabled`
    - If this value is set to 'true', the provided color map is used (if one was provided in the configuration). If no color map was provided, changing this setting does not do anything.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `File`
    - The path to the color map file to use for coloring the points.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `HideValuesOutsideRange`
    - If true, points with values outside the provided range for the coloring will be hidden, i.e. not rendered at all.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Invert`
    - If true, the colors of the color map will be read in the inverse order.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `NoDataColor`
    - The color to use for items with values corresponding to missing data values, if enabled. This color can also be read from the color map, but setting this value overrides any value in the color map. If a color value for the below range values is provided, the ShowMissingData property will automatically be set to true.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `Parameter`
    - This value determines which paramenter is used for coloring the points based on the color map. The property is set based on predefined options specified in the asset file. When changing the parameter, the value range to used for themapping will also be changed. Per default, it is set to the last parameter in the list of options.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ParameterOptions`
    - A list of options for color parameters to use for color mapping, that will appear as options in the drop-down menu in the user interface. Per default, the first option in the list is selected. Each option is a table in the form { Key = "theKey", Range = {min, max} }, where the value range is optional. If added, this range will automatically be set when the option is selected
    - `Table`
    
    -   [Table parameters](#ColorMappingComponentParameterOptions-target) 
    
    - Yes
    
*   - `ShowMissingData`
    - If true, use a separate color (see NoDataColor) for items with values corresponding to missing data values.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseAboveRangeColor`
    - If true, use a separate color (see AboveRangeColor) for items with values larger than the one in the provided data range. Otherwise, the values will be clamped to use the color at the upper limit of the color map. If a color is provided in the color map, this value will automatically be set to true.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseBelowRangeColor`
    - If true, use a separate color (see BelowRangeColor) for items with values smaller than the one in the provided data range. Otherwise, the values will be clamped to use the color at the lower limit of the color map. If a color is provided in the color map, this value will automatically be set to true.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ValueRange`
    - This value changes the range of values to be mapped with the current color map.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
:::























(ColorMappingComponentParameterOptions-target)=
::::{dropdown} Table parameters for `ParameterOptions`
A list of options for color parameters to use for color mapping, that will appear as options in the drop-down menu in the user interface. Per default, the first option in the list is selected. Each option is a table in the form { Key = "theKey", Range = {min, max} }, where the value range is optional. If added, this range will automatically be set when the option is selected


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
    
    -   [Table parameters](#ColorMappingComponentParameterOptions*-target) 
    
    - Yes
    
:::



(ColorMappingComponentParameterOptions*-target)=
#### Table parameters for `*`



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

*   - `Key`
    - The key for the data variable to use for color
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Range`
    - An optional value range to use for coloring when this option is selected. If not included, the range will be set from the min and max value in the dataset
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
:::




::::











