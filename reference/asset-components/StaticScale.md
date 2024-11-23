



(base_scale_static)=
# StaticScale

_Inherits [Scale](#core_transform_scaling)_

This Scale type scales the scene graph node that it is attached to by a fixed amount that does not change over time. It is possible to change the fixed scale after starting the application, but it otherwise remains unchanged. The scaling is a simple multiplication so that a `Scale` value of 10 means that the object will be 10 times larger than its original size.


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

*   - `Scale`
    - This value is used as a scaling factor for the scene graph node that this transformation is attached to relative to its parent.
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
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

This asset creates a SceneGraphNode that only displays coordinate axes. The coordinate
axis normally have a length of 1 meter and are scaled in this example by a factor of
149597870700, which means they will be 149597870700 m (1 AU) long, thus reaching the
same distance as Earth's orbit around the Sun.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "StaticScale_Example",
  Transform = {
    Scale = {
      Type = "StaticScale",
      Scale = 149597870700
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "StaticScale - Basic",
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


