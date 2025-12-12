---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---


# Actions Panel

![Action Panel Button](/using-openspace/toolbar/actions/toolbar_button_actions.png)

## What Is an Action?

Actions are set of instructions that can automatically alter one or more properties in OpenSpace. Typically, one would alter these properties in the Scene Panel, but Actions automate one or more such adjustments with the press of a button. These can be used to make a planet larger, turn off object trails, or change the Simulation Speed or time, among many other things. There is no editor, per se, to create actions---currently they are only available via asset files by coding the proper OpenSpace commands.


:::{note}
Authoring actions is too advanced for this section. We will discuss authoring actions later in this guide (coming soon).
:::

The idea with an action is to automate one or many adjustments that you would otherwise have to enact via checking something on or off, adjusting a slider, or changing a color. With one button, you can accomplish many adjustments to many datasets to craft a scene to your liking.


:::{figure} actions_panel.png
:align: center
:width: 50%
:figwidth: 90%
:alt: OpenSpace's Actions Panel

The Actions Panel with buttons that open hierarchical folders of related actions.
:::




## Using the Actions Panel

The panel has three main sections: your location, a search box, and the folder and action buttons.

### Your location
At the top of the panel is the current location. This is denoted by a house icon, which represents the top, or root. When you navigate into subfolders, for example if you press the {menuselection}`Trails` action button (which is a folder denoted by its icon), the location will appear as {octicon}`home-fill;1em` / `Trails`. Click the parts of the location path, or use the arrow button, to go up in the folder hierarchy.

:::{figure} actions_panel_trails.png
:align: center
:width: 50%
:figwidth: 90%
:alt: Actions Panel's Trails folder

The Actions Panel's Trails folder, listing a number of actions related to trails.
:::


### Search for an Action
Use the search box to enter terms that go directly to an action. If you know the name or subject of the action, this is the quickest way to reach the button you want.

The search is relative to your current location in Actions Panel, so that only actions that are deeper in the hierarchy will be matched in the search. If you want to search among all loaded actions, go to the top level.


### Explore Actions
The primary way to explore the available actions is via the buttons in the panel. The buttons resemble a file system, where clicking on a folder (button with the {octicon}`file-directory;1em` icon) will open up a new view of actions and possible subfolders. Clicking on an action button will execute the action. As you descend into the actions hierarchy, your location within it will appear at the top of the window.

