# `openspace.sessionRecording`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`disableTakeScreenShotDuringPlayback`](#sessionRecordingdisableTakeScreenShotDuringPlayback-target)
    - [Used to disable that renderings are saved during playback]{#sessionRecordingdisableTakeScreenShotDuringPlayback-list}


*   - [`enableTakeScreenShotDuringPlayback`](#sessionRecordingenableTakeScreenShotDuringPlayback-target)
    - [Enables that rendered frames should be saved during playback]{#sessionRecordingenableTakeScreenShotDuringPlayback-list}


*   - [`fileFormatConversion`](#sessionRecordingfileFormatConversion-target)
    - [Performs a conversion of the specified file to the most most recent file format, creating a copy of the recording file]{#sessionRecordingfileFormatConversion-list}


*   - [`isPlayingBack`](#sessionRecordingisPlayingBack-target)
    - [Returns true if session recording is currently playing back a recording]{#sessionRecordingisPlayingBack-list}


*   - [`isRecording`](#sessionRecordingisRecording-target)
    - [Returns true if session recording is currently recording a recording]{#sessionRecordingisRecording-list}


*   - [`setPlaybackPause`](#sessionRecordingsetPlaybackPause-target)
    - [Pauses or resumes the playback progression through keyframes]{#sessionRecordingsetPlaybackPause-list}


*   - [`startPlayback`](#sessionRecordingstartPlayback-target)
    - [Starts a playback session with keyframe times that are relative to the time since the recording was started (the same relative time applies to the playback)]{#sessionRecordingstartPlayback-list}


*   - [`startPlaybackApplicationTime`](#sessionRecordingstartPlaybackApplicationTime-target)
    - [Starts a playback session with keyframe times that are relative to application time (seconds since OpenSpace application started)]{#sessionRecordingstartPlaybackApplicationTime-list}


*   - [`startPlaybackRecordedTime`](#sessionRecordingstartPlaybackRecordedTime-target)
    - [Starts a playback session with keyframe times that are relative to the time since the recording was started (the same relative time applies to the playback)]{#sessionRecordingstartPlaybackRecordedTime-list}


*   - [`startPlaybackSimulationTime`](#sessionRecordingstartPlaybackSimulationTime-target)
    - [Starts a playback session with keyframe times that are relative to the simulated date & time]{#sessionRecordingstartPlaybackSimulationTime-list}


*   - [`startRecording`](#sessionRecordingstartRecording-target)
    - [Starts a recording session]{#sessionRecordingstartRecording-list}


*   - [`startRecordingAscii`](#sessionRecordingstartRecordingAscii-target)
    - [Starts a recording session]{#sessionRecordingstartRecordingAscii-list}


*   - [`stopPlayback`](#sessionRecordingstopPlayback-target)
    - [Stops a playback session before playback of all keyframes is complete]{#sessionRecordingstopPlayback-list}


*   - [`stopRecording`](#sessionRecordingstopRecording-target)
    - [Stops a recording session]{#sessionRecordingstopRecording-list}


*   - [`togglePlaybackPause`](#sessionRecordingtogglePlaybackPause-target)
    - [Toggles the pause function, i]{#sessionRecordingtogglePlaybackPause-list}

:::

## Functions

(sessionRecordingdisableTakeScreenShotDuringPlayback-target)=
### [`disableTakeScreenShotDuringPlayback`](#sessionRecordingdisableTakeScreenShotDuringPlayback-list)
Used to disable that renderings are saved during playback.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.disableTakeScreenShotDuringPlayback()
:::
___

(sessionRecordingenableTakeScreenShotDuringPlayback-target)=
### [`enableTakeScreenShotDuringPlayback`](#sessionRecordingenableTakeScreenShotDuringPlayback-list)
Enables that rendered frames should be saved during playback. The parameter determines the number of frames that are exported per second if this value is not provided, 60 frames per second will be exported.


:::{card} Parameters


* fps `Integer?` - Default value: `60` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.enableTakeScreenShotDuringPlayback(fps)
:::
___

(sessionRecordingfileFormatConversion-target)=
### [`fileFormatConversion`](#sessionRecordingfileFormatConversion-list)
Performs a conversion of the specified file to the most most recent file format, creating a copy of the recording file.


:::{card} Parameters


* convertFilePath `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.fileFormatConversion(convertFilePath)
:::
___

(sessionRecordingisPlayingBack-target)=
### [`isPlayingBack`](#sessionRecordingisPlayingBack-list)
Returns true if session recording is currently playing back a recording.


Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.isPlayingBack()
:::
___

(sessionRecordingisRecording-target)=
### [`isRecording`](#sessionRecordingisRecording-list)
Returns true if session recording is currently recording a recording.


Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.isRecording()
:::
___

(sessionRecordingsetPlaybackPause-target)=
### [`setPlaybackPause`](#sessionRecordingsetPlaybackPause-list)
Pauses or resumes the playback progression through keyframes.


:::{card} Parameters


* pause `Boolean` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.setPlaybackPause(pause)
:::
___

(sessionRecordingstartPlayback-target)=
### [`startPlayback`](#sessionRecordingstartPlayback-list)
Starts a playback session with keyframe times that are relative to the time since the recording was started (the same relative time applies to the playback). When playback starts, the simulation time is automatically set to what it was at recording time. The string argument is the filename to pull playback keyframes from (the file path is relative to the RECORDINGS variable specified in the config file). If a second input value of true is given, then playback will continually loop until it is manually stopped.


:::{card} Parameters


* file `String` 



* loop `Boolean?` - Default value: `false` 



* shouldWaitForTiles `Boolean?` - Default value: `true` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startPlayback(file, loop, shouldWaitForTiles)
:::
___

(sessionRecordingstartPlaybackApplicationTime-target)=
### [`startPlaybackApplicationTime`](#sessionRecordingstartPlaybackApplicationTime-list)
Starts a playback session with keyframe times that are relative to application time (seconds since OpenSpace application started). The string argument is the filename to pull playback keyframes from (the file path is relative to the RECORDINGS variable specified in the config file).


:::{card} Parameters


* file `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startPlaybackApplicationTime(file)
:::
___

(sessionRecordingstartPlaybackRecordedTime-target)=
### [`startPlaybackRecordedTime`](#sessionRecordingstartPlaybackRecordedTime-list)
Starts a playback session with keyframe times that are relative to the time since the recording was started (the same relative time applies to the playback). The string argument is the filename to pull playback keyframes from (the file path is relative to the RECORDINGS variable specified in the config file). If a second input value of true is given, then playback will continually loop until it is manually stopped.


:::{card} Parameters


* file `String` 



* loop `Boolean?` - Default value: `false` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startPlaybackRecordedTime(file, loop)
:::
___

(sessionRecordingstartPlaybackSimulationTime-target)=
### [`startPlaybackSimulationTime`](#sessionRecordingstartPlaybackSimulationTime-list)
Starts a playback session with keyframe times that are relative to the simulated date & time. The string argument is the filename to pull playback keyframes from (the file path is relative to the RECORDINGS variable specified in the config file).


:::{card} Parameters


* file `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startPlaybackSimulationTime(file)
:::
___

(sessionRecordingstartRecording-target)=
### [`startRecording`](#sessionRecordingstartRecording-list)
Starts a recording session. The string argument is the filename used for the file where the recorded keyframes are saved. The file data format is binary.


:::{card} Parameters


* recordFilePath `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startRecording(recordFilePath)
:::
___

(sessionRecordingstartRecordingAscii-target)=
### [`startRecordingAscii`](#sessionRecordingstartRecordingAscii-list)
Starts a recording session. The string argument is the filename used for the file where the recorded keyframes are saved. The file data format is ASCII.


:::{card} Parameters


* recordFilePath `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.startRecordingAscii(recordFilePath)
:::
___

(sessionRecordingstopPlayback-target)=
### [`stopPlayback`](#sessionRecordingstopPlayback-list)
Stops a playback session before playback of all keyframes is complete.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.stopPlayback()
:::
___

(sessionRecordingstopRecording-target)=
### [`stopRecording`](#sessionRecordingstopRecording-list)
Stops a recording session.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.stopRecording()
:::
___

(sessionRecordingtogglePlaybackPause-target)=
### [`togglePlaybackPause`](#sessionRecordingtogglePlaybackPause-list)
Toggles the pause function, i.e. temporarily setting the delta time to 0 and restoring it afterwards.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.sessionRecording.togglePlaybackPause()
:::

