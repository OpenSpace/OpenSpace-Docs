---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Profile Editor

:::{warning}
This section is in progress. Some sections remain incomplete.
:::


A profile is an assemblage of data assets and settings that, grouped together, allow you to tell a story. A crucial aspect of the Profile Editor is selecting which data sets are included and, therefore, loaded into OpenSpace. 

OpenSpace provides access to the profile editor via the Launcher Window:

:::{figure} /getting-started/launch/launcher.png
:align: center
:width: 70%
:figwidth: 80%
:alt: OpenSpace launcher window

The OpenSpace launcher window, with the profile chooser at top, and the New and Edit buttons.
:::


## Create a Profile

The easiest way to create a new profile is to find a profile that has many of the items you want and duplicate it. Select the profile that's closest to what you want, and bring up the profile editor by pressing the {menuselection}`Edit` Button in the Launcher Window. You will see the Profile Editor Window:

:::{figure} profile_editor.png
:align: center
:width: 100%
:figwidth: 80%
:alt: OpenSpace Profile Editor

The OpenSpace Profile Editor.
:::


Press the {menuselection}`Duplicate Profile` Button in the upper-right corner. This will create a copy of the profile and append to the name an `_1`. So, if you chose the Default Profile as the basis for your new profile, pressing the Duplicate Profile Button will give you a new profile called `default_1`.

This new, unsaved profile will adopt all the settings of the default profile, including the assets to load, the default camera settings, the included keybindings, etc.

Once you have a new profile, you can change its meta-information: the name, description, author, version, and so on. Use the {menuselection}`Edit` Button under `Meta` in the top-right of the Profile Editor.

:::{figure} profile_editor_meta.png
:align: center
:width: 100%
:figwidth: 70%
:alt: OpenSpace Profile Editor metadata editor

The OpenSpace Profile Editor's Meta Editor.
:::

## Adding or Removing Data Sets

The most-used portion of the Profile Editor is the Assets section in the middle of the window. Click the {menuselection}`Edit` Button to the right of the Assets subwindow title, and the Assets Editor will appear. (Note, there are many {menuselection}`Edit` buttons in this window, to edit the assets included choose the one on the same line as the Assets title.)


:::{figure} profile_editor_assets.png
:align: center
:width: 100%
:figwidth: 80%
:alt: OpenSpace Profile Editor's Asset Section

The OpenSpace Profile Editor's Assets section, where you can add or remove assets in the profile.
:::

The Assets Editor is a long list of available assets available to you. It is in a hierarchical list similar to what you'd see in the OpenSpace Scene Panel. Check an item on to include it in the profile, and uncheck the item to remove it from the profile. Neither of these operations affects the asset itself, which remains unchanged in its folder.

There is also a search bar to directly find the assets you want to include.

:::{caution}
Because of redundancies, the state of the assets in the Assets Editor list---checked or unchecked---does not always reflect reality. For example, by including the `base` asset, you automatically include a whole bundle of other assets. These same assets will appear in the list here, but their box will remain unchecked despite the fact that they are now included in the profile. This is a known issue.
:::


:::{note}
Assets may also be added to a session temporarily (as opposed to saving it in a profile to load automatically). The easiest way to do this is to drag the asset file into the OpenSpace Graphics Window. A more advanced way is to use the console to enter OpenSpace commands, a topic we will take up soon.
:::




## Mark Interesting Nodes

:::::{grid} 1 1 1 2
::::{grid-item}
The Mark Interesting Nodes section allows you to determine what appears in the Navigation Panel. Each asset that appears there is available for targeting, aiming toward, or flying to. See the [Navigation Panel](/using-openspace/navigation-panel/index) for more.

For this panel, you need to know the name of the asset, or node, you want to add.
::::

::::{grid-item}
:::{image} profile_editor_nodes.png
:align: right
:width: 90%
:alt: OpenSpace Profile Editor's add nodes
:::
::::
:::::



## Simulation Time Increments

Simulation Time Increments allows you to edit the time increments that function within the [Time Panel](/using-openspace/time-panel/index). These increments are triggered by button on that panel, or more easily by keystrokes outlined in the Time Panel page.

:::{figure} profile_editor_time_increments.png
:align: center
:width: 80%
:figwidth: 100%
:alt: OpenSpace Profile Editor's Simulation Time Increments section.
:::


## Camera Settings

You can set the default camera position for your new profile using the {menuselection}`Edit` Button under `Camera` in the Profile Editor.

