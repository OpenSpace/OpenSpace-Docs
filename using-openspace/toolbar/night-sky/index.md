---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---

# Night Sky Panel

![Tour Panel Button](/using-openspace/toolbar/night-sky/toolbar_button_nightsky.png)

{menuselection}`Windows --> Night Sky`




The Night Sky Panel provides a customized set of functions that simulate the night sky and add tools to understand the motions of the sun, moon, planets, and stars throughout the course of the day and year.

:::{admonition} Night Sky Profile
A [nightsky profile](/profiles/night-sky/index) exists that is tailored toward using the Night Sky Panel. It is not necessary to use this profile if you want to use the panel, but it offers some default settings that set you up upon launch to have a night sky view.
:::

::::::{admonition} Planetarium Versus Rectangular Mode
The Night Sky Panel offers functionality that is inherently optimized for a planetarium setting. It can be used in OpenSpace's default rectangular mode that launches on your desktop computer, but offers more insight when used in a fish-eye mode on the desktop. A fish-eye view will replicate a planetarium view on your desktop.


:::{figure} night_sky_two_panel_view.png
:align: left
:width: 100%
:alt: Night Sky rectangular view

Two renditions of the night sky. The rectangular mode (left) seen when loading the default OpenSpace window settings, and the fish-eye view (right) when starting OpenSpace with the `single_fisheye` Window Option in the Launcher.
:::

<br>

Each view has its strengths. Fish-eye will display the entire sky giving you a sense of what's up and when objects and constellations rise and set. The rectangular view will allow you to focus on one part of the sky to see, for example, the setting of the Sun, Moon, and planets on the western horizon, or other more localized phenomena.
::::::

The panel is divided into six subpanels. Each tabbed subpanel offers functionality around displaying cardinal points and coordinate systems, buttons to change time and position, and changing the appearance of the Sun, stars, and solar system objects.


## Markings Tab

The Markings tab enables the display of lines, grids, labels, and other elements that lend themselves to understanding the sky as a map. These include the cardinal directions, various coordinate systems projected on the sky, and the mapping of the constellations in the night sky.

:::{figure} night_sky_panel_markings.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Markings tab

The Markings tab in OpenSpace's Night Sky Panel.
:::

### Alt/Az

Alt/Az is the shorthand for the Altitude-Azimuth coordinate system. Alt/Az is a local coordinate system based on your location on Earth. Altitude is measured from your horizon, with 0&deg; at the horizon and 90&deg; located at your zenith, the point directly above your head. Azimuth is measured as the angle from true north around the horizon. The {math}`(Alt, Az) = (0^\circ, 0^\circ)` point is on your horizon in the direction of true north. The meridian is the line that passes through due north and due south and, hence, your zenith point too.


### Ecliptic

Ecliptic coordinates are based on Earth's orbital plane centered on the Sun. The "equator" is called the *ecliptic* and, from our point of view, is the path of the Sun in the sky. The 0&deg; longitude line, called the prime meridian on Earth, is defined by a line that crosses through the March equinox. A given object can be described by its ecliptic longitude and latitude in this system.


### Equatorial

The equatorial coordinate system is a popular system to pinpoint objects in the sky. Latitude in equatorial coordinates is merely a projection of Earth's latitude in the sky, and is called *declination*. So, 90&deg; north declination is directly above the North Pole, and the Celestial Equator, 0&deg; declination, is above Earth's equator.

Longitude in this system is a bit different and, given there are 24 hours in a day, is expressed in hours, minutes, and seconds. The lines of longitude in the equatorial system are called *right ascension,* and a typical location might be expressed {math}`RA = (14^h \; 23^m \; 56.2^s)`. The primary direction is toward the March equinox, so the {math}`(RA, Dec) = (0^h, 0^\circ)` point is where the celestial equator crosses that equinox point.

Astronomers use this coordinate system most often to describe the location of objects in the sky.


### Constellations

The constellations section provides buttons to toggle the constellation data on and off. {menuselection}`Lines` will bring up the [familiar lines](/content/milky-way/constellations/constellation-lines/index) that trace the constellation figures. {menuselection}`Art` turns on the [artwork for the constellations](/content/milky-way/constellations/constellation-art/index). {menuselection}`Grid` will show the [constellation boundaries](/content/milky-way/constellations/constellation-boundaries/index). And {menuselection}`Labels` show each constellation's label. These buttons provide a convenient place to control these functions which otherwise exist in the [Scene Panel](/using-openspace/toolbar/scene/index) or the [Actions Panel](/using-openspace/toolbar/actions/index).


:::{figure} constellation_anatomy.png
:align: left
:width: 100%
:alt: Constellations in OpenSpace

Anatomy of a constellation. Lines connect stars that make up the figure, art gives us a picture of the constellation, labels can be turned on to show each constellation's name, and we can see the boundaries of each constellation in yellow.
:::



