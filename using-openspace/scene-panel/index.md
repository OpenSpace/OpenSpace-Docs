---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Scene Panel: Manipulating Data

We covered the Scene Panel basics in [](/getting-started/orientation/index). Here, we are going to go deeper into the structure of the Scene Panel and its functionality.


<div style="margin-left: auto; margin-right: auto; width: 640px;">
<iframe width="640" height="360" src="https://www.youtube.com/embed/MGnsgElqo1w?si=xR-c_PxzUDa5NWAA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{dropdown} Visual Transcript

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Open the Scene Panel. The current focus will be at the top of the list. |
| 0:09 | Open the scene hierarchy by clicking on one of the options. |
| 0:15 | Search for data sets using the search bar. |
| 0:21 | Turn on the data set by clicking the checkbox next to its name. |
| 0:25 | Change the properties of a data set by clicking on its name to open its submenu. Under Renderable, change the color and size, and enable labels. |
:::
</div>


:::{figure} scene_panel.png
:align: right
:width: 90%
:figwidth: 40%
:alt: OpenSpace's Scene Panel

The Scene Panel in OpenSpace, looking at the data sets under Star Clusters.
:::

The Scene Panel is a hierarchial listing of all the data sets in your OpenSpace session, which are determined by what assets are in the profile you loaded upon launching OpenSpace.

Expanding a data set will display its properties and their adjustment tools. These can be color choosers, sliders, or text boxes to type into that can change the size of a data set or its labels, the color and opacity of data, and the width and length of trails, to name a few. 



## Locating Data Sets
First and foremost, the Scene Panel is used to access all the data sets loaded into OpenSpace. What shows up in the Scene Panel is based on which assets are loaded into the profile used to launch OpenSpace.

The Scene Panel is organized by scales, with groups for the Solar System, Milky Way, and Universe (everything outside the Milky Way Galaxy). It is not limited to these three groups---there is a Night Sky group too---but much of the data you see in OpenSpace is in one of these three.

The entire [](/content/index) chapter's structure is based on the structure of the Scene Panel.

### Search Is Faster
Rather than fish through the tree to deeper and deeper levels looking for one particular data set, it's often easiest to simply search for it in the search box at the top of the panel.

The resulting matches will appear as a list, replacing the main list. Here, you can access their settings and make changes or turn the data set on or off.

To get the rest of the tree back, clear the search box.




:::{note}
We will refer to aspects of the Scene Panel with the path convention, for example: \
{menuselection}`Scene --> Milky Way --> Star Clusters --> Open Clusters`
 
In the context of a data set, we'll use the ellipses to abbreviate the path: \
{menuselection}`... --> Open Clusters --> Renderable --> Labels --> Size` \
or, for example, to change the size (brightness) of the Open Clusters: \
{menuselection}`... --> Renderable --> Sizing --> Scale Exponent`.
:::



## Turning Data On and Off
One of the primary uses of the Scene Panel is to turn data sets on and off. Using the check box beside each data set's name in the panel, you can toggle the data set on or off.

:::{note}
For some objects, you may have to turn off more than one data set to remove it from view. Most notably, planets with atmospheres, where the planet is one checkbox and the atmosphere is a different data set to uncheck.
:::

:::{warning}
Some data sets have a sizing or fading setting applied to them based on your distance from them, so they may not appear even if you turn them on. The galaxy surveys like [Tully Galaxies](/content/universe/nearby-surveys/tully-galaxies/index) or the [](/content/universe/deep-sky-surveys/sloan-galaxies/index) or the planet labels are examples of this. If you want to see Tully Galaxies from the night sky, you must uncheck: \
{menuselection}`Scene --> Universe --> Nearby Surveys --> Tully Galaxies --> Renderable --> Fading --> Enable Distance Based Fading`
:::



## Targeting a Data Set
To the right of the data set is the target icon ![Focus button](/getting-started/orientation/navigation_panel_focus_button.png). You can press this button to set that data set as the focus.

:::{note}
Many of these data sets are observationally based---so they are centered on the Sun. If you were to press ![Focus button](/getting-started/orientation/navigation_panel_focus_button.png) for the Open Star Clusters, the Sun would remain the Focus. This button is more critical when you want to visit a planet, moon, or a spacecraft.
:::


## Quick Access Menu

:::{figure} scene_panel_context_menu.png
:align: right
:width: 100%
:figwidth: 30%
:alt: OpenSpace's Scene Panel Context Menu
:::

Beside the target button is a context menu ![Context menu](/getting-started/orientation/navigation_panel_context_menu_button.png). This opens up a subpanel that has the navigation options to Fly To, Jump To, or Pan+Fly To. There is also a button to connect you to information about the data set.





## Asset Settings
The Scene Panel has a hierarchial structure, expanding deeper and deeper depending on how many nested items you have. Under each data set, there is a hierarchical list of settings. At its most basic, each data set will have three settings submenus:
- Renderable: where all of the settings for the renderable used by the data set can be changed---the look of the data set.
- Scale: where you can scale the data up or down spatially.
- Translation: where you can move the data set spatially in x, y, z.

:::{figure} scene_panel_open_clusters.png
:align: center
:width: 70%
:figwidth: 60%
:alt: The Scene Panel's settings for the Open Star Clusters.

The Scene Panel's settings for the Open Star Clusters. \
{menuselection}`Scene --> Milky Way --> Star Clusters --> Open Star Clusters`.
:::


:::{important}
**The Asset's Renderable Determines the Data Set's Settings**

