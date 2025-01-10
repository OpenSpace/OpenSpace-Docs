---
authors:
  - name: OpenSpace Team
---

# Specialized Telemetry Types
The specialized telemetry types in the Telemetry Module monitor specific aspects of OpenSpace and send that information over the OSC connection for a particular purpose. There are a few telemetry types that monitor certain aspects, and each of them is explained in more detail in the sections below.

All the specialized telemetry types that are available in OpenSpace:
- Planets Sonification
- Planets Compare Sonification
- Planets Overview Sonification

## Planets Sonification
The Planets Sonification telemetry type require an asset file to specify which planets and moons are of interest to monitor. The file _planets.asset_ located in _data\assets\modules\telemetry\sonification_ adds all the planets in the solarsystem and their major moons to the list of planets to monitor with this telemetry type. The OSC messages from this telemetry type are split up to each of the planets that has been added. Using the planets sonificaiton, the OSC messages would be sent under the OSC label `/Earth`, `/Mars`, etc. The messages contian at least four items but depending on how many major moons the planet has there can be more items, each are explained in detail below:

@TODO Add a link to the explanation that the angles for the moons are calculated in another manner and add figures for that too.

  1. The distance from the camera to the planet in kilometers.
  2. The horizontal angle in radians to the planet, with the current angle calculation mode taken into account.
  3. The elevation angle in radians to the planet, with the current angle calculation mode taken into account.
  4. List of user interface settings for the planet sonification, which aspectes of the sonification should be turned on or off. A value of 0 means that it is turned off and a 1 means that it is turned on. The order of the settings can be seen in the table below. If the setting does not exist for a planet, the value is always 0.
  5. The distance from the camera to the first moon in kilometers
  6. The horizontal angle in radians to the first moon, with the current angle calculation mode taken into account.
  7. The elevation angle in radians to the first moon, with the current angle calculation mode taken into account.
  8. The distance from the camera to the second moon in kilometers
  9. The horizontal angle in radians to the second moon, with the current angle calculation mode taken into account.
  10. The elevation angle in radians to the second moon, with the current angle calculation mode taken into account.
  11. Data continues in the same pattern for as many moons there are for the planet

:::{table}
:align: center
| Index in settings list | Aspect of the planets sonification that the setting turns on/off |
|------------------------|------------------------------------------------------------------|
| 0                      | Size/day                                                         |
| 1                      | Gravity                                                          |
| 2                      | Temperature                                                      |
| 3                      | Atmosphere                                                       |
| 4                      | Moons                                                            |
| 5                      | Rings                                                            |
:::

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Mercury, 132973827.75397, 3.0632956233535, 2.4592313674705, Int8Array[ 1, 1, 0, 0, 0, 0 ] ]
[ /Earth, 23378.137051742, -1.3549538910548, 0.0, Int8Array[ 1, 0, 0, 1, 0, 0 ], 393844.29544736, 1.1503961663306, 1.4013056448997 ]
[ /Uranus, 2802287304.3966, -0.51042779334867, 0.77991915326513, Int8Array[ 1, 0, 0, 0, 1, 0 ], 2802327335.3037, -2.296671696741, 1.0691106829325, 2802319474.7116, -0.39361430235799, 2.0952173560493, 2802407613.9156, -0.35519426892961, 2.1357200596744, 2802296365.598, 0.18863273887734, 2.195427733976, 2802217828.1715, 0.99476981366003, 2.0118520154497 ]
:::

In the example above, there are three messages. The first message is for Mercury, the second is for Earth, and the last third message is for Uranus. Here is a breakdown of the three example message above:

::::{grid} 1 1 2 3

