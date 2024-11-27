# Advanced Rendering
This page includes some more advanced rendering concepts for the `RenderablePointCloud` renderable type and its [specializations](./point-data.md#specializations-of-renderablepointcloud). For the basics on settings, options, and customizations when rendering point datasets, see the page on [Rendering Point Data](./point-data.md).

## Using Multiple Textures
Most commonly, we want to use one texture, or sprite, for all the points in a dataset. More about how to do this on [this page](./point-data.md#adding-a-texture). However, it is also possible to use multiple textures and map which one is used for which point using a column in the dataset.

To add multiple textures to a point cloud, the dataset must include a mapping of image names to a number that can be added to each data point. All the images should be located in the same folder, or the name has to be specified as a path relative to a specific folder. You also need to provide information about which column in the dataset corresponds to the texture index for the point, as well as a location for where the textures are located on disk. How to do this depends on whether the dataset is loaded from a CSV file or SPECK file.

The sections below cover how to load multiple textures from the data when using SPECK or CSV, respectively.

:::{note}
The `Texture` entry in the asset when using multiple textures looks very similar to [adding a single texture](./point-data.md#adding-a-texture), but here a `Folder` is specified instead of a `File`. By specifying a folder, the renderable will automatically be set to multi-texture mode, and any single file will be ignored.
:::

:::{note}
Note that while the path to a single texture can be edited during runtime, this is not possible when using multiple textures.
:::

### Texture data - SPECK
In a [SPECK](./data-formats.md#speck-speck) file, all the information can be included in one single file - the SPECK file itself. The texture mapping is done by adding lines starting with `texture`, followed by the texture index and texture name. In addition, we need to specify which of the `datavar` variables corresponds to the texture index for each data point. This is done by adding a line starting with `texturevar`, followed by the index of the `datavar`. See example below.

```{code-block}
---
emphasize-lines: 4, 5-8
---
datavar 0 a_variable
datavar 1 another_variable
datavar 2 texture
texturevar 2 # The index of the data column with the texture data (here, "texture")
texture 0 texture1.jpg
texture 1 texture2.png
texture 2 texture3.jpg

13428000 26239000 45870000 -3.226548224 33.95773276 0
14727000 45282000 10832000 45.05941924 -106.0395917 2
24999000 28370000 19911000 -70.58906931 154.1851656 0
26539000 36165000 39582000 -13.3663358  71.79484733 1
```

In this example, the texture index is added as the final data column on each line.

In the asset, we need to specify where the texture files are located. This is done by providing a `Folder` in the `Texture` section of the Renderable, as shown below. All the other information needed is included in the SPECK file.

```{code-block} lua
---
emphasize-lines: 8
---
...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.speck"),
    Texture = {
      -- When using multiple textures, we need to specify the folder where the textures
      -- are located. But all the other information is in the SPECK file.
      Folder = openspace.absPath("path/to/folder")
    }
  }
...
```

:::{note}
The `openspace.absPath` call is needed if you want to use path tokens (like `${USER}` for files in the user folder) when specifying the path to the folder. Alternatively, you may also use `asset.resource` for specifying a relative path to a folder (e.g. `"../images"` if the folder is located on level up in the file system).
:::

### Texture data - CSV
When using a CSV file, the texture mapping is done in a separate [texture map (.tmap)](./data-formats.md#texture-map-tmap) file. Below is an example of a CSV data file and a texture map file. The final column in the CSV file contains the index of the data file, which should match the ones in the texture map.

```
x,y,z,a,b,texture
13428000,26239000,45870000,-3.226548224,33.95773276,1
14727000,45282000,10832000,45.05941924,-106.0395917,0
24999000,28370000,19911000,-70.58906931,154.1851656,2
26539000,36165000,39582000,-13.3663358,71.79484733,0
```

```{literalinclude} example_texturemap.tmap
```

The mapping to which column in the data file specifies the texture index is done in the asset, in addition to the location of the folder with the textures. We also need to provide the location of the texture map file. Both the texture column and the path to the texture map file is added in the `DataMapping` section, as shown in the example below.

```{code-block} lua
---
emphasize-lines: 8, 11, 15
---
...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    DataMapping = {
      -- The name of the column in the CSV file that corresponds to the texture (should
      -- be an integer)
      TextureColumn = "texture",
      -- A texture mapping file that provides information about what value/index
      -- corresponds to which texture file
      TextureMapFile = asset.resource("path/to/texturemap.tmap")
    },
    Texture = {
      -- Where to find the texture files
      Folder = openspace.absPath("path/to/folder")
    }
  }
...
```

### About texture formats
Compared to rendering a point cloud with a single texture, using multiple different textures leads to some overhead time in rendering. This is especially the case if textures of multiple different texture formats are used. The reason for this is that all textures of each format (including resolution and whether the texture has three or four color channels) are bundled together and each bundle is handled in a separate rendering pass, as illustrated in the image below. That means that the more different types of texture formats, the more render passes are needed to render all the points, and the larger the rendering overhead will be.

:::{figure} multiple_textures.svg
:align: center
:width: 600px
Textures with the same resolution will be bundled together into one render pass. The fewer bundles, the better the rendering speed will be.
:::

:::{admonition} Tip - Minimize the number of render calls!
To reduce the number of render calls needed for your point cloud, make sure to use textures with as few different texture formats as possible. Using one single format, that is, the same pixel resolution and number of color channels, for all images will lead to only one single render call.
:::

## Orientation From Data
When using the `Fixed Rotation` [orientation option](./point-data.md#orientation) for rendering the points, the orientation per point may be read from the dataset. In that case, the points are no longer rendered based on the position of the camera, but on a specified orientation per point. This can be useful when rendering objects that are given as just 3D positions, but which should be represented as 3D planes with a certain rotation. For example, the images for the galaxies in the Tully dataset of Digital Universe are rendered using this method.

Below is an example of what parameters must be specified in the asset file to render points based on orientation data in the dataset. In addition, the data file must, of course, also include this orientation information. More about this in the next section.

```{code-block} lua
---
emphasize-lines: 6, 9
---
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.speck"),
    -- Use fixed orientation, i.e. do not rotate based on where the camera is
    OrientationRenderOption = "Fixed Rotation",
    -- We must also specify that we are to use any orientation data that is in
    -- the dataset. This is not done by default
    UseOrientationData = true
  },
  ...
```

### Loading the orientation data
The orientation per point is given as six values that specify the desired orientation of the plane. These values represent two 3D vectors (XYZ) that together span up the plane for the point. For now, the orientation-from-data feature is only supported when using [SPECK](./data-formats.md#speck-speck) files and SPECK files with orientation have a custom format for specifying the vectors that give the orientation per point.

:::{figure} orientation_fromdata.svg
:align: center
:width: 300px
The orientation per point is given as two vectors that decide how the plane is oriented.
:::

Below is an example of a short SPECK file with orientation data:
```{code-block}
---
emphasize-lines: 4
---
datavar 0 a_variable
datavar 1 another_variable
datavar 2 orientation
polyorivar 2 # The index of the data column that has the orientation data

-0.006 0.001 -0.005 0.0 55 -0.735 -0.074 0.673 0.677 -0.081 0.731
91.451 5.958 70.563 2.8 12 -0.735 -0.074 0.673 0.677 -0.081 0.731
85.169 5.465 36.676 2.8 20 -0.370 0.650 -0.660 -0.840 -0.540 -0.060
```

As per the [SPECK](./data-formats.md#speck-speck) format definition, the first three values always give the position of the point (XYZ). Next follow two arbitrary data values, and then the orientation, which is given as six values that specify the two XYZ vectors for the orientation of the plane. The vectors should be orthogonal. In the exmaple above, the two first points have the same orientation, and the third point has another. Importantly, the `polyorivar` line specifies which `datavar` index corresponds to the orientation data. This is required for the orientation values to be read correctly.
