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
| Index in settings list | Aspect of the sonification that the setting turns on/off |
|------------------------|-----------------------------------------------------------|
| 0                      | Size/day                                                  |
| 1                      | Gravity                                                   |
| 2                      | Temperature                                               |
| 3                      | Atmosphere                                                |
| 4                      | Moons                                                     |
| 5                      | Rings                                                     |
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

1. Download and install [SuperCollider](https://supercollider.github.io/)
2. Run the SuperCollider planets sonification file _OpenSpaceSonification.scd_ located in _data\assets\modules\telemetry\sonification_.
    - To run the file in SuperCollider, click on line 8 and press CTRL + ENTER
    - Wait a while for the sonification to boot up
    - The SuperCollider console should respond with: `probing C:\Program Files\VSTPlugins\StereoEncoder.dll... ok!` (or similar filepath) when it is finished
3. Run OpenSpace with the profile called _sonification_
4. Turn on the Telemetry module in the user interface under _Settings/Modules_
5. Turn on the telemetries/sonifications that are of interest with the checkboxes in the telemetry module settings
6. Fly around in OpenSpace, and you should see messages being printed in the SuperCollider console window
7. Now, you can freely try the different settings for the different telemetries/sonifications, read the tooltips, and stress-test it in general.

:::{danger}
Before you shut down OpenSpace after using the telemetry module, you will need to turn off the telemetry module in the settings menu. If OpenSpace is shut down while the telemetry module is still enabled, it will **crash**. This is an issue with the Scene not being safe for multiple threads, especially around startup and shutdown. Due to the same reason, the telemetry module cannot be enabled with scripts before OpenSpace has properly booted up completely.
:::

## The Sounds of the Planets Sonification
The table below describes shortly what aspects of the planets are conveyed by the sonification, how they sound, and how the sounds change depending on the data.
| Planet Property      | Sonification Sound        | Mapping Polarity                                            |
|----------------------|---------------------------| ------------------------------------------------------------|
| Mass                 | Pitch                     | Higher pitch = Lower mass                                   |
| Length of day        | Tempo of oscillation      | Faster tempo = Shorter day                                  |
| Length of Year       | Surround position         | Uses [angle calculations](./general.md#angle-calculations-explanation) to place the planet in a surround speaker setup |
| Gravity              | Bouncing ball sound       | Faster bouncing ball = Higher gravity                       |
| Temperature          | Sizzling intensity        | More sizzling = Higher temperature                          |
| Atmospheric pressure | Depth of wind sound       | Deeper wind sound = Higher atmospheric pressure             |
| Average wind speed   | Fluctuation of wind sound | More fluctuations in wind sound = Higher average wind speed |

For more details about the sonification of the planets see the paper **OpenSpace Sonification: Complementing Visualization of the Solar System with Sound** by Elias Elmquist, Malin Ejdbo, Alexander Bock, and Niklas Rönnberg, published in _International Community for Auditory Displays_, 2021 [doi:10.21785/icad2021.018](http://dx.doi.org/10.21785/icad2021.018).
