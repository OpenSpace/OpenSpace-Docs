---
authors:
  - name: Brian Abbott, Alex Bock
    affiliation: American Museum of Natural History
---


# Record Panel: Save and Playback a Session


:::{figure} toolbar_record.png
:align: center
:width: 1000px
:alt: Toolbar with the Record Panel highlighted

The Record Panel Button in the OpenSpace Toolbar.
:::

The Record Panel enables the recording of a session. Included are the flightpath, the assets used, and the time settings. Once a session is recorded and saved, you can play it back later using the same panel.

While OpenSpace was designed to be an interactive tool to explore data, there are times when you'll want to record a session to playback for an audience so you do not have to recreate all the camera moves and scene settings. Or, you may want to render frames from a recording session into a movie. We will discuss how to do these things below.


:::{figure} record_panel.png
:align: center
:width: 50%
:figwidth: 80%
:alt: OpenSpace's Record Panel

The Record Panel in OpenSpace.
:::


## Record a Session
Recording a session is easy, but you'll want to do some homework before you hit the Record Button. First, you'll want to have the data sets configured how you like to see them. If you want trails on or off, if you want certain data sets on or off, etc. Second, you'll want to adjust the time settings to your liking. Finally, you'll want to map out your planned flight a bit to have a notion of your planned route and any flight moves.

Once you're ready, proceed to your starting point. Enter a filename, without an extension, in the `Enter recording filename` box, the press the {menuselection}`Record` Button, leaving all other options unchecked.

Once the recording begins, you will see a red indicator on the Toolbar as well as in the Record Panel.

:::{figure} record_panel_recording.png
:align: center
:width: 70%
:alt: OpenSpace's Stop Recording button

Portion of the OpenSpace Toolbar showing a recording in progress.
:::

:::{figure} record_panel_recording_2.png
:align: center
:width: 40%
:alt: OpenSpace's Stop Recording button, in the record panel

Portion of the Record Panel showing a recording in progress.
:::

Once you're finished with your session, press the red {menuselection}`Stop Recording` Button in the Toolbar.

The resulting file is saved in the `user/recordings` folder and has an `.osrec` extension. The file itself is binary, so it is unreadable in a standard text editor.



{.advanced-topic}
[Advanced]{.advanced}
::::{dropdown} Option: Text File Format

If you check the `Use text file format` option in the Record Panel, the file will be saved in a readable text format. This is less efficient than the default binary format, but allows you to fine-tune the parameters. This is an advanced topic because you can only fine-tune these parameters by writing code yourself to hand-make a flightpath over some period of time. It is virtually impossible to create a sensible flightpath by altering the position and view angles by hand.

With this option checked, the resulting file will have an `.osrectxt` extension.



An example line from the resulting text file will appear, mostly, as a series of numbers:

`camera 35.6259 0.125842 624861769.816 14150159.7269534 1447711.8646562 22214479.4404503 -0.2036835 -0.1934829 -0.7594912 -0.5867287 4.0000052e-07 F Earth`

Each field in this line is defined as:

:::{table} Table with caption
:widths: auto
:align: center

| Column | Description | units |
| --- | --- | --- |
| 1 | [`camera` or `script`] denotes that this row represents a camera keyframe or script action. |  |
| 2 | Time since OpenSpace launch | seconds |
| 3 | Time since the start of the recording session | seconds |
| 4 | A time stamp for the simulation time in OpenSpace | J2000 seconds |
| 5 | X coordinate of the camera position | meters |
| 6 | Y coordinate of the camera position | meters |
| 7 | Z coordinate of the camera position | meters |
| 8 | X value of the camera's rotation vector | unitless |
| 9 | Y value of the camera's rotation vector | unitless |
| 10 | Z value of the camera's rotation vector | unitless |
| 11 | W value of the camera's rotation vector | unitless |
| 12 | A scale value realted to camera's zoom (smaller = zoomed out) |  |
| 13 | [`T` or `F`] Is the camera following the the rotation of the focus mode (e.g., rotating along with a planet to remain fixed over a position on that planet) | True or False |
| 14 | OpenSpace identifier of the camera's focus node |  |
:::

If you wish to comment out a line, you can use the `#` character.

::::



% The taskrunner is no longer included in the distribution. So, we comment out this section.
%
%
% ::::{dropdown} Converting from Binary to Text File
% OpenSpace has a series of tools outside the main program that accomplish specific tasks called the TaskRunner. The TaskRunner can be used to convert a binary file to readable text. You may want to do this to modify a recording, or split/combine recordings.

% TASKRUNNER NOT INCLUDED ANYMORE.

% Follow these steps to convert a file:
% 1. Open the directory: `OpenSpace/data/tasks`.
% 2. Duplicate the file `sessionRecordConvertExample1.task` and rename the new file with a `.task` extension.
% 3. Edit the new file to specify the `InputFilePath` and `OutputFilePath`.
% 4. In a terminal, run `OpenSpace/bin/TaskRunner` ??? .
% 5. At the prompt, type the full name of the task file you created above to run the conversion.

% ::::



## Playback a Session

