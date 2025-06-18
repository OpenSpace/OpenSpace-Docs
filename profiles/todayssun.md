---
authors:
  - name: Elon Olsson
    affiliation: Community Coordinated Modeling Center
---



# Today's Sun

This profile shows the Sun's magnetic field using outputs from the WSA (Wang-Sheeley-Arge) simulation model. All simulation data in this profile is downloaded dynamically during runtime. The visuals will be tied to the time in OpenSpace, so you can jump or scrub time to a previous time stamp within the sequence interval and see historic outputs visualized without needing to download all the data in between or the whole sequence. The field lines trace the Sun's magnetic field. Some loop back into the Sun (closed, shown in yellow), while others stream into space (open). The simulation data throughout this visualization is colored red for positive values and blue for negative. Red field lines indicate that the direction of the field is pointing away from the sun and blue that it is pointing inward toward the Sun. On the Sun's surface, white and black indicate areas of positive and negative magnetic polarity, respectively. Understanding these fields is critical, as solar activity like Coronal Mass Ejections (CMEs) can disrupt satellites, power grids,and pose risks to astronauts and spacecraft throughout the solar system.

This page focuses on the content in the profile and how to use it. For more information on the back-end, data and underlying features see [Space Weather](/creating-data-assets/space-weather).


::::::::{tab-set}

:::::::{tab-item} Tour

## Tour

The main visuals are solar surfaces and magnetic field lines. There are also a hand-full of different lines that help us get oriented better in space.

### Solar Surfaces

In total there are six assets with time varying textures on spheres. There are two different input data sources to the WSA simulation model, for three spheres each. The input sources are from GONG-Z and from GONG ADAPT.
The [Renderable Time Varying Fits Sphere](/reference/asset-components/RenderableTimeVaryingFitsSphere.md) is the renderable that visualizes the solar textures. These are created straight from the .fits files downloaded using the Dynamic File Sequence Downloader, and are not saved as images. For each scene graph node there are some settings in the Scene menu in the GUI in OpenSpace for these surface textures. First of all, there are alternative data sets, one per entry in the menu labeled Solar Surface. In the .fits files, there are different layers which show different data. By default the Observed Photospheric Field is shown, also known as magnetogram. There are other options to choose from. There is a setting to choose if you want to use a color map or not, and a field to specify a transfer function file (color map file) to change it. You can also choose to apply a linear smoothing filter, which makes the texture look more blurry rather than discrete pixel squares. Additionally there is an option to save the downloaded content for next time.
### Field Lines

### Guiding Lines

There is a white line that connects the Sun and Earth, as well as an arc that goes from pole to pole and intersect the Sun-Earth line, that show the longitude on the Sun that is facing Earth. Additionally the Carrington prime meridian longitude line is visualized in red and also a grid with 10 degrees (on default) between each segment.

:::::::




:::::::{tab-item} Keyboard Shortcuts

## Keyboard Shortcuts


No shortcuts provided.

:::::::

:::::::{tab-item} Data Sets

## Data Sets

:::::::




:::::::{tab-item} Dossier

## Dossier

:::{list-table}
:header-rows: 0
:stub-columns: 1
:align: left
:width: 90%

* - Name:
  - Today's Sun
* - File:
  - `data/profiles/spaceweather/todays_sun.profile`
* - Anchor:
  - [Sun](/content/solar-system/sun/sun/index)
* - Time:
  - Today, 2 hours ago
* - Author:
  - CCMC
* - License:
  - [MIT](https://github.com/OpenSpace/OpenSpace/blob/master/LICENSE.md)
* - Version:
  - 1.0
:::
:::::::
::::::::
