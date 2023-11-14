# Profile Syntax
A `.profiles` file is a JSON file with a predefined set of sections that can be used. Extra keys are silently ignored.

These files are not intended to be edited by hand. The profile editor GUI that launches with OpenSpace should be used to create or edit a profile. The editor provides complete control over every aspect of the file. However, this document can be a useful reference guide for an advanced user who wants to edit a profile manually or via some kind of script automation.


## Sections
The supported sections are: `version`, `'modules`, `meta`, `assets`, `properties`, `keybindings`, `time`, `delta_times`, `camera`, `mark_nodes`, and `additional_scripts`. These sections have to be keys of the root JSON object. Each of the sections is described below. _italic_ values are JSON types, `monospaced` values are valid key names, **optional** denotes keys that do not have to be present.

### Version
Used to specify the version number of the profile's format.
Type: _object_
Children:
  - `major` (_number_): Describes the major version of the profile
  - `minor` (_number_): Describes the minor version of the profile

### Modules
This section is intended to be used only for a module that needs to be running to ensure functionality. Each value specifies an OpenSpace module whose load status will be checked. This can be used to perform an OpenSpace action if a module is loaded or is *not* loaded. These actions are optional; normally only one command would be used.
Type: _object_
Children:
  - `name` (_string_): The name of the module that is to be checked
  - `loadedInstruction` (_string_) **optional**: The Lua command that is executed when the module is present
  - `notLoadedInstruction` (_string_) **optional**: The Lua command that is executed when the module is not present

### Assets
Used to load assets. Each value specifies an OpenSpace asset that will be loaded
Type: _array of strings_

### Properties
This section sets specific property values at the time the profile is loaded. Each entry specifies a property and the value to set it.
Type: _object_
Children:
  - `type` (_string_): Denotes the Lua function that should be called to set the property. Must be either `setPropertyValue` or `setPropertyValueSingle`
  - `name` (_string_): The fully qualified identifier of the Property
  - `value` (_string_): The value that is to be set; this will be used as is for the Lua script, so if this is a string, it has to include escaped quote characters `\"`

### Keybindings
Used to set custom keybindings. Each value specifies the necessary elements in the required order. Note that the Lua command at the end may be a long list of commands (separated by `;` for example), and may contain one or more tab characters which will not be confused with the delimiters between the arguments.
Type: _object_
Children:
  - `key` (_string_): The key + modifier that the keybind should be bound to
  - `documentation` (_string_): A textual description of what the keybind should do
  - `name` (_string_): A human-readable name for the keybind
  - `gui_path` (_string_): The location in the GUI where the keybind should be stored
  - `is_local` (_boolean_): If `true` the results of the keybind action will not be transmitted to connected peers
  - `script` (_string_): The script to be executed

### Time
This specifies the time to be set at startup.
Type: _object_
Children:
 - `type` (_string_): Denotes the type of Time setting, must be either `absolute` or `relative`
 - `value` (_string_): The value of the time, if `type` is `absolute`, this is an ISO time string, for example `2018-10-30T23:00:00.500` otherwise a time relative to the time when the application starts, for example `-1d` for rewinding one day

### Camera
Used to set the camera position at startup. There are two types of camera position initializations: **setNavigationState** or **goToGeo**.
Type: _object_
Children:
  - `type` (_string_): Determines the type of the camera specification. Must be `setNavigationState` or `goToGeo`. The choice of type determines the remaining types

#### setNavigationState
  - `anchor` (_string_): The name of the scene graph node used as the anchor for the camera
  - `aim` (_string_) **optional** : The name of the scene graph node used as the aim for the camera
  - `frame` (_string_): The name of the reference frame in which the camera is specified
  - `position` (_object_): Provides the location of the camera, must have the keys `x`, `y`, and `z`, all _number_ s
  - `up` (_object_) **optional**: Sets the up vector of the camera. If it exists it must have the keys `x`, `y`, and `z`, all _number_ s
  - `yaw` (_number_) **optional**: Sets the yaw, which is an additional rotation around the view direction
  - `pitch` (_number_) **optional**: Sets the pitch of the camera, that is an additional rotation up or down

#### goToGeo
  - `anchor` (_string_): The name of the scene graph node used as the anchor for the camera. Must be a planetary body
  - `latitude` (_number_): The latitude of the camera location (in degrees)
  - `longitude` (_number_): The longitude of the camera location (in degrees)
  - `altitude` (_number_) **optional**: The height of the camera in meters

