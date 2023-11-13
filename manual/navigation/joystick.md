# Joystick navigation
In addition to the normal navigation using the keyboard and mouse, it is also possible to navigate using a controller, such as an Xbox controller, PS4 controller, or a SpaceMouse. If you want to use any of these supported controllers you need to include their corresponding `.asset` file in a profile. See the manual on [Profiles](../content/profiles) for further information about this. All of the joystick assets are located in the sub-folder `data/assets/util/joysticks` inside the OpenSpace folder. It is important to include the right asset file for the type of controller you are using. For example, the wireless Xbox asset will not work with a non-wireless Xbox controller and vice versa. If you are unsure about what type of controller you are using, you could instead try to include the `any-joystick` asset. This asset will try to auto-detect what type of controller is connected to the computer and add the corresponding asset file automatically. If you want to use a controller that does not have an already provided asset file in OpenSpace, you can create your own asset file for it, see [Joystick Customization](joystick-customization) for an in-depth guide. The same page also includes information on how to customize the asset files to enable new functionality.


## Xbox controller
The image below shows a map of the buttons and joysticks on an Xbox controller.

:::{image} xbox.png
:alt: "Xbox Controller Schematic"
:width: 80%
:align: center
:class: only-light
:::

:::{image} xbox_dark.png
:alt: "Xbox Controller Schematic"
:width: 80%
:align: center
:class: only-dark
:::

Navigation using an Xbox controller in OpenSpace is defined in the Xbox asset file (`xbox.asset`) or the Xbox wireless asset file (`xbox-wireless.asset`). The table below shows the function for each button or joystick on the Xbox controller. NA in the table specifies that this button or joystick has no functionality per default, read more about how to add or customize functionality in [Joystick Customization](joystick-customization).

| Button or joystick | Description |
|--------------------|-------------|
| A | Toggle rotation friction |
| B | Toggle zoom friction |
| Y | Toggle roll friction |
| X | NA |
| LB | Focus on the previous object in the interesting objects list |
| RB | Focus on the next object in the interesting objects list |
| LT | Zoom out |
| RT | Zoom in |
| Up | Pressed: Enable local roll for right joystick left/right <br/> Released: Disable local roll for right joystick left/right |
| Right | Make time go faster forward, press several times for faster |
| Left | Make time go faster backward, press several times for faster |
| Down | Reset time speed to real-time |
| Left joystick up/down | Orbit around focus up/down |
| Left joystick left/right | Orbit around focus left/right |
| Left joystick Press | NA |
| Right joystick up/down | Pan camera up/down |
| Right joystick left/right | Pan camera left/right <br/>If Up is pressed: Roll camera |
| Right joystick Press | Refocus the camera, look at the currently focused object |
| Select | Reset time to yesterday |
| Start | Pause time |


## PS4 controller
The navigation using an Xbox or PS4 controller is very similar, the only difference is the layout of the controllers. Otherwise, the functionality is the same. The image below shows a map of the buttons and joysticks on a PS4 controller.

:::{image} ps4.png
:alt: "PS4 Controller Schematic"
:width: 80%
:align: center
:class: only-light
:::

:::{image} ps4_dark.png
:alt: "PS4 Controller Schematic"
:width: 80%
:align: center
:class: only-dark
:::

Navigation using a PS4 controller in OpenSpace is defined in the PS4 asset file (`ps4.asset`). The table below gives an overview of what each button or joystick on the PS4 controller does in OpenSpace. NA in the table specifies that this button or joystick has no functionality per default, read more about how to add or customize functionality in [Joystick Customization](joystick-customization).

| Button or joystick | Description |
|--------------------|-------------|
| Cross | Toggle rotation friction |
| Circle | Toggle zoom friction |
| Triangle | Toggle roll friction |
| Square | NA |
| L1 | Focus on the previous object in the interesting objects list |
| R1 | Focus on the next object in the interesting objects list |
| L2 | Zoom out |
| R2 | Zoom in |
| Up | Pressed: Enable local roll for right joystick left/right <br/> Released: Disable local roll for right joystick left/right |
| Right | Make time go faster forward, press several times for faster |
| Left | Make time go faster backward, press several times for faster |
| Down | Reset time speed to real-time |
| Left joystick up/down | Orbit around focus up/down |
| Left joystick left/right | Orbit around focus left/right |
| Left joystick Press | NA |
| Right joystick up/down | Pan camera up/down |
| Right joystick left/right | Pan camera left/right <br/>If Up is pressed: Roll camera |
| Right joystick Press | Refocus the camera, look at the currently focused object |
| Share | NA |
| Options | Reset time to yesterday |
| Touch Pad | Pause time |
| PS | NA |


