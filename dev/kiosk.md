# Kiosk

## How to Build
There are two repositories that need to be at their kiosk-specific branches:
 - OpenSpace (https://github.com/OpenSpace/OpenSpace) in the **feature/gui-for-touch** branch.
 - Web GUI Front-End (https://github.com/OpenSpace/OpenSpace-WebGuiFrontend) in the **storyTouch** branch.  The software tools listed [here](compiling/windows) must be installed.  In addition, a [node.js](https://nodejs.org/en/download/) install is required.

### OpenSpace repository build instructions:
1. Clone the repository using the github URL listed above.
2. Select **feature/gui-for-touch** branch.
3. Open project in CMake
   a. Ensure that the following variables are enabled:
          - **OPENSPACE_MODULE_CEFWEBGUI**
            - **OPENSPACE_MODULE_WEBBROWSER**
            - **OPENSPACE_MODULES_WEBGUI**
            - **OPENSPACE_BEHAVIOR_KIOSK**
   b. Configure and Generate the project.
4. Open project in Visual Studio
   a. Set to **Release** or **RelWithDebInfo**.
   b. Build the project.

### Web GUI Front-End repository build instructions:
1. Clone the repository using the github URL listed above.
2. Select **storyTouch** branch.
3. Open a Windows console (cmd.exe) and cd to this repository location.
4. Type `npm install`, and handle any npm warnings or errors that may occur (for example if there are problems with the system's npm install).

## How to Run
1. Set OpenSpace to web gui development mode by editing the file **data/assets/customization/gui.asset** and set the variable `webguiDevelopmentMode` to `true`.
2. If not already open, from the Web GUI build step above, open a Windows console (`cmd.exe`) and cd to the location where the Web GUI repository above was cloned.
3. Type `npm start`, and the console output should finish with "compiled successfully."
4. Run the batch script file (contents in Appendix A) for starting OpenSpace in touch mode.  This script will first start OpenSpace, and then start the TUIO server which interprets the touch gesture.  *Note: as of June 2019, there is a **feature/touch-server-integrated** branch in which OpenSpace automatically starts the TUIO touch server.  When this branch is merged into master, this step will no longer be necessary.*

## Appendix A: How to Start OpenSpace in Touch Interface Mode
Touch screen gestures are interpreted by an instance  a separate software application.  Currently, a script is necessary to start OpenSpace and the TUIO touch server is a synchronized manner.
The simplest form of this script is shown below:
```
START C:\OpenSpace\bin\Release\OpenSpace.exe
ping -n 5 127.0.0.1 >nul
START C:\path\to\touchServer_x64.exe
```
Here, the `ping` command is used to create a simple 5 second delay before starting the TUIO touch server.  This method works most of the time, but is not foolproof; sometimes the touch server fails to properly install its windows hooks into the OpenSpace executable, and a restart is required.  Optional commands can be added to the end of the file in order to bring the Windows focus on the OpenSpace window rather than the touch server console.  It is also necessary to manually stop the touch server after OpenSpace exits.  Otherwise there may be two instances of the touch server running if the startup script runs again, and this causes unexpected touch interaction behavior.
