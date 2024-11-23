# `openspace.asset`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`add`](#assetadd-target)
    - [Adds an asset to the current scene]{#assetadd-list}


*   - [`allAssets`](#assetallAssets-target)
    - [Returns the paths to all loaded assets, loaded directly or indirectly, as a table containing the paths to all loaded assets]{#assetallAssets-list}


*   - [`isLoaded`](#assetisLoaded-target)
    - [Returns true if the referenced asset already has been loaded]{#assetisLoaded-list}


*   - [`remove`](#assetremove-target)
    - [Removes the asset with the specfied name from the scene]{#assetremove-list}


*   - [`removeAll`](#assetremoveAll-target)
    - [Removes all assets that are currently loaded]{#assetremoveAll-list}


*   - [`rootAssets`](#assetrootAssets-target)
    - [Returns the paths to all loaded root assets, which are assets that are loaded directly either through a profile or by calling the `openspace]{#assetrootAssets-list}

:::

## Functions

(assetadd-target)=
### [`add`](#assetadd-list)
Adds an asset to the current scene. The parameter passed into this function is the path to the file that should be loaded.


:::{card} Parameters


* assetName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.asset.add(assetName)
:::
___

(assetallAssets-target)=
### [`allAssets`](#assetallAssets-list)
Returns the paths to all loaded assets, loaded directly or indirectly, as a table containing the paths to all loaded assets.


Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.asset.allAssets()
:::
___

(assetisLoaded-target)=
### [`isLoaded`](#assetisLoaded-list)
Returns true if the referenced asset already has been loaded. Otherwise false is returned. The parameter to this function is the path of the asset that should be tested.


:::{card} Parameters


* assetName `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.asset.isLoaded(assetName)
:::
___

(assetremove-target)=
### [`remove`](#assetremove-list)
Removes the asset with the specfied name from the scene. The parameter to this function is the same that was originally used to load this asset, i.e. the path to the asset file.


:::{card} Parameters


* assetName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.asset.remove(assetName)
:::
___

(assetremoveAll-target)=
### [`removeAll`](#assetremoveAll-list)
Removes all assets that are currently loaded


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.asset.removeAll()
:::
___

(assetrootAssets-target)=
### [`rootAssets`](#assetrootAssets-list)
Returns the paths to all loaded root assets, which are assets that are loaded directly either through a profile or by calling the `openspace.asset.add` method.


Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.asset.rootAssets()
:::

