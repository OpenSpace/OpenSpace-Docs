# `openspace.systemCapabilities`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`cacheLineSize`](#systemCapabilitiescacheLineSize-target)
    - [Returns the cache line size]{#systemCapabilitiescacheLineSize-list}


*   - [`cacheSize`](#systemCapabilitiescacheSize-target)
    - [Returns the cache size]{#systemCapabilitiescacheSize-list}


*   - [`cores`](#systemCapabilitiescores-target)
    - [Returns the number of cores]{#systemCapabilitiescores-list}


*   - [`extensions`](#systemCapabilitiesextensions-target)
    - [Returns all supported exteions as comma-separated string]{#systemCapabilitiesextensions-list}


*   - [`fullOperatingSystem`](#systemCapabilitiesfullOperatingSystem-target)
    - [Returns the operating system as a string]{#systemCapabilitiesfullOperatingSystem-list}


*   - [`installedMainMemory`](#systemCapabilitiesinstalledMainMemory-target)
    - [Returns the amount of available, installed main memory (RAM) on the system in MB]{#systemCapabilitiesinstalledMainMemory-list}


*   - [`L2Associativity`](#systemCapabilitiesL2Associativity-target)
    - [Returns the L2 associativity]{#systemCapabilitiesL2Associativity-list}


*   - [`os`](#systemCapabilitiesos-target)
    - [This function returns a string identifying the currently running operating system]{#systemCapabilitiesos-list}

:::

## Functions

(systemCapabilitiescacheLineSize-target)=
### [`cacheLineSize`](#systemCapabilitiescacheLineSize-list)
Returns the cache line size.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.cacheLineSize()
:::
___

(systemCapabilitiescacheSize-target)=
### [`cacheSize`](#systemCapabilitiescacheSize-list)
Returns the cache size.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.cacheSize()
:::
___

(systemCapabilitiescores-target)=
### [`cores`](#systemCapabilitiescores-list)
Returns the number of cores.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.cores()
:::
___

(systemCapabilitiesextensions-target)=
### [`extensions`](#systemCapabilitiesextensions-list)
Returns all supported exteions as comma-separated string.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.extensions()
:::
___

(systemCapabilitiesfullOperatingSystem-target)=
### [`fullOperatingSystem`](#systemCapabilitiesfullOperatingSystem-list)
Returns the operating system as a string. The exact format of the returned string is implementation and operating system-dependent but it should contain the manufacturer and the version.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.fullOperatingSystem()
:::
___

(systemCapabilitiesinstalledMainMemory-target)=
### [`installedMainMemory`](#systemCapabilitiesinstalledMainMemory-list)
Returns the amount of available, installed main memory (RAM) on the system in MB.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.installedMainMemory()
:::
___

(systemCapabilitiesL2Associativity-target)=
### [`L2Associativity`](#systemCapabilitiesL2Associativity-list)
Returns the L2 associativity.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.L2Associativity()
:::
___

(systemCapabilitiesos-target)=
### [`os`](#systemCapabilitiesos-list)
This function returns a string identifying the currently running operating system. For Windows, the string is 'windows', for MacOS, it is 'osx', and for Linux it is 'linux'. For any other operating system, this function returns 'other'.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.systemCapabilities.os()
:::

