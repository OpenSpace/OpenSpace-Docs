



(base_dashboarditem_spacing)=
# DashboardItemSpacing

_Inherits [DashboardItem](#DashboardItem)_




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

*   - `Spacing`
    - This value determines the spacing (in pixels) that this item represents. The default value is 15.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
:::









## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 7
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


