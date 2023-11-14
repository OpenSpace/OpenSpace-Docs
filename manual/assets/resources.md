# Resources
## What are resources?
Resources are files that can be loaded as data into OpenSpace. A resource can for example consist of a movie, images, maps, positional data, etc. You can use two types of resources in OpenSpace:
  1. **Local resources**: Files that you have stored locally on your computer. For example, a movie in your `Documents` folder.
  1. **Synchronized resources**: Files that are stored on a server and downloaded when they are loaded into OpenSpace. For example, a map on our BigBang server.


## Local resources
To load a local resource into OpenSpace you need to tell OpenSpace where the file is located. You can do this in two different ways depending on if your file is located in the same folder as the asset.

The recommended method is to place the resource in the same folder as the asset as it makes it easier to share assets with others.

### If your resource is in the same folder as the asset
If your asset file and resource are in the same folder you can include the resource by writing `asset.localResource("filename.fileextension")`. In the example below, it would be:

```lua
asset.localResource("myVideo.mp4")
```

![An asset and a file in the same folder](asset_path.png)

Here is how the `video.asset` file above could load the video file `myVideo.mp4` in a video screen space renderable:

```lua
local ScreenSpace = {
  Identifier = "ScreenSpaceVideoExample",
  Type = "ScreenSpaceVideo",
  Name = "Screen Space Video Example",
  Video = asset.localResource("myVideo.mp4")
}


asset.onInitialize(function()
  openspace.addScreenSpaceRenderable(ScreenSpace)
end)

asset.onDeinitialize(function()
  openspace.removeScreenSpaceRenderable(ScreenSpace)
end)

asset.export(ScreenSpace)
```

### If your resource is not located in the same folder as the asset
To load a file that is located somewhere else than where your asset file is, you need to specify the **absolute path**. An absolute path tells the location of the file and usually starts with the name of the disk the file is located on, most commonly `C:/` or `D:/`. This is the absolute path for the movie in the image above:

```
"C:/Users/yourname/Desktop/Documents/myVideo.mp4"
```

To find the absolute path, you can copy the text in the search field in the file explorer and then add the filename. You can also right-click on the file and click `Properties`, which opens a window where the path should be displayed.
  1. The path must only contain forward slashes `/`, not backwards slashes `\`. If your path contains backward slashes, just change them to forward slashes.
  1. The path must be surrounded by quotation marks.

Here is an example of an asset where an absolute path is used for the `Video` property:

```lua
local ScreenSpace = {
  Identifier = "ScreenSpaceVideoExample",
  Type = "ScreenSpaceVideo",
  Name = "Screen Space Video Example",
  Video = "C:/Users/yourname/Desktop/Documents/myVideo.mp4"
}


asset.onInitialize(function()
  openspace.addScreenSpaceRenderable(ScreenSpace)
end)

asset.onDeinitialize(function()
  openspace.removeScreenSpaceRenderable(ScreenSpace)
end)

asset.export(ScreenSpace)
```


## Synchronized resources
There are two built-in mechanisms of resource synchronizations in OpenSpace: The `HttpSynchronization` and the `UrlSynchronization`. The `HttpSynchronization` is designed to fetch versioned data from the official OpenSpace server (data.openspaceproject.com), like this:

```lua
local path = asset.syncedResource({
    Type = "HttpSynchronization",
    Name = "Foo"
    Identifier = "foo",
    Version = 1
})
```

The UrlSynchronization can be used to fetch arbitrary data from the web.

```lua
local path = asset.syncedResource({
    Type = "UrlSynchronization",
    Name = "Bar",
    Identifier = "bar",
    Url = "http://example.com/data.zip",
    Override = true
})
```

While a synchronized asset can be required or requested from multiple locations, it can only declared in one location. For example, consider a synchronized asset that contains more than one file (e.g. `solarsystem/planets/jupiter/jupiter_labels.asset`). If the individual label files are used in different asset files, they must all reference the same source asset, and then append the label filename to the _jupiter_labels_ asset path. An error will occur if different synchronized assets are defined in order to request the individual label files.

The `Override` parameter can be used to force a new download even if the file has already previously been downloaded.
