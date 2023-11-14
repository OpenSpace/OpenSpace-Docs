# Satellites
This rendering code was created to visualize satellites in Earth's orbit. The precise position of each satellite above the Earth is rendered according to the date & time. The Two-Line Element set (TLE) file format is a standard for defining satellite orbital mechanics. It contains all of the necessary Keplerian elements to define an orbital path. When running the satellites module, OpenSpace reads all of the provided TLE files and generates a renderable for each entry.


## Automation
OpenSpace features like regular expressions and keyboard bindings can be used to automate control of satellite layers. Keyboard bindings can be added to an individual scene. For example, in the `preInitialization` function of the file `default.scene`, the following `bindkey` command can be added:
```lua
openspace.bindKey(
  "p",
  "openspace.setPropertyValue('stations_*.renderable.Enabled', false)",
  "Disable stations visibility"
)
```
The **\*** wildcard will apply the command to all renderables that meet the `stations_*` criteria in this case. Regular expression syntax can also be used. When running OpenSpace, press _p_ to make all station satellites invisible. Specific commands can also be entered in the terminal at runtime, without pre-configuring a scene file. Press **\`** to get a terminal at the top of the window, and type: `openspace.setPropertyValue('stations_*.renderable.Enabled', true)`, and then all satellites from the `stations.txt` TLE file will become visible again.


## Customizing the Satellites Module
When OpenSpace starts the satellites module, it tries to download `.tle` files that are specified in the `data/assets/scene/solarsystem/planets/earth/satellites/satellites.asset` file. At the top of this file, `satelliteGroups` contains a dictionary entry for each .tle file to be included in the visualization. Each file has a `title` for its description, a `url` for where to download the latest .tle file, and a `trailColor`. Further down in this file, the `UrlSynchronization` type is used to tell OpenSpace to download a copy from the URL specified (this is done for best orbital accuracy, since some satellite positions are updated often). After downloading, OpenSpace will open each file and read all of the satellite entries that it contains (two lines for each satellite TLE entry). For each TLE entry, OpenSpace computes the current orbital position and generates a renderable object. If a large number of satellites are listed, then the initialization time as well as the rendering performance may be negatively impacted.


## Adding new Satellite Data to OpenSpace
OpenSpace can render satellites that have a periodic orbit that is defined in the TLE format. To add a new data TLE source, a new .asset file can be created by using other similar files as inspiration. Setting the `url` field mentioned above to the online source for the data will prompt OpenSpace to download the file each time it starts.
For other types of solar system objects, such as asteroids, comets, or small solar system bodies, see some of the other [Ephemeris](ephemeris/index.md) wiki pages.


## Selectively Rendering Individual Satellites in a Group
The satellite rendering software groups satellites together by category, and any change to that category (e.g. visibility, trail color, trail length) affects all of them simultaneously.
There is an advanced method for limiting the satellites rendered within a group. By selecting Scene -> Solar System -> Planets -> Earth -> Satellites, the different satellite groups can be seen. Underneath a satellite group, expand the Renderable category to see slider controls for "Starting Index of Render" and "Size of Render Block". The Starting Index selects which satellite to start rendering (the previous satellites will be hidden), and the Size controls how many are rendered starting from the index. The size can be set to 1 or more satellites. When the Starting Index is set to a non-zero value, an info message containing the name & description of that satellite will be added to the OpenSpace log.html file.


## Satellite Data from Celestrak
The satellite data included in OpenSpace comes from service [Celestrak](https://celestrak.com/), and in particular their current data page: [https://celestrak.com/NORAD/elements/](https://celestrak.com/NORAD/elements/). On this page, you will find overall categories in **BOLD** and their sub cateories listed below them. Listed below are the OpenSpace assets files that correspond. Should you wish to include an entire category, there are asset files to include named *satellites_communications*, *satellites_debris*, etc. The OpenSpace category of **Misc** corresponds to the first Celestrak category 'Special-Interest Satellites'.


## Satellites in the 'default' Profile
Satellites in the default scene can be activated with the 's' hotkey, or the 'Toggle Satellites' shortcut. They can also be found in the Scene menu under {menuselection}`Solar System-->Planets-->Earth-->Satellites`. Below is a listing of the ones included in the default scene.

| Menu name | Celestrak category | Description |
| --- | ----------- | ------- |
| geo | Active Geosynchronous | Satellites that currently active and in a Geosynchronous orbit, meaning their orbital period matches Earth's rotation. |
| gps-ops | GPS Operational | The GPS satellites that give us our precise locations back here on Earth. |
| ISS | N/A | In this sub category you will find the model and the trail for the ISS. The trail for the ISS is the same data that can be found in the stations category. |
| stations | Space Stations | A collection of space stations (Including the ISS and China's Tiangong), along with certian cubesats and satellite constellations from space agencies. |
| tle-new | Last 30 Days' Launches | All the satellites that have been launched in the last 30 days. |
| visual | 100 (or so) Brightest | The 100 (or so) satellites that will appear brighest when viewed from Earth. |


## All Satellite Categories and Assets Included in OpenSpace
As mentioned above, satellites are grouped by categories and sub-categories that are created by CelesTrak.com. Below is a current listing of the ones included in OpenSpace:

### Communications
  - amateur
  - experimental
  - geostationary
  - globalstar
  - gorizont
  - intelsat
  - iridium
  - iridium_next
  - molniya
  - orbcomm
  - other_comm
  - raduga
  - ses

### Debris
  - debris_asat
  - debris_breezem
  - debris_fengyun
  - debris_iridium33
  - debris_kosmos2251

### Misc
  - brightest
  - cubesats
  - iss
  - military
  - other
  - radar
  - spacestations
  - tle-new

### Navigation
  - beidou
  - galileo
  - glosnass
  - gps
  - musson
  - nnss
  - sbas

### Science
  - education
  - engineering
  - geodetic
  - spaceearth

### Weather
  - argos
  - dmc
  - earth_resources
  - goes
  - noaa
  - planet
  - sarsat
  - spire
  - tdrss
  - weather
