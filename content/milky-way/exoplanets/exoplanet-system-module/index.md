---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Exoplanet System Module

:::{image} exoplanet_module_icon_lighttheme.png
:align: left
:scale: 50%
:alt: Exoplanet module icon
:::


The exoplanets module enables the visualization of exoplanetary systems in OpenSpace. While the main [exoplanets](../exoplanets/index) data displays all the stars that have exoplanets with a simple, blue ring, the exoplanets module depicts the system of planets around these stars. This includes the planetary orbits, at the proper inclination, a depiction of the {term}`habitable zone`, and, when available, the planets themselves.


:::{figure} exoplanet_system_55cnc.png
:align: left
:alt: A rendition of the exoplanetary system 55 Cancri, with the orbits of the planests, the habitable zone, and the OpenSpace controls

A visualization of the planetary system around the star 55 Cancri along with the OpenSpace controls showing the exoplanetary system. This star is in the constellation Cancer and is about 55 light years from Earth. It has four planets, one of which lies inside the green habitable zone.
:::




## Adding systems

Unlike the main exoplanets data, where you see all the planetary systems from afar, with the exoplanets module you must add the systems you want to see. It would be too computationally expensive to load every planetary system, so you must load the ones you're interested in examining.


### 1. Bring up the exoplanets module panel

To load a system, click on ![Exoplanets module icon](exoplanet_module_icon_lighttheme.png){width="2.5em" height="1.5em" class="only-light"} to bring up the panel.


:::{figure} exoplanet_systems_panel.png
:align: left
:alt: A screenshot from OpenSpace showing the exoplanet module icon and panel.

A red indicator highlights the exoplanet module icon. Click on this symbol to open the exoplanet module panel.
:::


### 2. Search for the exoplanetary system

Inside the panel, search for the system you want to add by typing the name of the system where it says "Star name." In the image below, we typed "Kepler-11" which brings up all the text matches. (The Kepler-11 system, discovered in 2010, has a total of 6 confirmed planets orbiting the host star Kepler-11.)


:::{figure} exoplanet_systems_panel_search.png
:align: center
:width: 35%
:alt: A screenshot of the exoplanets panel with the results of a search for the star Kepler 11.

The exoplanets module panel with the results of a search for "Kepler-11," a multiplanet system around the star Kepler 11. 
:::





### 3. Add the system

Click on the desired system and then click the "Add System" button to the right. The system will then appear in the list of added systems at the bottom of the panel, and will also appear in the scene menu: \
{menuselection}`Scene -> Milky Way --> Exoplanets --> Exoplanet Systems`

:::{figure} exoplanet_systems_panel_added.png
:align: center
:width: 35%
:alt: The exoplanet module panel with the Kepler-11 system added

The exoplanet module panel with the Kepler-11 system added.
:::



:::{note}
Adding a system does not automatically display it on the screen. You must fly up to it, and it will take longer than you expect before it becomes visible to you---these systems are very small.
::: 



:::{dropdown} Adding systems via command line

It is possible to add exoplanet systems using the `openspace.exoplanets.addExoplanetSystem(name)` function in the OpenSpace scripting API. Here, `name` is the name of the host star to add, in our example the value of `name` would be "Kepler-11". So, the command would be typed:  
`openspace.exoplanets.addExoplanetSystem("Kepler-11")`

Executing this command in OpenSpace's command line results in adding the system. Multiple systems can be added by specifying a list of host names as input, for example, `{"Kepler-11", "GJ 1061"}`. 

This function may be used to add exoplanets to OpenSpace before start-up.
:::


### 4. Target the system and approach

Use the target button beside the added system to center on the exoplanetary system. Once you center on it, you can fly forward to visit it. It will take longer than you expect to see the system---keep flying forward.

Once you approach a system, it will appear similar to the image below for the Kepler-11 system. You see the host star at center, and the system of planetary orbits encircling it.

:::{figure} exoplanet_system_kepler11.png
:align: left
:alt: The Kepler-11 system with its six planets, and the habitable zone in green.

The Kepler-11 system of six planets with the yellowish host star, Kepler-11, and accompanying planetary orbits. Encircling the system is a diagram of the {term}`habitable zone`, with red and blue edges indicating its probable boundaries and a green center indicating where liquid water could exist.
:::



## Visualizing the exoplanetary systems

The exoplanets module renders planetary systems based on the orbital characteristics of the planets and the host's stellar type. The planet's eccentricity, semi-major axis, and orbital period are used to visualize the system. The wider the orbital path of a planet, the less certain the semi-major axis value. When there is information available on the radius of a planet, we draw a diagrammatic globe with the proper radius.

The host star is the the proper color, representing its stellar type, and it is necessary to dim the star as we pull into the system---just as we do in the Solar System. Dimming the star means it's no longer calibrated with the other stars. Once you pull away from the system, the star brightens up and is back on par with the other stars.

The {term}`habitable zone` is represented by a multicolored disk. Green indicates where liquid water could likely exist given the properties of the host star, though the zone can change with planetary mass as well. The red and blue edges represent the estimated edges of the zone. These are conservative estimates and could be refined with more atmospheric modeling.




## Dossier
:::{list-table}
:header-rows: 0
:class: full-width

* - **Census:**
  - 4,139 planets in 3,023 systems  CHECK THESE NUMBERS
* - **Asset File:**
  - `data/assets/modules/exoplanets/exoplanets.asset`
* - **OpenSpace Version:**
  - 6
* - **Reference:**
  - [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/index.html); [Habitable Zones Around Main-sequence Stars: Dependence on Planetary Mass](https://doi.org/10.1088/2041-8205/787/2/L29)
* - **Prepared by:**
  - Emma Broman, Karin Reidarman, OpenSpace Team
* - **License:**
  - [MIT license](https://github.com/OpenSpace/OpenSpace/blob/master/LICENSE.md)
:::