In this section we are showing the Scene Panel and settings for the [Open Star Clusters](/content/milky-way/star-clusters/open-clusters/index). The Renderable for the Open Clusters is [RenderablePolygonCloud](/reference/asset-components/RenderablePolygonCloud), and that Rendedrable has a Sizing setting. The [Stars](/content/milky-way/stars/stars/index) data set, for example, uses [RenderableStars](/reference/asset-components/RenderableStars), which has no Sizing setting.

We chose Open Clusters because a lot of data sets use the RenderablePolygonCloud renderable, but you will need to see a specific data set's renderable to understand its settings.
:::


### Sizing
The most important setting under each data set is {menuselection}`... --> Renderable --> Sizing`. This determines the size of the points and, hence, their brightness. This is critical because as you change your distance from a data set, you will need to make it brighter for it to remain in view. Like the universe, light falls off with distance, so as you move away from a data set, it will become dimmer. This is an important cue for our brains to absorb the scales which we're traversing.

To remedy this, you can use the Sizing sliders. Bring the value up to increase the size, making it more visible form farther away.

:::{figure} scene_panel_sizing.png
:align: center
:width: 70%
:figwidth: 60%
:alt: The Open Star Clusters' Sizing settings.

The Open Star Clusters' Sizing settings consists of a slider for Scale Factor and one for Scale Exponent. {menuselection}`... --> Renderable --> Sizing`.
:::

Sizing a data set's points is a bit tricky. There are several variables that determine a point's final size. You see two here, Scale Exponent, and Scale Factor. There are also settings to determine a maximum size for the points that can clamp the size. And, your position also factors into the point size particularly when you are close to a point.

#### Scale Exponent
This is an exponential slider that ranges from 0 to 25. It sets the absolute size of the points in meters to this exponent. If you set this value to zero, the resulting size will be 1 ({math}`e^0 = 1`). It's wise to set this value first such that the data set looks decent close up, for example from the night sky view with the Open Clusters, but also so they don't totally disappear if you fly out to see the entire data set.

#### Scale Factor
This is a simple multiplying factor on top of the Scale Exponent. With the Open Clusters, you'll notice they are sized well for viewing in the night sky---the points don't dominate the entire sky. However, when you fly out of the Galaxy, they are barely visible. It's best here to use the Scale Factor to simply scale the point size up.

:::{note}
Because we traverse such vast scales in OpenSpace, it's challenging to get a size setting that works for nearby and far away.

It is inevitable that as you move through space, you will need to adjust your sizing to see the view you want. What may work for inside the [Tully Galaxies](/content/universe/nearby-surveys/tully-galaxies/index) will absolutely not work if you want to see these galaxies from the outside and highlight the large-scale structure.

In OpenSpace, size is crucial for the visual comprehension of these data sets.
:::


### Scale
The Scale Slider simply rescales the data set. A data set is generally made of {math}`(x, y, z)` positions, and changing this slider literally adds a scaling factor to each coordinate.

In the case of a planet or an object (like a spacecraft model), the Scale Slider will make the object larger. This can be extremely useful if you want to see a planet while in the outer reaches of the Solar System.


### Translation
This is a set of three sliders, one for each coordinate in x, y, z, that will move a data set from its current position.

The tricky thing with these sliders is that, natively, everything is in meters in OpenSpace. As you can imagine, once you reach even Neptune's distance, let alone far-off galaxies, the number of meters becomes unwieldy. These sliders are in meters, so it can be cumbersome to use them effectively.



### Coloring
Changing color in OpenSpace is fairly straightforward. Under the Coloring section is a color chooser, a three-parameter red-green-blue color input, and settings for outlines.

:::{figure} scene_panel_coloring.png
:align: center
:width: 70%
:figwidth: 60%
:alt: The Open Star Clusters' Coloring settings.

The Open Star Clusters' Coloring settings consists of a color chooser (recommended) as well as a red-green-blue inputs. {menuselection}`... --> Renderable --> Coloring`.
:::

The color chooser is the easiest method here to change a color interactively in OpenSpace.


### Labels
Label settings are controlled in the Labels dropdown. Here, you can set an opacity, color, size, and font size. But, most importantly, you turn them on and off with the checkbox.

:::{figure} scene_panel_labels.png
:align: center
:width: 70%
:figwidth: 60%
:alt: The Open Star Clusters' Labels settings.

The Open Star Clusters' Labels settings. {menuselection}`... --> Renderable --> Labels`.
:::

The Opacity merely controls how transparent the labels are drawn. This can affect their brightness and color. Opacity ranges from 0 to 1, where 0 is completely transparent (and, hence, invisible), and 1 is totally opaque. If you set the label color to white, then they will be pure white at an opacity of 1. If you have an opacity less than 1, they will be a bit more grayer.

The Size is the most important slider here, but it is also exponential, so it can be ultra sensitive.

:::{warning}
Some data sets, for example [](/content/milky-way/stars/star-labels/index), [](/content/universe/nearby-surveys/galaxy-group-labels/index), [](/content/universe/nearby-surveys/voids/index), or [](/content/universe/deep-sky-surveys/supercluster-labels/index), only have labels.

When you look at their settings in the Scene Panel, you will still see the Sizing setting. _This will not change the label size_. You still must change the label size under {menuselection}`... --> Renderable --> Labels --> Size`.
:::



## Can I Save my Changes?
Short answer: no. 

Longer answer, yes, but not in an automated way yet. If you find settings that you want to preserve, you must add them to that data set's asset file, then save that file. Each data set's asset file is listed in that data set's dossier in the [Content](/content/index) Chapter.

