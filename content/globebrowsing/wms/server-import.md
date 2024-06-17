# Server Import
This wiki covers the steps required to import a single WMS dataset into a web server configured to be a AHTSE (An Httpd Tile-Serving Engine) server. Such a server can of course handle multiple WMS datasets in the MRF (Meta-Raster Format), but these instructions can be used to import each set into the server.

[This wiki](server-install) covers the steps involved in getting a AHTSE server installed and configured. [This wiki](server-conversion) covers the steps involved in converting a raw raster image into the MRF format. *This wiki assumes that the dataset has already been converted using GDAL software tools.*

These instructions are specific to a Linux server.

## Modify AHTSE.conf File
The AHTSE configuration file resides in the directory that contains the Apache web server config files (multiple .conf files), which may be `/etc/apache2/` or `/etc/httpd/conf.d/`, for example. Create the file **AHTSE.conf** here if it does not already exist.
This text file has the header:
```
<Location "/server-info">
  SetHandler server-info
</Location>
```
and is followed by a 5-line block for every WMS dataset to be served, which has the following format:
```
<Directory /path/to/directory_tree/containing/wms_files>
  Options -Indexes -FollowSymLinks -ExecCGI
  MRF_RegExp .*/tile/.*
  MRF_ConfigurationFile /path/to/directory/with/webconf/dataset_name.webconf
</Directory>
```
There are really only two entries to change in this block, assuming that the tile service will use the default options from the second line, and the regular expression format for the URL in the third line. The path in the first line points to the directory tree that contains a `.wms` file for each data set. This directory tree has directories arranged in the same manner and same names as the directory tree of the source data (for example the base of this tree may have `Earth/`, `Mars/`, `Mercury/` directories, each with subdirectories for the tiled data sets for each of those planets. Usually, only a single `.wms` file exists in those locations to represent the data set.

This directory exists in Apache's **DocumentRoot** location, where it stores web content to be served-up. On the Utah server, Apache has a virtual host set up for web requests with the **openspace.sci.utah.edu** address. This virtual host is configured with a **DocumentRoot** path of `/srv/www/vhosts/openspace` (discussed in detail [here](server-install)). This location contains a directory tree that matches that of the WMS datasets in the data directory (discussed below in "Add .wms file" section).

The other directory that needs to be modified from the above example is the **MRF_ConfigurationFile** path. Like the wms file & directory structure described above, this path contains a directory tree that matches that of the WMS datasets in the data directory. Also like the wms directories, there is usually only a single .webconf file exists for each dataset. This file contains information about the MRF file, which is needed by the **mod_mrf** module.
Both the .wms and .webconf files are discussed in more detail below. Here is an example entry in the Utah server:
```
<Directory /srv/www/vhosts/openspace/Mars/MolaElevation>
  Options -Indexes -FollowSymLinks -ExecCGI
  MRF_RegExp .*/tile/.*
  MRF_ConfigurationFile /home/openspace/AHTSE/conf/Mars/MolaElevation.webconf
</Directory>
```
For clarification, `/srv/www/vhosts/openspace` and `/home/openspace/AHTSE/conf` have the same sub-directory structure, with a single file for each WMS data set. The filenames are the same, but with a `.wms` extension in the former, and a `.webconf` extension in the latter. There is also a third location with this sub-directory structure, which is where the actual data is stored. The reason for the separate `.wms` and `.webconf` directories is to keep configuration and data files out of the Apache **DocumentRoot** directory.


## Add a _.webconf_ File for the Data Set
A webconf file is required for, and provides a basic summary of, each MRF data set. The file contains 6 lines that provide the total raster size, overview size, path to data & index files, and regular expression syntax. The necessary information can be found by using the **gdalinfo** software tool (usage : `gdalinfo <path to your mrf file>`). [This readme](https://github.com/lucianpls/mod_mrf/blob/master/README.md) provides more detailed information about this format, which follows the outline below:
```
RegExp .*/tile/.*
Size <total size of raster>
PageSize <page size>
DataFile <path to data file>
IndexFile <path to index file>
SkippedLevels   <no of levels to skip>
```
Description of each line:

Line 1: A Regular Expression to match with the URL. You can specify multiple RegExp and the provided URL will be processed by mod_mrf module if at least one match is found.

Line 2: Size of the total raster (4 space-separated values: horizontal resolution of entire image, vertical resolution (entire), 1, number of bands in data source).

Line 3: Tile(Block) Size (4 space-separated values: horizontal resolution of block, vertical resolution of block, 1, number of bands in data source).

Line 4: Path to raster file. This is the GDAL-converted form of the JPEG-compressed (.pjg) or PNG-compressed (.ppg) source file.

Line 5: Path to index (.idx) file

Line 6: SkippedLevels can be used to serve the top level (lowest resolution) of the MRF data set. This can be used for some clients which might expect two blocks at the top level.


## Add a _.wms_ File for the Data Set
A single .wms file contains detailed information about the MRF data set. The following is the **MolaElevation.wms** file from the Mars data set:
```
<GDAL_WMS>
  <Service name="TMS">
    <ServerUrl>http://openspace.sci.utah.edu/Mars/MolaElevation/tile/${z}/${y}/${x}</ServerUrl>
  </Service>
  <DataWindow>
    <UpperLeftX>-180.0</UpperLeftX>
    <UpperLeftY>90.0</UpperLeftY>
    <LowerRightX>180.0</LowerRightX>
    <LowerRightY>-90.0</LowerRightY>
    <SizeX>46080</SizeX>
    <SizeY>23040</SizeY>
    <TileLevel>6</TileLevel>
    <YOrigin>top</YOrigin>
  </DataWindow>
  <Projection>GEOGCS["GCS_Mars_2000_Sphere",DATUM["D_Mars_2000_Sphere",SPHEROID["Mars_2000_Sphere_IAU_IAG",3396190.0,0.0]],PRIMEM["Reference_Meridian",0.0],UNIT["Degree",0.0174532925199433]]</Projection>
  <BlockSizeX>360</BlockSizeX>
  <BlockSizeY>360</BlockSizeY>
  <BandsCount>1</BandsCount>
  <MaxConnections>10</MaxConnections>
</GDAL_WMS>
```
This wiki assumes that the data set to be imported has already been converted to MRF format. However, a `.wms` file for the set is not necessarily provided. The example above can be copy/pasted with the filename matching that of the 3 MRF files (except their extensions).

Values for some of these items may be obtained by using the **gdalinfo** tool (discussed in the wiki for converting data to MRF format) on an MRF file. For example, typing `gdalinfo MolaElevation.mrf` will display the information needed for this section.

The following paragraphs discuss the important parts of this file and how they need to be modified for a new imported data set.

The **\<ServerUrl\>** tag needs to have the proper server hostname (in this case **openspace.sci.utah.edu**) followed by the relative path to the data set, which is given by the **AHTSE.conf** entry for the set minus the Apache **DocumentRoot** path (in this case sub-directories located in `/srv/www/vhosts/openspace/`). Here, the path to the data is **Mars/MolaElevation**, followed by **/tile/** which is specified as the regular expression string in both the `.wms` and `.webconf` file examples shown above. The z,y,x values following are for specifying overviews/tiles. A specific URL example for this data set is:
`http://openspace.sci.utah.edu/Mars/MolaElevation/tile/0/0/0`

Next are tags for geo-locating the raster data to a globe. An upper-left and lower-right corner are required. The **X** (longitude) and **Y** (latitude) in degrees are supplied to specify where the image is to be overlaid. Here, the full globe is covered by the range of these values.

**\<Size\*\>** are based on the full raster size of the data.

**\<TileLevel\>** is the number of tiles or overviews in the MRF data.

The **\<Projection\>** is a coordinate system projection used to geo-locate the raster data onto the globe. This is obtainable using `gdalinfo` as described above. Many coordinate system projections can be found at www.spatialreference.org. The OGC WKT or ESRI WKT formats have been verified to work here.

**\<BlockSize\*\>** are based on the block size for tiles/overviews.

**\<BandsCount\>** is the number of bands in the MRF data.

**\<MaxConnections\>** specifies the maximum number of clients for this data.


## Add Set of MRF Data Files
A single tiled WMS data set is provided in a set of 3 files, each with the same filename and the following file extensions:
  - `.mrf`: containing the raster metadata
  - `.idx`: containing the indeces for where tiles are located in the raster data
  - `.p*g`: the raster data compressed in either JPEG (.pjg) or PNG (.ppg)

If a data location does not already exist on the server, create one here. This directory path should have a sub-directory tree that matches that of the Apache vhosts and webconf directory trees. Create a sub-directory for each data set (with the same name) in the data location, and place the 3 MRF files here.

The Utah server uses `/data/AHTSE/` as its data path. To continue with the Mars MoleElevation example, this data set is located at `/data/AHTSE/Mars/MolaElevation`, and contains 3 **MolaElevation.*** files (with .mrf, .idx, .ppg extensions). The **DataFile** entry in the `/home/openspace/AHTSE/conf/Mars/MolaElevation.webconf` file is `/data/AHTSE/Mars/MolaElevation/MolaElevation.ppg`, and the **IndexFile** entry is `/data/AHTSE/Mars/MolaElevation/MolaElevation.idx`.


## Summary of Overall File Layout ##
Since the AHTSE server as described here has a very distributed layout, a summary is included here for clarification.

The Apache web server runs in a standard or virtual host configuration with a specific URL request mapped to the `.wms` file in the URL's relative path (according to Apache's configuration file). On startup, Apache includes the AHTSE.conf file which maps specific locations in the web content location (matches URL) to the path of the .webconf file for that data set. This file lists links to the data path that contains the 3 MRF files for this particular data set. The MRF Apache module uses the x,y,z coordinates supplied in the URL (the format of which is defined in the `.wms` file), and accesses the raster file (`.ppg` or `.pjg`) based on the matching `.idx` file which provides pointers for specific tiles in the raster file.