### Cardinal Directions
Displys the cardinal points---north, south, east, west---on the horizon as N, S, E, W. There are two sizes, and you can add tick marks on the horizon with the Marks button.





## Time Tab

The Time tab has some preset buttons to conveniently change the simulation time.

:::{admonition} Solar and Sidereal Time
Time can be measured in the sky by observing the length of time it takes for an object to return to the same spot in the sky. This, of course, is determined by Earth's rotation and its revolution around the Sun.

If we consider when a distant star, say Sirius in Canis Major, crosses our local meridian, the line that crosses due north and south on your horizon and your zenith point directly above your head, we can call the time between two such crossings one *sidereal day*. This is how long Earth takes to rotate once relative to the distant stars and is 23 hours, 56 minutes, and 4.1 seconds.

When we measure how long it takes the Sun to make two such crossings of the local meridian, or the time between two successive local noons, we call that the *solar day*. Because Earth also revolves around the sun, it takes a little longer for two such crossings---about 24 hours. And, this is really the mean solar day, because Earth speeds up and slows down over the course of its eccentric orbit around the Sun.

In OpenSpace, the practical meaning of these two systems of time is if you advance time in solar days, you will see the stars rise and set along with the motion of the planets, Sun, and Moon. If you advance by sidereal days, the stars will remain fixed in the sky and the motions of the Sun, Moon, and planets will move against a stationary starry sky.
:::


:::{figure} night_sky_panel_time.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Time tab

The Time tab in OpenSpace's Night Sky Panel.
:::

### Simulation Time
The simulation time is displayed in UTC, which mirrors the time on the Toolbar. Also, more importantly, it is displayed in local time with the time zone specified. This is the time you'll use to calibrate what you want to see in the night sky.

### Jumps
This section has buttons that allow you to jump forward or backward in time. You can alter the view by sidereal time or solar time. If we want to see the rising and the setting of the stars, along with the motions of the Sun, Moon, and planets, it makes sense to adjust by solar day. If we want to examine the motion of the Sun, Moon, and planets against the night sky, advance time by sidereal day.

### Diurnal Motion
Diurnal motion refers to the apparent motion of the stars and planets across the sky in the course of the day. In this section, there are preset buttons to move time forward 1, 2, or 5 minutes per second. And, there are buttons to play or pause time and return to realtime (1 second per second).

:::{tip}
Use the [Time Panel](/using-openspace/toolbar/time/index) for access to all the time controls in OpenSpace.
:::






## Location / View Tab

The Location / View tab shows your location status, and provides buttons for preset locations and views from that location.


:::{figure} night_sky_panel_location.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Location / View tab

The Location / View tab in OpenSpace's Night Sky Panel.
:::


### Globe Location
This section shows your location status. The map displays where you are, indicated by the OpenSpace icon, along with the day/night portions of Earth. The precise latitude and longitude (and altitude, though that is less relevant when night sky viewing) are also listed.

The icon will move as you move across Earth. However, if you want total control of your location or to move to a specific place, use the ![GeoLocation Panel Button](/using-openspace/toolbar/geolocation/toolbar_button_geolocation.png){height=20px} [GeoLocation Panel](/using-openspace/toolbar/geolocation/index).


### Jump to Position
The Jump to Position section consists of buttons that take you instantaneously to the North Pole, South Pole, and Equator. These points are important positional extremes that show how the sky looks and moves from the poles or the equator. 

At the poles, of course, the celestial north or south pole is directly above one's head and the equator is on the horizon. The sky moves in a circular fashion, like a slow-moving kaleidoscope as Earth spins on its axis. Here, the stars, except for the Sun, do not rise and set but, instead, form circlular paths on the sky.

At the equator, all the stars, planets, and the Moon rise and set. The poles lie on the horizon at due north and south, respectively. The celestial equator, where {math}`declination = 0^\circ`, stretches across the sky from due east to due west, and intersects the zenith, the point directly above one's head.

### Direction
These buttons will center your view on the four cardinal points. If you're in fish-eye mode, it brings the chosen direction to the bottom of the window. If you press the {menuselection}`Look South` button, for example, then the sky will rotate such that south is at the bottom of the screen. In rectangular mode, pressing one of these buttons will aim you toward that direction.

### Horizon
These buttons reorient you relative to the horizon. {menuselection}`Look at Horizon` will bring the horizon into view. {menuselection}`Look Up` will orient your view toward the zenith. And, {menuselection}`Level the Horizon` will... level the horizon relative to your view. These aren't as relevant in the fish-eye view becasue you always see the entire sky and the full horizon in that view.



:::{tip}
Use the ![GeoLocaiton Panel Button](/using-openspace/toolbar/geolocation/toolbar_button_geolocation.png){h=20px} [GeoLocation Panel](/using-openspace/toolbar/geolocation/index) to fine-tune the control of your location on Earth.
:::

## Stars Tab

