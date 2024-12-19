---
authors:
  - name: OpenSpace Team
---

:::{toctree}
:maxdepth: 1
:hidden:

general
specialized
:::

# Telemetry Module
The telemetry module in OpenSpace can be used to send information from OpenSpace to a remote receiver using [Open Sound Control](https://ccrma.stanford.edu/groups/osc/index.html) (OSC). The IP address and port of the receiver, along with other settings of the module, can be set in the _openspace.cfg_ file located in the OpenSpace folder.

:::{note}
Note that the OSC receiver settings cannot be changed during the runtime of OpenSpace. However, other settings related to the module can be changed in the settings menu of the user interface under the telemetry module when OpenSpace is running.
:::

An example of how the settings for the telemetry module in the _openspace.cfg_ file can look:
:::{code-block} lua
:linenos:
:emphasize-lines: 4-9

...
ModuleConfigurations = {
    ...
    Telemetry = {
        IpAddress = "127.0.0.1",
        Port = 57120,
        AngleCalculationMode = "Horizontal",
        IncludeElevationAngle = false
    }
    ...
},
...

:::

The first two settings in the example above are the IP address and port for the receiver of the OSC telemetry messages. The next setting is the type of angle calculation that is used, and the last setting is whether an elevation angle should be added in the angle calculations. For more information about the angle modes and which is more suitable for your system, see [Angle Calculations Explanation](./general.md#angle-calculations-explanation). In the example above, the IP address used is localhost (the local computer) and the port used is the one that the software [SuperCollider](https://supercollider.github.io/) receives OSC messages from by default. More about SuperCollider and how it can be used for sonification can be found on the [Sonification](./specialized.md#sonification) page. Lastly, the angle calculation mode is Horizontal, and no elevation angle is added.

## Telemetry types
The telemetry module sends out messages with information about OpenSpace over the OSC connection. There are different types of messages that can be sent, each with different information. There are two categories of telemetry types: the [general](general) telemetry types and the [specialized](specialized) telemetry types. The general category of telemetry types monitors the general state of OpenSpace, such as the current time and focus. The specialized category of telemetry types is used for a specific purpose and monitors specific aspects of OpenSpace. For example, there are types that specifically monitor the planets in the solar system, and that information is then used for a sonification of the solar system.

Table of the available telemetry types and what type category they belong to:
| [General Telemetry Types](general) | [Specialized Telemetry Types](specialized) |
|------------------------------------|--------------------------------------------|
| [Angle Calculation Mode](./general.md#angle-calculation-mode) | [Planets Compare Sonification](./specialized.md#planets-compare-sonification) |
| [Camera Information](./general.md#camera-information) | [Planets Overview Sonification](./specialized.md#planets-overview-sonification) |
| [Focus](./general.md#focus) | [Planets Sonification](./specialized.md#planets-sonification) |
| [Customized Nodes Information](./general.md#customized-nodes-information) | |
| [Time Information](./general.md#time-information) | |

## OSC messages
Each telemetry message type sends OSC messages to the specified receiver IP address and port with the telemetry information it monitors. Each OSC message is labeled with a forward slash followed by a word (e.g., `/Camera`), similar to the subject of an email. The OSC receiving software (e.g., SuperCollider) can then listen to these messages and use the labels to sort out the information. The content of the OSC message is a list of information. The first item in the list is always the OSC label. The rest of the content, its order, and the number of items in the message are specific to each telemetry message type.

## Precision
For most telemetry types, there is at least one setting to adjust the precision of the telemetry. This can be adjusted in the settings menu of the user interface under the telemetry module and for each telemetry section. The precision value decides how sensitive the telemetry is, which in turn decides how often new messages are sent. In order for a new message to be sent, the information needs to have changed by at least the amount specified by the precision setting of that telemetry type. For some telemetry types, there can be several precision settings, either for different aspects that are monitored (for example, both angle and distance), or as a low and high precision value. The high precision value is used when the object that is monitored is also the object that is the current focus.

## How to use it
1. Turn on the Telemetry module in the user interface under _Settings/Modules_ when OpenSpace is running.
2. Turn on the telemetries/sonifications that are of interest with the checkboxes in the telemetry module settings.
3. Now, you can fly around in OpenSpace and freely try the different settings for the different telemetry types.

:::{danger}
Before you shut down OpenSpace after using the telemetry module, you will need to turn off the telemetry module in the settings menu. If OpenSpace is shut down while the telemetry module is still enabled, it will **crash**. This is an issue with the Scene not being safe for multiple threads, especially around startup and shutdown. For the same reason, the telemetry module cannot be enabled with scripts before OpenSpace has properly booted up completely.
:::