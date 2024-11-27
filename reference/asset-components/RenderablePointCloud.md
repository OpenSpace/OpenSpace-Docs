



(base_renderablepointcloud)=
# RenderablePointCloud

_Inherits [Renderable](#renderable)_

A RenderablePointCloud can be used to render point-based datasets in 3D space, optionally including color mapping, a sprite texture and labels. There are several properties that affect the visuals of the points, such as settings for scaling, fading, sprite texture, color mapping and whether the colors of overlapping points should be blended additively or not.

The points are rendered as planes whose size depends on a few different things:

- At the core, scaling is done based on an exponential value, the `ScaleExponent`. A relatively small change to this value will lead to a large change in size. When no exponent is set, one will be created based on the coordinates in the dataset. The points will be visible, but may be appeared as too large or small. One option is to not specify the exponent when loading the dataset for the the, first time, to make sure the points are visual, and then adapt the value interactively when OpenSpace is running until you find a value that you find suitable.

- There is also an option to limit the size of the points based on a given max size value.

- And an option to scale the points based on a data value (see `SizeMapping` in `SizeSettings`)

- To easily change the visual size of the points, the multiplicative `ScaleFactor` may be used. A value of 2 makes the points twice as large, visually, compared to 1.


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

*   - `Coloring`
    - Settings related to the coloring of the points, such as a fixed color, color map, etc.
    - `Table`
    
    -   [Table parameters](#RenderablePointCloudColoring-target) 
    
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
    
    -   [Table parameters](#RenderablePointCloudFading-target) 
    
    - Yes
    
*   - `File`
    - The path to the data file that contains information about the point to be rendered. Can be either a CSV or SPECK file.
    - `File`
    
    - Value of type 'File' 
    
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
    
    -   [Table parameters](#RenderablePointCloudSizeSettings-target) 
    
    - Yes
    
*   - `SkipFirstDataPoint`
    - If true, skip the first data point in the loaded dataset.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Texture`
    - Settings related to the texturing of the points.
    - `Table`
    
    -   [Table parameters](#RenderablePointCloudTexture-target) 
    
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






(RenderablePointCloudColoring-target)=
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








(RenderablePointCloudFading-target)=
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










(RenderablePointCloudSizeSettings-target)=
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






(RenderablePointCloudTexture-target)=
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


:::{dropdown} Color Mapping with Pre-set Options and Missing Values

This example creates a point cloud where the color is set from a color map and the
options for parameters to color by are pre-set to a limited number of options,
including settings for which range to use. It also includes settings to render
missing data values in gray.
Note that the color map is loaded from another asset. This is a utility asset that
includes some common color maps for general usage.

:::{code-block} lua
:linenos:
:emphasize-lines: 6, 28

local colormaps = asset.require("util/default_colormaps")

local Node = {
  Identifier = "RenderablePointCloud_Example_ColorMapped_More",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      ColorMapping = {
        File = colormaps.Uniform.Viridis,
        -- Specify which parameters we want to show up in the user interface, as
        -- well as what range we want the color mapping to be done based on. If not
        -- included, all the columns in the data file would be exposed as options
        ParameterOptions = {
          { Key = "number_withNan" }, -- No range => compute min and max
          { Key = "normaldist_withMissing", Range = { -0.5, 0.5 } }
        },
        -- Also show missing data values in a specific color
        ShowMissingData = true,
        NoDataColor = { 0.5, 0.5, 0.5, 1.0 }
      }
    },
    SizeSettings = {
      ScaleExponent = 6.5
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Color Mapped with Settings",
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



:::{dropdown} Orientation - Face Camera Position

This example creates a point cloud where the planes that make up the points are
oriented to face the camera position, rather than the view direction (which is
default). This means that the point will be layed out in a spherical way around the
camera, which works better for spherical displays compared to the default
orientation.
A texture is added so that we can more easily see how the orientation is altered.
See Textured example for more details.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 16

local Node = {
  Identifier = "RenderablePointCloud_Example_FaceCameraPosition",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    -- Change the orientation render option to face the camera position instead
    -- of its view direction
    OrientationRenderOption = "Camera Position Normal",
    -- Add a texture so we can more easily see how the orientation is changed
    Texture = {
      File = openspace.absPath("${DATA}/test3.jpg")
    },
    UseAdditiveBlending = false
  },
  GUI = {
    Name = "RenderablePointCloud - Face Camera Position",
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



:::{dropdown} Textured

This example creates a point cloud using a texture to render each point.
Note that other color related settings, like color mapping, can still be applied.
The color will then be multiplied with the texture color.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 19

local Node = {
  Identifier = "RenderablePointCloud_Example_Textured",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Texture = {
      -- The path to the texture file. Here we use openspace.absPath so that we can use
      -- the ${DATA} token to get the path to a texture in the "OpenSpace/data" folder,
      -- but for a file at a relative location it would also work to use asset.resource,
      -- like for the data file above
      File = openspace.absPath("${DATA}/test3.jpg")
    },
    -- Disable additive blending, so that points will be rendered with their actual color
    -- and overlapping points will be sorted by depth. This works best when the points
    -- have an opacity of 1
    UseAdditiveBlending = false
  },
  GUI = {
    Name = "RenderablePointCloud - Textured",
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



:::{dropdown} Limit Max Size

This example creates a point cloud where the size of the points is limited to a
given max size. The color is set to a fixed value.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 17

local Node = {
  Identifier = "RenderablePointCloud_Example_MaxSize",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      FixedColor = { 0.0, 0.8, 0.8 }
    },
    -- Set the max size of the points. The larger the "MaxSize" value, the larger the
    -- points are allowed to get when moving the camera closer to them
    SizeSettings = {
      MaxSize = 0.7,
      EnableMaxSizeControl = true
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Max Size",
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



:::{dropdown} Point Size / Scaling

This example creates a point cloud where the size of the points is set by entering a
a scale exponent. This makes it so that the points will be given a world-scale size of
10 to the power of the provided scale exponent.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 16

local Node = {
  Identifier = "RenderablePointCloud_Example_Scaled",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      FixedColor = { 0.0, 0.0, 0.8 }
    },
    SizeSettings = {
      -- We set the exponent for the scale explicitly, to a value that
      -- gives the points a suitable size based on their world-space coordinates
      ScaleExponent = 6.5
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Point Size / Scaling",
    Path = "/Examples",
    Description = "Point cloud with configured point size"
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



:::{dropdown} Basic (Fixed Color and Size)

This example creates a point cloud with a fixed color and default size.
All the points will have the same size.

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 11

local Node = {
  Identifier = "RenderablePointCloud_Example",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      FixedColor = { 0.0, 0.5, 0.0 }
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Fixed Color and Size",
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



:::{dropdown} Color Mapping

This example creates a point cloud where the color is set from a color map. All the
data column in the dataset will be exposed in the user interface and can be used for
color mapping during runtime. The range for the color mapping is set based on the min
and max values in the dataset, for each column respoectively.
Note that the color map is loaded from another asset. This is a utility asset that
includes some common color maps for general usage.

:::{code-block} lua
:linenos:
:emphasize-lines: 6, 15

local colormaps = asset.require("util/default_colormaps")

local Node = {
  Identifier = "RenderablePointCloud_Example_ColorMapped",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      ColorMapping = {
        File = colormaps.Uniform.Viridis
      }
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Color Mapped",
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



:::{dropdown} Units

This example creates a point cloud where the positions are interpreted to be in
another unit than meters (here kilometers).

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 9

local Node = {
  Identifier = "RenderablePointCloud_Example_Units",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Unit = "Km"
  },
  GUI = {
    Name = "RenderablePointCloud - Units",
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



:::{dropdown} Draw Point Outline

This example creates a point cloud where the points have a colored outline with a
given color and thickness (weight).

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 15

local Node = {
  Identifier = "RenderablePointCloud_Example_Outline",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      EnableOutline = true,
      OutlineColor = { 0.2, 0.2, 1.0 },
      OutlineWidth = 0.1
    },
    -- It might be desired to disable additive blending when using an outline
    UseAdditiveBlending = false
  },
  GUI = {
    Name = "RenderablePointCloud - Outlined",
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



:::{dropdown} Point Size from Data

This example creates a point cloud where the size of the points is computed based on
a column in the dataset

:::{code-block} lua
:linenos:
:emphasize-lines: 4, 25

local Node = {
  Identifier = "RenderablePointCloud_Example_ScaledFromData",
  Renderable = {
    Type = "RenderablePointCloud",
    File = asset.resource("data/dummydata.csv"),
    Coloring = {
      FixedColor = { 0.5, 0.5, 0.0 }
    },
    SizeSettings = {
      SizeMapping = {
        -- The options for the columns that the points can be scaled by. The first
        -- alternative in the list is chosen per default
        ParameterOptions = { "a", "b" },
        -- Specify which option we want to use for size mapping at start up. Here we
        -- use the last of the provided options rather than the first one, which is
        -- otherwise used by default
        Parameter = "b"
      },
      -- The size mapping can be used together with other scale parameters, such as a
      -- scale exponent or scale factor
      ScaleExponent = 4.8
    }
  },
  GUI = {
    Name = "RenderablePointCloud - Size from Data",
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


