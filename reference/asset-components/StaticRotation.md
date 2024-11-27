



(base_transform_rotation_static)=
# StaticRotation

_Inherits [Rotation](#core_transform_rotation)_

A StaticRotation is using a fixed and constant rotation factor that does not change over time. The rotation value is provided as a property that can be changed at runtime, but it will not change automatically over time.


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

*   - `Rotation`
    - Stores the static rotation as a vector containing Euler angles, a quaternion representation, or a rotation matrix.  For the Euler angles, the values have to be provided in radians. To convert degres to radians, you can use the `math.rad` function.  For the Quaternion representation, the values have to be provided in the order (w, x, y, z).  For the matrix form, the provided matrix will be converted into Euler angles, an operation which might fail if the matrix is not a true rotation matrix. The values are assumed to be in row-major order.
    - `Vector3<double>, Vector4<double>, or Matrix3x3<double>`
    
    - Value of type 'Vector3<double>', Value of type 'Vector4<double>', or Value of type 'Matrix3x3<double>' 
    
    - {bdg-info}`No`
    
:::



### Inherited members from [Rotation](#core_transform_rotation)

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
    - The type of the rotation that is described in this element. The available types of rotations depend on the configuration of the application and can be written to disk on application startup into the FactoryDocumentation
    - `String`
    
    - Must name a valid Rotation type 
    
    - {bdg-info}`No`
    
:::








## Asset Examples


:::{dropdown} Euler Angles

This asset creates a rotation provided by Euler angles and applies it to a
SceneGraphNode that only displays coordinate axes. The rotation of the coordinate axes
are determined by a constant and unchanging static rotation.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "StaticRotation_Example_Euler",
  Transform = {
    Rotation = {
      Type = "StaticRotation",
      Rotation = { math.pi / 2.0, 0.0, math.pi }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "StaticRotation - Euler Angles",
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



:::{dropdown} Matrix

This asset creates a SceneGraphNode that only displays coordinate axes. The rotation of
the coordinate axes are determined by a constant and unchanging static rotation that is
provided by a 3-by-3 rotation matrix in column-major order.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 17

local Node = {
  Identifier = "StaticRotation_Example_Matrix",
  Transform = {
    Rotation = {
      Type = "StaticRotation",
      Rotation = {
        -0.9999987, -0.0015927, 0.0000000,
         0.0015927, -0.9999987, 0.0000000,
         0.0000000,  0.0000000, 1.0000000
      }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "StaticRotation - Matrix",
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



:::{dropdown} Quaternion

This asset creates a SceneGraphNode that only displays coordinate axes. The rotation of
the coordinate axes are determined by a constant and unchanging static rotation that is
provided by a four-dimensional quaternion.

:::{code-block} lua
:linenos:
:emphasize-lines: 5, 13

local Node = {
  Identifier = "StaticRotation_Example_Quaternion",
  Transform = {
    Rotation = {
      Type = "StaticRotation",
      Rotation = { 0.4873552, -0.4869268, -0.5127203, 0.5123526 }
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "StaticRotation - Quaternion",
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


