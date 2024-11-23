# `openspace.audio`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`currentlyPlaying`](#audiocurrentlyPlaying-target)
    - [Returns the list of all tracks that are currently playing]{#audiocurrentlyPlaying-list}


*   - [`globalVolume`](#audioglobalVolume-target)
    - [Returns the global volume for all track]{#audioglobalVolume-list}


*   - [`isLooping`](#audioisLooping-target)
    - [Returns whether the track referred to by the \\p identifier is set to be looping or whether it should played only once]{#audioisLooping-list}


*   - [`isPaused`](#audioisPaused-target)
    - [Returns whether the track refered to by the \\p identifier is currently playing or paused]{#audioisPaused-list}


*   - [`isPlaying`](#audioisPlaying-target)
    - [Returns whether the track referred to by the \\p identifier is currently playing]{#audioisPlaying-list}


*   - [`pauseAll`](#audiopauseAll-target)
    - [Pauses the playback for all sounds, while keeping them valid]{#audiopauseAll-list}


*   - [`pauseAudio`](#audiopauseAudio-target)
    - [Pauses the playback of the track referred to by the \\p identifier]{#audiopauseAudio-list}


*   - [`playAllFromStart`](#audioplayAllFromStart-target)
    - [Takes all of the sounds that are currently registers, unpauses them and plays them from their starting points]{#audioplayAllFromStart-list}


*   - [`playAudio`](#audioplayAudio-target)
    - [Starts playing the audio file located and the provided \\p path]{#audioplayAudio-list}


*   - [`playAudio3d`](#audioplayAudio3d-target)
    - [Starts playing the audio file located and the provided \\p path]{#audioplayAudio3d-list}


*   - [`resumeAll`](#audioresumeAll-target)
    - [Resumes the playback for all sounds that have been paused]{#audioresumeAll-list}


*   - [`resumeAudio`](#audioresumeAudio-target)
    - [Resumes the playback of a track that was previously paused through the #pauseAudio function]{#audioresumeAudio-list}


*   - [`set3dListenerPosition`](#audioset3dListenerPosition-target)
    - [Sets the position and orientation of the listener]{#audioset3dListenerPosition-list}


*   - [`set3dSourcePosition`](#audioset3dSourcePosition-target)
    - [Updates the 3D position of a track started through the #playAudio3d function]{#audioset3dSourcePosition-list}


*   - [`setGlobalVolume`](#audiosetGlobalVolume-target)
    - [Sets the global volume for all track referred to the new \\p volume]{#audiosetGlobalVolume-list}


*   - [`setLooping`](#audiosetLooping-target)
    - [Controls whether the track referred to by the \\p identifier should be looping or just be played once]{#audiosetLooping-list}


*   - [`setSpeakerPosition`](#audiosetSpeakerPosition-target)
    - [Sets the position of the speaker for the provided \\p channel to the provided \\p position]{#audiosetSpeakerPosition-list}


*   - [`setVolume`](#audiosetVolume-target)
    - [Sets the volume of the track referred to by \\p handle to the new \\p volume]{#audiosetVolume-list}


*   - [`speakerPosition`](#audiospeakerPosition-target)
    - [Returns the position for the speaker of the provided \\p channel]{#audiospeakerPosition-list}


*   - [`stopAll`](#audiostopAll-target)
    - [Stops all currently playing tracks]{#audiostopAll-list}


*   - [`stopAudio`](#audiostopAudio-target)
    - [Stops the audio referenced by the \\p identifier]{#audiostopAudio-list}


*   - [`volume`](#audiovolume-target)
    - [Returns the volume for the track referred to by the \\p handle]{#audiovolume-list}

:::

## Functions

(audiocurrentlyPlaying-target)=
### [`currentlyPlaying`](#audiocurrentlyPlaying-list)
Returns the list of all tracks that are currently playing.


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.audio.currentlyPlaying()
:::
___

(audioglobalVolume-target)=
### [`globalVolume`](#audioglobalVolume-list)
Returns the global volume for all track. The number returned will be greater or equal to 0.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.audio.globalVolume()
:::
___

(audioisLooping-target)=
### [`isLooping`](#audioisLooping-list)
Returns whether the track referred to by the \\p identifier is set to be looping or whether it should played only once. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped 
:::

Return type: `Boolean`  `Yes` if the track is looping, `No` otherwise

:::{code-block} lua
:caption: Signature
openspace.audio.isLooping(identifier)
:::
___

(audioisPaused-target)=
### [`isPaused`](#audioisPaused-list)
Returns whether the track refered to by the \\p identifier is currently playing or paused. If it was be paused through a previous call to #pauseAudio, this function will return `true`. If it has just been created or resumed through a call to #resumeAudio, it will return `false`. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped 
:::

Return type: `Boolean`  `true` if the track is currently paused, `false` if it is playing

:::{code-block} lua
:caption: Signature
openspace.audio.isPaused(identifier)
:::
___

(audioisPlaying-target)=
### [`isPlaying`](#audioisPlaying-list)
Returns whether the track referred to by the \\p identifier is currently playing. A volume of 0 is still considered to be playing. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped 
:::

Return type: `Boolean`  `true` if the track is currently playing, `false` otherwise

:::{code-block} lua
:caption: Signature
openspace.audio.isPlaying(identifier)
:::
___

(audiopauseAll-target)=
### [`pauseAll`](#audiopauseAll-list)
Pauses the playback for all sounds, while keeping them valid. This function behaves the same as if calling #pauseAudio on all of the sounds that are currently playing.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.pauseAll()
:::
___

(audiopauseAudio-target)=
### [`pauseAudio`](#audiopauseAudio-list)
Pauses the playback of the track referred to by the \\p identifier. The playback can later be resumed through the #resumeAudio function. Trying to pause an already paused track will not do anything, but is valid. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.pauseAudio(identifier)
:::
___

(audioplayAllFromStart-target)=
### [`playAllFromStart`](#audioplayAllFromStart-list)
Takes all of the sounds that are currently registers, unpauses them and plays them from their starting points


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.playAllFromStart()
:::
___

(audioplayAudio-target)=
### [`playAudio`](#audioplayAudio-list)
Starts playing the audio file located and the provided \\p path. The \\p loop parameter determines whether the file is only played once, or on a loop. The sound is later referred to by the \\p identifier name. The audio file will be played in \"background\" mode, which means that each channel will be played at full volume. To play a video using spatial audio, use the #playAudio3d function instead.


:::{card} Parameters


* path `Path` 


    * The audio file that should be played 

* identifier `String` 


    * The name for the sound that is used to refer to the sound 

* shouldLoop `Boolean?` - Default value: `true` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.playAudio(path, identifier, shouldLoop)
:::
___

(audioplayAudio3d-target)=
### [`playAudio3d`](#audioplayAudio3d-list)
Starts playing the audio file located and the provided \\p path. The \\p loop parameter determines whether the file is only played once, or on a loop. The sound is later referred to by the \\p identifier name. The \\p position parameter determines the spatial location of the sound in a meter-based coordinate system. The position of the listener is (0,0,0) with the forward direction along the +y axis. This means that the \"left\" channel in a stereo setting is towards -x and the \"right\" channel towards x. This default value can be customized through the #set3dListenerParameters function. If you want to play a video without spatial audio, use the #playAudio function instead.


:::{card} Parameters


* path `Path` 


    * The audio file that should be played 

* identifier `String` 


    * The name for the sound that is used to refer to the sound 

* position `vec3` 


    * The position of the audio file in the 3D environment 

* shouldLoop `Boolean?` - Default value: `true` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.playAudio3d(path, identifier, position, shouldLoop)
:::
___

(audioresumeAll-target)=
### [`resumeAll`](#audioresumeAll-list)
Resumes the playback for all sounds that have been paused. Please note that this will also resume the playback for the sounds that have been manually paused, not just those that were paused through the #pauseAll function.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.resumeAll()
:::
___

(audioresumeAudio-target)=
### [`resumeAudio`](#audioresumeAudio-list)
Resumes the playback of a track that was previously paused through the #pauseAudio function. Trying to resume an already playing track will not do anything, but is valid. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.resumeAudio(identifier)
:::
___

(audioset3dListenerPosition-target)=
### [`set3dListenerPosition`](#audioset3dListenerPosition-list)
Sets the position and orientation of the listener. This new position is automatically used to adjust the relative position of all 3D tracks. Each parameter to this function call is optional and if a value is omitted, the currently set value continues to be used instead. The coordinate system for the tracks and the listener is a meter-based coordinate system.


:::{card} Parameters


* position `vec3` 


    * The position of the listener. 

* lookAt `vec3?` 


    * The direction vector of the forward direction 

* up `vec3?` 


    * The up-vector of the coordinate system
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.set3dListenerPosition(position, lookAt, up)
:::
___

(audioset3dSourcePosition-target)=
### [`set3dSourcePosition`](#audioset3dSourcePosition-list)
Updates the 3D position of a track started through the #playAudio3d function. See that function and the #set3dListenerParameters function for a complete description. The \\p identifier must be a name for a sound that was started through the #playAudio3d function.


:::{card} Parameters


* identifier `String` 



* position `vec3` 


    * The new position from which the track originates
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.set3dSourcePosition(identifier, position)
:::
___

(audiosetGlobalVolume-target)=
### [`setGlobalVolume`](#audiosetGlobalVolume-list)
Sets the global volume for all track referred to the new \\p volume. The total for each track is the global volume set by this function multiplied with the volume for the specific track set through the #setVolume function. The default value for the global volume is 0.5. The volume should be a number bigger than 0, where 1 is the maximum volume level. The \\p fade controls whether the volume change should be immediately (if it is 0) or over how many seconds it should change. The default is for it to change over 500 ms.


:::{card} Parameters


* volume `Number` 


    * The new volume level. Must be greater or equal to 0 

* fade `Number?` - Default value: `0.5f` 


    * How much time the fade from the current volume to the new volume should take
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.setGlobalVolume(volume, fade)
:::
___

(audiosetLooping-target)=
### [`setLooping`](#audiosetLooping-list)
Controls whether the track referred to by the \\p identifier should be looping or just be played once. If a track is converted to not looping, it will finish playing until the end of the file. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped 

* shouldLoop `Boolean` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.setLooping(identifier, shouldLoop)
:::
___

(audiosetSpeakerPosition-target)=
### [`setSpeakerPosition`](#audiosetSpeakerPosition-list)
Sets the position of the speaker for the provided \\p channel to the provided \\p position. In general, this is considered an advanced feature to accommodate non-standard audio environments.


:::{card} Parameters


* handle `Integer` 



* position `vec3` 


    * The new position for the speaker
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.setSpeakerPosition(handle, position)
:::
___

(audiosetVolume-target)=
### [`setVolume`](#audiosetVolume-list)
Sets the volume of the track referred to by \\p handle to the new \\p volume. The volume should be a number bigger than 0, where 1 is the maximum volume level. The \\p fade controls whether the volume change should be immediately (if it is 0) or over how many seconds it should change. The default is for it to change over 500 ms.


:::{card} Parameters


* identifier `String` 



* volume `Number` 


    * The new volume level. Must be greater or equal to 0 

* fade `Number?` - Default value: `0.5f` 


    * How much time the fade from the current volume to the new volume should take
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.setVolume(identifier, volume, fade)
:::
___

(audiospeakerPosition-target)=
### [`speakerPosition`](#audiospeakerPosition-list)
Returns the position for the speaker of the provided \\p channel.


:::{card} Parameters


* handle `Integer` 


:::

Return type: `vec3` 

:::{code-block} lua
:caption: Signature
openspace.audio.speakerPosition(handle)
:::
___

(audiostopAll-target)=
### [`stopAll`](#audiostopAll-list)
Stops all currently playing tracks. After this function, none of the identifiers used to previously play a sound a valid any longer, but can still be used by the #playAudio or #playAudio3d functions to start a new sound. This function behaves the same way as if manually calling #stopAudio on all of the sounds that have been started.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.stopAll()
:::
___

(audiostopAudio-target)=
### [`stopAudio`](#audiostopAudio-list)
Stops the audio referenced by the \\p identifier. The \\p identifier must be a name for a sound that was started through the #playAudio or #playAudio3d functions. After this function, the \\p identifier can not be used for any other function anymore except for #playAudio or #playAudio3d to start a new sound.


:::{card} Parameters


* identifier `String` 


    * The identifier to the track that should be stopped
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.audio.stopAudio(identifier)
:::
___

(audiovolume-target)=
### [`volume`](#audiovolume-list)
Returns the volume for the track referred to by the \\p handle. The number returned will be greater or equal to 0.


:::{card} Parameters


* identifier `String` 


:::

Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.audio.volume(identifier)
:::

