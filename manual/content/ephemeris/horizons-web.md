# Horizons Web
This covers the basics of downloading ephemeris data for a solar system object from JPL Horizons web page in the proper format for OpenSpace, and then configuring a renderable asset for it. This document only applies to an object in the solar system, using the Sun as the origin.

Since version 0.18.0 of OpenSpace, there is a feature to download Horizons data directly in the OpenSpace launcher, for more information check [Download Horizons data via OpenSpace](horizons-gui).

This method differs from the JPL Small SolarSystem Body Database ([SBDB page](sbdb)) in that it provides pre-computed coordinates in a specified time window. The SBDB method provides orbital characteristics that are used to compute the position without a time window restriction. Objects with irregular orbits must use this Horizons method.

## Downloading Ephemeris Data from JPL Horizons Site
Browse to the Horizons page (https://ssd.jpl.nasa.gov/horizons.cgi). Follow the instructions for each input section below.

### Ephemeris Type
Click the box to the right of the text and select **Vector Table** or **Observer Table**. OpenSpace supports both of these options but we recommend you to use **Vector Table**.

### Target Body
Click *edit* and enter the desired object identifier.

### Coordinate Center or Observer Location
Click *edit* and type `@0` in the text entry box. You should end up with `Solar System Barycenter (SSB) [500@0]`.

### Time Specification
Click *edit* and pick the time range you want. Note that these depend on the target, and an error may result if no data exists in the specified range.

### Table Settings
Click *edit* on **Table Settings**.

For the **Vector Table** format, the settings should be:

- Select Output Quantities = 1. Position components {x, y, z} only
- (None of the options for the __Statistical Uncertainties__ should be checked)

For the optional settings at the bottom, use the following:

- Reference frame = ICRF
- Reference plane = ecliptic x-y plane derived from reference frame (standard obliquity, inertial)
- Vector correction = geometric states
- Output units = km and seconds
- Vector labels = disabled
- Output TDB-UT = disabled
- CSV format = disabled
- Object summary = enabled

For the **Observer Table** format, only the following checkboxes should be selected:
```
20. Observer range & range-rate
33. Galactic longitude & latitude
```
For the optional settings at the bottom, use the following:

- date/time format = calendar date/time
- time digits = HH:MM:SS
- angle format = decimal degrees
- output units = km & km/s
- range units = kilometers
- refraction model = none
- (no values for the 5 cutoff variables)
- suppress range-rate = enabled
- skip daylight = disabled
- extra precision = disabled
- RTS flag = disable
- reference system = ICRF/J2000.0
- CSV format = disabled
- object page = enabled

### Generate Output
Finally, click on the **Generate Ephemeris** button to get the ephemeris data in text format. Then click the button **Download Results** and save it to a **.hrz** file.

## Examine Downloaded Output
Examine the .hrz file and verify that it is valid. If it only contains the header but no space-delimited lines of data, then there should be an error message explaining the problem. For example, this will happen if the start/end dates are beyond the valid time range of the target object.

## Data Usage
This wiki covers the scenario where an asset file references a data file served by one of the OpenSpace sync servers. At runtime, the file will be downloaded if a local copy does not already exist. This requires the file generated in the steps above to be uploaded to an OpenSpace sync server by one of the project's server administrators.

For testing purposes, the file can be included in the asset by using the `localResource` method, but this is not discussed here (however the [builders/asteroids](asteroids) page contains an example using this method).

## Create an Asset File
The following is an example asset file of the interstellar object 'Oumuamua. This file is located at **data/assets/scene/solarsystem/interstellar/oumuamua.asset** in the OpenSpace directory structure. This asset file will create a node (not renderable) for the position of the object, and a renderable trail.
```
local sunTransforms = asset.require("scene/solarsystem/sun/transforms")

local trajectory = asset.syncedResource({
  Name = "'Oumuamua Trajectory",
  Type = "HttpSynchronization",
  Identifier = "oumuamua_horizons",
  Version = 2
})

local OumuamuaTrail = {
  Identifier = "OumuamuaTrail",
  Parent = sunTransforms.SolarSystemBarycenter.Identifier,
  Renderable = {
    Type = "RenderableTrailTrajectory",
    Translation = {
      Type = "HorizonsTranslation",
      HorizonsTextFile = trajectory .. "horizons_oumuamua.hrz"
    },
    Color = { 0.9, 0.9, 0.0 },
    StartTime = "2014 JAN 01 00:00:00",
    EndTime = "2050 JAN 01 00:00:00",
    SampleInterval = 86400,
    TimeStampSubsampleFactor = 1
  },
  GUI = {
    Name = "'Oumuamua Trail",
    Path = "/Solar System/Interstellar"
  }
}

local OumuamuaPosition = {
  Identifier = "OumuamuaPosition",
  Parent = sunTransforms.SolarSystemBarycenter.Identifier,
  Transform = {
    Translation = {
      Type = "HorizonsTranslation",
      HorizonsTextFile = trajectory .. "horizons_oumuamua.hrz"
    },
  },
  GUI = {
    Name = "'Oumuamua",
    Path = "/Solar System/Interstellar"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(OumuamuaPosition)
  openspace.addSceneGraphNode(OumuamuaTrail)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(OumuamuaTrail)
  openspace.removeSceneGraphNode(OumuamuaPosition)
end)

asset.export(OumuamuaPosition)
asset.export(OumuamuaTrail)
```
In this example, the position and trail use the sun's barycenter (from `sunTransforms`) as the parent observer. The Horizons data file is included here as an `HttpSynchronization` synced resource with the `trajectory` variable. The translation type is `HorizonsTranslation` which requires a `HorizonsTextFile` to be specified using the `trajectory` path from the asset mentioned above. The renderable trail has a start & end time, with a `SampleInterval` value that divides the time range into a number of segments.

## Add the Asset to OpenSpace
The final step is to simply add this asset to OpenSpace for rendering. This can be done by either:
1. Including the asset in a **.profile** file before starting OpenSpace. The easiest way to do this is to use the profile editor in the launcher when starting OpenSpace.
2. Typing in the \` console while OpenSpace is running:
`openspace.asset.add("scene/solarsystem/interstellar/oumuamua")`
