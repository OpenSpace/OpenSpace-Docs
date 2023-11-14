# Exoplanets
## About the Exoplanets Module
The exoplanets module includes the possibility of adding visualizations of confirmed exoplanets and their host stars to OpenSpace. The data comes from the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu) and includes a large range of properties on the exoplanet systems, often including uncertainty estimations. A table of the complete dataset can be found here: [Planetary Systems Composite Data](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars).

The visualizations are based on a thesis project done by Karin Reidarman in 2018.

## Adding exoplanet systems to OpenSpace
Exoplanet systems of interest must be added to OpenSpace individually. The reason for this is that it is impractical from a visualization standpoint to load all the systems in the database into OpenSpace on start-up, due to the large number of confirmed exoplanets.

Exoplanet systems can be added and removed during runtime through the Exoplanets GUI panel, with the symbol:

![Exoplanets GUI Symbol](exoplanet-gui-icon.png){w="1.5em" h="1.5em" class="only-light"}

![Exoplanets GUI Symbol](exoplanet-gui-icon_dark.png){w="1.5em" h="1.5em" class="only-dark"}

Added exoplanet systems, including scene graph nodes for individual planets, can be found in the Scene GUI under {menuselection}`Milky Way --> Exoplanets --> Exoplanet Systems`.

It is also possible to add exoplanet systems using the `openspace.exoplanets.addExoplanetSystem(name)` function in the OpenSpace scripting API, where the name of the system is the name of the host star. For example, `openspace.exoplanets.addExoplanetSystem("Kepler-11")` adds the Kepler-11 system, a system discovered in 2010 with a total of 6 confirmed orbiting the host star Kepler-11. Multiple systems can be added at once by specifying a list of host names as input, for example like `{"Kepler-11", "GJ 1061"}`. This function can be used to add exoplanets to OpenSpace before start-up.

## About the visualizations
The focus of the visualization lies on the composition of the exoplanet systems and the orbital properties of the planets, such as their eccentricity, semi-major axis and orbital period. The upper and lower uncertainty of the semi-major axis are also visualized by a band around the planet's orbit. The wider the band is, the more uncertain is the data on the semi-major axis of the orbit.

In the cases when there is data on the radius of a star/planet, they are visualized by a renderable globe with a corresponding radius. The color of the star is also computed from its effective color, ranging from coolest to hottest, red, yellow, white, and blue.

The habitable zone disk has three colors, with red and blue indicating optimistic boundaries and green a conservative boundary where liquid water may be possible. The habitable zone disk was computed using formulas and coefficients by Kopparapu et al (2015) *[Habitable Zones Around Main-Sequence Stars: Dependence on Planetary Mass](https://arxiv.org/abs/1404.5292])*.

### Resources
For more about exoplanets, see [NASA's 'What is an Exoplanet?'](https://exoplanets.nasa.gov/what-is-an-exoplanet/stars/)
