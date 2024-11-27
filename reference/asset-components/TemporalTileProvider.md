



(globebrowsing_temporaltileprovider)=
# TemporalTileProvider

_Inherits [TileProvider](#TileProvider)_




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

*   - `Mode`
    - The mode that his temporal tile provider operates in. In the `Prototyped` mode, a given start and end time, temporal resolution, and perscriptive time format is used to generate the information used by GDAL to access the data. In the `folder` method, a folder and a time format is provided and each file in the folder is scanned using the time format instead
    - `String`
    
    - In list { Prototyped, Folder } 
    
    - {bdg-info}`No`
    
*   - `Colormap`
    - If provided, the tile provider will use this color map to convert a greyscale image to color
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `FixedTime`
    - If the 'UseFixedTime' is enabled, this time will be used instead of the actual time taken from OpenSpace for the displayed tiles.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Folder`
    - 
    - `Table`
    
    -   [Table parameters](#TemporalTileProviderFolder-target) 
    
    - Yes
    
*   - `Interpolation`
    - Determines whether this tile provider should interpolate between two adjacent layers
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Prototyped`
    - 
    - `Table`
    
    -   [Table parameters](#TemporalTileProviderPrototyped-target) 
    
    - Yes
    
*   - `UseFixedTime`
    - If this value is enabled, the time-varying timevarying dataset will always use the time that is specified in the 'FixedTime' property, rather than using the actual time from OpenSpace.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::













(TemporalTileProviderFolder-target)=
::::{dropdown} Table parameters for `Folder`



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

*   - `Folder`
    - The folder that is parsed for files. Every file in the provided directory is checked against the provided format and added if it adheres to said format
    - `Directory`
    
    - Value of type 'Directory' 
    
    - {bdg-info}`No`
    
*   - `Format`
    - The format of files that is pared in the provided folder. The format string has to be compatible to the C++ function get_time. https://en.cppreference.com/w/cpp/io/manip/get_time
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



::::






(TemporalTileProviderPrototyped-target)=
::::{dropdown} Table parameters for `Prototyped`



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

*   - `Prototype`
    - The text that will be used as the prototype to generate the data to load the image layer. Any occurance of `${OpenSpaceTimeId}` in this prototype is replaced with the current date according to the remaining information such as the resolution and the format and the resulting text is used to load the corresponding images
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `TemporalResolution`
    - The temporal resolution between each image
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Time`
    - The starting and ending times for the range of values
    - `Table`
    
    -   [Table parameters](#TemporalTileProviderPrototypedTime-target) 
    
    - {bdg-info}`No`
    
*   - `TimeFormat`
    - The specification of the date format that is used in the tile provider. The time format must be specified in a manner appropriate for the SPICE function `timout_c`. https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/timout_c.html
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



(TemporalTileProviderPrototypedTime-target)=
#### Table parameters for `Time`
The starting and ending times for the range of values


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `End`
    - The (inclusive) ending time of the temporal image range
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Start`
    - The (inclusive) starting time of the temporal image range
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::




::::






## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 16, 35
local globe = asset.require("scene/solarsystem/planets/earth/earth")



local path = asset.resource({
  Name = "Earth Textures Climate",
  Type = "HttpSynchronization",
  Identifier = "earth_textures_climate",
  Version = 1
})


local LayerPrototype = {
  Identifier = "ERA5_Land_HighRes_Monthly_2M_Temperature_Temporal_prototype",
  Name = "ERA5 Land HighRes Monthly 2M Temperature (Temporal) [Prototype]",
  Type = "TemporalTileProvider",
  Mode = "Prototyped",
  Prototyped = {
    Time = {
      Start = "1981-01-01",
      End = "1990-10-01"
    },
    TemporalResolution = "1M",
    TimeFormat = "YYYY-MM-DD",
    Prototype = path .. "${OpenSpaceTimeId}-land.png"
  },
  Interpolation = true,
  Colormap = path .. "rainbow.png",
  Description = "Temporal coverage: 01 Jan 1981 - 31 Dec 2020"
}

local LayerFolder = {
  Identifier = "ERA5_Land_HighRes_Monthly_2M_Temperature_Temporal_folder",
  Name = "ERA5 Land HighRes Monthly 2M Temperature (Temporal) [Folder]",
  Type = "TemporalTileProvider",
  Mode = "Folder",
  Folder = {
    Folder = path,
    Format = "%Y-%m-%d-land.png"
  },
  Interpolation = true,
  Colormap = path .. "rainbow.png",
  Description = "Temporal coverage: 01 Jan 1981 - 31 Dec 2020"
}


asset.onInitialize(function()
  openspace.globebrowsing.addLayer(globe.Earth.Identifier, "ColorLayers", LayerPrototype)
  openspace.globebrowsing.addLayer(globe.Earth.Identifier, "ColorLayers", LayerFolder)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteLayer(globe.Earth.Identifier, "ColorLayers", LayerFolder)
  openspace.globebrowsing.deleteLayer(globe.Earth.Identifier, "ColorLayers", LayerPrototype)
end)

asset.export("Prototype", LayerPrototype)
asset.export("Folder", LayerFolder)



asset.meta = {
  Name = "Climate Earth Layers",
  Description = "ERA5 data",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