## SpaceMouse
The SpaceMouse is a controller that has a joystick with 6 degrees of freedom that is sold by the company [3Dconnexion](https://3dconnexion.com/uk/spacemouse/). There are a few different versions of it and therefore there are a few different versions of the asset files that specify the navigation. The versions that are currently supported (since release 0.18.0) are the SpaceMouse Compact (`space-mouse-compact.asset`) and the SpaceMouse Enterprise (`space-mouse-enterprise.asset`). Both of these can be in wireless mode `space-mouse-compact-wireless.asset` and `space-mouse-enterprise-wireless.asset` respectively. The image below is a map of the different movements of the SpaceMouse and a translation of the terminology used by 3Dconnexion (3D) and the terminology used by OpenSpace (OS).

:::{image} spacemouse-map.png
:alt: "Spacemouse Mapping Schematic"
:align: center
:class: only-light
:::

:::{image} spacemouse-map_dark.png
:alt: "Spacemouse Mapping Schematic"
:align: center
:class: only-dark
:::

The table below gives an overview of what each button or joystick on the SpaceMouse does in OpenSpace. The `Left` and `Right` buttons are only supported for the Compact version of the SpaceMouse. However, if you are using the Enterprise version you can bind some of the buttons to a regular key on the keyboard and bind actions to them.

| Button or joystick | Description |
|--------------------|-------------|
| Push left/right    | Orbit around focus left/right |
| Push back/forth    | Orbit around focus up/down |
| Push up/down       | Zoom in/out |
| Twist left/right   | Pan camera left/right |
| Tilt left/right    | Roll camera |
| Tilt up/down       | Pan camera up/down |
| Left button        | Switch to local roll mode (Default) |
| Right button       | Switch to global roll mode |

The Left and Right buttons switch the roll mode to local or global respectively. The difference between these two is that the local roll mode rolls the camera around the center of the screen, while the global roll mode rolls the camera around the current focus.


## Customizing the joystick navigation
It is possible to customize the joystick navigation to your own liking. However, this will require some editing in the asset files, for an in-depth guide on how to do this see [Joystick Customization](joystick-customization). There you can also read more about how to define your own asset for a controller that OpenSpace does not yet provide an asset.


## Issues and solutions
Here is a list of some issues you can encounter related to the controllers and some tips on how to fix them.

### Openspace does not react to the controller input
The first thing to check here is that the controller is connected correctly to the computer, that the correct asset file has been included in the profile, and that the right profile is run. If OpenSpace still does not react to the controller then it is possible that your controller has a different name than what OpenSpace expects. You can check the name of your controller when OpenSpace is running in any profile. Press the *F1* button on the keyboard and you will see the old GUI interface of OpenSpace pop up. In the window called **OpenSpace GUI**, press the empty checkbox next to **Joysticks Information**. This will open a new window and here all the connected controllers will be listed. In this list you can search for your controller and note down what name it has in the list, ignoring the number in the end. The items in the list called *3Dconnexion KMJ Emulator* or *Summed contributions* can be ignored. The next step is to change the name of the controller in the asset file. Start by opening the asset file corresponding to your controller in a text editor. You will need to change one line of code that specifies the controller name, you can see an example for the Xbox controller below (all other joystick assets look similar).

```lua
  asset.onInitialize(function()
    local controller = XBoxController;
    local name = "Xbox Controller"; -- Change this to the name of your controller

    local deadzoneJoysticks = 0.2
    local deadzoneTriggers = 0.05

    ...
```

### Openspace keeps spinning even when the joysticks are not touched
This issue is caused by the deadzone being too small for the joysticks or the triggers on the controller. To fix it you can increase the size of the deadzone by editing one or two lines in the asset file. Start by opening the asset file corresponding to your controller in a text editor. You will need to change one or two lines of code that specify the deadzone size for the joysticks and triggers respectively, you can see an example for the PS4 controller below (all other joystick assets look similar).

```lua
  asset.onInitialize(function()
    local controller = PS4Controller;
    local name = "Wireless Controller";

    local deadzoneJoysticks = 0.2 -- Increase this number to increase the deadzone for the joysticks
    local deadzoneTriggers = 0.05 -- Increase this number to increase the deadzone for the triggers

    ...
```

Adjust these values until the spinning stops and the feel of the navigation is good. Every time you change the values you need to restart OpenSpace. If the value is too small then the spinning might still occur on some occasions, if the value is too large then OpenSpace reaction to the input might feel delayed.

### Have an issue that is not included in this list?
Have a look at our [GitHub](https://github.com/OpenSpace/OpenSpace) for more information and potential solutions, or open a [new issue](https://github.com/OpenSpace/OpenSpace/issues/new). You can also reach us on our [Slack](https://openspacesupport.slack.com).
