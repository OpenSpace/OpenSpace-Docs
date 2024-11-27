



(sync_synchronization_url)=
# UrlSynchronization

_Inherits [ResourceSynchronization](#ResourceSynchronization)_




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

*   - `Identifier`
    - This identifier will be part of the used folder structure and, can be used to manually find the downloaded folder in the synchronization folder
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - {bdg-info}`No`
    
*   - `Url`
    - The URL or urls from where the files are downloaded. If multiple URLs are provided, all files will be downloaded to the same directory and the filename parameter must not be specified simultaneously
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - {bdg-info}`No`
    
*   - `Filename`
    - Optional to provide filename to override the one which is otherwise automatically created from the url. If this value is specified, the url parameter only only contain exactly one URL
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Override`
    - Deprecated, use SecondsUntilResync instead
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `SecondsUntilResync`
    - This variable determines the validity period of a file(s) in seconds before it needs to be re-downloaded. The default value keeps the file permanently cached, while a value of 0 forces the file to be downloaded on every startup. If the symbolic value `math.huge` is used, a file is never redownloaded after the first time.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
*   - `UseHash`
    - If this value is set to 'true' (the default), the hash of the URL is appended to the directory name to produce a unique directory under all circumstances. If this is not desired, the URLSynchronization use the bare directory name alone if this value is 'false'. If this value is 'false', the identifier has to be specified
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 7
local earth = asset.require("scene/solarsystem/planets/earth/earth")



local data = asset.resource({
  Name = "GeoJSON Example Lines",
  Type = "UrlSynchronization",
  Identifier = "geojson_example_lines",
  Url = "http://liu-se.cdn.openspaceproject.com/files/examples/geojson/lines.geojson"
})


local ExampleLines = {
  Identifier = "Lines-Example",
  File = data .. "lines.geojson",
  HeightOffset = 20000.0,
  DefaultProperties = {
    LineWidth = 2.0
  },
  Name = "Example Lines"
}


asset.onInitialize(function()
  openspace.globebrowsing.addGeoJson(earth.Earth.Identifier, ExampleLines)
end)

asset.onDeinitialize(function()
  openspace.globebrowsing.deleteGeoJson(earth.Earth.Identifier, ExampleLines)
end)

asset.export(ExampleLines)



asset.meta = {
  Name = "GeoJson Example - Lines",
  Description = [[GeoJson example asset with lines]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


