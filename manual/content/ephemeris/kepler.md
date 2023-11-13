# Kepler Translation
In order to implement a Kepler Translation, you will need to obtain the following values:

Eccentricity, SemiMajorAxis, Inclination, AscendingNode, ArgumentOfPeriapsis, MeanAnomaly, Epoch, Period (values for this example were taken from here: [https://www.princeton.edu/~willman/planetary_systems/Sol/Pluto]( https://www.princeton.edu/~willman/planetary_systems/Sol/Pluto))

You will create an asset file to draw a trail, the trail will use the KeplerTranstion to decide where its points are. Once you have created the file, you will add the asset to OpenSpace.


## Create an Asset File
For this example, you will create a file and put it at `data/assets/keplertranslation.asset` in the OpenSpace directory structure. This asset file will create a renderable trail displaying the orbit.

```lua
--keplertranslationexample.asset
local assetHelper = asset.require('util/asset_helper')
local sunTransforms = asset.require('scene/solarsystem/sun/transforms')

local PlutoKeplerTrail = {
    Identifier = "PlutoKeplerTrail",
    Parent = sunTransforms.SolarSystemBarycenter.Identifier,
    Renderable = {
        Type = "RenderableTrailOrbit",
        Translation = {
            Type = "KeplerTranslation",
            Eccentricity = 0.24883,
            SemiMajorAxis = 5906438091.0,
            Inclination = 17.14001,
            AscendingNode = 110.30,
            ArgumentOfPeriapsis = 113.76,
            MeanAnomaly = 0.003973966,
            Epoch = "2000 01 01 00:00:00",
            Period = 7821583948.8,
        },
        Color = { 0.00, 0.62, 1.00 },
        Period = 7821583948.8,
        Resolution = 86000
    },
    GUI = {
        Name = "Pluto Kepler Trail",
        Path = "/Solar System/Dwarf Planets/Pluto"
    }
}

assetHelper.registerSceneGraphNodesAndExport(asset, { PlutoKeplerTrail })
```


## Add the Asset to OpenSpace
The final step is to simply add this asset to OpenSpace for rendering. This can be done by either:
  1. Including the asset in a **.scene** file before starting OpenSpace: `asset.require('keplertranslationexample')`
  1. Typing in the \` console while OpenSpace is running: `openspace.asset.add('keplertranslationexample')`
