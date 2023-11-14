# Solar Video Overlay
This page discusses how to overlay a plane containing a coronal video with the sun's position. The steps here could be used for any video plane positioning, with a variety of orientations and scales.


## Source of Corona Video
This example uses a video obtained by the Solar Dynamics Observatory (SDO). A coronal video for August 21, 2017 was obtained from [this page](https://sdo.gsfc.nasa.gov/assets/img/dailymov/2017/08/21/), because it aligned with an eclipse on that date. The file 20170821_1024_0171.mp4 was selected for this example because of its corona quality.


## Create an Asset File for the Coronoa Video
The following example asset file was placed in the data/assets/scene/solarsystem/sun directory. It requires the transforms.asset file, which is referenced in the first line.

Since the video plane is centered with the sun renderable globe, its translation is zero. In order to orient the video plane toward Earth, a `StaticRotation` is applied. The pi/2 x-axis rotation orients it perpendicular to the ecliptic plane, and the 0.45 radian z-axis rotation orients it at Earth for this particular day. The `StaticScale` value was obtained by trial-and-error in order to make the sun's size in the video match the sun renderable globe (and the `RenderableVideoPlane` size).

Since the video is only valid for one day, the `StartTime` and `EndTime` values are set accordingly. In addition, the script scheduler is used to make the video plane visible only on August 21, 2017 (see the `onInitialize` section near the end of the file). These scripts make the video plane appear only during this day, regardless of which direction the time may be adjusted.

```lua
local transforms = asset.require("./transforms")

local Plane = {
  Identifier = "CoronaVideoPlane",
  Parent = transforms.SunIAU.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = { 0.0, 0.0, 0.0 }
    },
    Rotation = {
      Type = "StaticRotation",
      Rotation = { 1.57, 0.0, 0.45 }
    },
    Scale = {
      Type = "StaticScale",
      Scale = 30.3
    }
  },
  Renderable = {
    Type = "RenderableVideoPlane",
    MirrorBackside = true,
    Size = 3E7,
    Video = asset.localResource("20170821_1024_0171.mp4")
  },
  GUI = {
    Name = "Sun Corona",
    Path = "/Solar System/Sun"
  },
  StartTime = "2017 AUG 21 00:00:00",
  EndTime = "2017 AUG 21 23:59:59"
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Plane)
  openspace.scriptScheduler.loadScheduledScript(
    "2017 AUG 21 00:00:00",
    [[openspace.setPropertyValueSingle("Scene.CoronaVideoPlane.Renderable.Enabled", true)]],
    [[openspace.setPropertyValueSingle("Scene.CoronaVideoPlane.Renderable.Enabled", false)]]
  )
  openspace.scriptScheduler.loadScheduledScript(
    "2017 AUG 21 23:59:59",
    [[openspace.setPropertyValueSingle("Scene.CoronaVideoPlane.Renderable.Enabled", false)]],
    [[openspace.setPropertyValueSingle("Scene.CoronaVideoPlane.Renderable.Enabled", true)]]
  )
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Plane)
end)

asset.export(Plane)

asset.meta = {
  Name = "Corona 2017-08-21",
  Version = "1.0",
  Description = "Sun image 2017-08-21",
}
```


## Add the Downloaded Video File
The mp4 video file can be placed in the same directory as the asset file, or a relative path can be added to the reference line if it is placed elsewhere.


## Create a Profile With The Corona Asset
Use the profile editor in the OpenSpace launcher to create a new profile, click the Asset Edit button, search for the name of the asset that was created in the steps above, and check the box to add it to the profile.
