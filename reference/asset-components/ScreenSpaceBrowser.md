



(core_screenspace_browser)=
# ScreenSpaceBrowser

_Inherits [ScreenSpaceRenderable](#core_screenspacerenderable)_

This `ScreenSpaceRenderable` can be used to render a webpage in front of the camera. This can be used to show various dynamic content, for example using the scripting API.

Note that mouse input will not be passed to the rendered view, so it will not be possible to interact with the web page.


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

*   - `Dimensions`
    - The dimensions of the web browser window in pixels.
    - `Vector2<double>`
    
    - Greater than: {0,0} 
    
    - Yes
    
*   - `Identifier`
    - A unique identifier for this screen space browser.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - Yes
    
*   - `Url`
    - The URL to load.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



### Inherited members from [ScreenSpaceRenderable](#core_screenspacerenderable)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Type`
    - The type of the `ScreenSpaceRenderable` that is to be created.
    - `String`
    
    - Must name a valid ScreenSpaceRenderable 
    
    - {bdg-info}`No`
    
*   - `BackgroundColor`
    - A fixed color that is combined with the screen space renderable to create the final color. The actual color of the screen space renderable is alpha-blended with the background color to produce the final result.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - Yes
    
*   - `BorderColor`
    - The color of the border.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `BorderWidth`
    - The width of the border.
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `CartesianPosition`
    - Determines the position of this screen space plane in Cartesian three-dimensional coordinates (meters).
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `Enabled`
    - Determines whether this sceen space object will be rendered or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `FaceCamera`
    - If enabled, the object will be rotated to face the camera position. Any local rotation is then applied after this rotation.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `GammaOffset`
    - Sets the gamma correction of the texture that is applied in addition to the global gamma value.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Identifier`
    - The unique identifier for this screen space renderable. It has to be unique amongst all existing screen space nodes that have been added to the scene.
    - `Identifier`
    
    - An identifier string. May not contain '.', spaces, newlines, or tabs 
    
    - Yes
    
*   - `MultiplyColor`
    - If set, the plane's texture is multiplied with this color. Useful for applying a color grayscale images.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `Name`
    - The name of the `ScreenSpaceRenderable`, which will be shown in the GUI. This does not have to be unique to the scene, but it is recommended to be.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Opacity`
    - The opacity of the screen space object. If 1, the object is completely opaque. If 0, the object is completely transparent.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `RadiusAzimuthElevation`
    - Determines the position of this screen space plane in a coordinate system based on radius (meters), azimuth (radians), and elevation (radians).
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `RenderDuringBlackout`
    - If true, this screen space renderable is going to ignore the global blackout factor from the Render Engine and will always render at full opacity. If false, it will adhere to the factor and fade out like the rest of the 3D rendering.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Scale`
    - A scale factor for the plane that can be used to increase or decrease the visual size. The default size is determined separately for each screen space renderable type and may for example be affected by the size of an image being displayed.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Tag`
    - Defines either a single or multiple tags that apply to this `ScreenSpaceRenderable`, thus making it possible to address multiple, separate Renderables with a single property change.
    - `String, or Table`
    
    - Value of type 'String', or Value of type 'Table' 
    
    - Yes
    
*   - `UsePerspectiveProjection`
    - Determines whetether the z/radius values affects the size of the plane or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `UseRadiusAzimuthElevation`
    - Determines whether the location of this screen space plane will be specified using radius, azimuth and elevation (if 'true') or using Cartesian coordinates. The Cartesian coordinate system is useful if a regular rendering is applied, whereas the radius azimuth elevation are most useful in a planetarium environment.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::












## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 2
local Browser = {
  Type = "ScreenSpaceBrowser",
  Identifier = "ScreenSpaceBrowserExample",
  Name = "Screen Space Browser Example",
  Url = "https://www.openspaceproject.com/"
}


asset.onInitialize(function()
  openspace.addScreenSpaceRenderable(Browser)
end)

asset.onDeinitialize(function()
  openspace.removeScreenSpaceRenderable(Browser)
end)

asset.export(Browser)



asset.meta = {
  Name = "ScreenSpaceBrowser Example",
  Description = [[Example of how to load and show a webpage in the rendering. The loaded
    webpage is shown in screen space.]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::

