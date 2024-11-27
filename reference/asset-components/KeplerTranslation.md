



(space_transform_kepler)=
# KeplerTranslation

_Inherits [Translation](#core_transform_translation)_




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

*   - `ArgumentOfPeriapsis`
    - This value determines the argument of periapsis in degrees, that is the position on the orbit that is closest to the orbiting body.
    - `Double`
    
    - In range: ( -360,360 ) 
    
    - {bdg-info}`No`
    
*   - `AscendingNode`
    - This value determines the right ascension of the ascending node in degrees, that is the location of position along the orbit where the inclined plane and the horizonal reference plane intersect.
    - `Double`
    
    - In range: ( -360,360 ) 
    
    - {bdg-info}`No`
    
*   - `Eccentricity`
    - This value determines the eccentricity, that is the deviation from a perfect sphere, for this orbit. Currently, hyperbolic orbits using Keplerian elements are not supported.
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - {bdg-info}`No`
    
*   - `Epoch`
    - This value determines the epoch for which the initial location is defined in the form of YYYY MM DD HH:mm:ss.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Inclination`
    - This value determines the degrees of inclination, or the angle of the orbital plane, relative to the reference plane, on which the object orbits around the central body.
    - `Double`
    
    - In range: ( -360,360 ) 
    
    - {bdg-info}`No`
    
*   - `MeanAnomaly`
    - This value determines the mean anomaly at the epoch in degrees, which determines the initial location of the object along the orbit at epoch.
    - `Double`
    
    - In range: ( -360,360 ) 
    
    - {bdg-info}`No`
    
*   - `Period`
    - Specifies the orbital period (in seconds).
    - `Double`
    
    - Greater than: 0 
    
    - {bdg-info}`No`
    
*   - `SemiMajorAxis`
    - This value determines the semi-major axis, that is the distance of the object from the central body in kilometers (semi-major axis = average of periapsis and apoapsis).
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [Translation](#core_transform_translation)

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
    - The type of translation that is described in this element. The available types of translations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Translation type 
    
    - {bdg-info}`No`
    
:::






















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 7
local transforms = asset.require("scene/solarsystem/sun/transforms")


local OneAU = 1.496e+8

local Translation = {
  Type = "KeplerTranslation",
  Eccentricity = 0.4319581224809352,
  SemiMajorAxis = 68.14536545526268	 * OneAU,
  Inclination = 43.76049565740999,
  AscendingNode = 36.07068767579804,
  ArgumentOfPeriapsis = 150.9970340507818,
  MeanAnomaly = 208.7617474668772,
  Epoch = "2023 02 08 21:38:05",
  Period = 205472.1258735657 * 60 * 60 * 24
}

local Position = {
  Identifier = "ErisPosition",
  Parent = transforms.SunEclipJ2000.Identifier,
  Transform = {
    Translation = Translation
  },
  GUI = {
    Name = "Eris Position",
    Path = "/Solar System/Dwarf Planets/Eris",
    Hidden = true
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Position)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Position)
end)

asset.export("Translation", Translation)
asset.export("Position", Position)



asset.meta = {
  Name = "Eris Position (Keplerian)",
  Description = [[Position of Eris. KeplerTranslation Version Data from
    JPL Horizons]],
  Author = "OpenSpace Team",
  URL = "https://ssd.jpl.nasa.gov/sbdb.cgi?sstr=Eris",
  License = "JPL/NASA"
}

:::
:::