:::{grid-item}
- `/Mercury`: The OSC label indicating that this is a message for planet Mercury.
- `132973827.75397`: The distance from the camera to Mercury in kilometers.
- `3.0632956233535`: The horizontal angle in radians to Mercury. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2.4592313674705`: The elevation angle in radians to Mercury. In this example the angle calculation mode Circular was used with the elevation angle included.
- `Int8Array[ 1, 1, 0, 0, 0, 0 ]`: The list of user interface settings, where:
    - `1` Size/day, is turned on.
    - `1` Gravity, is turned on.
    - `0` Temperature, is turned off.
    - `0` Atmosphere, is turned off.
    - `0` Moons, is turned off.
    - `0` Rings, is turned off.
:::

:::{grid-item}
- `/Earth`: The OSC label indicating that this is a message for planet Earth.
- `23378.137051742`: The distance from the camera to Earth in kilometers.
- `-1.3549538910548`: The horizontal angle in radians to Earth. In this example the angle calculation mode Circular was used with the elevation angle included.
- `0.0`: The elevation angle in radians to Earth. In this example the angle calculation mode Circular was used with the elevation angle included.
- `Int8Array[ 1, 0, 0, 1, 0, 0 ]`: The list of user interface settings, where:
    - `1` Size/day, is turned on.
    - `0` Gravity, is turned off.
    - `0` Temperature, is turned off.
    - `1` Atmosphere, is turned on.
    - `0` Moons, is turned off.
    - `0` Rings, is turned off.
- `393844.29544736`: The distance from the camera to the Moon in kilometers.
- `1.1503961663306`: The horizontal angle in radians to the Moon. In this example the angle calculation mode Circular was used with the elevation angle included.
- `1.4013056448997`: The elevation angle in radians to the Moon. In this example the angle calculation mode Circular was used with the elevation angle included.
:::

:::{grid-item}
- `/Uranus`: The OSC label indicating that this is a message for planet Uranus.
- `2802287304.3966`: The distance from the camera to Uranus in kilometers.
- `-0.51042779334867`: The horizontal angle in radians to Uranus. In this example the angle calculation mode Circular was used with the elevation angle included.
- `0.77991915326513`: The elevation angle in radians to Uranus. In this example the angle calculation mode Circular was used with the elevation angle included.
- `Int8Array[ 1, 0, 0, 0, 1, 0 ]`: The list of user interface settings, where:
    - `1` Size/day, is turned on.
    - `0` Gravity, is turned off.
    - `0` Temperature, is turned off.
    - `0` Atmosphere, is turned off.
    - `1` Moons, is turned on.
    - `0` Rings, is turned off.
- `2802327335.3037`: The distance from the camera to the first moon, Ariel, in kilometers.
- `-2.296671696741`: The horizontal angle in radians to the first moon, Ariel. In this example the angle calculation mode Circular was used with the elevation angle included.
- `1.0691106829325`: The elevation angle in radians to the first moon, Ariel. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2802319474.7116`: The distance from the camera to the second moon, Miranda, in kilometers.
- `-0.39361430235799`: The horizontal angle in radians to the second moon, Miranda. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2.0952173560493`: The elevation angle in radians to the second moon, Miranda. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2802407613.9156`: The distance from the camera to the third moon, Oberon, in kilometers.
- `-0.35519426892961`: The horizontal angle in radians to the third moon, Oberon. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2.1357200596744`: The elevation angle in radians to the third moon, Oberon. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2802296365.598`: The distance from the camera to the fourth moon, Titania, in kilometers.
- `0.18863273887734`: The horizontal angle in radians to the fourth moon, Titania. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2.195427733976`: The elevation angle in radians to the fourth moon, Titania. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2802217828.1715`: The distance from the camera to the fifth moon, Umbriel, in kilometers.
- `0.99476981366003`: The horizontal angle in radians to the fifth moon, Umbriel. In this example the angle calculation mode Circular was used with the elevation angle included.
- `2.0118520154497`: The elevation angle in radians to the fifth moon, Umbriel. In this example the angle calculation mode Circular was used with the elevation angle included.
:::

::::

