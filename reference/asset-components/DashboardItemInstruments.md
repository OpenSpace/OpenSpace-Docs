



(dashboarditeminstruments-identifier )=
# DashboardItemInstruments

_Inherits [DashboardItem](#DashboardItem)_











## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 24
asset.require("./model")
asset.require("./pluto")



local Spacing = {
  Type = "DashboardItemSpacing",
  Identifier = "NewHorizonsSpacing",
  GuiName = "New Horizons Spacing",
  Spacing = 25
}

local Distance = {
  Type = "DashboardItemDistance",
  Identifier = "NewHorizonsPlutoDistance",
  GuiName = "New Horizons Pluto Distance",
  SourceType = "Node",
  SourceNodeName = "NewHorizons",
  DestinationType = "Node Surface",
  DestinationNodeName = "PlutoProjection"
}

local Instruments = {
  Type = "DashboardItemInstruments",
  Identifier = "NewHorizonsInstruments",
  GuiName = "NewHorizons Instruments"
}


asset.onInitialize(function()
  openspace.dashboard.addDashboardItem(Spacing)
  openspace.dashboard.addDashboardItem(Distance)
  openspace.dashboard.addDashboardItem(Instruments)
end)

asset.onDeinitialize(function()
  openspace.dashboard.removeDashboardItem(Instruments)
  openspace.dashboard.removeDashboardItem(Distance)
  openspace.dashboard.removeDashboardItem(Spacing)
end)

:::
:::


