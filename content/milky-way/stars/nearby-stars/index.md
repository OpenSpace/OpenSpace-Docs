# Nearby Stars
{menuselection}`Scene --> Milky Way --> Stars --> Nearby Stars`

::::::{tab-set}
:::::{tab-item} Overview

## Overview

The Nearby Stars is, more formally, the Gaia Catalog of Nearby Stars (GCNS). Gaia is a revolutionary mission to get precise information on the brightnesses, positions, and motions of billions of stars. See the index page on [Stars](content--milky-way--stars--gaia) for more information on the Gaia mission and data release.



:::{figure} gcns_extent_constellation_lines.png
:align: left
:alt: The nearby stars along with the constellation lines.

The brightened Nearby Stars as seen from about 1,500 light years away. This sample of stars is limited to 100 parsecs, or 326 light years. Here, we see them in concert with contextural grids and the lines of the constellations, to provide scale and remind ourselves that these are a small subsample of stars and do not cover all the stars in the night sky. 
:::


## Limitations of the Nearby Stars

With over 300,000 stars, the GCNS provides the most complete picture of stars within 326 light years (100 {term}`parsecs <parsec>`) of the Sun, with a few important caveats. This is a *limited* sample of stars, but is a complete catalog within these following limitations.


### Cool stars limitation

The coolest stars grow too faint to see within 100 parsecs (326 light years), so the first limitation is the distance cutoff so that we can have a complete sample that includes a representation of cooler, dimmer stars. This Gaia sample is volume complete for spectral type M8 objects and earlier, and down to the Gaia magnitude {math}`G` = 20.7 to about 95% probability. Stars cooler than M8 are not fully represented in this data set and their completeness volumes will be increasingly smaller than 100 parsecs as we consider dimmer and dimmer stars.


### Bright stars limitation

Many of the bright stars we see in our night sky are too bright for Gaia's normal observation mode. These stars must be handled differently by the telescope. Many of the stars you are familiar with in the sky are absent from Gaia, for now. Gaia's Data Release 4 will include some of these bright stars, and the remaining will be included in Data Release 5, expected around 2030.



:::{figure} night_sky_gcns_sky.png
:align: left
:alt: A comoparison view of the night sky with Stars on and then only Nearby Stars displayed

A night sky comparison. The **top panel** shows the normal night sky view looking toward Scorpius and Sagittarius. The **bottom panel** shows the same view with only the Nearby Stars turned on where, notably, the brightest stars are absent because they are not yet in Gaia.
:::




### Binary and multiple star systems

Confusion can rein when it comes to deriving quality data from two stars whose light mingles with each other. Accounting for binary systems takes further analysis, some of which is present in these data, but more refined data will arrive in subsequent data releases from Gaia.


## Moving the Nearby Stars

As discussed above, the Nearby Stars are complete within the aforementioned limits. This is highly unusual in astrophysics to have such a complete sample of data, particularly with distances. Given the Nearby Stars do not, alone, yield a rendition of the night sky, what can we glean from these data?

First, it will be helpful, and perhaps necessary, to brighten the stars to examine them fully. Many of the stars are dimmer than naked eye limit. This is accomplished using the {menuselection}`Magnitude Exponent` in the Scene Menu settings for `Nearby Stars`.

Gaia is revolutionary because it will supply not only brightness and distance to billions of stars, but also motions for a large subset. Astronomers call this stellar kinematics---the space velocity of the stars. Gaia observes their proper motions in the sky, which is their motion as projected in the night sky, but it also derives their radial velocities from the star's spectrum. Radial velocity is the component of the space velocity toward or away from the Sun. The proper motions along with the radial velocity yield the trajectory of the star through space. Gaia DR3 provides radial velocities for roughly 33 million stars, while Gaia DR4 will have over 300 million stars' radial velocities.

In order to see the Nearby Stars move in time, you need to adjust the simulation time in OpenSpace. To speed the rate of time up, use the [Time Panel](/using-openspace/toolbar/time/index) to adjust the Simulation Speed to, say, 10,000 years per second. The stars will begin to move in space.


:::{note}
See [Moving Stars](content--milky-way--stars--moving-stars) on the Stars index page to understand the accuracy of moving stars in time.
:::





:::::


:::::{tab-item} Profiles

## Profiles
::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} [](/profiles/default/index)
[![default profile](/profiles/default/profile_default_icon.png)](/profiles/default/index)
:::

::::

:::::


:::::{tab-item} Dossier

## Dossier
:::{dossier}
:census: 331,312 stars
:assetfile: data/assets/scene/digitaluniverse/nearby_stars.asset
:openspaceversion: 1
:preparedby: Jackie Faherty, Brian Abbott, Zack Reeves, & Cade Mohrhardt (AMNH)
:sourceversion: 1.03
:license: amnh
:reference: Gaia DR3=<https://doi.org/10.5270/esa-qa4lep3>
:::

:::::
::::::
