---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Scene Panel: Manipulating Data

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::

We covered the Scene Panel basics in [](/getting-started/orientation/index). Here, we are going to go deeper into the structure of the Scene Panel and its functionality.


:::{note}
We will refer to aspects of the Scene Panel with the path convention, for example: \
{menuselection}`Scene --> Solar System --> Planets --> Earth`
 
In the context of a data set, we'll use the ellipses to abbreviate the path: \
{menuselection}`... --> Earth --> Moon --> Moon Label` \
or, for example, to change the scale of the Moon Label: \
{menuselection}`... --> Moon --> Moon Label --> Scale`.
:::


## Locating Data Sets
First and foremost, the Scene Panel is used to access all the data sets loaded into OpenSpace. What shows up in the Scene Panel is based on which assets are loaded into the profile used to launch OpenSpace.

The Scene Panel is organized by scales, with groups for the Solar System, Milky Way, and Universe---everything outside the Milky Way Galaxy. It is not limited to these three groups---there is a Night Sky group too---but much of the data you see in OpenSpace is in one of these three.

The entire [](/content/index) chapter's structure is based on the structure of the Scene Panel.

### Search Is Faster
Rather than fish through the tree to deeper and deeper levels looking for one particular data set, it's often easiest to simply search for it in the search box at the top of the panel.

The resulting matches will appear as a list, replacing the main list. Here, you can access their settings and make changes or turn the data set on or off.

To get the rest of the tree back, clear the search box.

## Turning Data On and Off


## Hierarchial Structure
Renderable, Scale, Translation
even labels have these

and labels have Sizing, which does notihing... need to use Labels then Size under that.

## 


## Using the Menus - Datasets
This section will cover using the menus to turn on and off or manipulate datasets.


### Finding Datasets
  - All datasets in OpenSpace can be found in the Scene menu.
  - You can search for datasets by typing into the search bar, or browse for them in the menus.
  - Some things you find will not be datasets, and instead are just a focus node. All items that are datasets will show a checkbox next to their name.
  - Some items with checkboxes may not be traditionally considered a dataset, such as a 3D model, or a planet.

### Enabling and Disabling Datasets
  - Use the checkbox next to the dataset's name in the menu to turn it on or off in OpenSpace.
  - Sometimes you will have to enable or disable multiple items for the effect you want. For example, if you don't want to see Mars, you must also turn off its atmosphere, which is a separate checkbox.
  - Some datasets have sizing or fading applied to them based on distances, so they may not appear even if they are enabled. The 'Tully Galaxies' or 'Earth Label' are examples of this.


### Manipulating Datasets
  - For most datasets, you can change aspects of how they are visualized in OpenSpace. Examples include changing the color, opacity of items, the size of text, and the width or length of trails.
  - Changes can be made by clicking the item's title to open its submenu.
  - You can also click the wrench icon to pop out a panel for the item's properties.
  - Changes made are not saved between OpenSpace sessions. To learn how to save your changes, stay tuned for the [Customizing OpenSpace - Profiles](/using-openspace/create-profile/index) tutorial.


### Video
<iframe width="740" height="530" src="https://www.youtube.com/embed/MGnsgElqo1w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Open the scene menu. The current focus will be at the top of the list. |
| 0:09 | Open the scene hierarchy by clicking on one of the options. |
| 0:15 | Search for datasets using the search bar. |
| 0:21 | Turn on the dataset by clicking the checkbox next to its name. |
| 0:25 | Change the properties of a dataset by clicking on its name to open its submenu. Under Renderable, change the color and size, and enable labels. |
