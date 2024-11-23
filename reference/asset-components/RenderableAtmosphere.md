



(atmosphere_renderable_atmosphere)=
# RenderableAtmosphere

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

*   - `AtmosphereHeight`
    - The thickness of the atmosphere in kilometers.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `GroundRadianceEmission`
    - Multiplier of the ground radiance color during the rendering phase.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Mie`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereMie-target) 
    
    - {bdg-info}`No`
    
*   - `PlanetAverageGroundReflectance`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `PlanetRadius`
    - The radius of the planet in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Rayleigh`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereRayleigh-target) 
    
    - {bdg-info}`No`
    
*   - `AtmosphereDimmingHeight`
    - Percentage of the atmosphere where other objects, such as the stars, are faded.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Debug`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereDebug-target) 
    
    - Yes
    
*   - `LightSourceNode`
    - The name of a scene graph node to be used as the source of illumination for the atmosphere. If not specified, the solar system's Sun is used.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `MieScatteringExtinctionPropCoefficient`
    - Mie Scattering/Extinction Proportion Coefficient.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Ozone`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereOzone-target) 
    
    - Yes
    
*   - `ShadowGroup`
    - Declares shadow groups, meaning which nodes are considered in shadow calculations.
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereShadowGroup-target) 
    
    - Yes
    
*   - `SunAngularSize`
    - The angular size of the Sun in degrees.
    - `Double`
    
    - In range: ( 0,180 ) 
    
    - Yes
    
*   - `SunIntensity`
    - A unitless value that controls the intensity/brightness of the Sun.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `SunsetAngle`
    - The angle (degrees) between the Camera and the Sun where the sunset starts, and the atmosphere starts to fade in objects such as the stars.
    - `Vector2<double>`
    
    - Value of type 'Vector2<double>' 
    
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










(RenderableAtmosphereMie-target)=
::::{dropdown} Table parameters for `Mie`



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

*   - `Coefficients`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereMieCoefficients-target) 
    
    - {bdg-info}`No`
    
*   - `G`
    - 
    - `Double`
    
    - In range: ( -1,1 ) 
    
    - {bdg-info}`No`
    
*   - `H_M`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::



(RenderableAtmosphereMieCoefficients-target)=
#### Table parameters for `Coefficients`



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

*   - `Extinction`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `Scattering`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
:::




::::








(RenderableAtmosphereRayleigh-target)=
::::{dropdown} Table parameters for `Rayleigh`



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

*   - `Coefficients`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereRayleighCoefficients-target) 
    
    - {bdg-info}`No`
    
*   - `H_R`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::



(RenderableAtmosphereRayleighCoefficients-target)=
#### Table parameters for `Coefficients`



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

*   - `Scattering`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
*   - `Wavelengths`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - {bdg-info}`No`
    
:::




::::






(RenderableAtmosphereDebug-target)=
::::{dropdown} Table parameters for `Debug`



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

*   - `PreCalculatedTextureScale`
    - 
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `SaveCalculatedTextures`
    - 
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



::::








(RenderableAtmosphereOzone-target)=
::::{dropdown} Table parameters for `Ozone`



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

*   - `Coefficients`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereOzoneCoefficients-target) 
    
    - Yes
    
*   - `H_O`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::



(RenderableAtmosphereOzoneCoefficients-target)=
#### Table parameters for `Coefficients`



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

*   - `Extinction`
    - 
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
:::




::::




(RenderableAtmosphereShadowGroup-target)=
::::{dropdown} Table parameters for `ShadowGroup`
Declares shadow groups, meaning which nodes are considered in shadow calculations.


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

*   - `Casters`
    - A list of objects that cast light on this atmosphere.
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereShadowGroupCasters-target) 
    
    - {bdg-info}`No`
    
*   - `Sources`
    - A list of light sources.
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereShadowGroupSources-target) 
    
    - {bdg-info}`No`
    
:::



(RenderableAtmosphereShadowGroupCasters-target)=
#### Table parameters for `Casters`
A list of objects that cast light on this atmosphere.


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

*   - `*`
    - Individual shadow casters.
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereCasters*-target) 
    
    - Yes
    
:::



(RenderableAtmosphereCasters*-target)=
#### Table parameters for `*`
Individual shadow casters.


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

*   - `Name`
    - The scene graph node name of the source.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Radius`
    - The radius of the object in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::





(RenderableAtmosphereShadowGroupSources-target)=
#### Table parameters for `Sources`
A list of light sources.


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

*   - `*`
    - Individual light sources.
    - `Table`
    
    -   [Table parameters](#RenderableAtmosphereSources*-target) 
    
    - Yes
    
:::



(RenderableAtmosphereSources*-target)=
#### Table parameters for `*`
Individual light sources.


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

*   - `Name`
    - The scene graph node name of the source.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Radius`
    - The radius of the object in meters.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::





::::










## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 9
local transforms = asset.require("./titan")



local Atmosphere = {
  Identifier = "TitanAtmosphere",
  Parent = transforms.Titan.Identifier,
  Renderable = {
    Type = "RenderableAtmosphere",
    -- Atmosphere radius in Km
    AtmosphereHeight = 2666.0 - 2576.0,
    PlanetRadius = 2576.0,
    PlanetAverageGroundReflectance = 0.1,
    GroundRadianceEmission = 0.9,
    SunIntensity = 6.9,
    Rayleigh = {
      Coefficients = {
        -- Wavelengths are given in 10^-9m
        Wavelengths = { 680, 550, 440 },
        -- Reflection coefficients are given in km^-1
        Scattering = { 0.005349578367831898, 0.01265595939366191, 0.03133178295339324 }
      },
      -- Thickness of atmosphere if its density were uniform, in Km
      H_R = 20.0
    },
    Mie = {
        Coefficients = {
          -- Reflection coefficients are given in km^-1
          Scattering = { 0.005, 0.012, 0.08 },
          -- Extinction coefficients are a fraction of the Mie coefficients
          Extinction = { 0.004 / 0.37, 0.004 / 0.37, 0.004 / 0.37 }
        },
        -- Height scale (atmosphere thickness for constant density) in km
        H_M = 14.85,
        -- Mie Phase Function Value
        -- (G e [-1.0, 1.0]. If G = 1.0, Mie phase function = Rayleigh Phase Function)
        G = -0.52
    },
    Debug = {
        PreCalculatedTextureScale = 1.0,
        SaveCalculatedTextures = false
    }
  },
  GUI = {
    Name = "Titan Atmosphere",
    Path = "/Solar System/Planets/Saturn/Major Moons/Titan"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Atmosphere)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Atmosphere)
end)

asset.export(Atmosphere)



asset.meta = {
  Name = "Titan Atmosphere",
  Description = "RenderableAtmosphere for Titan",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


