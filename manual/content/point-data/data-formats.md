# File Formats

Below are descriptions of some data formats that are relevant to point clouds and point datasets.

## CSV
The most straightforward way data format to use for point cloud rendering is probably the CSV format. These files can essentially be loaded without any modification, but there are some expectations as to the format of the file:

- Unless alternative column names have been specified in the [Data Mapping](./point-data.md#data-mapping) for the point cloud, the CSV file must have a column for the x-, y- and z-coordinate, named `x`, `y` and `z`, respectively.

- For now, only numeric data values are supported. Any string-based values will be converted to a number when possible, and otherwise interpreted as a missing data value.

```
x,y,z,aVariable,anotherVariable
70.8,-18.7,-13.3,1,242.5
346.3,-417.3,149.9,0,1834.2
41.1,-544.2,50.8,3,1786.9
...
```

## SPECK (.speck)
The SPECK file format is an OpenSpace-specific format, initially created to represent objects in the [Digital Universe Atlas](https://www.amnh.org/research/hayden-planetarium/digital-universe). It is a plain text format that is easily editable by humans and is parsed in a line-by-line format.

A simple example of a SPECK file that represents a set of points may look like this
```
# Some kind of descriptive comment or maybe a license.
# Whatever you want can be included in this comment here at the top, really

datavar 0 aVariable
datavar 1 anotherVariable
70.8 -18.7 -13.3 1 242.5 # Point 1
346.3 -417.3 149.9 0 1834.2 # Point 2
41.1 -544.2 50.8 3 1786.9 # Point 3
...
```
where the lines starting with `datavar` specify data parameters in the file and the name, including an index. Following those, each line represents one data point:
- The first three values correspond to the position of the point (X, Y, Z).
- The following numbers are values for the provided data variables, in order according to the index. The number of values shall match the number of data variables (so, in total the number of numeric values is `3 + number of datavar`).
- Finally, at the end is an optional comment that may be used to provide more information about the object. Everything after the `#` is parsed into this comment.

## Labels (.label)
Label files are similar to SPECK files, but used specifically to provide positions and text for labels that can be placed in 3D space, using for example a `RenderablePointCloud`. See more details on how to add labels for a point cloud on the [Labels page](./labels.md).

The number of labels and their positions may match the points in the dataset, but they also may not. The number of labels can be more or fewer than the number of points, and the position can be different compared to that of the points if desired. It is also possible to not have any point at all, just labels.

The format of a .label file looks like this:
```
# An optional comment
# That can be multiple lines

70.8 -18.7 -13.3 text The label - Point 1
346.3 -417.3 149.9 text The label - Point 2
41.1 -544.2 50.8 text And Point 3
...
```

Like SPECK files, the first three values correspond to the 3D position (X, Y, Z). After that is a `text` key, which signals that the text that follows is the one to use for the label.
<!--
It is also possible to add an identifier for each label, that can be utilized to .... **@TODO Explain mapping to alternative files for labels text**
```
# A .label file with an identifier per label

70.8 -18.7 -13.3 id Label1 text The label - Point 1
346.3 -417.3 149.9 id Label2 text The label - Point 2
41.1 -544.2 50.8 id Label3 text And Point 3
...
``` -->

## Color Maps (.cmap)

For color maps, we use a specific format that is similar to that of the .label and .speck files, but every line defines a color rather than a position.

The file starts with an integer number specifying the number of colors in the color map, followed by one line per color. The colors are given by four values, for the Red, Green, Blue and Alpha. Below is an example of a color map with three colors.

```
# An optional comment
# That can be multiple lines

3
0.0 1.0 0.0 1.0  # Color 1 (green)
0.2 0.6 1.0 1.0  # Color 2 (blue)
1.0 1.0 0.0 1.0  # Color 3 (yellow)
```
Anything that is added after the expected value per line (such as the comments marked with `#` above) will be ignored. The colors are interpreted increasingly, so that the first color will be mapped to the first value in the value range and the last color to the second value.

It is also possible to specify colors to use for missing data values (NaN) as well as values below or above the value range that the color mapping is done based on.
This is done by marking lines with `nan`, `belowRange`, or `aboveRange`, before specifying to color to use for that case. These colors should not be counted as one of the colors in the color map, i.e. not towards the number on the first line in the file.

```
# A color map with specific colors for NaN values and values outside the
# specified range

2
belowRange 1.0 1.0 0.0 1.0  # (yellow)
0.0 1.0 0.0 1.0  # Color 1 (green)
0.0 0.2 1.0 1.0  # Color 2 (blue)
aboveRange 1.0 0.0 1.0 1.0  # (magenta)
nan 0.3 0.3 0.3 0.5  # (transparent gray)
```
Note that the exact position of the lines with the `nan`, `belowRange`, or `aboveRange` keys in the file does not matter.