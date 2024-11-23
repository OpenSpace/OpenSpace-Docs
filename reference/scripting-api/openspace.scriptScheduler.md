# `openspace.scriptScheduler`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`clear`](#scriptSchedulerclear-target)
    - [Clears all scheduled scripts]{#scriptSchedulerclear-list}


*   - [`loadFile`](#scriptSchedulerloadFile-target)
    - [Load timed scripts from a Lua script file that returns a list of scheduled scripts]{#scriptSchedulerloadFile-list}


*   - [`loadScheduledScript`](#scriptSchedulerloadScheduledScript-target)
    - [Load a single scheduled script]{#scriptSchedulerloadScheduledScript-list}


*   - [`scheduledScripts`](#scriptSchedulerscheduledScripts-target)
    - [Returns the list of all scheduled scripts]{#scriptSchedulerscheduledScripts-list}


*   - [`setModeApplicationTime`](#scriptSchedulersetModeApplicationTime-target)
    - [Sets the time reference for scheduled scripts to application time (seconds since OpenSpace application started)]{#scriptSchedulersetModeApplicationTime-list}


*   - [`setModeRecordedTime`](#scriptSchedulersetModeRecordedTime-target)
    - [Sets the time reference for scheduled scripts to the time since the recording was started (the same relative time applies to playback)]{#scriptSchedulersetModeRecordedTime-list}


*   - [`setModeSimulationTime`](#scriptSchedulersetModeSimulationTime-target)
    - [Sets the time reference for scheduled scripts to the simulated date & time (J2000 epoch seconds)]{#scriptSchedulersetModeSimulationTime-list}

:::

## Functions

(scriptSchedulerclear-target)=
### [`clear`](#scriptSchedulerclear-list)
Clears all scheduled scripts.


:::{card} Parameters


* group `Integer?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.clear(group)
:::
___

(scriptSchedulerloadFile-target)=
### [`loadFile`](#scriptSchedulerloadFile-list)
Load timed scripts from a Lua script file that returns a list of scheduled scripts.


:::{card} Parameters


* fileName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.loadFile(fileName)
:::
___

(scriptSchedulerloadScheduledScript-target)=
### [`loadScheduledScript`](#scriptSchedulerloadScheduledScript-list)
Load a single scheduled script. The first argument is the time at which the scheduled script is triggered, the second argument is the script that is executed in the forward direction, the optional third argument is the script executed in the backwards direction, and the optional last argument is the universal script, executed in either direction.


:::{card} Parameters


* time `String` 



* forwardScript `String` 



* backwardScript `String?` 



* universalScript `String?` 



* group `Integer?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.loadScheduledScript(time, forwardScript, backwardScript, universalScript, group)
:::
___

(scriptSchedulerscheduledScripts-target)=
### [`scheduledScripts`](#scriptSchedulerscheduledScripts-list)
Returns the list of all scheduled scripts


Return type: `Table[]` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.scheduledScripts()
:::
___

(scriptSchedulersetModeApplicationTime-target)=
### [`setModeApplicationTime`](#scriptSchedulersetModeApplicationTime-list)
Sets the time reference for scheduled scripts to application time (seconds since OpenSpace application started).


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.setModeApplicationTime()
:::
___

(scriptSchedulersetModeRecordedTime-target)=
### [`setModeRecordedTime`](#scriptSchedulersetModeRecordedTime-list)
Sets the time reference for scheduled scripts to the time since the recording was started (the same relative time applies to playback).


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.setModeRecordedTime()
:::
___

(scriptSchedulersetModeSimulationTime-target)=
### [`setModeSimulationTime`](#scriptSchedulersetModeSimulationTime-list)
Sets the time reference for scheduled scripts to the simulated date & time (J2000 epoch seconds).


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.scriptScheduler.setModeSimulationTime()
:::

