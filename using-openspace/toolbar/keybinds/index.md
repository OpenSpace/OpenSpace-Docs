---
authors:
  - name: Brian Abbott
    affiliation: American Museum of Natural History
---

# Keybinds Panel

![Tour Panel Button](/using-openspace/toolbar/keybinds/toolbar_button_keybinds.png)

{menuselection}`Windows --> Keybinds`

The Keybinds Panel shows all the active keyboard bindings for the current profile loaded upon startup. These are so called keyboard shortcuts that perform tasks, often in lieu of the mouse acting on the user interface. For example, you can click on the Flight Friction buttons in the top-right corner of the window, but you can also use the keyboard to toggle the friction on and off (more on thnis below).

:::{note}
The keybinds panel images here reflect these set in the [Default Profile](/profiles/default/index). Keybind settings are profile-dependent.
:::

The Keybinds Panel is informative and interactive. It shows the active keybindings on a virtual keybnoard. You can click on any active key to see a description of its binding.

:::{figure} keybinds_panel.png
:align: center
:width: 100%
:alt: OpenSpace's Getting Started Keybinds Panel

OpenSpace's Keybinds Panel for the Default Profile.
:::


You can also see only the active keys for the modifier keys, {kbd}`Shift`, {kbd}`Ctrl`, and {kbd}`Alt`, by pressing on those keys in the panel with your mouse. For the Default Profile, these keybindings are:

:::{figure} keybinds_panel_shift.png
:align: center
:width: 100%
:alt: OpenSpace's Keybinds Panel for the shift key
:::

<br>


:::{figure} keybinds_panel_ctrl.png
:align: center
:width: 100%
:alt: OpenSpace's Keybinds Panel for the ctrl key
:::

<br>


:::{figure} keybinds_panel_alt.png
:align: center
:width: 100%
:alt: OpenSpace's Keybinds Panel for the alt key
:::


<br>


Once you select a key on the panel using your mouse, information for the keybinding will appear in the panel. For example, if we examine the {kbd}`f` key, we can see there are three separate keybindings assigned to it, and they each affect the flight friction:
- {kbd}`f` toggles the rotational friction on and off.
- {kbd}`Shift` + {kbd}`f` toggles the zoom friction.
- {kbd}`Ctrl` + {kbd}`f` toggles the roll friction.

:::{figure} keybinds_panel_f_key.png
:align: center
:width: 100%
:alt: OpenSpace's Getting Started Keybinds Panel
:::

<br>

The Keybindings Panel is a helpful way to learn the keyboard functionality, which will make using OpenSpace easier and, in the case of navigation, improves the [quality of the flight experience](getting-started--navigation--compound-motion).