The Stars tab handles the visibility properties of the [stars](/content/milky-way/stars/stars/index).

:::{figure} night_sky_panel_stars.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Stars tab

The Stars tab in OpenSpace's Night Sky Panel.
:::

### Visibility
Two buttons specify when the stars are visible. On by default, the {menuselection}`Show Stars` checkbox turns the stars on and off. The {menuselection}`Show During Day` checkbox keeps the stars visible after the sun rises in the sky, so you see the stars during daytime.

### Star Labels
The stars have two sets of labels. The {menuselection}`Show Labels` checkbox turns on the [star names](/content/milky-way/stars/star-labels/index), like Sirius, Betelgeuse, and Vega. The {menuselection}`Show Alternate Labels` checkbox displays the more technical names for the stars, as in Alpha Canis Majoris, Alpha Orionis, or Alpha Lyrae, what we call [alternate star labels](/content/milky-way/stars/star-labels-alternate/index). 

### Appearance
The buttons in the Appearance section concern the look of the stars. 

The default settings resemble those of the stars when you launch OpenSpace. These have two images that make up the look of the star, a core image and a glow image; the larger these are, the brighter the star. Restore this view using the {menuselection}`Default Settings` button.

Many paper star atlases use a more primative system of discrete dots to represent the stars. The larger the dot, the brighter the star. The {menuselection}`More Point-like Stars` button will give you this visual quality to the stars.

:::{note}
The Appearance section of the Stars tab only appears when the [nightsky profile](/profiles/night-sky/index) is loaded.
:::

:::{figure} nightsky_stars_types.png
:align: left
:width: 100%
:figwidth: 100%
:alt: OpenSpace's Night Sky star types

Two renditions of the stars in the night sky, one the standard with a core-glow appearance (left), the other as point-like stars (right).
:::



## Solar System Tab

The Solar System tab controls how the Sun, Moon, and planets appear.

:::{figure} night_sky_panel_solar_system.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Solar System tab

The Solar System tab in OpenSpace's Night Sky Panel.
:::

### Trails
Trails are the lines that trace out the paths of the planets. There are times you may want trails on, to see the path of a planet across the sky, and other times when those paths may clutter your view. 

The paths do fade over the planet's orbit. To increase the visibility of the trail over time, adjust the planet's trail in Scene Panel to brighten them up over time. For example: \
{menuselection}`Scene --> Solar System --> Venus --> Venus Trail --> Period`

### Planet Labels
Use these buttons to show or hide the labels for the planets and Moon.

### Planets
When we're exploring the planets in 3-D space, we want to see the planets as they are, with their respective surface imagery and detail. However, when we're viewing the planets from the night sky, we need them to accurately represent how we see them in a dark sky. This view is called Night Sky Planets, and is toggled on and off with these buttons.

### Moon
We may want to see the Moon differently from the night sky. For one, it helps to enlarge the Moon to see it in the sky. The Moon is set to its accurate size by default, but it can be helpful to enlarge it to make it more prominent in the sky. The {menuselection}`+` and {menuselection}`-` buttons allow you to customize the size you want. The {menuselection}`Show Phase`, on by default, toggles whether the Moon's phase is displayed, or if it appears fully lit.


## Sun Tab

The Sun tab controls the appearance of the Sun and can add trails that delineate the Sun's path in the sky.

:::{figure} night_sky_panel_sun.png
:align: right
:width: 100%
:figwidth: 40%
:alt: OpenSpace's Night Sky Panel's Sun tab

The Sun tab in OpenSpace's Night Sky Panel.
:::

### Glare
When you have a night sky view in OpenSpace, it can be helpful to change the appearance of the Sun in the sky to be less realistic and more diagrammatic. On by default, the Sun's glare is a glow of light surrounding the Sun. When viewing the sky from Earth, it may be helpful to turn that glare off and see the Sun as a discrete object in the sky.

### Size
In addition to the glare, it can be helpful to increase the size of the Sun as perceived from Earth. There are some preset buttons that do this: {menuselection}`Large Angular Size` and {menuselection}`Extra Large Angular Size`, and you can customize the size using the {menuselection}`+` and {menuselection}`-` buttons.

### Sun Trails
You can add a trail for the Sun's path. Two preset trails are the {menuselection}`Add Trail for Simulation Date` and {menuselection}`Add Trail for Today`. The former adds a trail for the Sun's path in the sky on the date in OpenSpace, whatever time is displayed in the Toolbar, the latter will add a trail for today's calendar date in the real world that you live in.

You can add a custom trail using the Choose Date window and the dropdown calendar to choose a date, then press the {menuselection}`Add Trail` button to see it in OpenSpace. 

Once you add a trail, it will appear in the Added Sun Trails list. From that list, you can navigate to them, and delete them from the list. Note, too, that you can access these trails in the Scene Panel under {menuselection}`Scene --> Night Sky --> Sun Trails`.
