# Renderable Stars
The `RenderableStars` class requires a few different data variables in the SPECK file. The mapping between the internal name and the name of the variable in the SPECK file can be specified in the `.asset` file.  The combination of selected rendering parameter determines which values are necessary:

| Size Composition             | Color Option  | Required Data Value |
| ---------------------------- | ------------- | ------------------- |
| App Brightness               | Color         | luminance
| Lum and Size                 | Color         | bv, luminance, absoluteMagnitude
| Lum, Size and App Brightness | Color         | bv, luminance, absoluteMagnitude
| Abs Magnitude                | Color         | bv, absoluteMagnitude
| App Magnitude                | Color         | bv, absoluteMagnitude
| **Distance Modulus**         | **Color**     | bv, absoluteMagnitude
| App Brightness               | Velocity      | luminance, vx, vy, vz
| Lum and Size                 | Velocity      | luminance, absoluteMagnitude,  vx, vy, vz
| Lum, Size and App Brightness | Velocity      | bv, luminance, absoluteMagnitude,  vx, vy, vz
| Abs Magnitude                | Velocity      | absoluteMagnitude,  vx, vy, vz
| App Magnitude                | Velocity      | absoluteMagnitude,  vx, vy, vz
| Distance Modulus             | Velocity      | absoluteMagnitude,  vx, vy, vz
| App Brightness               | Speed         | luminance, speed
| Lum and Size                 | Speed         | luminance, absoluteMagnitude, speed
| Lum, Size and App Brightness | Speed         | bv, luminance, absoluteMagnitude, speed
| Abs Magnitude                | Speed         | absoluteMagnitude, speed
| App Magnitude                | Speed         | absoluteMagnitude, speed
| Distance Modulus             | Speed         | absoluteMagnitude, speed
| App Brightness               | Other Data    | luminance, <other data>
| Lum and Size                 | Other Data    | luminance, absoluteMagnitude, <other data>
| Lum, Size and App Brightness | Other Data    | bv, luminance, absoluteMagnitude, <other data>
| Abs Magnitude                | Other Data    | absoluteMagnitude, <other data>
| App Magnitude                | Other Data    | absoluteMagnitude, <other data>
| Distance Modulus             | Other Data    | absoluteMagnitude, <other data>
| App Brightness               | Fixed Color   | luminance
| Lum and Size                 | Fixed Color   | luminance, absoluteMagnitude
| Lum, Size and App Brightness | Fixed Color   | bv, luminance, absoluteMagnitude
| Abs Magnitude                | Fixed Color   | absoluteMagnitude
| App Magnitude                | Fixed Color   | absoluteMagnitude
| Distance Modulus             | Fixed Color   | absoluteMagnitude

The **bold** values denote the default value for the stars.asset distributed with OpenSpace
