# Asteroids
This profile addon shows the trails of approximately 936,000 asteroids from the JPL Horizons [Small-Body Database (SBDB)](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/).

The asteroids are grouped into a number of categories. The [table below](#asteroid-content-categories) lists the categories of asteroids included in this addon, together with a description of each category.


## Showing the Asteroids in OpenSpace
The individual asteroid groups can be enabled/disabled using the {menuselection}`Scene --> Solar System --> Small Bodies` menu.

:::{note}
Some of the asteroid categories contain a very high number of objects, which will affect frame rate and program responsiveness. If performance slows too much, then deselect the offending category to prevent it from being rendered.
:::

Each asteroid trail is rendered as a line with a color corresponding to its group. It is possible to modify the length of the orbital trail by adjusting the "Trail fade" value in {menuselection}`Renderable --> Appearance` in the menu for asteroid/comet group. A higher fade value shows more of the periodic orbital trails. The trail color and width can also be changed here (opacity is accessible underneath 'Renderable').


## Asteroid Content Categories
All trajectory data were obtained from the [JPL Small-Body Database (SBDB)](https://ssd.jpl.nasa.gov/sbdb.cgi). The following categories are defined on this site and were used to group the orbital data.

| Category | Description |
| --- | --- |
| Amor Asteroids | Earth-approaching Near-Earth Asteroids with orbits exterior to Earth's but interior to Mars'. |
| Apollo Asteroids | Earth-crossing Near-Earth Asteroids with semi-major axes larger than Earth's. |
| Aten Asteroids | Earth-crossing Near-Earth Asteroids with semi-major axes smaller than Earth's. |
| Atira Asteroids | Near-Earth Asteroids whose orbits are contained entirely within the orbit of the Earth. |
| Centaur Asteroids | Asteroids with either a perihelion or a semi-major axis between those of the four outer planets. |
| Chiron-Type Comets | Comets with a Tisserand's parameter with respect to Jupiter of greater than 3 and a semi-major axis greater than that of Jupiter. |
| Encke-Type Comets | Comets with a Tisserand's parameter with respect to Jupiter of greater than 3 and a semi-major axis less than that of Jupiter. |
| Halley-Type Comets | Periodic comets with an orbital period between 20 and 200 years. |
| Inner Main Asteroid Belt | Asteroids with a semi-major axis less than 2.0 au and a perihelion distance greater than 1.666 au. |
| Jupiter Family Comets | Comets with a Tisserand's parameter with respect to Jupiter of between 2 and 3. |
| Jupiter Trojan Asteroids | Asteroids trapped in Jupiter's L4/L5 Lagrange points (semimajor axis of between 4.6 and 5.5 au), with an eccentricity of less than 0.3. |
| Main Asteroid Belt | Asteroids with a semi-major axis of between 2.0 and 3.2 au, and a perihelion distance greater than 1.666 au. |
| Mars Crossing Asteroids | Asteroids that cross the orbit of Mars, with a semi-major axis of less than 3.2 au, and a perihelion distance of between 1.3 and 1.666 au. |
| Outer Main Asteroid Belt | Asteroids with a semi-major axis of between 3.2 and 4.6 au. |
| Potentially Hazardous Asteroids (PHAs) | Asteroids that are deemed potentially hazardous to Earth based on their close approaches. All asteroids with an Earth Minimum Orbit Intersection Distance (MOID) of 0.05 au or less, and with an absolute magnitude (H) of 22.0 or less. |
| Trans-Neptunian Asteroids | Any minor or dwarf planets in the solar system that orbit the Sun at a greater average distance than Neptune (semi-major axis of 30.1 AU). |

## Additional Features
See the following pages under "Building Content" for more detailed information and advanced usage of this content:
  - [Ephemeris/Asteroids](/building-content/ephemeris/asteroids)
  - [Components/Satellites](/building-content/satellites)
