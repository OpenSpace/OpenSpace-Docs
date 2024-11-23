



(generate_raw_volume_task)=
# GenerateRawVolumeTask

_Inherits [Task](#core_task)_




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

*   - `DictionaryOutput`
    - The lua dictionary file to export metadata to
    - `String`
    
    - A valid filepath 
    
    - {bdg-info}`No`
    
*   - `Dimensions`
    - A vector representing the number of cells in each dimension
    - `Vector3<int>`
    
    - Value of type 'Vector3<int>' 
    
    - {bdg-info}`No`
    
*   - `LowerDomainBound`
    - A vector representing the lower bound of the domain
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `RawVolumeOutput`
    - The raw volume file to export data to
    - `String`
    
    - A valid filepath 
    
    - {bdg-info}`No`
    
*   - `Time`
    - The timestamp that is written to the metadata of this volume
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `UpperDomainBound`
    - A vector representing the upper bound of the domain
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `ValueFunction`
    - The Lua function used to compute the cell values
    - `String`
    
    - A Lua expression that returns a  function taking three numbers as arguments (x, y, z) and returning a  number 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [Task](#core_task)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - This key specifies the type of Task that gets created. It has to be one of the valid Tasks that are available for creation (see the FactoryDocumentation for a list of possible Tasks), which depends on the configration of the application
    - `String`
    
    - A valid Task created by a factory 
    
    - {bdg-info}`No`
    
:::



















