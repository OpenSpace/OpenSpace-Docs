---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# User Interface Overview

OpenSpace's user interface is unconventional, but straightforward and easy to learn. Here, we will touch on the elements of the interface and discuss the details of each item later.

:::{figure} user_interface_orientation.png
:align: center
:width: 100%
:alt: OpenSpace user interface annotated

The main parts of the OpenSpace user interface.
:::



:::{tip}
You can toggle the text on and off in the Graphics Window using the {kbd}`Shift` + {kbd}`Tab` keys.

You can toggle the menus on and off using the {kbd}`Tab` key.
:::




## Menus


:::{figure} menus_orientation.png
:align: center
:width: 50%
:alt: OpenSpace annotated menus.

OpenSpace's menus annotated.
:::



### System Menu

:::{image} system_menu_icon.svg
:align: left
:width: 4%
:alt: System menu icon
:::

The System Menu exists in the bottom-left corner of the Graphics Window. It offers some high-level operations in OpenSpace, such as an about panel, links to resources and feedback, and quitting the program. Click this symbol to see the menu.


:::{figure} system_menu.png
:align: right
:width: 100%
:alt: The OpenSpace System Menu

The OpenSpace {menuselection}`System` Menu.
:::


:::{list-table}
:header-rows: 0
:stub-columns: 1

* - About OpenSpace
  - Version information and a short description.
* - Open Web Tutorials
  - Opens this documentation website in your browser.
* - Open Getting Started Tour
  - Launches a wizard panel that will guide you the the basics of OpenSpace.
* - Send Feedback
  - Opens a web form to send feedback.
* - Show keybindings
  - Displays an onscreen, interactive keyboard with the keyboard shortcuts for the loaded profile.
* - Open GUI in Browser
  - Opens the user interface in a separate browser window.
* - Toggle console
  - Displays (or hides) a single-line [console](/using-openspace/scripting/console/index) at the top of the Graphics Window which enables you to enter OpenSpace commands. Use {kbd}`~` to toggle on and off.
* - Toggle native GUI
  - Displays (or hides) an older user interface rendered as an overlay over the main window. Use {kbd}`F1` to toggle on and off.
* - Quit OpenSpace
  - Gives you a 3-second grace period, then quits OpenSpace. The grace period allows you to abort an errant quit during a show if you accidentally quit OpenSpace. Use the shortcut {kbd}`Esc` key to quit, and hit {kbd}`Esc` again to cancel the quit within the grace period.
:::









### Scene Menu

:::::{grid} 1 1 1 2
::::{grid-item}

:::{image} scene_menu_icon.png
:align: left
:width: 25%
:alt: Scene menu icon
:::

The Scene Menu collects all the assets (data sets) that were loaded via the profile chosen upon launch. It is, by far, the most used menu in OpenSpace.

#### List of Data Assets

For the [Default](/profiles/default/index) Profile, all the general data sets for the universe are loaded. This includes the planets, moons, and other objects and satellites in the Solar System, the zoo of objects in the Milky Way, and the large surveys outside the Galaxy, in Universe.

The menu is a essentially a vertical, sidebar menu with expanding items to reveal the data sets inside each hierarchical group. For example, under the Solar System are the groups Sun, Planets, Dwarf Planets, Comets, etc. Each of these reveals a submenu, and so on.


#### Data Adjustments

Under each data set you will find adjustments. You can brighten objects, change their color, change a label size, and so on.
::::

::::{grid-item}

:::{figure} scene_menu.png
:align: center
:width: 70%
:alt: OpenSpace Scene Menu

OpenSpace {menuselection}`Scene` Menu
:::

::::
:::::



### Settings Menu

:::::{grid} 1 1 1 2
::::{grid-item}

:::{image} settings_menu_icon.png
:align: left
:width: 25%
:alt: Settings menu icon
:::

The Settings Menu is rarely used, but has a number of useful items that change some behaviors or alter what's displayed, or how it's displayed.

We do not have time here to discuss each item---some are too advanced for this section---but here are some of the more relevant ones for the average user.

