# Sonification
The [Telemetry Module](index.md) can be used together with a _sonification_ of the planets in our solar system. Sonification is the concept of conveying information using sound (in contrast to visualization, where information is conveyed using images). In addition to the telemetry module, the sonification requires a separate application/program called [SuperCollider](#supercollider). This software will be used as the receiver for the OSC messages from the telemetry module.

The files for the sonification can be found in _data\assets\modules\telemetry\sonification_ in the OpenSpace folder. The file _planets.asset_ is a regular OpenSpace asset that configures the telemetry module to monitor each of the planets in the solar system and their major moons. The sonification file itself is the _OpenSpaceSonification.scd_ file, which is a SuperCollider file and needs to be run separately in that program. The sonification will then be produced by SuperCollider and just uses the information that OpenSpace sends with the OSC messages provided by the telemetry module.

:::{note}
Note that the _planets.asset_ file cannot be customized or altered since the sonification expects the data from the telemetry module to be in a certain format determined by this file. If this file is altered, then the sonification file needs to be updated to reflect the change as well. If you want to create your own sonification for objects in OpenSpace other than the planets, then the general [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) telemetry type is likely a better fit for that purpose.
:::

## SuperCollider
[SuperCollider](https://supercollider.github.io/) is the software used to produce the sounds of the sonification. The messages from the telemetry module are sent to SuperCollider and it then uses that information to create sounds that respond to that information. To run the sonification follow the steps below:

<!-- @TODO (malej) Add instruction on how to add needed SuperCollider dependencies to run the sonification in an immersive surround environment -->

1. Download and install [SuperCollider](https://supercollider.github.io/)
1. Run the SuperCollider planets sonification file _OpenSpaceSonification.scd_ located in _data\assets\modules\telemetry\sonification_.
    - To run the file in SuperCollider, click on line 8 and press CTRL + ENTER
    - Wait a while for the sonification to boot up
    - The SuperCollider console should respond with: `Sonification is ready` when it is finished
1. Run OpenSpace with the profile called _sonification_
1. Turn on the Telemetry module in the user interface under _Settings/Modules_
1. Turn on the telemetries/sonifications that are of interest with the checkboxes in the telemetry module settings
1. Fly around in OpenSpace, and you should see messages being printed in the SuperCollider console window
1. Now, you can freely try the different settings for the different telemetries/sonifications, read the tooltips, and stress-test it in general.

:::{danger}
Due to an unsolved issue with the Scene not being safe for multiple threads, especially around startup, the telemetry module cannot be enabled before OpenSpace has completely initialized.
:::

## The Sounds of the Planets Sonification
The table below describes what aspects of the planets are conveyed by the sonification, how they sound, and how the sounds change depending on the data.
:::{table}
:align: center
| Planet Property      | Sonification Sound        | Mapping Polarity                                            |
|----------------------|---------------------------| ------------------------------------------------------------|
| Mass                 | Pitch                     | Higher pitch = Lower mass                                   |
| Length of day        | Tempo of oscillation      | Faster tempo = Shorter day                                  |
| Length of Year       | Surround position         | Uses [angle calculations](./angle-information.md#angle-calculations-explanation) to place the planet in a surround sound configuration |
| Gravity              | Bouncing ball sound       | Faster bouncing ball = Stronger gravity                     |
| Temperature          | Sizzling intensity        | More sizzling = Higher temperature                          |
| Atmospheric pressure | Depth of wind sound       | Deeper wind sound = Higher atmospheric pressure             |
| Average wind speed   | Fluctuation of wind sound | More fluctuations in wind sound = Faster average wind speed |
:::

:::{note}
Note that the sonification uses additional data provided in the SuperCollider files. This data comes from the [Nasa Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
:::

:::{seealso}
For more details about the sonification of the planets see the paper **OpenSpace Sonification: Complementing Visualization of the Solar System with Sound** by Elias Elmquist, Malin Ejdbo, Alexander Bock, and Niklas Rönnberg, published in _International Community for Auditory Displays_, 2021 [doi:10.21785/icad2021.018](http://dx.doi.org/10.21785/icad2021.018).
:::

## Surround Sound Configurations
The surround sound aspect of the sonification is designed for two specific configurations, as shown in the images below. In both images, black dots represent speakers, and the subwoofer is positioned outside the circle since it is not considered a directional sound source.

<!-- @TODO (malej) Generate a dark mode version of this image -->
:::{image} images/NKPG-Dome.png
:alt: "Surround Sound Configuration Schematic for the Visualization Center Dome Theater in Norrköping, Sweden"
:width: 100%
:align: center
:class: only-light
:::

This image shows a top-down view of the surround sound setup for the Visualization Center Dome Theater in Norrköping, Sweden. The audience sits in rows inside the circle, facing the front center of the dome surface, which is marked as _Center_ at the top of the image. The circle represents the edge of the dome surface. This configuration uses the [Horizontal](./angle-information.md#horizontal) angle calculation mode without the elevation angle, as it only has one ring of speakers.

<!-- @TODO (malej) Generate a dark mode version of this image -->
:::{image} images/AMNH-Dome.png
:alt: "Surround Sound Configuration Schematic for the Hayden Planetarium at the American Museum of Natural History in New York, USA"
:width: 100%
:align: center
:class: only-light
:::

This image shows a bottom-up view of the surround sound setup for the Hayden Planetarium at the American Museum of Natural History in New York, USA. The audience sits in concentric rings inside the outermost circle, looking up towards the center of the dome surface, which is marked as _Center_ with a blue cross in the middle of the image. The outermost ring represents the edge of the dome surface. This configuration uses the [Circular](./angle-information.md#circular) angle calculation mode with the elevation angle enabled, as it has multiple rings of speakers.
