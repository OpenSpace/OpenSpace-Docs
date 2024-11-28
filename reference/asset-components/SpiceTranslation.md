



(space_translation_spicetranslation)=
# SpiceTranslation

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

*   - `Observer`
    - This is the SPICE NAIF name for the parent of the body whose translation is to be computed by the SpiceTranslation. It can either be a fully qualified name (such as 'SOLAR SYSTEM BARYCENTER') or a NAIF integer id code (such as '0').
    - `String, or Integer`
    
    - Value of type 'String', or Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `Target`
    - This is the SPICE NAIF name for the body whose translation is to be computed by the SpiceTranslation. It can either be a fully qualified name (such as 'EARTH') or a NAIF integer id code (such as '399').
    - `String, or Integer`
    
    - Value of type 'String', or Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `FixedDate`
    - 
    - `String`
    
    - A date to lock the position to 
    
    - Yes
    
*   - `Frame`
    - 
    - `String`
    
    - A valid SPICE NAIF name for a reference frame 
    
    - Yes
    
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


:::{dropdown} Fixed Date

This asset creates a time-varying translation with information from a SPICE kernel and
applies it to a SceneGraphNode that only displays coordinate axes. The position of the
coordinate axes are determined by SPICE, in this case pretending that the axes are
orbiting the same way the Moon does around Earth. In this specific example, the
position is independent of the actual in-game time in OpenSpace and only uses a fixed
date of 2000 JAN 01 instead.
For more information about SPICE see: https://naif.jpl.nasa.gov/naif/

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 18

-- Load the default SPICE kernels, which are the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceTranslation_Example_FixedDate",
  Transform = {
    Translation = {
      Type = "SpiceTranslation",
      Target = "MOON",
      Observer = "EARTH",
      FixedDate = "2000 JAN 01 00:00:00.000"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceTranslation - Fixed Date",
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



:::{dropdown} Reference Frame

This asset creates a time-varying translation with information from a SPICE kernel and
applies it to a SceneGraphNode that only displays coordinate axes. The position of the
coordinate axes are determined by SPICE, in this case pretending that the axes are
orbiting the same way the Moon does around Earth. The calculated position will be
provided in the rotating coordinate system of Earth itself.
For more information about SPICE see: https://naif.jpl.nasa.gov/naif/

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 18

-- Load the default SPICE kernels, which are the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceTranslation_Example_ReferenceFrame",
  Transform = {
    Translation = {
      Type = "SpiceTranslation",
      Target = "MOON",
      Observer = "EARTH",
      Frame = "IAU_EARTH"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceTranslation - Reference Frame",
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



:::{dropdown} Basic

This asset creates a time-varying translation with information from a SPICE kernel and
applies it to a SceneGraphNode that only displays coordinate axes. The position of the
coordinate axes are determined by SPICE, in this case pretending that the axes are
orbiting the same way the Moon does around Earth.
For more information about SPICE see: https://naif.jpl.nasa.gov/naif/

:::{code-block} lua
:linenos:
:emphasize-lines: 8, 17

-- Load the default SPICE kernels, which are the planetary constants and the DE430 kernel
asset.require("spice/core")

local Node = {
  Identifier = "SpiceTranslation_Example",
  Transform = {
    Translation = {
      Type = "SpiceTranslation",
      Target = "MOON",
      Observer = "EARTH"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "SpiceTranslation - Basic",
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


