# `openspace.openglCapabilities`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`extensions`](#openglCapabilitiesextensions-target)
    - [Returns all available extensions as a list of names]{#openglCapabilitiesextensions-list}


*   - [`glslCompiler`](#openglCapabilitiesglslCompiler-target)
    - [Returns the value of a call to `glGetString(GL_VENDOR)`]{#openglCapabilitiesglslCompiler-list}


*   - [`gpuVendor`](#openglCapabilitiesgpuVendor-target)
    - [Returns the vendor of the main graphics card]{#openglCapabilitiesgpuVendor-list}


*   - [`hasOpenGLVersion`](#openglCapabilitieshasOpenGLVersion-target)
    - [Tests whether the current instance supports the passed OpenGL version]{#openglCapabilitieshasOpenGLVersion-list}


*   - [`isExtensionSupported`](#openglCapabilitiesisExtensionSupported-target)
    - [Checks is a specific `extension` is supported or not]{#openglCapabilitiesisExtensionSupported-list}


*   - [`max2DTextureSize`](#openglCapabilitiesmax2DTextureSize-target)
    - [Returns the largest dimension for a 2D texture on this graphics card]{#openglCapabilitiesmax2DTextureSize-list}


*   - [`max3DTextureSize`](#openglCapabilitiesmax3DTextureSize-target)
    - [Returns the largest dimension for a 3D texture on this graphics card]{#openglCapabilitiesmax3DTextureSize-list}


*   - [`maxAtomicCounterBufferBindings`](#openglCapabilitiesmaxAtomicCounterBufferBindings-target)
    - [Returns the maximum number of atomic counter buffer bindings that are available on the main graphics card]{#openglCapabilitiesmaxAtomicCounterBufferBindings-list}


*   - [`maxShaderStorageBufferBindings`](#openglCapabilitiesmaxShaderStorageBufferBindings-target)
    - [Returns the maximum number of shader storage bindings that are available on the main graphics card]{#openglCapabilitiesmaxShaderStorageBufferBindings-list}


*   - [`maxTextureUnits`](#openglCapabilitiesmaxTextureUnits-target)
    - [Returns the maximum number of texture units that are available on the main graphics card]{#openglCapabilitiesmaxTextureUnits-list}


*   - [`maxUniformBufferBindings`](#openglCapabilitiesmaxUniformBufferBindings-target)
    - [Returns the maximum number of uniform buffer bindings that are available on the main graphics card]{#openglCapabilitiesmaxUniformBufferBindings-list}


*   - [`openGLVersion`](#openglCapabilitiesopenGLVersion-target)
    - [Returns the maximum OpenGL version that is supported on this platform]{#openglCapabilitiesopenGLVersion-list}

:::

## Functions

(openglCapabilitiesextensions-target)=
### [`extensions`](#openglCapabilitiesextensions-list)
Returns all available extensions as a list of names.


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.extensions()
:::
___

(openglCapabilitiesglslCompiler-target)=
### [`glslCompiler`](#openglCapabilitiesglslCompiler-list)
Returns the value of a call to `glGetString(GL_VENDOR)`. This will give detailed information about the vendor of the main graphics card. This string can be used if the automatic Vendor detection failed.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.glslCompiler()
:::
___

(openglCapabilitiesgpuVendor-target)=
### [`gpuVendor`](#openglCapabilitiesgpuVendor-list)
Returns the vendor of the main graphics card.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.gpuVendor()
:::
___

(openglCapabilitieshasOpenGLVersion-target)=
### [`hasOpenGLVersion`](#openglCapabilitieshasOpenGLVersion-list)
Tests whether the current instance supports the passed OpenGL version. The parameter has to have the form 'X.Y' or 'X.Y.Z'.


:::{card} Parameters


* version `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.hasOpenGLVersion(version)
:::
___

(openglCapabilitiesisExtensionSupported-target)=
### [`isExtensionSupported`](#openglCapabilitiesisExtensionSupported-list)
Checks is a specific `extension` is supported or not.


:::{card} Parameters


* extension `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.isExtensionSupported(extension)
:::
___

(openglCapabilitiesmax2DTextureSize-target)=
### [`max2DTextureSize`](#openglCapabilitiesmax2DTextureSize-list)
Returns the largest dimension for a 2D texture on this graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.max2DTextureSize()
:::
___

(openglCapabilitiesmax3DTextureSize-target)=
### [`max3DTextureSize`](#openglCapabilitiesmax3DTextureSize-list)
Returns the largest dimension for a 3D texture on this graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.max3DTextureSize()
:::
___

(openglCapabilitiesmaxAtomicCounterBufferBindings-target)=
### [`maxAtomicCounterBufferBindings`](#openglCapabilitiesmaxAtomicCounterBufferBindings-list)
Returns the maximum number of atomic counter buffer bindings that are available on the main graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.maxAtomicCounterBufferBindings()
:::
___

(openglCapabilitiesmaxShaderStorageBufferBindings-target)=
### [`maxShaderStorageBufferBindings`](#openglCapabilitiesmaxShaderStorageBufferBindings-list)
Returns the maximum number of shader storage bindings that are available on the main graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.maxShaderStorageBufferBindings()
:::
___

(openglCapabilitiesmaxTextureUnits-target)=
### [`maxTextureUnits`](#openglCapabilitiesmaxTextureUnits-list)
Returns the maximum number of texture units that are available on the main graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.maxTextureUnits()
:::
___

(openglCapabilitiesmaxUniformBufferBindings-target)=
### [`maxUniformBufferBindings`](#openglCapabilitiesmaxUniformBufferBindings-list)
Returns the maximum number of uniform buffer bindings that are available on the main graphics card.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.maxUniformBufferBindings()
:::
___

(openglCapabilitiesopenGLVersion-target)=
### [`openGLVersion`](#openglCapabilitiesopenGLVersion-list)
Returns the maximum OpenGL version that is supported on this platform.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.openglCapabilities.openGLVersion()
:::

