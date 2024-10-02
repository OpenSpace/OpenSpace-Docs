# Streaming User Guide
By Hanna Timander and Nisse Bergman, June 2022 (hanna.timander.exjobb@gmail.com); Edited by Gene Payne, August 2024

## Initial Setup
These setup/configuration steps need to be performed on both the Server and Viewer prior to any connection attempts.

**Server:**
Currently this only works on Windows. The Linux version has been mothballed.
  1. Ensure that Node.js is installed on the system.
  1. Ensure that you are using the `feature/streaming-2024` branch of OpenSpace-WebGuiFrontend.
  1. Ensure that you are using the `feature/streaming` branch of OpenSpace (Clone with `--recurse-submodules`). Verify that the sgct submodule (apps/OpenSpace/ext/sgct) that it contains is at the `thesis/2022/streaming` branch (or at the correct commit to match).
  1. Configure and generate the OpenSpace project in CMake with the `SGCT_GSTREAMER_SUPPORT` checkbox enabled
  1. In **OpenSpace**
     - In _openspace.cfg_
       - Add the viewer(s) IP-address(es) to *ModuleConfigurations > Server > AllowAddresses*.
       - Make sure that *ModuleConfiguration > Server > Interfaces > Type = "WebSocket" > DefaultAccess* is set to _Allow_.
     - Enable developer mode for the front-end GUI
       - Go to *data/assets/customization/gui.asset* and change the _webguiDevelopmentMode_ flag to _true_.
       - (Optional) Go to *data/assets/util/webgui.asset* to see how the ports and routes are setup.
  1. In **OpenSpace-WebGuiFrontend**
     - For _Environment.js_ make sure the `wsAddress` is the same as the host IP (not `localhost` but can be `127.0.0.1`).
     - For _WebRTCStreaming.jsx_ make sure the `signalingServer` is the same as the host IP.
  1. Verify that the GStreamer pipeline (_pipelineDescription_) in _gstreamerWebRTC.h_ looks good for your use case.
  1. Setup the developer frontend GUI
     - Open a terminal, go to _OpenSpace-WebGuiFrontend_
     - Run `npm install` when running first time, ensure that there are no errors. You can add the `--legacy-peer-deps` option if there are dependency problems.
  1. Setup the signaling server
     - Open another terminal, go to _OpenSpace-WebGuiFrontend/src/signalingserver_
     - Run `npm install` when running first time.
  1. Build OpenSpace (Preferably using *RelWithDebInfo* configuration).

**Viewer:**
  1. Make sure you're using a Chromium based browser (e.g. Google Chrome, Opera, Microsoft Edge)
  1. Chrome might not trust the source of the video streaming, so go to _chrome://flags_ and add the host's IP-address and port under the "_Insecure origins treated as secure"_-section. An address entered here should look something like `192.168.1.39:4690`. Note that this step is not necessary if running both the Server and Viewer on the same machine using `127.0.0.1`.

## Starting a Remote Viewing Session
There are steps are provided here for both the Server and the Viewer, because the current state of the software is somewhat fragile. In the future, the following Server steps won't be required each time.
Do all of the following steps in one sequence, starting with the Server.

**OBS:** Make sure that the OpenSpace WebGUI page is _not_ open in the browser. The connection won't work if the frontend GUI connects to OpenSpace too soon.

**Server:**
  1. Start the developer frontend GUI in a terminal at _OpenSpace-WebGuiFrontend_
     - Run `npm start` to start frontend GUI (no need to restart if already running)
  1. Start the signaling server in a terminal at _OpenSpace-WebGuiFrontend/src/signalingserver_
     - Stop this server (CTRL+C) if it is already running
     - Run `node signalingserver` to start the server
  1. Start OpenSpace
     - Run OpenSpace.exe, and select the _remote_gstreamer_output_ config option in the _Window Options_ popup menu
     - If desired, you can use a direct command to bypass the launcher: `bin\RelWithDebInfo\OpenSpace.exe -c config\remote_gstreamer_output.json -b`

**Viewer:**
  1. One again, verify that the frontend GUI page is not open in a browser tab
  1. Wait until OpenSpace is past the initialization screen and starts rendering
  1. Watch the log messages in the OpenSpace console, and wait until you see messages of type `[webpack-dev-server]` scroll by
  1. In a browser, open the URL for the frontend GUI, which should look like: `192.168.x.xx:4690/frontend/#/streaming` (bookmark this for convenience)
  1. In the GUI, open the streaming menu (icon of a computer with an arrow on it), and pick "Join session"
  1. After a few seconds, the video feed should appear in the GUI, and you should be able to control the camera view with the mouse in the browser window.

If the frontend GUI crashes or loses video, or if any other problem occurs, you will need to go back to the beginning of this process and restart everything.
