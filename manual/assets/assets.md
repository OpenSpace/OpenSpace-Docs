# Assets
In OpenSpace, Assets are modular components used to populate the scene and provide configurations. Assets can declare dependencies on other assets, which let them form a directed acyclic graph. Furthermore, assets can declare dependencies on external resources, that can be stored in the local filesystem or downloaded from the internet. An asset may represent a planet, a trail of a spacecraft, a volumetric dataset, a set of keybindings, or any other component that can be added and removed from an OpenSpace scene using the Lua API. Assets may also represent more abstract building blocks, such as invisible scene graph nodes used as reference coordinate frames, or Lua functions that can be reused by other assets.

Assets are written in Lua and have access to all OpenSpace Lua scripting functions. One asset file corresponds to exactly one asset and has the suffix `.asset`.


## Asset lifecycle
When OpenSpace loads, a _root-level asset_ will be loaded according to the `Asset` setting in `openspace.cfg`. Typically, the scene asset refers to several other assets, which in turn reference others. Additional root-level assets can be added while OpenSpace is running using the Lua command `openspace.asset.add(<path to asset>)`. Assets can be removed by calling `openspace.asset.remove(<path to asset>)`. Only root-level assets may be removed using this method, while assets that are dependencies of other root-level will be automatically deinitialized when the last referencing root-level asset is removed.

An asset that is imported into OpenSpace goes through a sequence of states: _Loading_, _Synchronization_, _Initialization_ and _Deinitialization_.

### Loading
When an asset is loaded, the asset file's Lua code is executed. The method `asset.require` may be used to declare dependencies on other assets, stating that they should be loaded first.

The asset may register resource synchronizations using `asset.syncedResource` and provide functions to be executed upon asset initialization (`asset.onInitialize`) and deinitialization (`asset.onDeinitialize`). The loading step itself should not manipulate the OpenSpace scene in any way. Instead, it should register any such logic with the `asset.onInitialize` and `asset.onDeinitialize` methods. If an asset is loaded successfully it will transition to the `Synchronizing` state.

### Synchronization
OpenSpace will asynchronously download resources from the internet based on specifications passed into `asset.syncedResource`. If the synchronization succeeds for the asset and all its dependencies, it will be marked as ready to transition to the Initialization phase. See the page [Resources](./resources) for examples using `syncedResource`.

### Initialization
Once an asset's synchronization is done the asset can be initialized. This involves calling all functions passed into `asset.onInitialize`, in the order they were registered. OpenSpace guarantees that all required child assets are initialized before the parent asset starts initializing. Typically the initialization includes adding scene graph nodes to the scene, adding dashboard components, binding keyboard shortcuts, etc.

### Deinitialization
When an asset is deinitialized, all functions passed to `asset.onDeinitialize` are executed in reversed order. Required child assets are guaranteed to be deinitialized after their parent asset. The deinitialization step typically removes scene graph nodes, removes dashboard items or unbinds keyboard shortcuts.


## Simple Example
The following asset file instructs OpenSpace to create a sphere with [NASA's Blue Marble texture](https://visibleearth.nasa.gov/view.php?id=74092) and add it to the scene:

```lua
-- example_sphere.asset

-- Define a synchronized resource to be downloaded before the asset can be initialized
local blueMarbleFolder = asset.syncedResource({
  Type = "UrlSynchronization",
  Name = "Blue Marble July Texture",
  Identifier = "blueMarbleJulyTexture",
  Url = "http://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74092/world.200407.3x5400x2700.jpg",
})

-- Create a scene graph node representing a textured sphere
local Sphere = {
  Identifier = "ExampleSphere",
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = { 10, 0, 0 }
    }
  },
  Renderable = {
    Type = "RenderableSphere",
    Enabled = true,
    Size = 1,
    Segments = 80,
    Opacity = 1,
    Texture = blueMarbleFolder .. "/world.200407.3x5400x2700.jpg",
    Orientation = "Both"
  },
  GUI = {
    Name = "Test Sphere",
    Path = "/Other/Spheres"
  }
}

-- Add the scene graph node when this asset is initialized
asset.onInitialize(function ()
  openspace.addSceneGraphNode(Sphere)
end)

-- Remove the scene graph node when this asset is deinitialized
asset.onDeinitialize(function ()
  openspace.removeSceneGraphNode(Sphere);
end)

-- Export the table, so it can be referenced in other assets
asset.export("ExampleSphere", Sphere);
```

Other assets can now import the `sphere` specification, like so:

```lua
local sphereAsset = asset.require("./example_sphere")
asset.onInitialize(function ()
  -- Do something with the result from the imported asset
  openspace.printDebug("Imported " .. sphereAsset.ExampleSphere.GUI.Name .. " into the scene")
end)

```

More examples can be found in `${BASE}/data/assets/examples`.


## Asset API Reference
OpenSpace provides lua APIs for managing assets within a running OpenSpace instance, as well as defining the assets themselves and declaring resource synchronizations.

### Managing assets
Assets can be added and removed at runtime using the Lua API in OpenSpace.

`void      openspace.asset.add(string path)`
Adds the asset located at the path to the current scene as a root-level asset.

`void      openspace.asset.remove(string path)`
Removes the asset located at the path from the scene. The asset will only be removed as a root-level asset; if it is also declared as a dependency of some other root-level asset, it will remain in the scene until that root-level asset is removed.

### Defining assets
Asset files have access to a special `asset` object that represents the current asset. The `asset` object is only valid during the loading phase, and exposes the following methods:

`table      asset.require(string path)`
Declares a dependency on another asset. Paths are specified without the `.asset` suffix. Paths starting with `/` or a drive letter are treated as absolute paths. Paths beginning with `./` or `../` are treated as relative to the current asset file. Paths starting with a directory name or file name are relative to the asset root directory, which is typically `${BASE}/data/assets` (configurable in `openspace.cfg`).
The method returns a table of the exports provided by the required asset, such as scene graph node specifications or Lua functions.

`void      asset.onInitialize(void() initializationFunction)`
Registers a lua function to be executed when the asset is initialized. This method may be called several times to register several callbacks. The functions will be called in the same order as they were registered.

`void      asset.onDeinitialize(void() deinitializationFunction)`
Registers a lua function to be executed when the asset is deinitialized. This method may be called several times to register several callbacks. The functions will be called in the reverse order as they were registered.

`string    asset.syncedResource(table syncSpecification)`
Declares a data resource to be synchronized before the asset can be initialized. This includes downloading data from the official OpenSpace server (data.openspaceproject.com), but can also be used to make arbitrary HTTP requests. The data is downloaded to the sync folder (typically `${BASE}/sync` but can be changed in `openspace.cfg`). The method returns the absolute path to the folder of the downloaded resource. Valid inputs are tables representing `ResourceSynchronization`s documented in more detail on the [Resources](./resources) page.

`string    asset.localResource(string relativePath)`
Declares a data resource already located on disk. The input to the function is a path relative to the asset file and the function returns the absolute path to that resource.

`void      asset.export(string key, any value)`
Export any data structure to other assets that require this asset. For example, assets that adds scene graph nodes upon initialization can export the identifiers of the scene graph nodes, so that other assets can reference these scene graph nodes. Furthermore, functions can be exported, allowing assets to behave more like software modules.
