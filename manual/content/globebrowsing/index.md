# Globebrowsing
Information about Globebrowsing for users that only want to view the content.

- [Working With Layers](working-with-layers) Description of handling layers for renderable globes.


Globes are commonly used within OpenSpace to represent planets and other celestial bodies. They include several special features related to globes in space, such as showing eclipses or displaying maps or other information on planetary surfaces.

This section collects wiki pages related to Globes in OpenSpace, such as working with [Globebrowsing layers](./working-with-layers) or [adding geometry through GeoJson files](./geojson-layers).

This page goes through everything that should be known about the globe browsing feature in OpenSpace. This page is both for content creators and for developers but I will try to separate the text so that it is a bit easier to follow.

## Builders
- [Creating a Renderable Globe]({{ site.url }}/docs/builders/globebrowsing/creating-a-renderableglobe) This page describes what settings are possible when building a renderable globe using a Lua table for the renderable.
- [Readable Datasets]({{ site.url }}/docs/builders/globebrowsing/readable-datasets) A summation of the dataset types that can be read and used for globe layers.
- [Build Local DEM Patches to Load With OpenSpace]({{ site.url }}/docs/builders/globebrowsing/build-local-dem-patches) A tutorial describing how to preprocess local patches so that they can be read as layer datasets.

:::{toctree}
:maxdepth: 1
:caption: GlobeBrowsing

working-with-layers
geojson-layers
creation/index
wms/index
:::
