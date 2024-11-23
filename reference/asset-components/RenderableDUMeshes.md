



(digitaluniverse_renderabledumeshes)=
# RenderableDUMeshes

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

*   - `File`
    - The path to the SPECK file that contains information about the astronomical object being rendered.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `DrawLabels`
    - Determines whether labels should be drawn or hidden.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LabelFile`
    - The path to the label file that contains information about the astronomical objects being rendered.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `LineWidth`
    - If the DU mesh is of wire type, this value determines the width of the lines.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `MeshColor`
    - The defined colors for the meshes to be rendered.
    - `Table`
    
    -   [Table parameters](#RenderableDUMeshesMeshColor-target) 
    
    - Yes
    
*   - `TextColor`
    - The text color for the astronomical object.
    - `Color3`
    
    - Value of type 'Color3' 
    
    - Yes
    
*   - `TextMinMaxSize`
    - The minimum and maximum size (in pixels) of the text for the labels for the astronomical objects being rendered.
    - `Vector2<int>`
    
    - Value of type 'Vector2<int>' 
    
    - Yes
    
*   - `TextOpacity`
    - Determines the transparency of the text label, where 1 is completely opaque and 0 fully transparent.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `TextSize`
    - The text size for the astronomical object labels.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `Unit`
    - The unit used when interpreting the positions in the dataset.
    - `String`
    
    - In list { m, Km, pc, Kpc, Mpc, Gpc, Gly } 
    
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














(RenderableDUMeshesMeshColor-target)=
::::{dropdown} Table parameters for `MeshColor`
The defined colors for the meshes to be rendered.


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
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
:::



::::














## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 17, 35, 53, 71, 89, 107, 125
local transforms = asset.require("scene/solarsystem/sun/transforms")
local earth_transforms = asset.require("scene/solarsystem/planets/earth/transforms")



local speck = asset.resource({
  Name = "Star Orbits Speck Files",
  Type = "HttpSynchronization",
  Identifier = "digitaluniverse_starorbits_speck",
  Version = 2
})


local SunOrbit = {
  Identifier = "SunOrbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-Sun.speck",
    MeshColor = { { 1.0, 0.65, 0.0 } },
    Unit = "pc"
  },
  GUI = {
    Name = "Sun Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of the Sun around the Milky Way over the next 1
      billion years.]]
  }
}

local BarnardsOrbit = {
  Identifier = "BarnardsOrbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-BarnardsStar.speck",
    MeshColor = { { 0.39, 0.58, 0.93 } },
    Unit = "pc"
  },
  GUI = {
    Name = "Barnards Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of Barnard's Star around the Milky Way over the next
      1 billion years.]]
  }
}

local KapteynsOrbit = {
  Identifier = "KapteynsOrbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-KapteynsStar.speck",
    MeshColor = { { 0.6, 0.6, 0.6 } },
    Unit = "pc"
  },
  GUI = {
    Name = "Kapteyns Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of Kapteyn's Star around the Milky Way over the next
      1 billion years.]]
  }
}

local Lacaille9352Orbit = {
  Identifier = "Lacaille9352Orbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-Lacaille9352.speck",
    MeshColor = { { 0.58, 0.0, 0.83 } },
    Unit = "pc"
  },
  GUI = {
    Name = "Lacaille 9352 Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of Lacaille9352 around the Milky Way over the next
      1 billion years.]]
  }
}

local LSR1826Orbit = {
  Identifier = "LSR1826Orbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-LSR1826+3014.speck",
    MeshColor = { { 0.0, 0.39, 0.0 } },
    Unit = "pc"
  },
  GUI = {
    Name = "LSR1826+3014 Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of LSR1826+3014 around the Milky Way over the next 1
      billion years.]]
  }
}

local LSRJ0822Orbit = {
  Identifier = "LSRJ0822Orbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-LSRJ0822+1700.speck",
    MeshColor = { { 0.5, 1.0, 0.0 } },
    Unit = "pc"
  },
  GUI = {
    Name = "LSRJ0822+1700 Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of LSRJ0822+1700 around the Milky Way over the next 1
      billion years.]]
  }
}

local PM_J13420Orbit = {
  Identifier = "PM_J13420Orbit",
  Renderable = {
    Type = "RenderableDUMeshes",
    Enabled = false,
    Opacity = 1.0,
    File = speck .. "starorbits-PM_J13420-3415.speck",
    MeshColor = { { 0.70, 0.13, 0.13 } },
    Unit = "pc"
  },
  GUI = {
    Name = "PM_J13420-3415 Orbit",
    Path = "/Milky Way/Stars/Stars Orbits",
    Description = [[Projected orbit of PM_J13420-3415 around the Milky Way over the next
      1 billion years.]]
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(SunOrbit)
  openspace.addSceneGraphNode(BarnardsOrbit)
  openspace.addSceneGraphNode(KapteynsOrbit)
  openspace.addSceneGraphNode(Lacaille9352Orbit)
  openspace.addSceneGraphNode(LSR1826Orbit)
  openspace.addSceneGraphNode(LSRJ0822Orbit)
  openspace.addSceneGraphNode(PM_J13420Orbit)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(PM_J13420Orbit)
  openspace.removeSceneGraphNode(LSRJ0822Orbit)
  openspace.removeSceneGraphNode(LSR1826Orbit)
  openspace.removeSceneGraphNode(Lacaille9352Orbit)
  openspace.removeSceneGraphNode(KapteynsOrbit)
  openspace.removeSceneGraphNode(BarnardsOrbit)
  openspace.removeSceneGraphNode(SunOrbit)
end)

asset.export(SunOrbit)
asset.export(BarnardsOrbit)
asset.export(KapteynsOrbit)
asset.export(Lacaille9352Orbit)
asset.export(LSR1826Orbit)
asset.export(LSRJ0822Orbit)
asset.export(PM_J13420Orbit)



asset.meta = {
  Name = "Star Orbits",
  Description = [[Projected star orbits for selected stars over the next 1 billion years. Census: 7 star orbits.]],
  Author = "Brian Abbott, Zack Reeves (AMNH)",
  URL = "https://www.amnh.org/research/hayden-planetarium/digital-universe",
  License = "AMNH Digital Universe"
}

:::
:::


