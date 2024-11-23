



(space_renderablestars)=
# RenderableStars

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
    - The path to the texture that is used to convert from the B-V value of the star to its color. The texture is used as a one dimensional lookup function.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `DataMapping`
    - The mappings between data values and the variable names specified in the SPECK file.
    - `Table`
    
    -   [Table parameters](#RenderableStarsDataMapping-target) 
    
    - {bdg-info}`No`
    
*   - `File`
    - The path to the SPECK file containing the data for rendering these stars.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
*   - `Glare`
    - Settings for the glare portion of the star.
    - `Table`
    
    -   [Table parameters](#RenderableStarsGlare-target) 
    
    - {bdg-info}`No`
    
*   - `ColorOption`
    - This value determines which quantity is used for determining the color of the stars.
    - `String`
    
    - In list { Color, Velocity, Speed, Other Data, Fixed Color } 
    
    - Yes
    
*   - `Core`
    - Settings for the central core portion of the star.
    - `Table`
    
    -   [Table parameters](#RenderableStarsCore-target) 
    
    - Yes
    
*   - `EnableFadeIn`
    - Enables/Disables the Fade-in effect.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FadeInDistances`
    - These values determine the initial and final distances from the center of our galaxy from which the astronomical object will start and end fading-in.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
    - Yes
    
*   - `FilterOutOfRange`
    - Determines whether other data values outside the value range should be visible or filtered away.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `MagnitudeExponent`
    - Adjust star magnitude by 10^MagnitudeExponent. Stars closer than this distance are given full opacity. Farther away, stars dim proportionally to the logarithm of their distance.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `OtherData`
    - The index of the SPECK file data column that is used as the color input.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `OtherDataColorMap`
    - The color map that is used if the 'Other Data' rendering method is selected.
    - `File`
    
    - Value of type 'File' 
    
    - Yes
    
*   - `SizeComposition`
    - Method to determine the size for the stars.
    - `String`
    
    - In list { Distance Modulus, App Brightness, Lum and Size, Abs Magnitude, App Magnitude } 
    
    - Yes
    
*   - `StaticFilter`
    - Specifies a value that is always filtered out of the value ranges on load. This can be used to trim the dataset's automatic value range.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `StaticFilterReplacement`
    - A value that is used to replace statically filtered values. Setting this value only makes sense if `StaticFilter` is set as well.
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








(RenderableStarsDataMapping-target)=
::::{dropdown} Table parameters for `DataMapping`
The mappings between data values and the variable names specified in the SPECK file.


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `AbsoluteMagnitude`
    - The name of the variable in the SPECK file that is used as the absolute magnitude variable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Bv`
    - The name of the variable in the SPECK file that is used as the b-v color variable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Luminance`
    - The name of the variable in the SPECK file that is used as the luminance variable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Speed`
    - The name of the variable in the SPECK file that is used as the speed.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Vx`
    - The name of the variable in the SPECK file that is used as the star velocity along the x-axis.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Vy`
    - The name of the variable in the SPECK file that is used as the star velocity along the y-axis.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Vz`
    - The name of the variable in the SPECK file that is used as the star velocity along the z-axis.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::






(RenderableStarsGlare-target)=
::::{dropdown} Table parameters for `Glare`
Settings for the glare portion of the star.


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Gamma`
    - An individual gamma exponent for this texture component. Using the multiplier and gamma values for both components, it is possible to finetune the look of the stars.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Multiplier`
    - An individual multiplication factor for this texture component. Using the multiplier and gamma values for both components, it is possible to fine tune the look of the stars or disable the contributions altogether by setting it to 0.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Scale`
    - A uniform scale factor that determines how much of the total size of the star this component is using. If it is 0, it will be hidden. If it is 1, it will take the entire size.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Texture`
    - The path to the texture that should be used.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
:::



::::






(RenderableStarsCore-target)=
::::{dropdown} Table parameters for `Core`
Settings for the central core portion of the star.


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

*   - `Gamma`
    - An individual gamma exponent for this texture component. Using the multiplier and gamma values for both components, it is possible to finetune the look of the stars.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Multiplier`
    - An individual multiplication factor for this texture component. Using the multiplier and gamma values for both components, it is possible to fine tune the look of the stars or disable the contributions altogether by setting it to 0.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Scale`
    - A uniform scale factor that determines how much of the total size of the star this component is using. If it is 0, it will be hidden. If it is 1, it will take the entire size.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Texture`
    - The path to the texture that should be used.
    - `File`
    
    - Value of type 'File' 
    
    - {bdg-info}`No`
    
:::



::::






















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 26
local textures = asset.resource({
  Name = "Stars Textures",
  Type = "HttpSynchronization",
  Identifier = "stars-denver_textures",
  Version = 1
})

local speck = asset.resource({
  Name = "Stars Speck Files",
  Type = "HttpSynchronization",
  Identifier = "stars-denver_speck",
  Version = 1
})

local colorLUT = asset.resource({
  Name = "Stars Color Table",
  Type = "HttpSynchronization",
  Identifier = "stars-denver_colormap",
  Version = 2
})


local Object = {
  Identifier = "Stars-Denver",
  Renderable = {
    Type = "RenderableStars",
    File = speck .. "denver_stars.speck",
    Glare = {
      Texture = textures .. "halo.png"
    },
    ColorMap = colorLUT .. "denver_colorbv.cmap",
    MagnitudeExponent = 6.2,
    SizeComposition = "Distance Modulus",
    DataMapping = {
      Bv = "colorb_v",
      Luminance = "lum",
      AbsoluteMagnitude = "absmag",
      ApparentMagnitude = "appmag",
      Vx = "vx",
      Vy = "vy",
      Vz = "vz",
      Speed = "speed"
    }
  },
  GUI = {
    Name = "Stars (Denver)",
    Path = "/Milky Way/Stars"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Object)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Object)
end)

asset.export(Object)



asset.meta = {
  Name = "Stars Denver",
  Description = [[Alternative Milky Way Atlas: based on HIPPARCOS and Yale Bright
    Star catalogs]],
  Author = "Ka chun Yu",
  URL = "http://openspaceproject.com",
  License = "Creative Commons Attribution-Share Alike 3.0 Unported"
}

:::
:::


