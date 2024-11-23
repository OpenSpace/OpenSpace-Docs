# `openspace.spice`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`convertTLEtoSPK`](#spiceconvertTLEtoSPK-target)
    - [This function converts a TLE file into SPK format and saves it at the provided path]{#spiceconvertTLEtoSPK-list}


*   - [`kernels`](#spicekernels-target)
    - [Returns a list of all loaded kernels]{#spicekernels-list}


*   - [`loadKernel`](#spiceloadKernel-target)
    - [Loads the provided SPICE kernel by name]{#spiceloadKernel-list}


*   - [`position`](#spiceposition-target)
    - [Returns the position for a given body relative to another body, in a given frame of reference, at a specific time]{#spiceposition-list}


*   - [`rotationMatrix`](#spicerotationMatrix-target)
    - [Returns the rotationMatrix for a given body in a frame of reference at a specific time]{#spicerotationMatrix-list}


*   - [`spiceBodies`](#spicespiceBodies-target)
    - [Returns a list of Spice Bodies loaded into the system]{#spicespiceBodies-list}


*   - [`unloadKernel`](#spiceunloadKernel-target)
    - [Unloads the provided SPICE kernel]{#spiceunloadKernel-list}

:::

## Functions

(spiceconvertTLEtoSPK-target)=
### [`convertTLEtoSPK`](#spiceconvertTLEtoSPK-list)
This function converts a TLE file into SPK format and saves it at the provided path. The last parameter is only used if there are multiple craft specified in the provided TLE file and is selecting which (0-based index) of the list to create a kernel from.

This function returns the SPICE ID of the object for which the kernel was created


:::{card} Parameters


* tle `Path` 



* spk `Path` 



* elementToExtract `Integer?` - Default value: `0` 


:::

Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.spice.convertTLEtoSPK(tle, spk, elementToExtract)
:::
___

(spicekernels-target)=
### [`kernels`](#spicekernels-list)
Returns a list of all loaded kernels


Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.spice.kernels()
:::
___

(spiceloadKernel-target)=
### [`loadKernel`](#spiceloadKernel-list)
Loads the provided SPICE kernel by name. The name can contain path tokens, which are automatically resolved.


:::{card} Parameters


* kernel `String | String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.spice.loadKernel(kernel)
:::
___

(spiceposition-target)=
### [`position`](#spiceposition-list)
Returns the position for a given body relative to another body, in a given frame of reference, at a specific time. Example: openspace.spice.position('INSIGHT', 'MARS',' GALACTIC', '2018 NOV 26 19:45:34')


:::{card} Parameters


* target `String` 



* observer `String` 



* frame `String` 



* date `String` 


:::

Return type: `vec3` 

:::{code-block} lua
:caption: Signature
openspace.spice.position(target, observer, frame, date)
:::
___

(spicerotationMatrix-target)=
### [`rotationMatrix`](#spicerotationMatrix-list)
Returns the rotationMatrix for a given body in a frame of reference at a specific time. Example: openspace.spice.rotationMatrix('INSIGHT_LANDER_CRUISE','MARS', '2018 NOV 26 19:45:34')


:::{card} Parameters


* body `String` 



* frame `String` 



* date `String` 


:::

Return type: `mat3x3` 

:::{code-block} lua
:caption: Signature
openspace.spice.rotationMatrix(body, frame, date)
:::
___

(spicespiceBodies-target)=
### [`spiceBodies`](#spicespiceBodies-list)
Returns a list of Spice Bodies loaded into the system. Returns SPICE built in frames if builtInFrames. Returns User loaded frames if !builtInFrames.


:::{card} Parameters


* includeBuiltIn `Boolean` 


:::

Return type: `String -> String` 

:::{code-block} lua
:caption: Signature
openspace.spice.spiceBodies(includeBuiltIn)
:::
___

(spiceunloadKernel-target)=
### [`unloadKernel`](#spiceunloadKernel-list)
Unloads the provided SPICE kernel. The name can contain path tokens, which are automatically resolved.


:::{card} Parameters


* kernel `String | String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.spice.unloadKernel(kernel)
:::

