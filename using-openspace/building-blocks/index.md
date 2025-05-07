---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# The Building Blocks of OpenSpace

OpenSpace, like any program, is made up of components that build upon themselves to deliver complex scenes to the user. These elements are apparent to the user, but perhaps not intimately understood. Here, we will broadly describe these elements so that in the following sections we can discuss how these elements are visible to you and how you can work with them.


## Profiles: Define an OpenSpace Session
When you launch OpenSpace, you choose a profile and then press Start. You can [create and edit profiles](/using-openspace/profile-editor/index) in the Profile Editor, as we'll see soon.

%%%% LINK ABOVE

When you create or edit a profile, you are adding components called _assets_. 


## Assets: Profile Building Blocks
An Asset is a file that defines a Scene in OpenSpace. Assets are at the root of every data set you interact with in OpenSpace, from stars, star clusters, Earth, Mars's atmosphere, and so on. In a basic sense, they define what data we see in a scene, they set the scene's parameters (think color, labels, size, etc.), and they deliver the commands to OpenSpace to load the data files and settings when the profile containing the asset is used to launch OpenSpace.

Not only do assets define data sets for scenes, but they also can define keyboard shortcuts, actions, and more esoteric building blocks.

Many of the following sections will refer to the existence of asset files. While you don't need to understand how to read or create one, it's good to understand what one is before we go deeper into OpenSpace. We will discuss all the gritty details of asset building in [](/creating-data-assets/index).


::::{dropdown} Asset File Syntax
Assets are text-based files coded using [Lua](https://www.lua.org/about.html), a high-level scripting language. As code goes, it is very readable within this context---one may not know all the Lua syntax, but, upon reading, it's fairly clear what's going on in a given asset file.

In general, asset files are located in your OpenSpace folder under `data/assets` with a file extension of `.asset`. In addition, on each data set's page under [](/content/index) you'll find the path to that data set's asset file.

This is a portion of the asset file for [Open Star Clusters](/content/milky-way/star-clusters/open-clusters/index), just to give you a sense of what it looks like.

```lua
local Object = {
  Identifier = "OpenStarClusters",
  Renderable = {
    Type = "RenderablePolygonCloud",
    Enabled = false,
    Labels = {
      File = speck .. "oc.label",
      Color = { 0.0, 0.36, 0.14 },
      Size = 15.5,
      MinMaxSize = { 4, 30 },
      Unit = "pc"
    },
    Coloring = {
      FixedColor = { 0.13, 0.99, 0.50 }
    },
    Opacity = 0.9,
    File = speck .. "oc.speck",
    Unit = "pc",
    PolygonSides = 12,
    SizeSettings = {
      ScaleExponent = 17.8,
      MaxSize = 23.0,
      EnableMaxSizeControl = true
    }
  },
  GUI = {
    Name = "Open Star Clusters",
    Path = "/Milky Way/Star Clusters",
    Description = [[An open star cluster is a loose assemblage of stars numbering from
      hundreds to thousands that are bound by their mutual gravitation. Because these are
      young stars, we expect to see them in the star-forming regions of our Galaxy, namely
      in the spiral arms. For this reason, open clusters exist, for the most part, in the
      plane of the Galaxy and indicate relatively recent star formation. Census: 1,867 star
      clusters.]]
  }
}
```
::::


## Renderables: Defining the Visual
If you look up the word renderable, you will find the smarty-pants definition of "capable of being rendered." But, if you look deeper, past the "to melt something down" and "to give something in return or retribution," you will eventually come to the definition "to cause something, such as an image or text, to display (as on a screen)."

Here, we apply the latter in OpenSpace by setting [Renderables](/reference/renderable-overview) to assets. These Renderables know how to draw objects---a point in 3-D space, a line between two points, a planet's atmosphere, or a model of a space station or satellite, among many others.

Assets call on Renderables to do the heavy lifting by taking its settings---color, label size, size (or brightness)---and applying them to a renderable. Every data set you see has a renderable enabling it to appear in OpenSpace.