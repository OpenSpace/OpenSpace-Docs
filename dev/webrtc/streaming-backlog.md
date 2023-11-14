# OpenSpace Streaming Structure and Good-To-Knows

By Hanna Timander and Nisse Bergman, June 2022

Feel free to add and/or remove stuff here that gains or loses relevance.

## OpenSpace Front-end
These are the most important files that are new for this thesis in the frontend repo:

  - `src/utils/WebRTCStreaming.jsx`
    This file takes care of all WebRTC related functionality within the GUI.
  - `src/views/StreamingGui.jsx`
    This is the GUI the streaming viewer should use, and is accessed by the _/streaming_ route in the URL as defined in _App.jsx_. Some new/modified components are used in the GUI: `NavigationLayer`, `StreamingBottomBar`, `StreamedVideo`, and `FlightSettings`.
  - `src/components/NavigationLayer`
    This component is the same as the "Control Area" div in the `FlightControlPanel` component, but is spanned over the entire screen.
  - `src/views/HostGui.jsx`
    This GUI was primarily used for the WebRTC screen share and Spout solutions, so it could be removed. It is not needed for the GStreamer solution to start.
  - `signalingserver/signaling.js`
    Server that is at the core of the WebRTC peer-to-peer initiation

## OpenSpace Application
These are the most important files that are new for this thesis in the OpenSpace repo.

  - `gstreamerWebRTC.h`
    This file contains all necessary functions needed for the GStreamer functionality. As is, a few of these functions are called in the _main.cpp_ OpenSpace file as part of the SGCT/render engine callbacks. All code in _main.cpp_ that we've added have the `#if SGCT_HAS_GSTREAMER `wrapper around it, so it should be easy to find.
  - `remote_gstreamer_output.json`
    This config file must be used in order for the streaming to work properly. It contains two windows, one for the host to use as normal, and one to be streamed (basically one with and one without the GUI rendered on top).

## GStreamer
The CMake tag for GStreamer is in: `apps/OpenSpace/ext/sgct/CMakeLists.txt`

The linking of GStreamer libraries and copying of dll's to the .exe folder is done in: `apps/OpenSpace/CMakeLists.txt`

The GStreamer folder with all its code and files is in: `apps/OpenSpace/ext/sgct/ext/gstreamer`

Errors regarding GStreamer do not always show up in the general CMD-window running OpenSpace. Run the OpenSpace.exe with` –gst-debug-level=3` (You can go to level 5 but that is like a scene from The Matrix, dodge this) to get better debug messages. (i.e `.\OpenSpace.exe –gst-debug-level=3`)

When adding/removing plugin dll's to GStreamer, they often have dependent dll's that have to be dealt with as well. We used the `dumpbin /dependents plugin.dll` command using Developer Command Prompt for VS to list these.

### GStreamer Pipeline
The proposed GStreamer pipeline looks like this, and can be found in `gstreamerWebRTC.h`. The documentation for each element is linked to the GStreamer web page below:

  - [appsrc](https://gstreamer.freedesktop.org/documentation/app/appsrc.html)
    ```
    stream-type=0 do-timestamp=1
    format=GST_FORMAT_TIME is-live=1 name=source
    caps=\"video/x-raw(memory:GLMemory), width=", pWidth, ",height=", pHeight, framerate=50/1, format=(string)RGBA, texture-target=(string)2D
    ```
  - [glvideoflip](https://gstreamer.freedesktop.org/documentation/opengl/glvideoflip.html?gi-language=c#glvideoflip-page)
    ```
    method=vertical-flip
    ```
  - [glcolorconvert](https://gstreamer.freedesktop.org/documentation/opengl/glcolorconvert.html?gi-language=c#glcolorconvert-page)
  - [gldownload](https://gstreamer.freedesktop.org/documentation/opengl/gldownload.html#gldownload-page)
  - [nvh264enc](https://gstreamer.freedesktop.org/documentation/nvcodec/nvh264enc.html?gi-language=c#nvh264enc-page)
    ```
    gop-size=-1 qp-const=5 preset=low-latency-hq rc-mode=cbr bitrate=6000
    ```
  - [rtph264pay](https://gstreamer.freedesktop.org/documentation/rtp/rtph264pay.html?gi-language=c#rtph264pay-page)
    ```
    application/x-rtp, framerate=50/1, profile=main, media=video, encoding-name=H264, payload=96
    ```
  - [webrtcbin](https://gstreamer.freedesktop.org/documentation/webrtc/index.html#webrtcbin-page)
    ```
    name=sendrecv
    ```

Instead of the Nvidia h264 encoder (nvh264enc), the default h264 encoder ([x264enc](https://gstreamer.freedesktop.org/documentation/x264/index.html#x264enc-page)) can be used.



