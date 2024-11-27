---
authors:
  - name: Brian Abbott, Alex Bock
    affiliation: American Museum of Natural History
---


# Record Menu: 

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::


# Session Recording
The Session Recording feature provides a way to record all views, renderables, and time control to a file that can be played back at a later time. OpenSpace is interactive software, meant to be used in real-time. However, it can be difficult and time-consuming to recreate all of the camera movements and content settings when presenting content that is complex and/or prolonged. Session Recording can be used to automate some or all parts of a particular presentation.


## Recording a Session
Clicking the camera icon at the bottom menu bar will display the Session Recording menu. If using Linux (which currently does not support the on-screen menu), a separate browser can be used to show the menu (http://localhost:4680/) or console commands can be used (see the advanced wiki page which is linked at the bottom of this page). The top half of the menu has controls for starting a recording. Leave the "Text file format" option unchecked unless advanced features are being used (see section below if interested). Enter a filename (without extension) for the recording, and press the Record button when ready to start. The file will be saved in `user/recordings/` directory. Upon recording, the sub-menu disappears and the program can be used normally, with all actions & settings being recorded. Click the red "Stop recording" button when done, and a file of the specified name will be saved to user/recordings/ in the OpenSpace directory.


## Playback of a Recorded Session
There are two ways to handle the simulation time when playing back a session. The most common method is to allow OpenSpace to set the simulation time (the current time visible in the menu) to exactly what it was when recorded ("Force time change to recorded time" checkbox). If the "Loop playback" option is checked, then the recording will continually repeat itself until manually stopped. The drop-down menu contains a list of files in the user/recordings/ directory that can be played. Mouse camera control is disabled during playback. The bottom menu (as well as log messages) will indicate when playback is finished. You can abort the playback by clicking the 'Stop Recording' button, or entering: `openspace.sessionRecording.stopPlayback()` in the console. It is also possible to simply pause playback by clicking the menu button.


## Session Recording Advanced Features
### Console Script Commands
To start a recording, open the console with the **\`** key and enter: `openspace.sessionRecording.startRecording('filename.osrec');` To finish recording, open the console again and enter: `openspace.sessionRecording.stopRecording();` The GUI restricts the available playback files to those that reside in user/recordings (or possibly elsewhere if the USER variable has a custom definition). However, a relative path to a playback file anywhere in the filesystem can be entered in the `startPlayback` function. To see a full list of these commands, open a browser URL window and type the directory path to where OpenSpace is installed, and add the following path:
/documentation/index.html#openspace.sessionRecording

### Playback Using Advanced Time Options
There are two ways to handle the simulation time when playing back a session. The most common method is to allow OpenSpace to set the simulation time (the current time visible in the menu) to exactly what it was when recorded.
  1. To play back a session in this manner, use the syntax: `openspace.sessionRecording.startPlayback('filename.osrec');` This function is available in the GUI with the "Force time change to match recording" box checked. Playback can also be performed without changing the current simulation time, in which case there are three different time options that can be used:
  1. Recorded Time - recorded actions will play back relative to the time that the recording started, or the time that the playback started. For example, if a layer was turned on 3 seconds after starting recording, then in the playback it will turn on 3 seconds after playback started (regardless of what simulation time is). Example: `openspace.sessionRecording.startPlaybackRecordedTime('filename.osrec');` This function is available in the GUI with the "Force time change to match recording" box is *un*-checked.
  1. Application Time - recorded actions will play back relative to the time that the OpenSpace application started. Consider the example of a session file that, at the time it was recorded, OpenSpace had been running for 10 minutes. In a later session, a user starts OpenSpace and then starts playback of that file 1 minute later. In this case, the playback will begin 9 minutes after that point (regardless of what simulation time is). Example: `openspace.sessionRecording.startPlaybackApplicationTime('filename.osrec');`
  1. Simulation Time - recorded actions will be locked to the simulated time in OpenSpace, and will not play back unless the time is set to the specific date & time. With this mode, it is necessary to manually set the simulation time to before what it was when recorded. Playback will begin when the current simulation time reaches the recorded simulation time. Example: `openspace.sessionRecording.startPlaybackSimulationTime('filename.osrec');` You can abort the playback by entering: `openspace.sessionRecording.stopPlayback();`

### Known Issues
Problems currently occur when playing back files that contain some types of time manipulation. If playback gets in a strange state because of this, then the `openspace.sessionRecording.stopPlayback()` command can be used to end playback. Camera positions are time.dependent, so things will look different if you don't play back in simulation mode and the time is set far in the past/future.

### ASCII File Format
When saving the recording in ASCII format instead of binary, the file becomes editable and will contain a series of rows like this:

`camera 35.6259 0.125842 624861769.816 14150159.7269534 1447711.8646562 22214479.4404503 -0.2036835 -0.1934829 -0.7594912 -0.5867287 4.0000052e-07 F Earth`

Below is an explanation of the 14 columns in the example entry:
  - 00 - "camera" this denotes that this row represents a camera keyframe.
  - 01 - "35.6259" - a timestamp representing the number of seconds since openspace has been launched.
  - 02 - "0.125842" - a timestamp representing the number of seconds since the recording has been started.
  - 03 - "624861769.816" - a time stamp representing the simulation time in openspace represented as J2000 seconds.
  - 04 - "14150159.7269534" - the x coordinate of the camera position.
  - 05 - "1447711.8646562" - the y coordinate of the camera position.
  - 06 - "22214479.4404503" - the z coordinate of the camera position.
  - 07 - "-0.2036835" - the x value of the camera's rotation vector.
  - 08 - "-0.1934829" - the y value of the camera's rotation vector
  - 09 - "-0.7594912" - the z value of the camera's rotation vector
  - 10 - "-0.5867287" - the w value of the camera's rotation vector
  - 11 - "4.0000052e-07" - a scale value (current scaling of the focus node; in this example, the small value means the camera is zoomed far out)
  - 12 - "F" - a value representing (T)rue or (F)alse for whether or not the camera is following the rotation of the focus node (e.g. rotating along with a planet to stay fixed at a spot on its surface)
  - 13 - "Earth" - the openspace identifier of the camera's focus node

### Saving Screen Frames for Offline Movie Rendering
Session Recording can be used to generate individual screen frames which can be rendered into a movie file.
When playing back using the GUI, check the "Output Frames" box, enter the desired saved framerate, then click Play. A .png image file will be saved for every frame in the user/screenshots/\<date/time\> directory.

### File Conversion
OpenSpace's TaskRunner executable can now be used to convert between ascii and binary recording formats. The typical format is binary, since it is much more space efficient. Using the conversion task to switch a binary recording to ascii makes it possible to debug or modify a recording in a readable form. It is also possible to split or combine recordings.
The conversion task can be run by doing the following:
  1. Copy the file **data/tasks/sessionRecordConvertExample1.task** and rename it. Edit the contents to specify the `InputFilePath` to convert, and the desired `OutputFilePath`.
  1. Start **bin/TaskRunner** in a terminal. At the prompt, type the full name (with **.task** extension) of the task file copied & edited above.

### File Extensions
The extension of recording filenames is **.osrec** for binary format recordings and **.osrectxt** for ascii format. When starting a recording it is not necessary to add the file extension, as it will be added based on the recording mode. It is necessary to specify the full filename at playback, however.

### Comment Lines
Comments can be added to ascii recordings to help with debugging, joining, or splicing. Any line that starts with `#` is ignored as a comment line.
