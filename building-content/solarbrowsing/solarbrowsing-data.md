# Solar Browsing Data
This page describes how to download and prepare solar imagery data for use with the solar browsing feature in OpenSpace. The imagery is sourced from [Helioviewer](https://helioviewer.org/), a service that provides access to solar observations from several spacecraft.

Downloaded images are stored as JPEG 2000 (`.jp2`) files on disk and loaded into OpenSpace at runtime using the `RenderableSolarImagery` renderable. See the [Solar Browsing Rendering](./solarbrowsing-rendering.md) page for details on how to set up the renderables.

## Supported Spacecraft and Instruments
The system currently supports images from three spacecraft. A full list of available instruments and their source identifiers can be found in the [Helioviewer API documentation](https://api.helioviewer.org/docs/v2/appendix/data_sources.html).

| Spacecraft | Notes |
| ---------- | ----- |
| SDO | Solar Dynamics Observatory |
| SOHO | Solar and Heliospheric Observatory |
| STEREO | STEREO-A and STEREO-B |

Images are only available for the duration of each mission. If a requested time range falls outside the available data, the Helioviewer API will return a message indicating this.

## Downloading Data with the HelioviewerDownloadTask
Data is downloaded using the `HelioviewerDownloadTask`, a pre-processing step run via the TaskRunner before starting OpenSpace. The task queries the Helioviewer API and downloads all available images within a specified time interval at a given cadence, storing the downloaded images on disk.

See the [HelioviewerDownloadTask](#solarbrowsing_task_helioviewerdownload) documentation for a full reference of available parameters.

An example task file is available at `data/tasks/solarbrowsing/download_from_helioviewer.task`. It downloads imagery for both SDO AIA-171 and STEREO EUVI-A 171. To run the task, pass the file to the TaskRunner executable via drag-and-drop.

The three parameters most commonly edited are `StartTime`, `EndTime`, and `TimeStep`:
  - `StartTime` and `EndTime` define the time interval to download, in ISO 8601 format
  - `TimeStep` sets the desired cadence in seconds between downloaded images. The actual spacing depends on data availability from Helioviewer, but will never be shorter than this value

:::{note}
The task downloads images in parallel and skips files that already exist on disk, making it safe to rerun if a download was interrupted.
:::

:::{tip}
It is recommended to store downloaded images in `${SYNC_DYNAMIC}/solarbrowsing/` as this path will be used for dynamic solar imagery downloads in a future version of OpenSpace.
:::

## Common Tasks

### Getting Data for a Specific Time Range
To download data for a specific period, update the `StartTime` and `EndTime` fields in the task file using ISO 8601 format. These define the time range of the data you want to retrieve. For example, to download the last 10 days of data, set `EndTime` to the current time and `StartTime` to 10 days earlier:

```lua
StartTime = "2026-04-01T00:00:00.000Z",
EndTime = "2026-04-11T00:00:00.000Z",
```

More generally, you can adjust these values to match any desired time range. For instance, the example below retrieves one week of hourly SDO AIA-171 images starting from a specific date:

```lua
{
  Type = "HelioviewerDownloadTask",
  Name = "SDO",
  SourceId = 10,
  Instrument = "AIA-171",
  ColorMap = openspace.absPath("${SYNC}/http/solarbrowsing/AIA-171.txt"),
  StartTime = "2024-05-06T00:00:00.000Z",
  EndTime = "2024-05-13T00:00:00.000Z",
  TimeStep = 60 * 60, -- one image per hour
  OutputFolder = "${SYNC_DYNAMIC}/solarbrowsing/sdo/aia-171"
}
```

:::{note}
You can request up to 1000 images per download from the HelioViewer API. If the combination of `StartTime`, `EndTime`, and `TimeStep` would result in more than 1000 images, the API will automatically increase the timestep to stay within this limit. A warning will be issued by the task when this adjustment occurs.
::

### Adding More Images to an Existing Dataset
Since the task skips files that already exist, it is safe to run it multiple times with different or overlapping time ranges for the same instrument. All downloaded images are placed in the same `OutputFolder` and will be loaded together by OpenSpace at startup. For example, to extend a previously downloaded dataset with an additional week:

```lua
{
  Type = "HelioviewerDownloadTask",
  Name = "SDO",
  SourceId = 10,
  Instrument = "AIA-171",
  ColorMap = openspace.absPath("${SYNC}/http/solarbrowsing/AIA-171.txt"),
  StartTime = "2024-05-13T00:00:00.000Z", -- continues from where we left off
  EndTime = "2024-05-20T00:00:00.000Z",
  TimeStep = 60 * 60,
  OutputFolder = "${SYNC_DYNAMIC}/solarbrowsing/sdo/aia-171" -- same folder as before
}
```

### Downloading Multiple Instruments
There are multiple instruments available for viewing. Each instrument requires its own task entry and its own `OutputFolder`. The time range and cadence do not need to be the same for different instruments. For example, to download SDO AIA-171 and AIA-193 over the same period:

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

:::{attention}
Each spacecraft and instrument combination requires its own `OutputFolder`.
:::

After running the task, the `sdo/` root directory will contain one subdirectory for each instrument, and both will be discovered automatically by the renderable.

### Adding a New Instrument
To add data for an instrument not included in the example task, you need to know its `SourceId` from the [Helioviewer API documentation](https://api.helioviewer.org/docs/v2/appendix/data_sources.html), and (optionally) have a color map file available for it, see [Color Maps](#color-maps) for additional info on the color map structure. Add a new entry to the task file with its own `OutputFolder`, and make sure to update the `Instrument` name.

:::{note}
The `Instrument` name and the `ColorMap` filename does not need to match, the task will automatically update the `ColorMap` file to match the `Instrument` name. This name is displayed in the `ActiveInstrument` dropdown menu in OpenSpace.
:::

(solarimagery_directory_structure_id)=
## Directory Structure
Images for each instrument must be stored in their own subdirectory. The `OutputFolder` in the task specifies this subdirectory. A typical layout for SDO with two instruments would look like:

```text
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

```text
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