### Mark Nodes
Used to mark interesting nodes at startup.
Type: _array of strings_

### AdditionalScripts
Additional Lua scripts that should be executed when the profile is loaded. This should not be used to execute scripts that could be handled through one of the other sections.
Type: _array of strings_

### Meta
Meta information describing the profile; who made it, etc
Type: _object_
Children:
  - `name` (_string_) **optional**: A descriptive name of the profile
  - `version` (_string_) **optional**: A content-based version; not to be mixed up with the other `Version` parameter which describes the **format** of the profile file
  - `description` (_string_) **optional**: A description for the profile that tells the user what to expect
  - `author` (_string_) **optional**: The name of the author or authors of the profile
  - `url` (_string_) **optional**: A URL that describes where the data comes from, points to the personal homepage of the authors, etc
  - `license` (_string_) **optional**: The license under which this profile can be used

### Delta Times (a.k.a. 'Simulation Time Increments')
Array of time increments in units of simulation seconds per wall-clock seconds. These provide ways to speed up the simulation time.
By default, these map to the number keys 1 through 0, then SHIFT+ 1 through 0, and finally CTRL+ 1 through 0. However, they can also be re-mapped to other keys.
Type: _array of integers_


## Example
The following file is the NewHorizons .scene file converted to .profile format:
```json
{
  "version": { "major": 22, "minor": 21 },
  "meta": {
    "name": "name",
    "version": "version",
    "description": "description",
    "author": "author",
    "url": "url",
    "license": "license"
  },
  "modules": [
    { "name": "abc-module" },
    { "name": "def-module" },
    { "name": "ghi-module" }
  ],
  "assets": [
    "scene/solarsystem/planets/earth/earth",
    "scene/solarsystem/planets/earth/satellites/satellites",
    "folder1/folder2/asset",
    "folder3/folder4/asset2",
    "folder5/folder6/asset3"
  ],
  "properties": [
    {
      "type": "setPropertyValue",
      "name": "{earth_satellites}.Renderable.Enabled",
      "value": "false"
    },
    {
      "type": "setPropertyValue",
      "name": "property_name_1",
      "value": "property_value_1"
    },
    {
      "type": "setPropertyValue",
      "name": "property_name_2",
      "value": "property_value_2"
    },
    {
      "type": "setPropertyValue",
      "name": "property_name_3",
      "value": "property_value_3"
    },
    {
      "type": "setPropertyValueSingle",
      "name": "property_name_4",
      "value": "property_value_4"
    },
    {
      "type": "setPropertyValueSingle",
      "name": "property_name_5",
      "value": "property_value_5"
    },
    {
      "type": "setPropertyValueSingle",
      "name": "property_name_6",
      "value": "property_value_6"
    }
  ],
  "delta_times": [
    1.0,
    5.0,
    30.0,
    60.0,
    300.0,
    1800.0,
    3600.0,
    43200.0,
    86400.0,
    604800.0,
    1209600.0,
    2592000.0,
    5184000.0,
    7776000.0,
    15552000.0,
    31536000.0,
    63072000.0,
    157680000.0,
    315360000.0,
    630720000.0,
    1250000000.0
  ],
  "keybindings": [
    {
      "key": "T",
      "documentation": "T documentation",
      "name": "T name",
      "gui_path": "T Gui-Path",
      "is_local": true,
      "script": "T script"
    },
    {
      "key": "U",
      "documentation": "U documentation",
      "name": "U name",
      "gui_path": "U Gui-Path",
      "is_local": false,
      "script": "U script"
    },
    {
      "key": "CTRL+V",
      "documentation": "CTRL+V documentation",
      "name": "CTRL+V name",
      "gui_path": "CTRL+V Gui-Path",
      "is_local": false,
      "script": "CTRL+V script"
    }
  ],
  "time": {
    "type": "relative",
    "value": "-1d"
  },
  "camera": {
    "type": "goToGeo",
    "anchor": "Earth",
    "latitude": 58.5877,
    "longitude": 16.1924,
    "altitude": 2.0e+07
  },
  "mark_nodes": [
    "Earth", "Mars", "Moon", "Sun"
  ],
  "additional_scripts": [
    "script-1",
    "script-2",
    "script-3"
  ]
}
```
