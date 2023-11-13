# Asteroids
This page covers the more advanced topics of asteroid/comet visualization. OpenSpace has a wide range of data for such objects, but the instructions here can be used to add newly-available data, or a custom-selected set of data.


## Adding New Asteroid or Comet Data to OpenSpace
### Download the New Data from the JPL Small-Body Database (SBDB)
The existing SBDB [wiki](sbdb) covers the steps for selecting and downloading the data. Once this procedure is complete and the data has been downloaded, copy the file to **data/assets/scene/solarsystem/sssb/**, and continue the steps below.

### Create an Asset File for the Data
Create a new .asset file in **data/assets/scene/solarsystem/sssb/** using the following template. Provide information specific to the downloaded object(s) in the <bracketed> fields:

```lua
local assetHelper = asset.require('util/asset_helper')
local sharedSssb = asset.require('./sssb_shared')

local filepath = asset.localResource("./")
local object = sharedSssb.createSssbGroupObject('<downloaded filename>.csv', "<Name of object(s)>", filepath, { 1.0, 1.0, 1.0 })
object.Renderable.Enabled = true
object.Renderable.SegmentQuality = 7
object.Renderable.TrailFade = 10

assetHelper.registerSceneGraphNodesAndExport(asset, { object })

asset.meta = {
    Name = "<Name of object(s)>",
    Version = "1.0",
    Description = [[ <Your description for object(s)> ]],
    Author = "JPL Small-Body Database hosted by California Institute of Technology",
    URL = "https://ssd.jpl.nasa.gov/sbdb_query.cgi",
    License = "JPL-authored documents are sponsored by NASA under Contract NAS7-030010. All documents available from this server may be protected under the U.S. and Foreign Copyright Laws."
}
```
This example contains default rendering settings (color, segment quality, fade, etc). Sections below discuss how to modify these settings.
Please note that this example uses a local downloaded file (here in the same directory as the asset file), rather than a file synchronized from one of the OpenSpace sync servers. Existing files in the `sssb/` directory use this method (refer to them for the syntax of using `HttpSynchronization`). If you would like to add this new data to the OpenSpace sync servers, contact the team [here](https://www.openspaceproject.com/support).

### Add the Asset to a Scene or Profile
When starting OpenSpace, the Launcher window will appear first. You can either create a new profile, or edit an existing profile in the list. With either method, the profile editor window will appear. Modify the Profile Name at the top if desired. Click the Edit button of the Assets section, and then scroll through the directory navigation list to find the new asset file. Click the checkbox to enable this asset and then press the Save button. Finally, press the Save button back in the Profile editor to save the profile and then run OpenSpace with it.

### Start OpenSpace and Find the New Content in the Menu
Start OpenSpace, and open the Scene menu. The added data can be found by expanding the *Solar System -> Small Bodies* menu. The example above enables the visibility (*Renderable.Enabled*) by default, so it should have an enabled checkbox.


## Selective Rendering of Asteroids
Expanding a particular asteroid/comet object in the menu shows additional controls under the *Renderable* category. A few of the options:

### Reducing the Total Number of Rendered Objects in a Group

Some groupings contain thousands of objects which can slow the rendering. The *Upper Limit* option can be used to reduce the number of objects while retaining the overall shape of the group. For example, the main asteroid belt contains almost a million asteroids. Setting *Upper Limit* to 10,000 will make OpenSpace render every 100th object in the main belt file, providing an even sampling (rendering only the first 10,000 objects could skew the visualization because some data files are sorted).

### Rendering a Subset of the Objects in a Group
A contiguous subset of a group can be rendered by changing the *Starting Index of Render* and *Size of Render Block* parameters. The first selects where in the group the rendering starts, and the second controls how many objects are rendered starting from there.


## Trail Rendering Settings
### Changing Trail Color and Opacity
Change the red, green, and blue slider values under *Renderable --> Appearances --> Color* to modify the trail color. Reduce the *Renderable --> Opacity* slider value to make the trails more transparent.

### Changing Trail Length
Under *Renderable --> Appearances*, the *Line fade* parameter can be adjusted to change how much of the total orbital trail is displayed. Setting this to the maximum will display the entire elliptical orbit. The results will differ with this adjustment because the amount of trail fade is proportional to the total orbital path, and some asteroids/comets have much longer paths than others.
