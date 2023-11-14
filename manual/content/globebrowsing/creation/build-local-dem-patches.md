# Build Local DEM Patches to Load With OpenSpace
## Requirements
  - GDAL version 1.7 or later (libcurl and proj4 linked)
  - Kadkadu software (if a jpeg2000 library is not linked with GDAL, details below)
  - Fix_jp2 (applies to some HiRISE datasets, details below)
  - OpenSpace prerelease/ips-2016 or later


## Introduction
Please begin by reading [Working With Layers](../working-with-layers), [Creating a Renderable Globe](creating-a-renderableglobe), and [Readable Datasets](readable-datasets) to get a hold of how to configure globe rendering in OpenSpace.

The current requirements OpenSpace has on the datasets that can be loaded are that the geo-referenced coordinates are given in equirectangular longlat space (degrees), as opposed to meters or kilometers, and that the dataset has global coverage of the globe, ie covers the longlat space longitude \[-180,180\] and latitude \[-90,90\]. There is a solution to loading local patches that we will get in to soon. GDAL is also able to load JPEG2000 (by linking one of the suggested JPEG2000 libraries when building GDAL) but that functionality is not currently handled within OpenSpace, hence we unfortunately have to convert JPEG2000 files to geotiffs before loading them. This will lead to an increase in the file size of local patches.


## Installing GDAL
GDAL can either be built from source or installed with binaries. To download the software, go to http://www.gdal.org/ and follow the instructions for installing. Important to notice is that to be able to use GDAL with the features needed in the following tutorial for local patches, GDAL needs to be linked with curl (for WMS reading) and with proj4 (for reprojection).


## Local Patches
OpenSpace is not currently able to read local datasets which is why there is some preprocessing needed for these types of local patches. The essential idea is to define a so called virtual dataset which lets GDAL trick OpenSpace to think that a local patch dataset is actually a global dataset. There are some downsides to doing this. The main thing is that OpenSpace will not only load map data at places covered by the local patch. It will also load empty tiles into memory where there are no data. Due to another current restriction in OpenSpace which basically says that the georeferenced coordinates of a dataset needs to be in equidistant lat-long space there is often some more preprocessing needed to be able to load local datasets into OpenSpace.

Below follows a tutorial on which preprocessing steps are needed to be able to read local map datasets in OpenSpace.

### Getting The Patches
We are going to use a HiRISE DTM (Digital Terrain Model) patch as an example. These patches are generated from a stereo process using images from the HiRISE on NASA's Mars Reconnaissance Orbiter (http://mars.nasa.gov/mro/mission/instruments/hirise/). All the latest added DTMs can be found on this site: http://www.uahirise.org/dtm/.

If a DTM is created using NASAs stereo pipeline it should be exported as two datasets (one texture and one height map) in geotiff format. The georeferenced coordinates should if possible be set to longlat. If not possible, we will have to use GDAL to do the reprojection.

Let's now focus on a specific HiRISE DTM patch and all the steps needed to get it to work within OpenSpace. The patch we are focusing on covers a small part of the South-West Candor Chasma and can be found on this link: http://www.uahirise.org/dtm/dtm.php?ID=PSP_001918_1735.
Information about the HiRISE DTMs and what the file names mean can be found here: http://www.uahirise.org/dtm/about.php.

First, we download the **heightmap DTEEC_001918_1735_001984_1735_U01.IMG** together with one of the corresponding texture maps, for example **PSP_001918_1735_RED_A_01_ORTHO.JP2**. These are provided under "DTM & ORTHOIMAGES" and have a resolution of 0.25 cm per pixel. Both the left observation and the right observation of the stereo pair are provided, both with high (0.25 cm) resolution and low(er) (1 m) resolution. The file size of the 1 m resolution image will of course be smaller.

### Fix Incorrect Metadata (applies only to HiRISE DTMs)
Unfortunately, many of the HiRISE DTMs downloaded from the site provided above have some errors in their metadata which essentially defines the longlat position and size of the patch on a globe. To see this problem, run the command `gdalinfo` on both the height map (IMG) and the texture (JP2). When looking at the output we can see that there is a slight miss match in the corner coordinates of each patch. If there is no miss match, this step is unnecessary.

