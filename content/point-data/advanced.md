# Advanced Rendering

This page includes some more advanced rendering concepts for the `RenderablePointCloud` renderable type, and its [specializations](/content/point-data/point-data.md#specializations-of-renderablepointcloud). For the basics on settings, options, and custimizations when rendering point datasets, see the page on [Rendering Point Data](/content/point-data/point-data.md).

## Using Multiple Textures

@TODO

## Orientation From Data

When using the `Fixed Rotation` [orientation option](/content/point-data/point-data.md#orientation) for rendering the points, the orientation per point may be read from the dataset. In that case, the points are no longer rendered based on the position of the camera, but on a specified orientation per point. This can be useful when rendering objects that are given as just 3D positions, but which should be represented as 3D planes with a certain rotation. For example, the images for the galaxies in the Tully dataset of Digital Universe are rendered using this method.

Below is an example of what parameters must be specified in the asset file to render points based on orientation data in the dataset. In addition, the data file must of course also include this orientation information. More about this in the next section.

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
```
datavar 0 a_variable
datavar 1 another_variable
datavar 2 orientation
polyorivar 2
-0.006 0.001 -0.005 0.0 55 -0.735 -0.074 0.673 0.677 -0.081 0.731
91.451 5.958 70.563 2.8 12 -0.735 -0.074 0.673 0.677 -0.081 0.731
85.169 5.465 36.676 2.8 20 -0.370 0.650 -0.660 -0.840 -0.540 -0.060
```

As per the [SPECK](./data-formats.md#speck-speck) format definition, the first three values always give the position of the point (XYZ). Next follows two arbitrary data values, and then the orientation, which is given as six values that specify the two XYZ vectors for the orientation of the plane. The vectors should be orthogonal. In the exmaple above, the two first points have the same orientation, and the third point has another. Importantly, the `polyorivar` line specifies which `datavar` index corresponds to the orientation data. This is required for the orientation values to be read correctly.
