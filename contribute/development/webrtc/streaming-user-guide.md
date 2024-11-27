# Streaming User Guide
By Hanna Timander and Nisse Bergman, June 2022 (hanna.timander.exjobb@gmail.com); Edited by Gene Payne, September 2024

## Initial Setup
These setup/configuration steps need to be performed on both the Server and Viewer prior to any connection attempts. Currently the server only runs on Windows. The Linux version has been mothballed.

### **Server:**
#### **Determine Server IP Address**
Some of the steps below require the server's IP address. This depends on the network configuration of the server and client:
- If the server and client are running on the same machine, then use `127.0.0.1` instead of `localhost`.
- If both machines are running on the same LAN, then the server's LAN IP address can be used (probably starting with `192.`).
- If the client will be accessing the server from another network, then the server's public IP, or external IP, address will be used.
#### **OpenSpace Software**
- Checkout the `feature/streaming` branch of OpenSpace (Clone with `--recurse-submodules`). In addition, verify that the sgct submodule within OpenSpace (apps/OpenSpace/ext/sgct) is using the `thesis/2022/streaming` branch (or at the correct commit to match).
- Configure and generate the OpenSpace project in CMake with the `SGCT_GSTREAMER_SUPPORT` checkbox enabled
- Build OpenSpace (Preferably using *RelWithDebInfo* configuration).
- Edit _openspace.cfg_
  - Add the viewer(s) IP-address(es) to *ModuleConfigurations > Server > AllowAddresses*.
  - Make sure that *ModuleConfiguration > Server > Interfaces > Type = "WebSocket" > DefaultAccess* is set to _Allow_.
- Enable developer mode for the front-end GUI
  - Go to *data/assets/customization/gui.asset* and change the _webguiDevelopmentMode_ flag to _true_.
  - (Optional) Go to *data/assets/util/webgui.asset* to see how the ports and routes are setup.
#### **OpenSpace-WebGuiFrontend Software**
- Install Node.js and npm if necessary.
- Checkout the `feature/streaming-2024` branch of OpenSpace-WebGuiFrontend.
- In _src/api/Environment.js_, set `wsAddress` to the server IP address discussed above.
- In _environment.js_, also set `wsAddress` to the server IP address.
- In _WebRTCStreaming.jsx_ set the `signalingServer` to the server IP address.
- Verify that the GStreamer pipeline (_pipelineDescription_) in _gstreamerWebRTC.h_ looks good for your use case.
- Setup the developer frontend GUI
  - Open a terminal, go to _OpenSpace-WebGuiFrontend_
  - Run `npm install` when running first time, ensure that there are no errors. You can add the `--legacy-peer-deps` option if there are dependency problems.
- Setup the signaling server
  - Open another terminal, go to _OpenSpace-WebGuiFrontend/src/signalingserver_
  - Run `npm install` when running first time.

### **Viewer:**
 - Use a Chromium based browser (e.g. Google Chrome, Opera, Microsoft Edge)
 - The Chrome browser won't trust the source of the video streaming if it comes from a non-secure server (plain http rather than https). If the server does not have an SSL certificate, go to _chrome://flags_ and add the server's IP-address and port under the "_Insecure origins treated as secure"_-section. An address entered here should look like `http://192.168.1.39:4690`. Note that this step is not necessary if running both the Server and Viewer on the same machine using `127.0.0.1`.

## Starting a Remote Viewing Session
Do all of the following steps in one sequence, starting with the Server.

**Server:**
1. Start the developer frontend GUI in a terminal at _OpenSpace-WebGuiFrontend_
  - Run `npm start` to start frontend GUI (no need to restart if already running)
1. Start the signaling server in a terminal at _OpenSpace-WebGuiFrontend/src/signalingserver_
  - Run `node signalingserver` to start the server
1. Start OpenSpace
  - Run OpenSpace.exe, and select the _remote_gstreamer_output_ config option in the _Window Options_ popup menu
  - If desired, you can use a direct command to bypass the launcher: `bin\RelWithDebInfo\OpenSpace.exe -c config\remote_gstreamer_output.json -b`

**Viewer:**
1. In a browser, open the URL for the frontend GUI, which should look like: `192.168.x.xx:4690/frontend/#/streaming` (bookmark this for convenience)
1. In the GUI, open the streaming menu (icon of a computer with an arrow on it), and click "Join session"
1. After a few seconds, the video feed should appear in the GUI, and you should be able to control the camera view with the mouse in the browser window.
1. If there is a problem, refresh the browser and Join the session again. It won't be necessary to restart the other components.