```
    gdalinfo DTEEC_001918_1735_001984_1735_U01.IMG
    ...
    Corner Coordinates:
    Upper Left  (   -3094.483, -378027.655) ( 76d58'56.67"W,  6d22'40.21"S)
    Lower Left  (   -3094.483, -388919.547) ( 76d58'56.67"W,  6d33'41.75"S)
    Upper Right (    3347.383, -378027.655) ( 76d52'23.91"W,  6d22'40.21"S)
    Lower Right (    3347.383, -388919.547) ( 76d52'23.91"W,  6d33'41.75"S)
    Center      (     126.450, -383473.601) ( 76d55'40.29"W,  6d28'10.98"S)
    ...
```

and

```
    gdalinfo PSP_001918_1735_RED_A_01_ORTHO.JP2
    ...
    Corner Coordinates:
    Upper Left  (   -3093.092, -378029.046) ( 76d58'55.86"W, 11d22'39.28"S)
    Lower Left  (   -3093.092, -388920.432) ( 76d58'55.86"W, 11d33'40.76"S)
    Upper Right (    3348.774, -378029.046) ( 76d52'24.61"W, 11d22'39.28"S)
    Lower Right (    3348.774, -388920.432) ( 76d52'24.61"W, 11d33'40.76"S)
    Center      (     127.841, -383474.739) ( 76d55'40.24"W, 11d28'10.02"S)
    ...
```

