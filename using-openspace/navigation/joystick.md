# Joystick Navigation
In addition to keyboard and mouse controls, OpenSpace also supports game controllers (such as Xbox controllers) and SpaceMouse devices. To use one of these controllers, connect it and make sure to include its corresponding `.asset` file in your profile. Alternatively, drag-and-drop the asset file into OpenSpace while it is running or select it from the Asset window.

The joystick assets are located in the `data/assets/util/joysticks` folder inside the OpenSpace folder. Make sure to include the asset that matches your controller. If you are unsure which controller type you have, you could instead try to include the `any-joystick` asset. This asset checks what type of controller is connected to the computer and adds the corresponding asset file automatically, if available.

We have prepared assets for some common gamepad controllers (Xbox, PS4/PS5) and for the SpaceMouse. The following sections describe how to use these controllers in OpenSpace and what each button or joystick does.

If your controller is not supported by a provided asset, you can create your own. See [Joystick Customization](joystick-customization) for instructions on creating and customizing joystick assets.


## Xbox and PS4/PS5 Controllers
Navigation using an Xbox or PS4/PS5 controller in OpenSpace is defined in the respective asset files (`xbox.asset`, `ps4.asset`, `ps5.asset`). These all define the same functionality, but the buttons and joysticks are mapped to the respective controller.

The schematics and table below show the controller inputs and their assigned functions in the provided assets. N/A indicates that no function is assigned by default. Read more about how to add or customize functionality in [Joystick Customization](joystick-customization).


::::::{container} only-light
:::::{grid} 1 1 1 2
::::{grid-item}
:::{figure} xbox.png
:alt: "Xbox Controller Schematic"
:width: 100%
:align: center
Xbox controller
:::
::::
::::{grid-item}
:::{figure} ps4.png
:alt: "PS4 Controller Schematic"
:width: 100%
:align: center
PS4 controller (PS5 has same layout)
:::
::::
:::::
::::::

::::::{container} only-dark
:::::{grid} 1 1 1 2
::::{grid-item}
:::{figure} xbox_dark.png
:alt: "Xbox Controller Schematic"
:width: 100%
:align: center
Xbox controller
:::
::::
::::{grid-item}
:::{figure} ps4_dark.png
:alt: "PS4 Controller Schematic"
:width: 100%
:align: center
PS4 controller (PS5 has same layout)
:::
::::
:::::
::::::

:::{table}
:align: center
| XBOX | PS4/PS5 | Description |
| ---- | ------- | ----------- |
| A | Cross | Toggle rotation friction |
| B | Circle | Toggle zoom friction |
| Y | Triangle | N/A |
| X | Square | Reset time to yesterday (and real-time speed) |
| LB | L1 | Roll left |
| RB | R1 | Roll right |
| LT | L2 | Zoom out |
| RT | R2 | Zoom in |
| Up | Up | Pause/Unpause time |
| Right | Right | Make time go faster forward, press several times for faster |
| Left | Left | Make time go faster backward, press several times for faster |
| Down | Down | Reset time speed to real-time |
| Left joystick up/down | Left joystick up/down | Orbit around focus up/down |
| Left joystick left/right | Left joystick left/right | Orbit around focus left/right |
| Left joystick Press | Left joystick Press | Jump to the current anchor node |
| Right joystick up/down | Right joystick up/down | Pan camera up/down |
| Right joystick left/right | Right joystick left/right | Pan camera left/right |
| Right joystick Press | Right joystick Press | Refocus the camera, look at the currently focused object |
| Back | Share | Focus on the previous object in the interesting objects list |
| Start | Options | Focus on the next object in the interesting objects list |
| | Touch Pad | N/A |
| | PS | N/A |
:::


