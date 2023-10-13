# Commandline
This wiki covers the use of the OpenSpace console, which allows precise details of a scene to be accessed or controlled.  The console is an advanced tool, and a basic understanding of OpenSpace properties and namespaces is recommended before using it.

## Basic Use
The console is opened using the \` backtick character (below ~ on most keyboards). A **>** prompt will appear, where commands can be entered. Pressing \` again hides the console.  Just as in a normal terminal window, a command is typed and executed using the Enter key.  If there is a problem with the command, an error message will appear at the bottom of the screen.

On startup, OpenSpace auto-generates documentation files in HTML format in the `documentation/` folder.  Since these documentation files are "living documents" that are always up-to-date, they should always be consulted for specific details. A summary of the commands that can be entered in the console can be found in the generated documentation, by selecting `Scripting` in the menu to the left.

In contrast to these auto-generated reference documents, this wiki is intended to explain how to use these commands, what value they provide, and in what situations they are useful.

Some of the command specifics are covered in the sections below.

## Command Expansion / Globbing with Properties
OpenSpace's console supports command expansion, or globbing, which refers to a single command affecting multiple properties or representing multiple actions.  Just as multiple files can be specified using the `*` wildcard in an operating system console, multiple properties can be set with a command.

Each command for setting properties has 2 arguments:
1. Identity of property or properties to be set
2. Value that the property(s) will be assigned

Three different methods exist mainly to distinguish how the property or properties are identified:
* `setPropertyValueSingle` is used only if a specific property is to be identified exactly by name
* `setPropertyValue` can use the `*` wildcard represent any character(s) in the property name

Different properties require different types of values (e.g. string, integer, float).  In order for these methods to be flexible in this way, they do not enforce a type.  It is therefore up to the user to ensure that the type of property value supplied matches what is expected.
The `getPropertyValue` method works in the opposite way that `setPropertyValueSingle` works.  The "single" isn't part of the name, however, because there is no grouping ability with "get"--only the value of a single property can be obtained with each call.  The return value of the `getPropertyValue` call isn't visible unless it is routed to an output method.  For example, the command:
`openspace.getPropertyValue("Scene.EarthTrail.Renderable.Enabled")`
will return a 1 or 0 (for true or false), but that value isn't visible at the console.  In order to see the return value, enclose the command inside the `printInfo` command, like so:
`openspace.printInfo(openspace.getPropertyValue("Scene.EarthTrail.Renderable.Enabled"))`

At the bottom of the screen, the 0 or 1 value will be visible in an Info message.

### Examples
The following examples work with the default solar system scene.

`openspace.setPropertyValueSingle("Scene.MarsTrail.Renderable.Enabled", false)`

This command will disable the visibility of the Mars orbit trail.  To re-enable it, use `true` as the 2nd argument.

`openspace.setPropertyValue("Scene.*Trail.Renderable.Enabled", false)`

will disable all planet trails by matching any property with any characters before the `Trail` in its name.

## Tagging
Another way to control objects together is to use the tagging feature.  Objects can be put into a group by tagging them with a common tag name. A Tag can be applied to an object in a .mod file, and there is no limit on the number of tags that can be applied to a single object.  Tags can be added to a section in a .mod file using the syntax:

`Tag = { "tag_name_1" [, "tag_name_2",] }`

One or more tags can be listed within the curly braces.  Tags can also be added using the command `addTag(string, string)` where the tag name (2nd arg) is added to the scene graph node specified as the first argument.

### Examples
The Saturn module `saturn.mod` has the following tag entry within its "SaturnTrail" module:

`Tag = { "planetTrail_solarSystem", "planetTrail_giants" },`

since it belongs to a grouping that includes all planets in the solar system as well as the gas giant planets.  Earth's trail is tagged with `planetTrail_terrestrial`, but not `planetTrail_giants`.  To see how the tags can be used to differentiate planets, enter the following commands:
```
openspace.setPropertyValue("{planetTrail_solarSystem}.Renderable.Enabled", false)
openspace.setPropertyValue("{planetTrail_terrestrial}.Renderable.Enabled", false)
openspace.setPropertyValue("{planetTrail_giants}.Renderable.Enabled", false)
```
and using true/false arguments to enable/disable visibility.

## The Script Log
Each command/script that is run in the software during a session shows up in the log document `logs/ScriptLog.txt`. This includes commands that are triggered through button clicks in the UI. The commands are logged from top to bottom, with the most recent call at the bottom of the file. For example, clicking the checkbox to disable the Earth globe in the UI results in the following line at the bottom of the script log:

```
openspace.setPropertyValueSingle("Scene.Earth.Renderable.Enabled", false)
```

Note that the script log file is cleared and overwritten on every startup.

The script log can be useful when trying to figure out how to achieve a certain visual effect with scripting, or find the identifier to access a certain property (e.g. `"Scene.Earth.Renderable.Enabled"` above). A common approach is to first get the visual appearance wanted using the settings in the UI, and then collect the commands to achieve that appearance from the ScriptLog.txt file.
