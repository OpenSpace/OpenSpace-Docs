



(globebrowsing_renderableglobe)=
# RenderableGlobe

_Inherits [Renderable](#renderable)_




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

*   - `Layers`
    - A list of layers that should be added to the globe.
    - `Table`
    
    -   [Table parameters](#RenderableGlobeLayers-target) 
    
    - {bdg-info}`No`
    
*   - `Labels`
    - Specifies information about planetary labels that can be rendered on the object's surface.
    - `Table`
    
    - [GlobeLabelsComponent](#globebrowsing_globelabelscomponent)
    
    - Yes
    
*   - `LightSourceNode`
    - The identifier of a scene graph node that should be used as the source of illumination for the globe. If not specified, the solar system's Sun is used.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `PerformShading`
    - Specifies whether the planet should be shaded by the primary light source or not. If disabled, all parts of the planet are illuminated. Note that if the globe has a corresponding atmosphere, there is a separate setting to control the shadowing induced by the atmosphere.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Radii`
    - The radii for this planet. If only one value is given, all three radii are set to that value.
    - `Vector3<double>, or Double`
    
    - Value of type 'Vector3<double>', or Value of type 'Double' 
    
    - Yes
    
*   - `RenderAtDistance`
    - Tells the rendering engine not to perform distance based performance culling for this globe. Turning this property on will let the globe to be seen at far away distances when normally it would be hidden.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Rings`
    - Details about the rings of the globe, if it has any.
    - `Table`
    
    - [RingsComponent](#globebrowsing_rings_component)
    
    - Yes
    
*   - `ShadowGroup`
    - Information about any object that might cause shadows to appear on the globe.
    - `Table`
    
    -   [Table parameters](#RenderableGlobeShadowGroup-target) 
    
    - Yes
    
*   - `Shadows`
    - 
    - `Table`
    
    - [ShadowComponent](#globebrowsing_shadows_component)
    
    - Yes
    
:::



### Inherited members from [Renderable](#renderable)

:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `DimInAtmosphere`
    - Decides if the object should be dimmed (i.e. faded out) when the camera is in the sunny part of an atmosphere.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Enabled`
    - Determines whether this object will be visible or not.
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Opacity`
    - This value determines the opacity of this renderable. A value of 0 means completely transparent
    - `Double`
    
    - In range: ( 0,1 ) 
    
    - Yes
    
*   - `RenderBinMode`
    - A value that specifies if the renderable should be rendered in the Background, Opaque, Pre-/PostDeferredTransparency, Overlay, or Sticker rendering step.
    - `String`
    
    - In list { Background, Opaque, PreDeferredTransparent, PostDeferredTransparent, Overlay } 
    
    - Yes
    
*   - `Tag`
    - A single tag or a list of tags that this renderable will respond to when setting properties
    - `Table, or String`
    
    - Value of type 'Table', or Value of type 'String' 
    
    - Yes
    
*   - `Type`
    - The type of the renderable.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::






(RenderableGlobeLayers-target)=
::::{dropdown} Table parameters for `Layers`
A list of layers that should be added to the globe.


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    - [LayerManager](#globebrowsing_layermanager)
    
    - {bdg-info}`No`
    
:::



::::
















(RenderableGlobeShadowGroup-target)=
::::{dropdown} Table parameters for `ShadowGroup`
Information about any object that might cause shadows to appear on the globe.


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Casters`
    - A list of potential shadow casters.
    - `Table`
    
    -   [Table parameters](#RenderableGlobeShadowGroupCasters-target) 
    
    - {bdg-info}`No`
    
*   - `Sources`
    - A list of objects (light sources) that may cause shadows from the provided list of shadow casting objects.
    - `Table`
    
    -   [Table parameters](#RenderableGlobeShadowGroupSources-target) 
    
    - {bdg-info}`No`
    
:::



(RenderableGlobeShadowGroupCasters-target)=
#### Table parameters for `Casters`
A list of potential shadow casters.


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableGlobeCasters*-target) 
    
    - Yes
    
:::



(RenderableGlobeCasters*-target)=
#### Table parameters for `*`



* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Name`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Radius`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::





(RenderableGlobeShadowGroupSources-target)=
#### Table parameters for `Sources`
A list of objects (light sources) that may cause shadows from the provided list of shadow casting objects.


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    -   [Table parameters](#RenderableGlobeSources*-target) 
    
    - Yes
    
:::



(RenderableGlobeSources*-target)=
#### Table parameters for `*`



* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Name`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Radius`
    - 
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::





::::






## Asset Examples


:::{dropdown} 

:::{code-block} lua
:linenos:
:emphasize-lines: 13
-- Basic
-- This asset creates a rotation that places a coordinate axes on the surface of a
-- planetary body. The rotation causes the coordinate axes to remain fixed to the surface
-- of the globe.
--
-- In order for this feature to work properly, the coordinate axes need to be located at
-- the same place as well, so this example also needs a `GlobeTranslation` applied.

-- The example needs a `RenderableGlobe` as a parent to function
local Globe = {
  Identifier = "GlobeRotation_Example_Globe",
  Renderable = {
    Type = "RenderableGlobe"
  },
  GUI = {
    Name = "GlobeRotation - Basic (Globe)",
    Path = "/Examples"
  }
}

local Node = {
  Identifier = "GlobeRotation_Example",
  Parent = "GlobeRotation_Example_Globe",
  Transform = {
    Translation = {
      Type = "GlobeTranslation",
      Globe = "GlobeRotation_Example_Globe",
      Latitude = 20.0,
      Longitude = -45.0
    },
    Rotation = {
      Type = "GlobeRotation",
      Globe = "GlobeRotation_Example_Globe",
      Latitude = 20.0,
      Longitude = -45.0
    }
  },
  Renderable = {
    Type = "RenderableCartesianAxes"
  },
  GUI = {
    Name = "GlobeRotation - Basic",
    Path = "/Examples"
  }
}

asset.onInitialize(function()
  openspace.addSceneGraphNode(Globe)
  openspace.addSceneGraphNode(Node)
end)

asset.onDeinitialize(function()
  openspace.removeSceneGraphNode(Node)
  openspace.removeSceneGraphNode(Globe)
end)

:::
:::