## Planets Compare Sonification
This telemetry type sends out information about the user interface settings regarding the Planets Compare sonification. The OSC messages from this telemetry type goes under the OSC label `/Compare` and contains three items, explained in detail below:

  1. The index of the first planet to be compared, see the first table below on how to convert the index to a planet name.
  2. The index of the second planet to be compared, (will never be the same as the first).
  3. List of user interface settings for the comparison. This determines which aspects of the sonification should be turned on or off. A value of 0 means that it is turned off and a 1 means that it is turned on. The order of the settings can be seen in the second table below.

:::::{grid} 1 1 1 2

::::{grid-item}
:::{table}
:align: right
| Selected Planet Index | Selected Planet Name |
|-----------------------|----------------------|
| 0                     | None selected        |
| 1                     | Mercury              |
| 2                     | Venus                |
| 3                     | Earth                |
| 4                     | Mars                 |
| 5                     | Jupiter              |
| 6                     | Saturn               |
| 7                     | Uranus               |
| 8                     | Neptune              |
:::
::::

::::{grid-item}
:::{table}
:align: left
| Index in settings list | Aspect of the compare sonification that the setting turns on/off |
|------------------------|------------------------------------------------------------------|
| 0                      | Size/day                                                         |
| 1                      | Gravity                                                          |
| 2                      | Temperature                                                      |
| 3                      | Atmosphere                                                       |
| 4                      | Moons                                                            |
| 5                      | Rings                                                            |
:::
::::

:::::

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Compare, 3, 5, Int8Array[ 1, 1, 0, 0, 1, 0 ] ]
:::

Here is a breakdown of the example message above:
- `/Compare`: The OSC label indicating that this is a message from the **Planets Compare Sonification** telemetry type.
- `3`: The index of the first planet (Earth).
- `5`: The index of the second planet (Jupiter).
- `Int8Array[ 1, 1, 0, 0, 1, 0 ]`: The list of user interface settings, where:
    - `1` Size/day, is turned on.
    - `1` Gravity, is turned on.
    - `0` Temperature, is turned off.
    - `0` Atmosphere, is turned off.
    - `1` Moons, is turned on.
    - `0` Rings, is turned off.

## Planets Overview Sonification
This telemetry type sends out information about the user interface settings regarding the Planets Overview sonification. The OSC messages from this telemetry type go under the OSC label `/Overview` and contain only one item, explained in detail below:

  1. List of user interface settings for the planets overview. This determines which planets are part of the sonification or not. A value of 0 means that the planet is turned off and a 1 means that it is turned on. The order of the settings can be seen in the table below.

:::{table}
:align: center
| Index in settings list | The planet that the setting turnes on/off |
|------------------------|-------------------------------------------|
| 0                      | Mercury                                   |
| 1                      | Venus                                     |
| 2                      | Earth                                     |
| 3                      | Mars                                      |
| 4                      | Jupiter                                   |
| 5                      | Saturn                                    |
| 6                      | Uranus                                    |
| 7                      | Neptune                                   |
:::

Here is an example of how a message from this telemetry type can look:
:::{code-block}
[ /Overview, Int8Array[ 0, 0, 1, 0, 1, 1, 1, 1 ] ]
:::

Here is a breakdown of the example message above:
- `/Overview`: The OSC label indicating that this is a message from the **Planets Overview Sonification** telemetry type.
- `Int8Array[ 0, 0, 1, 0, 1, 1, 1, 1 ]`: The list of user interface settings, where:
    - `0` Mercury, is turned off.
    - `0` Venus, is turned off.
    - `1` Earth, is turned on.
    - `0` Mars, is turned off.
    - `1` Jupiter, is turned on.
    - `1` Saturn, is turned on.
    - `1` Uranus, is turned on.
    - `1` Neptune, is turned on.

# Sonification
There is a sonification of the planets in our solar system that can be used together with the telemetry module. Sonification is when information is conveyed using sound in contrast to visualization when images are used. The files for the sonification can be found in _data\assets\modules\telemetry\sonification_ in the OpenSpace folder. The file _planets.asset_ is a regular Lua script OpenSpace asset that configures the telemetry module to monitor each of the planets in the solar system and their major moons. The sonification file itelf _OpenSpaceSonification.scd_ is a SuperCollider file and needs to be run seperatly in that program. The sonification will then be produced by SuperCollider and just uses the informaiton that OpenSpace sends with the OSC messages provided by the telemetry module.

