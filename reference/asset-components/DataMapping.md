



(dataloader_datamapping)=
# DataMapping

This is a data mapping structure that can be used when creating point cloud datasets, e.g. from a CSV or Speck file.

It allows specifying things like column names, whether the reading of those column names should be case sensitive, data value that represents missing values in the dataset, and more. See details for each field / class member.

Note that things related to reading the point position will not be handled for SPECK files, as for those we always expect the first three values per row to specify the XYZ position


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

*   - `CaseSensitive`
    - Specifies whether to do case sensitive checks when reading column names. Default is not to, so that 'X' and 'x' are both valid column names for the x position column, for example
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ExcludeColumns`
    - A list of column names, of columns that will not be loaded into the dataset. Note that not all data formats support this. E.g. SPECK files do not
    - `Table`
    
    -   [Table parameters](#DataMappingExcludeColumns-target) 
    
    - Yes
    
*   - `MissingDataValue`
    - Specifies a value that, when read from the file, should be interpreted as 'no value', i.e. a missing data value. Note that the same value is used across all data columns
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Name`
    - Specifies the column name for the optional name column. Not valid for SPECK files, where the name is given by the comment at the end of each line
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `TextureColumn`
    - Specifies a column name for a column that has the data for which texture to use for each point (given as an integer index). If included, a texture map file need to be included as well
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `TextureMapFile`
    - A file where each line contains an integer index and an image file name. Not valid for SPECK files, which includes this information as part of its data format. This map will be used to map the data in the TextureColumn to an image file to use for rendering the points. Note that only the files with indices that are used in the dataset will actually be loaded
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `X`
    - Specifies the column name for the x coordinate
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Y`
    - Specifies the column name for the y coordinate
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Z`
    - Specifies the column name for the z coordinate
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::









(DataMappingExcludeColumns-target)=
::::{dropdown} Table parameters for `ExcludeColumns`
A list of column names, of columns that will not be loaded into the dataset. Note that not all data formats support this. E.g. SPECK files do not


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

















