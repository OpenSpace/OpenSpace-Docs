# Download, Install, and Run
This section will cover downloading OpenSpace from our website and running it on your computer.

## OpenSpace for Windows
This video covers downloading OpenSpace from our [website](https://www.openspaceproject.com/), extracting the application from the zip file, and running the application for the first time.
<iframe width="740" height="530" id="tutorialPlayer" src="https://www.youtube.com/embed/YHl5L85hEUQ?enablejsapi=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Download the zip file from the OpenSpace website. |
| 0:30 | Get the zip file from your downloads and extract the OpenSpace folder. |
| 0:50 | Find the .exe inside the extracted folder and create a desktop shortcut. |
| 1:04 | Running the application for the first time, you will get a Windows protection pop-up. Click "More info" then "Run Anyway." |
| 1:13 | When the Launcher opens, start OpenSpace with the start button. |
| 1:15 | You will be presented with more Windows protection pop-us, this time for the firewall. Click "Allow access" on each. |
| 1:35 | OpenSpace is started and you can use the application. |

## Windows installation "VCRUNTIME140_1.dll" error
When you run OpenSpace for the first time, if you experience the error "VCRUNTIME140_1.dll was not found" you must first install the Microsoft Visual C++ Redistributable for Visual Studio 2019. This can be downloaded from Microsoft here: [https://aka.ms/vs/16/release/vc_redist.x64.exe](https://aka.ms/vs/16/release/vc_redist.x64.exe)

## Windows frame rate issue
If your frame rate is low (the FPS number in the top left corner), please ensure that OpenSpace is using your NVIDIA graphics card. This can be adjusted in settings under the graphics.

## OpenSpace for MacOS

This video covers downloading OpenSpace from our website, running the installer package, and launching OpenSpace for the first time.
<iframe width="740" height="530" src="https://www.youtube.com/embed/uSceew-98Cg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

| Video time | Description |
|:-------------|:------------------|
| 0:00 | Download the pkg file from the OpenSpace website. |
| 1:45 | Run the pkg file to install OpenSpace. |
| 2:33 | If a MacOS installation "unidentified developer" error pops up, go to System Preferences, Security & Privacy and click "Open Anyways." Another pop up will say the software cannot be verified. Click "Open." |
| 3:28 | Run the installer and close when it is complete. You can delete the pkg file when prompted. |
| 4:53 | Select the installed OpenSpace folder and File > Get Info. In the info window, apply Read & Write privileges to the  OpenSpace folder. |
| 5:23 | Run the OpenSpace application, found in the bin folder. When the Launcher opens, start OpenSpace with the start button. |
| 6:25 | Open OpenSpace in low resolution mode by selecting the application and going to File > Get Info. Check the box that says "Open in Low Resolution" and then run the application. |

## MacOS Folder Permissions
As shown in the video, most users will need to adjust the folder permissions on the installed OpenSpace folder, and "Apply to Enclosed Items" as outlined here by Apple: [https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)

## MacOS Installation "unidentified developer" error
If you try to launch OpenSpace and you get an error that the application is not registered with Apple by an identified developer, you can follow these steps from Apple to run OpenSpace anyway: [https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)

## Open in Low Resolution Mode
For users running on a Retina display, you may want to apply the "Open in Low Resolution Mode" setting on the OpenSpace.app to get better performance.
