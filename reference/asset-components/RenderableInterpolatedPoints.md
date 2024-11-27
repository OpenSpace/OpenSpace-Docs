



(base_renderableinterpolatedpoints)=
# RenderableInterpolatedPoints

_Inherits [Renderable](#renderable)_

RenderableInterpolatedPoints is a version of the RenderablePointCloud class, where the dataset may contain multiple time steps that can be interpolated between. It supports interpolation of both of positions and data values used for color mapping or size.

The dataset should be structured in a way so that the first N rows correspond to the first set of positions for the objects, the next N rows to the second set of positions, and so on. The number of objects in the dataset must be specified in the asset.

MultiTexture: Note that if using multiple textures for the points based on values in the dataset, the used texture will be decided based on the first N set of points.


## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `NumberOfObjects`
    - The number of objects to read from the dataset. Every N:th datapoint will be interpreted as the same point, but at a different step in the interpolation.
    - `Integer`
    
    - Greater or equal to: 1 
    
    - {bdg-info}`No`
    
*   - `Coloring`
    - Settings related to the coloring of the points, such as a fixed color, color map, etc.
    - `Table`
    
    -   [Table parameters](#RenderableInterpolatedPointsColoring-target) 
    
    - Yes
    
*   - `DataMapping`
    - A dictionary specifying details on how to load the dataset. Updating the data mapping will lead to a new cached version of the dataset.
    - `Table`
    
    - [DataMapping](#dataloader_datamapping)
    
    - Yes
    
*   - `DrawElements`
    - Enables/Disables the drawing of the points.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Fading`
    - Settings related to fading based on camera distance. Can be used to either fade away or fade in the points when reaching a certain distance from the origin of the dataset.
    - `Table`
    
    -   [Table parameters](#RenderableInterpolatedPointsFading-target) 
    
    - Yes
    
*   - `File`
    - The path to the data file that contains information about the point to be rendered. Can be either a CSV or SPECK file.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `Interpolation`
    - Initial settings for the interpolation.
    - `Table`
    
    -   [Table parameters](#RenderableInterpolatedPointsInterpolation-target) 
    
    - Yes
    
*   - `Labels`
    - The labels for the points. If no label file is provided, the labels will be created to match the points in the data file. For a CSV file, you should then specify which column is the 'Name' column in the data mapping. For SPECK files the labels are created from the comment at the end of each line.
    - `Table`
    
    - [LabelsComponent](#labelscomponent)
    
    - Yes
    
*   - `OrientationRenderOption`
    - Controls how the planes for the points will be oriented. "Camera View Direction" rotates the points so that the plane is orthogonal to the viewing direction of the camera (useful for planar displays), and "Camera Position Normal" rotates the points towards the position of the camera (useful for spherical displays, like dome theaters). In both these cases the points will be billboarded towards the camera. In contrast, "Fixed Rotation" does not rotate the points at all based on the camera and should be used when the dataset contains orientation information for the points.
    - `String`
    
    - In list { Camera View Direction, Camera Position Normal, Fixed Rotation } 
    
    - Yes
    
*   - `SizeSettings`
    - Settings related to the scale of the points, whether they should limit to a certain max size, etc.
    - `Table`
    
    -   [Table parameters](#RenderableInterpolatedPointsSizeSettings-target) 
    
    - Yes
    
*   - `SkipFirstDataPoint`
    - If true, skip the first data point in the loaded dataset.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Texture`
    - Settings related to the texturing of the points.
    - `Table`
    
    -   [Table parameters](#RenderableInterpolatedPointsTexture-target) 
    
    - Yes
    
*   - `TransformationMatrix`
    - Transformation matrix to be applied to the position of each object.
    - `Matrix4x4<double>`
    
    - Value of type 'Matrix4x4<double>' 
    
    - Yes
    
*   - `Unit`
    - The unit used for all distances. Should match the unit of any distances/positions in the data files.
    - `String`
    
    - In list { m, Km, pc, Kpc, Mpc, Gpc, Gly } 
    
    - Yes
    
*   - `UseAdditiveBlending`
    - If true (default), the color of points rendered on top of each other is blended additively, resulting in a brighter color where points overlap. If false, no such blending will take place and the color of the point will not be modified by blending. Note that this may lead to weird behaviors when the points are rendered with transparency.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseCaching`
    - If true (default), the loaded dataset and color map will be cached so that they can be loaded faster at a later time. This does however mean that any updates to the values in the dataset will not lead to changes in the rendering without first removing the cached file. Set it to false to disable caching. This can be useful for example when working on importing a new dataset or when making changes to the color map.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseOrientationData`
    - If true, the orientation data in the dataset is included when rendering the points, if there is any. To see the rotation, you also need to set the "Orientation Render Option" to "Fixed Rotation".
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



### Inherited members from [Renderable](#renderable)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `DimInAtmosphere`
    - Decides if the object should be dimmed (i.e. faded out) when the camera is in the sunny part of an atmosphere.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - Determines whether this object will be visible or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of this renderable. A value of 0 means completely transparent
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `RenderBinMode`
    - A value that specifies if the renderable should be rendered in the Background, Opaque, Pre-/PostDeferredTransparency, Overlay, or Sticker rendering step.
    - `String`
    
    - In list { Background, Opaque, PreDeferredTransparent, PostDeferredTransparent, Overlay } 
    
    - Yes
    
*   - `Tag`
    - A single tag or a list of tags that this renderable will respond to when setting properties
    - `Table, or String`
    
    - Value of type 'Table', or Value of type 'String' 
    
    - Yes
    
*   - `Type`
    - The type of the renderable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::








(RenderableInterpolatedPointsColoring-target)=
::::{dropdown} Table parameters for `Coloring`
Settings related to the coloring of the points, such as a fixed color, color map, etc.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `ApplyColorMapToOutline`
    - If true and the outline is enabled, the color map will be applied to the outline rather than the point body. Only works if color mapping is enabled.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ColorMapping`
    - Settings related to the choice of color map, parameters, etc.
    - `Table`
    
    - [ColorMappingComponent](#colormappingcomponent)
    
    - Yes
    
*   - `EnableOutline`
    - Determines whether each point should have an outline or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FixedColor`
    - The color of the points, when no color map is used.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `OutlineColor`
    - The color of the outline. Darker colors will be less visible if "Additive Blending" is enabled.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `OutlineStyle`
    - Decides the style of the outline (round, square, or a line at the bottom). The style also affects the shape of the points.
    - `String`
    
    - In list { Round, Square, Bottom } 
    
    - Yes
    
*   - `OutlineWidth`
    - The thickness of the outline, given as a value relative to the size of the point. A value of 0 will not show any outline, while a value of 1 will cover the whole point.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



::::








(RenderableInterpolatedPointsFading-target)=
::::{dropdown} Table parameters for `Fading`
Settings related to fading based on camera distance. Can be used to either fade away or fade in the points when reaching a certain distance from the origin of the dataset.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Enabled`
    - Enables/disables the Fade-in effect based on camera distance. Automatically set to true if FadeInDistances are specified in the asset.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeInDistances`
    - Determines the initial and final distances from the origin of the dataset at which the points will start and end fading-in. The distances are specified in the same unit as the points, that is, the one provodied as the Unit, or meters. With normal fading the points are fully visible once the camera is outside this range and fully invisible when inside the range. With inverted fading the case is the opposite: the points are visible inside when closer than the min value of the range and invisible when further away.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `Invert`
    - If true, inverts the fading so that the points are invisible when the camera is further away than the max fade distance and fully visible when it is closer than the min distance.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



::::






(RenderableInterpolatedPointsInterpolation-target)=
::::{dropdown} Table parameters for `Interpolation`
Initial settings for the interpolation.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Speed`
    - Affects how long the interpolation takes when triggered using one of the trigger properties. A value of 1 means that a step takes 1 second.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `UseSplineInterpolation`
    - If true, the points will be interpolated using a Catmull-Rom spline instead of linearly. This leads to a smoother transition at the breakpoints, i.e. between each step.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Value`
    - The value used for interpolation. The max value is set from the number of steps in the dataset, so a step of one corresponds to one step in the dataset and values in-between will be determined using interpolation.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



::::








(RenderableInterpolatedPointsSizeSettings-target)=
::::{dropdown} Table parameters for `SizeSettings`
Settings related to the scale of the points, whether they should limit to a certain max size, etc.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `EnableMaxSizeControl`
    - If true, the Max Size property will be used as an upper limit for the size of the point. This reduces the size of the points when approaching them, so that they stick to a maximum visual size depending on the Max Size value.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MaxSize`
    - Controls the maximum allowed size for the points, when the max size control feature is enabled. This limits the visual size of the points based on the distance to the camera. The larger the value, the larger the points may be. In the background, the computations are made by limiting the size to a certain angle based on the field of view of the camera. So a value of 1 limits the point size to take up a maximum of one degree of the view space.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ScaleExponent`
    - An exponential scale value used to set the absolute size of the point. In general, the larger distance the dataset covers, the larger this value should be. If not included, it is computed based on the maximum positional component of the data points. This is useful for showing the dataset at all, but you will likely want to change it to something that looks good. Note that a scale exponent of 0 leads to the points having a diameter of 1 meter, i.e. no exponential scaling.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ScaleFactor`
    - A multiplicative factor used to adjust the size of the points, after the exponential scaling and any max size control effects. Simply just increases or decreases the visual size of the points.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `SizeMapping`
    - Settings related to scaling the points based on data.
    - `Table`
    
    - [SizeMappingComponent](#base_sizemappingcomponent)
    
    - Yes
    
:::



::::






(RenderableInterpolatedPointsTexture-target)=
::::{dropdown} Table parameters for `Texture`
Settings related to the texturing of the points.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `AllowCompression`
    - If true, the textures will be compressed to preserve graphics card memory. This is enabled per default, but may lead to visible artefacts for certain images, especially up close. Set this to false to disable any hardware compression of the textures, and represent each color channel with 8 bits.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - If true, use a provided sprite texture to render the point. If false, draw the points using the default point shape.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `File`
    - The path to the texture of the point sprite. Note that if multiple textures option is set in the asset, by providing a texture folder, this value will be ignored.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `Folder`
    - The folder where the textures are located when using multiple different textures to render the points. Setting this value means that multiple textures shall be used and any single sprite texture file is ignored.  Note that the textures can be any format, but rendering efficiency will be best if using textures with the exact same resolution.
    - `Directory`
    
    - Value of type 'Directory' 
    
    - Yes
    
*   - `UseAlphaChannel`
    - If true, include transparency information in the loaded textures, if there is any. If false, all loaded textures will be converted to RGB format. 
This setting can be used if you have textures with transparency, but do not need the transparency information. This may be the case when using additive blending, for example. Converting the files to RGB on load may then reduce the memory footprint and/or lead to some optimization in terms of rendering speed.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



::::














## Asset Examples


:::{dropdown} Basic

This example creates a point cloud that supports interpolation. The dataset is split
up into 10 objects, so that every tenth row represents a new position for an item at a
step in the interpolation.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 14

local Node = {
  Identifier = "RenderableInterpolatedPoints_Example",
  Renderable = {
    Type = "RenderableInterpolatedPoints",
    -- The dataset here is just a linearly expanding dataset, where the points move in
    -- a straight line
    File = asset.resource("data/interpolation_expand.csv"),
    -- Specify how many objects the rows in the dataset represent. Here, the dataset is
    -- consists of 10 objects with positions at 6 different time steps. This information
    -- is required
    NumberOfObjects = 10
  },
  GUI = {
    Name = "RenderableInterpolatedPoints - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::



:::{dropdown} Smoother Interpolation (Spline-based)

Example of interpolating points with spline-based interpolation for the position. This
leads to smoother transitions at the nodes of the interpolation.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 21

local Node = {
  Identifier = "RenderableInterpolatedPoints_Example_Spline",
  Renderable = {
    Type = "RenderableInterpolatedPoints",
    -- Using a random walk dataset, to get movement in some different directions
    File = asset.resource("data/interpolation_randomwalk.csv"),
    -- Specify how many objects the rows in the dataset represent. Here, the dataset is
    -- consists of 10 objects with positions at 6 different time steps
    NumberOfObjects = 10,
    Interpolation = {
      -- Smoothen transitions between two different sets of points, by
      -- using a spline based interpolation of the points
      UseSplineInterpolation = true
    },
    -- Reduce the scale of the points a bit compared to default, so we see them more clearly
    SizeSettings = {
      ScaleExponent = 3.0
    }
  },
  GUI = {
    Name = "RenderableInterpolatedPoints - Spline",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::



:::{dropdown} Interpolated Points with Color Mapping

Example of interpolating points with a color map. The data value used for the coloring
will also be interpolated, leading to the points changing color throughout the
interpolation.
Note that the color map is loaded from another asset. This is a utility asset that
includes some common color maps for general usage.

:::{code-block} lua
:linenos:
:emphasize-lines: 6, 25

local colormaps = asset.require("util/default_colormaps")

local Node = {
  Identifier = "RenderableInterpolatedPoints_Example_ColorMapped",
  Renderable = {
    Type = "RenderableInterpolatedPoints",
    -- The dataset here is just a linearly expanding dataset, where the points move in
    -- a straight line
    File = asset.resource("data/interpolation_expand.csv"),
    -- Specify how many objects the rows in the dataset represent. Here, the dataset is
    -- consists of 10 objects with positions at 6 different time steps
    NumberOfObjects = 10,
    Coloring = {
      ColorMapping = {
        -- For this example, we are using one of the example colormaps "Viridis"
        File = colormaps.Uniform.Viridis
      }
    },
    -- Reduce the scale of the points a bit compared to default, so we see them more clearly
    SizeSettings = {
      ScaleExponent = 3.5
    }
  },
  GUI = {
    Name = "RenderableInterpolatedPoints - Color Mapped",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
end)

:::
:::


