# Console
This page covers the use of the OpenSpace in-game console, which allows precise control of the details in the scene. The console is an advanced tool, and a basic understanding of OpenSpace [properties](/manual/properties/index) and the [scene graph](/manual/scenegraph/index) is recommended before using it.


## Basic Use
The console is opened using the \` backtick character (the key to the left of {kbd}`1` on most keyboards). A **>** prompt will appear, where commands can be entered. Pressing \` again hides the console. Just as in a normal terminal window, a command is typed and executed using the {kbd}`Enter` key. If there is a problem with the command, an error message will appear at the bottom of the screen.

:::{figure} console.png
:align: center
:width: 100%
The _Console Window_ appearing after pressing the \` character with a script already entered.,
:::

On startup, OpenSpace auto-generates documentation files in HTML format inside the `documentation/` folder. The documentation of the commands that can be entered in the console can be found in the generated documentation, by selecting `Scripting API` in the menu to the left.

When entering a partial command, you can press the {kbd}`TAB` key, to autocomplete it. Subsequent presses of {kbd}`TAB` will cycle through the list of commands that start with the prefix you entered first. {kbd}`Shift+TAB` will cycle through this list backwards. For example entering `openspace.print`, followed by {kbd}`TAB` will cause `openspace.printDebug()` to be shown, another press of {kbd}`TAB` cycles to `openspace.printError()`, and {kbd}`Shift+TAB` will then go back to `openspace.printDebug()`.


## Command Expansion / Globbing with Properties
Two of the most important and most often used commands are `openspace.setPropertyValue` and `openspace.setPropertyValueSingle`, which allow you to set the value of any property to any value you like. For example executing
```lua
openspace.setPropertyValueSingle("Scene.Earth.Scale.Scale", 250.0)
```
will cause the Earth to be 250 times larger than normal, even though the user interface will only allow it to go to 100.

Each command for setting properties has at least 2 arguments:
  1. Identity of property or properties to be set
  1. Value that the property(s) will be assigned
  1. (optional) the number of seconds it should take to change to that value smoothly

Following the previous example,
```lua
openspace.setPropertyValueSingle("Scene.Earth.Scale.Scale", 4500.0, 5.0)
```
will cause the Earth to grow to a size of 4500 times its normal size, interpolated over a time of 5 seconds.

The two different methods exist mainly to distinguish how the property or properties are identified:
  - `setPropertyValueSingle` is used only if a specific property is to be identified exactly by name
  - `setPropertyValue` can use the `*` wildcard represent any character(s) in the property name which can be used to change multiple parameters at the same time

The `getPropertyValue` method works in the opposite way that `setPropertyValueSingle` works. The return value of the `getPropertyValue` call isn't visible unless it is routed to an output method. For example, the command: `openspace.getPropertyValue("Scene.EarthTrail.Renderable.Enabled")` will return a `true` or `false` representing whether the line behind the Earth is currently enabled or not, but that value isn't visible at the console. In order to see the return value, enclose the command inside the `openspace.printInfo` command, like so: `openspace.printInfo(openspace.getPropertyValue("Scene.EarthTrail.Renderable.Enabled"))`. Read this as: First get the value of the property `Scene.EarthTrail.Renderable.Enabled`, and then print it to the log. At the bottom of the screen, the `false` or `true` value will be visible in an Info message.

### Example
The following examples work with the default solar system scene:
```lua
openspace.setPropertyValueSingle("Scene.MarsTrail.Renderable.Enabled", false)
```
This command will disable the visibility of the Mars orbit trail. To re-enable it, use `true` as the 2nd argument: `openspace.setPropertyValueSingle("Scene.MarsTrail.Renderable.Enabled", true)`

```lua
openspace.setPropertyValue("Scene.*Trail.Renderable.Enabled", false)
```
will disable all planet trails by matching any property whose name ends with `Trail`.


## Tagging
Another way to control objects together is to use the tagging feature. Objects can be put into a group by tagging them with a common tag name. A Tag can be applied to an object in an `.asset` file, and there is no limit on the number of tags that can be applied to a single object. Tags can be added to a section in an `.asset` file using the syntax:

```lua
Tag = { "tag_name_1" }
```

or

```lua
Tag = { "tag_name_1", "tag_name_2" }
```

for multiple tags


One or more tags can be listed within the curly braces. Tags can also be added using the command `addTag(string, string)` where the tag name (2nd arg) is added to the scene graph node specified as the first argument.

### Examples
The Saturn asset `saturn.asset` has the following tag entry within its "SaturnTrail" entry:
```lua
Tag = { "planetTrail_solarSystem", "planetTrail_giants" },
```
since it belongs to a grouping that includes all planets in the solar system as well as the gas giant planets. Earth's trail is tagged with `planetTrail_terrestrial`, but not `planetTrail_giants`. To see how the tags can be used to differentiate planets, enter the following commands:
```lua
openspace.setPropertyValue("{planetTrail_solarSystem}.Renderable.Enabled", false)
openspace.setPropertyValue("{planetTrail_terrestrial}.Renderable.Enabled", false)
openspace.setPropertyValue("{planetTrail_giants}.Renderable.Enabled", false)
```
and using `true`/`false` arguments to enable/disable visibility.


## The Script Log
Each command that is run during a session shows up in the log document `logs/ScriptLog.txt`. This includes commands that are triggered through the user interface. The commands are logged from top to bottom, with the most recent call at the bottom of the file. For example, clicking the checkbox to disable the Earth globe in the UI results in the following line at the bottom of the script log:

```lua
openspace.setPropertyValueSingle("Scene.Earth.Renderable.Enabled", false)
```

Note that the script log file is cleared and overwritten on every startup.

The script log can be useful when trying to figure out how to achieve a certain visual effect with scripting, or find the identifier to access a certain property (for example `"Scene.Earth.Renderable.Enabled"` above). A common approach is to first get the visual appearance wanted using the settings in the UI, and then collect the commands to achieve that appearance from the `ScriptLog.txt` file and modify them to achieve the desired result.