:::{note}
Note that the _planets.asset_ file cannot be customized or altered since the sonification expects the data from the telemetry module to be in a certain format determined by this file. If this file is altered, then the sonification file needs to be updated to reflect the change as well. If you want to create your own sonification for other objects in OpenSpace other than the planets, then the general [Customized Nodes Information](./general.md#customized-nodes-information) telemetry type is likely a better fit for that purpose.
:::

## SuperCollider
[SuperCollider](https://supercollider.github.io/) is the software used to produce the sounds of the sonification. The messages from the telemetry module is sent to SuperCollider and it then uses that information to create sounds that corresonds to that informaiton. In order to run the sonification follow the steps below:

@TODO Add instruction on how to add needed SuperCollider dependencies to run the sonification in an immersive surround environment

1. Download and install [SuperCollider](https://supercollider.github.io/)
2. Run the SuperCollider planets sonification file _OpenSpaceSonification.scd_ located in _data\assets\modules\telemetry\sonification_.
    - To run the file in SuperCollider, click on line 8 and press CTRL + ENTER
    - Wait a while for the sonification to boot up
    - The SuperCollider console should respond with: `Sonification is ready` when it is finished
3. Run OpenSpace with the profile called _sonification_
4. Turn on the Telemetry module in the user interface under _Settings/Modules_
5. Turn on the telemetries/sonifications that are of interest with the checkboxes in the telemetry module settings
6. Fly around in OpenSpace, and you should see messages being printed in the SuperCollider console window
7. Now, you can freely try the different settings for the different telemetries/sonifications, read the tooltips, and stress-test it in general.

:::{danger}
Before you shut down OpenSpace after using the telemetry module, you will need to turn off the telemetry module in the settings menu. If OpenSpace is shut down while the telemetry module is still enabled, it will **crash**. This is an issue with the Scene not being safe for multiple threads, especially around startup and shutdown. Due to the same reason, the telemetry module cannot be enabled with scripts before OpenSpace has properly booted up completely.
@TODO I am planning to (hopefully) fix the shutdown issue in th PR. However, the startup problem will remain.
:::

## The Sounds of the Planets Sonification
The table below describes shortly what aspects of the planets are conveyed by the sonification, how they sound, and how the sounds change depending on the data.
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

@TODO Generate a dark mode version of this image
:::{image} images/NKPG-Dome.png
:alt: "Surround Sound Configuration Schematic for the Visualization Center Dome Theater in Norrköping, Sweden"
:width: 100%
:align: center
:class: only-light
:::

This image shows a top-down view of the surround sound setup for the Visualization Center Dome Theater in Norrköping, Sweden. The audience sits in rows inside the circle, facing the front center of the dome surface, which is marked as _Center_ at the top of the image. The circle represents the edge of the dome surface. This configuration uses the [Horizontal](./angle-information.md#horizontal) angle calculation mode without the elevation angle, as it only has one ring of speakers.

@TODO Generate a dark mode version of this image
:::{image} images/AMNH-Dome.png
:alt: "Surround Sound Configuration Schematic for the Hayden Planetarium at the American Museum of Natural History in New York, USA"
:width: 100%
:align: center
:class: only-light
:::

This image shows a bottom-up view of the surround sound setup for the Hayden Planetarium at the American Museum of Natural History in New York, USA. The audience sits in concentric rings inside the outermost circle, looking up towards the center of the dome surface, which is marked as _Center_ with a blue cross in the middle of the image. The outermost ring represents the edge of the dome surface. This configuration uses the [Circular](./angle-information.md#circular) angle calculation mode with the elevation angle enabled, as it has multiple rings of speakers.
