# How to load a model into OpenSpace
To load a model into OpenSpace you will need to create a new asset file. To learn more about assets see [Assets](../../assets/assets), and load the model with this piece of code:
```lua
  ...
  local sun = asset.require('scene/solarsystem/sun/sun')

  Renderable = {
    Type = "RenderableModel",
    GeometryFile = modelPath .. "BoxAnimated.glb",
    LightSources = { sun.LightSource }
  }
  ...
```

The first line in this example imports the asset for the Sun, this is to add it as a light source to the model in the end. Then you add the `Renderable` with the `"RenderableModel"` as Type. Lastly, you define the path to the model file as the `GeometryFile`, for more information regarding paths in assets see [Resources](../../assets/resources). The line `modelPath .. "BoxAnimated.glb",` creates a path to your sync folder where the model is downloaded from our servers. If you want to add a local model file instead that is not located on our servers, then you could use the `localResource` function to create the path, like this (example with a local model file of New York City):
```lua
  GeometryFile = asset.localResource("nyc-model.obj"),
```

The `localResource` function here refers to a file that is located next to the asset file on the filesystem. If you want to reference a file on your computer that is not located directly next to the asset file, you can instead give the full path to that file like this:
```lua
  GeometryFile = "C:/Users/username/Documents/data/nyc-model.obj",
```

Note that the slashes in the path need to be forward slashed (`/`) and not backward slashes (`\`). There are additional properties you can set for your model, such as scale and animation, to read more about these see [Model Scale](scale), and [Animated Models](animation).


## Formats
OpenSpace uses the [Assimp library](https://github.com/assimp/assimp) to load models; therefore, our supported formats are similar to their supported formats. For a complete list see [List of formats](#list-of-formats) further down this page.


## Debugging your model
If your model does not show up in OpenSpace and you are sure that you have done everything right in the loading, there is a tool that you could use for debugging. In the asset file, you can add an optional property for forcing invisible pieces of the model to render. This forces any part of the model that is invisible (has no texture or color) to render. This property is called `ForceRenderInvisible`. Here is an example where it is used for the Juno spacecraft:
```lua
  ...
  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "Juno.obj",
    ForceRenderInvisible = true,
    ModelTransform = RotationMatrix,
    LightSources = { sun.LightSource }
  },
  ...
```

Any part of the model that is invisible will now be rendered with a bright and colorful pink and green chessboard pattern. This pattern will also be forced if OpenSpace encountered any Error while loading the material or texture for the model, even without the property. This could make it easier to identify errors with your model.

If this property is left out in the asset file and your model has invisible parts there will be an info message in the log making you aware that there might be something wrong with the model. However, just because a part of the model is invisible does not necessarily mean that something is wrong with the model. If you are aware that your model has invisible parts and want to suppress this info message you can set the property to false to keep the log cleaner.


## List of formats
Here is a list of supported formats in OpenSpace:

| Extension     | Name                                     | Comment                     |
| ------------- | ---------------------------------------- | --------------------------- |
| 3d, uc        | Unreal Mesh                              |                             |
| 3ds, prj      | 3ds Max 3DS                              | Limited support by Assimp   |
| 3mf           | 3D Manufacturing Format                  |                             |
| ac, acc, ac3d | AC3D                                     |                             |
| amf           | Additive manufacturing file format       | Limited support by Assimp   |
| ase, ask      | 3ds Max ASE                              |                             |
| assbin        | Assimp Binary                            |                             |
| b3d           | BlitzBasic 3D                            |                             |
| blend         | Blender 3D                               | Limited support by Assimp   |
| cob, scn      | TrueSpace                                | Limited support by Assimp   |
| dae, zae      | Collada                                  |                             |
| dxf           | AutoCAD DXF                              |                             |
| fbx           | Autodesk                                 |                             |
| gltf, glb     | glTF       | Export from Blender does not support specular texture maps |
| ifc, ifczip   | Industry Foundation Classes (IFC / Step) |                             |
| irr           | Irrlicht Scene                           |                             |
| irrmesh       | Irrlicht Mesh                            |                             |
| lwo           | LightWave                                |                             |
| lws, mot      | LightWave Scene                          |                             |
| lxo           | Modo                                     |                             |
| m3d           | Model 3D                                 |                             |
| md2           | Quake II Mesh                            |                             |
| md3           | Quake III Mesh                           |                             |
| md5anim, md5camera, md5mesh | Doom 3 / MD5 Mesh          |                             |
| mdc           | Return To Castle Wolfenstein Mesh        |                             |
| mdl           | Quake Mesh / 3D GameStudio Mesh          |                             |
| mesh, mesh.xml | Ogre3D Mesh                             |                             |
| ms3d          | Milkshape 3D                             |                             |
| ndo           | Nendo Mesh                               |                             |
| nff, enff     | Neutral File Format                      |                             |
| obj           | Wavefront Object                         | Limited support by Assimp   |
| off           | OFF                                      |                             |
| ogex          | Open Game Engine Exchange                |                             |
| osmodel       | OpenSpace binary model format            |                             |
| pk3, bsp      | Quake III BSP                            |                             |
| ply           | Stanford Polygon Library                 |                             |
| q3o, q3s      | Quick3D                                  |                             |
| raw           | Raw                                      |                             |
| sib           | Silo SIB                                 | Limited support by Assimp   |
| smd, vta      | Valve SMD                                |                             |
| stl           | Stereolithography | Mostly used for 3D printing, might not support colors or textures |
| x             | DirectX X                                |                             |
| x3d, x3db     | Extensible 3D                            | Limited support by Assimp   |
| xgl, zgl      | XGL                                      |                             |
