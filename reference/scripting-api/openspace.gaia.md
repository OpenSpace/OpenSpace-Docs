# `openspace.gaia`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addClippingBox`](#gaiaaddClippingBox-target)
    - [Creates a clipping box for the Gaia renderable in the first argument]{#gaiaaddClippingBox-list}


*   - [`addClippingSphere`](#gaiaaddClippingSphere-target)
    - [Creates a clipping sphere for the Gaia renderable in the first argument]{#gaiaaddClippingSphere-list}


*   - [`removeClippingBox`](#gaiaremoveClippingBox-target)
    - []{#gaiaremoveClippingBox-list}

:::

## Functions

(gaiaaddClippingBox-target)=
### [`addClippingBox`](#gaiaaddClippingBox-list)
Creates a clipping box for the Gaia renderable in the first argument


:::{card} Parameters


* name `String` 



* size `vec3` 



* position `vec3` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.gaia.addClippingBox(name, size, position)
:::
___

(gaiaaddClippingSphere-target)=
### [`addClippingSphere`](#gaiaaddClippingSphere-list)
Creates a clipping sphere for the Gaia renderable in the first argument


:::{card} Parameters


* name `String` 



* radius `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.gaia.addClippingSphere(name, radius)
:::
___

(gaiaremoveClippingBox-target)=
### [`removeClippingBox`](#gaiaremoveClippingBox-list)



Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.gaia.removeClippingBox()
:::

