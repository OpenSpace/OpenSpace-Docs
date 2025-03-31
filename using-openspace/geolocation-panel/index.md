---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# GeoLocation Panel: 

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::

:::{figure} toolbar_geolocation.png
:align: center
:alt: Toolbar with the Geo Location Panel highlighted

The Geo Location Panel Button in the OpenSpace Toolbar.
:::


Use the GeoLocation Panel to locate places on Earth and fly to them. The panel is straightforward with only few sections: the mode, the search area, and the Custom Coordinate section.

:::{figure} geolocation_panel.png
:align: center
:width: 50%
:figwidth: 80%
:alt: OpenSpace's GeoLocation Panel

The GeoLocation Panel in OpenSpace.
:::


## Mode

The Mode specifies the action implemented once you've chosen a place to go. There are three modes that result in different actions:
- {menuselection}`Fly To`: Upon choosing a place, this mode will do exactly what you think---fly you to the location.
- {menuselection}`Jump To`: This will fade the screen to black and fade back up centered over the chosen location.
- {menuselection}`Add Focus`: This adds a `GeoLocation` item to the Scene Panel and populates it with the chosen location. From that Scene Panel item you can choose to aim toward or fly to that location. In essence, this saves locations for you to use throughout your session and to return to later.



## Search

Enter a place or feature on Earth in the search box and hit the {menuselection}`Search` Button. Results will appear below, awaiting your selection.


:::{figure} geolocation_panel_search.png
:align: center
:width: 100%
:alt: OpenSpace's GeoLocation panel searching for Grand Canyon

OpenSpace's GeoLocation Panel with a search for "Grand Canyon."
:::


Once you choose a result, action will commence according to the Mode chosen. If you are in {menuselection}`Fly To` mode, then OpenSpace will fly you to the location. A blue `Cancel` button will appear in the Toolbar to cancel the flight if need be. The duraiton of the flight will also appear beside the plane icon.


:::{figure} geolocation_panel_flyto_button.png
:align: center
:width: 70%
:alt: OpenSpace's Stop Recording button

When OpenSpace is flying to a target automatically, a portion of the Toolbar will turn blue, and the duration of the transition will be shown, 10 seconds in this image, beside a Cancel Button.
:::


In {menuselection}`Jump To` mode, the screen will fade to black, then fade back up at your location.

:::{figure} geolocation_panel_flyto.png
:align: center
:width: 100%
:alt: OpenSpace's GeoLocation Panel flying to Grand Canyon

The GeoLocation Panel shown after locating, and flying to the Grand Canyon.
:::


If you choose the {menuselection}`Add Focus` Mode, the location will be added to the Scene Panel for you to target anytime in your session, but there will be no immediate action taken---your position will not immediately change.


:::{figure} geolocation_panel_add_focus.png
:align: center
:width: 100%
:alt: OpenSpace's GeoLocation Panel using the Add Focus

Using the Add Focus mode in the GeoLocation Panel adds a `GeoLocation` folder to the Scene Panel, and populates it with the searched location.
:::






