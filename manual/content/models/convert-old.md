# Breaking change in 0.17.0: Model Loading
In release 0.17.0, the model loading in OpenSpace was updated to support models with multiple parts, materials, and textures. This update unfortunately means that previous asset files with models need to be updated.

Previously a model was specified in an asset file as a `Geometry` with a `Type`, `GeometryFile`, and a `ColorTexture`. Now it is just specified with a `GeometryFile`, there is no need for a `ColorTexture` since this information will be read from the model. This may mean that the models that have previously been used might need to be exchanged or updated to properly work with the new model loading system, more on that later.


## Examples
How the Renderable for the Juno spacecraft was specified before:
```lua
  ...
  Renderable = {
    Type = "RenderableModel",
    Geometry = {
      Type = "MultiModelGeometry",
      GeometryFile = model .. "/Juno.obj",
      ColorTexture =  textures .. "/gray.png"
    },
    ModelTransform = RotationMatrix,
    LightSources = assetHelper.getDefaultLightSources(sunTransforms.SolarSystemBarycenter.Identifier)
  },
  ...
```

How the Renderable for the Juno spacecraft is specified now:
```lua
  ...
  local sun = asset.require('scene/solarsystem/sun/sun')

  Renderable = {
    Type = "RenderableModel",
    GeometryFile = model .. "Juno.obj",
    ModelTransform = RotationMatrix,
    LightSources = { sun.LightSource }
  },
  ...
```


## RenderableModelProjection
This breaking change is also applied to the RenderableModelProjection. For example, in the Rosetta profile the model for 67P Churymov-Gerasimenkou was previously specified as:
```lua
  ...
  Renderable = {
    Type = "RenderableModelProjection",
    Geometry = {
      Type = "MultiModelGeometry",
      GeometryFile = models .. "/67P_rotated_5_130.obj",
      ColorTexture = textures .. "/gray.jpg"
    },
    Projection ...
  },
  ...
```

Now it is specified as:
```lua
  ...
  Renderable = {
    Type = "RenderableModelProjection",
    GeometryFile = models .. "67P_rotated_5_130.obj",
    Projection ...
  },
  ...
```


## Models
As you may have noticed there is no need to specify the ColorTexture as before. Instead, this information will be read from the model itself, which may mean that your old models need to be updated or exchanged. This depends very much on what kind of model you are using but in general, there are two different ways to update the old model:
  - Embed the material or texture in the model.
  - Define a material file (.mtl) and link it to your model.

Both of these could be done with any modeling software (such as Blender, Maya or 3ds Max). In both cases, you need to make sure that you export the model with the materials or textures. In the second case, you would get a material file (.mtl) that should be next to your model file. You can also do the second case manually as explained below.

### Create your own material file for your model
It is possible to create your own material file and connect your model to the correct textures by editing the files in a text editor. Depending on how complex and large your model is this could take some time and effort.
  1. Start by creating a new text file and rename its extension to .mtl instead of .txt (you might have to turn on visible file extensions in Windows for this).
  1. Open your model file and material file in a text editor (such as Notepad, Notepad++, or Visual Studio Code).
  1. In the model file, at the top you need to link the material file you just created with `mtllib filename.mtl` replacing the filename with the name of the material file you created in step 1.
  1. In the model file there should be a long list of data, go to the line where the data shifts to `f`. A tip is to use the search function that most text editors have with Ctrl + f and search for `f`. Right before the first line of `f` insert the line: `usemtl materialName`. This tells the model that this part of the model should have this material.
  1. If there are several different lists of `f` you repeat step 4 until all lists of `f` has a material. You can use different materials (change materialName) if you would like the different parts of the model to have different materials or textures.
  1. Your model file should look something like this at this point (example with two materials):
     ```
     # Header ..
     mtllib 0.mtl
     o 10_(ESP)_External_Stowage_Platform_1_z1_ext_01.000
     v 2.529284 -0.517977 3.555833
     v 2.559681 -0.517977 3.55583
     ..
     vn -0.6966 0.4229 0.5796
     vn -0.8944 0.2626 -0.3619
     s off
     usemtl ISS_03_dull
     f 246/1/1 247/2/1 248/3/1
     f 246/1/1 249/4/1 247/2/
     ..
     vn -0.3987 -0.5324 0.7467
     vn -0.7104 -0.4799 0.5148
     s 1
     usemtl white
     f 1216/1216/491 1217/1217/492 1218/1218/493
     f 1216/1216/491 1219/1219/494 1217/1217/49
     ...
     ```
  1. Switch to the material file. Here is where you define your materials and the textures. Create a new material with `newmtl materialName`. Note that materialName should be the same as you specified in the model file in Step 4. Then connect the material to a texture using: `map_Kd textureName.png`. Note that the path to the texture should be given relative to the material file.
  1. If you specified several **different** materials in step 5 you will need to repeat step 7 for every new material.
  1. In the end your material file should look something like this (with two materials):
     ```
     newmtl ISS_03_dull
         map_Kd 0.png

     newmtl white
         map_Kd white_20.png
     ```
  1. Make sure that your material file is in the same directory as the model file. Your model should now be textured in OpenSpace.
