---
authors:
  - name: OpenSpace Team
---

# Sonification
The [Telemetry Module](index.md) can be used together with [SuperCollider](#supercollider) to create a sonification. Sonification is the practice of conveying information using sound (in contrast to visualization, where information is conveyed using visuals). In addition to the telemetry module in OpenSpace, the sonification requires a separate program, for example [SuperCollider](https://supercollider.github.io/). However, any software can act as the receiver for the OSC messages from the telemetry module and use that information to generate sounds, creating a sonification.

:::{note}
Only one sonification can be listened to at a time in SuperCollider. Users need to keep in mind to disable the currently active sonification before enabling another one to listen to.
:::

## SuperCollider
[SuperCollider](https://supercollider.github.io/) is the software used to produce the sounds of the sonifications. The messages from the telemetry module are sent to SuperCollider, which then uses that information to create sounds that correspond to that information.
To run a sonification file in SuperCollider, follow the following steps:
  1. Download and install [SuperCollider](https://supercollider.github.io/) (if not already installed).
  1. Click any line within the outer parentheses `()` in the file and press <kbd>CTRL</kbd> + <kbd>ENTER</kbd>. For example, the line with the comment `// To run this example...` (should be around line 50) in the [_osc-example.scd_](#osc-example-sonification) file.
  1. Wait a while for SuperCollider to boot.
  1. When you want to stop the sonification in SuperCollider, press <kbd>CTRL</kbd> + <kbd>.</kbd> and go back to the second step to start it up again.

### Switching Audio Output
The [sonification examples from OpenSpace](#sonifications-provided-by-openspace) use the computer's default audio output device. To specify a different output device in SuperCollider, locate the line `o = Server.default.options;` (around line 55) in the example files and follow the steps below:

1. Open the SuperCollider file you want to switch the audio output device for and press <kbd>CTRL</kbd> + <kbd>B</kbd>.
1. Look for the `Device options:` list in the printed console output.
1. Find the desired device name in the list (e.g., `- MME : Headset Earphone (Poly BT700)   (device #6 with 0 ins 2 outs)`).
1. Add the line `o.outDevice_("Device Name");` below the line `o = Server.default.options;` in the sonification file, replacing `Device Name` with the chosen device name. The device name is the name found in the list, minus the dash at the start and the device information at the end (e.g., `MME : Headset Earphone (Poly BT700)`).

### Ambisonics
To run the sonification with ambisonics, a few additional plugins must be installed in SuperCollider. Once installed, these plugins enable ambisonics functionality in SuperCollider for an enhanced surround experience. Follow these steps to install them:

1. Locate the Extensions folder of SuperCollider:
    - Run `Platform.userExtensionDir` in SuperCollider to find the path to the extensions folder. This command is included in all the example files provided by OpenSpace, located below the copyright header (around line 25).
    - Click the line with this command and press <kbd>CTRL</kbd> + <kbd>SHIFT</kbd>. The console will display a path similar to _C:\Users\user\AppData\Local\SuperCollider\Extensions_.

1. Install the Required Plugins:
    - **VST Plugin**:
        - Download [VST Plugin](https://git.iem.at/pd/vstplugin/-/releases).
        - Place the downloaded plugin folder in the SuperCollider extensions folder.
    - **IEMPluginOSC**:
        - Download [IEMPluginOSC](https://git.iem.at/ressi/iempluginosc).
        - Place the downloaded plugin folder in the SuperCollider extensions folder.
    - **IEM Plug-in**:
        - Download [IEM Plug-ins](https://plugins.iem.at/download/).
        - Create a folder named _VSTPlugins_ in _C:\Program Files_.
        - Move all `.dll` files from the downloaded IEM Plug-in into this folder.

1. Restart SuperCollider after the plugins have been installed.

## Sonifications Provided by OpenSpace
OpenSpace currently provides five sonifications. The first is the {ref}`Planets Sonification <planets-sonification-details>`, which is a complete sonification of the planets in the solar system. Then there are two smaller example sonifications that use the [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) telemetry type, the [Space Station Sonification](#space-station-sonification), and the [Voyager Sonification](#voyager-sonification). Lastly, there is the [OSC Example Sonification](#osc-example-sonification), which does not produce any sounds but instead contains more details on each telemetry type and basic examples of how to receive the OSC messages in SuperCollider.

### Planets Sonification
(planets-sonification-details)=
OpenSpace provides a sonification of the planets in the solar system. The files for this can be found in the folder _data\assets\modules\telemetry\sonification_ within the OpenSpace directory. The file _planets.asset_ is a regular OpenSpace asset that configures the [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) in the telemetry module to monitor each of the planets in the solar system and their major moons. The sonification file itself is the _planets-sonification.scd_ file, which is a SuperCollider file and needs to be run separately in that program. The sonification will then be produced by SuperCollider using the information received from OpenSpace with the OSC messages from the telemetry module.

:::{important}
The _planets.asset_ file cannot be customized or altered since the sonification expects the data from the telemetry module to be in a certain format determined by this file. If this file is altered, then the sonification file needs to be updated to reflect the change as well. If you want to create your own sonification for objects in OpenSpace other than the planets, then the general [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) telemetry type is likely a better fit for that purpose.
:::

The telemetry module contains several telemetry types that send different information to the OSC receiver. The planets' sonification only uses some of the available telemetry types, namely:
  - [Planets Sonification](./telemetry-types-specialized.md#planets-sonification)
  - [Planets Compare Sonification](./telemetry-types-specialized.md#planets-compare-sonification)
  - [Planets Overview Sonification](./telemetry-types-specialized.md#planets-overview-sonification)
  - [Focus](./telemetry-types-general.md#focus)
  - [Time Information](./telemetry-types-general.md#time-information)
  - [Angle Calculation Mode](./telemetry-types-general.md#angle-calculation-mode)

The steps below explain how to run the planet sonification provided by OpenSpace:
  1. Download and install [SuperCollider](#supercollider) (if not already installed).
  1. Run the sonification file _planets-sonification.scd_ located in _data\assets\modules\telemetry\sonification_ in SuperCollider.
      - To run the file in SuperCollider, find the line with the comment `// To run this sonification...` (should be around line 50), click on that line and press <kbd>CTRL</kbd> + <kbd>ENTER</kbd>.
      - Wait for the sonification to boot up.
      - The SuperCollider console should display: `Sonification is ready` when it finishes booting.
  1. Run OpenSpace with any profile (make sure that the planets and their major moons are included).
  1. Load the asset file _planets.asset_ (which is located in the same directory as the sonification file) either by dragging and dropping the file into OpenSpace while it is running, or by creating a new profile that loads that asset.
  1. Turn on the Telemetry module in the user interface under _Settings/Modules_.
  1. Turn on the telemetry types that are of interest with the checkboxes in the telemetry module settings (refer to the list above).
  1. Fly around in OpenSpace and enjoy the sonification. When flying close to a planet, when its sonification is enabled in the Planets Sonification, you should be able to hear it.

#### The Sounds of the Planets Sonification
The table below briefly describes what aspects of the planets are conveyed by the sonification, how they sound, and how the sounds change depending on the data. A demo of the sonification and its sounds can be listened to in the video below.

<center><iframe width="740" height="530" src="https://player.vimeo.com/video/528822742?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" title="OpenSpace Sonification" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media"></iframe></center>

:::{table}
:align: center
| Planet Property      | Sonification Mapping      | Mapping Polarity                                            |
|----------------------|---------------------------|-------------------------------------------------------------|
| Mass                 | Pitch                     | Higher pitch = Lower mass                                   |
| Length of Day        | Tempo of oscillation      | Faster tempo = Shorter day                                  |
| Length of Year       | Surround position         | Uses [angle calculations](./angle-information.md) to place the planet in a surround sound configuration |
| Gravity              | Bouncing ball analogy     | Faster bouncing ball = Stronger gravity                     |
| Temperature          | Sizzling intensity        | More sizzling = Higher temperature                          |
| Atmospheric Pressure | Depth of wind sound       | Deeper wind sound = Higher atmospheric pressure             |
| Average Wind Speed   | Fluctuation of wind sound | More fluctuations in wind sound = Faster average wind speed |
| Distance to the Planet (From the Camera) | Loudness | Louder = Closer |
:::

:::{note}
The planets sonification uses additional planetary data that is specified in the _planets-sonification.scd_ file and does not solely depend on the data from OpenSpace. This data comes from the [Nasa Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/) and does not change.
:::

:::{seealso}
For more details about the sonification of the planets, see the paper **OpenSpace Sonification: Complementing Visualization of the Solar System with Sound** by Elias Elmquist, Malin Ejdbo, Alexander Bock, and Niklas Rönnberg, published in _International Community for Auditory Displays_ in 2021 [doi:10.21785/icad2021.018](http://dx.doi.org/10.21785/icad2021.018).
:::

### Space Station Sonification
This sonification is a smaller example using the [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) telemetry type. It uses the file _space-station-sonification.scd_, which can be found in the folder _data\assets\examples\sonification_ within the OpenSpace directory. This sonification follows the two space stations ISS and Tiangong in OpenSpace and makes sounds when the camera is located close to either of them.

The steps below explain how to run the space station sonification provided by OpenSpace:
  1. Download and install [SuperCollider](#supercollider) (if not already installed).
  1. Run the sonification file _space-station-sonification.scd_ located in _data\assets\examples\sonification_ in SuperCollider.
      - To run the file in SuperCollider, find the line with the comment `// To run this example...` (should be around line 50), click on that line and press <kbd>CTRL</kbd> + <kbd>ENTER</kbd>.
      - Wait a while for the sonification to boot up.
      - The SuperCollider console should respond with: `Sonification is ready` when it is finished booting.
  1. Run OpenSpace with any profile (make sure that the ISS and Tiangong models are included).
  1. Load the asset file _nodes-space-stations.asset_ (which is located in the same directory as the sonification file) either by dragging and dropping the file into OpenSpace while it is running, or by creating a new profile that loads that asset.
  1. Turn on the Telemetry module in the user interface under _Settings/Modules_.
  1. Turn on the Customized Nodes Information telemetry (called Nodes Telemetry in the user interface) type with the checkbox in the telemetry module settings.
  1. Fly around in OpenSpace and enjoy the sonification. When flying close to ISS or Tiangong, when the sonification is enabled, you should be able to hear it.

This example demonstrates using SuperCollider to create a simple parametric sonification based on OSC messages from OpenSpace's telemetry module. The sonification emits a impulse sound for both stations, with Tiangong having a higher pitch and ISS a lower pitch. The sound's loudness varies based on the distance to each station.

### Voyager Sonification
This sonification is a smaller example using the [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) telemetry type. It uses the file _voyager-sonification.scd_, which can be found in the folder _data\assets\examples\sonification_ within the OpenSpace directory. This sonification follows the Voyager 1 and 2 space probes in OpenSpace and plays the sonification when the camera is located close to either of them.

The steps below explain how to run the Voyager sonification provided by OpenSpace:
  1. Download and install [SuperCollider](#supercollider) (if not already installed).
  1. Run the sonification file _voyager-sonification.scd_ located in _data\assets\examples\sonification_ in SuperCollider.
      - To run the file in SuperCollider, find the line with the comment `// To run this example...` (should be around line 50), click on that line and press <kbd>CTRL</kbd> + <kbd>ENTER</kbd>.
      - Wait a while for the sonification to boot up.
      - The SuperCollider console should respond with: `Sonification is ready` when it is finished booting.
  1. Run OpenSpace with the missions/voyager profile (or any profile as long as the Voyager 1 and 2 space probes are included).
  1. Load the asset file _nodes-voyager.asset_ (which is located in the same directory as the sonification file) either by dragging and dropping the file into OpenSpace while it is running, or by creating a new profile that loads that asset with the profile editor.
  1. Turn on the Telemetry module in the user interface under _Settings/Modules_.
  1. Turn on the Customized Nodes Information (called Nodes Telemetry in the user interface) telemetry type with the checkbox in the telemetry module settings.
  1. Fly around in OpenSpace and enjoy the sonification. When flying close to either Voyager 1 or 2 when the sonification is enabled, you should be able to hear it.

This is an example of how to use SuperCollider to create a sonification using local sound files. When the camera is near Voyager 1 or 2, the sonification will play and loop the [Greetings to the Universe](https://science.nasa.gov/mission/voyager/golden-record-contents/greetings/) audio clip, one of the recordings included on the golden records aboard both probes.

### OSC Example Sonification
This is an example sonification that does not produce any sounds but instead provides additional documentation for each telemetry type and provides basic examples of how the OSC messages can be received from OpenSpace. It uses the file _osc-example.scd_, which can be found in the folder _data\assets\examples\sonification_ within the OpenSpace directory.

The steps below explain how to run the OSC example sonification provided by OpenSpace:
  1. Download and install [SuperCollider](#supercollider) (if not already installed).
  1. Run the sonification file _osc-example.scd_ located in _data\assets\examples\sonification_ in SuperCollider.
      - To run the file in SuperCollider, find the line with the comment `// To run this example...` (should be around line 50), click on that line and press <kbd>CTRL</kbd> + <kbd>ENTER</kbd>.
      - Wait a while for the sonification to boot up.
      - The SuperCollider console should respond with: `-> OSCdef(Neptune, /Neptune, nil, nil, nil)` when it is finished booting.
  1. Run OpenSpace with any profile.
  1. Load the asset file _nodes-space-stations.asset_ either by dragging and dropping the file into OpenSpace, or by creating a new profile that loads that asset.
  1. Turn on the Telemetry module in the user interface under _Settings/Modules_.
  1. Turn on all telemetry types with the checkboxes in the telemetry module settings.
  1. Fly around in OpenSpace, and you should see messages being printed in the SuperCollider console window.

## Surround Sound Configurations
The surround sound aspect of the provided sonifications is designed for two specific configurations, as shown in the images below. In both images, black dots represent speakers, and the subwoofer is positioned outside the circle because it is not considered a directional sound source.

<!-- @TODO (malej) Generate a dark mode version of this image -->
:::{image} images/nkpg-dome.png
:alt: "Surround Sound Configuration Schematic for the Visualization Center Dome Theater in Norrköping, Sweden"
:width: 70%
:align: center
<!-- :class: only-light -->
:::

The image above shows a **top-down** view of the surround sound setup for the Visualization Center Dome Theater in Norrköping, Sweden. The audience sits in rows inside the circle, facing the front center of the dome surface, which is marked as _Center_ at the top of the image. The arrow in the image represents the viewing direction of the audience. The circle represents the edge of the dome surface. This configuration uses the [Horizontal](./angle-information.md#horizontal) angle calculation mode without the elevation angle, as it only has one ring of speakers.

<!-- @TODO (malej) Generate a dark mode version of this image -->
:::{image} images/amnh-dome.png
:alt: "Surround Sound Configuration Schematic for the Hayden Planetarium at the American Museum of Natural History in New York, USA"
:width: 70%
:align: center
<!-- :class: only-light -->
:::

The image above shows a **bottom-up** view of the surround sound setup for the Hayden Planetarium at the American Museum of Natural History in New York, USA. The audience sits in concentric rings inside the outermost circle, looking up toward the center of the dome surface, which is marked as _Center_ with a blue cross in the middle of the image. For a better understanding of the 3D structure, see the image below that shows the dome in 3D from a side view. In the image below, the arrow represents the viewing direction of the audience. The outermost ring represents the edge of the dome surface. This configuration uses the [Circular](./angle-information.md#circular) angle calculation mode with the elevation angle enabled, as it has multiple rings of speakers.

<!-- @TODO (malej) Generate a dark mode version of this image -->
:::{image} images/amnh-dome-3d.png
:alt: "Surround Sound Configuration Schematic in 3D from the side for the Hayden Planetarium at the American Museum of Natural History in New York, USA"
:width: 70%
:align: center
<!-- :class: only-light -->
:::

### Further Notes
Even though the sonifications have been designed with these specific surround configurations in mind, it is still possible to use them in other surround configurations. When choosing the appropriate [Angle Calculation Mode](./angle-information.md) for your surround sound configuration, consider two factors: whether there is a clear forward direction and the number of rings or rows of speakers. Use [Horizontal](./angle-information.md#horizontal) mode if there is a clear forward direction, and [Circular](./angle-information.md#circular) mode otherwise. If there is only one ring or row of speakers, then the elevation information can be omitted. Otherwise, the multiple rings or rows of speakers can be used to convey elevation information, and the elevation angle can be included in the angle calculations.
