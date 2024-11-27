



(base_dashboarditem_velocity)=
# DashboardItemVelocity

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

*   - `FontName`
    - This value is the name of the font that is used. It can either refer to an internal name registered previously, or it can refer to a path that is used.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `FontSize`
    - This value determines the size of the font that is used to render the distance.
    - `Double`
    
    - Value of type 'Double' 
    
    - Yes
    
*   - `RequestedUnit`
    - If the simplification is disabled, this distance unit is used for the velocity display.
    - `String`
    
    - In list { nanometer, micrometer, millimeter, centimeter, decimeter, meter, km, AU, lighthour, lightday, lightmonth, lightyear, parsec, kiloparsec, megaparsec, gigaparsec, gigalightyear, thou, inch, foot, yard, chain, furlong, mile, league } 
    
    - Yes
    
*   - `Simplification`
    - If this value is enabled, the velocity is displayed in nuanced units, such as m/s, AU/s, light years / s etc. If this value is disabled, the unit can be explicitly requested.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::















## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 2
local Item = {
  Type = "DashboardItemVelocity",
  Identifier = "CameraVelocity",
  Simplification = true,
  GuiName = "Camera Velocity"
}


asset.onInitialize(function()
  openspace.dashboard.addDashboardItem(Item)
end)

asset.onDeinitialize(function()
  openspace.dashboard.removeDashboardItem(Item)
end)

asset.export(Item)



asset.meta = {
  Name = "Dashboard - Velocity",
  Description = "This asset provides a dashboard item that shows the camera's velocity",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


