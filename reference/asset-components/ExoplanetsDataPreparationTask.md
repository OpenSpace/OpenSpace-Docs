



(exoplanets_data_preparation_task)=
# ExoplanetsDataPreparationTask

_Inherits [Task](#core_task)_

This task is used for generating the binary data files that are used for the exoplanet system loading in OpenSpace. Using this binary file allows efficient data loading of an arbitrary exoplanet system during runtime, without keeping all data in memory.

Two output files are generated, whose paths have to be specified: One binary with the data for the exoplanets (OutputBIN) and one look-up table that is used to find where in the binary file a particular system is located (OutputLUT).

Additionally, the task uses three different files as input: 1) a CSV file with the data from the NASA Exoplanet Archive, 2) A SPECK file that contains star positions, and 3) a TXT file that is used for the conversion from the stars' effective temperature to a B-V color index. The paths for all these paths have to be specified. The SPECK file (2) will be used for the positions of the host stars, to make sure that they line up with the stars in that dataset. The cross-matching is done by star name, as given by the comment in the SPECK file and the host star column in the exoplanet dataset.

Note that the CSV (1) has to include a certain set of columns for the rendering to be correct. Use the accompanying python script to download the datafile, or make sure to include all columns in your download.


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

*   - `InputDataFile`
    - The csv file to extract data from
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `InputSPECK`
    - The speck file with star locations
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `OutputBIN`
    - The bin file to export data into
    - `String`
    
    - A valid filepath 
    
    - {bdg-info}`No`
    
*   - `OutputLUT`
    - The txt file to write look-up table into
    - `String`
    
    - A valid filepath 
    
    - {bdg-info}`No`
    
*   - `TeffToBvFile`
    - The path to a teff to bv conversion file. Should be a txt file where each line has the format 'teff,bv'
    - `String`
    
    - Value of type 'String' 
    
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















