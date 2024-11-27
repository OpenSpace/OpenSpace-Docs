# Labels

Text labels can be added to the points to help identify what entity each point represents. For now, this is done using a separate [label file format](./data-formats.md#labels-label), but in the future it will be possible to generate these directly from a CSV file that is used to create a point dataset.

To add labels to your point cloud, add a Labels Component (`Labels`) to the table in the asset:

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    -- Add a component for drawing labels
    Labels = {
      -- Load the file with the label texts and positions
      File = asset.resource("path/to/labelsfile.label"),
      -- Labels are disabled per default
      Enabled = true
    }
  },
  ...
```

:::{admonition} Labels without points?
:class: note
The .label file is essentially standalone from the data file for the `RenderablePointCloud`. This means that it is possible to create a set of labels that is completely different compared to the points, or even create a set of labels without any points at all. To do so, just omit the `File` parameter
:::

## Unit

Similiarly to the data loading for the points, a specific unit can be used when interpreting the values in the .label file.

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Labels = {
      File = asset.resource("path/to/labelsfile.label"),
      Enabled = true,
      -- Note that the unit has to specified for the labels as well as
      -- for the data file
      Unit = "pc" -- short for "parsec"
    },
    -- Here we use the same unit for the points in the .csv files as for
    -- the ones in the .label file
    Unit = "pc" -- short for "parsec"
  },
  ...
```

## Appearance

It is also possible to modify the look of the labels, by increasing their size or color.

```lua
  ...
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("path/to/dataset.csv"),
    Labels = {
      File = asset.resource("path/to/labelsfile.label"),
      Enabled = true,
      -- This parameter can be used to control the size of the labels
      Size = 7.5,
      -- The labels can also be given a speicific color
      Color = { 0.0, 1.0, 0.0 }
    }
  },
  ...
```

(@TODO: Explain how size works, as well as the min and max size scaling... (Leave until after Labels rewrite))