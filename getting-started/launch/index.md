---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Launching OpenSpace

Launching OpenSpace is as easy as double-clicking on the app from the `OpenSpace/bin` folder: \
`OpenSpace.exe` file in Windows, or \
`OpenSpace.app` file for macOS.


:::{tip}
If you see any errors or pop-up windows you're unsure about, please refer back to [](../install/index) and see the items under your operating system.
:::


## Terminal Window

The first item that pops up is a terminal with output streaming by at a rapid pace. The output to this window is basically all the commands OpenSpace is executing to get itself up and running. You can generally ignore this window; however, it can be useful for troubleshooting, though we recommend using the [OpenSpace Log](/using-openspace/log/index) to trace errors.

:::{figure} console.png
:align: center
:width: 70%
:alt: OpenSpace's Terminal Window
The Terminal Window, giving you real-time status of the launch.
:::


## Launcher Window

Next, the Launcher Window will appear with two basic options. 

:::::{grid} 1 1 2 2

::::{grid-item}
### Choose Profile
This is a drop-down menu with a list of available profiles. For the initial run, stick with the [`default` profile](/profiles/default/index).

### Window Options
The cryptic names in this list set the type of screen you're displaying OpenSpace. By default, the `scgt.config.single` setting is for a single screen, which is most appropriate for running on a computer.


### Start Button
Click the `START` button to bring up the Graphics Window with the chosen profile and window setting.
::::


::::{grid-item}
:::{figure} launcher.png
:align: center
:width: 100%
:alt: OpenSpace's Launcher Window
OpenSpace's Launcher Window pops up upon launching the app.
:::
::::

:::::


## Graphics Window

### Asset Loading Screen

The Asset Loading Screen gives you the status of each asset as it loads. On your first launch, OpenSpace needs to retrieve data from its servers, so this step can take a few minutes. 

Most assets load instantaneously, but some take some time to download then load. Each asset's name appears on the loading screen. As it downloads it's color is gray and it has a progress indicator beside it. As it loads it is yellow. And, once it's green it's loaded and will slowly fade from the screen.

Once you download the data once, it will be cached and the launch will progress more quickly next time.

:::{figure} loading-screen.png
:align: center
:width: 100%
:alt: OpenSpace's profile loading screen
The profile loading screen showing the status of loading each data set.
:::


### The Cosmos

Once the profile and all its assets have loaded, you will now have a view of Earth along with the user interface. Next, we will explore the [interface basics](/getting-started/orientation/index).

:::{figure} openspace.png
:align: center
:width: 100%
:alt: Earth as seen in OpenSpace
The initial view of Earth in OpenSpace when launching is complete (except for a portion of the cloud layer).
:::
