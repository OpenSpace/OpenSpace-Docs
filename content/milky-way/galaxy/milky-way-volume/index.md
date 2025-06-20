---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Milky Way Volume

{menuselection}`Scene --> Milky Way --> Galaxy --> Milky Way Volume`


::::::{tab-set}
:::::{tab-item} Overview

## Overview

While a two-dimensional [Milky Way Image](../milky-way-image/index) of the Galaxy can be useful for seeing data sets within the context of the Galaxy, the Milky Way Galaxy is, of course, a massive, three-dimensional entity, so it would be nice to see its dimensionality here to compare its scale with other objects in the universe and have a more realistic depiction of the Galaxy.


### Perspective Problem

We have one small problem in showing the Milky Way galaxy in 3-D. We---all of us Earthlings---are stuck _inside_ the Galaxy. For that reason, we cannot know exactly what the Galaxy looks like. Scientists continue to debate the structure of the Galaxy, what the arms look like, the shape of the central bar, and even how many arms the Galaxy has.

This presents problems, as you might imagine, when it comes time to construct a scientifically accurate model of the Milky Way.


:::{figure} milky_way_model_edgeon.png
:align: left
:alt: The three-dimensional Milky Way Galaxy model

The three-dimensional model of the Milky Way Galaxy. Looking toward the center, along the Galaxy's disk, we see the gas elements, the stars in the disk, and some of the arm structure.
:::


### Building a Model

The model in OpenSpace was developed by Jon Parker for the American Museum of Natural History's [_Dark Universe_](https://www.amnh.org/global-business-development/planetarium-content/dark-universe) Space Show. This was a pre-rendered show (a video), so the model needed to be adapted for real-time use in OpenSpace. But, before that, we needed a scientific basis for modeling the Galaxy.

The team collaborated with scientists at the [National Astronomical Observatory of Japan](https://www.nao.ac.jp/en/) (NAOJ), who conduct research on the structure and dynamics of galaxies. Specifically, they modeled the gas dynamics of a 3-D galaxy using an [_N_-body](https://en.wikipedia.org/wiki/N-body_simulation#Direct_gravitational_N-body_simulations) plus [hydrodynamical](https://en.wikipedia.org/wiki/Fluid_dynamics) simulation with the hope of reproducing the overall structure of the Galaxy, as well as the clumpiness seen in the gas distribution within the Galaxy. Their model accounted for the gravitational potential, star formation, dark matter, and other factors that determine the nature of the Galaxy.



:::{figure} milky_way_model_faceon_composite.png
:align: left
:alt: A two-panel image of the Milky Way Galaxy in OpenSpace. On the left is the Milky Way Volume model and on the right is the volumetric model and the Milky Way Image.

The Milky Way Galaxy Volume in OpenSpace. The left panel shows only the volumetric model, while the right panel shows the volumetric model and the [Milky Way Galaxy Image](../milky-way-image/index). From this view, it is clear the two assets complement one another nicely, and should typically be shown together.
:::


### Display Options

The Milky Way Volume has specific options that can be accessed via its [renderable settings](/reference/asset-components/Renderable/RenderableGalaxy). These options, specified in its asset file (below), control the look and quality of the volumentric model rendering in OpenSpace. These can be adjusted if the model is too detailed for your system, or not detailed enough. There is also the option to enable or disable star rendering within the model.

:::{dropdown} Asset File

:::{code-block} lua
local transforms = asset.require("scene/solarsystem/sun/transforms")



local data = asset.resource({
  Name = "Milkyway Volume Data",
  Type = "HttpSynchronization",
  Identifier = "milkyway_volume_data",
  Version = 1
})


local KiloParsec = 3.086E19

local MilkyWayVolume = {
  Identifier = "MilkyWayVolume",
  Parent = transforms.SolarSystemBarycenter.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      -- The center of the Milky Way is approximately 8 kiloparsec from the Sun.
      -- The x-axis of galactic coordinates points from the sun towards the center
      -- of the galaxy.
      Position = { 8 * KiloParsec, 0, 0 }
    }
  },
  Renderable = {
    Type = "RenderableGalaxy",
    StepSize = 0.01,
    AbsorptionMultiply = 200,
    EmissionMultiply = 250,
    Rotation = { math.pi, 3.1248, 4.45741 },
    Volume = {
      Type = "Volume",
      Filename = data .. "MilkyWayRGBAVolume1024x1024x128.raw",
      Dimensions = { 1024, 1024, 128 },
      Size = { 1.2E21, 1.2E21, 0.15E21 },
      Downscale = 0.4
    },
    Points = {
      Type = "Points",
      Filename = data .. "MilkyWayPoints.off",
      EnabledPointsRatio = 0.3,
      Texture = data .. "halo.png"
    }
  },
  GUI = {
    Path = "/Milky Way/Galaxy",
    Name = "Milky Way Volume",
    Description = "Volumetric rendering of Milky Way galaxy based on simulation from NAOJ"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(MilkyWayVolume)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(MilkyWayVolume)
end)

asset.export(MilkyWayVolume)



asset.meta = {
  Name = "Milky Way Volume",
  Description = "Volumetric rendering of Milky Way galaxy based on simulations from NAOJ",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT License"
}
:::

:::
:::::


:::::{tab-item} Profiles

## Profiles

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} [](/profiles/default/index)
[![default profile](/profiles/default/profile_default_icon.png)](/profiles/default/index)
:::


:::{grid-item-card} [](/profiles/default-full/index)
[![default-full profile](/profiles/default-full/profile_default_full_icon.png)](/profiles/default-full/index)
:::


:::{grid-item-card} [](/profiles/offline/index)
[![offline profile](/profiles/offline/profile_offline_icon.png)](/profiles/offline/index)
:::
::::

:::::


:::::{tab-item} Dossier

## Dossier

:::{dossier}
:census: 1 volumetric model
:assetfile: data/assets/scene/milkyway/milkyway/volume.asset
:openspaceversion: 1
:preparedby: Jon Parker, Emil Axelsson, Carter Emmart, OpenSpace Team
:sourceversion: 1.0
:license: mit
:reference: On the Interpretation of the _l_ − _v_ Features in the Milky Way Galaxy=https://doi.org/10.48550/arXiv.1009.3096
:::

:::::
::::::
