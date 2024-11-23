# `openspace.parallel`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`connect`](#parallelconnect-target)
    - [Connect to parallel]{#parallelconnect-list}


*   - [`disconnect`](#paralleldisconnect-target)
    - [Disconnect from parallel]{#paralleldisconnect-list}


*   - [`joinServer`](#paralleljoinServer-target)
    - []{#paralleljoinServer-list}


*   - [`requestHostship`](#parallelrequestHostship-target)
    - [Request to be the host for this session]{#parallelrequestHostship-list}


*   - [`resignHostship`](#parallelresignHostship-target)
    - [Resign hostship]{#parallelresignHostship-list}

:::

## Functions

(parallelconnect-target)=
### [`connect`](#parallelconnect-list)
Connect to parallel.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.parallel.connect()
:::
___

(paralleldisconnect-target)=
### [`disconnect`](#paralleldisconnect-list)
Disconnect from parallel.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.parallel.disconnect()
:::
___

(paralleljoinServer-target)=
### [`joinServer`](#paralleljoinServer-list)



:::{card} Parameters


* port `String` 



* address `String` 



* password `String` 



* hostpassword `String?` - Default value: `""` 



* name `String?` - Default value: `"Anonymous"` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.parallel.joinServer(port, address, password, hostpassword, name)
:::
___

(parallelrequestHostship-target)=
### [`requestHostship`](#parallelrequestHostship-list)
Request to be the host for this session.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.parallel.requestHostship()
:::
___

(parallelresignHostship-target)=
### [`resignHostship`](#parallelresignHostship-list)
Resign hostship.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.parallel.resignHostship()
:::

