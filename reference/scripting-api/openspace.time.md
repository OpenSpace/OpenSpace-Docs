# `openspace.time`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`advancedTime`](#timeadvancedTime-target)
    - [Modifies the passed time (first argument) by the delta time (second argument)]{#timeadvancedTime-list}


*   - [`convertTime`](#timeconvertTime-target)
    - [Converts the given time to either a J2000 seconds number or a ISO 8601 timestamp, depending on the type of the given time]{#timeconvertTime-list}


*   - [`currentApplicationTime`](#timecurrentApplicationTime-target)
    - [Returns the current application time as the number of seconds since the OpenSpace application started]{#timecurrentApplicationTime-list}


*   - [`currentTime`](#timecurrentTime-target)
    - [Returns the current time as the number of seconds since the J2000 epoch]{#timecurrentTime-list}


*   - [`currentWallTime`](#timecurrentWallTime-target)
    - [Returns the current wall time as an ISO 8601 date string (YYYY-MM-DDTHH-MN-SS) in the UTC timezone]{#timecurrentWallTime-list}


*   - [`deltaTime`](#timedeltaTime-target)
    - [Returns the amount of simulated time that passes in one second of real time]{#timedeltaTime-list}


*   - [`interpolateDeltaTime`](#timeinterpolateDeltaTime-target)
    - [Sets the amount of simulation time that happens in one second of real time]{#timeinterpolateDeltaTime-list}


*   - [`interpolateNextDeltaTimeStep`](#timeinterpolateNextDeltaTimeStep-target)
    - [Interpolate the simulation speed to the first delta time step in the list that is larger than the current simulation speed, if any]{#timeinterpolateNextDeltaTimeStep-list}


*   - [`interpolatePause`](#timeinterpolatePause-target)
    - [Same behaviour as setPause, but with interpolation]{#timeinterpolatePause-list}


*   - [`interpolatePreviousDeltaTimeStep`](#timeinterpolatePreviousDeltaTimeStep-target)
    - [Interpolate the simulation speed to the first delta time step in the list that is smaller than the current simulation speed, if any]{#timeinterpolatePreviousDeltaTimeStep-list}


*   - [`interpolateTime`](#timeinterpolateTime-target)
    - [Sets the current simulation time to the specified value]{#timeinterpolateTime-list}


*   - [`interpolateTimeRelative`](#timeinterpolateTimeRelative-target)
    - [Increments the current simulation time by the specified number of seconds]{#timeinterpolateTimeRelative-list}


*   - [`interpolateTogglePause`](#timeinterpolateTogglePause-target)
    - [Toggles the pause function, i]{#timeinterpolateTogglePause-list}


*   - [`isPaused`](#timeisPaused-target)
    - [Returns whether the simulation time is currently paused or is progressing]{#timeisPaused-list}


*   - [`pauseToggleViaKeyboard`](#timepauseToggleViaKeyboard-target)
    - [This allows for a keypress (via keybinding) to have dual functionality]{#timepauseToggleViaKeyboard-list}


*   - [`setDeltaTime`](#timesetDeltaTime-target)
    - [Sets the amount of simulation time that happens in one second of real time]{#timesetDeltaTime-list}


*   - [`setDeltaTimeSteps`](#timesetDeltaTimeSteps-target)
    - [Sets the list of discrete delta time steps for the simulation speed that can be quickly jumped between]{#timesetDeltaTimeSteps-list}


*   - [`setNextDeltaTimeStep`](#timesetNextDeltaTimeStep-target)
    - [Immediately set the simulation speed to the first delta time step in the list that is larger than the current choice of simulation speed, if any]{#timesetNextDeltaTimeStep-list}


*   - [`setPause`](#timesetPause-target)
    - [Toggles a pause function i]{#timesetPause-list}


*   - [`setPreviousDeltaTimeStep`](#timesetPreviousDeltaTimeStep-target)
    - [Immediately set the simulation speed to the first delta time step in the list that is smaller than the current choice of simulation speed if any]{#timesetPreviousDeltaTimeStep-list}


*   - [`setTime`](#timesetTime-target)
    - [Sets the current simulation time to the specified value]{#timesetTime-list}


*   - [`SPICE`](#timeSPICE-target)
    - [Returns the current time as an date string of the form (YYYY MON DDTHR:MN:SC]{#timeSPICE-list}


*   - [`togglePause`](#timetogglePause-target)
    - [Toggles the pause function, i]{#timetogglePause-list}


*   - [`UTC`](#timeUTC-target)
    - [Returns the current time as an ISO 8601 date string (YYYY-MM-DDTHH:MN:SS)]{#timeUTC-list}

:::

## Functions

(timeadvancedTime-target)=
### [`advancedTime`](#timeadvancedTime-list)
Modifies the passed time (first argument) by the delta time (second argument). The first argument can either be an ISO 8601 date string or the number of seconds past the J2000 epoch. The second argument can either be a string of the form [-]XX(s,m,h,d,M,y] with (s)econds, (m)inutes, (h)ours, (d)ays, (M)onths, and (y)ears as units and an optional - sign to move backwards in time. If the second argument is a number, it is interpreted as a number of seconds. The return value is of the same type as the first argument.


:::{card} Parameters


* base `String | Number` 



* change `String | Number` 


:::

Return type: `String | Number` 

:::{code-block} lua
:caption: Signature
openspace.time.advancedTime(base, change)
:::
___

(timeconvertTime-target)=
### [`convertTime`](#timeconvertTime-list)
Converts the given time to either a J2000 seconds number or a ISO 8601 timestamp, depending on the type of the given time.

If the given time is a timestamp: the function returns a double precision value representing the ephemeris version of that time; that is the number of TDB seconds past the J2000 epoch.

If the given time is a J2000 seconds value: the function returns a ISO 8601 timestamp.


:::{card} Parameters


* time `String | Number` 


:::

Return type: `String | Number` 

:::{code-block} lua
:caption: Signature
openspace.time.convertTime(time)
:::
___

(timecurrentApplicationTime-target)=
### [`currentApplicationTime`](#timecurrentApplicationTime-list)
Returns the current application time as the number of seconds since the OpenSpace application started.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.time.currentApplicationTime()
:::
___

(timecurrentTime-target)=
### [`currentTime`](#timecurrentTime-list)
Returns the current time as the number of seconds since the J2000 epoch.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.time.currentTime()
:::
___

(timecurrentWallTime-target)=
### [`currentWallTime`](#timecurrentWallTime-list)
Returns the current wall time as an ISO 8601 date string (YYYY-MM-DDTHH-MN-SS) in the UTC timezone.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.time.currentWallTime()
:::
___

(timedeltaTime-target)=
### [`deltaTime`](#timedeltaTime-list)
Returns the amount of simulated time that passes in one second of real time.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.time.deltaTime()
:::
___

(timeinterpolateDeltaTime-target)=
### [`interpolateDeltaTime`](#timeinterpolateDeltaTime-list)
Sets the amount of simulation time that happens in one second of real time. If a second input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* deltaTime `Number` 



* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolateDeltaTime(deltaTime, interpolationDuration)
:::
___

(timeinterpolateNextDeltaTimeStep-target)=
### [`interpolateNextDeltaTimeStep`](#timeinterpolateNextDeltaTimeStep-list)
Interpolate the simulation speed to the first delta time step in the list that is larger than the current simulation speed, if any. If an input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolateNextDeltaTimeStep(interpolationDuration)
:::
___

(timeinterpolatePause-target)=
### [`interpolatePause`](#timeinterpolatePause-list)
Same behaviour as setPause, but with interpolation. If no interpolation duration is provided, the interpolation time will be based on the `defaultPauseInterpolationDuration` and `defaultUnpauseInterpolationDuration` properties of the TimeManager.


:::{card} Parameters


* isPaused `Boolean` 



* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolatePause(isPaused, interpolationDuration)
:::
___

(timeinterpolatePreviousDeltaTimeStep-target)=
### [`interpolatePreviousDeltaTimeStep`](#timeinterpolatePreviousDeltaTimeStep-list)
Interpolate the simulation speed to the first delta time step in the list that is smaller than the current simulation speed, if any. If an input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolatePreviousDeltaTimeStep(interpolationDuration)
:::
___

(timeinterpolateTime-target)=
### [`interpolateTime`](#timeinterpolateTime-list)
Sets the current simulation time to the specified value. If the first parameter is a number, the target is the number of seconds past the J2000 epoch. If it is a string, it has to be a valid ISO 8601-like date string of the format YYYY-MM-DDTHH:MN:SS (Note: providing time zone using the Z format is not supported. UTC is assumed). If a second input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* time `String | Number` 



* interpolationDutation `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolateTime(time, interpolationDutation)
:::
___

(timeinterpolateTimeRelative-target)=
### [`interpolateTimeRelative`](#timeinterpolateTimeRelative-list)
Increments the current simulation time by the specified number of seconds. If a second input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* delta `Number` 



* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolateTimeRelative(delta, interpolationDuration)
:::
___

(timeinterpolateTogglePause-target)=
### [`interpolateTogglePause`](#timeinterpolateTogglePause-list)
Toggles the pause function, i.e. temporarily setting the delta time to 0 and restoring it afterwards. If an input value is given, the interpolation is done over the specified number of seconds.


:::{card} Parameters


* interpolationDuration `Number?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.interpolateTogglePause(interpolationDuration)
:::
___

(timeisPaused-target)=
### [`isPaused`](#timeisPaused-list)
Returns whether the simulation time is currently paused or is progressing.


Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.time.isPaused()
:::
___

(timepauseToggleViaKeyboard-target)=
### [`pauseToggleViaKeyboard`](#timepauseToggleViaKeyboard-list)
This allows for a keypress (via keybinding) to have dual functionality. In normal operational mode it will behave just like time_interpolateTogglePause, but during playback of a session recording it will pause the playback without manipulating the delta time.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.pauseToggleViaKeyboard()
:::
___

(timesetDeltaTime-target)=
### [`setDeltaTime`](#timesetDeltaTime-list)
Sets the amount of simulation time that happens in one second of real time.


:::{card} Parameters


* deltaTime `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setDeltaTime(deltaTime)
:::
___

(timesetDeltaTimeSteps-target)=
### [`setDeltaTimeSteps`](#timesetDeltaTimeSteps-list)
Sets the list of discrete delta time steps for the simulation speed that can be quickly jumped between. The list will be sorted to be in increasing order. A negative verison of each specified time step will be added per default as well.


:::{card} Parameters


* deltaTime `Number[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setDeltaTimeSteps(deltaTime)
:::
___

(timesetNextDeltaTimeStep-target)=
### [`setNextDeltaTimeStep`](#timesetNextDeltaTimeStep-list)
Immediately set the simulation speed to the first delta time step in the list that is larger than the current choice of simulation speed, if any.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setNextDeltaTimeStep()
:::
___

(timesetPause-target)=
### [`setPause`](#timesetPause-list)
Toggles a pause function i.e. setting the delta time to 0 and restoring it afterwards.


:::{card} Parameters


* isPaused `Boolean` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setPause(isPaused)
:::
___

(timesetPreviousDeltaTimeStep-target)=
### [`setPreviousDeltaTimeStep`](#timesetPreviousDeltaTimeStep-list)
Immediately set the simulation speed to the first delta time step in the list that is smaller than the current choice of simulation speed if any.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setPreviousDeltaTimeStep()
:::
___

(timesetTime-target)=
### [`setTime`](#timesetTime-list)
Sets the current simulation time to the specified value. If the parameter is a number, the value is the number of seconds past the J2000 epoch. If it is a string, it has to be a valid ISO 8601-like date string of the format YYYY-MM-DDTHH:MN:SS. Note: providing time zone using the Z format is not supported. UTC is assumed.


:::{card} Parameters


* time `Number | String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.setTime(time)
:::
___

(timeSPICE-target)=
### [`SPICE`](#timeSPICE-list)
Returns the current time as an date string of the form (YYYY MON DDTHR:MN:SC.### ::RND) as returned by SPICE.


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.time.SPICE()
:::
___

(timetogglePause-target)=
### [`togglePause`](#timetogglePause-list)
Toggles the pause function, i.e. temporarily setting the delta time to 0 and restoring it afterwards.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.time.togglePause()
:::
___

(timeUTC-target)=
### [`UTC`](#timeUTC-list)
Returns the current time as an ISO 8601 date string (YYYY-MM-DDTHH:MN:SS).


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.time.UTC()
:::