This is a known issue, however, not properly addressed on the HiRISE website. Information about the problem and a solution can be found here: https://isis.astrogeology.usgs.gov/IsisSupport/index.php?topic=3440.0,
And here: https://trac.osgeo.org/gdal/ticket/2706.
The problem basically has to do with an incorrect radius set as part of the metadata in the JP2 (JPEG2000) files. We need to download the small program "fix_jp2", either an executable (ftp://pdsimage2.wr.usgs.gov/pub/pigpen/c_FORTRAN_code/) or the C++ code to compile it yourself (see the link to the trac ticket above), and run it with the JP2 file of interest as argument:

```
    fix_jp2 PSP_001918_1735_RED_A_01_ORTHO.JP2
    Success, file updated
```

Now when running gdalinfo on the JP2 file again we get better results:

```
    gdalinfo PSP_001918_1735_RED_A_01_ORTHO.JP2
    ...
    Corner Coordinates:
    Upper Left  (   -3093.092, -378029.046) ( 76d58'56.57"W,  6d22'39.28"S)
    Lower Left  (   -3093.092, -388920.432) ( 76d58'56.57"W,  6d33'40.76"S)
    Upper Right (    3348.774, -378029.046) ( 76d52'23.84"W,  6d22'39.28"S)
    Lower Right (    3348.774, -388920.432) ( 76d52'23.84"W,  6d33'40.76"S)
    Center      (     127.841, -383474.739) ( 76d55'40.21"W,  6d28'10.02"S)
    ...
```

There is still some difference between the height map and the texture. This is mainly because a height map and a corresponding texture don't necessarily have the same pixel size and position.

### File Format Conversion
When looking at the corner coordinates of the patch output when running gdalinfo on it,

```
    gdalinfo PSP_001918_1735_RED_A_01_ORTHO.TIFF
```

we notice that each corner (for example the upper left corner) has two coordinates defined in two spaces. The first one is the georeferenced space and the second one is in longlat space. The georeferenced space can be given in many different units including meters, kilometers and degrees. The HiRISE patches have the georeferenced coordinates given in meters and this is not what we want since OpenSpace does conversion between pixel space and longlat space assuming the georeferenced coordinates are given in longlat space (which is the case for almost all global WMS datasets).

We run the command gdalwarp to do a reprojection from the georeferenced space in meters to a georeferenced space in longlat. The program takes the arguments **-t_srs** where a target projection should be specified (we specify it using a so called proj4 string which tells GDAL to set the target georeferenced space to longlat). Run the program on both the height map **DTEEC_001918_1735_001984_1735_U01.IMG** and the texture **PSP_001918_1735_RED_A_01_ORTHO.TIFF**:

```
    gdalwarp -t_srs "+proj=longlat" DTEEC_001918_1735_001984_1735_U01.IMG DTEEC_001918_1735_001984_1735_U01_longlat.TIFF
    gdalwarp -t_srs "+proj=longlat" PSP_001918_1735_RED_A_01_ORTHO.TIFF PSP_001918_1735_RED_A_01_ORTHO_lonlat.TIFF
```

Now we get two new files with georeferenced coordinates given in longlat space. We can check this by running gdalinfo on both of the new files:

```
    gdalinfo.exe DTEEC_001918_1735_001984_1735_U01_longlat.TIFF
    ...
    Corner Coordinates:
    Upper Left  ( -76.9824075,  -6.3778369) ( 76d58'56.67"W,  6d22'40.21"S)
    Lower Left  ( -76.9824075,  -6.5615920) ( 76d58'56.67"W,  6d33'41.73"S)
    Upper Right ( -76.8733093,  -6.3778369) ( 76d52'23.91"W,  6d22'40.21"S)
    Lower Right ( -76.8733093,  -6.5615920) ( 76d52'23.91"W,  6d33'41.73"S)
    Center      ( -76.9278584,  -6.4697145) ( 76d55'40.29"W,  6d28'10.97"S)
    ...
```

and

```
    gdalinfo PSP_001918_1735_RED_A_01_ORTHO_longlat.TIFF
    ...
    Corner Coordinates:
    Upper Left  ( -76.9823817,  -6.3775787) ( 76d58'56.57"W,  6d22'39.28"S)
    Lower Left  ( -76.9823817,  -6.5613214) ( 76d58'56.57"W,  6d33'40.76"S)
    Upper Right ( -76.8732883,  -6.3775787) ( 76d52'23.84"W,  6d22'39.28"S)
    Lower Right ( -76.8732883,  -6.5613214) ( 76d52'23.84"W,  6d33'40.76"S)
    Center      ( -76.9278350,  -6.4694501) ( 76d55'40.21"W,  6d28'10.02"S)
    ...
```

By looking at the corner coordinates we can now see that the georeferenced coordinates (left) match up with the longlat coordinates (right).

### Creating Virtual Global Datasets
As mentioned earlier the datasets need to be global (longitude \[-180,180\] and latitude \[-90,90\]) for OpenSpace to read them correctly. Since the datasets we currently have only covers a small patch of the global longlat space we need to expand the coverage with empty pixels so that the whole globe is covered. This is done by using GDALs virtual datasets.

#### Building Virtual Datasets
We can build a VRT (virtual dataset) by running the command gdalbuildvrt on the two latest files we have obtained. We need some specific arguments to get the results we want, using **-te** we can specify the georeferenced extent of the VRT file. **-addalpha** adds an alpha channel to the output VRT where there are no data. This is necessary for the texture dataset since we don't want the patch to hide underlying textures where there is no data. **-r** sets the resampling algorithm to use when reading the dataset. The default value is *nearest* which can cause significant *stair stepping* artifacts when used with height data, it can therefore be benefitial to change it to *bilinear* or any of the other algorithms listed [here](https://gdal.org/programs/gdalbuildvrt.html#cmdoption-gdalbuildvrt-r).

```
    gdalbuildvrt Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_Heightmap.vrt -te -180 -90 180 90 DTEEC_001918_1735_001984_1735_U01_longlat.TIFF

    gdalbuildvrt Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_Texture.vrt -te -180 -90 180 90 -addalpha PSP_001918_1735_RED_A_01_ORTHO_longlat.TIFF
```

Now if we again run the command `gdalinfo` on our new VRT datasets we can see that they cover the whole longlat space (with some negligible precision errors):

```
    gdalinfo Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_Heightmap.vrt
    ...
    Corner Coordinates:
    Upper Left  (-180.0000000,  90.0000000) (180d 0' 0.00"W, 90d 0' 0.00"N)
    Lower Left  (-180.0000000, -90.0000012) (180d 0' 0.00"W, 90d 0' 0.00"S)
    Upper Right ( 180.0000024,  90.0000000) (180d 0' 0.01"E, 90d 0' 0.00"N)
    Lower Right ( 180.0000024, -90.0000012) (180d 0' 0.01"E, 90d 0' 0.00"S)
    Center      (   0.0000012,  -0.0000006) (  0d 0' 0.00"E,  0d 0' 0.00"S)
    ...
```

and

```
    gdalinfo.exe Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_texture.vrt
    ...
    Corner Coordinates:
    Upper Left  (-180.0000000,  90.0000000) (180d 0' 0.00"W, 90d 0' 0.00"N)
    Lower Left  (-180.0000000, -89.9999985) (180d 0' 0.00"W, 89d59'59.99"S)
    Upper Right ( 180.0000013,  90.0000000) (180d 0' 0.00"E, 90d 0' 0.00"N)
    Lower Right ( 180.0000013, -89.9999985) (180d 0' 0.00"E, 89d59'59.99"S)
    Center      (   0.0000007,   0.0000007) (  0d 0' 0.00"E,  0d 0' 0.00"N)
    ...
```

### Changing Configurations for Alpha Channel
The **-addalpha** argument we used for the texture only made sure that alpha is set to 0 where there are no data. The patch however is often slightly tilted and also not necessarily rectangular so there might be some parts of the image file that have data even though it is not used in the patch, see image below:

![](https://raw.githubusercontent.com/OpenSpace/OpenSpace-Wiki/master/images/globebrowsing/patch1.png?token=AD7-OPJHYH2zHrt7B1gRxFaYIE9_gQybks5Y0OgQwA%3D%3D)

To get rid of the black border we need to fiddle with some constants defined in the `vrt` file for the texture dataset. The tag **<ScaleRatio>** defines a value that is used as a scale factor when creating an alpha channel from the grayscale raster. We want the alpha to be either 0 or 255. If we set the **ScaleRatio** to 255 we will make sure that every pixel that has a value of 1 will get an alpha value of 255. Every pixel with a higher value will get an even higher alpha value but since the data type used in the dataset is byte these values will just get clamped down to 255. We just remove the **<ScaleOffset>** tag since we still want the pixel values of 0 to generate alpha values of 0. Also, no data values need to be set to get correct transparency. We need both a no data value for the source and for the target. For the source, the tag is `<NODATA>` and for the target it is `<NoDataValue>`. In this case, both the source and the target no data values should be 0.

The result is the following VRT for the texture dataset:
```xml
<VRTDataset rasterXSize="84293269" rasterYSize="42146634">
        <SRS>GEOGCS["unnamed ellipse",DATUM["unknown",SPHEROID["unnamed",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]</SRS>
        <GeoTransform> -1.8000000000000000e+02,  4.2708036548961860e-06,  0.0000000000000000e+00,  9.0000000000000000e+01,  0.0000000000000000e+00, -4.2708036548961860e-06</GeoTransform>
    <VRTRasterBand dataType="Byte" band="1">
        <NoDataValue>0</NoDataValue>
        <ColorInterp>Gray</ColorInterp>
        <SimpleSource>
            <SourceFilename relativeToVRT="1">PSP_001918_1735_RED_A_01_ORTHO_longlat.TIFF</SourceFilename>
            <SourceBand>1</SourceBand>
            <SourceProperties RasterXSize="25544" RasterYSize="43023" DataType="Byte" BlockXSize="25544" BlockYSize="1" />
            <SrcRect xOff="0" yOff="0" xSize="25544" ySize="43023" />
            <DstRect xOff="24121366.0622929" yOff="22566614.2605087" xSize="25544" ySize="43023" />
            <NODATA>0</NODATA>
        </SimpleSource>
    </VRTRasterBand>
    <VRTRasterBand dataType="Byte" band="2">
        <ColorInterp>Alpha</ColorInterp>
        <ComplexSource>
            <SourceFilename relativeToVRT="1">PSP_001918_1735_RED_A_01_ORTHO_longlat.TIFF</SourceFilename>
            <SourceBand>1</SourceBand>
            <SourceProperties RasterXSize="25544" RasterYSize="43023" DataType="Byte" BlockXSize="25544" BlockYSize="1" />
            <SrcRect xOff="0" yOff="0" xSize="25544" ySize="43023" />
            <DstRect xOff="24121366.0622929" yOff="22566614.2605087" xSize="25544" ySize="43023" />
            <ScaleRatio>255</ScaleRatio>
            <NODATA>0</NODATA>
        </ComplexSource>
    </VRTRasterBand>
</VRTDataset>
```


## Wrapping Up
Now we are finally done creating the virtual datasets we need to be able to make OpenSpace read the local datasets correctly!  The files we still need are the two longlat geotiffs and the virtual dataset definition files. Since the VRTs use relative paths to find the image files they use, they should be kept in the same folder if they were built in the same directory.

Now these files can be read by OpenSpace as part of a RenderableGlobe. The texture dataset can be added as a color layer while the height map is simply set as a height layer. To use underlying color information, we can set the blend mode to **Color** for the texture layer.
```lua
    ...
        ColorLayers = {
            ...
            {
                Name = "Layered Rock Outcrops in Southwest Candor Chasma",
                FilePath = "hirise_tutorial/Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_Texture.vrt",
                BlendMode = "Color"
            },
            ...
        },
        ...
        HeightLayers = {
            ...
            {
                Name = "Layered Rock Outcrops in Southwest Candor Chasma",
                FilePath = "hirise_tutorial/Layered_Rock_Outcrops_in_Southwest_Candor_Chasma_HeightMap.vrt"
            },
            ...
        },
    ...
```
