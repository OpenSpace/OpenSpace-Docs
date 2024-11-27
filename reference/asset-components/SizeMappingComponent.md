



(base_sizemappingcomponent)=
# SizeMappingComponent




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

*   - `Enabled`
    - If this value is set to 'true' and at least one column was loaded as an option for size mapping, the chosen data column will be used to scale the size of the points. The first option in the list is selected per default.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `IsRadius`
    - If true, the size value in the data is interpreted as the radius of the points. Otherwise, it is interpreted as the diameter.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Parameter`
    - This value determines which parameter is used for scaling of the point. The parameter value will be used as a multiplicative factor to scale the size of the points. Note that they may however still be scaled by max size adjustment effects.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ParameterOptions`
    - A list specifying all parameters that may be used for size mapping, i.e. scaling the points based on the provided data columns.
    - `Table`
    
    -   [Table parameters](#SizeMappingComponentParameterOptions-target) 
    
    - Yes
    
*   - `ScaleFactor`
    - The scale used for the size values in the dataset, given as either a string representing a specific unit or a value to multiply all the datapoints with to convert the value to meter. The resulting value will be applied as a multiplicative factor. For example, if the size data is given in is in kilometers then specify either <code>ScaleFactor = 'Kilometer'</code> or <code>ScaleFactor = 1000.0</code>.
    - `String, or Double`
    
    - In list { Nanometer, Micrometer, Millimeter, Centimeter, Decimeter, Meter, Kilometer, AU, Lighthour, Lightday, Lightmonth, Lightyear, Parsec, Kiloparsec, Megaparsec, Gigaparsec, Gigalightyear }, or Value of type 'Double' 
    
    - Yes
    
:::













(SizeMappingComponentParameterOptions-target)=
::::{dropdown} Table parameters for `ParameterOptions`
A list specifying all parameters that may be used for size mapping, i.e. scaling the points based on the provided data columns.


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
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::





