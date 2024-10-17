---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Tully Galaxies

{menuselection}`Scene --> Universe --> Nearby Surveys --> Tully Galaxies`



The Tully Catalog is the most polished, accurate catalog of nearby galaxies. It includes over 30,000 galaxies in the local universe that surround the Milky Way. This catalog demonstrates the large-scale structure of the universe exceptionally well. And, each galaxy has a representative image reflecting its morphological type, and is properly sized and inclined. These data have also been "massaged" a bit, correcting and smoothing some of the observational artifacts and data contamination to produce a more realistic view of the structure.


:::{figure} tully_outside.png
:align: left
:alt: The Tully Nearby Galaxy Catalog represented as points of orange, green, and aqua points. 

The Tully Nearby Galaxy Catalog from outside the data. It's difficult to capture the nature of this atlas in a static image, but we see here the large-scale structure of the local universe, with large galaxy clusters in orange and yellow and more remote galaxies in aqua.
:::



## Portraying Galaxies 

From this perspective and at this scale, the galaxies are so small that you have to be beside one to see its representative image. In order to see the galaxies, we must assign points to them that will be seen from great distances. We color-code these points by relative density, so galaxies in a relatively dense area are orange and yellow, galaxies in less dense areas are in green then aqua.

On each point we place an image that is representative of its morphological type---spiral, elliptical, or irregular. Most of these come from [The Galaxy Catalog](http://zsolt-frei.net/catalog.htm). A handful of galaxies are represented by their actual images, which primarily come from the [National Optical Astronomy Observatory](https://en.wikipedia.org/wiki/National_Optical_Astronomy_Observatory) (NOAO).

Each of these images has been altered from its original state. These images were taken from Earth on some of the world's largest telescopes, so foreground stars from our own Galaxy appear in each image. We are representing galaxies in extragalactic space, so we have removed the stars from each image. See more in [Tully Galaxies Images](../tully-galaxies-images/index).


## Large-scale Structure

The strength of these data are not visiting individual galaxies, but seeing the overall structure of the galaxies. This so called large-scale structure divides into galaxy clusters, sheets, walls, filaments, and voids. Clusters are prominent groups of hundreds or thousands of galaxies. The nearest cluster to us is the Virgo Cluster. Walls, sheets, and filaments describe the amalgam of galaxy clusters and superclusters into massive, tubelike structures. A local example is the Ursa Major Filament that stretches up from the Virgo Cluster, or the [Great Wall](https://en.wikipedia.org/wiki/CfA2_Great_Wall). 

Large-scale structure is reflective of the primordial universe and tells us about the fluctuations in the early universe, how galaxies form, the distribution of dark matter, and the rate of expansion of the universe. However, it is fleeting---because the universe is expanding and accelerating in its expansion, these superstructures will fly apart over time as they recede from us.


:::{figure} tully_virgo_cluster_nightsky.png
:align: left
:alt: A view of the night sky with the Tully galaxies turned on, seen as multicolored points among the stars and constellation lines of the night sky.

The Virgo Cluster, the group of orange points at center, as seen from Earth. Here, we view the stars in the night sky along with the far-off galaxies. It's clear that the Virgo Cluster is so named because it appears in the constellation Virgo from our vantage point.
:::


:::{figure} tully_virgo_cluster_within.png
:align: left
:alt: Multicolored points represent galaxies. The nearest have labels and are located inside the Virgo Cluster. We look from this vantage point back toward the Milky Way, which is roughly 55 million light years away from the Virgo Cluster.

A 55-million-light-year view back toward the Milky Way (Home) from inside the Virgo Cluster. Some of the foreground galaxies in the Virgo Cluster are labeled, the largest of which is Messier 87 (M87). The inner grid, located near Home, is a 1-million-light-year grid. The next grid out is 10 million light years, and the large grid that stretches out of the frame is a 100-million-light-year frame.   
:::



:::{figure} tully_virgo_cluster_nearby.png
:align: left
:alt: A view of the galaxies from outside the Virgo Cluster, with the milky Way in the distance.

A view from outside the Virgo Cluster (top), with the Milky Way (Home) in the distance.
:::



## Size and Shape of These Data

The Tully data forms a cube, which is a cutoff based on the {term}`completeness` of these data. Beyond this, data from these sources are not as reliable, so effort is made to show a complete picture, albeit limited by observations (for example, we cannot see dwarf galaxies much beyond the Local Group).

The size of the cube is roughly 700 million light years on a side, or about 1 billion light years on the diagonal.


:::{figure} tully_cube.png
:align: left
:alt: A cube of points, each representing a galaxy, form a cube-shaped distribution because of the completeness cut-off.

The cubic nature of the Tully Nearby Galaxies Catalog. This is an arbitrary cutoff that was made to maintain completeness in the data set, so these data are consistent no matter where we look.
:::




## Galaxy Morphological Types

The galaxy morphological type metadata is an integer that reflects the type of galaxy classified first by Edwin Hubble (1889--1953) in the 1930s. The classification scheme has four main groups: elliptical galaxies (E), barred spiral galaxies (SB), unbarred spiral galaxies (S), and irregular galaxies (Irr). 

The integers assigned to these types are decoded in the table below. In this numbering system, barred and unbarred spiral galaxies (S & SB) are merged, since data on bars are often inconclusive.


:::{table} Morphological type codes and census
:widths: auto
:align: center

| Hubble Stage | de Vaucouleurs Class | Galaxy Type | Census |
| ------------ | -------------------- | ----------- | ------ |
| -5 | E | Elliptical | 990 |
| -3 | E/SO | Elliptical/Lenticular (class uncertain) | 652 |
| -2 | SO | Lenticular | 1,439 |
| 0 | SO/a | Lenticular/Spiral | 9,132 |
| 1 | Sa | Spiral | 1,314 |
| 2 | Sab | Spiral | 1,629 |
| 3 | Sb | Spiral | 2,046 |
| 4 | Sbc | Spiral | 2,332 |
| 5 | Sc | Spiral | 3,323 |
| 6 | Scd | Spiral | 2,284 |
| 7 | Sd | Spiral | 581 |
| 8 | Sdm |Spiral  | 498 |
| 9 | Sm | Spiral/Irregular | 311 |
| 10 | Irr | Irregular | 481 |
| 12 | S | Spiral/Irregular (class uncertain) | 0 |
| 13 | P | Peculiar | 0 |
:::


## Dossier
:::{list-table}
:header-rows: 0
:class: full-width

* - **Census:**
  - 30,159 galaxies
* - **Asset File:**
  - `data/assets/scene/digitaluniverse/tully.asset`
* - **OpenSpace Version:**
  - 4
* - **Reference:**
  - Nearby Galaxy Catalog (private communication, Brent Tully)
* - **Prepared by:**
  - R. Brent Tully, Stuart Levy, Brian Abbott (AMNH)
* - **Source Version:**
  - 1.05
* - **License:**
  - [AMNH's Digital Universe](https://www.amnh.org/research/hayden-planetarium/digital-universe/download/digital-universe-license)
:::