# `openspace.exoplanets`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addExoplanetSystem`](#exoplanetsaddExoplanetSystem-target)
    - [Add one or multiple exoplanet systems to the scene, as specified by the input]{#exoplanetsaddExoplanetSystem-list}


*   - [`getListOfExoplanets`](#exoplanetsgetListOfExoplanets-target)
    - [Deprecated in favor of 'listOfExoplanets']{#exoplanetsgetListOfExoplanets-list}


*   - [`listAvailableExoplanetSystems`](#exoplanetslistAvailableExoplanetSystems-target)
    - []{#exoplanetslistAvailableExoplanetSystems-list}


*   - [`listOfExoplanets`](#exoplanetslistOfExoplanets-target)
    - [Returns a list with names of the host star of all the exoplanet systems that have sufficient data for generating a visualization, based on the module's loaded data file]{#exoplanetslistOfExoplanets-list}


*   - [`loadExoplanetsFromCsv`](#exoplanetsloadExoplanetsFromCsv-target)
    - [Load a set of exoplanets based on custom data, in the form of a CSV file, and add them to the rendering]{#exoplanetsloadExoplanetsFromCsv-list}


*   - [`removeExoplanetSystem`](#exoplanetsremoveExoplanetSystem-target)
    - []{#exoplanetsremoveExoplanetSystem-list}

:::

## Functions

(exoplanetsaddExoplanetSystem-target)=
### [`addExoplanetSystem`](#exoplanetsaddExoplanetSystem-list)
Add one or multiple exoplanet systems to the scene, as specified by the input. An input string should be the name of the system host star.


:::{card} Parameters


* starNames `String | String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.addExoplanetSystem(starNames)
:::
___

(exoplanetsgetListOfExoplanets-target)=
### [`getListOfExoplanets`](#exoplanetsgetListOfExoplanets-list)
Deprecated in favor of 'listOfExoplanets'


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.getListOfExoplanets()
:::
___

(exoplanetslistAvailableExoplanetSystems-target)=
### [`listAvailableExoplanetSystems`](#exoplanetslistAvailableExoplanetSystems-list)



Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.listAvailableExoplanetSystems()
:::
___

(exoplanetslistOfExoplanets-target)=
### [`listOfExoplanets`](#exoplanetslistOfExoplanets-list)
Returns a list with names of the host star of all the exoplanet systems that have sufficient data for generating a visualization, based on the module's loaded data file.


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.listOfExoplanets()
:::
___

(exoplanetsloadExoplanetsFromCsv-target)=
### [`loadExoplanetsFromCsv`](#exoplanetsloadExoplanetsFromCsv-list)
Load a set of exoplanets based on custom data, in the form of a CSV file, and add them to the rendering. Can be used to load custom datasets, or more recent planets than what are included in the internal data file that is released with OpenSpace.

The format and column names in the CSV sould be the same as the ones provided by the NASA Exoplanet Archive. https://exoplanetarchive.ipac.caltech.edu/

We recommend downloading the file from the Exoplanet Archive's Composite data table, where multiple sources are combined into one row per planet. https://exoplanetarchive.ipac.caltech.edu /cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars

Please remember to include all columns in the file download, as missing data columns may lead to an incomplete visualization.

Also, avoid loading too large files of planets, as each added system will affect the rendering performance.


:::{card} Parameters


* csvFile `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.loadExoplanetsFromCsv(csvFile)
:::
___

(exoplanetsremoveExoplanetSystem-target)=
### [`removeExoplanetSystem`](#exoplanetsremoveExoplanetSystem-list)



:::{card} Parameters


* starName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.exoplanets.removeExoplanetSystem(starName)
:::

