# Create and display a "Water Moon"
The objective is to show all the volume of the water on Earth as a little "moon" right next to Earth. 
For this, we're going to create an asset. 
We could create a [renderable globe](/creating-data-assets/globebrowsing/creation/creating-a-renderableglobe) to do this, 
but we have a simpler way, using the [RenderableSphereImageLocal](/reference/asset-components/RenderableSphereImageLocal) asset component 
introduced in version 0.20.

In order to locate the newly created sphere at a chosen location near Earth, we can use the [GlobeTranslation](/reference/asset-components/GlobeTranslation) 
asset component. To load the texture, if we save the texture image (many such water textures are available for free online) as "watertexture.jpg" in the same directory as the asset file created below, 
we can use the [resource method](/creating-data-assets/asset-creation/resources) to render the texture on the sphere.

The whole thing can be put together as an asset file called for example **sphereonglobe.asset**, and saved under the user/data/assets directory of our OpenSpace installation, since all assets in that folder show up 
automatically in the asset selection part of profile editor, as seen below.
:::{figure} create-water-moon-asset-editor-screen.jpg 
The user asset shows up like this in the Profile Editor under Assets -- Edit
:::

The complete asset file can be as below. Please note the comments which are preceded by two dashes, like `--`.
```
local earth_asset = asset.require('scene/solarsystem/planets/earth/earth')

local Sphere1 = {
  Identifier = "Sphere1",
  Parent = earth_asset.Earth.Identifier,
  Transform = {
    -- A GlobeTranslation puts the sphere on the location on Earth you want it to be located.
    -- I have set the altitude to be the same as the size
    Translation = {
      Type = "GlobeTranslation",
      Globe = earth_asset.Earth.Identifier,
      Longitude = 16.188313,
      Latitude = 58.588455,
      Altitude = 100000 -- Put this to the same as the size to offset it from the surface
    }
  },
  Renderable = {
    Type = "RenderableSphereImageLocal",
    Size = 100000, -- The size you want the sphere to be (radius) in meter
    Segments = 80,
    Texture = asset.resource("watertexture.jpg"), -- asset.localResource is deprecated, we use asset.resource instead from 0.20 onwards
    Orientation = "Both"
  },
  GUI = {
    Name = "Sphere 1",
    Path = "/Earth Water/Spheres"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Sphere1)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Sphere1)
end)

asset.export(Sphere1)

```
Next, we can create a new profile by editing an existing profile, and add this asset to that profile as described in a separate tutorial. 
Or, we can also just drag and drop the asset file into OpenSpace once it is up and running, and make this asset show up as seen in the image below.
:::{figure} create-water-moon-openspace-screen.jpg 
After dragging and dropping the **sphereonglobe.asset** file into OpenSpace, the sphere is seen rendered
:::
