---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Installing OpenSpace

This guide has information about installing the downloadable application from the [OpenSpace website](https://www.openspaceproject.com/).

:::{note}
If you wish to download the source code and build the application, please see [Compiling](/contribute/development/compiling/index).
:::


## Hardware Requirements

OpenSpace is designed for use on a wide array of devices ranging from laptops to state-of-the-art planetarium domes. However, its ability to create complex scenes demands graphics power to run efficiently.

::::{grid}
:::{grid-item}

%%%% Would be good to link or elaborate on AMD issues

### Minimum Requirements
- i5 processor (Apple's M-chip is not supported)
- NVIDIA 1060 GTX GPU (or comparable) (AMD cards work with some issues)
- 8 GB RAM
- 4 GB VRAM
- 25 Mbps internet connection is recommended (the [default profile](/profiles/default/index) requires an internet connection)

:::

:::{grid-item}
### Optimal Specs
- Windows 10 or above or macOS 10.15 or above
- 16 GB RAM (or more)
- 6 GB VRAM (or more)
:::
::::








## Installation

To install OpenSpace, follow these steps:
1. Download OpenSpace according to the instructions on the [OpenSpace website](https://openspaceproject.com) for your operating system.

2. Unzip or extract the resulting file.

3. Place the resulting unzipped folder anywhere you like. OpenSpace is self-contained. We recommend a location inside your user folder or home directory.

:::{tip}
Multiple versions of OpenSpace may be installed beside one another without conflict.
:::

4. Continue below for your particular operating system:

::::::::{tab-set}
:::::::{tab-item} Windows

### Windows Installation Video

<div style="margin-left: auto; margin-right: auto; width: 640px;"><iframe width="640" height="360" src="https://www.youtube.com/embed/YHl5L85hEUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{dropdown} Visual Transcript

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Download the zip file from the OpenSpace website. |
| 0:30 | Get the zip file from your downloads and extract the OpenSpace folder. |
| 0:50 | Find the .exe inside the extracted folder and create a desktop shortcut. |
| 1:04 | Running the application for the first time, you will get a Windows protection pop-up. Click "More info" then "Run Anyway." |
| 1:13 | When the Launcher opens, start OpenSpace with the start button. |
| 1:15 | You will be presented with more Windows protection pop-us, this time for the firewall. Click "Allow access" on each. |
| 1:35 | OpenSpace is started and you can use the application. |
:::
</div>



### Error: “VCRUNTIME140_1.dll was not found
If you receive this error, you will need to [download](https://aka.ms/vs/17/release/vc_redist.x64.exe) and install Microsoft Visual C++ Redistributable for Visual Studio 2022.



### Network Access Pop-ups 
Upon running OpenSpace for the first time, it will ask for permission to access the internet via two pop-up windows. If you do not give OpenSpace that permission, some important features, such as the user interface, will be inaccessible.


### Slow Performance---Low Frame Rate Issue

If your frame rate is low (the FPS number in the top left corner), please ensure that OpenSpace is using your dedicated graphics card. If the frame rate is debilitatingly slow, OpenSpace is probably using your system's integrated graphics card.

You can set which graphics OpenSpace uses via the following procedure:


::::::{dropdown} Windows 11

In Windows 11, these setting are found in Window's Settings App under {menuselection}`System --> Display --> Graphics`. 

:::{figure} windows_graphics_panel.png
:width: 50%
:align: center
:alt: Windows graphics settings

:::

1. Under `Add an app`, browse to choose the OpenSpace.exe file in the `OpenSpace/bin` folder in your main OpenSpace folder.

2. Click on the resulting OpenSpace entry in the list of apps, and click the `Options` button.

:::{figure} windows_graphics_panel_options.png
:width: 50%
:align: center
:alt: Windows graphics settings options
:::

3. Choose `High performance` and save.

::::::


::::::{dropdown} Windows 10

In Windows 10, assuming you have an NVIDIA card, you must use the NVIDIA Control Panel to set which application explicitly uses the NVIDIA card. Access the NVIDIA Control Panel through these steps:

1. Right click on the desktop to bring up the contextual menu.

:::{figure} context-menu.png
:width: 50%
:align: center
:alt: Windows context menu

Windows Desktop contextural menu.
:::

2. Select {menuselection}`NVIDIA Control Panel`.

:::{figure} control-panel.png
:width: 80%
:align: center
:alt: NVIDIA control panel

NVIDIA Control Panel.
:::

3. Select "Manage 3D settings" from the left navigation menu.
4. Search for the dropdown menu called "Preferred graphics processor."
5. These settings should indicate "Integrated graphics." Double-click that setting to choose "High-Performance NVIDIA processor."
6. Relaunch OpenSpace.

::::::







:::::::





:::::::{tab-item} macOS

### macOS Installation Video

<div style="margin-left: auto; margin-right: auto; width: 640px;"><iframe width="640" height="360" src="https://www.youtube.com/embed/uSceew-98Cg?si=SSP9iDw9Y0rsazFD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::{dropdown} Visual Transcript

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Download the pkg file from the OpenSpace website. |
| 1:45 | Run the pkg file to install OpenSpace. |
| 2:33 | If a macOS installation "unidentified developer" error pops up, go to System Preferences, Security & Privacy and click "Open Anyways." Another pop up will say the software cannot be verified. Click "Open." |
| 3:28 | Run the installer and close when it is complete. You can delete the pkg file when prompted. |
| 4:53 | Select the installed OpenSpace folder and {menuselection}`File --> Get Info`. In the info window, apply Read & Write privileges to the  OpenSpace folder. |
| 5:23 | Run the OpenSpace application, found in the `bin` folder. When the Launcher opens, start OpenSpace with the start button. |
| 6:25 | Open OpenSpace in low resolution mode by selecting the application and going to {menuselection}`File --> Get Info`. Check the box that says "Open in Low Resolution" and then run the application. |
:::
</div>



### macOS Folder Permissions
As demonstrated in the video, most users will need to adjust the folder permissions on the installed OpenSpace folder, and "Apply to Enclosed Items" as [outlined by Apple](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac).


### macOS "Unidentified Developer" Error
If you try to launch OpenSpace and you get an error that the application is not registered with Apple by an identified developer, you can follow [these steps from Apple](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac) to override macOS's default security settings to run OpenSpace.


### Open in Low Resolution Mode
For users running on a Retina display, you may want to apply the "Open in Low Resolution Mode" setting on the OpenSpace.app to get better performance.
%%%% HOW ISD THIS DONE???
:::::::





:::::::{tab-item} Linux

### Linux Installation

A binary version exists for Debian on the [OpenSpace website](https://www.openspaceproject.com/).

All other Linux platforms will require you to build the application. Please see [Compiling](/contribute/development/compiling/index).

:::::::
::::::::


## Uninstalling OpenSpace
Because OpenSpace is self-contained, all the files it needs to run are in the OpenSpace folder where you installed it.

Uninstalling OpenSpace is as easy as deleting the OpenSpace folder.


## Getting Help
If you encounter any errors with installing OpenSpace, please reach out to us on [Slack](https://openspacesupport.slack.com/).

Or, for the code-savvy, create an [issue](https://github.com/OpenSpace/OpenSpace/issues/new) on OpenSpace's GitHub.