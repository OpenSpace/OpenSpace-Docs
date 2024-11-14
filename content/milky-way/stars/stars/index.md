---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Stars

{menuselection}`Scene --> Milky Way --> Stars --> Stars`


In many ways, stars form the foundation of our astronomical knowledge and are incremental toward our understanding of the universe itself. We base much of what we know about the universe on the characteristics and evolution of stars, and they are an important rung on the so-called distance ladder that other distance-determination methods rely upon.


:::{figure} stars_scorpius+constellations.png
:align: left
:alt: A starry sky looking toward the constellation Scorpius and Sagittarius. Lines connect the stars of the constellations in view, and the band of light crossing the image is the Milky Way.

A view of the night sky toward Scorpius and Sagittarius, shown with the constellations lines connecting the main stars within each constellation. The band of light, called the Milky Way, is prominent in this part of the sky.
:::

## What Is a Star?

Stars are, in a literal sense, light factories. Their light is a product of the nuclear processes that naturally occur in stars and define the lifespan of a star. Stars are born, live a stable life, then transform into a [stellar remnant](../../stellar-remnants/index). They condense from clouds of hydrogen, exist in equilibrium throughout their life as a *{term}`main sequence`* star, and evolve into a post stellar object like a [white dwarf](../../stellar-remnants/white-dwarfs/index), [neutron star](../../stellar-remnants/pulsars/index), or a black hole.

How massive the star is at birth determines its characteristics and longevity. Stars spend most of their time in a stable state, called the main sequence because of its placement on the [Hertzsprung–Russell diagram](https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram). During this phase, gravity is balanced by the radiation pressure within the star---the star is in equilibrium. The Sun is on the main sequence, and will remain there for a few billion years. In general, the initial mass of the object results in different types of stars---some are cooler, redder, and live a long time, while others are hotter, bluer, and cycle off the main sequence more quickly toward their ultimate fate.


## History

We've communed with the night sky since humans evolved. Stories passed down from antiquity remain in our lore of the night sky today, and the ancients catalogued the sky's objects. [Hipparchus](https://en.wikipedia.org/wiki/Hipparchus) (c. 190--c.120 BCE), the Greek astronomer, created the first catalog of the stars. However, our understanding of the distance to the stars is a relatively recent phenomenon. The first relatively accurate measurement of a star's distance was in 1838 by German astronomer-mathematician [Friedrich Bessel](https://en.wikipedia.org/wiki/Friedrich_Wilhelm_Bessel) (1784--1846), who measured the parallax to the star [61 Cygni](https://en.wikipedia.org/wiki/61_Cygni). 

Before 1997, we had good distances for about 3,800 stars via the [Gliese](https://en.wikipedia.org/wiki/Gliese_Catalogue_of_Nearby_Stars) catalog; however, in 1997 the results from ESA's [Hipparcos](https://en.wikipedia.org/wiki/Hipparcos) mission gave us far more accurate distances to roughly 120,000 stars, revolutionizing our understanding of the Milky Way. This was surpassed by the [Gaia](https://en.wikipedia.org/wiki/Gaia_(spacecraft)) mission, which provides highly accurate data for about two billion stars around the Sun. For reference, we can see roughly 9,000 stars in the night sky with our eye, and around 6,500 stars on any given night.


## Source Catalogs

For this {menuselection}`Stars` data set, we base our data on the Hipparcos catalog. Hipparcos provides the colors we see with our eye, and the brightnesses we're accustomed to seeing. However, when we have Gaia data for the distance or velocity of the star, we use that information, which will be far more accurate than Hipparcos. We continue to rely on Hipparcos for most of the bright stars in the night sky because these are not yet in the Gaia catalog.

:::{figure} stars_orion+taurus.png
:align: left
:alt: A starry sky looking toward the constellation Orion and Taurus.

A view of the night sky toward Orion and Taurus. Orion, the hunter, is conspicuous in the northern and southern sky, with its distinctive three-star belt. The Hyades and Pleiades, two [open star clusters](../../star-clusters/open-clusters/index) in Taurus, are easily seen in the night sky.
:::



## Brightnening in OpenSpace

The most common operation on the stars is to brighten them. By default, the stars are loaded at their accurate brightness, according to how we see them in the night sky. However, if you fly away from the Sun, they will quickly disappear. You may want to brighten the stars using the slider: \
{menuselection}`Scene --> Milky Way --> Stars --> Stars --> Renderable --> Magnitude Exponent`

This will allow you to see the stars as you fly away from them, yielding the view in the figure below. This is, of course, wildly exaggerated.


:::{figure} stars_from_afar.png
:align: left
:alt: A view of the spiral structure of the Milky Way Galaxy with the local stars near the sun in the foreground, brightened up to see them as a "ball" of stars located in our region of the galaxy.

Exaggerating the brightness of the stars allows you to see even the dimmest among them from outside the Milky Way Galaxy, and acts as a crude marker for where we are located.
:::




:::{dossier}
:census: 112,746 stars
:assetfile: data/assets/scene/digitaluniverse/stars.asset
:openspaceversion: 6
:preparedby: Brian Abbott, Zack Reeves, Andrew Ayala, Jackie Faherty (AMNH)
:sourceversion: 8.10
:license: amnh
:reference: Gaia DR3=https://doi.org/10.5270/esa-qa4lep3;XHIP An Extended Hipparcos Compilation=https://doi.org/10.48550/arXiv.1108.4971
:::