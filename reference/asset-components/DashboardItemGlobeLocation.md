



(dashboarditemglobelocation-identifier )=
# DashboardItemGlobeLocation

_Inherits [DashboardItem](#DashboardItem)_











## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 2
local Item = {
  Type = "DashboardItemGlobeLocation",
  Identifier = "GlobeLocation",
  GuiName = "Globe Location"
}


asset.onInitialize(function()
  openspace.dashboard.addDashboardItem(Item)
end)

asset.onDeinitialize(function()
  openspace.dashboard.removeDashboardItem(Item)
end)

asset.export(Item)



asset.meta = {
  Name = "Dashboard - GlobeLocation",
  Description = "This asset provides a GlobeLocation dashboard item",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


