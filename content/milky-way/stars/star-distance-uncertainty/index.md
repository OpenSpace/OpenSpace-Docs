---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Star Distance Uncertainty


{menuselection}`Milky Way --> Stars --> Star Distance Uncertainty`


In this asset, we provide a visual representation of the {term}`uncertainty` in a star's distance. Each line is along the line-of-sight back to Earth, and the length of each line represents how uncertain the distance value is for the particular star.



:::{figure} star_distance_uncertainty.png
:align: left
:alt: Among a starfield, from a perspective about 1,500 light years from earth, we see lines on select stars that represent their uncertainty range in distance. 

Lines that represent the range of distance uncertainty for a selection of stars. From this vantage point, 1,500 light years from Earth, these lines radially point back to the Earth, so it appears to form a vortex from this perspective. A few of the foreground stars are labeled with their star name and the length of distance uncertainty in light years. Aqua lines represent stars with Gaia geometric parallax distances, orange lines denote Gaia photogeometric parallax distances, and yellow lines represent uncertainties for Hipparcos distances.
:::



## Parallax uncertainty

Every object that we measure has some uncertainty associated with that measurement. For the stars, we measure something called *parallax*. Generally, parallax refers to the apparent motion of something relative to something else. If you hold your phone at arm's length to take a selfie, as you move your position to set up the perfect shot, your phone will appear to move relative to those objects in the background. Similarly, as Earth traverses around the Sun each year, nearby stars appear to shift relative to the more distant background stars. This apparent motion is imperceptible to the eye---we need highly specialized telescopes to measure the motion created by this parallax.

:::{figure} Parallax_02.png
:align: left
:alt: A two-panel diagram showing how parallax works. In panel A, we see the earth to the left of the sun in its orbit, a line is drawn to a foreground star, and extended to background stars, showing the star appears to be beside those background stars in January. A similar diagram in July, when the Sun is on the opposite side of the Sun, shows the foreground star appears to be beside different stars because of the parallax effect.

A diagram of how stellar parallax works. The Sun is shown along with Earth's orbit, and the Earth is shown at two different positions in its orbit, six months apart. A dotted line is drawn to a foreground star as seen from each epoch, January and June. The dashed line is extended out to the background stars. You can see in January the star appears to be beside the stars on the right from Earth's perspective, while six months later in July the star appears to be beside the stars on the left according to our view on Earth. Credit: Shay Krasinski/AMNH
:::



## Distance uncertainty

Once we have the parallax angle measured, it's a simple geometric formula to derive the distance to the star. And, of course, stars closer to the sun will have larger parallax angles. Because every measurement we make has some uncertainty associated with it, there will be an uncertainty associated with the parallax angle. This uncertainty could be due to the glare of the star, the nature of the sky during the observation, or the limitations of the instrument. Regardless, the uncertainty in the parallax angle results in an uncertainty in the star's distance, which we visualize in this data set.



## Drawing distance uncertainty

We represent the distance uncertainty as lines that are plotted around the star in question. So, while each star may be plotted at the center of their respective line, in reality we do not know exactly where the star is located within the uncertainty line it sits on.

We have three different colored lines that represent different data:

| Line Color | `dcalc` Value | Description |
| ---------- | ------------------ | ----------- |
| [Aqua]{.star_uncertainty_aqua}       | 2                  | Aqua lines are for geometric parallax measurements using the Gaia Catalog. These are the most accurate and so these uncertainty lines will be shorter. |
| Orange     | 1                  | These are also derived from Gaia data, but for stars with statistically small parallax angles, other stellar characteristics are used to inform a distance. |
| Yellow     | 3                  | Yellow uncertainty lines use the Hipparcos geometric parallax values, which are the least accurate. |


## Just a sample

We've chosen to illustrate the distance uncertainty on a small number of stars---only 3,440. These are the more well-known stars with more commonly used names. However, every star has an uncertainty on its distance. In fact, as you explore the universe, consider that there is uncertainty associated with every object---stars, nebulae, and galaxies---and often the uncertainty for nonstellar objects will be far greater. 




## Dossier
:::{list-table}
:header-rows: 0
:class: full-width

* - **Census:**
  - 3,440 stars
* - **Asset File:**
  - `data/assets/scene/digitaluniverse/star_uncertainty.asset`
* - **OpenSpace Version:**
  - 1
* - **Reference:**
  - [Gaia DR3](https://doi.org/10.5270/esa-qa4lep3); [XHIP An Extended Hipparcos Compilation](https://ui.adsabs.harvard.edu/link_gateway/2012AstL...38..331A/doi:10.48550/arXiv.1108.4971)
* - **Prepared by:**
  - Brian Abbott, Zack Reeves (AMNH)
* - **Source Version:**
  - 6.06
* - **License:**
  - [AMNH's Digital Universe](https://www.amnh.org/research/hayden-planetarium/digital-universe/download/digital-universe-license)
:::