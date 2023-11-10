# Readable Datasets
OpenSpace uses GDAL as the main tool for loading dynamic map datasets for globe rendering. However, OpenSpace can also be compiled without GDAL, in which case the readable image files will be limited to simple local files such as JPEG and PNG.

As described in [Creating a Renderable Globe](creating-a-renderableglobe), a layer is defined by a Lua table. What we want is a dataset definition to be used for the **FilePath** of the Lua table and there are many alternatives.

## Web Map Services
The main source of map datasets we can use within OpenSpace is provided through web map services which let the user download parts of the datasets from remote servers. There are different variations of web map services used by different providers. The main types are:

  - **WMS** -- Very general and lets the user download any part of a map, heavy for the server
  - **TMS** -- Tiled service, faster than WMS
  - **TiledWMS** -- Tiled service (different interface), faster than WMS
  - **VirtualEarth**

GDAL wms configurations are described on this page: [http://www.gdal.org/frmt_wms.html](http://www.gdal.org/frmt_wms.html). **FilePath** can either be set to a file or to the complete GDAL wms config itself in string format.

### NASA GIBS WMS Datasets
NASA GIBS provides several datasets accessible through a web map service interface which OpenSpace can read using GDAL. Information about the XML configs for reading these datasets using GDAL can be found on this site: https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers.
 Depending on resolution, number of channels, image formats etc, different settings need to be set in the GDAL WMS config files to read. Information and available datasets can be found on this site:
https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+Products.

As described in [Creating a Renderable Globe](creating-a-renderableglobe), scripting can be used to create definitions for these datasets.

## Local Files
GDAL also allows for reading a vast number of image files including geo-referenced map datasets such as GeoTIFF, CUBE, VRT and others. When it comes to geo-referenced formats, the current requirements OpenSpace has on these datasets are that the geo-referenced coordinates are given in longlat space (degrees), as opposed to meters or kilometers, and that the dataset has global coverage of the globe, i.e. covers the longlat space longitude \[-180,180\] and latitude \[-90,90\].

## Temporal Datasets
A temporal dataset is an extension of GDAL's WMS dataset definition used by OpenSpace. The layer type needs to be **TemporalTileLayer** to load these datasets. Currently, this is only supported if OpenSpace was compiled with GDAL. The dataset features are defined in an XML file just as the WMS files that GDAL reads. An example of an OpenSpaceTemporalGDALDataset is defined below:

Important tags are:
- `<OpenSpaceTemporalGDALDataset>` - Encloses the dataset XML definition
- `<OpenSpaceTimeStart>` - Time in UTC when the first image is to be used (clamps the time)
- `<OpenSpaceTimeEnd>` - Time in UTC when the last image is to be used (clamps the time)
- `<OpenSpaceTimeResolution>` - Temporal resolution of the dataset. E.g. One image per day would be "1d"
- `<OpenSpaceTimeIdFormat>` - Format of the time placeholder `${OpenSpaceTimeId}` to be pasted in the URL
- `<GDAL_WMS>` - The GDAL WMS is defined here

The placeholder `${OpenSpaceTimeId}` is replaced with the current Openspace time quantized according to the value provided for `<OpenSpaceTimeResolution>`. Then a new dataset will be loaded and texture images will be updated on the fly.

```xml
<OpenSpaceTemporalGDALDataset>
    <OpenSpaceTimeStart>2015-11-24</OpenSpaceTimeStart>
    <OpenSpaceTimeEnd></OpenSpaceTimeEnd>
    <OpenSpaceTimeResolution>1d</OpenSpaceTimeResolution>
    <OpenSpaceTimeIdFormat>YYYY-MM-DD</OpenSpaceTimeIdFormat>
    <GDAL_WMS>
        <Service name="TMS">
            <ServerUrl>http://map1.vis.earthdata.nasa.gov/wmts-geo/VIIRS_SNPP_CorrectedReflectance_TrueColor/default/${OpenSpaceTimeId}/EPSG4326_250m/${z}/${y}/${x}.jpg</ServerUrl>
        </Service>
        <DataWindow>
            <UpperLeftX>-180.0</UpperLeftX>
            <UpperLeftY>90</UpperLeftY>
            <LowerRightX>396.0</LowerRightX>
            <LowerRightY>-198</LowerRightY>
            <TileLevel>8</TileLevel>
            <TileCountX>2</TileCountX>
            <TileCountY>1</TileCountY>
            <YOrigin>top</YOrigin>
        </DataWindow>
        <Projection>EPSG:4326</Projection>
        <BlockSizeX>512</BlockSizeX>
        <BlockSizeY>512</BlockSizeY>
        <BandsCount>3</BandsCount>
    </GDAL_WMS>
</OpenSpaceTemporalGDALDataset>
```
This specific dataset is from NASA GIBS and has daily global coverage from 2015-11-24.

Temporal datasets can also be used with local files. Here is a simple example:
```xml
<OpenSpaceTemporalGDALDataset>
    <OpenSpaceTimeStart>2015-11-24</OpenSpaceTimeStart>
    <OpenSpaceTimeEnd></OpenSpaceTimeEnd>
    <OpenSpaceTimeResolution>1d</OpenSpaceTimeResolution>
    <OpenSpaceTimeIdFormat>YYYY-MM-DD</OpenSpaceTimeIdFormat>
    <FilePath>"path/to/file${OpenSpaceTimeId}.jpg"</FilePath>
</OpenSpaceTemporalGDALDataset>
```
where `path/to` is a folder containing files such as `file2015-11-24.jpg` where the date is interchangeable.

## Local Patches
See [Build Local DEM Patches to Load With OpenSpace](build-local-dem-patches)
