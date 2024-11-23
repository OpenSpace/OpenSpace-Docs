# `openspace.iswa`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addCdfFiles`](#iswaaddCdfFiles-target)
    - [Adds a cdf files to choose from]{#iswaaddCdfFiles-list}


*   - [`addCygnet`](#iswaaddCygnet-target)
    - [Adds a IswaCygnet]{#iswaaddCygnet-list}


*   - [`addKameleonPlanes`](#iswaaddKameleonPlanes-target)
    - [Adds KameleonPlanes from cdf file]{#iswaaddKameleonPlanes-list}


*   - [`addScreenSpaceCygnet`](#iswaaddScreenSpaceCygnet-target)
    - [Adds a Screen Space Cygnets]{#iswaaddScreenSpaceCygnet-list}


*   - [`removeCygnet`](#iswaremoveCygnet-target)
    - [Remove a Cygnets]{#iswaremoveCygnet-list}


*   - [`removeGroup`](#iswaremoveGroup-target)
    - [Remove a group of Cygnets]{#iswaremoveGroup-list}


*   - [`removeScreenSpaceCygnet`](#iswaremoveScreenSpaceCygnet-target)
    - [Remove a Screen Space Cygnets]{#iswaremoveScreenSpaceCygnet-list}


*   - [`setBaseUrl`](#iswasetBaseUrl-target)
    - [Sets the base url]{#iswasetBaseUrl-list}

:::

## Functions

(iswaaddCdfFiles-target)=
### [`addCdfFiles`](#iswaaddCdfFiles-list)
Adds a cdf files to choose from.


:::{card} Parameters


* path `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.addCdfFiles(path)
:::
___

(iswaaddCygnet-target)=
### [`addCygnet`](#iswaaddCygnet-list)
Adds a IswaCygnet.


:::{card} Parameters


* id `Integer?` - Default value: `-1` 



* type `String?` - Default value: `"Texture"` 



* group `String?` - Default value: `""` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.addCygnet(id, type, group)
:::
___

(iswaaddKameleonPlanes-target)=
### [`addKameleonPlanes`](#iswaaddKameleonPlanes-list)
Adds KameleonPlanes from cdf file.


:::{card} Parameters


* group `String` 



* pos `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.addKameleonPlanes(group, pos)
:::
___

(iswaaddScreenSpaceCygnet-target)=
### [`addScreenSpaceCygnet`](#iswaaddScreenSpaceCygnet-list)
Adds a Screen Space Cygnets.


:::{card} Parameters


* d `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.addScreenSpaceCygnet(d)
:::
___

(iswaremoveCygnet-target)=
### [`removeCygnet`](#iswaremoveCygnet-list)
Remove a Cygnets.


:::{card} Parameters


* name `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.removeCygnet(name)
:::
___

(iswaremoveGroup-target)=
### [`removeGroup`](#iswaremoveGroup-list)
Remove a group of Cygnets.


:::{card} Parameters


* name `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.removeGroup(name)
:::
___

(iswaremoveScreenSpaceCygnet-target)=
### [`removeScreenSpaceCygnet`](#iswaremoveScreenSpaceCygnet-list)
Remove a Screen Space Cygnets.


:::{card} Parameters


* id `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.removeScreenSpaceCygnet(id)
:::
___

(iswasetBaseUrl-target)=
### [`setBaseUrl`](#iswasetBaseUrl-list)
Sets the base url.


:::{card} Parameters


* url `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.iswa.setBaseUrl(url)
:::

