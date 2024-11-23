# Navigation
Here we will learn how to control the virtual camera to navigate around objects and fly to other places in the universe using a mouse and keyboard. A mouse with three buttons is recommended, but not necessary.


## Controlling the Camera
The camera is always focus on an object called the _Focus_. All navigation is always relative to the _Focus_ and remembering this will make the camera controls a lot more intuitive.

**Rotation**: Use the left mouse button and drag your mouse to rotate or orbit around your target. The camera will rotate in the direction you drag. How far you drag the mouse will determine how fast the camera will move.

**Zoom**: Use the right mouse button and drag to zoom closer or further away from your target. Dragging down will zoom away, and dragging up will zoom closer. How far you drag the mouse will determine how fast the camera moves. To zoom quickly, press and hold the 'Z' key.

**Roll**: Using the middle mouse button (depressing the scroll wheel) lets you roll the camera. If you do not have a third button, you can also roll the camera by holding the SHIFT key and dragging while pressing the left mouse button.

**Yaw/Pitch**: Hold the CTRL key while dragging with the left mouse button to yaw or pitch the camera away from the _Focus_. Especially in the beginning, use this movement sparingly as it is very easy to move the camera away from the _Focus_ and losing sight of it.

Try out the navigation by rotating around Earth, and trying to find your home town. When you are in the right approximate location, zoom in, and when you are close to Earth use the Yaw/Pitch motion to bring the camera up to see the horizon.

### Friction
By default, all camera movements have friction enabled that slows the camera to a stop after you let go of the mouse button. However, friction can be toggled independently for _Rotation_, _Zoom_, or _Roll/Yaw/Pitch_ by clicking the words in the upper right on-screen to toggle the type of friction you want to change. The easier way to toggle the friction is to use the {kbd}`F` (Rotation), {kbd}`Shift+F` (Zoom), or {kbd}`Ctrl+F` (Roll/Yaw/Pitch) keyboard shortcuts.

### Video Controls
This video shows how using the mouse lets you control the camera:
<iframe width="740" height="530" src="https://www.youtube.com/embed/uhbbGGgdcgM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Rotating around Earth by dragging while holding the left mouse button. |
| 0:39 | Zooming closer to and further away from Earth by dragging while holding the right mouse button. |
| 1:06 | Yaw or pitch the camera by pressing CTRL and dragging while holding the left mouse button. |
| 1:33 | Roll the camera by dragging while pressing the middle mouse button. |
| 1:42 | Toggle friction on and off by clicking the words in the upper right of the screen. |
| 3:48 | BONUS: Land on Earth using a combination of controls. |


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


## Leaving the Solar System
As you have just learned, most of the datasets are based around the Sun. To leave the Solar System, you just have to zoom away from your current target. And you will soon be flying among the stars.

### Video Menu
This video illustrates these concepts further:
<iframe width="740" height="530" src="https://www.youtube.com/embed/mJLMu8FC0OQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Retarget and fly to the Moon using the focus menu. |
| 0:30 | Change the retargeting speed in the settings menu. |
| 1:09 | The difference between focusing on Jupiter's trail, which will bring you to the Sun, and Jupiter, which will bring you to the planet. |
| 1:39 | Leave the Solar System by zooming away. |
