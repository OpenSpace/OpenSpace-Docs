---
authors:
  - name: OpenSpace Team
---

# The Telemetry Module
The telemetry module in OpenSpace can be used to send information from OpenSpace to a remote receiver using [Open Sound Control](https://ccrma.stanford.edu/groups/osc/index.html) (OSC). OSC is a realtime data transport messaging format used for communication between applications and even certain hardware. It is commonly used for music/sound-related applications, however, it can be used as a messaging protocol for a wide range of applications beyond that. The IP address and port of the receiver, along with other module settings, can be set in the _openspace.cfg_ file located in the OpenSpace folder.

:::{important}
Note that the OSC receiver settings cannot be changed while OpenSpace is running, those settings need to be set in the _openspace.cfg_ file before startup. However, other settings related to the module can be changed while OpenSpace is running in the settings menu of the user interface.
:::

This is an example of how the settings for the telemetry module in the _openspace.cfg_ file can look like:
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

The first two settings in the example above are the IP address and port for the receiver of the OSC telemetry messages. The next setting is the angle calculation mode that is used, and the last setting is whether an elevation angle should be added in the angle calculation. For more information about the angle calculation modes and which is more suitable for your system, see [Angle Calculations](./angle-information.md). In the example above, the IP address used is `"127.0.0.1"`, which is the local computer, and the port `57120` is used, which is the port where the software [SuperCollider](https://supercollider.github.io/) receives OSC messages from by default. For more information about SuperCollider and how it can be used for sonification, see [Sonification](./sonification.md#sonification). Lastly, the angle calculation mode is set as `"Horizontal"`, and no elevation angle is added.

## How To Use It
<!--@TODO (malej) Add a short text of how the telemetry module can be used. Including the sonification examples and possible other OSC reciving software. -->

To use the telemetry module in OpenSpace, follow these steps:

  1. Configure the telemetry settings, such as the receiver's IP address and port, in the _openspace.cfg_ file before starting OpenSpace. See an example of this above.
  1. Start OpenSpace and navigate to the settings menu in the user interface.
  1. Under _Settings/Modules_ locate and enable the telemetry module.
  1. Select the desired telemetry types to be used by checking the corresponding checkboxes. See the next section [Telemetry Types](#telemetry-types) for an overview of the different telemetry types.
  1. Now you can freely fly around in OpenSpace and the telemetry data will be sent to the specified OSC receiver in real-time.

:::{danger}
Due to an unsolved issue with the Scene not being safe for multiple threads, especially around startup, the telemetry module cannot be enabled before OpenSpace has completely initialized.
:::

## Telemetry Types
The telemetry module sends out messages with information about OpenSpace to the OSC receiver. The module supports multiple types of messages, each with different information. These message types are referred to as different telemetry types.

There are two categories of telemetry types: the [general](telemetry-types-general) telemetry types and the [specialized](telemetry-types-specialized) telemetry types. The general category of telemetry types monitors the general state of OpenSpace, such as the current time and focus. The specialized category of telemetry types is used for a specific purpose and monitors specific aspects of OpenSpace. For example, there are telemetry types that specifically monitor the planets in the solar system, and that information is then used for a [sonification](./sonification.md#sonification).

Below is a table of the available telemetry types and which category they belong to. More details about each type can be found on the linked pages.
:::{table}
:align: center
| **[General Telemetry Types](telemetry-types-general)** | **[Specialized Telemetry Types](telemetry-types-specialized)** |
|----------------------------------------|------------------------------------------------|
| [Camera Information](./telemetry-types-general.md#camera-information) | [Planets Sonification](./telemetry-types-specialized.md#planets-sonification) |
| [Focus](./telemetry-types-general.md#focus) | [Planets Compare Sonification](./telemetry-types-specialized.md#planets-compare-sonification) |
| [Time Information](./telemetry-types-general.md#time-information) | [Planets Overview Sonification](./telemetry-types-specialized.md#planets-overview-sonification) |
| [Customized Nodes Information](./telemetry-types-general.md#customized-nodes-information) | |
| [Angle Calculation Mode](./telemetry-types-general.md#angle-calculation-mode) | |
:::

## OSC Message Structure
Each telemetry type sends OSC messages containing specific telemetry information to the specified receiver IP address and port. Each OSC message is identified by a label starting with a forward slash (`/`) followed by a descriptive word (e.g., `/Camera`). OSC receiving software (e.g., SuperCollider) uses these labels to categorize the information. The message content is a list where the first item is always the OSC label, and the subsequent items vary depending on the telemetry type. For detailed information about the structure of each telemetry type's messages, refer to the links in the table above.

An OSC message can for example look like this:
:::{code-block}
[ /Time, 30.0, Minute, 787312539.37412 ]
:::

In the example above, the first item, `\Time` is the label and all subsequent items are part of the payload for that message. This message is from the [Time Information](./telemetry-types-general.md#time-information) telemetry type.

## Precision
For some telemetry types, it is possible to adjust one or more precision settings in the user interface. The precision setting determines how sensitive the telemetry is, which affects how frequently new messages are sent. A new message is only sent if the monitored information changes by at least the specified precision amount.

Some telemetry types have multiple precision settings for different monitored aspects, such as angles and distances, or for different levels of detail. The high precision value (high level of detail) is used when the monitored object is the current focus in OpenSpace, providing more accurate data. While the low precision value (low level of detail) is used for objects that are not the current focus, saving performance.

:::{toctree}
:maxdepth: 1
:hidden:

telemetry-types-general
telemetry-types-specialized
sonification
angle-information
:::
