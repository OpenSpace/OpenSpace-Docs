



(base_scale_timedependent)=
# TimeDependentScale

_Inherits [Scale](#core_transform_scaling)_

This Scale type provides the ability to scale an object dynamically as time in the simulation passes. The provided `ReferenceDate`, specifies when the total scale should be equal to 0 and the scales grows by `Speed` meters for every second in the simulation. If `ClampToPositive` is specified as `true`, then the resulting scale will always be positive or 0 if the simulation time is before the `ReferenceDate`.

A common use-case for this Scale type would be to represent the Radiosphere, which grows at the speed of light.


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

*   - `ReferenceDate`
    - The date at which this scale will be 0. The current value of the scale is computed by taking the difference between the current time and the reference date and multiplying it by the speed. This field must be formatted as: YYYY-MM-DDThh:mm:ss.uuu  where h is a 24h clock and u microseconds.
    - `Date and time`
    
    - Value of type 'Date and time' 
    
    - {bdg-info}`No`
    
*   - `ClampToPositive`
    - If this value is true, the velocity computation will be clamped to a positive value if the current simulation time is before the `ReferenceDate`. This is useful for instantaneous events that only propagate forwards in time. The default value is 'true'.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Speed`
    - The speed at which the value grows or shrinks. The units for this are meters per second. The default value is 1 m/s.
    - `Double`
    
    - Greater or equal to: 0 
    
    - Yes
    
:::



### Inherited members from [Scale](#core_transform_scaling)

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
    - The type of the scaling that is described in this element. The available types of scaling depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Scale type 
    
    - {bdg-info}`No`
    
:::












## Asset Examples


:::{dropdown} Basic

This asset creates a SceneGraphNode that only displays coordinate axes, which grow at
a speed of 1 m/s starting on January 1st, 2000 00:00:00. This means that on
that date, the coordinate axes will disappear and, for example, on January 1st, 2000
12:00:00, the coordinate axes will be 43200 meters long.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "TimeDependentScale_Example",
  Transform = {
    Scale = {
      Type = "TimeDependentScale",
      ReferenceDate = "2000 JAN 01 00:00:00"
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "TimeDependentScale - Basic",
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



:::{dropdown} with Speed

This asset creates a SceneGraphNode that only displays coordinate axes, which grow at
a speed of 12 km/s starting on August 8th, 1969 12:00:00. This means that on
that date, the coordinate axes will disappear and, for example, on August 8th, 1969
23:00:00, the coordinate axes will be 475200 km long.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 14

local Node = {
  Identifier = "TimeDependentScale_Example_Speed",
  Transform = {
    Scale = {
      Type = "TimeDependentScale",
      ReferenceDate = "1969 AUG 08 12:00:00",
      Speed = 12000
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "TimeDependentScale - With Speed",
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


