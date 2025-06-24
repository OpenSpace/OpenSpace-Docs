(spaceweather_id)=
# Space Weather

There are three publically available profiles dedicated to space weather. They are all made by the collaborators at the [Community Coordinated Modeling Center](https://ccmc.gsfc.nasa.gov/) (CCMC) at NASA Goddard Space Flight Center. The data used for these are mainly either observation data or simulation outputs from different simulation models. This page is focused on these data sources and back-end features. Read more about the different profiles under [Profiles](/profiles/index.md).

## ISWA & Dynamic File Sequence Downloader

The CCMC Integrated Space Weather Analysis (ISWA) system is a platform that distributes real-time space weather information. All this data is public and readily available to the public and can be browsed and downloaded from the ISWA data tree.

In OpenSpace this data is downloaded using the Dynamic File Sequence Downloader. This downloader downloads few data files at a time. It correlates the time in OpenSpace with the files associated time stamps to ensure to only download the relevant data. This downloader is using HTTP-requests and is independet of the type of data it is downloading. Therefore it can, in theory, be used and support visualizations for any of CCMC continuous simulation models. Because the responsibility of reading the data downloaded does not lie on the downloader, implementation in renderables are needed to add the support of the downloader. The renderables who are supported by the Dynamic File Sequence Downloader are [Renderable Time Varying Fits Sphere](fitsfilereader_renderable_time_varying_fits_sphere) and [Renderable Field Lines Sequence](fieldlinessequence_renderablefieldlinessequence). To use it, four parameters in the asset is required to be added; LoadingType set to "DynamicDownloading", two URLs needs to be specified, one to InfoURL and one to DataURL. They are expected to return JSON-formated pages. The InfoURL will return with a min and max time for the data sequence. This is then used to construct a url for the HTTP-request together with DataURL. Lastly a DataID is required. This will correspond to a dataset of a specific simulation model.

The InfoURL and DataURL can look like so:

InfoURL = "https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/DataInfoServlet?id=" <br>
DataURL = "https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/FilesInRangeServlet?dataID="

Note that these URLs expect the data ID. This is added internaly from the input parameter DataID.

The DataInfoServlet can look like so: <br>
https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/DataInfoServlet?id=2284

The min and max time for the sequence is then used in the FilesInRangeServlet like so: <br>
https://iswa.gsfc.nasa.gov/IswaSystemWebApp/FilesInRangeServlet?dataID=2284&time.min=2008-12-24T23:44:00.000&time.max=2025-05-18T06:14:00.000

### Features and Notes on Robustness

There are a few note worthy things about the Dynamic File Sequence Downloader. When for any reason a download fails, it discards that file. Whenever a download succeeds, it notes its name in a text file. If the user has chosen to save the files for next run, only the files in the list will be used. It might seem redundant at first since failed downloads are discarded, but this also ensures it will not use corrupted files that might stick around if the software crashes for any other reason, while a file was downloading.

It ensures that internal memory is not overloaded, since the longer you run a visualization with this, more and more files are downloaded, read and loaded into memory. It keeps an internal list to keep track of the newest to oldest files. It will unload the data from the oldest file if too many are loaded. If the user has low internal memory, this does not guarantee that it will not run out. The max number of files loaded is 100.
