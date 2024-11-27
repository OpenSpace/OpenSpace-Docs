---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# What is an Asset? 

Assets are the files that define much of the data you interact with in OpenSpace. In a basic sense, they define what data we see in the scene, they set the scene's parameters (think color, labels, size, etc.), and they deliver the commands to OpenSpace to load the data files and settings when the profile containing the asset is used to launch OpenSpace.

Not only do assets define data sets for scenes, but they also can define keyboard shortcuts, actions, and more esoteric building blocks.

Assets are text-based files coded using [Lua](https://www.lua.org/about.html), a high-level scripting language. As code goes, it is very readable within this context---one may not know all the Lua syntax, but, upon reading, it's fairly clear what's going on in a given asset file.

In general, asset files are located in your OpenSpace folder under `data/assets` with a file extension of `.asset`. In addition, on each data set's page under [](/content/index) you'll find the path to that data set's asset file.

Many of the following sections will refer to the existence of asset files. While you don't need to understand how to read or create one, it's good to understand what one is before we go deeper into OpenSpace.

We will discuss all the gritty details of asset building in [](/creating-data-assets/index).


::::{dropdown} Sample Snippet from `openclusters.asset`
This is a portion of the asset file for [Open Clusters](/content/milky-way/star-clusters/open-clusters/index), just to give you a sense of what it looks like.

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