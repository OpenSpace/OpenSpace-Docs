# Server Conversion
This wiki covers the steps required to convert raster data to MRF (Multi-Raster Format) so that it can be served-up by a AHTSE (An Httpd Tile-Serving Engine) web server.

See [this wiki](server-install) for how to install & configure a AHTSE server, and [this wiki](server-import) for importing an MRF data set into the server.

[GDAL](http://www.gdal.org/usergroup0.html) (version 2.1.3 or greater) software tools are required to perform these conversion steps.

## 1.0 Basic Description of the MRF Data Format
A single tiled WMS data set in MRF format consists of a set of 3 files, each with the same filename but with the following file extensions:
 * **.mrf** : contains the raster metadata.
 * **.idx** : contains the indeces for where the tiles are located in the raster data file.
 * **.p\*g** : the raster data compressed in either JPEG (.pjg) or PNG (.ppg).

Once these files are created, the data set is ready to be imported into the AHTSE server.

## 2.0 How to Convert a Geospatically-Located GeoTIFF File to MRF Format
This section assumes that the input is a raster image file in GeoTIFF (GTiff) format. [This page](http://www.gdal.org/frmt_gtiff.html) provides a detailed description of this format. Perform the following steps in order to create the MRF files (as described in the above section) from this source file. Before proceeding, verify that the input file has geospatial information by typing:
`gdalinfo dataset.tif`
If the "**Coordinate System is:**" entry is blank, then skip the rest of this section and proceed to section 3.0 below in order to convert the file to GeoTIFF format, and then come back to section 2.1. Otherwise, section 3.0 will not be needed.

### 2.1 _Build VRT_ step
This step builds a .vrt (ViRTual dataset) file from the GeoTIFF file. Here is a simple usage example:
`gdal_translate -of VRT dataset.tif dataset.vrt`
where **dataset.tif** is the GeoTIFF input file, and **dataset.vrt** is the output file.

Here is an example of specifying the geo-referenced extents of the map:
`gdal_translate -of VRT -a_ullr -180 90 180 -90 dataset.tif dataset.vrt`
The **-a_ullr** flag is used to specify the x,y of the upper-left corner, and then the x,y of the lower-right corner. Here, **x** is the longitude angle and **y** the latitude angle in degrees. The +/- 180° and +/- 90° range, respectively, in this example covers the entire globe. It is probably best to leave the **-a_ullr** options out, unless specifying the map extents is necessary.
Note that the previously-used method for this was the `gdalbuildvrt` tool, where "gdalbuildvrt" was used instead of "gdal_translate -of VRT", and "-te" flag was used instead of "-a_ullr" (the "-te" flag has different coordinates ordering). Apparently `gdal_translate` is the more reliable tool for this application.

### 2.2 _gdal\_translate_ step
This step creates a raster image using either PNG or JPEG compression, and a .mrf file for the data set. [This page](http://www.gdal.org/gdal_translate.html) provides a usage description for the **gdal\_translate** software tool. This is the usage for PNG:
```
gdal_translate -of MRF -co COMPRESS=PNG -co BLOCKSIZE=512 -r bilinear dataset.vrt dataset.mrf
```
Here, the **-of** specifies MRF output format, and **-co BLOCKSIZE=** specifies the blocksize in pixels, where values of 256, 360, or 512 are common. Sometimes the dimensions of the original image have a common multiple that can be used for the blocksize value. The flag **-r** specifies resampling algorithm to be used. The input .vrt file from the previous step is provided, followed by the output filename.

If JPEG compression is desired, this can be specified instead by **-co COMPRESS=JPEG -co QUALITY=xx**, where the quality can be an integer from 1 to 100 to specify jpeg compression quality.

Another option that is used in some conversions is **-co OPTIONS="V1:1"**. The documentation is not very clear on the function of this option, however.

### 2.3 _gdaladdo_ step
This step creates overviews/tiles at a series of lower-resolution levels from the MRF data set base image. Provided as arguments are subsampling factors that increase by the power of 2, which will be used to divide the base image for each overview/tile level. This count increases up to the point where any further sub-sampling would produce an image with a horizontal resolution less than or equal to the block size (e.g. tile size) specified in the **gdal\_translate** step. [This page](http://www.gdal.org/gdaladdo.html) provides a usage description for the **gdal\_translate** software tool.
Put another way, the number of overviews must satisfy:
`(Horizontal_resolution / 2^n ) > block size (pixels)`
where n is the tile level (number of overviews). For example, a common map configuration used is a source map with a 92160 x 46080 resolution and a block size of 360. Choosing n=8 overviews, the equation would be: 92160 / 256 = 360, which is equal to the block size. Even though this divides evenly, it will result in a distorted map when projected on the planet. So for this particular map configuration, the following command would be used to generate 7 overviews:
`gdaladdo -r avg dataset.mrf 2 4 8 16 32 64 128`
Here, **-r avg** specifies a sub-sampling algorithm to average the colors, and the 7 integers specify the subsampling factors for the 7 overview/tile levels.
Another way to compute the number of overviews:
`INT(LOG2(Horizontal_resolution/block_size) - 0.0001)`

The rule for how many overviews are allowed does not seem to have been made clear. However, all maps currently used by OpenSpace follow the above rule. It should be noted that all of these maps have an aspect ratio of `2.0`. An image with a different ratio (especially if larger) might violate the rule.

## 3.0 How to Convert Raw Raster Data to Geospatially-Located GeoTIFF Format
This section covers the case where a raw raster data file (e.g. image) does not contain any geo-spatial information (e.g. no coordinate system, no location).

### 3.1 Simple Example of a Complete Mapping of Source Image to Sphere
The **gdal\_translate** software tool is used to convert the source raster file. Here is a usage example:
`gdal_translate -of GTiff -a_ullr -180 90 180 -90 -a_srs <SRS_Coordinates> main_COL_v007.png main_COL_v007.tif`
First, note that the text <SRS_Coordinates> is a substitute for the following string:
```
 GEOGCS["Mars 2000",DATUM["D_Mars_2000",SPHEROID["Mars_2000_IAU_IAG",3396190.0,169.89444722361179]],PRIMEM["Greenwich",0],UNIT["Decimal_Degree",0.0174532925199433]]
```
which can be given directly in the **gdal\_translate** command, or can be put into a text file in which case the **-a\_srs** argument is that filename.
The **-of** specifies the GeoTIFF output format using the **GTiff** tag, and **-a\_ullr** lists the longitude & latitude of the upper-left corner and lower-right corner of the raster mapping on the globe in degrees. The final arguments are the input raster file and output GeoTIFF file.

### 3.2 Example of Swapping East & West Hemispheres
It is apparently a common situation for a map to be shifted to the east by 180 degrees, making it necessary to swap the east/west hemispheres of the map (left/right halves of the image). The following console commands can be used to create a `.vrt` file that performs this swap operation:
```
gdal_translate -of VRT -srcwin ${halfX} 0 ${halfX} ${fullY} -a_ullr -180 90 0 -90 -a_srs "${PRJ}" ${SRC} west.vrt
gdal_translate -of VRT -srcwin 0 0 ${halfX} ${fullY} -a_ullr 0 90 180 -90 -a_srs "${PRJ}" ${SRC} east.vrt
```
where:
* `${SRC}` is the source image file
* `${PRJ}` is the string that defines the map projection
* `${halfX}` is half the horizontal resolution of the source image
* `${fullY}` is the full vertical resolution of the source image
After this, the *gdalbuildvrt* tool can be used to combine the two inputs (combining inputs is the main use for this tool):
`gdalbuildvrt -q -overwrite whole.vrt west.vrt east.vrt`
If this swap operation is not performed, then the steps in section 2.1 should be used.

## 4.0 Handling Binary Source Files Masquerading as Image Files
Maps for the planet Mercury were created for OpenSpace using maps from the Messenger mission at the USGS site. Although the files appeared to be image files (due to their .tif extensions), they required special treatment in order to be converted. This special case is covered here in case this format type is encountered in future maps.

The source files had a 32-bit float data type. It is necessary to add **-ot Byte** to the `gdal_translate` step in order to get an 8-bit integer type expected for an image channel. In addition to specifying byte output, a lookup table entry is needed in the .vrt file to map the range of floating-point values to the 8-bit range. After the .vrt file is generated, `<LUT>` entries should be added to it manually using a text editor. Each color channel (or just one for grayscale) has a `<VRTRasterBand>` tag, and inside this there is a `<ComplexSource>` tag. A new `<LUT>` entry is added as a sub-entry to this. For example:
`<LUT>0.2:0, 2.5:255</LUT>`
maps the 0.2 to 2.5 floating-point range to the full 8-bit integer range. Using the `gdalinfo -hist` is a good way to see the distribution of floating-point values in the file. In the case of the Mercury maps, however, the value chosen to represent "no data" pixels was a very large value. In bands with such pixels, unfortunately, the histogram was useless by these large values and the range had to be determined by trial-and-error.

The files contained multiple bands, as shown in their `gdalinfo` output. Some had as many as 17 separate bands, and it was unclear which ones were color channels. Fortunately, treating the first 3 bands as RGB channels worked. The command `gdalbuildvrt -b 1 -b 2 -b 3 input.vrt source_image.tif` was used to import only the first 3 bands in the order listed. Together with adding **-co PHOTOMETRIC=RGB** to the `gdal_translate` command, a successful color conversion was achieved. For a grayscale map, the **PHOTOMETRIC** options is not used, and the **-b** option specifies which band is used as the input (used only if the input file has more than one band).

## 5.0 An Example Case of a Digital Elevation Map (DEM)
This is a summary of the conversion process performed on the Venus MagellanDEM map, which is a companion to the MagellanMosaic imagery. Only the details that differ from the above sections are written here.

The Build VRT process was the same as in Section 2.1 above, but the process of using `gdal_translate` to generate an .mrf file (Section 2.2) did have a few differences. The **-ot Byte** option mentioned in Section 4.0 was used in order to create an 8-bit grayscale for elevation. This made it easy to see the results in a viewer, although the original 16-bit resolution was lost in this step. The **-co OPTIONS="V1:1"** option mentioned in Section 2.2 was also used. The blocksize was important. Originally a blocksize of 360 was used, but the resulting geometry of the map was incorrect. On the second attempt, a blocksize of 256 was used because the 8192x4096 resolution of the map was evenly divisible by this. In order to get the grayscale range correct, the **-scale** option was used to match the data range (obtained from `gdalinfo -hist`) to the desired 0 - 255 8-bit range. The resulting translation command was:
```
gdal_translate -q -of MRF -ot Byte -scale -2757 8000 0 255 -co COMPRESS=PNG -co BLOCKSIZE=256 -co OPTIONS="V1:1" ${inputVrt} ${outputMrf}
```