Playing back a previously recorded session will abruptly move you to the starting point of the recoded session, then play the session. The time in OpenSpace will shift to the time settings when the sessions was recorded. Navigation control is disabled during playback.

Choose a file to be played back using the dropdown menu. The files that appear here are located in your `user/recordings` directory. Choose the desired file, then press the {menuselection}`Play` Button. Once you play a recording back, the blue Pause and Stop Playback buttons appear in the Toolbar.

:::{figure} record_panel_playback.png
:align: center
:width: 70%
:alt: OpenSpace's playback butttons

Portion of the OpenSpace Toolbar showing a playback in progress.
:::

:::{figure} record_panel_playback_2.png
:align: center
:width: 40%
:alt: OpenSpace's playback buttons, in the record panel

Portion of the Record Panel showing a playback in progress.
:::


### Option: Loop Playback

When the `Loop Playback` option is checked, the session will repeat itself, going directly to the beginning of the recorded session once it has reached the end. Time will revert back to the beginning of the session as well.

Playback will run continuously until you use the {menuselection}`Stop Playback` or {menuselection}`Pause` buttons.

### Option: Output Frames

The `Output Frames` option determines whether screen shots are generated for the recoded session during playback. Once you check this option, you can specify the desired framerate. Pressing {menuselection}`Play` will then play the session, and take a snapshot at each frame---this will cause the playback to be a bit slower. Outputting frames will create a series of `.png` image files in the `user.screenshots/[timestamp]`, for example, `user/screenshots/2024-10-27-14-30-00` if you began recording frames on 27 October 2024 at 2:30pm.

The resulting images may be imported into a program that can render them into a movie file.


### Options: Hide User Interface Components on Playback
The `Hide GUI on playback` and `Hide dashboards on playback` options can be used to hide the user interface overlays while a recording is being played back. This can for example be useful when outputting the frames of a recording, to not show the user interface in the outputed frames. The overlays will be shown again once the playback is finished.

:::{note}
Hiding the user interface during playback also hides the buttons for pausing or stopping the playback. If you want to abort a sessions recording, you can use the {kbd}`F1` key to bring back the user interface.
:::


% ### Playback of a Recorded Session
%There are two ways to handle the simulation time when playing back a session. The most common method is to allow OpenSpace to set the simulation time (the current time visible in the menu) to exactly what it was when recorded ("Force time change to recorded time" checkbox). If the "Loop playback" option is checked, then the recording will continually repeat itself until manually stopped. The drop-down menu contains a list of files in the user/recordings/ directory that can be played. Mouse camera control is disabled during playback. The bottom menu (as well as log messages) will indicate when playback is finished. You can abort the playback by clicking the 'Stop Recording' button, or entering: `openspace.sessionRecording.stopPlayback()` in the console. It is also possible to simply pause playback by clicking the menu button.


% ### Session Recording Advanced Features
% #### Console Script Commands
% To start a recording, open the console with the **\`** key and enter: `openspace.sessionRecording.startRecording('filename.osrec');` To finish recording, open the console again and enter: `openspace.sessionRecording.stopRecording();` The GUI restricts the available playback files to those that reside in user/recordings (or possibly elsewhere if the USER variable has a custom definition). However, a relative path to a playback file anywhere in the filesystem can be entered in the `startPlayback` function. To see a full list of these commands, open a browser URL window and type the directory path to where OpenSpace is installed, and add the following path: /documentation/index.html#openspace.sessionRecording
%
% #### Playback Using Advanced Time Options
% There are two ways to handle the simulation time when playing back a session. The most common method is to allow OpenSpace to set the simulation time (the current time visible in the menu) to exactly what it was when recorded.
%   1. To play back a session in this manner, use the syntax: `openspace.sessionRecording.startPlayback('filename.osrec');` This function is available in the GUI with the "Force time change to match recording" box checked. Playback can also be performed without changing the current simulation time, in which case there are three different time options that can be used:
%   1. Recorded Time - recorded actions will play back relative to the time that the recording started, or the time that the playback started. For example, if a layer was turned on 3 seconds after starting recording, then in the playback it will turn on 3 seconds after playback started (regardless of what simulation time is). Example: `openspace.sessionRecording.startPlaybackRecordedTime('filename.osrec');` This function is available in the GUI with the "Force time change to match recording" box is *un*-checked.
%   1. Application Time - recorded actions will play back relative to the time that the OpenSpace application started. Consider the example of a session file that, at the time it was recorded, OpenSpace had been running for 10 minutes. In a later session, a user starts OpenSpace and then starts playback of that file 1 minute later. In this case, the playback will begin 9 minutes after that point (regardless of what simulation time is). Example: `openspace.sessionRecording.startPlaybackApplicationTime('filename.osrec');`
%   1. Simulation Time - recorded actions will be locked to the simulated time in OpenSpace, and will not play back unless the time is set to the specific date & time. With this mode, it is necessary to manually set the simulation time to before what it was when recorded. Playback will begin when the current simulation time reaches the recorded simulation time. Example: `openspace.sessionRecording.startPlaybackSimulationTime('filename.osrec');` You can abort the playback by entering: `openspace.sessionRecording.stopPlayback();`


