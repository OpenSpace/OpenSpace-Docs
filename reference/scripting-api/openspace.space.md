# `openspace.space`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`convertFromRaDec`](#spaceconvertFromRaDec-target)
    - [Returns the cartesian world position of a ra dec coordinate with distance]{#spaceconvertFromRaDec-list}


*   - [`convertToRaDec`](#spaceconvertToRaDec-target)
    - [Returns the formatted ra, dec strings and distance for a given cartesian world coordinate]{#spaceconvertToRaDec-list}


*   - [`readKeplerFile`](#spacereadKeplerFile-target)
    - []{#spacereadKeplerFile-list}


*   - [`tleToSpiceTranslation`](#spacetleToSpiceTranslation-target)
    - [Takes the provided TLE file, converts it into a SPICE kernel and returns a
        SpiceTranslation instance that can be used to access the information in the TLE
        file using SPICE's superior integral solver]{#spacetleToSpiceTranslation-list}

:::

## Functions

(spaceconvertFromRaDec-target)=
### [`convertFromRaDec`](#spaceconvertFromRaDec-list)
Returns the cartesian world position of a ra dec coordinate with distance. If the coordinate is given as strings the format should be ra 'XhYmZs' and dec 'XdYmZs'. If the coordinate is given as numbers the values should be in degrees.


:::{card} Parameters


* rightAscension `Number | String` 



* declination `Number | String` 



* distance `Number` 


:::

Return type: `vec3` 

:::{code-block} lua
:caption: Signature
openspace.space.convertFromRaDec(rightAscension, declination, distance)
:::
___

(spaceconvertToRaDec-target)=
### [`convertToRaDec`](#spaceconvertToRaDec-list)
Returns the formatted ra, dec strings and distance for a given cartesian world coordinate.


:::{card} Parameters


* x `Number` 



* y `Number` 



* z `Number` 


:::

Return type: `(String, String, Number)` 

:::{code-block} lua
:caption: Signature
openspace.space.convertToRaDec(x, y, z)
:::
___

(spacereadKeplerFile-target)=
### [`readKeplerFile`](#spacereadKeplerFile-list)



:::{card} Parameters


* p `Path` 



* type `String` 


:::

Return type: `Table[]` 

:::{code-block} lua
:caption: Signature
openspace.space.readKeplerFile(p, type)
:::
___

(spacetleToSpiceTranslation-target)=
### [`tleToSpiceTranslation`](#spacetleToSpiceTranslation-list)
Takes the provided TLE file, converts it into a SPICE kernel and returns a
        SpiceTranslation instance that can be used to access the information in the TLE
        file using SPICE's superior integral solver.

        The second return value is the spice kernel that should be loaded and unloaded by
        whoever called this function.


:::{card} Parameters


* tlePath `String` 


:::

Return type: `{ Translation, SpiceKernel }` 

:::{code-block} lua
:caption: Signature
openspace.space.tleToSpiceTranslation(tlePath)
:::