## SpaceMouse
The SpaceMouse is a controller that has a joystick with 6 degrees of freedom that is sold by the company [3Dconnexion](https://3dconnexion.com/uk/spacemouse/). There are a few different versions of it and therefore there are a few different versions of the asset files that specify the navigation. The versions that are currently supported (since release 0.18.0) are the SpaceMouse Compact (`space-mouse-compact.asset`) and the SpaceMouse Enterprise (`space-mouse-enterprise.asset`).

The image below is a map of the different movements of the SpaceMouse and a translation of the terminology used by 3Dconnexion (3D) and the terminology used by OpenSpace (OS).

:::{figure} spacemouse-map.png
:alt: "Spacemouse Mapping Schematic"
:align: center
Space Mouse mapping schematic, showing the different movements and their corresponding terminology in OpenSpace and 3Dconnexion.
:::

:::::{grid} 1 1 1 2

::::{grid-item}
The table to the right summarizes the SpaceMouse buttons and joystick controls in OpenSpace. The `Left` and `Right` buttons are only available on the Compact version. On the Enterprise version, these buttons can instead be mapped to keyboard keys and assigned actions.

The `Left` and `Right` buttons switch between local and global roll modes. Local roll rotates the camera around the screen center, while global roll rotates it around the current focus.
::::

::::{grid-item}

:::{table}
:align: right
| Button or joystick | Description |
| ------------------ | ----------- |
| Push left/right | Orbit around focus left/right |
| Push back/forth | Orbit around focus up/down |
| Push up/down | Zoom in/out |
| Twist left/right | Pan camera left/right |
| Tilt left/right | Roll camera |
| Tilt up/down | Pan camera up/down |
| Left button | Switch to local roll mode (Default) |
| Right button | Switch to global roll mode |
:::

::::
:::::

## Customizing the Joystick Navigation
It is possible to customize the joystick navigation to your own liking. However, this will require some editing in the asset files, for an in-depth guide on how to do this see [Joystick Customization](joystick-customization). There you can also read more about how to define your own asset for a controller that OpenSpace does not yet provide an asset.

## Issues and Solutions
Here is a list of some issues you can encounter related to the controllers and some tips on how to fix them.

:::{dropdown} OpenSpace Does Not React to Controller Input  ([Link](#joystick-issue-noinput))
(joystick-issue-noinput)=

First, check that the controller is connected, the correct asset file is included in the profile, and the correct profile is running. If OpenSpace still does not detect the controller, the controller name may not match the expected name.

To find the controller name, press *F2* while OpenSpace is running to open the "old" (legacy) OpenSpace GUI. In the window called **OpenSpace GUI**, enable the **Joysticks Information** window to view connected controllers. Find your controller in the list and note its name (ignore the number at the end). The items in the list called *3Dconnexion KMJ Emulator* or *Summed contributions* can be ignored.

Next, open the controller's asset file in a text editor and update the line specifying the controller name. An example for the PS4 controller is shown below (other joystick assets have a similar structure).

```lua
local name = "Wireless Controller"; -- Change this to the name of your controller

asset.onInitialize(function()
  local controller = PS4Controller;

  local deadzoneJoysticks = 0.2
  local deadzoneTriggers = 0.05
  ...
```

Some assets load mappings for multiple controllers, for example the `xbox.asset` which loads both a wired and wireless version. In this case, you will instead need to make sure your controller name is included in the list of supported names, as shown below.

```lua
local names = {
  "Xbox Controller",
  "Wireless Xbox Controller"
} -- Add the name of your controller to this list


local function bindInputs(name)
  local controller = XBoxController

  local deadzoneJoysticks = 0.2
  local deadzoneTriggers = 0.05
  ...
```
:::


:::{dropdown} Camera Keeps Spinning Without Input ([Link](#joystick-issue-nodeadzone))
(joystick-issue-nodeadzone)=

This issue is caused by a joystick or trigger deadzone that is too small. To fix it, open the asset file for your controller in a text editor and increase the deadzone values. The file contains one or two lines defining the deadzone size for the joysticks and triggers, respectively. An example for the PS4 controller is shown below (other joystick assets follow a similar structure).

```lua
asset.onInitialize(function()
  local controller = PS4Controller;

  local deadzoneJoysticks = 0.2 -- Increase this number to increase the deadzone for the joysticks
  local deadzoneTriggers = 0.05 -- Increase this number to increase the deadzone for the triggers
  ...
```

Adjust these values until the spinning stops and the feel of the navigation is good. Every time you change the values you need to restart OpenSpace. If the value is too small then the spinning might still occur on some occasions, if the value is too large then OpenSpace reaction to the input might feel delayed.
:::

**Do you have an issue that is not included in this list?**
Have a look at our [GitHub](https://github.com/OpenSpace/OpenSpace) for more information and potential solutions, or open a [new issue](https://github.com/OpenSpace/OpenSpace/issues/new). You can also reach us on our [Slack](https://openspacesupport.slack.com).
