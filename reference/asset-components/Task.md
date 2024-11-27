



(core_task)=
# Task

The base class of all tasks. Specify the Type property to create one of the available task types. This property should be included in the same table object as the properties of the specific task.

Tasks can be executed using the separate TaskRunner application. When starting the application, just enter the path to the file describing the task you want to run as input in the command line to initiate the run. All tasks should live in the task folder in the data folder of the OpenSpace installation.


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

*   - `Type`
    - This key specifies the type of Task that gets created. It has to be one of the valid Tasks that are available for creation (see the FactoryDocumentation for a list of possible Tasks), which depends on the configration of the application
    - `String`
    
    - A valid Task created by a factory 
    
    - {bdg-info}`No`
    
:::








