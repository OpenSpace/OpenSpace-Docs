



(spacecraftinstruments_renderablecrawlingline)=
# RenderableCrawlingLine

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

*   - `Color`
    - The colors used for the crawling line, given as one color at the start of the line and one at the end.
    - `Table`
    
    -   [Table parameters](#RenderableCrawlingLineColor-target) 
    
    - {bdg-info}`No`
    
*   - `Instrument`
    - The SPICE name of the instrument that is used to render the crawling line.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Source`
    - The SPICE name of the source of the crawling line. For example, the spacecraft.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Target`
    - The SPICE name of the target of the crawling line.
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
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






(RenderableCrawlingLineColor-target)=
::::{dropdown} Table parameters for `Color`
The colors used for the crawling line, given as one color at the start of the line and one at the end.


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

*   - `End`
    - The color at the end of the line.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - {bdg-info}`No`
    
*   - `Start`
    - The color at the start of the line.
    - `Color4`
    
    - Value of type 'Color4' 
    
    - {bdg-info}`No`
    
:::



::::










## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 346
local transforms = asset.require("./transforms")
local kernels = asset.require("./kernels")
local coreKernels = asset.require("spice/core")



local LorriOffset = { -6.626, -4.1, -3.23 }
local RalphOffset = {   -6.9, -4.6,  8.7  }
local AliceOffset = {   -7.9, -1.7,  8.3  }
local RexOffset   = {      0,    0,    0  }

local Lorri = {
  Identifier = "NH_LORRI",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = LorriOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    Color = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.Lorri,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "LORRI",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphLeisa = {
  Identifier = "NH_RALPH_LEISA",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphLeisa,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH LEISA",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicPan1 = {
  Identifier = "NH_RALPH_MVIC_PAN1",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicPan1,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC PAN 1",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicPan2 = {
  Identifier = "NH_RALPH_MVIC_PAN2",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicPan2,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC PAN 2",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicRed = {
  Identifier = "NH_RALPH_MVIC_RED",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicRed,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC RED",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicBlue = {
  Identifier = "NH_RALPH_MVIC_BLUE",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicBlue,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC BLUE",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicFt = {
  Identifier = "NH_RALPH_MVIC_FT",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicFT,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC FT",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicMethane = {
  Identifier = "NH_RALPH_MVIC_METHANE",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicMethane,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC METHANE",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local RalphMvicNir = {
  Identifier = "NH_RALPH_MVIC_NIR",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RalphOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.RalphMvicNIR,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "RALPH MVIC NIR",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local AliceAirglow = {
  Identifier = "NH_ALICE_AIRGLOW",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = AliceOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.AliceAirglow,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    },
    SimplifyBounds = true
  },
  GUI = {
    Name = "ALICE AIRGLOW",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local AliceSoc = {
  Identifier = "NH_ALICE_SOC",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = AliceOffset
    }
  },
  Renderable = {
    Type = "RenderableFov",
    Body = kernels.ID.NewHorizons,
    Frame = kernels.Frame.NewHorizons,
    RGB = { 0.8, 0.7, 0.7 },
    Instrument = {
      Name = kernels.Frame.AliceSOC,
      Aberration = "NONE"
    },
    PotentialTargets = {
      kernels.ID.Pluto,
      kernels.ID.Charon
    }
  },
  GUI = {
    Name = "ALICE SOC",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}

local Rex = {
  Identifier = "NH_REX",
  Parent = transforms.NewHorizonsPosition.Identifier,
  Transform = {
    Translation = {
      Type = "StaticTranslation",
      Position = RexOffset
    },
    Rotation = {
      Type = "StaticRotation",
      Rotation = { -math.pi / 2, 0.0, -math.pi / 2 }
    }
  },
  Renderable = {
    Type = "RenderableCrawlingLine",
    Source = kernels.ID.Rex,
    Target = coreKernels.ID.Earth,
    Instrument = kernels.Frame.Rex,
    Color = {
      Start = { 1.0, 0.7, 0.0, 1.0 },
      End = { 0.0, 0.0, 0.0, 0.0 }
    }
  },
  GUI = {
    Name = "REX",
    Path = "/Solar System/Missions/New Horizons/Instruments"
  }
}


asset.onInitialize(function()
  openspace.addSceneGraphNode(Lorri)
  openspace.addSceneGraphNode(RalphLeisa)
  openspace.addSceneGraphNode(RalphMvicPan1)
  openspace.addSceneGraphNode(RalphMvicPan2)
  openspace.addSceneGraphNode(RalphMvicRed)
  openspace.addSceneGraphNode(RalphMvicBlue)
  openspace.addSceneGraphNode(RalphMvicFt)
  openspace.addSceneGraphNode(RalphMvicMethane)
  openspace.addSceneGraphNode(RalphMvicNir)
  openspace.addSceneGraphNode(AliceAirglow)
  openspace.addSceneGraphNode(AliceSoc)
  openspace.addSceneGraphNode(Rex)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Rex)
  openspace.removeSceneGraphNode(AliceSoc)
  openspace.removeSceneGraphNode(AliceAirglow)
  openspace.removeSceneGraphNode(RalphMvicNir)
  openspace.removeSceneGraphNode(RalphMvicMethane)
  openspace.removeSceneGraphNode(RalphMvicFt)
  openspace.removeSceneGraphNode(RalphMvicBlue)
  openspace.removeSceneGraphNode(RalphMvicRed)
  openspace.removeSceneGraphNode(RalphMvicPan2)
  openspace.removeSceneGraphNode(RalphMvicPan1)
  openspace.removeSceneGraphNode(RalphLeisa)
  openspace.removeSceneGraphNode(Lorri)
end)

asset.export(Lorri)
asset.export(RalphLeisa)
asset.export(RalphMvicPan1)
asset.export(RalphMvicPan2)
asset.export(RalphMvicRed)
asset.export(RalphMvicBlue)
asset.export(RalphMvicFt)
asset.export(RalphMvicMethane)
asset.export(RalphMvicNir)
asset.export(AliceAirglow)
asset.export(AliceSoc)
asset.export(Rex)

:::
:::


