# Creating Camera Paths Using Scripting

The Scripting API includes functions for creating camera paths to specific positions and for providing more detailed fly-to behavior. This page gives an overview of the available functions and some tips on how to use them.

For the most up-to-date information on available functions and how they work, see the `openspace.navigation` and `openspace.pathnavigation` parts of the [Scripting API Reference](/reference/scripting-api/index).

:::{note}
Before reading this page, you should first have a look at the [Settings](camera-paths.md#settings) part of the [Camera Paths](camera-paths) page, which explains the different available path types and settings.
:::

## Fly to a Target
To fly to a target using the scripting API, you can use the `openspace.navigation.flyTo` function. This function takes a single parameter, which is the name of the target node in the scene graph. The target node must have a valid bounding sphere for the fly-to to work correctly.

```lua
openspace.navigation.flyTo("Earth")
```

It is also possible to specify how long the fly-to should take, and whether the up-direction of the target node should be accounted for when determining the camera orientation at the end of the path.
```lua
-- Fly to a target node with a specified duration (5 seconds)
openspace.navigation.flyTo("Earth", 5.0)

-- Fly to a target node using the up-direction of the target node computing the
-- target orientation at the end of the path
openspace.navigation.flyTo("Earth", true)

-- Fly to a target node using the up-direction of the target node, with a
-- specified duration (5 seconds)
openspace.navigation.flyTo("Earth", 5.0, true)
```

:::{admonition} Enable roll for correct up-direction
For the up-direction to be correct when using the up-direction of the target, the {menuselection}`Navigation handler -> Path Navigator -> Include roll` setting must be enabled. Otherwise, the camera will not have the correct orientation when reaching the target state.
:::

## Flying to a Specific Position or Height

There are a few available functions for flying to a specific position or height in relation to a scene graph node:

| Function | Description |
| -------- | ----------- |
| [`openspace.navigation.flyToHeight`](#navigationflytoheight-target) | Fly to a specific height above a scene graph node. |
| [`openspace.navigation.flyToGeo`](#navigationflytogeo-target) | Fly to a latitude/longitude/altitude target relative to a scene graph node. The node is often a globe (for example Earth), but it can also be any other node. |
| [`openspace.navigation.flyToNavigationState`](#navigationflytonavigationstate-target) | Fly to a specific [NavigationState](#core_navigationstate). Note that the timestamp will not be used in the fly-to operation, and you need to make sure that the simulation time is set correctly for the behavior you expect. |

For all of these, it is also possible to some specify additional parameters such as the duration of the path and the up-direction of the target node. Below are some examples

```lua
-- Fly to a specific height above a scene graph node
openspace.navigation.flyToHeight("Earth", 100000)

-- Fly to a specific height above a scene graph node using the up-direction of
-- the reference node and parameters
openspace.navigation.flyToHeight("Earth", 100000, true)

-- Fly to a specific height above a scene graph node with a specified duration
-- (5 seconds)
openspace.navigation.flyToHeight("Earth", 100000, 5.0)
```

```lua
-- Fly to a latitude, longitude, altitude position relative to Earth
openspace.navigation.flyToGeo("Earth", 45.0, -120.0, 10000)

-- Fly to a latitude, longitude, altitude position relative to Earth, using the
-- up-direction of the reference node and a specified duration (5 seconds)
openspace.navigation.flyToGeo("Earth", 45.0, -120.0, 10000, true, 5.0)
```

```lua
-- Fly to a specific navigation state. Note that the timestamp will not be used
-- in the fly-to, but is included here for context as it will be saved in the
-- navigation state.
openspace.navigation.flyToNavigationState({
    Up = { -0.3381334006389302, 0.8719917989296857, 0.35397189997473527 },
    Position = { -1205410.4887627328,  941781.8267593941, -3471506.006929062 },
    Anchor = "Mars",
    Timestamp = "2026 SEP 01 14:57:06"
})
```

:::{admonition} Enable roll for correct up-direction
For the up-direction to be correct when using the up-direction of the target or a navigation state, the {menuselection}`Navigation handler -> Path Navigator -> Include roll` setting must be enabled. Otherwise, the camera will not have the correct orientation when reaching the target state.
:::

## Instant Flight (Jump)
There are also "jump-to" versions for some of the navigation functions. These move the camera instantly, using a fading transition, rather than a continuous motion. Examples are [`openspace.navigation.jumpTo`](#navigationjumpto-target), [`openspace.navigation.jumpToGeo`](#navigationjumptogeo-target), and [`openspace.navigation.jumpToNavigationState`](#navigationjumptonavigationstate-target).

## More Customized Camera Paths

The most flexible way to create a camera path is to use the [`openspace.pathnavigation.createPath`](#pathnavigationcreatepath-target) function, which lets you create some paths that the other functions cannot be used for. For context, the other functions are convenience wrappers around `createPath` that use default parameter values. Note that the `createPath` function is located in the `openspace.pathnavigation` sublibrary, while the other functions are located in the `openspace.navigation` sublibrary.

In a single call, you can define the target position (with varying level of detail), the desired [path type](./camera-paths.md#about-path-types), and the duration. You can also provide an optional start position and orientation using a [NavigationState](#core_navigationstate), which can be used to create a path from a specific point in space instead of the current camera position.

The `createPath` function takes a table of parameters that can be used to customize the path, called a [PathInstruction](#core_path_instruction). This lets you create two different types of paths: a path to a position in relation to a scene graph node, or a path to a specific navigation state. For the node option, the target position can be specified in different ways, depending on the level of detail you want to provide. See the [PathInstruction](#core_path_instruction) documentation for more details.

### Node Target

Below are some examples of paths to positions in relation to a scene graph node:

```lua
-- Create a path to the Earth node, with a duration of 5 seconds
openspace.pathnavigation.createPath({
    TargetType = "Node",
    Target = "Earth",
    Duration = 5.0
})

-- Create a path to a position 1,000,000 meters above the Earth node, with North
-- as the up-direction
openspace.pathnavigation.createPath({
    TargetType = "Node",
    Target = "Earth",
    Height = 1000000,
    UseTargetUpDirection = true
})

-- Create a path from a given start position, to Earth, using a zoom-out effect, over 5 seconds
openspace.pathnavigation.createPath({
    TargetType = "Node",
    Target = "Earth",
    StartState = { ... }, -- The navigation state to start from
    PathType = "ZoomOutOverview",
    Duration = 5.0
})
```

### Navigation State Target

When it comes to creating a path to a specific navigation state, most of the functionality is available through `openspace.navigation.flyToNavigationState` function.  However, the `createPath` function can for example be used to include a specific start position and orientation, which is not possible with `flyToNavigationState`. An example of this is shown below:

```lua
openspace.pathnavigation.createPath({
    TargetType = "NavigationState",
    NavigationState = { ... }, -- The navigation state to fly to
    StartState = { ... }, -- The navigation state to start from
    Duration = 5.0 -- Other options, such as duration, can also be specified
})
```

## Utility Functions
The scripting API also includes some utility functions for working with camera paths when scripting. These can be used to check if a path is currently playing, to cancel a path, or to get the current path progress.

The most commonly used function lives in the [`openspace.navigation`](/reference/scripting-api/openspace.navigation) sublibrary, and is called [`openspace.navigation.isFlying()`](#navigationisflying-target). It can be used to check if a path is currently playing.

A number of other functions can be found in the [`openspace.pathnavigation`](/reference/scripting-api/openspace.pathnavigation) sublibrary, including functions for aborting a path or pausing it during playback, for example.

## The Camera Paths are Under Development

The camera path system is still under development, and the available functions and their behavior may change in future releases. If you are interested in the camera path system and plans for its development, feel free to check the [currently open issues related to camera paths](https://github.com/OpenSpace/OpenSpace/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Feature%3A%20Camera%20Paths%22) on GitHub.

:::{important}
The generated camera paths are considered experimental and may not work as expected in all situations. They have primarily been calibrated to create nice flights between different scene graph nodes, and may not work as well for more complex camera scenarios such as navigation states, for example.

If you are relying on camera paths for a specific use case, we recommend testing them thoroughly to ensure that they work as expected. In sensitive situations, it may be better to use the session recording system to create a recorded path that is guaranteed to work as expected.

If you encounter any issues, or have ideas for improvement, please report them on Github or contact the OpenSpace team.
:::
