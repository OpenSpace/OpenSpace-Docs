



(base_transform_rotation_fixed)=
# FixedRotation

_Inherits [Rotation](#core_transform_rotation)_




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

*   - `Attached`
    - This is the name of the node that this rotation is attached to, this value is only needed if any of the three axis uses the Object type. In this case, the location of the attached node is required to compute the relative direction.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `XAxis`
    - This value specifies the direction of the new X axis. If this value is not specified, it will be computed by completing a right handed coordinate system from the Y and Z axis, which must be specified instead. If this value is a string, it is interpreted as the identifier of another scenegraph node. If this value is a 3-vector, it is interpreted as a direction vector
    - `String, or Vector3<double>`
    
    - Value of type 'String', or Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `XAxisInvert`
    - If this value is set to 'true', and the type is set to 'Object', the inverse of the pointing direction is used, causing the object to point away from the referenced object.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `XAxisOrthogonal`
    - This value determines whether the vector specified is used directly, or whether it is used together with another non-coordinate system completion vector to construct an orthogonal vector instead.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `YAxis`
    - This value specifies the direction of the new Y axis. If this value is not specified, it will be computed by completing a right handed coordinate system from the X and Z axis, which must be specified instead. If this value is a string, it is interpreted as the identifier of another scenegraph node. If this value is a 3-vector, it is interpreted as a direction vector
    - `String, or Vector3<double>`
    
    - Value of type 'String', or Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `YAxisInvert`
    - If this value is set to 'true', and the type is set to 'Object', the inverse of the pointing direction is used, causing the object to point away from the referenced object.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `YAxisOrthogonal`
    - This value determines whether the vector specified is used directly, or whether it is used together with another non-coordinate system completion vector to construct an orthogonal vector instead.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ZAxis`
    - This value specifies the direction of the new Z axis. If this value is not specified, it will be computed by completing a right handed coordinate system from the X and Y axis, which must be specified instead. If this value is a string, it is interpreted as the identifier of another scenegraph node. If this value is a 3-vector, it is interpreted as a direction vector
    - `String, or Vector3<double>`
    
    - Value of type 'String', or Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `ZAxisInvert`
    - If this value is set to 'true', and the type is set to 'Object', the inverse of the pointing direction is used, causing the object to point away from the referenced object.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ZAxisOrthogonal`
    - This value determines whether the vector specified is used directly, or whether it is used together with another non-coordinate system completion vector to construct an orthogonal vector instead.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
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


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 10
local CarringtonLongitudeToHEEQ180Rotation = {
  -- This is a rotation matrix to go from Carrington longitude referens frame to HEEQ180
  -- reference fram. At the reference time, MAS_seq = 0, 2000-07-14T08:33:37.105 the
  -- Carrington longitude was 309.3 degrees.
  -- Difference from HEEQ => 360-309.3=50.7
  -- (or 0-309.3 = -309.3 However this leads to the same rotation matrix in the end)
  -- Since OpenSpace supports HEEQ180 and not HEEQ, 180 was added or subtracted
  -- => a1 = -129.3 and a2 = 230.7
  -- Rotation matrix: (cos a, -sin a, 0)(sin a, cos a, 0)(0, 0, 1) leads to the result.
  Type = "FixedRotation",
  XAxis = { -0.63338087262755016203262119192353, -0.77384020972650618518999944537717, 0.0 },
  YAxis = { 0.77384020972650618518999944537717, -0.63338087262755016203262119192353, 0.0 },
  ZAxis = { 0.0, 0.0, 1.0 }
}

asset.export("CarringtonLongitudeToHEEQ180Rotation", CarringtonLongitudeToHEEQ180Rotation)



asset.meta = {
  Name = "Carrington Longitude To HEEQ180 Rotation",
  Description = "Contains a rotation for HEEQ180 to be used by another file",
  Author = "OpenSpace Team",
  URL = "http://openspaceproject.com",
  License = "MIT license"
}

:::
:::


