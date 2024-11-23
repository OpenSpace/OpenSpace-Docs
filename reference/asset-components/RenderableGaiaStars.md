



(gaiamission_renderablegaiastars)=
# RenderableGaiaStars

_Inherits [Renderable](#renderable)_




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

*   - `ColorMap`
    - The path to the texture that is used to convert from the magnitude of the star to its color. The texture is used as a one dimensional lookup function.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `File`
    - The path to the file with data for the stars to be rendered.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `FileReaderOption`
    - This value tells the renderable what format the input data file has. 'Fits' will read a FITS file, construct an Octree from it and render full data. 'Speck' will read a SPECK file, construct an Octree from it and render full data. 'BinaryRaw' will read a preprocessed binary file with ordered star data, construct an Octree and render it. 'BinaryOctree' will read a constructed Octree from binary file and render full data. 'StreamOctree' will read an index file with full Octree structure and then stream nodes during runtime. (This option is suited for bigger datasets).
    - `String`
    
    - In list { Fits, Speck, BinaryRaw, BinaryOctree, StreamOctree } 
    
    - {bdg-info}`No`
    
*   - `Texture`
    - The path to the texture that should be used as a point spread function for the stars.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `AdditionalNodes`
    - Determines how many additional nodes around the camera that will be fetched from disk. The first value determines how many additional layers of parents that will be fetched. The second value determines how many layers of descendant that will be fetched from the found parents.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `BillboardSize`
    - Set the billboard size of all stars. [Works only with billboards].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `CloseUpBoostDist`
    - Set the distance where stars starts to increase in size. Unit is Parsec [Works only with billboards].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `ColumnNames`
    - A list of strings with the names of all the columns that are to be read from the specified FITS file. No need to define if data already has been processed. [Works only with FileReaderOption::Fits].
    - `Table`
    
    -   [Table parameters](#RenderableGaiaStarsColumnNames-target) 
    
    - Yes
    
*   - `CutOffThreshold`
    - Set threshold for when to cut off star rendering. Stars closer than this threshold are given full opacity. Farther away, stars dim proportionally to the 4-logarithm of their distance.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `FilterBpRp`
    - If defined then only stars with Bp-Rp color values between [min, max] will be rendered (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterDist`
    - If defined then only stars with Distances values between [min, max] will be rendered (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). Measured in kParsec.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterGMag`
    - If defined then only stars with G mean magnitude values between [min, max] will be rendered (if min is set to 20.0 it is read as -Inf, if max is set to 20.0 it is read as +Inf). If min = max then all values equal min|max will be filtered away.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosX`
    - If defined then only stars with Position X values between [min, max] will be rendered (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). Measured in kiloParsec.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosY`
    - If defined then only stars with Position Y values between [min, max] will be rendered (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). Measured in kiloParsec.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterPosZ`
    - If defined then only stars with Position Z values between [min, max] will be rendered (if min is set to 0.0 it is read as -Inf, if max is set to 0.0 it is read as +Inf). Measured in kiloParsec.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterSize`
    - Set the filter size in pixels used in tonemapping for point splatting rendering[Works only with points].
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `FirstRow`
    - Defines the first row that will be read from the specified FITS file No need to define if data already has been processed. [Works only with FileReaderOption::Fits].
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LastRow`
    - Defines the last row that will be read from the specified FITS file; has to be equal to or greater than FirstRow. No need to define if data already has been processed. [Works only with FileReaderOption::Fits].
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `LodPixelThreshold`
    - The number of total pixels a nodes AABB can have in clipping space before its parent is fetched as LOD cache.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `LuminosityMultiplier`
    - Factor by which to multiply the luminosity with. [Works in Color and Motion modes].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MagnitudeBoost`
    - Sets what percent of the star magnitude that will be used as boost to star size. [Works only with billboards in Color and Motion modes].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MaxCpuMemoryPercent`
    - Sets the max percent of existing CPU memory budget that the streaming of files will use.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MaxGpuMemoryPercent`
    - Sets the max percent of existing GPU memory budget that the streaming will use.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `PixelWeightThreshold`
    - Set the threshold for how big the elliptic weight of a pixel has to be to contribute to the final elliptic shape. A smaller value gives a more visually pleasing result while a bigger value will speed up the rendering on skewed frustums (aka Domes).
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `RenderMode`
    - This value determines which predefined columns to use in rendering. If 'Static' only the position of the stars is used. 'Color' uses position + color parameters and 'Motion' uses pos, color as well as velocity for the stars.
    - `String`
    
    - In list { Static, Color, Motion } 
    
    - Yes
    
*   - `ReportGlErrors`
    - If set to true, any OpenGL errors will be reported if encountered.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ShaderOption`
    - This value determines which shaders to use while rendering. If 'Point_*' is chosen then gl_Points will be rendered and then spread out with a bloom filter. If 'Billboard_*' is chosen then the geometry shaders will generate screen-faced billboards for all stars. For '*_SSBO' the data will be stored in Shader Storage Buffer Objects while '*_VBO' uses Vertex Buffer Objects for the streaming. OBS! SSBO won't work on Apple.
    - `String`
    
    - In list { Point_SSBO, Point_VBO, Billboard_SSBO, Billboard_VBO, Billboard_SSBO_noFBO } 
    
    - Yes
    
*   - `Sharpness`
    - Adjust star sharpness. [Works only with billboards].
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Sigma`
    - Set the normal distribution sigma used in tonemapping for point splatting rendering. [Works only with points].
    - `Double`
    
    - Value of type 'Double' 
    
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




















(RenderableGaiaStarsColumnNames-target)=
::::{dropdown} Table parameters for `ColumnNames`
A list of strings with the names of all the columns that are to be read from the specified FITS file. No need to define if data already has been processed. [Works only with FileReaderOption::Fits].


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

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::














































## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 34
local fullOS = openspace.systemCapabilities.fullOperatingSystem()
if string.find(fullOS, "Darwin") then
  openspace.printWarning("Gaia module (RenderableGaiaStars) not supported on mac")
  return
end

-- Download a preprocessed binary octree of Radial Velocity subset values per star
-- (preprocessed into 8 binary files).
local starsFolder = asset.resource({
  Name = "Gaia Stars RV",
  Type = "HttpSynchronization",
  Identifier = "gaia_stars_rv_octree",
  Version = 1
})

local colormaps = asset.resource({
  Name = "Stars Color Table",
  Type = "HttpSynchronization",
  Identifier = "stars_colormap",
  Version = 3
})

local textures = asset.resource({
  Name = "Stars Textures",
  Type = "HttpSynchronization",
  Identifier = "stars_textures",
  Version = 1
})


local GaiaStars = {
  Identifier = "GaiaStars",
  Renderable = {
    Type = "RenderableGaiaStars",
    File = starsFolder,
    FileReaderOption = "StreamOctree",
    RenderMode = "Motion",
    ShaderOption = "Point_SSBO",
    Texture = textures .. "halo.png",
    ColorMap = colormaps .. "colorbv.cmap",
    LuminosityMultiplier = 35,
    MagnitudeBoost = 25,
    CutOffThreshold = 38,
    BillboardSize = 1,
    CloseUpBoostDist = 250,
    Sharpness = 1.45,
    LodPixelThreshold = 0,
    MaxGpuMemoryPercent = 0.24,
    MaxCpuMemoryPercent = 0.4,
    FilterSize = 5,
    Sigma = 0.5,
    AdditionalNodes = { 3.0, 2.0 },
    FilterPosX = { 0.0, 0.0 },
    FilterPosY = { 0.0, 0.0 },
    FilterPosZ = { 0.0, 0.0 },
    FilterGMag = { 20.0, 20.0 },
    FilterBpRp = { 0.0, 0.0 },
    FilterDist = { 9.0, 9.0 }
  },
  GUI = {
    Name = "Gaia Stars",
    Path = "/Milky Way",
    Description = "Radial Velocity subset of GaiaDR2"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(GaiaStars)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(GaiaStars)
end)

asset.export(GaiaStars)



asset.meta = {
  Name = "Gaia Stars",
  Description = [[This asset contains a subset of GaiaDR2. This subset contains 7.5M stars which have
  accurate values for a number of columns]],
  Author = "ESA/Gaia/DPAC",
  URL = "https://gea.esac.esa.int/archive/documentation/GDR2/index.html",
  License = [[The Gaia data are open and free to use, provided credit is given to
    'ESA/Gaia/DPAC'. In general, access to, and use of, ESA's Gaia Archive (hereafter
    called 'the website') constitutes acceptance of the following general terms and
    conditions. Neither ESA nor any other party involved in creating, producing, or
    delivering the website shall be liable for any direct, incidental, consequential,
    indirect, or punitive damages arising out of user access to, or use of, the website.
    The website does not guarantee the accuracy of information provided by external
    sources and accepts no responsibility or liability for any consequences arising from
    the use of such data]]
}

:::
:::


