---
authors:
  - name: Brian Abbott, Alex Bok
    affiliation: American Museum of Natural History
---


# SkyBrowsing Panel

:::{figure} toolbar_skybrowser.png
:align: center
:width: 1000px
:alt: Toolbar with the SkyBrowsing Panel highlighted

The SkyBrowser Panel Button in the OpenSpace Toolbar.
:::


:::{warning}
This section is in progress. Text will appear on this page in the future.
:::



## Sky Browser
The Sky Browser feature is a virtual telescope. It lets you see telescope images taken by famous telescopes, such as Hubble, Chandra and Spitzer, while also visualizing their locations in the sky. The Sky Browser is powered by [AAS WorldWide Telescope](http://worldwidetelescope.org/webclient/).


## Browser
The browser displays a part of the sky. By clicking images in the list, you can load them into the browser. It is possible to change the opacity and the ordering of the images by using the buttons in the browser's tab. You can add many browsers and select between them in the tab section.


## Target
Each target belongs to a browser and is either in the shape of a crosshair or a crosshair and a rectangle. It shows where the browser is aiming and how large a portion of the sky it is viewing. The target can be moved around by dragging on the Sky Browser.


## Image list
The image list has two modes: Images Within View and All Images. The Images Within View mode display the images that are currently in the view of the target. It changes as you move around the target. The All Images displays all images in the collection in alphabetical order.


## Tab buttons
![Tab buttons](tabbuttons.png)

From left to right:
  - Look at target: Rotates the camera so that the target is placed in the center of the view
  - Move target to center of view: Animates the target so that it is placed in the center of the view
  - Zoom in: Makes the vertical field of view of the target 10 degrees smaller
  - Zoom out: Makes the vertical field of view of the target 10 degrees larger

  - Point Spacecraft: Dispatches an event to the space crafts in the scene to look at the target
  - Remove all images: Remove all images that had been added to the browser
  - Settings: Settings for this particular browser and general settings

## Display Copies
Sometimes it is necessary to show the browser outside of the graphical user interface, for example, if you are in a dome or are using a display wall. To display the sky browser there, you can simply add Display Copies. The Display Copies are rendered in the 3D environment in OpenSpace and will be visible even if the GUI is not shown. If you are in a dome environment, you can add many Display Copies at once in order to spread them out on the Azimuth.
  - Scale: Sets the height of the Display Copy
  - Face Camera: Rotates the Display Copy to face the camera
  - Use Radius Azimuth Elevation: Uses spherical coordinates instead of Cartesian
  - Position for first copy: The position for a new Display Copy. If more than one copy is added, they will be spread out evenly on the Azimuth
  - Number of copies: How many new copies are added

## General Settings
  - Show Title in GUI: Displays the title of the sky browser on the top bar of the browser
  - Allow Camera Rotation: Decides if the camera should rotate if the target is outside of the master node screen
  - Camera Rotation Speed: The speed of the camera rotation. A higher number means higher speed
  - Target Animation Speed: The speed of the animation of the target. A higher number means higher speed
  - Field of View Animation Speed: the speed of the animation of the field of view. A higher number means higher speed
  - Hide targets and browsers with GUI: If checked, the targets and browsers are not rendered if the sky browser panel is not visible
  - Inverse Zoom Direction: Flips the zoom direction
  - Space Craft Animation Time: Sets the animation time for moving space crafts in seconds
