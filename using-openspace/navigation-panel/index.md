---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Navigation Panel: Focus & Fly

:::{figure} toolbar_navigation.png
:align: center
:alt: Toolbar with the Navigation Panel highlighted

The Navigation Panel Button in the OpenSpace Toolbar.
:::

The Navigation Panel is primarily used to target an object and navigate to those objects.

The name of the object that is set to Focus will appear in the button, in this case Earth is set to Focus. If you focus on the James Web Space Telescope, then the button would expand to accommodate that name in the Toolbar.

:::{figure} /getting-started/orientation/panel_navigation.png
:align: center
:width: 50%
:figwidth: 80%
:alt: OpenSpace's Navigation Panel

The Navigation Panel, with a top, iconized menu that sets the menu below.
:::




The panel has an iconized submenu at the top that determines what you see in the panel:
- ![focus button](/getting-started/orientation/navigation_panel_focus_button.png) --- This shows the list of objects that you can quickly designate as Focus, and includes a search box to choose other data sets that don't appear in the menu.
- ![anchor button](/getting-started/orientation/navigation_panel_anchor_button.png) --- This brings the list of objects that one casn set as the anchor.
- ![aim button](/getting-started/orientation/navigation_panel_aim_button.png) --- Brings up a list of objects that one can choose to aim toward.


## Focus

In OpenSpace, there must be an object that is set as the Focus. This can be any asset that you load in the profile, or it can be the _root_: (0, 0, 0). In most profiles, Earth is set as the Focus because most data sets and navigation takes place around Earth.

The Focus is important because it affects _how_ one flies through data. With Earth as the default Focus, you will orbit around Earth with the {menuselection}`left mouse button` and you will zoom in and out relative to Earth with the {menuselection}`right mouse button`.

As long as the focused object remains in view, your flying will make sense. If the object that is set to Focus is out of view in the Graphics Window, then flying will be a little counterintuitive. We discuss this more in [](/getting-started/navigation/index).

:::{note}
See [](/getting-started/navigation/index) in [](/getting-started/index) for details about the Flight Modes and how the Focus affects each of them.
:::



### Change Your Focus

In order to visit another object in OpenSpace, it is easier, and often necessary, to make that object the Focus. This is particularly true if you want to visit another planet, moon, or spacecraft.

:::{note}
All of the large data sets in OpenSpace are observed from telescopes on Earth, or in low-earth orbit. These data sets are typically centered on Earth, so there is little need to change Focus to them because you're not attempting to fly up to an object, per se. Rather, you will examine these data from a macro level that allows you to view the entire data set.

There is no need to change focus unless you're planning to visit in individual point in space or object in the Solar System.
:::

To change the focus, make sure ![focus button](/getting-started/orientation/navigation_panel_focus_button.png){w=25px} is selected in the panel's top menu, then you can do one of three things:
- Click on the object in the resulting list,
- If the object you're looking for is not there, you can search for it, 
- If you don't know the name of the object you're looking for, hit the {menuselection}`More` button and an alphabetical list of all loaded assets will appear.


:::{dropdown} Changing the Focus Time


The time it takes to transition from one object to the newly focused object can be adjusted in the Settings Menu using Retarget Interpolation Time. \
{menuselection}`Settings --> Navigation Handler --> Orbital Navigator --> Retarget Interpolation Time`.

The higher the number, the longer it will take between the two targets.
:::


Once you select an object, OpenSpace will center that object up for you, but it will not fly there for you. That is the next step...



## Flying to an Object

Once you change your target, there are several ways to fly to that object.
- Because OpenSpace has centered the object up, you can use the Zoom Flight Mode and fly directly to it yourself at your own pace.
- ![refocus button](/getting-started/orientation/navigation_panel_panfly.png){w=25px} You can use the Refocus Button to have OpenSpace fly there by taking a straight line to the object but panning your view for a graceful tansition.
- ![fly to button](/getting-started/orientation/navigation_panel_fly.png){w=25px} You can use the Fly To Button to have OpenSpace fly to the object using a curved path to the target.
- Or, you can see a few more options on the context menu ![nav panel context menu](/getting-started/orientation/navigation_panel_context_menu_button.png), which offers the above options plus:
  * ![jump to button](/getting-started/orientation/navigation_panel_jump_button.png){w=25px} The Jump To Button which fades your view to black, then fades back up beside the object.


:::{dropdown} Changing the Flight Time
The time it takes to fly to a target can be adjusted in the Settings Menu using the Speed Scale. \
{menuselection}`Settings --> Navigation Handler --> Path Navigator --> Speed Scale`.
:::




## Setting an Anchor

![anchor button](/getting-started/orientation/navigation_panel_anchor_button.png) The Anchor panel menu reveals the list of possible objects to set as your anchor. The anchor object sets the "relative to" place. It also sets the focus.

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::


## Aim To an Object

![aim to button](/getting-started/orientation/navigation_panel_aim_button.png)

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::