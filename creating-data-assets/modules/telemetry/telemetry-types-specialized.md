---
authors:
  - name: OpenSpace Team
---

# Specialized Telemetry Types
The specialized telemetry types in the [Telemetry Module](index.md) monitor specific aspects of OpenSpace and send that information to the OSC receiver. In contrast to the general telemetry types, these telemetry types are designed to be used for a particular purpose, such as adding a specific type of sonification to the planets in the solar system. See [sonification](./sonification.md#sonification) for more information on how the sonification works.

There are a few specialized telemetry types that monitor different aspects. Each is explained in more detail in the sections below.

The specialized telemetry types available in OpenSpace are:
  - [Planets Sonification](#planets-sonification)
  - [Planets Compare Sonification](#planets-compare-sonification)
  - [Planets Overview Sonification](#planets-overview-sonification)

## Planets Sonification
This telemetry type requires an asset file or script to specify which planets and moons are of interest to monitor. The file _planets.asset_ located in _data\assets\modules\telemetry\sonification_ adds all the planets in the solar system and their major moons to the list of planets to monitor with this telemetry type.

:::{important}
The _planets.asset_ file located in _data\assets\modules\telemetry\sonification_ should not be altered. The planet sonification in SuperCollider expects the file to remain unchanged. If any changes are made to the asset file, they must also be reflected in the SuperCollider sonification file. See [sonification](./sonification.md#sonification) for more information.
:::

In this telemetry type, angle information is provided for both planets and their moons (if present). The method for calculating these angles varies based on the [Angle Calculation Mode](./angle-information.md) in use. However, the method differs when calculating the angle for the planet versus its moons. For planets, the angle is calculated from the camera to the planet. For moons, the angle is calculated from the planet to the moon while taking the camera's orientation into account. For further details, see {ref}`Moon Angle <moon-angle-horizontal>` for both the {ref}`Horizontal <moon-angle-horizontal>` and {ref}`Circular <moon-angle-circular>` angle calculation modes.

:::{note}
When the Planets Overview Sonification is enabled, the angle calculated for the planet is modified in this telemetry type. Instead of calculating the angle from the camera to the planet, the angle is calculated similarly to that for the moons, from the Sun to the planet. More information can be found in [Further Notes](#further-notes).
:::

The OSC messages from this telemetry type are divided among the planets that have been added. These messages are sent under OSC labels such as `/Earth`, `/Mars`, etc. Each message contains at least four items, but there may be more depending on the number of major moons the planet has. Each item is explained in detail below:

  1. The distance from the camera to the planet in kilometers.
  1. The horizontal angle in radians to the planet, with the current angle calculation mode taken into account. For more information, see [Angle Calculations](./angle-information.md).
  1. The elevation angle in radians to the planet, with the current angle calculation mode taken into account. Again, see [Angle Calculations](./angle-information.md) for details.
  1. List of user interface settings for the planet sonification, which aspects of the sonification should be turned on or off. A value of 0 means that it is turned off, and a 1 means that it is turned on. The order of the settings can be seen in the table below. If the setting does not exist for a planet, the value is always 0.
  1. (optional) The distance from the camera to the **first** moon in kilometers.
  1. (optional) The horizontal angle in radians to the first moon.
  1. (optional) The elevation angle in radians to the first moon.
  1. (optional) The distance from the camera to the **second** moon in kilometers
  1. (optional) The horizontal angle in radians to the second moon.
  1. (optional) The elevation angle in radians to the second moon.
  1. (optional) ... The data then continues in the same pattern for as many moons as the planet has, with three values per moon. The moons are in the order of distance to the planet, the closest moon first and the farthest away moon last, which was specified in the _planets.asset_ file located in the _data\assets\modules\telemetry\sonification_ folder.

The table below lists the aspects of the planets that can be conveyed by the sonification. Each of the aspects can be turned on or off in the settings of the user interface.
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

A  message from this telemetry type can for example, look like this:
:::{code-block}
[ /Mercury, 132973827.75397, 3.0632956233535, 2.4592313674705, Int8Array[ 1, 1, 0, 0, 0, 0 ] ]
[ /Earth, 23378.137051742, -1.3549538910548, 0.0, Int8Array[ 1, 0, 0, 1, 0, 0 ], 393844.29544736, 1.1503961663306, 1.4013056448997 ]
:::

In the example above, there are two messages. The first message is for Mercury, and the second is for Earth. In this example the angle calculation mode [Circular](./angle-information.md#circular) was used with the {ref}`elevation angle <additional-elevation-angle-circular>` included. The example messages above can be broken down into the following parts:

::::{grid} 1 1 1 2
:::{grid-item}
  - `/Mercury`: The OSC label indicating that this is a message for planet Mercury.
  - `132973827.75397`: The distance from the camera to Mercury in kilometers.
  - `3.0632956233535`: The horizontal angle in radians to Mercury.
  - `2.4592313674705`: The elevation angle in radians to Mercury.
  - `Int8Array[ 1, 1, 0, 0, 0, 0 ]`: The list of user interface settings, where:
    - `1` Size/day is turned on.
    - `1` Gravity is turned on.
    - `0` Temperature is turned off.
    - `0` Atmosphere is turned off.
    - `0` Moons is turned off.
    - `0` Rings is turned off.
:::

:::{grid-item}
  - `/Earth`: The OSC label indicating that this is a message for planet Earth.
  - `23378.137051742`: The distance from the camera to Earth in kilometers.
  - `-1.3549538910548`: The horizontal angle in radians to Earth.
  - `0.0`: The elevation angle in radians to Earth.
  - `Int8Array[ 1, 0, 0, 1, 0, 0 ]`: The list of user interface settings, where:
    - `1` Size/day is turned on.
    - `0` Gravity is turned off.
    - `0` Temperature is turned off.
    - `1` Atmosphere is turned on.
    - `0` Moons is turned off.
    - `0` Rings is turned off.
  - `393844.29544736`: The distance from the camera to the **Moon** in kilometers.
  - `1.1503961663306`: The horizontal angle in radians to the Moon.
  - `1.4013056448997`: The elevation angle in radians to the Moon.
:::

::::

Another message from this telemetry type for a planet with many moons can for example, look like this:
:::{code-block}
[ /Uranus, 2802287304.3966, -0.51042779334867, 0.77991915326513, Int8Array[ 1, 0, 0, 0, 1, 0 ], 2802327335.3037, -2.296671696741, 1.0691106829325, 2802319474.7116, -0.39361430235799, 2.0952173560493, 2802407613.9156, -0.35519426892961, 2.1357200596744, 2802296365.598, 0.18863273887734, 2.195427733976, 2802217828.1715, 0.99476981366003, 2.0118520154497 ]
:::

The example message above can be broken down into the following parts:
  - `/Uranus`: The OSC label indicating that this is a message for planet Uranus.
  - `2802287304.3966`: The distance from the camera to Uranus in kilometers.
  - `-0.51042779334867`: The horizontal angle in radians to Uranus.
  - `0.77991915326513`: The elevation angle in radians to Uranus.
  - `Int8Array[ 1, 0, 0, 0, 1, 0 ]`: The list of user interface settings, where:
    - `1` Size/day is turned on.
    - `0` Gravity is turned off.
    - `0` Temperature is turned off.
    - `0` Atmosphere is turned off.
    - `1` Moons is turned on.
    - `0` Rings is turned off.
  - `2802327335.3037`: The distance from the camera to the first moon, **Ariel**, in kilometers.
  - `-2.296671696741`: The horizontal angle in radians to the first moon, Ariel.
  - `1.0691106829325`: The elevation angle in radians to the first moon, Ariel.
  - `2802319474.7116`: The distance from the camera to the second moon, **Miranda**, in kilometers.
  - `-0.39361430235799`: The horizontal angle in radians to the second moon, Miranda.
  - `2.0952173560493`: The elevation angle in radians to the second moon, Miranda.
  - `2802407613.9156`: The distance from the camera to the third moon, **Oberon**, in kilometers.
  - `-0.35519426892961`: The horizontal angle in radians to the third moon, Oberon.
  - `2.1357200596744`: The elevation angle in radians to the third moon, Oberon.
  - `2802296365.598`: The distance from the camera to the fourth moon, **Titania**, in kilometers.
  - `0.18863273887734`: The horizontal angle in radians to the fourth moon, Titania.
  - `2.195427733976`: The elevation angle in radians to the fourth moon, Titania.
  - `2802217828.1715`: The distance from the camera to the fifth moon, **Umbriel**, in kilometers.
  - `0.99476981366003`: The horizontal angle in radians to the fifth moon, Umbriel.
  - `2.0118520154497`: The elevation angle in radians to the fifth moon, Umbriel.

## Planets Compare Sonification
This telemetry type sends out information about the user interface settings regarding the Planets Compare sonification. The OSC messages from this telemetry type go under the OSC label `/Compare` and contain three items:

  1. The index of the first planet to be compared. See the first table below on how to convert the index to a planet name.
  1. The index of the second planet to be compared (will never be the same as the first).
  1. List of user interface settings for the comparison, which determines which aspects of the sonification should be turned on or off. A value of 0 means that a setting is turned off, and 1 means that it is turned on. The order of the settings can be seen in the second table below.

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

A  message from this telemetry type can for example, look like this:
:::{code-block}
[ /Compare, 3, 5, Int8Array[ 1, 1, 0, 0, 1, 0 ] ]
:::

The example message above can be broken down into the following parts:
  - `/Compare`: The OSC label indicating that this is a message from the **Planets Compare Sonification** telemetry type.
  - `3`: The index of the first planet (Earth).
  - `5`: The index of the second planet (Jupiter).
  - `Int8Array[ 1, 1, 0, 0, 1, 0 ]`: The list of user interface settings, where:
    - `1` Size/day is turned on.
    - `1` Gravity is turned on.
    - `0` Temperature is turned off.
    - `0` Atmosphere is turned off.
    - `1` Moons is turned on.
    - `0` Rings is turned off.

## Planets Overview Sonification
This telemetry type sends out information about the user interface settings regarding the Planets Overview sonification. The OSC messages from this telemetry type go under the OSC label `/Overview` and contain only one item:

  1. List of user interface settings for the planets overview. This determines which planets are part of the sonification or not. A value of 0 means that the planet is turned off, and a 1 means that it is turned on. The order of the settings can be seen in the table below.

:::{table}
:align: center
| Index in settings list | The planet that the setting turns on/off |
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

A  message from this telemetry type can for example, look like this:
:::{code-block}
[ /Overview, Int8Array[ 0, 0, 1, 0, 1, 1, 1, 1 ] ]
:::

The example message above can be broken down into the following parts:
  - `/Overview`: The OSC label indicating that this is a message from the **Planets Overview Sonification** telemetry type.
  - `Int8Array[ 0, 0, 1, 0, 1, 1, 1, 1 ]`: The list of user interface settings, where:
    - `0` Mercury is turned off.
    - `0` Venus is turned off.
    - `1` Earth is turned on.
    - `0` Mars is turned off.
    - `1` Jupiter is turned on.
    - `1` Saturn is turned on.
    - `1` Uranus is turned on.
    - `1` Neptune is turned on.

## Further Notes
Note that neither the [Planets Compare Sonification](#planets-compare-sonification) nor the [Planets Overview Sonification](#planets-overview-sonification) sends detailed information about the planets themselves. Instead, they only send a list of user interface settings and depend on the [Planets Sonification](#planets-sonification) to send the rest. These settings are used to modify the sonification in SuperCollider, altering how it sounds. However, the Planets Overview Sonification also changes the angle information for the planets sent by the Planets Sonification. Normally, the angle is calculated from the camera to the planet, but when the Planets Overview Sonification is active, the angle is calculated from the Sun to the planet, using the same method as described for the {ref}`Moon Angle <moon-angle-horizontal>`. Fortunately, users do not need to manually enable the Planets Sonification in OpenSpace while exploring the other sonifications, as OpenSpace will automatically send data from the Planets Sonification whenever any of the sonifications are enabled.

:::{note}
Only one sonification can be listened to at a time in SuperCollider. Users need to keep in mind to disable the currently active sonification before enabling another one to listen to.
:::
