# Focus

## Orbital Navigation and Focus
In order to fly to another place, you must change the _Focus_ object that the camera is attached to. To change your object of focus use the focus menu, located at the bottom of your screen between the settings and time menus:

:::{figure} focus-menu.png
:align: center
:width: 30%
The focus menu at the bottom of the screen used to change the current _Focus_
:::

Open the focus menu by clicking on it. You can either select your focus from the list or search for another node using the text field at the top of the focus window. Selecting a node will cause the camera to target the new _Focus_, but you still have to fly to it by zooming in. You can also click the airplane icon ![Fly-to](flyto_icon.png) which will cause the camera to fly to your selected _Focus_ automatically.

The amount of time taken to change the focus can be adjusted in the settings under {menuselection}`Settings --> Navigation Handler --> Orbital Navigator --> Retarget interpolation time`. The higher the number, the longer it will take to switch between targets. Similarly the {menuselection}`Settings --> Navigation Handler --> Path Navigator --> Speed Scale` allows you to adjust the time taken to automatically fly to another location.

:::{note}
**Many items will focus you on the Sun**

Since focusing on an item will always focus on its center, focusing on many items will appear to target the Sun instead. This is because items like "HII Regions" or "Jupiter Trail" are datasets centered on the sun. For these types of items, there is no point in focusing on them, instead target "Orion Nebula" or 'Jupiter.'
:::