The **Dashboard** sets what information is visible in the on-screen Dashboard. We discuss the particulars of the Dashboard [later on this page](#dashboard).

The **OpenSpace Engine** has a setting called Property Visibility. It sets the level of detailed information about an asset in the Scene Menu based on the user level you choose. Choices include Novice User, User, Advanced User, Developer, Everything. 

:::{figure} settings_openspace_engine.png
:align: center
:width: 70%
:alt: The OpenSpace Engine Property Visibility setting

{menuselection}`Settings --> OpenSpace Engine --> Property Visibility`
:::

You might be tempted to choose Everything, but it quickly clutters up the Scene Menu and makes its use more cumbersome. The more advanced categories are really useful when adding your own data or working in the source code and you want additional information reported to you about the asset. 

::::

::::{grid-item}

:::{figure} settings_menu.png
:align: center
:width: 70%
:alt: OpenSpace Setting Menu

OpenSpace {menuselection}`Settings` Menu
:::

::::
:::::




## Panels

A panel collects specific functionality to alter time, record your session, access actions, and so on. Each will bring up a window that is attached to its corresponding icon, but may also be detached as a floating window.

:::{figure} panels_orientation.png
:align: center
:width: 90%
:alt: OpenSpace panels annotated.

OpenSpace's panels annotated.
:::

We will discuss details of each of these panels in the [Using OpenSpace](/using-openspace/index) chapter. For now, we will give you an overview of each panel.





## Dashboard

The Dashboard reports information in realtime about your status and location in OpenSpace.

:::{figure} dashboard_default.png
:align: center
:width: 60%
:alt: Default Dashboard display.
The default Dashboard display.
:::

It reports on:
- Current date and time in Universal Time (UT)
- The simulation increment
- Your distance to the current focus
- Average frames per second (FPS)---useful for seeing how well OpenSpace is performing on your system
- Position, in Latitude and Longitude, and altitude from the object set to Focus


### Set What is Shown

In Settings Menu, under Dashboard, you can set what appears in the Dashboard, or turn it off completely.

:::{figure} settings_menu_dashboard.png
:align: center
:width: 40%
:alt: The Dashboard settings

{menuselection}`Settings --> Dashboard`
:::

The full-on Dashboard with all items on looks like this:

:::{figure} dashboard_full.png
:align: center
:width: 50%
:alt: The Dashboard with all items on

The Dashboard with all items displayed.
:::



## Flight Friction Status

An important aspect of navigating in OpenSpace, a topic we will discuss soon, is friction. When friction is on and you let off the gas (either let go of the mouse button or your controller), your flight will gradually come to a halt. This is friction.

In OpenSpace you can toggle friction on and off using keyboard shortcuts. There is one for each type of flight: Rotation, Zoom, and Roll.

When you start OpenSpace, friction for each of these types of flight is on. This is indicated by green indicators in the Friction Status, like this:

:::{figure} friction_status_default.png
:align: center
:width: 20%
:alt: Friction status is on

Friction status is "on".
:::


You can use keyboard shortcuts (recommended) or click on the green Flight Mode words to toggle them on and off.

To toggle friction on and off, we use these keys:
:::{list-table}
:header-rows: 1
:stub-columns: 1
:align: center
* - Shortcut
  - Function
* - {kbd}`f`
  - Toggle rotational friction on and off
* - {kbd}`Shift` + {kbd}`f`
  - Toggle zoom friction on and off
* - {kbd}`Ctrl` + {kbd}`f`
  - Toggle roll friction on and off

:::

If we turn the rotational friction off, so when we orbit it will continue at a constant pace once we let go of the controller, the Friction Status will look like this:

:::{figure} friction_status_on.png
:align: center
:width: 20%
:alt: Friction status is off for rotational flight (orbiting)

Friction status is "off" for rotational flight (orbiting).
:::




## Version

In the bottom-right of the Graphics Window is the version number you are running. This cryptic string reflects the current build you are using, and can be useful for troubleshooting.

The string is the branch and commit you are running, for those who speak [Git](https://github.com/OpenSpace).
