# Solar Imagery Data
This page describes how to download and prepare solar imagery data for use with the solar browsing feature in OpenSpace. The imagery is sourced from [Helioviewer](https://helioviewer.org/), a service that provides access to solar observations from several spacecraft.

Downloaded images are stored as JPEG 2000 (`.jp2`) files on disk and loaded into OpenSpace at runtime using the `RenderableSolarImagery` renderable. See the [Solar Browsing Rendering](./solarbrowsing-rendering.md) page for details on how to set up the renderables.

## Supported Spacecraft and Instruments
The system currently supports images from three spacecraft. A full list of available instruments and their source identifiers can be found in the [Helioviewer API documentation](https://api.helioviewer.org/docs/v2/appendix/data_sources.html).

| Spacecraft | Notes                              |
| ---------- | ---------------------------------- |
| SDO        | Solar Dynamics Observatory         |
| SOHO       | Solar and Heliospheric Observatory |
| STEREO     | STEREO-A and STEREO-B              |

## Downloading Data with the HelioviewerDownloadTask
Data is downloaded using the `HelioviewerDownloadTask`, a pre-processing step run via the TaskRunner before starting OpenSpace. The task queries the Helioviewer API and downloads all available images within a specified time interval at a given cadence, storing the downloaded images on disk.

See the [HelioviewerDownloadTask](/reference/asset-components/Task/solarbrowsing_helioviewerdownload_task) documentation for a full reference of available parameters.

An example task file is available at `data/tasks/solarbrowsing/download_from_helioviewer.task`. It downloads the color maps from the OpenSpace data servers and then runs the download for SDO AIA-171 and STEREO EUVI-A 171. The relevant portion of the task looks like this:

```lua
return {
  {
    Type = "HelioviewerDownloadTask",
    Name = "SDO",
    SourceId = 10,
    Instrument = "AIA-171",
    ColorMap = openspace.absPath("${SYNC}/http/solarbrowsing/AIA-171.txt"),
    StartTime = "2024-05-06T00:00:00.000Z",
    EndTime = "2024-05-14T00:00:00.000Z",
    TimeStep = 60 * 60, -- Download an image every hour
    OutputFolder = "${SYNC_DYNAMIC}/solarbrowsing/sdo/aia-171"
  }
}
```

To run the task, pass the `download_from_helioviewer.task` file to the TaskRunner executable via drag-and-drop.

:::{note}
The task downloads images in parallel and skips files that already exist on disk, making it safe to rerun if a download was interrupted.
:::

:::{tip}
It is recommended to store downloaded images in `${SYNC_DYNAMIC}/solarbrowsing/` as this path will be used for dynamic solar imagery downloads in a future version of OpenSpace.
:::

### Downloading Multiple Instruments
To download imagery data for multiple instruments, add one task entry per instrument. For example, to download both AIA-171 and AIA-193 for SDO:

```lua
return {
  {
    Type = "HelioviewerDownloadTask",
    Name = "SDO",
    Instrument = "AIA-171",
    SourceId = 10,
    ColorMap = openspace.absPath("${SYNC}/http/solarbrowsing/AIA-171.txt"),
    StartTime = "2024-05-08T00:00:00",
    EndTime = "2024-05-08T06:00:00",
    TimeStep = 60 * 60,
    OutputFolder = "${SYNC_DYNAMIC}/solarbrowsing/sdo/aia-171"
  },
  {
    Type = "HelioviewerDownloadTask",
    Name = "SDO",
    Instrument = "AIA-193",
    SourceId = 11,
    ColorMap = openspace.absPath("${SYNC}/http/solarbrowsing/AIA-193.txt"),
    StartTime = "2024-05-08T00:00:00",
    EndTime = "2024-05-08T06:00:00",
    TimeStep = 60 * 60,
    OutputFolder = "${SYNC_DYNAMIC}/solarbrowsing/sdo/aia-193"
  }
}
```

After running the task, the `sdo/` root directory will contain one subdirectory for each instrument, and both will be discovered automatically by the renderable.

(solarimagery_directory_structure_id)=
## Directory Structure
Images for each instrument must be stored in their own subdirectory. The `OutputFolder` in the task specifies this subdirectory. A typical layout for SDO with two instruments would look like:

```
${SYNC_DYNAMIC}/solarbrowsing/sdo/
  aia-171/
    AIA-171.txt              <- colormap, copied here automatically by the task
    2024_05_08__00_00_11_000__SDO_AIA-171.jp2
    2024_05_08__00_10_23_000__SDO_AIA-171.jp2
    ...
  aia-193/
    AIA-193.txt
    2024_05_08__00_00_23_000__SDO_AIA-193.jp2
    ...
```

The `ImageDirectory` property in the Renderable asset should point to the root folder (e.g. `sdo/`), and the Renderable will automatically discover all instrument subdirectories at startup.

:::{note}
The filename format is handled entirely by the task and is required for OpenSpace to correctly parse timestamps and instrument names from the files. Downloaded files should not be renamed.
:::

## Color Maps
Each instrument requires a color map file that defines how grayscale image data is translated into color. Color maps are currently provided for all SDO AIA instruments and for the STEREO EUVI-A 171 instrument included in the example task. The task automatically downloads these from the OpenSpace data servers and copies them into the appropriate instrument subdirectory. The color maps are equivalent to those used by NASA.

The color map is a plain text file where each `mappingkey` entry maps a normalized intensity value in the range [0, 1] to an RGBA color, with each channel as an integer in the range [0, 255]:

```
width 256
lower 0.0
upper 1.0
mappingkey 0.0   0   0   0   255
mappingkey 0.004 0   0   0   255
...
mappingkey 1.0   255 255 255 255
```

## Metadata Caching
On the first startup after downloading new images, OpenSpace parses the metadata embedded in each JP2 file and writes a cache file (e.g. `AIA-171_cached.txt`) to the root directory. Subsequent startups use this cache and load much faster. If the contents of an instrument directory change (for example, when new images are added), the cache for that directory is regenerated automatically.
