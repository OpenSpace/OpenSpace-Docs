---
authors:
  - name: Elon Olsson
    affiliation: Community Coordinated Modeling Center
---


(todayssun_id)=
# Today's Sun

This profile shows the Sun's magnetic field using outputs from the WSA (Wang-Sheeley-Arge) simulation model. All simulation data in this profile is downloaded dynamically during runtime. The visuals will be tied to the time in OpenSpace, so you can jump or scrub time to a previous time stamp within the sequence interval and see historic outputs visualized without needing to download all the data in between or the whole sequence. The field lines trace the Sun's magnetic field. Some loop back into the Sun (closed, shown in yellow), while others stream into space (open). The simulation data throughout this visualization is colored red for positive values and blue for negative. Red field lines indicate that the direction of the field is pointing away from the sun and blue that it is pointing inward toward the Sun. On the Sun's surface, white and black indicate areas of positive and negative magnetic polarity, respectively. Understanding these fields is critical, as solar activity like Coronal Mass Ejections (CMEs) can disrupt satellites, power grids,and pose risks to astronauts and spacecraft throughout the solar system.

This page focuses on the content in the profile and how to use it. For more information on the back-end, data and underlying features see [Space Weather](spaceweather_id).


::::::::{tab-set}

:::::::{tab-item} Tour

## Tour

The main visuals are solar surfaces and magnetic field lines. There are also a hand-full of different guiding lines that help us get oriented better in space.
The simulation data throughout this visualization is colored red for positive values and blue for negative.
### Solar Surfaces

In total there are six assets with time varying textures on spheres. There are two different input data sources to the WSA simulation model, for three spheres each. The input sources are from GONG-Z and from GONG ADAPT.
The [Renderable Time Varying Fits Sphere](fitsfilereader_renderable_time_varying_fits_sphere) is the renderable that visualizes the solar textures. These are created straight from the .fits files downloaded using the Dynamic File Sequence Downloader, and are not saved as images. For each scene graph node there are some settings in the Scene menu in the GUI in OpenSpace for these surface textures. In the .fits files, there are different layers which show different data. By default the Observed Photospheric Field is shown, also known as magnetogram. There are other options to choose from. There is a setting to choose if you want to use a color map or not, and a field to specify a transfer function file (color map file) to change it. You can also choose to apply a linear smoothing filter, which makes the texture look more blurry rather than discrete pixel squares. Additionally there is an option to save the downloaded content for next time.

### Field Lines

For the field lines [Renderable Field Lines Sequence](fieldlinessequence_renderablefieldlinessequence) is used to visualize them. The WSA simulation model has many components. The solar coronal portion of WSA is comprised of two potential field type models. The inner model is Potential Field Source Surface (PFSS) which specifies the coronal field from the inner, photospheric boundary at 1 solar radii (Rs) to its outer boundary or source surface at 2.5Rs. The outer model is the Schatten Current Sheet (SCS) model. The radial magnetic field components of the PFSS magnetic field solution at 2.5Rs are used as the inner boundary condition to the SCS model.
There are four different sets of field lines in this profile. The main difference is where the start points are for tracing the magnetic vector field. The field lines can either be closed, meaning they loop back onto the surface of the Sun, or they are open, meaning only one end of the line is at the surface.
Red field lines indicate that the direction of the field is pointing away from the sun and blue that it is pointing inward toward the Sun.

One is the Corona SCS, out to in tracing. These are field lines traced from the outer boundary at 21.5 Rs to the source surface at 2.5 Rs using GONGZ as input. These are open field lines per definition in the model.

Then there is Corona PFSS, in to out tracing and also out to in tracing. The in to out tracing are field lines traced from the solar surface outwards. This set of lines have both closed and open lines. The out to in tracing are field lines traced from the source surface at 2.5 Rs to the solar surface. They both use GONGZ as input.

Lastly there is the Tracing from Earth. These are field line trace from the Earth's orbit around the Sun, using GONGZ as input. These lines are composed with sets of three lines close to eachother to be able to find divergent areas in the field.

### Guiding Lines

A few guiding lines are added in the scene. There are there to help the user navigate around the Sun to get a better sense of orientation. There is a white line that connects the Sun and Earth, as well as an arc that goes from pole to pole and intersect the Sun-Earth line, that show the longitude on the Sun that is facing Earth. Additionally the Carrington prime meridian longitude line is visualized in red and also a grid with 10 degrees (on default) between each segment.

:::::::




:::::::{tab-item} Keyboard Shortcuts

## Keyboard Shortcuts

No additional shortcuts provided.

:::::::


:::::::{tab-item} Data Sets

## Data Sets

The data for this profile is visualized mainly by the two renderables: <br>
[Renderable Time Varying Fits Sphere](fitsfilereader_renderable_time_varying_fits_sphere) and [Renderable Field Lines Sequence](fieldlinessequence_renderablefieldlinessequence). They grab data on the data formats FITS and OSFLS respectively. They are downloading these data sets dynamicaly during run-time from the [Community Coordinated Modeling Center](https://ccmc.gsfc.nasa.gov/) (CCMC) at NASA Goddard Space Fight Center and their Integrated Space Weather Analysis (ISWA) system. It is using the [Dynamic File Sequence Downloader](spaceweather_id) to achive this.

The profile is exclusivly using simulation outputs from the space weather simulation model called [WSA](https://ccmc.gsfc.nasa.gov/models/WSA~5.4) version 5.4.

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
