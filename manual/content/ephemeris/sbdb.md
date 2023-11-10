# SBDB
This page covers the basics of downloading orbital data for a solar system object in the proper format required by OpenSpace, and then configuring a renderable scenegraph node for it.

This method differs from the JPL Horizons [page](horizons-web) in that it provides parameters that describe the orbit of an object rather than its pre-computed coordinates. This SBDB method is best for objects that have stable, predictable orbits.

# Downloading Orbital Data from the JPL Small-Body Database (SBDB)
Browse to the JPL SBDB query page [here](https://ssd.jpl.nasa.gov/tools/sbdb_query.html) and follow the instructions for each input section below.

## Search Constraints
There are currently just under one million Small SolarSystem Bodies (SSSB) listed in this database. Attempting to render all of them at once would cause low rendering performance and result in "visualization overload," so some level of filtering is necessary.

Click the **Limit by Orbit Class** header to expand its contents. Sub-groups of asteroids and/or comets (e.g. main asteroid belt) can be selected. If desired, additional filtering can be applied using object characteristics such as size, orbital period, or inclination. Filters can be selected and combined with a logical AND/OR operation. This _advanced_ option is available under the **Custom Object/Orbit Constraints** header.

## Output Selection ##
Click the **Output Selection Controls** header to expand this section. Do not select "Output Field Preset Selector". In the "Available Fields" box, click each of the following options to select _only_ these:
- **[object fullname]**
- **[epoch_cal]**  epoch of osculation in Julian day form (TDB)
- **[e]** eccentricity
- **[a]** semi-major axis (au)
- **[i]** inclination; angle with respect to x-y ecliptic plane (deg)
- **[node]** longitude of the ascending node (deg)
- **[peri]** argument of perihelion (deg)
- **[M]** mean anomaly (deg)
- **[period (d)]** sidereal orbital period (d)

When all are selected, click the **add->** button to add them to the "Output Fields" box. Make sure that the order inside this box is exactly the same as listed above.

Finally, enable the "Full Precision" checkbox.

## Generate Output
Click "Get Results" button, and then the "Download (CSV-format)" button to save as a .csv file locally.

# Data Usage
This wiki covers the scenario where an asset file references a data file served by one of the OpenSpace sync servers. At runtime, the file will be downloaded if a local copy does not already exist. This requires the file generated in the above steps to be uploaded to an OpenSpace sync server by one of the project's server administrators.

For testing purposes, the file can be included in the asset by using the `localResource` method, but this is not discussed here.

# Create an Asset File
The following is an example from the `solarsystem/sssb/pha.asset` file that is currently included in the latest OpenSpace release. This asset renders the asteroids that have been flagged in the JPL database as being **A**steroids which are **P**otentially **H**azardous (PHA) to Earth.
```
local assetHelper = asset.require('util/asset_helper')
local sharedSssb = asset.require('./sssb_shared')

local filepath = sharedSssb.downloadSssbDatabaseFile(asset, 'pha', 'sssb_data_pha')
local object = sharedSssb.createSssbGroupObject("sssb_data_pha.csv", filepath, { 0.75, 0.2, 0.2 })
object.Renderable.Enabled = false

assetHelper.registerSceneGraphNodesAndExport(asset, { object })
```
The `util/asset_helper` file provides utilities and is included in almost all assets. The `sssb_shared` file provides the functionality necessary to configure the object in a format that can be interpreted by OpenSpace as a scenegraph node.

The `downloadSssbDatabaseFile` function sets up a reference to an HTTP-synchronized file which will be downloaded from the sync server mentioned previously. The 2nd argument is just a name, but the final argument needs to match the corresponding entry stored at the sync server. The `createSssbGroupObject` is also provided by the `sssb_shared` file, and it creates a Lua table in the format expected of a scenegraph node. The 1st argument is the exact filename that will be stored in the local sync folder as a result of the download step above. The final argument is the RGB color of its orbital trail.

In this example, the renderable will not be enabled by default, but can of course be enabled manually in the GUI or console. As the function name implies, the final call to `registerSceneGraphNodesAndExport` completes the process and registers this asset as a scenegraph node in OpenSpace.

# Add the Asset to OpenSpace
The final step is to simply add this asset to OpenSpace for rendering. This can be done by either:
1. Including the asset in a **.scene** file before starting OpenSpace:
`asset.require('scene/solarsystem/sssb/pha')`
2. Typing in the **\`** console while OpenSpace is running:
`openspace.asset.add('scene/solarsystem/sssb/pha')`
