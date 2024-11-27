



(base_dashboarditem_distance)=
# DashboardItemDistance

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

*   - `DestinationNodeName`
    - If a scene graph node is selected as type, this value specifies the name of the node that is to be used as the destination for computing the distance.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `DestinationType`
    - The type of position that is used as the destination to calculate the distance. The default value for this is 'Focus'.
    - `String`
    
    - In list { Node, Node Surface, Focus, Camera } 
    
    - Yes
    
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
    
*   - `FormatString`
    - The format string that is used for formatting the distance string.  This format receives four parameters:  The name of the source, the name of the destination the value of the distance and the unit of the distance.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `RequestedUnit`
    - If the simplification is disabled, this distance unit is used as a destination to convert the meters into.
    - `String`
    
    - In list { nanometer, micrometer, millimeter, centimeter, decimeter, meter, km, AU, lighthour, lightday, lightmonth, lightyear, parsec, kiloparsec, megaparsec, gigaparsec, gigalightyear, thou, inch, foot, yard, chain, furlong, mile, league } 
    
    - Yes
    
*   - `Simplification`
    - If this value is enabled, the distance is displayed in nuanced units, such as km, AU, light years, parsecs, etc. If this value is disabled, the unit can be explicitly requested.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `SourceNodeName`
    - If a scene graph node is selected as type, this value specifies the name of the node that is to be used as the source for computing the distance.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `SourceType`
    - The type of position that is used as the source to calculate the distance. The default value is 'Camera'.
    - `String`
    
    - In list { Node, Node Surface, Focus, Camera } 
    
    - Yes
    
:::

























## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 13
local earth = asset.require("scene/solarsystem/planets/earth/earth")

local Dashboard = {
  Identifier = "ScreenSpaceDistanceToEarth",
  Name = "Distance to Earth",
  Type = "ScreenSpaceDashboard",
  FaceCamera = false,
  Scale = 3.0,
  UseRadiusAzimuthElevation = true,
  RadiusAzimuthElevation = { 2.0, -0.2, -0.2 },
  Items = {
    {
      Type = "DashboardItemDistance",
      Identifier = "EarthToCameraDistance",
      GuiName = "Distance to Earth",
      FontSize = 40,
      SourceType = "Camera",
      DestinationType = "Node",
      DestinationNodeName = earth.Earth.Identifier,
      -- Specify to use a specific unit, by disabling the automatic simplification of
      -- unit and instead use light-years
      Simplification = false,
      RequestedUnit = "lightyear",
      -- If we don't want to use the default format of the text, we can specify our own
      -- format. Here we've decided to not include the name of the source object (index 0),
      -- which would be "Camera". We just include the name of the destination node (Earth,
      -- index 1), the distance (index 2) as a floating point number (f), and then the
      -- name for the unit (index 3)
      FormatString = "Distance to {1}: {2:f} {3}"
    }
  }
}


asset.onInitialize(function()
  openspace.addScreenSpaceRenderable(Dashboard)
  openspace.setPropertyValueSingle(
    "ScreenSpace.ScreenSpaceDistanceToEarth.Size",
    {0.0, 0.0, 640.0, 320.0}
  )
end)

asset.onDeinitialize(function()
  openspace.addScreenSpaceRenderable(Dashboard)
end)

asset.export(Dashboard)



asset.meta = {
  Name = "ScreenSpace - Distance to Earth",
  Description = [[
    This asset provides a screenspace dashboard item that shows the distance from the
    camera to Earth, in light-years. This can be placed on a dome surface to show the
    current distance to the audience.
  ]],
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


