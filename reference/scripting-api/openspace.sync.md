# `openspace.sync`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`syncResource`](#syncsyncResource-target)
    - [Synchronizes the http resource identified by the name passed as the first parameter and the version provided as the second parameter]{#syncsyncResource-list}


*   - [`unsyncResource`](#syncunsyncResource-target)
    - [Unsynchronizes the http resources identified by the name passed as the first parameter by removing all data that was downloaded as part of the original synchronization]{#syncunsyncResource-list}

:::

## Functions

(syncsyncResource-target)=
### [`syncResource`](#syncsyncResource-list)
Synchronizes the http resource identified by the name passed as the first parameter and the version provided as the second parameter. The application will hang while the data is being downloaded.


:::{card} Parameters


* identifier `String` 



* version `Integer` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.sync.syncResource(identifier, version)
:::
___

(syncunsyncResource-target)=
### [`unsyncResource`](#syncunsyncResource-list)
Unsynchronizes the http resources identified by the name passed as the first parameter by removing all data that was downloaded as part of the original synchronization. If the second parameter is provided, is it the version of the resources that is unsynchronized, if the parameter is not provided, all versions for the specified http resource are removed.


:::{card} Parameters


* identifier `String` 



* version `Integer?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sync.unsyncResource(identifier, version)
:::

