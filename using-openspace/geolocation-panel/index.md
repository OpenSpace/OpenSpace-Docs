---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# GeoLocation Panel: Pinpoint a Place

:::{figure} toolbar_geolocation.png
:align: center
:width: 1000px
:alt: Toolbar with the Geo Location Panel highlighted

The Geo Location Panel Button in the OpenSpace Toolbar.
:::


Use the GeoLocation Panel to locate places on Earth and fly to them. The panel is straightforward with only few sections: the search area, the Custom Coordinate section, and a list of any added nodes. There is also a section at the top for selecting the anchor (globe) for which to search and/or add nodes for. At the time of writing, only Earth is supported.

:::{figure} geolocation_panel.png
:align: center
:width: 400px
:alt: OpenSpace's GeoLocation Panel

The GeoLocation Panel in OpenSpace.
:::

## Search

Enter a place or feature on Earth in the search box and hit the {menuselection}`Search` Button. Results will appear below, awaiting your selection.


:::{figure} geolocation_panel_search.png
:align: center
:width: 1000px
:alt: OpenSpace's GeoLocation panel searching for Grand Canyon

OpenSpace's GeoLocation Panel with a search for "Grand Canyon."
:::

For each search result in the list, there are three buttons that result in different actions:
- ![Fly to button](geolocation_panel_button_flyto.png){w=1em} {menuselection}`Fly To`: Automatically fly to the selected location. A `Cancel` button will appear in the Toolbar to cancel the flight if need be. The duration of the flight will also appear beside the plane icon.
:::{figure} geolocation_panel_flyto_button.png
:align: center
:width: 300px
:alt: OpenSpace's Stop Recording button
When OpenSpace is flying to a target automatically, a portion of the Toolbar will change, and the duration of the transition will be shown, 8 seconds in this image, beside a Cancel Button.
:::

- ![Jump to button](geolocation_panel_button_jumpto.png){w=1em} {menuselection}`Jump To`: This will fade the screen to black and fade back up centered over the chosen location.
- ![Add focus button](geolocation_panel_button_addfocus.png){w=1em} {menuselection}`Add Focus`: This adds a `GeoLocation` item for the chosen location to the scene. It will show in the list of added nodes, but also in the Scene Panel under `GeoLocation`. From that item you can choose to aim toward or fly to that location. In essence, this saves locations for you to use throughout your session and to return to later.

If you choose the {menuselection}`Add Focus` option, the location will be added to the Scene Panel and Added Nodes list for you to target anytime in your session, but there will be no immediate action taken---your position will not immediately change.



:::{figure} geolocation_panel_add_focus.png
:align: center
:width: 1000px
:alt: OpenSpace's GeoLocation Panel using the Add Focus

Using the Add Focus mode in the GeoLocation Panel adds a `GeoLocation` folder to the Scene Panel, and populates it with the searched location. It is also added to the list of added nodes.
:::



## Custom Coordinate

You can also enter a specific coordinate and fly to that location using the Custom Coordinates tag. Enter the latitude, longitude, and altitude above Earth, as well as an optional name for the position. Then, you may do any of the following actions as explained above: {menuselection}`Fly To`, {menuselection}`Jump To` or {menuselection}`Add Focus`.

:::{figure} geolocation_panel_custom_coordinates.png
:align: center
:width: 400px
:alt: The Curtom Coordinates tab in OpenSpace's GeoLocation Panel

The Custom Coordinates tab can be used to add or fly to a location based on a customly given latitude and longitude coordinate.
:::



