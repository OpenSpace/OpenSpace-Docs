(spaceweather_id)=
# Space Weather

There are three publicly available profiles dedicated to showing space weather phenomena. They are all made by the collaborators at the [Community Coordinated Modeling Center](https://ccmc.gsfc.nasa.gov/) (CCMC) at NASA Goddard Space Flight Center. The data used for these are mainly either observation data or simulation outputs from different simulation models. This page is focused on these data sources and back-end features. Read more about the different profiles under [Profiles](/profiles/index.md).

## ISWA & Dynamic File Sequence Downloader

The CCMC Integrated Space Weather Analysis [(ISWA)](https://ccmc.gsfc.nasa.gov/tools/ISWA/) system is a platform that distributes real-time space weather information. All this data is public and readily available to the public and can be browsed and downloaded from the ISWA data tree.

In OpenSpace, this data is downloaded using the Dynamic File Sequence Downloader. This downloader downloads a few data files at a time. It correlates the in-game time in OpenSpace with the files' associated time stamps to ensure that only relevant data is downloaded. This downloader is using HTTP requests and is independent of the type of data it is downloading. Therefore, it can, in theory, be used and support visualizations for any of CCMC's continuous simulation models.

The downloader takes care of downloading the data, but not reading it. Hence, any renderables that use the downloader must implement support for data handling. The renderables that support the Dynamic File Sequence Downloader are [RenderableTimeVaryingFitsSphere](fitsfilereader_renderable_time_varying_fits_sphere) and [RenderableFieldLinesSequence](fieldlinessequence_renderablefieldlinessequence). To use it, four parameters are required in the asset; First, `LoadingType` must be set to `"DynamicDownloading"`. In addition, two URLs need to be specified: one to `InfoURL` and one to `DataURL`. They are expected to return JSON-formatted pages. The `InfoURL` will return with a min and max time for the data sequence. This is then used to construct a URL for the HTTP request together with `DataURL`. Lastly, a `DataID` is required. This will correspond to a dataset of a specific simulation model within the requested data.

Here are examples for the `InfoURL` and `DataURL`:
  - `InfoURL` = "https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/DataInfoServlet?id="
  - `DataURL` = "https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/FilesInRangeServlet?dataID="

Note that these URLs expect the data ID. This is added internally from the input parameter `DataID`.

The DataInfoServlet can look like so: <br>
`https://iswaa-webservice1.ccmc.gsfc.nasa.gov/IswaSystemWebApp/DataInfoServlet?id=2284`

The min and max time for the sequence is then used in the FilesInRangeServlet like so: <br>
`https://iswa.gsfc.nasa.gov/IswaSystemWebApp/FilesInRangeServlet?dataID=2284&time.min=2008-12-24T23:44:00.000&time.max=2025-05-18T06:14:00.000`

### Features and Notes on Robustness

There are a few noteworthy things about the Dynamic File Sequence Downloader:
- When, for any reason, a download fails, that file is discarded. Whenever a download succeeds, the file name is noted in a text file. If the user has chosen to save the files for next run, only the files in the list will be used. In addition to discarding failed downloads, this is needed to ensures corrupted files are not used, that might have stuck around if the software had crashed for any other reason, while a file was downloading.

- The longer you run a visualization with the Dynamic File Sequence Downloader, more and more files are downloaded. To ensure internal memory is not overloaded, an internal list keeps track of the loaded files, ordered newest to oldest. When the list is full, the oldest file will be unloaded, but the file still exists on the hard drive. If the user has low internal memory, this does not guarantee that it will not run out. The max number of files loaded is 100.
