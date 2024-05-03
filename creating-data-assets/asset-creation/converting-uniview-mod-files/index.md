# Uniview Mod File Conversion

As an example on the Tesla in space module
  1. Starting with tesla.mod file
  1. Creating tesla.asset
     1. Specifying local files we later need. By specifying with `localResource`, we put them in the same folder as the asset file and don't need to put them on a server anywhere
        ```lua
        local kernel = asset.localResource("tesla.bsp")
        local model = asset.localResource("tesla.obj")
        local texture = asset.localResource("white.jpg")
        ```
  1. Converting
     ```
     coord
     {
       name tesla
       parent SolarSystem

       unit 1000000.0
       unitname 1000 Km
       entrydist 10
       positionfile modules/tesla/teslapos.conf
       orbitfile modules/tesla/teslaorbit.conf
       positionhook tesla
     }
     ```
     1. `teslapos.conf` mentions the spice information which is converted into
     1. `teslaOrbit.conf` contains information about the orbit
     1. First we create a coordinate system for the Tesla (this can be merged with the model as well)
     1. Then a *Trail object. In this case, because we have a start and end time, we use a `RenderableTrailTrajectory` rather than `RenderableTrailOrbit`
        ```lua
        local TeslaPosition = {
          -- Name is arbitrary
          Name = "Tesla Position",
          -- Parent uses the asset.require to retrieve the name from another asset file
          Parent = transforms.SolarSystemBarycenter.Name,
          -- Values for this come from the original file
          Transform = {
            Translation = {
              Type = "SpiceTranslation",
              Target = "-143205",
              Observer = "SUN",
              Kernels = kernel
            }
          },
          -- GuiPath is an arbitrary string that is only used in the user interface to build a tree
          GuiPath = "/Solar System/Tesla"
        }

        local TeslaTrail = {
          Name = "Tesla Trail",
          Parent = transforms.SolarSystemBarycenter.Name,
          Renderable = {
            Type = "RenderableTrailTrajectory",
            Translation = {
              Type = "SpiceTranslation",
              Target = "-143205",
              Observer = "SUN",
              Kernels = kernel
            },
            Color = { 1.0, 0.6, 0.2 },
            StartTime = "2018 02 07 02:46:00",
            EndTime = "2030 01 01 23:59:59",
            SampleInterval = 60 * 60 * 24 -- One sample every day
          },
          GuiPath = "/Solar System/Tesla"
        }
        ```
      1. Ignoring (not sure why it is needed for Uniview
         ```
         coord
         {
          name teslasmC
          parent tesla

          unit 1.0
          unitname 1 m
          entrydist 500

         }
         ```
      1. Converting
         ```
         object tesla sgOrbitalObject
         {
           coord teslasmC
           geometry SG_USES teslaMesh.conf

           cameraradius 0.40
           targetradius 140
           scale 0.33
           lsize 1000000
           align earth 1 0 0

           off

           guiName /Solar System/Satellites/Tesla
         }
         ```
         into
         ```lua
         local TeslaModel = {
           Name = "Tesla",
           Parent = TeslaPosition.Name,
           Renderable = {
             Type = "RenderableModel",
             Geometry = {
               Type = "MultiModelGeometry",
               GeometryFile = model
             },
             ColorTexture = texture
           },
           GuiPath = "/Solar System/Tesla"
         }
         ```
         Unfortunately, we don't support multiple textures or MTL files yet (or at least I don't know how to use the latter), so we have to use a pure white texture.
      1. Exporting assets to the outside world:
         ```lua
         local objects = { TeslaPosition, TeslaTrail, TeslaModel }
         assetHelper.registerSceneGraphNodesAndExport(asset, objects)
         ```
