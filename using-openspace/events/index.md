# Events
Events are signals that are emitted by the OpenSpace engine in response to specific _events_ that happen. The event system is build to be as low overhead as possible to provide a minimal impact on the overall rendering performance, however events should be considered to be relatively seldom activities. Events are signalled to connected instances via the socket connection as a seperate `Topic` or they can trigger `Action`s in the main system.


## Action Trigger
Using the `openspace.event.registerEventAction` and `openspace.event.unregisterEventAction` functions, an event can be set to trigger a specific action. The syntax of both functions as as follows:
```lua
openspace.event.registerEventAction(<<name of the event>>, <<identifier of the action>>, <<optional filter table>>)
```
The name of the event must be one of the event types that exist in the system (see a list below), the second parameter is the identifier of the action that is triggered whenever the specific event is encountered. Depending on the specific event, the Lua state in which this action is executed will contain an `args` table that contains additional information about the event. Each event type's arguments are described below. The last, optional, parameter is a table that is used to filter the events. The filter table has to be a matching subset of the arguments passed into the action in order to pass the filter. For example, if an event provides arguments `local args = { Foo = "abc", Bar = 1.0 }` to the action, a filter `{ Foo = "abc" }` will cause this event to pass through to the action as the existing value matches and since no value is provided for `Bar`, that value is ignored for the purpose of filtering. However a filter `{ Foo = "abc", Bar = 2.0 }` will not allow this event is passing as only one of the provided values `Foo` matches the filter, but `Bar` does not, so the action would not be triggered in this second case.


## Event Types
What follows is a complete list of all available event types that can be created within OpenSpace. The name of the event used for the `registerEventAction` and `unregisterEventAction` is the section heading.

### SceneGraphNodeAdded
This event is created whenever a new scene graph node is added to the system. By the time this event is signalled, the scene graph node has already been created and added to the scene.

`Node`: The identifier of the node that was added

### SceneGraphNodeRemoved
This event is created whenever a scene graph node was removed. By the time this event is signalled, the scene graph node has already been removed.

`Node`: The identifier of that node that was removed

### ParallelConnection
This event is created whenever something in the parallel connection subsystem changes. The new state is sent as an argument with this event.

`State`: The new state of the parallel connection system; is one of `Established`, `Lost`, `HostshipGained`, or `HostshipLost`

### ProfileLoadingFinished
This event is created when the loading of a profile is finished. This is emitted regardless of whether it is the initial profile, or any subsequent profile is loaded.

### ApplicationShutdown
This event is created whenever some information about the application shutdown sequence changes. This can either be that the seqeuence started, was aborted, or is finished, which means that OpenSpace is just about the shutdown.

`State`: The next state of the application shutdown sequence; is one of `Started`, `Aborted`,  or `Finished`

### ScreenSpaceRenderableAdded
This event is created when a new screenspace renderable has been created. By the time this event is craeted, the screenspace renderable is already registered and available.

`Renderable`: The identifier of the new screenspace renderable that was just added to the system

### ScreenSpaceRenderableRemoved
This event is created when a screenspace renderable has been removed from the system. When this event is created, the screenspace renderable has already been removed and is no longer available

`Renderable`: The identifier of the screenspace renderable that was removed

### CameraFocusTransition
This event is created when the camera transitions between different interaction sphere distances. Right now, only movement relative to camera's focus node is considered. Each scene graph node has an interaction sphere radius that serves as the reference distance for all spheres.
```
Diagram of events for a camera moving from right-to-left. Interaction sphere is 'O' in middle, and ')' are spherical boundaries. The approach factor, reach factor, and interaction sphere radius are all taken from the current focus node.

|<------------------->|  Approach factor * Interaction sphere
             |<------>|  Reach Factor * Interaction sphere

(                       (           O          )                       )
^                       ^                      ^                       ^
Exiting                 Receding               Reaching                Approaching
```

`Node`: The name of the node the camera is transitioning relative to. Currently is always the same as the camera's focus node

`Transition`: The name of the area the camera was in before the transition; is one of `Outside`, `ApproachSphere`, or `ReachedSphere`

`After`: The transition type that the camera just finished; is one of `Approaching`, `Reaching`, `Receding`, or `Exiting`

### TimeOfInterestReached
This event is created with a specific time of interest is reached. This event is currently unused.

### MissionEventReached
This event is created when the end of a mission phase is reached. This event is currently unused.

### PlanetEclipsed
This event is created when a planet is eclipsed by a moon or a different planet. This event is currently unused.

`Eclipsee`: The identifier of the scene graph node that is eclipsed by another object

`Eclipser`: The identifier of the scene graph node that is eclipsing the other object

### InterpolationFinished
This event is created when the interpolation of a property value is finished. If the interpolation time of a property change is 0s, this event is not fired

`Property`: The URI of the property whose interpolation has finished

### FocusNodeChanged
This event is created when the camera changes focus nodes. Even if the camera position is interpolated, the node change happens instantaneously and the event is fired at the same time.

`OldNode`: The identifier of the scene graph node which was the old focus node

`NewNode`: The identifier of the scene graph node that is the new focus node

### LayerAdded
This event is created when a layer is added to to a globe.

`Globe`: The identifier of the globe to which the layer is added

`Group`: The identifier of the layer group to which the layer is added

`Layer`: The identifier of the layer that was added

### LayerRemoved
This event is created when a layer is removed from a globe.

`Globe`: The identifier of the globe from which the layer is removed

`Group`: The identifier of the layer group from which the layer is removed

`Layer`: The identifier of the layer that was removed

### SessionRecordingPlayback
This event is created when something regarding a session recording playback changes. The event contains information about the new state of the session recording subsystem.

`State`: The new state of the session recording; one of `Started`, `Paused`, `Resumed`, `Finished`

### PointSpacecraft
This event is created if a spacecraft is asked to point at a specific direction.

`Ra`: The right ascension of the point at which the spacecraft will be pointed

`Dec`: The declination of the point at which the spacecraft will be pointed

`Duration`: The duration in seconds that the spacecraft will take to point at the specific position

### RenderableEnabled
This event is created when a scene graph node with an attached renderable is enabled for any reason.

`Node`: The name of the scene graph node that was enabled

### RenderableDisabled
This event is created when a scene graph node with an attached renderable is disabled for any reason.

`Node`: The name of the scene graph node that was disabled

### CameraPathStarted
This event is created when an automated camera path is triggered that will move the camera from the specified Origin to the Destination.

`Origin`: The name of the scene graph node that is the origin of the camera path

`Destination`: The name of the scene graph node that is the destination of the camera path

### CameraPathFinished
This event is created when an automated camera path that moved the camera from the specified Origin to the Destination is finished.

`Origin`: The name of the scene graph node that is the origin of the camera path

`Destination`: The name of the scene graph node that is the destination of the camera path

### CameraMovedPosition
This event is created if the camera is moved by the user for any reason. It will only be created if the camera was not moving. If the user continuously moves the camera, only the initial event is triggered.

### ScheduledScriptExecuted
This event is created when the script scheduler is asked to trigger a script at a specific simulation time.

`Script`: The script that will be executed in the next frame

### Custom
A custom event type that can be used in a pinch when no explicit event type is available. This should only be used in special circumstances and it should be transitioned to a specific event type, if it is deemed to be useful.

`Subtype`: The type of the event as a string

`Payload`: The payload for the event, also given as a string
