# `openspace.globebrowsing`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addBlendingLayersFromDirectory`](#globebrowsingaddBlendingLayersFromDirectory-target)
    - [Retrieves all info files recursively in the directory passed as the first argument to this function]{#globebrowsingaddBlendingLayersFromDirectory-list}


*   - [`addFocusNodeFromLatLong`](#globebrowsingaddFocusNodeFromLatLong-target)
    - [Creates a new SceneGraphNode that can be used as focus node]{#globebrowsingaddFocusNodeFromLatLong-list}


*   - [`addFocusNodesFromDirectory`](#globebrowsingaddFocusNodesFromDirectory-target)
    - [Retrieves all info files recursively in the directory passed as the first argument to this function]{#globebrowsingaddFocusNodesFromDirectory-list}


*   - [`addGeoJson`](#globebrowsingaddGeoJson-target)
    - [Add a GeoJson layer specified by the given table to the specified globe]{#globebrowsingaddGeoJson-list}


*   - [`addGeoJsonFromFile`](#globebrowsingaddGeoJsonFromFile-target)
    - [Add a GeoJson layer from the given file name and add it to the current anchor node, if it is a globe]{#globebrowsingaddGeoJsonFromFile-list}


*   - [`addGibsLayer`](#globebrowsingaddGibsLayer-target)
    - [Adds a new layer from NASA GIBS to the Earth globe]{#globebrowsingaddGibsLayer-list}


*   - [`addLayer`](#globebrowsingaddLayer-target)
    - [Adds a layer to the specified globe]{#globebrowsingaddLayer-list}


*   - [`capabilitiesWMS`](#globebrowsingcapabilitiesWMS-target)
    - [Returns an array of tables that describe the available layers that are supported by the WMS server identified by the provided name]{#globebrowsingcapabilitiesWMS-list}


*   - [`createGibsGdalXml`](#globebrowsingcreateGibsGdalXml-target)
    - [Creates an XML configuration for a GIBS dataset]{#globebrowsingcreateGibsGdalXml-list}


*   - [`createTemporalGibsGdalXml`](#globebrowsingcreateTemporalGibsGdalXml-target)
    - [Creates an XML configuration for a temporal GIBS dataset to be used in
            a TemporalTileprovider]{#globebrowsingcreateTemporalGibsGdalXml-list}


*   - [`deleteGeoJson`](#globebrowsingdeleteGeoJson-target)
    - [Remove the GeoJson layer specified by the given table or string identifier from the specified globe]{#globebrowsingdeleteGeoJson-list}


*   - [`deleteLayer`](#globebrowsingdeleteLayer-target)
    - [Removes a layer from the specified globe]{#globebrowsingdeleteLayer-list}


*   - [`flyToGeo`](#globebrowsingflyToGeo-target)
    - [Fly the camera to a geographic coordinate (latitude, longitude and altitude) on a globe, using the path navigation system]{#globebrowsingflyToGeo-list}


*   - [`flyToGeo2`](#globebrowsingflyToGeo2-target)
    - [Fly the camera to a geographic coordinate (latitude and longitude) on a globe, using the path navigation system]{#globebrowsingflyToGeo2-list}


*   - [`geoPositionForCamera`](#globebrowsinggeoPositionForCamera-target)
    - [Get geographic coordinates of the camera position in latitude, longitude, and altitude (degrees and meters)]{#globebrowsinggeoPositionForCamera-list}


*   - [`getGeoPositionForCamera`](#globebrowsinggetGeoPositionForCamera-target)
    - [Get geographic coordinates of the camera position in latitude, longitude, and altitude (degrees and meters)]{#globebrowsinggetGeoPositionForCamera-list}


*   - [`getLayers`](#globebrowsinggetLayers-target)
    - [Returns the list of layers for the specified globe for a specific layer group]{#globebrowsinggetLayers-list}


*   - [`getLocalPositionFromGeo`](#globebrowsinggetLocalPositionFromGeo-target)
    - [Returns the position in the local Cartesian coordinate system of the specified globe that corresponds to the given geographic coordinates]{#globebrowsinggetLocalPositionFromGeo-list}


*   - [`goToChunk`](#globebrowsinggoToChunk-target)
    - [Go to the chunk on a globe with given index x, y, level]{#globebrowsinggoToChunk-list}


*   - [`goToGeo`](#globebrowsinggoToGeo-target)
    - [Immediately move the camera to a geographic coordinate on a globe]{#globebrowsinggoToGeo-list}


*   - [`jumpToGeo`](#globebrowsingjumpToGeo-target)
    - [Immediately move the camera to a geographic coordinate on a globe by first fading the rendering to black, jump to the specified coordinate, and then fade in]{#globebrowsingjumpToGeo-list}


*   - [`layers`](#globebrowsinglayers-target)
    - [Returns the list of layers for the specified globe, for a specific layer group]{#globebrowsinglayers-list}


*   - [`loadWMSCapabilities`](#globebrowsingloadWMSCapabilities-target)
    - [Loads and parses the WMS capabilities XML file from a remote server]{#globebrowsingloadWMSCapabilities-list}


*   - [`loadWMSServersFromFile`](#globebrowsingloadWMSServersFromFile-target)
    - [Loads all WMS servers from the provided file and passes them to the 'openspace]{#globebrowsingloadWMSServersFromFile-list}


*   - [`localPositionFromGeo`](#globebrowsinglocalPositionFromGeo-target)
    - [Returns the position in the local Cartesian coordinate system of the specified globe that corresponds to the given geographic coordinates]{#globebrowsinglocalPositionFromGeo-list}


*   - [`moveLayer`](#globebrowsingmoveLayer-target)
    - [Rearranges the order of a single layer on a globe]{#globebrowsingmoveLayer-list}


*   - [`parseInfoFile`](#globebrowsingparseInfoFile-target)
    - [Parses the passed info file and return the table with the information provided in the info file]{#globebrowsingparseInfoFile-list}


*   - [`removeWMSServer`](#globebrowsingremoveWMSServer-target)
    - [Removes the specified WMS server from the list of available servers]{#globebrowsingremoveWMSServer-list}


*   - [`setNodePosition`](#globebrowsingsetNodePosition-target)
    - [Sets the position of a SceneGraphNode that has GlobeTranslation/GlobeRotations]{#globebrowsingsetNodePosition-list}


*   - [`setNodePositionFromCamera`](#globebrowsingsetNodePositionFromCamera-target)
    - [Sets the position of a SceneGraphNode that has GlobeTranslation/GlobeRotations to match the camera]{#globebrowsingsetNodePositionFromCamera-list}

:::

## Functions

(globebrowsingaddBlendingLayersFromDirectory-target)=
### [`addBlendingLayersFromDirectory`](#globebrowsingaddBlendingLayersFromDirectory-list)
Retrieves all info files recursively in the directory passed as the first argument to this function. The color and height tables retrieved from these info files are then added to the RenderableGlobe identified by name passed to the second argument.Usage: openspace.globebrowsing.addBlendingLayersFromDirectory(directory, "Earth")


:::{card} Parameters


* directory `String` 



* nodeName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addBlendingLayersFromDirectory(directory, nodeName)
:::
___

(globebrowsingaddFocusNodeFromLatLong-target)=
### [`addFocusNodeFromLatLong`](#globebrowsingaddFocusNodeFromLatLong-list)
Creates a new SceneGraphNode that can be used as focus node. Usage: openspace.globebrowsing.addFocusNodeFromLatLong("Olympus Mons", "Mars", -18.65, 226.2, optionalAltitude)


:::{card} Parameters


* name `String` 



* globeIdentifier `String` 



* latitude `Number` 



* longitude `Number` 



* altitude `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addFocusNodeFromLatLong(name, globeIdentifier, latitude, longitude, altitude)
:::
___

(globebrowsingaddFocusNodesFromDirectory-target)=
### [`addFocusNodesFromDirectory`](#globebrowsingaddFocusNodesFromDirectory-list)
Retrieves all info files recursively in the directory passed as the first argument to this function. The name and location retrieved from these info files are then used to create new SceneGraphNodes that can be used as focus nodes. Usage: openspace.globebrowsing.addFocusNodesFromDirectory(directory, "Mars")


:::{card} Parameters


* directory `String` 



* nodeName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addFocusNodesFromDirectory(directory, nodeName)
:::
___

(globebrowsingaddGeoJson-target)=
### [`addGeoJson`](#globebrowsingaddGeoJson-list)
Add a GeoJson layer specified by the given table to the specified globe.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* table `Table` 


    * A table with information about the GeoJson layer. See [this page](#globebrowsing_geojsoncomponent) for details on what fields and settings the table may contain
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addGeoJson(globeIdentifier, table)
:::
___

(globebrowsingaddGeoJsonFromFile-target)=
### [`addGeoJsonFromFile`](#globebrowsingaddGeoJsonFromFile-list)
Add a GeoJson layer from the given file name and add it to the current anchor node, if it is a globe. Note that you might have to increase the height offset for the added feature to be visible on the globe, if using a height map.


:::{card} Parameters


* filename `String` 


    * The path to the GeoJSON file 

* name `String?` 


    * An optional name that the loaded feature will get in the user interface
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addGeoJsonFromFile(filename, name)
:::
___

(globebrowsingaddGibsLayer-target)=
### [`addGibsLayer`](#globebrowsingaddGibsLayer-list)
Adds a new layer from NASA GIBS to the Earth globe. Arguments are: imagery layer name, imagery resolution, start date, end date, format. For all specifications, see https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+ProductsUsage:openspace.globebrowsing.addGibsLayer('AIRS_Temperature_850hPa_Night', '2km', '2013-07-15', 'Present', 'png')


:::{card} Parameters


* layer `String` 



* resolution `String` 



* format `String` 



* startDate `String` 



* endDate `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addGibsLayer(layer, resolution, format, startDate, endDate)
:::
___

(globebrowsingaddLayer-target)=
### [`addLayer`](#globebrowsingaddLayer-list)
Adds a layer to the specified globe. The second argument is the layer group which can be any of the supported layer groups. The third argument is the dictionary defining the layer.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node of which to add the layer. The renderable of the scene graph node must be a [RenderableGlobe](#globebrowsing_renderableglobe) 

* layerGroup `String` 


    * The identifier of the layer group in which to add the layer 

* layer `Table` 


    * A dictionary defining the layer. See [this page](#globebrowsing_layer) for details on what fields and settings the dictionary may contain
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.addLayer(globeIdentifier, layerGroup, layer)
:::
___

(globebrowsingcapabilitiesWMS-target)=
### [`capabilitiesWMS`](#globebrowsingcapabilitiesWMS-list)
Returns an array of tables that describe the available layers that are supported by the WMS server identified by the provided name. The `URL` component of the returned table can be used in the `FilePath` argument for a call to the `addLayer` function to add the value to a globe.


:::{card} Parameters


* name `String` 


    * The name of the WMS server for which to get the information
:::

Return type: `Table[]` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.capabilitiesWMS(name)
:::
___

(globebrowsingcreateGibsGdalXml-target)=
### [`createGibsGdalXml`](#globebrowsingcreateGibsGdalXml-list)
Creates an XML configuration for a GIBS dataset.Arguments are: layerName, date, resolution, format.For all specifications, see https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+ProductsUsage:openspace.globebrowsing.addLayer("Earth","ColorLayers",{Name = "MODIS_Terra_Chlorophyll_A",FilePath = openspace.globebrowsing.createGibsGdalXml("MODIS_Terra_Chlorophyll_A","2013-07-02","1km","png")})


:::{card} Parameters


* layerName `String` 



* date `String` 



* resolution `String` 



* format `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.createGibsGdalXml(layerName, date, resolution, format)
:::
___

(globebrowsingcreateTemporalGibsGdalXml-target)=
### [`createTemporalGibsGdalXml`](#globebrowsingcreateTemporalGibsGdalXml-list)
Creates an XML configuration for a temporal GIBS dataset to be used in
            a TemporalTileprovider


:::{card} Parameters


* layerName `String` 



* resolution `String` 



* format `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.createTemporalGibsGdalXml(layerName, resolution, format)
:::
___

(globebrowsingdeleteGeoJson-target)=
### [`deleteGeoJson`](#globebrowsingdeleteGeoJson-list)
Remove the GeoJson layer specified by the given table or string identifier from the specified globe.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* tableOrIdentifier `String | Table` 


    * Either an identifier for the GeoJson layer to be removed, or a table that includes the identifier
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.deleteGeoJson(globeIdentifier, tableOrIdentifier)
:::
___

(globebrowsingdeleteLayer-target)=
### [`deleteLayer`](#globebrowsingdeleteLayer-list)
Removes a layer from the specified globe.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node of which to remove the layer. The renderable of the scene graph node must be a [RenderableGlobe](#globebrowsing_renderableglobe) 

* layerGroup `String` 


    * The identifier of the layer group from which to remove the layer 

* layerOrName `String | Table` 


    * Either the identifier for the layer or a dictionary with the `Identifier` key that is used instead
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.deleteLayer(globeIdentifier, layerGroup, layerOrName)
:::
___

(globebrowsingflyToGeo-target)=
### [`flyToGeo`](#globebrowsingflyToGeo-list)
Fly the camera to a geographic coordinate (latitude, longitude and altitude) on a globe, using the path navigation system.


:::{card} Parameters


* globe `String` 


    * The identifier of a scene graph node that has a RenderableGlobe attached. If an empty string is provided, the current anchor node is used 

* latitude `Number` 


    * The latitude of the target coordinate, in degrees 

* longitude `Number` 


    * The longitude of the target coordinate, in degrees 

* altitude `Number` 


    * The altitude of the target coordinate, in meters 

* duration `Number?` 


    * An optional duration for the motion to take, in seconds. For example, a value of 5 means \"fly to this position over a duration of 5 seconds\" 

* shouldUseUpVector `Boolean?` 


    * If true, try to use the up-direction when computing the target position for the camera. For globes, this means that North should be up, in relation to the camera's view direction. Note that for this to take effect, rolling motions must be enabled in the Path Navigator settings.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.flyToGeo(globe, latitude, longitude, altitude, duration, shouldUseUpVector)
:::
___

(globebrowsingflyToGeo2-target)=
### [`flyToGeo2`](#globebrowsingflyToGeo2-list)
Fly the camera to a geographic coordinate (latitude and longitude) on a globe, using the path navigation system.

The distance to fly to can either be set to be the current distance of the camera to the target object, or the default distance from the path navigation system.


:::{card} Parameters


* globe `String` 


    * The identifier of a scene graph node that has a RenderableGlobe attached. If an empty string is provided, the current anchor node is used 

* latitude `Number` 


    * The latitude of the target coordinate, in degrees 

* longitude `Number` 


    * The longitude of the target coordinate, in degrees 

* useCurrentDistance `Boolean?` 


    * If true, use the current distance of the camera to the target globe when going to the specified position. If false, or not specified, set the distance based on the bounding sphere and the distance factor setting in Path Navigator 

* duration `Number?` 


    * An optional duration for the motion to take, in seconds. For example, a value of 5 means \"fly to this position over a duration of 5 seconds\" 

* shouldUseUpVector `Boolean?` 


    * If true, try to use the up-direction when computing the target position for the camera. For globes, this means that North should be up, in relation to the camera's view direction. Note that for this to take effect, rolling motions must be enabled in the Path Navigator settings.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.flyToGeo2(globe, latitude, longitude, useCurrentDistance, duration, shouldUseUpVector)
:::
___

(globebrowsinggeoPositionForCamera-target)=
### [`geoPositionForCamera`](#globebrowsinggeoPositionForCamera-list)
Get geographic coordinates of the camera position in latitude, longitude, and altitude (degrees and meters).


:::{card} Parameters


* useEyePosition `Boolean?` - Default value: `false` 


    * If true, use the view direction of the camera instead of the camera position
:::

Return type: `(Number, Number, Number)` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.geoPositionForCamera(useEyePosition)
:::
___

(globebrowsinggetGeoPositionForCamera-target)=
### [`getGeoPositionForCamera`](#globebrowsinggetGeoPositionForCamera-list)
Get geographic coordinates of the camera position in latitude, longitude, and altitude (degrees and meters).

Deprecated in favor of `geoPositionForCamera`.


:::{card} Parameters


* useEyePosition `Boolean?` - Default value: `false` 


    * If true, use the view direction of the camera instead of the camera position
:::

Return type: `(Number, Number, Number)` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.getGeoPositionForCamera(useEyePosition)
:::
___

(globebrowsinggetLayers-target)=
### [`getLayers`](#globebrowsinggetLayers-list)
Returns the list of layers for the specified globe for a specific layer group.

Deprecated in favor of `layers`.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* layerGroup `String` 


    * The identifier of the layer group for which to list the layers
:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.getLayers(globeIdentifier, layerGroup)
:::
___

(globebrowsinggetLocalPositionFromGeo-target)=
### [`getLocalPositionFromGeo`](#globebrowsinggetLocalPositionFromGeo-list)
Returns the position in the local Cartesian coordinate system of the specified globe that corresponds to the given geographic coordinates. In the local coordinate system, the position (0,0,0) corresponds to the globe's center.

Deprecated in favor of `localPositionFromGeo`.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* latitude `Number` 


    * The latitude of the geograpic position, in degrees 

* longitude `Number` 


    * The longitude of the geographic position, in degrees 

* altitude `Number` 


    * The altitude, in meters
:::

Return type: `(Number, Number, Number)` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.getLocalPositionFromGeo(globeIdentifier, latitude, longitude, altitude)
:::
___

(globebrowsinggoToChunk-target)=
### [`goToChunk`](#globebrowsinggoToChunk-list)
Go to the chunk on a globe with given index x, y, level.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* x `Integer` 


    * The x value of the tile index 

* y `Integer` 


    * The y value of the tile index 

* level `Integer` 


    * The level of the tile index
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.goToChunk(globeIdentifier, x, y, level)
:::
___

(globebrowsinggoToGeo-target)=
### [`goToGeo`](#globebrowsinggoToGeo-list)
Immediately move the camera to a geographic coordinate on a globe.


:::{card} Parameters


* globe `String` 


    * The identifier of a scene graph node that has a RenderableGlobe attached. If an empty string is provided, the current anchor node is used 

* latitude `Number` 


    * The latitude of the target coordinate, in degrees 

* longitude `Number` 


    * The longitude of the target coordinate, in degrees 

* altitude `Number?` 


    * An optional altitude, given in meters over the reference surface of the globe. If no altitude is provided, the altitude will be kept as the current distance to the reference surface of the specified globe.
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.goToGeo(globe, latitude, longitude, altitude)
:::
___

(globebrowsingjumpToGeo-target)=
### [`jumpToGeo`](#globebrowsingjumpToGeo-list)
Immediately move the camera to a geographic coordinate on a globe by first fading the rendering to black, jump to the specified coordinate, and then fade in.

This is done by triggering another script that handles the logic.


:::{card} Parameters


* globe `String` 


    * The identifier of a scene graph node that has a RenderableGlobe attached. If an empty string is provided, the current anchor node is used 

* latitude `Number` 


    * The latitude of the target coordinate, in degrees 

* longitude `Number` 


    * The longitude of the target coordinate, in degrees 

* altitude `Number?` 


    * An optional altitude, given in meters over the reference surface of the globe. If no altitude is provided, the altitude will be kept as the current distance to the reference surface of the specified globe. 

* fadeDuration `Number?` 


    * An optional duration for the fading. If not included, the property in Navigation Handler will be used
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.jumpToGeo(globe, latitude, longitude, altitude, fadeDuration)
:::
___

(globebrowsinglayers-target)=
### [`layers`](#globebrowsinglayers-list)
Returns the list of layers for the specified globe, for a specific layer group.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* layerGroup `String` 


    * The identifier of the layer group for which to list the layers
:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.layers(globeIdentifier, layerGroup)
:::
___

(globebrowsingloadWMSCapabilities-target)=
### [`loadWMSCapabilities`](#globebrowsingloadWMSCapabilities-list)
Loads and parses the WMS capabilities XML file from a remote server.


:::{card} Parameters


* name `String` 


    * The name of the capabilities that can be used to later refer to the set of capabilities 

* globe `String` 


    * The identifier of the globe for which this server is applicable 

* url `String` 


    * The URL at which the capabilities file can be found
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.loadWMSCapabilities(name, globe, url)
:::
___

(globebrowsingloadWMSServersFromFile-target)=
### [`loadWMSServersFromFile`](#globebrowsingloadWMSServersFromFile-list)
Loads all WMS servers from the provided file and passes them to the 'openspace.globebrowsing.loadWMSCapabilities' file.


:::{card} Parameters


* filePath `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.loadWMSServersFromFile(filePath)
:::
___

(globebrowsinglocalPositionFromGeo-target)=
### [`localPositionFromGeo`](#globebrowsinglocalPositionFromGeo-list)
Returns the position in the local Cartesian coordinate system of the specified globe that corresponds to the given geographic coordinates. In the local coordinate system, the position (0,0,0) corresponds to the globe's center.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the scene graph node for the globe 

* latitude `Number` 


    * The latitude of the geograpic position, in degrees 

* longitude `Number` 


    * The longitude of the geographic position, in degrees 

* altitude `Number` 


    * The altitude, in meters
:::

Return type: `(Number, Number, Number)` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.localPositionFromGeo(globeIdentifier, latitude, longitude, altitude)
:::
___

(globebrowsingmoveLayer-target)=
### [`moveLayer`](#globebrowsingmoveLayer-list)
Rearranges the order of a single layer on a globe. The first position in the list has index 0, and the last position is given by the number of layers minus one.

The `source` and `destination` parameters can also be the identifiers of the layers to be moved. If `destination` is a name, the source layer is moved below that destination layer.


:::{card} Parameters


* globeIdentifier `String` 


    * The identifier of the globe 

* layerGroup `String` 


    * The identifier of the layer group 

* source `Integer | String` 


    * The original position of the layer that should be moved, either as an index in the list or the identifier of the layer to be moved 

* destination `Integer | String` 


    * The new position in the list, either as an index in the list or as the identifier of the layer after which to place the moved layer
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.moveLayer(globeIdentifier, layerGroup, source, destination)
:::
___

(globebrowsingparseInfoFile-target)=
### [`parseInfoFile`](#globebrowsingparseInfoFile-list)
Parses the passed info file and return the table with the information provided in the info file. The return table contains the optional keys: 'Color', 'Height', 'Node', 'Location', 'Identifier'.Usage: local t = openspace.globebrowsing.parseInfoFile(file)openspace.globebrowsing.addLayer("Earth", "ColorLayers", t.color)openspace.globebrowsing.addLayer("Earth", "HeightLayers", t.height)


:::{card} Parameters


* file `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.parseInfoFile(file)
:::
___

(globebrowsingremoveWMSServer-target)=
### [`removeWMSServer`](#globebrowsingremoveWMSServer-list)
Removes the specified WMS server from the list of available servers. The name parameter corresponds to the first argument in the `loadWMSCapabilities` call that was used to load the WMS server.


:::{card} Parameters


* name `String` 


    * The name of the WMS server to remove
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.removeWMSServer(name)
:::
___

(globebrowsingsetNodePosition-target)=
### [`setNodePosition`](#globebrowsingsetNodePosition-list)
Sets the position of a SceneGraphNode that has GlobeTranslation/GlobeRotations. Usage: openspace.globebrowsing.setNodePosition("Scale_StatueOfLiberty", "Earth", 40.000, -117.5, optionalAltitude)


:::{card} Parameters


* nodeIdentifer `String` 



* globeIdentifier `String` 



* latitude `Number` 



* longitude `Number` 



* altitude `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.setNodePosition(nodeIdentifer, globeIdentifier, latitude, longitude, altitude)
:::
___

(globebrowsingsetNodePositionFromCamera-target)=
### [`setNodePositionFromCamera`](#globebrowsingsetNodePositionFromCamera-list)
Sets the position of a SceneGraphNode that has GlobeTranslation/GlobeRotations to match the camera. Only uses camera position not rotation. If useAltitude is true, then the position will also be updated to the camera's altitude.Usage: openspace.globebrowsing.setNodePositionFromCamera("Scale_StatueOfLiberty", optionalUseAltitude)


:::{card} Parameters


* nodeIdentifer `String` 



* useAltitude `Boolean` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.globebrowsing.setNodePositionFromCamera(nodeIdentifer, useAltitude)
:::

