



(base_dashboarditem_date)=
# DashboardItemDate

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

*   - `FormatString`
    - The format text describing how this dashboard item renders its text. This text must contain exactly one {} which is a placeholder that will contain the date.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `TimeFormat`
    - The format string used for formatting the date/time before being passed to the string in FormatString. See https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/timout_c.html for full information about how to structure this format.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::











## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 9
local Dashboard = {
  Identifier = "ScreenSpaceTime",
  Name = "Time",
  Type = "ScreenSpaceDashboard",
  FaceCamera = false,
  Scale = 3.0,
  Items = {
    {
      Type = "DashboardItemDate",
      Identifier = "Date",
      GuiName = "Date",
      FontSize = 72,
      FormatString = "{}",
      TimeFormat = "YYYY MON DD HR:MN:SC.### ::RND"
    }
  }
}


asset.onInitialize(function()
  openspace.addScreenSpaceRenderable(Dashboard)

  openspace.setPropertyValueSingle("ScreenSpace.ScreenSpaceTime.Size", {0.000000,0.000000,640.000000,320.000000})
end)

asset.onDeinitialize(function()
  openspace.removeScreenSpaceRenderable(Dashboard)
end)

asset.export(Dashboard)



asset.meta = {
  Name = "ScreenSpace - Date",
  Description = [[
    This asset provides a Date dashboard item that is shown on a screen space object.
    This can be place on a dome surface to show the current time to the audience.
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


