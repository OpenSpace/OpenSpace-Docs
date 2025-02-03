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

The first two settings in the example above are the IP address and port for the receiver of the OSC telemetry messages. The next setting is the angle calculation mode that is used, and the last setting is whether an elevation angle should be added in the angle calculation. For more information about the angle calculation modes and which is more suitable for your system, see [Angle Calculations Explanation](./angle-information.md#angle-calculations-explanation). In the example above, the IP address used is `"127.0.0.1"`, which is the local computer, and the port `57120` is used, which is the port where the software [SuperCollider](https://supercollider.github.io/) receives OSC messages from by default. For more information about SuperCollider and how it can be used for sonification, see [Sonification](./specialized.md#sonification). Lastly, the angle calculation mode is set as `"Horizontal"`, and no elevation angle is added.

## How To Use It
@TODO Add a short text of how the telemetry module can be used. Including the sonification examples and possible other OSC reciving software.

To use the telemetry module in OpenSpace, follow these steps:

1. Configure the telemetry settings, such as the receiver's IP address and port, in the _openspace.cfg_ file before starting OpenSpace. See an example of this above.
2. Start OpenSpace and navigate to the settings menu in the user interface.
3. Under _Settings/Modules_ locate and enable the telemetry module.
5. Select the desired telemetry types to be used by checking the corresponding checkboxes.
6. Now you can freely fly around in OpenSpace and the telemetry data will be sent to the specified receiver in real-time.

:::{danger}
After using the telemetry module, you need to turn off the telemetry module in the settings menu _before shutting down OpenSpace_. If OpenSpace is shut down while the telemetry module is still enabled, it will **crash**. This is an unsolved issue with the Scene not being safe for multiple threads, especially around startup and shutdown. For the same reason, the telemetry module cannot be enabled with scripts before OpenSpace has initialized completely.
<!-- @TODO (malej) I am planning to (hopefully) fix the shutdown issue in th PR. However, the startup problem will remain. -->
:::

## Telemetry Types
The telemetry module sends out messages with information about OpenSpace over the OSC connection. The module supports multiple types of messages, each with different information. These message types are referred to as different telemetry types. 

There are two categories of telemetry types: the [general](general) telemetry types and the [specialized](specialized) telemetry types. The general category of telemetry types monitors the general state of OpenSpace, such as the current time and focus. The specialized category of telemetry types is used for a specific purpose and monitors specific aspects of OpenSpace. For example, there are telemetry types that specifically monitor the planets in the solar system, and that information is then used for a [sonification](./specialized.md#sonification) of the planets in the solar system.

Below is a table of the available telemetry types and which category they belong to. More details about each type can be found on the linked pages. 
:::{table}
:align: center
| **[General Telemetry Types](general)** | **[Specialized Telemetry Types](specialized)** |
|----------------------------------------|------------------------------------------------|
| [Camera Information](./general.md#camera-information) | [Planets Sonification](./specialized.md#planets-sonification) |
| [Focus](./general.md#focus) | [Planets Compare Sonification](./specialized.md#planets-compare-sonification) |
| [Time Information](./general.md#time-information) | [Planets Overview Sonification](./specialized.md#planets-overview-sonification) |
| [Customized Nodes Information](./general.md#customized-nodes-information) | |
| [Angle Calculation Mode](./general.md#angle-calculation-mode) | |
:::

## OSC Message Structure
Each telemetry type sends OSC messages containing specific telemetry information to the specified receiver IP address and port. Each OSC message is identified by a label starting with a forward slash (`/`) followed by a descriptive word (e.g., `/Camera`). OSC receiving software (e.g., SuperCollider) uses these labels to categorize the information. The message content is a list where the first item is always the OSC label, and the subsequent items vary depending on the telemetry type. For detailed information about the structure of each telemetry type's messages, refer to the links in the table above.

## Precision
For some telemetry types, it is possible to adjust one or more precision settings in the user interface. The precision setting determines how sensitive the telemetry is, which affects how frequently new messages are sent. A new message is only sent if the monitored information changes by at least the specified precision amount.

Some telemetry types have multiple precision settings for different monitored aspects, such as angles and distances, or for different levels of detail. The high precision value (high level of detail) is used when the monitored object is the current focus in OpenSpace, providing more accurate data. While the low precision value (low level of detail) is used for objects that are not the current focus, saving performance.

:::{toctree}
:maxdepth: 1
:hidden:

general
specialized
angle-information
:::
