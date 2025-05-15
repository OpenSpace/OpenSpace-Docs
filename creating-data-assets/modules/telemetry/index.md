---
authors:
  - name: OpenSpace Team
---

# The Telemetry Module
The telemetry module in OpenSpace can be used to send information from OpenSpace to a remote receiver using the [Open Sound Control](https://ccrma.stanford.edu/groups/osc/index.html) (OSC) protocol. OSC is a real-time data transport messaging format used for communication between applications and even certain hardware. It is commonly used for music/sound-related applications, but can be used as a messaging protocol for a wide range of applications beyond that.

To use the telemetry module, some settings have to be specified in the _openspace.cfg_ file located in the OpenSpace folder. Below is an example of how these settings can look like:

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

The first two settings in the example above are the IP address and port for the receiver of the OSC telemetry messages. The next setting is the angle calculation mode that is used, and the last setting is whether an elevation angle should be added in the angle calculation. For more information about the angle calculation modes and which is more suitable for your system, see [Angle Calculations](./angle-information.md). In the example above, the IP address used is `"127.0.0.1"`, which is the local computer, and the port `57120` is used, which is the port where the software [SuperCollider](https://supercollider.github.io/) receives OSC messages from by default. For more information about SuperCollider and how it can be used for sonification, see [Sonification](./sonification.md#sonification). Lastly, the angle calculation mode is set as `"Horizontal"`, and no elevation angle is added.  See [Angle Calculations](./angle-information.md) for more information about the calculation modes.

:::{important}
Note that the OSC receiver settings (IP address and port) cannot be changed while OpenSpace is running; those settings must be set in the _openspace.cfg_ file before startup. However, other settings related to the module can be changed while OpenSpace is running in the settings menu of the user interface.
:::

## How To Use It
The telemetry module allows users to extract certain information from OpenSpace in real-time and send it to any software or hardware capable of receiving OSC messages for further use. What this information is used for depends entirely on the receiving application. For instance, OpenSpace provides examples where this data has been utilized for sonification, enabling users to "listen" to certain features within OpenSpace. For more details, see [Sonification](./sonification.md#sonification). Beyond sonification, there are numerous other possibilities for using this data.

To use the telemetry module in OpenSpace, follow these steps:
  1. Configure the telemetry settings, such as the receiver's IP address and port, in the _openspace.cfg_ file before starting OpenSpace. See an example of this above.
  1. Start OpenSpace and navigate to the settings menu in the user interface.
  1. Under _Settings/Modules_ locate and enable the telemetry module.
  1. Select the desired telemetry types to use by checking the corresponding checkboxes. See the next section [Telemetry Types](#telemetry-types) for an overview of the different telemetry types.
  1. Now you can freely fly around in OpenSpace, and the telemetry data will be sent to the specified OSC receiver in real-time.
  1. For further instructions on how to use the telemetry module together with any of the sonifications that OpenSpace provides, see [Sonification](./sonification.md#sonification).

:::{danger}
Due to an unresolved issue with the scene not being safe for multiple threads, especially during startup, the telemetry module cannot be enabled before OpenSpace has fully initialized. This means that it must be manually enabled each time OpenSpace is started. This is done through the checkbox for the module in the settings menu of the user interface.
:::

## Telemetry Types
The telemetry module sends out messages with information about OpenSpace to the OSC receiver. The module supports multiple types of messages, each with different information. These message types are referred to as different telemetry types.

There are two categories of telemetry types: the [general](telemetry-types-general) telemetry types and the [specialized](telemetry-types-specialized) telemetry types. The general category of telemetry types monitors the general state of OpenSpace, such as the current time and focused object. The specialized category of telemetry types is used for a specific purpose and monitors specific aspects of OpenSpace. For example, there are specific telemetry types that monitor the planets in the solar system, to be used for [sonification](./sonification.md#sonification).

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

An OSC message can for example, look like this:
:::{code-block}
[ /Time, 30.0, Minute, 787312539.37412 ]
:::

In the example above, the first item, `/Time` is the label and all subsequent items are part of the payload for that message. This message is from the [Time Information](./telemetry-types-general.md#time-information) telemetry type.

## Precision
For some telemetry types, it is possible to adjust one or more precision settings in the user interface. The precision setting determines how sensitive the telemetry is, which affects how frequently new messages are sent. A new message is only sent if the monitored information changes by at least the specified amount.

Some telemetry types have multiple precision settings for different monitored aspects, such as angles and distances, or for different levels of detail. The high precision value (high level of detail) is used when the monitored object is the current focus in OpenSpace, providing more accurate data. While the low precision value (low level of detail) is used for objects that are not the current focus, saving performance.

:::{toctree}
:maxdepth: 1
:hidden:

telemetry-types-general
telemetry-types-specialized
sonification
angle-information
:::
