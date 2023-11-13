# Asteroids
## How to add Asteroids/Comets to OpenSpace
To show the asteroid datasets, start OpenSpace with the "asteroids" profile from the launcher. The asteroids profile is similar to the default, but with 16 separate asset files that contain asteroid or comet orbits.

## Running OpenSpace with Asteroids/Comets
To start, double-click (or run from the terminal) `bin/Release/OpenSpace.exe`. The camera will be initially focused on Earth, so it is recommended to zoom out to a point where the solar system is visible. None of the asteroid/comet groups are visible by default. To enable one of these, expand the GUI's menus by selecting Scene -> Solar System -> Small Bodies. A list of all asteroid groups will be visible. Check one of the boxes to enable.

It is possible to modify the length of the orbital trail by adjusting the "Line fade" value in Renderable -> Appearance in the asteroid/comet group. A higher fade value shows more of the periodic orbital trails. The line color and width can also be changed here (transparency is accessible underneath 'Renderable').

Some of the asteroid categories contain a very high number of objects, which will affect frame rate and program responsiveness. If performance slows too much, then un-click the offending category to prevent it from being rendered.

## Additional Features
See the following pages for more detailed information and advanced usage of this content:
- [Ephemeris/Asteroids](ephemeris/asteroids)
- [Components/Satellites](satellites)

## Asteroid Content Categories
All trajectory data were obtained from the [JPL Small-Body Database (SBDB)](https://ssd.jpl.nasa.gov/sbdb.cgi). The following categories are defined on this site and were used to group the orbital data.

### Amor Asteroids
Earth-approaching Near-Earth Asteroids with orbits exterior to Earth's but interior to Mars'.

### Apollo Asteroids
Earth-crossing Near-Earth Asteroids with semi-major axes larger than Earth's.

### Aten Asteroids
Earth-crossing Near-Earth Asteroids with semi-major axes smaller than Earth's.

### Atira Asteroids
Near-Earth Asteroids whose orbits are contained entirely within the orbit of the Earth.

### Centaur Asteroids
Asteroids with either a perihelion or a semi-major axis between those of the four outer planets.

### Chiron-Type Comets
Comets with a Tisserand's parameter with respect to Jupiter of greater than 3 and a semi-major axis greater than that of Jupiter.

### Encke-Type Comets
Comets with a Tisserand's parameter with respect to Jupiter of greater than 3 and a semi-major axis less than that of Jupiter.

### Halley-Type Comets
Periodic comets with an orbital period between 20 and 200 years.

### Inner Main Asteroid Belt
Asteroids with a semi-major axis less than 2.0 au and a perihelion distance greater than 1.666 au.

### Jupiter Family Comets
Comets with a Tisserand's parameter with respect to Jupiter of between 2 and 3.

### Jupiter Trojan Asteroids
Asteroids trapped in Jupiter's L4/L5 Lagrange points (semimajor axis of between 4.6 and 5.5 au), with an eccentricity of less than 0.3.

### Main Asteroid Belt
Asteroids with a semi-major axis of between 2.0 and 3.2 au, and a perihelion distance greater than 1.666 au.

### Mars Crossing Asteroids
Asteroids that cross the orbit of Mars, with a semi-major axis of less than 3.2 au, and a perihelion distance of between 1.3 and 1.666 au.

### Outer Main Asteroid Belt
Asteroids with a semi-major axis of between 3.2 and 4.6 au.

### Potentially Hazardous Asteroids (PHAs)
Asteroids that are deemed potentially hazardous to Earth based on their close approaches. All asteroids with an Earth Minimum Orbit Intersection Distance (MOID) of 0.05 au or less, and with an absolute magnitude (H) of 22.0 or less.

### Trans-Neptunian Asteroids
Any minor or dwarf planets in the solar system that orbit the Sun at a greater average distance than Neptune (semi-major axis of 30.1 AU).
