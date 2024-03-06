# Streaming User Guide
By Hanna Timander and Nisse Bergman, June 2022

hanna.timander.exjobb@gmail.com

This SHOULD be all the steps that are needed to get things running but feel free to update, clarify, de-clutter these instructions if needed.

## Host
Follow these steps to host a OpenSpace session with GStreamer:
  1. Make sure that you are using the `thesis/2022/streaming` branch of OpenSpace-WebGuiFrontend (Node.js needs to be installed).
  1. Make sure that you are using the `thesis/2022/streaming` branch of OpenSpace. (Clone with `--recurse-submodules`)
  1. Make sure that you are using the `gstreamer-functionality` branch of the sgct repo as your submodule placed in in apps/ext/OpenSpace/sgct. If this is not yet a branch of the sgct repo, it can be found here https://github.com/nissebergman/sgct (Clone with `--recurse-submodules`) Just copy over and replace sgct/CMakeLists.txt and ext/gstreamer folder from the fork to the normal sgct.
  1. Configure and generate the OpenSpace project in CMake with the `SGCT_GSTREAMER_SUPPORT` checkbox enabled
  1. In **OpenSpace**
     - In _openspace.cfg_
       - Add the viewer(s) IP-address(es) to *ModuleConfigurations > Server > AllowAddresses*
       - Make sure that *ModuleConfiguration > Server > Interfaces > Type = "WebSocket" > DefaultAccess* is set to _Allow_
     - Enable developer mode for the front-end GUI
       - Go to *data/assets/customization/gui.asset* and change the _webguiDevelopmentMode_ flag to _true_.
       - (Optional) Go to *data/assets/util/webgui.asset* to see how the ports and routes are setup.
  1. In **OpenSpace-WebGuiFrontend**.
     - For _Environment.js_ make sure the `wsAddress` is the same as the host IP (not `localhost`).
     - For  _WebRTCStreaming.jsx_ make sure the `signalingServer` is the same as the host IP.
  1. (Optional) Check the GStreamer pipeline (_pipelineDescription_) in _gstreamerWebRTC.h_ looks good for your use case
  1. Start the developer frontend GUI
     - Open a terminal, go to _OpenSpace-WebGuiFrontend_
     - Run `npm install` when running first time.
     - Run `npm start` to start frontend GUI.
  1. Start the signaling server
     - Open a terminal, go to _OpenSpace-WebGuiFrontend/signalingserver_
     - Run `npm install` when running first time.
     - Run `node signaling` to start server.
  1. Build and run OpenSpace. (Preferably using *RelWithDebInfo* configuration)
  1. In the OpenSpace _Window Options_ popup menu, pick the _remote_gstreamer_output.json_ configuration file
  1. Leave the rest to the viewer!

## Viewer
Follow these steps to join a OpenSpace session from the GUI:
  1. Make sure you're using a Chromium based browser (e.g. Google Chrome, Opera, Microsoft Edge)
  1. Goto _chrome://flags_ (or other browser equivalent section) and add the host's IP-address and port under the "_Insecure origins treated as secure"_-section. An address entered here should look something like `192.168.1.39:4690`. This is probably because chrome finds IP-addresses sneaky to receive media from.
  1. Go to the address and port that the host has specified. If on same local network, should be similar to `192.168.x.xx:4690` format.
  1. Add _/frontend/#/streaming_ to the address to load the correct GUI. (Something like `192.168.x.xx:4690/frontend/#/streaming`)
     1. If this page is visited before OpenSpace has loaded on the host machine, you'll most likely get an error message. If so, wait until the host confirms the application has loaded, refresh the web page, and try again.
  1. Open the streaming menu (icon of a computer with an arrow on it) and pick "Join session". After a few seconds, the video feed should appear in the GUI.
  1. Explore OpenSpace as you'd like!
