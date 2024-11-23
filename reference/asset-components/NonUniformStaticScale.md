



(base_scale_nonuniformstatic)=
# NonUniformStaticScale

_Inherits [Scale](#core_transform_scaling)_

This Scale type scales the scene graph node that it is attached to by a fixed amount that does not change over time. It is possible to change the fixed scale after starting the application, but it otherwise remains unchanged. The scaling is a simple multiplication so that a `Scale` value of 10 means that the object will be 10 times larger than its original size. In comparison to the StaticScale type, this type has the ability to scale an object by different amounts for each direction.

This type can be used to adjust the aspect ratio of Renderable types, for example to make a RenderableSphericalGrid that is not a perfect spherical grid, but a tri-axial ellipsoid instead.


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
    - These values are used as scaling factors for the scene graph node that this transformation is attached to relative to its parent.
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
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


:::{dropdown} Ellipsoid

This asset creates a SceneGraphNode that is rendering a sphere which is adjust to an
ellipsoidal shape by using a non-uniform scaling. In particular, the second axis is
half as long as the first, and the third axis is a third as long.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "NonUniformStaticScale_Example_Ellipsoid",
  Transform = {
    Scale = {
      Type = "NonUniformStaticScale",
      Scale = { 149597870700, 149597870700 / 2, 149597870700 / 3 }
    }
  },
  Renderable = {
    Type = "RenderableSphericalGrid"
  },
  GUI = {
    Name = "NonUniformStaticScale - Ellipsoid",
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

This asset creates a SceneGraphNode that only displays coordinate axes. The coordinate
axis normally have a length of 1 meter and are scaled in this example by different
values for each axis. The x axis is scaled by a factor of 149597870700,  which means
they will be 149597870700 m (1 AU) long and thus reaching the same distance as Earth's
orbit around the Sun. The y-axis stays at its original size, and the z-axis will be
hidden entirely by setting the scale value close to 0.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "NonUniformStaticScale_Example",
  Transform = {
    Scale = {
      Type = "NonUniformStaticScale",
      Scale = { 149597870700, 1.0, 0.0005 }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "NonUniformStaticScale - Basic",
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


