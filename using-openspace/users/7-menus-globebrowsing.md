# Using the Menus - Globebrowsing
This section will cover the available functionality when exploring worlds in the Solar System.

## Globe Properties
  - As with any dataset in OpenSpace, globes have their own specific properties under Renderable in the Scene menu.
  - There are many infrequently used settings. The most commonly used ones are:
    - '*Labels*': Some globes have labels that can be turned on or off. Labels are a special property of a globe and have their own internal properties.
    - '*Layers*': See the sections about Layers below.
    - '*Perform Shading*': When enabled, this setting will darken the globe based on the Sun. See [Lighting Conditions](#lighting-conditions) for more details.
    - '*Use Accurate Normals*': Used in conjunction with the '*Perform Shading*' setting, this setting will use the enabled '*Height Layers*' to further adjust the lighting conditions.
    - '*Eclipse*': To see an eclipse happen on a globe, you must enable this setting.
    - '*Eclipse Hard Shadows*': Used with the '*Eclipse*' setting, this setting will disable the smoothing at the edges of the eclipse sections.
    - '*Target Level of Detail Scale Factor*': This setting will adjust the level of detail that is loaded for maps in relation to the distance to the camera.
      - Lower values will make the map load faster, and give better performance, at the cost of map resolution.
      - Higher values will take longer to load and negatively impact performance, but will give a more detailed overall image.


## Layers and their Settings
  - Without layers, the globe will be just a gray sphere.
  - The layers of a globe are organized into categories.
    - '*ColorLayers*' are used to add maps and other visual information to the globe.
    - '*HeightLayers*' are used to deform the globe, sometimes referred to as a *Digital Elevation Model*
    - Some globes will have other special groups such as '*Overlays*' or '*WaterMasks*' on Earth.
  - The layers of a globe can be turned on or off by using the checkbox next to their name.
    - Enabled layers will be tinted with the highlight color.
  - Adjust the settings of a layer by clicking to open its submenu.
    - For ColorLayers, use the *Opacity*, *Gamma*, and *Multiplier* settings to change the way the layer appears.
    - For HeightLayers, use the *Gamma* and *Multiplier* settings to exaggerate the elevation. This can sometimes lead to unexpected rendering issues.
    - For HeightLayers, the *Offset* can be used to elevate one heightmap relative to another.


## Layer Ordering and Blending
  - The order of the layers in the menu represents the order that they are wrapped over the globe, like the layers of an onion.
    - The last layer in the menu list will appear as the outermost layer of the globe.
    - The first layer in the menu would be the innermost layer.
  - If multiple global layers are enabled, only the outermost one will be visible.
    - This becomes important when combining different maps that are multi-color/monochromatic or global/regional.
    - If a layer is monochromatic, its '*Blend Mode*' can be set to '*Color*' and its pixels will inherit the color values of the layer underneath it.
  - Regional layers must appear lower in the menu than global layers in order to combine them.


## Lighting Conditions
  - By default, globes will have the '*Perform Shading*' setting enabled, and thus will be lit based on their rotation and position relative to the Sun. To light a different part of the globe, you will need to move time forward or backward.
  - For times when you don't want to change the simulation time, you can disable the '*Perform Shading*' property of the globe.
  - If you want the globe to be brighter even when not shaded, try increasing the '*Multiplier*' setting of the innermost layer as described above.


## Atmospheres
  - Venus, Earth, Mars, and Titan have an atmosphere attached to their globe. The atmosphere is a separate item in the scene menu.
  - The atmosphere will affect the lighting conditions on the globe, even if 'Perform Shading' is not enabled.
  - To always have the area of the globe you are looking at lit when an atmosphere is enabled, you must enable the '*Enable Sun on Camera Position*' setting for the globe's atmosphere along with disabling the '*Perform Shading*' setting on the globe.
  - The only other common settings to change in an atmosphere would be '*Enable Hard Shadows for Eclipes*' when you are trying to visualize an eclipse, or '*Sun Intensity*' if you wish to brighten or dim the overall lighting of a globe.


## Special Layers on Earth
  - The default layer on Earth is a special "combo layer" — this means that it is actually two layers that will fade from one to the other based on a specific tile level. The "*ESRI VIIRS COMBO*" fades between the "*VIIRS SNPP (Temporal)*" layer and the "*ESRI World Imagery Layer*."
  - Earth has special layers in the "Overlay" group that show country features/names, coastlines, and more.
  - Earth has a special NightLayers group since we create light that is visible on the dark side of the planet.
  - The portion of the Earth that would be darkened by the '*Perform Shading*' section is instead rendered with a different map depicting city lights as visible from space.
  - If you wish to show a fully lit Earth at any simulation time, you must disable any night layers.


## Video
<iframe width="740" height="530" src="https://www.youtube.com/embed/Bx_urBYAEqA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
| ---------- | ----------- |
| 0:00 | Turn on and off the *Perform shading* setting. |
| 0:22 | Turn on and off *Use Accurate Normals* setting. |
| 1:39 | Turn on *Labels* on the Moon, which appear as you zoom closer. The Labels size and colors can be adjusted in the submenu. |
| 2:24 | Turn on and off *ColorLayers* and *HeightLayers*. |
| 3:51 | Earth's default combo layer "*ESRI VIIRS COMBO*" fades from the "*VIIRS SNPP (Temporal)*" layer to the "*ESRI World Imagery Layer*" when closer to the globe. This can be done manually using the opacity setting when both layers are enabled. |
| 4:58 | Earth's temporal layers, such as "*VIIRS SNPP (Temporal)*," will load as the date is changed. |
| 6:03 | Earth's *NightLayers* appear on the part of the globe not lit by the Sun. |
| 6:38 | Earth has special *Overlays* that, when enabled add annotations such the outline of countries. |
| 7:30 | Adjusting the lighting conditions on Mars. |
| 8:24 | Adjust the settings on Mars' *ColorLayers* to change the way the layers appear. |
| 9:49 | Adjust the blending settings on Mars' *ColorLayers* to change how multiple layers appear when enabled. |
