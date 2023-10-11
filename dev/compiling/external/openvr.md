# OpenVR

## Building
You can now use OpenVR as projection source and for viewing an OpenSpace scene in an HMD, specially an Oculus Rift or an HTC Vive.  Only HMD tracking and rendering is currently considered, no controller.  You can compile with this functionality enabled, but they will be no setup/overhead if a window hasn't specified OpenVR in the currently utilized SGCT config file.

To build OpenSpace with OpenVR support enabled you need to check the box in CMake to select OPENSPACE_OPENVR_SUPPORT 

Then set path values for the following, also in CMake:
 - `OPENVR_INCLUDE_DIRS`
 - `SGCT_OPENVR_INCLUDE_DIRECTORY`
 - `OPENVR_LIBRARY`
 - `SGCT_OPENVR_DEFINITIONS`

OpenVR should be built first.  You can check out the [source](https://github.com/ValveSoftware/openvr), and then set `OPENVR_ROOT_DIR` to point to the directory.

You will also need to obtain the dynamic library and place it in the OpenSpace bin/ dir, along side the OpenSpace.exe file. You can obtain that dll from here: https://github.com/ValveSoftware/openvr/tree/master/bin (picking the correct system you are on, most likely win64).

## Running
Before running OpenSpace, set the SGCT configuration to use either of the following config files:
* openvr_htcVive.xml
* openvr_oculusRiftCv1.xml

This can be done by setting `SGCTConfig = "${SGCT}/openvr_*.xml"` in the `openspace.cfg` file, or at the command line with `-s /path/to/openvr_*.xml`.

The HMD unit must be started and running before starting OpenSpace.