Here, you have three ways to set the initial campera position: Geo State, Navigation State, and Scene Graph Node.

### Geo State

Use the Geo State tab to set a camera position. This is useful when a planet or moon is set as the target---which is often the case. 

:::{figure} profile_editor_camera_geo.png
:align: center
:width: 80%
:figwidth: 100%
:alt: Geo State tab in the Profile Editor's camera settings

The Geo State tab in the Profile Editor's camera settings. 
:::

Enter the anchor node (the object of focus), then the latitude, longitude, and altitude in meters. You can find values for these numbers interactively by flying to the desired position in OpenSpace, then reading the values for these in the informational Dashboard in the upper left of the Graphics Window. (If the Dashboard is not visible,  try {kbd}`Shift`+{kbd}`Tab` to toggle it on, or go to {menuselection}`Settings --> Dashboard`.)




### Navigation State



:::{figure} profile_editor_camera_navigation.png
:align: center
:width: 80%
:figwidth: 100%
:alt: Navigation State tab in the Profile Editor's camera settings

The Navigation State tab in the Profile Editor's camera settings.
:::


### Scene Graph Node

With this option, you can enter a scene graph node, or a known data object in OpenSpace---something you can click on and off in the Scene Panel---and use that data for determining an initial camera setting. 

:::{figure} profile_editor_camera_node.png
:align: center
:width: 80%
:figwidth: 100%
:alt: Scene Graph Node tab in the Profile Editor's camera settings

The Scene Graph Node tab in the Profile Editor's camera settings.
:::

Choose a static data set, like the [Stars](/content/milky-way/stars/index), and your initial position will begin outside the Milky Way Galaxy such that the entire stars data set will be centered and framed according to the extent of the data. In fact, from a vantage point from where the entire data set is represented in the Graphics Window, the star data is actually too dim to be seen, so you'd have to brighten them up.

Trpically, though, you set a planet as the opening view upon launch. So, if you put `Earth` into the Anchor Node field, it will center and frame up Earth. It will also attempt to show the sun-lit side of the planet. Therefore, each time you launch OpenSpace with that profile, the view could be slightly different depending on which side of the planet is facing the Sun.



## Initial Time Settings



:::::{grid} 1 1 1 2
::::{grid-item}
Pressing the {menuselection}`Edit` button in the Time section of the Profile Editor brings up a small window with a few time settings for the profile where you set the initial time for the profile.

You can choose `Relative` or `Absolute` from the dropdown menu. `Relative` is relative to the current time; `Absolute` will bring up a field for you to type in a custom date and time.

The Relative Time section allows you to provide an offset to the selected time above. This is typically set to `-1d`, or "minus one day." We use a one-day offset prior to the set time because the clouds on Earth are from satellite data that will be missing or incomplete if we choose the current day.
::::

::::{grid-item}
:::{figure} profile_editor_time.png
:width: 80%
:alt: OpenSpace Profile Editor's Actions and Keybindings section
:::

::::
:::::




{.advanced-topic}
[Advanced]{.advanced}
## Properties

:::{figure} profile_editor_properties.png
:align: center
:width: 100%
:figwidth: 100%
:alt: OpenSpace Profile Editor's Properties settings

The OpenSpace Profile Editor's Properties section, where you can add or remove actions and keyboard shortcuts in the profile.
:::


{.advanced-topic}
[Advanced]{.advanced}
## Actions & Keybindings

At the bottom left, you'll see the Actions & Keybindings section. Press its {menuselection}`Edit` Button and you will see this window: 

:::{figure} profile_editor_keybindings.png
:align: center
:width: 100%
:figwidth: 100%
:alt: OpenSpace Profile Editor's Actions and Keybindings section

The OpenSpace Profile Editor's Actions and Keybindings section, where you can add or remove actions and keyboard shortcuts in the profile.
:::

Here, you can add actions to perform adjustments to your scene, and assign keyboard shortcuts to those actions.

This section uses scripting expressions and functions that instruct OpenSpace what to do. This is a bit advanced for this section, so we will describe this more fully in the future.








{.advanced-topic}
[Advanced]{.advanced}
## Modules

:::::{grid} 1 1 1 2
::::{grid-item}

::::

::::{grid-item}
:::{figure} profile_editor_modules.png
:width: 80%
:alt: OpenSpace Profile Editor's Modules section
:::

::::
:::::


{.advanced-topic}
[Advanced]{.advanced}
## Additional Scripts

