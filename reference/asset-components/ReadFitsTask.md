



(gaiamission_fitsfiletorawdata)=
# ReadFitsTask

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

*   - `InFileOrFolderPath`
    - If SingleFileProcess is set to true then this specifies the path to a single FITS file that will be read. Otherwise it specifies the path to a folder with multiple FITS files that are to be read
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `OutFileOrFolderPath`
    - If SingleFileProcess is set to true then this specifies the name (including entire path) to the output file. Otherwise it specifies the path to the output folder which to export binary star data to
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `FilterColumnNames`
    - A list of strings with the names of all the additional columns that are to be read from the specified FITS file(s). These columns can be used for filtering while constructing Octree later
    - `Table`
    
    -   [Table parameters](#ReadFitsTaskFilterColumnNames-target) 
    
    - Yes
    
*   - `FirstRow`
    - Defines the first row that will be read from the specified FITS file(s). If not defined then reading will start at first row
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LastRow`
    - Defines the last row that will be read from the specified FITS file(s). If not defined (or less than FirstRow) then full file(s) will be read
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `SingleFileProcess`
    - If true then task will read from a single FITS file and output a single binary file. If false then task will read all files in specified folder and output multiple files sorted by location
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ThreadsToUse`
    - Defines how many threads to use when reading from multiple files
    - `Integer`
    
    - Greater than: 1 
    
    - Yes
    
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










(ReadFitsTaskFilterColumnNames-target)=
::::{dropdown} Table parameters for `FilterColumnNames`
A list of strings with the names of all the additional columns that are to be read from the specified FITS file(s). These columns can be used for filtering while constructing Octree later


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











