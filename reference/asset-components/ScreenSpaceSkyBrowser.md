



(skybrowser_screenspaceskybrowser)=
# ScreenSpaceSkyBrowser

_Inherits [ScreenSpaceRenderable](#core_screenspacerenderable)_

This `ScreenSpaceRenderable` is used to display a screen space window showing the integrated World Wide Telescope view. The view will be dynamically updated when interacting with the view or with images in the SkyBrowser panel.

A `ScreenSpaceSkyBrowser` should not be created from a `.asset` file, but is rather created from interacting with the SkyBrowser user interface panel. If created in an asset, it requires some extra scripting to work with the SkyBrowser feature.


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

*   - `IsHidden`
    - If checked, the browser will be not be displayed. If it is not checked, it will be.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `PointSpacecraft`
    - If checked, spacecrafts will point towards the coordinate of an image upon selection.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `TextureQuality`
    - A parameter to set the resolution of the texture. 1 is full resolution and slower frame rate. Lower value means lower resolution of texture and faster frame rate.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `UpdateDuringTargetAnimation`
    - If checked, the sky browser display copy will update its coordinates while the target is animating.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
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













